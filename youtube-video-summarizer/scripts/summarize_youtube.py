#!/usr/bin/env python3
"""
summarize_youtube.py — Summarize or exhaustively extract a YouTube video via the
Google Gemini API.

Two modes:
  succinct   (default) — "I don't want to watch this 10-minute video, just tell me
                          the thing it promises to reveal." Uses LOW media resolution
                          (cheaper/faster) and a prompt tuned to cut filler and lead
                          with the payoff. Prints to stdout.
  exhaustive           — "Pull every piece of information for my knowledge base."
                          Uses HIGH media resolution and a total-recall prompt with
                          timestamps and headings. Prints AND writes a .md file.

Auth: the Gemini client reads the GEMINI_API_KEY environment variable automatically.
      Do NOT hardcode the key here. Set it in your shell:  export GEMINI_API_KEY=...
Model: defaults to gemini-3.5-flash; override with the GEMINI_MODEL env var or --model.
"""

import argparse
import os
import re
import sys
from datetime import datetime

DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")

# --- The two "brains" of the skill. Tune these to taste. --------------------

SUCCINCT_PROMPT = """You are watching this video on behalf of someone who does NOT want to watch it.

Videos like this often stretch a small amount of real information across many minutes \
using intros, recaps, self-promotion, story build-up, and filler. Your job is to \
extract ONLY the actual payoff — the specific information, answer, method, or claim \
the video promises to deliver — and state it as directly as possible.

Rules:
- Lead with the answer. If the title or thumbnail poses a question or promises a \
reveal, answer it in the very first sentence.
- Be concise: a few sentences to a short paragraph. No "This video is about..." preamble.
- Skip intros, sponsor reads, subscribe requests, recaps, and motivational filler.
- If the key information is buried behind a long build-up, just give the information.
- Include only the concrete specifics (numbers, names, steps) that matter to the payoff.
- If the video never actually delivers on its promise (pure clickbait), say so plainly \
and state whatever partial information it did give."""

EXHAUSTIVE_PROMPT = """Extract the COMPLETE information content of this video for a \
knowledge base. This is not a summary — the goal is total recall of substantive content. \
Assume no real point is too minor to capture.

Capture, at minimum:
- Every distinct claim, fact, statistic, definition, and assertion.
- Every concept, principle, mental model, or framework introduced, with its explanation.
- Every step of any process, method, or procedure described.
- Every concrete example, case study, or anecdote, and what it is meant to illustrate.
- Named people, tools, products, companies, papers, and resources mentioned.
- Notable direct quotes worth preserving verbatim.
- Any open questions, caveats, disagreements, or stated limitations.

Requirements:
- Preserve specificity: keep exact numbers, names, and wording wherever they carry meaning.
- Attach an approximate timestamp (MM:SS) to each major point so it can be traced back.
- Organize under clear thematic headings that follow the video's own structure.
- Do NOT compress or editorialize. If the video spends five minutes on one idea with \
three sub-points, capture all three sub-points.
- Ignore only true non-content: sponsor reads, subscribe requests, and pure filler.
- Output clean Markdown suitable for downstream chunking and note extraction."""

# ---------------------------------------------------------------------------

_YT_ID_PATTERNS = [
    r"(?:v=|/watch\?.*v=)([0-9A-Za-z_-]{11})",
    r"youtu\.be/([0-9A-Za-z_-]{11})",
    r"/shorts/([0-9A-Za-z_-]{11})",
    r"/embed/([0-9A-Za-z_-]{11})",
    r"/live/([0-9A-Za-z_-]{11})",
]


def extract_video_id(url: str) -> str:
    for pat in _YT_ID_PATTERNS:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return "video"


def build_config(types, mode: str, media_resolution: str | None):
    """Return a GenerateContentConfig with the right media resolution for the mode."""
    res_map = {
        "low": types.MediaResolution.MEDIA_RESOLUTION_LOW,
        "medium": types.MediaResolution.MEDIA_RESOLUTION_MEDIUM,
        "high": types.MediaResolution.MEDIA_RESOLUTION_HIGH,
    }
    if media_resolution:
        res = res_map[media_resolution]
    else:
        res = res_map["low"] if mode == "succinct" else res_map["high"]
    return types.GenerateContentConfig(media_resolution=res)


def build_video_part(types, url: str, fps, start, end):
    vm_kwargs = {}
    if fps is not None:
        vm_kwargs["fps"] = fps
    if start:
        vm_kwargs["start_offset"] = start
    if end:
        vm_kwargs["end_offset"] = end
    video_metadata = types.VideoMetadata(**vm_kwargs) if vm_kwargs else None
    return types.Part(
        file_data=types.FileData(file_uri=url),
        video_metadata=video_metadata,
    )


def main():
    ap = argparse.ArgumentParser(description="Summarize/extract a YouTube video via Gemini.")
    ap.add_argument("url", help="Public YouTube video URL")
    ap.add_argument("--mode", choices=["succinct", "exhaustive"], default="succinct",
                    help="succinct = just the payoff (default); exhaustive = full extraction")
    ap.add_argument("--focus", default=None,
                    help="(succinct) The specific thing you want to know from the video")
    ap.add_argument("--out", default=None,
                    help="(exhaustive) Output .md path. Default: ./<videoid>-notes.md")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Model (default: {DEFAULT_MODEL})")
    ap.add_argument("--media-resolution", choices=["low", "medium", "high"], default=None,
                    help="Override the per-mode media resolution")
    ap.add_argument("--fps", type=float, default=None, help="Frame sampling rate (default: 1)")
    ap.add_argument("--start", default=None, help="Clip start, e.g. 00:30 or 90s")
    ap.add_argument("--end", default=None, help="Clip end, e.g. 05:00 or 300s")
    args = ap.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("ERROR: GEMINI_API_KEY is not set. Run:  export GEMINI_API_KEY=your_key")

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("ERROR: google-genai is not installed. Run:  pip install google-genai")

    prompt = SUCCINCT_PROMPT if args.mode == "succinct" else EXHAUSTIVE_PROMPT
    if args.mode == "succinct" and args.focus:
        prompt += f"\n\nThe viewer specifically wants to know: {args.focus}\nPrioritize that above everything else."
    if args.mode == "exhaustive":
        prompt += f"\n\nBegin the output with a line:  Source: {args.url}"

    client = genai.Client()  # reads GEMINI_API_KEY from the environment
    config = build_config(types, args.mode, args.media_resolution)
    video_part = build_video_part(types, args.url, args.fps, args.start, args.end)
    contents = types.Content(parts=[video_part, types.Part(text=prompt)])

    try:
        response = client.models.generate_content(
            model=args.model, contents=contents, config=config,
        )
    except Exception as e:
        sys.exit(f"ERROR calling Gemini: {e}")

    text = getattr(response, "text", None)
    if not text:
        # Surface why nothing came back (blocked, empty, etc.)
        reason = ""
        try:
            reason = str(response.candidates[0].finish_reason)
        except Exception:
            pass
        sys.exit(f"ERROR: model returned no text. finish_reason={reason or 'unknown'}")

    if args.mode == "exhaustive":
        out_path = args.out or f"{extract_video_id(args.url)}-notes.md"
        header = f"<!-- Extracted {datetime.now():%Y-%m-%d %H:%M} via {args.model} -->\n\n"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(header + text.strip() + "\n")
        print(text.strip())
        print(f"\n---\nSaved to: {out_path}", file=sys.stderr)
    else:
        print(text.strip())


if __name__ == "__main__":
    main()

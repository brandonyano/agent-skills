---
name: youtube-video-summarizer
description: >-
  Summarize or exhaustively extract the content of a YouTube video using the Google
  Gemini API, given only the video URL. Use this skill whenever the user pastes or
  mentions a YouTube link. Trigger even if the user doesn't say the word 
  "summarize": any YouTube URL plus an intent to get information out of it should 
  route here rather than trying to answer from the title or from memory.
---

# YouTube Video Summarizer (via Gemini)

Turns a YouTube URL into either a **quick payoff** (default) or an **exhaustive
extraction** for a knowledge base. Gemini ingests public YouTube URLs directly — no
downloading — and the two modes are controlled by two levers: the **prompt** and the
**`media_resolution`** setting (low ≈ 100 tokens/sec of video, high ≈ 300 tokens/sec).

## Prerequisites (check these first, once)

1. **API key** — the script reads `GEMINI_API_KEY` from the environment. If it isn't
   set, tell the user to run `export GEMINI_API_KEY=your_key` (or add it to their shell
   profile). Never put the key in the script or in chat.
2. **Library** — needs `google-genai`. If import fails, run
   `pip install google-genai --break-system-packages`.
3. **Model** — defaults to `gemini-3.5-flash`; override with the `GEMINI_MODEL` env var
   or `--model`.

## When to Use

Trigger on any YouTube video link, including:

- `https://www.youtube.com/watch?v=...`
- `https://youtu.be/...`
- `https://youtube.com/shorts/...`
- `https://www.youtube.com/live/...`
- `https://www.youtube.com/embed/...`

Default behavior when the user sends only a YouTube link: summarize it without asking a follow-up question.

## Choosing the mode

**Default to succinct.** Only switch to exhaustive when the user signals they want the
full contents — phrases like "extract everything", "for my knowledge base", "full
notes", "every point", "exhaustive", or "don't leave anything out". When in doubt, run
succinct; it's fast and cheap, and the user can ask for the full extraction after.

If the user names the specific thing they're after ("does it say which setting to
change?"), pass it via `--focus` so succinct mode answers that first.

## Usage

Succinct (the common case):
```bash
python scripts/summarize_youtube.py "<url>"
python scripts/summarize_youtube.py "<url>" --focus "the actual fix they recommend"
```

Exhaustive (knowledge-base extraction — saves a .md AND prints):
```bash
python scripts/summarize_youtube.py "<url>" --mode exhaustive
python scripts/summarize_youtube.py "<url>" --mode exhaustive --out notes/topic.md
```

Optional knobs: `--media-resolution {low,medium,high}` to override the per-mode default,
`--fps N` for denser/sparser frame sampling, and `--start MM:SS` / `--end MM:SS` to clip
to a section of the video.

## What each mode does

| | Succinct (default) | Exhaustive |
|---|---|---|
| media resolution | low | high |
| prompt | cut filler, lead with the payoff, answer the promise in sentence one | total recall: every claim, number, step, example, quote, with MM:SS timestamps |
| output | short answer, inline | clean Markdown, saved to `<videoid>-notes.md` **and** printed |

## After exhaustive extraction

The saved `.md` is structured for downstream processing. If the user is building a
knowledge base, offer to hand it to their pipeline: `source-chunker` →
`knowledge-extractor` → `concept-deduper`. Don't run those automatically — just offer.

## Edge cases & limits

- **Public videos only.** Private/unlisted videos won't work; say so if the API rejects it.
- **Clickbait:** succinct mode is told to state plainly when a video never delivers on its
  promise — surface that verdict, it's often the most useful answer.
- **Limits:** up to 10 videos per request on 2.5+ models; the free tier caps at ~8 hours
  of video per day (no cap on paid). Very long videos cost more tokens — mention this if
  someone runs exhaustive mode on a multi-hour video.
- **No text back:** if the script reports an empty response with a `finish_reason`, relay
  it — it usually means the content was blocked or the URL wasn't accessible.

## Fallback Workflow: Transcript Then Gemini/Text Summary

If Gemini returns an access error for the YouTube URL:

1. Load/use the `youtube-content` skill.
2. Fetch transcript with timestamps:
   ```bash
   python3 <youtube-content-skill-dir>/scripts/fetch_transcript.py "URL" --timestamps
   ```
3. If the transcript is available, summarize it. Prefer Gemini for summarizing the transcript if credentials work; otherwise summarize with the current model and disclose that Gemini URL ingestion failed.
4. If transcripts are disabled or unavailable, tell the user the video cannot be summarized from available sources.

## Error Handling

- Missing Gemini key: say that Gemini credentials are not available, then use `youtube-content` transcript fallback if possible.
- Gemini 400/403/404: the URL may be private, unavailable, restricted, unsupported, or too long for direct video ingestion. For `token count exceeds`, first retry direct video ingestion with lower frame sampling (`video_metadata.fps`, helper default `0.2`) because Gemini's docs recommend low FPS for long mostly-static videos; if that still fails, use clipping (`start_offset`/`end_offset`), transcript fallback, or metadata fallback as documented in `references/long-video-token-limit-and-fallbacks.md`.
- Gemini quota/rate limit: tell the user Gemini hit a quota/rate-limit issue and offer transcript fallback.
- No transcript fallback: ask the user for a transcript or accessible video file.
- Long videos: Gemini should handle the video URL directly; if transcript fallback is needed, chunk transcripts over roughly 40,000 characters and merge summaries.

## Common Pitfalls

1. Do not summarize from the YouTube title alone. Use Gemini URL ingestion or a transcript.
2. Do not claim to have watched the video unless Gemini or transcript extraction succeeded.
3. Do not invent timestamps or quotes.
4. Do not ask for confirmation when the message is simply a YouTube link; the default action is to summarize.
5. Do not use transcript extraction as the primary path unless Gemini credentials or access fail.
6. If a text-only Gemini URL fallback returns a summary that conflicts with the browser-visible title/description, treat it as ungrounded; summarize browser-visible metadata/chapters instead and disclose that limitation.

## Verification Checklist

- [ ] Detected a valid YouTube URL.
- [ ] Tried Gemini first using the URL itself.
- [ ] Returned the actual summary text to the user.
- [ ] Used transcript fallback only if Gemini could not access/summarize the URL.
- [ ] Clearly disclosed any blocker, quota issue, or fallback.
# Agent Skills

This repository contains a collection of AI agent skills I use to extend Cursor and other agent workflows. Each skill lives in its own directory with a `SKILL.md` file and, when useful, supporting scripts or reference material.

## Skills

- `deduplicator` - removes repeated information across one or more inputs while preserving every unique detail.
- `knowledge-extractor` - extracts reusable, standalone knowledge from source material.
- `source-chunker` - splits long-form source material into coherent chunks for downstream extraction or RAG.
- `youtube-video-summarizer` - summarizes or exhaustively extracts public YouTube videos through the Google Gemini API.
- `prose-coach` - critiques, revises, and drafts nonfiction prose using a curated writing-principles reference.
- `facebook-ads-strategist` - analyzes and plans Meta/Facebook ad account strategy using a bundled knowledge base.
- `landing-page-expert.skill` - packaged skill for landing page critique, strategy, and conversion-focused recommendations.

## Repository Layout

```text
.
├── deduplicator/
├── facebook-ads-strategist/
├── knowledge-extractor/
├── landing-page-expert.skill
├── prose-coach/
├── source-chunker/
└── youtube-video-summarizer/
```

## Public Repo Notes

This repo is intended to be safe to publish publicly.

- Do not commit API keys, tokens, credentials, customer data, private transcripts, or generated working notes.
- Runtime secrets should come from environment variables. For example, `youtube-video-summarizer` expects `GEMINI_API_KEY` to be set locally.
- Generated extraction outputs such as `extractions/`, `concepts/`, `chunks/`, and `*-notes.md` are ignored by Git by default.
- Local environment files such as `.env`, virtual environments, editor settings, logs, and OS metadata are ignored by Git.

## YouTube Summarizer Setup

The YouTube helper script requires Python and the Google GenAI client:

```sh
pip install google-genai
export GEMINI_API_KEY=your_key
python youtube-video-summarizer/scripts/summarize_youtube.py "https://www.youtube.com/watch?v=..."
```

Keep the actual key in your shell environment or a local ignored `.env` file, never in tracked files.

## GitHub Publishing

When ready to publish:

```sh
git remote add origin git@github.com:<your-username>/<repo-name>.git
git push -u origin main
```

# Agent Skills

This repository contains a collection of AI agent skills that I've created and use. Each skill lives in its own directory with a `SKILL.md` file and, when useful, supporting scripts or reference material.

## Skills

- `deduplicator` - removes repeated information across one or more inputs while preserving every unique detail.
- `copywriter` - writes, rewrites, critiques, and improves persuasive copy using a bundled copywriting reference.
- `knowledge-extractor` - extracts reusable, standalone knowledge from source material.
- `source-chunker` - splits long-form source material into coherent chunks for downstream extraction or RAG.
- `youtube-video-summarizer` - summarizes or exhaustively extracts public YouTube videos through the Google Gemini API.
- `prose-coach` - critiques, revises, and drafts nonfiction prose using a curated writing-principles reference.
- `facebook-ads-strategist` - analyzes and plans Meta/Facebook ad account strategy using a bundled knowledge base.
- `landing-page-expert` - audits, critiques, builds, and improves landing pages using conversion-focused references and an HTML skeleton asset.

## Repository Layout

```text
.
├── copywriter/
├── deduplicator/
├── facebook-ads-strategist/
├── knowledge-extractor/
├── landing-page-expert/
├── prose-coach/
├── source-chunker/
└── youtube-video-summarizer/
```

## YouTube Summarizer Setup

The YouTube helper script requires Python and the Google GenAI client:

```sh
pip install google-genai
export GEMINI_API_KEY=your_key
python youtube-video-summarizer/scripts/summarize_youtube.py "https://www.youtube.com/watch?v=..."
```

Keep the actual key in your shell environment or a local ignored `.env` file, never in tracked files.

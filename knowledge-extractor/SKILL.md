---
name: knowledge-extractor
description: "Extracts reusable, standalone knowledge from any source material, on any topic. Pulls out core ideas, concepts, claims, principles, mental models, procedures, examples, memorable quotes, and open questions as atomic notes for a knowledge base. Use this skill whenever the user wants to extract knowledge from a piece of content, process a video/transcript/article/chapter/paper for a knowledge base, turn reading or meeting notes into structured insights, run extraction on a file, or build atomic notes from source material. Trigger for phrases like 'extract knowledge from this', 'pull out the key ideas', 'process this for my knowledge base', 'turn this into notes', 'extract this transcript/article/paper', 'run extraction on', or any request to convert raw content into structured, reusable notes. Always use this skill rather than doing ad-hoc extraction inline."
allowed-tools: Read, Write, Edit
---

# Knowledge Extractor

You extract reusable, standalone knowledge from source material of any kind on any topic.

Your output should read like a high-quality personal knowledge base — not a summary, not a recap, not a report. Every item you extract should be useful on its own, without needing to re-read the source.

The source's format and subject don't change the job. Whether it's a philosophy book, a marketing webinar transcript, a systems-design article, or a podcast on beekeeping, you are pulling out the durable, reusable ideas and rendering them as atomic notes.

---

## Input

The user will point you at content to extract from. It can arrive in several forms — identify which one you're dealing with and read accordingly:

| Input form | How to handle it |
|---|---|
| **A file** (`.md`, `.txt`, `.vtt`, `.srt`, `.json`, `.pdf`, etc.) | Read the file. For transcript formats (`.vtt`/`.srt`), strip timing markup but keep timestamps available for attribution. |
| **A directory** | Process every content file in order. One extraction file per source. |
| **Pasted text** | Extract directly from what the user provided in the message. |
| **A URL the user references** | If a fetch tool is available and the user wants it fetched, retrieve the text first; otherwise ask them to paste it. |

**Gather what metadata you can.** Different sources carry different metadata, and most of it is optional. Do your best to capture:

- `source` — the title (book title, article headline, video title, paper title). If unknown, ask the user or use a short descriptive label.
- `source_type` — one of: `book`, `article`, `transcript`, `paper`, `documentation`, `notes`, `other`.
- `author` / `speaker` — if identifiable.
- A locator for attribution — see **Attribution & location** below.

If a piece of metadata isn't available, omit that frontmatter field rather than inventing it.

### Handling long inputs

If the input is short-to-moderate (a single article, one transcript, a chapter), produce **one extraction file** for it.

If the input is very long (a whole book, a multi-hour transcript), don't try to extract it all in one pass — that produces shallow notes. Segment it along natural boundaries (chapters, headings, topic shifts, transcript timestamps) and produce one extraction file per segment.

---

## Attribution & location

Every extracted item must be traceable back to where it came from. The locator adapts to the source type — use whatever the source provides:

| Source type | Use as locator |
|---|---|
| Book | Chapter and/or section; page if available |
| Article / blog | Section heading or paragraph anchor; URL if known |
| Transcript (video/podcast) | Timestamp or timestamp range (e.g., `12:30–14:05`) |
| Paper | Section number/name (e.g., `§3 Methods`) or page |
| Documentation | Page title and heading |
| Notes / pasted text | A short descriptive locator, or omit if there's no meaningful subdivision |

Throughout the output, the per-item **Source / location** field carries this locator so any note can be traced without re-reading the whole source.

---

## Output format

Write one extraction file per source (or per segment), saved alongside the source or in an `extractions/` subdirectory.

**Filename**: `extraction_{slug}.md`, where `{slug}` is a short kebab-case identifier derived from the source title (e.g., `extraction_atomic-habits-ch2.md`, `extraction_meta-ads-webinar.md`). For multi-segment sources, append a segment marker: `extraction_{slug}_{NN}.md`.

```markdown
---
source: "{title of the source}"
source_type: "{book | article | transcript | paper | documentation | notes | other}"
author: "{author or speaker, if known}"
location: "{locator — chapter/section, timestamp range, URL, page, etc.}"
extracted: "{today's date}"
---

# Extraction: {short source label}

## Core Ideas
- {Atomic, reusable idea — in your own words}
- {Another atomic idea}

## Concepts
### {Concept Name}
- **Definition**: {Clear, self-contained definition}
- **Why it matters**: {Practical significance}
- **Related concepts**: {List any mentioned or implied}
- **Source / location**: {locator}

## Claims
### {Short label for the claim}
- **Claim**: {The assertion the author/speaker makes}
- **Evidence / reasoning**: {What they offer to support it}
- **Confidence**: high / medium / low
- **Caveats**: {Conditions under which this may not hold}
- **Source / location**: {locator}

## Principles / Rules
### {Principle name or short label}
- **Principle**: {The rule or heuristic, stated clearly}
- **When it applies**: {Context or conditions}
- **When it may not apply**: {Exceptions or edge cases}
- **Example from source**: {Concrete illustration, if given}

## Procedures / Frameworks
### {Name of the process or framework}
- **Steps**: {Numbered list}
- **Inputs**: {What you need to begin}
- **Outputs**: {What you produce}
- **Failure modes**: {What goes wrong and why}

## Examples
### {Short label}
- **Example**: {What the author/speaker describes}
- **What it illustrates**: {The concept or claim it supports}
- **Reusable lesson**: {What you'd take away and apply elsewhere}

## Memorable Quotes
- "{Exact quote}" — {attribution / locator}

## Questions Raised
**Answered by this source:**
- {Question this content resolves}

**Left open:**
- {Question this content raises but doesn't resolve}
```

---

## Section rules

### Core Ideas
- 3–7 bullets per source (or per segment).
- Each idea must be atomic — one concept per bullet.
- Write in your own words. Do not copy sentences from the source.
- Think: "Could this bullet stand alone as a flashcard or note?"

### Concepts
- Only extract concepts that are **explicitly defined or explained** in the content.
- Do not extract concepts that are merely mentioned in passing.
- If the content has no definitions, omit this section.

### Claims
- A claim is an assertion the author or speaker makes that could be true or false.
- Distinguish claims from definitions (definitions go in Concepts).
- Confidence rating reflects how well the source supports the claim **within this content** — not your personal assessment of its truth.

### Principles / Rules
- A principle is a generalized rule or heuristic (not a one-time claim).
- Include "When it may not apply" even if the source doesn't — reason from context.
- If the content has no principles, omit this section.

### Procedures / Frameworks
- Only include if the content describes a **repeatable process** with identifiable steps.
- Steps should be numbered and actionable.
- If the content has no procedures, omit this section.

### Examples
- An example is a concrete illustration used to support an idea.
- Capture the lesson separately from the example itself — the lesson is what makes it reusable.
- If the content has no examples, omit this section.

### Memorable Quotes
- Only include quotes that are **genuinely striking** — a well-turned phrase, a memorable formulation, or a line that captures an idea better than a paraphrase would.
- Keep quotes short (under 25 words).
- Do not pad this section. Zero quotes is fine.
- For transcripts, clean up obvious filler ("um", "you know") only if it doesn't alter meaning, and attach the timestamp.

### Questions Raised
- Always include at least one item in each sub-section.
- "Answered" questions should reflect what someone might have wondered before reading/watching this.
- "Left open" questions are the most valuable — they drive further reading and research.

---

## Hard rules

1. **Do not summarize** — extraction is not a recap. Every item must be independently useful.
2. **Do not invent** — only extract what is present in the content. If something is implied but not stated, flag it as an inference in parentheses: *(inference)*.
3. **Preserve attribution** — every item carries its **Source / location** reference.
4. **Omit empty sections** — if the content has no examples, don't write an empty `## Examples` section.
5. **Prefer atomic notes** — a source that yields 10 small, sharp notes is better than one yielding 2 sprawling ones.
6. **Stay format- and topic-agnostic** — a transcript on gardening gets the same rigorous treatment as a textbook chapter on statistics. Adapt the locator and tone to the source; keep the structure constant.

---

## Workflow

1. **Identify** the input form (file, directory, transcript, pasted text) and gather available metadata.
2. **Read** the content.
3. **Scan** it once for overall structure before extracting.
4. **Extract** section by section, in order.
5. **Write** the extraction file(s).
6. **Report** to the user: source processed, extraction saved to `{path}`, sections populated, anything notable (e.g., unusually dense source, no examples found, very long input that was segmented).

If processing multiple sources or segments, report a summary at the end: total sources processed, total concepts / claims / principles extracted.

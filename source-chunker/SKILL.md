---
name: source-chunker
description: "Cleans and splits any long-form source material into semantically coherent chunks for downstream knowledge extraction or RAG ingestion. Handles books, transcripts, interviews, articles, research papers, reports, documentation, meeting notes, and chat/Q&A logs. Use this skill whenever the user wants to split or chunk a document, prepare text for a knowledge base, process chapters/sections/segments into separate files, chunk content for RAG pipelines, or break long-form material into structured pieces. Trigger if they say things like 'break this into sections', 'prepare this for my knowledge base', 'split this up', 'chunk this text', 'process this transcript', or 'process these chapters'. Always use this skill rather than doing ad-hoc splitting inline."
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
---

# Source Chunker

You prepare long-form source material of any kind for downstream knowledge extraction or RAG ingestion. The source might be a book, transcript, interview, podcast, article, essay, research paper, report, technical documentation, manual, meeting notes, or a chat/forum/Q&A log — supplied as a single file or as many.

## Your job

1. **Read** the source — a single file or multiple files.
2. **Identify the source type and its structure** — different material has different natural seams.
3. **Choose a boundary strategy** that fits that structure.
4. **Split** into coherent chunks — never cut mid-unit.
5. **Add frontmatter metadata** to every chunk.
6. **Save** each chunk as its own Markdown file, plus a manifest.

---

## Step 1: Identify the source type and structure

Before chunking, figure out what you're working with. Use `Grep` to sample heading and marker patterns before reading the whole file — this is cheap and tells you which strategy applies. Look for `#`-style headings, ALL-CAPS titles, numeric prefixes (`1.2`), timestamps (`\d{1,2}:\d{2}`), and speaker labels (`^[A-Z][\w .]+:`).

Match the material to its natural boundaries:

| Source type | Natural boundaries to look for |
|-------------|-------------------------------|
| Book / long manuscript | Chapter headings, part dividers, section headings |
| Article / essay / blog post | Headings, subheadings, clear topic shifts |
| Research paper | Labeled sections (Abstract, Introduction, Methods, Results, Discussion), numbered sections |
| Transcript / interview / podcast | Speaker turns, timestamps, topic segments, question→answer pairs |
| Meeting notes | Agenda items, headed sections, grouped bullet blocks |
| Chat / forum / Q&A log | Message or turn boundaries, thread breaks |
| Documentation / manual | Headings, numbered steps, command or example blocks |
| Unstructured text dump | No reliable structure — use the fixed-size fallback |

---

## Step 2: Boundary priority (general)

Apply the highest-priority boundary type the source actually supports:

1. **Explicit structural headings** — chapter/section/heading at any level
2. **Source-type units** — a speaker turn, a Q/A pair, an agenda item, a numbered step
3. **Topic shifts** — a blank line followed by a new subject that doesn't continue the prior thought
4. **Page or segment markers** — `\f`, `--- page ---`, or transcript timestamps
5. **Fixed-size fallback** — when none of the above exist, chunk at ~800 words, always aligned to a paragraph break

---

## Hard rules (apply to every source type)

- **Never split** inside a sentence, paragraph, example/code block, numbered list, definition, speaker turn, or question→answer pair.
- **Minimum chunk size**: ~300 words. If a unit is shorter, merge it forward into the next one.
- **Maximum chunk size**: ~1,500 words. If a unit exceeds this, find the nearest semantic break (end of example, end of paragraph, end of turn) below 1,500 words and split there.
- **Overlap**: None by default. If the user asks for overlapping chunks, add a configurable trailing paragraph from the prior chunk.

---

## Output format

Each chunk is saved as a `.md` file with YAML frontmatter:

```
---
source: "{title or filename}"
source_type: "{book | article | paper | transcript | notes | docs | chat | other}"
section: "{top-level unit — chapter, labeled section, segment — or 'N/A'}"
subsection: "{nested unit if available, else 'N/A'}"
chunk_id: "{zero-padded 4-digit id, e.g. 0001}"
location: "{flexible human-readable locator}"
status: "ready_for_extraction"
---
# Chunk {chunk_id}

{chunk text}
```

The `location` field adapts to the source — for example `Ch. 3, ~p. 45`, `Part 2 §4`, `00:12:30–00:18:05`, `Section: Methods`, or `Thread 'pricing', msgs 4–9`.

### File naming convention
```
chunk_0001.md
chunk_0002.md
...
```

Save all chunks into a subdirectory named after the source (slugified):
```
{source-title-slug}/
  chunk_0001.md
  chunk_0002.md
  ...
  manifest.md
```

---

## Manifest file

After chunking, write a `manifest.md` in the output directory:

```markdown
# Manifest: {Source Title}

- **Source type**: {book / transcript / paper / ...}
- **Total chunks**: {N}
- **Source file(s)**: {list}
- **Chunking strategy**: {e.g., "by chapter heading", "by speaker turn", "fixed-size fallback"}
- **Date processed**: {today}

## Chunk index

| chunk_id | section | subsection | location |
|----------|---------|------------|----------|
| 0001     | ...     | ...        | ...      |
| 0002     | ...     | ...        | ...      |
```

---

## Workflow

1. **Discover source files**: Use `Glob` to find input files if the user gives a directory. Ask if unclear.
2. **Detect type and structure**: Scan for heading, timestamp, and speaker patterns with `Grep` before reading the full file. This reveals whether the source uses `#`-style headings, ALL-CAPS titles, numeric prefixes, timestamps, speaker labels, or has no reliable structure at all.
3. **Plan the splits**: State the detected source type, the chosen boundary strategy, and the chunk plan before writing files. Briefly confirm with the user if the structure is ambiguous (e.g., no clear boundaries of any kind).
4. **Write chunks**: For each chunk, write the frontmatter + body to its file.
5. **Write manifest**: Summarize all chunks produced.
6. **Report**: Tell the user how many chunks were created, where they were saved, which strategy was used, and any edge cases (very short units merged, long units force-split, etc.).

---

## Edge cases

| Situation | Handling |
|-----------|----------|
| No structure of any kind found | Fall back to fixed-size chunking (~800 words) aligned to paragraph breaks; note in manifest |
| Unit < 300 words | Merge with the following unit; note in manifest |
| Unit > 1,500 words | Split at nearest semantic break under 1,500 words |
| Front/back matter (ToC, preface, references, appendix, index) | Include as `chunk_0000` / a trailing chunk, or skip — ask the user |
| Multiple input files (one per chapter/segment) | Treat each file as one top-level unit; chunk within it if needed |
| Source is PDF-extracted text | Run light cleaning first (see below) |
| Source is a raw transcript | Preserve speaker labels for attribution; segment by turn or topic, not by line |

---

## Cleaning (if source is raw/dirty)

Before chunking, apply light cleaning matched to where the text came from. Never alter the actual prose — no paraphrasing, no reordering.

**PDF-extracted text:**
- Remove lines matching `^\d+$` (standalone page numbers)
- Remove repeated running headers (lines that appear verbatim 3+ times)
- Re-join hyphenated line breaks (`word-\n` → `word`)
- Collapse 3+ consecutive blank lines to 2

**Transcripts:**
- Keep speaker labels and timestamps — they are attribution, not noise
- Optionally normalize timestamp formatting for consistency
- Remove obvious auto-caption artifacts (`[inaudible]` runs, duplicated stutters) only if the user asks

**Web/HTML-extracted text:**
- Strip navigation, "Share this", cookie/consent banners, and other boilerplate
- Remove inline ad markers and social-button text

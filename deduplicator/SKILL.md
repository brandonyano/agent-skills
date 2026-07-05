---
name: deduplicator
description: "Finds information that is repeated across one or more inputs and merges each repeated group into a single, complete occurrence — losslessly, editing in place by default. Use this skill whenever the user wants to remove redundancy, dedupe, deduplicate, consolidate repeated content, strip repetition, merge overlapping notes, or clean up material that says the same thing in multiple places. Trigger for phrases like 'deduplicate these', 'these files repeat the same stuff', 'remove the redundancy', 'consolidate without losing anything', 'merge the duplicates', 'clean up the repetition', 'my notes overlap a lot', or any request to unify repeated information from one file or a whole pile of them. It matches on meaning, not just identical text, so use it even when the duplicates are worded differently. Always use this skill rather than doing ad-hoc merging inline."
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Deduplicator

You take one or more inputs and remove information that is repeated — merging each repeated group into a single occurrence that keeps **every** unique detail. The point is to make each thing get said once without losing anything.

Two commitments shape everything below:

- **Semantic, not literal.** Two passages are duplicates when they carry the same underlying claim, fact, instruction, or idea — even if the wording, length, or examples differ. You are not grepping for identical strings; you are recognizing when someone has said the same thing twice.
- **Lossless.** When you collapse a duplicate group, the surviving occurrence must contain the union of all unique detail from every copy. Nothing informative is dropped. If copies disagree, both claims are unique detail — keep both.

This is deduplication, not rewriting. Touch what's redundant; leave everything else — including the author's voice, formatting, and structure — alone.

---

## The one judgment that matters most

Aggressive about *phrasing*, careful about *substance*.

Merge freely when the difference between two passages is only how they're said. Do **not** merge two passages just because they share a topic, vocabulary, or subject. "X is fast" and "X is memory-hungry" are two distinct facts about X, not a duplicate — they get preserved separately. Collapsing distinct claims into one blended entry quietly destroys information and falsely implies they were ever one point.

When you genuinely can't tell whether two things are the same claim or two related claims, keep them separate and note it in the report. A missed merge is a minor cosmetic flaw; a wrong merge loses or distorts information.

---

## Modes

**In place (default).** Overwrite each input with its deduplicated version, then write a short report of what changed. This is what "deduplicate these" means unless the user says otherwise.

**Copy (opt-in).** Leave the originals untouched and write deduplicated versions to new files (`<name>.deduped.<ext>`, or a `deduped/` directory for a set). Switch to this when the user says anything like "keep the originals," "give me a clean copy," "don't overwrite," or "output a deduplicated version."

Before overwriting originals, state plainly which files you're about to modify. The report (below) makes every change auditable; for irreplaceable inputs, it's reasonable to suggest the user keep a backup, but don't force it.

---

## Workflow

Work in four passes. Think of them as: understand the material, find the repeats, merge them losslessly, apply the edits.

### Pass 1 — Read and characterize
Read every input fully. Identify the **content shape**, because it determines the atomic unit you dedupe at:

| Shape | Atomic unit | Notes |
|-------|-------------|-------|
| Prose / documents / articles | A claim or point | Repetition shows up as the same point restated in different sections. |
| Note piles / atomic notes / cards | A single note | The classic case: two notes saying the same thing. |
| Lists / bullets / checklists | A list item | Merge items that mean the same; keep item ordering sensible. |
| Structured records (JSON array, CSV rows, config blocks) | A record | Two records describing the same entity → one record with the union of fields. |
| Transcripts / meeting notes / Q&A logs | A point made | The same point often recurs across a conversation. |

If an input mixes shapes, dedupe each region at its own natural unit. Preserve the file's format exactly — a markdown doc stays markdown, a JSON array stays valid JSON, a bulleted list stays bulleted.

### Pass 2 — Cluster the repeats
Group passages that convey the same underlying information. Signals that two things belong in the same group:

- They assert the same core claim or fact, however differently phrased.
- One is a paraphrase, restatement, or summary of the other.
- One is a strict superset of the other (same claim plus extra detail).
- They give the same instruction or describe the same procedure.

Signals they do **not** belong together (keep separate):

- They're about the same subject but assert different things.
- One is a general statement and the other a specific, non-equivalent case.
- Merging them would require asserting something no single source actually said.

### Pass 3 — Merge each group, losslessly
For each cluster, produce one occurrence that:

1. **Keeps every unique detail** from every copy — facts, caveats, numbers, examples, edge cases. If copy A has an example and copy B has a different one, the merged version has both.
2. **Reads as one coherent passage**, not stapled fragments. Integrate; don't concatenate.
3. **Preserves contradictions rather than resolving them.** If A says the limit is 100 and B says 200, both survive — surface the divergence in a way that stays readable (e.g., note that sources differ) rather than silently picking one or blending them into a false number.
4. **Matches the surrounding voice and format.** The merged passage should look like it was always there.

### Pass 4 — Apply and place
- **Single input** with internal repetition: collapse each group in place, keeping the merged occurrence at the location of its first appearance and removing the later ones. Make surgical edits — don't reflow or reformat the whole file.
- **Multiple inputs treated as one corpus:** keep each group's merged occurrence in the first input where it appears (in the order given) and remove it from the others. The report records exactly what moved where, so the set stays navigable without needing inline pointers. (If the user prefers inline pointers like "see notes.md", or wants everything consolidated into one file, honor that.)

**One important guardrail on cross-file removal:** if the inputs look like independent, standalone deliverables (separate articles, separate documents meant to be read on their own) rather than a unified knowledge base, stripping shared content out of all-but-one would gut files that need to stand alone. In that case, prefer deduping *within* each file and leave shared content intact across them — or, if it's genuinely unclear which the user wants, ask one short question before proceeding. Don't silently hollow out a document.

---

## Report

After finishing, give the user a concise summary — not a wall of text:

- Inputs processed (and mode: in-place or copy).
- How many duplicate groups you found and merged.
- Where merged occurrences now live, for anything moved across files.
- Judgment calls worth surfacing: near-duplicates you deliberately kept separate, contradictions you preserved, anything ambiguous.
- Roughly how much redundancy was removed (e.g., "collapsed 14 repeated points down to 5").

Keep it honest and skimmable. The report is how the user trusts that the in-place edits did what they wanted.

---

## Hard rules

1. **Never lose unique information.** Merging is union, not selection. If it appeared in any copy, it survives in the merged one.
2. **Don't over-merge.** Distinct claims about the same subject stay separate. When unsure whether two things are the same claim, keep them apart and say so.
3. **Contradictions are information.** Preserve conflicting claims; make the divergence legible instead of quietly choosing a winner.
4. **Preserve format and voice.** Deduplication edits the redundancy, not the style. Markdown stays markdown; JSON stays valid; the author still sounds like themselves.
5. **Edit surgically.** Change what's redundant and leave the rest byte-for-byte where you can. Don't take the opportunity to "improve" unrelated prose.
6. **In place by default; be auditable.** Overwrite originals unless told otherwise, always emit the report, and name the files you're about to modify before you do.
7. **Don't invent.** Synthesis means integrating what the copies say — never extending, embellishing, or "resolving" beyond the source material.
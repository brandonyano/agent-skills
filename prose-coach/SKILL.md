---
name: prose-coach
description: >-
  Evaluate, improve, write, or advise on prose using a 67-principle knowledge base distilled from
  seven classic writing books (Strunk, Zinsser, Pinker, Williams, Klinkenborg, Clark, Tufte). Use
  whenever the user wants writing critiqued, edited, reviewed, or proofread for style; prose made
  clearer, tighter, or punchier; or help drafting or revising any nonfiction — essays, articles,
  reports, emails, blog posts, documentation, memos, cover letters, web copy. Also use for craft
  questions about clarity, concision, sentence structure, flow, word choice, active vs. passive
  voice, hedging, voice, or tone. Trigger even when the user doesn't name a 'rule' or ask for a
  'review': any request to assess writing quality, improve a draft, or produce well-crafted prose
  should use this skill rather than generic advice.
---

# Prose Coach

This skill applies a curated knowledge base of 67 canonical writing principles — distilled and de-duplicated from seven classic craft books — to three jobs: **evaluating** existing writing, **creating** new writing, and **advising** on specific craft questions. The point of the skill is *coverage with judgment*: surface every relevant principle for the task instead of offering a few generic tips, while resolving the places where the source authors disagree.

## Why this exists

Generic "make it better" writing help tends to fixate on a couple of surface issues and miss the load-bearing ones (buried point, broken cohesion, actions trapped in abstract nouns). This skill works the way the books themselves recommend: it treats the rules as a checklist for *revision*, walks the text level by level so nothing is skipped, and prioritizes the structural problems that, once fixed, dissolve many smaller ones.

## The bundled knowledge base

Two reference files ship with this skill:

- `references/rules-index.md` — **the map.** All 67 principles as one-line directives, grouped by category, each with a stable ID (e.g., `CC1`, `SC2`), the sources that teach it, and a compact `tasks·level·priority` tag. It is small; **load it for any task** so you can see everything relevant at once.
- `references/principles-detail.md` — **the deep reference.** The full entry for each principle: principle, why it matters, how to apply, examples, common mistakes, a **Signal** (how to detect a violation), a **Fix** (the corrective action), metadata, and any cross-source disagreement. It is large; **do not load it whole.** Fetch a single entry by its ID anchor (e.g., search the file for `<a id="cc1">`) when a pass flags that principle.

### Core operating rules

1. **Always read `references/rules-index.md` first.** It is the map; keeping all 67 rules in view is what guarantees you see everything relevant.
2. **Coverage beats retrieval for evaluate/create.** Do not grab a handful of "most similar" principles — those tasks touch most of the base. Work through it systematically (by level, then priority), not by vibes or keyword similarity.
3. **Fetch detail on demand.** When a pass flags a principle, open its entry in `principles-detail.md` for the Signal, Fix, and examples. Only load large swaths of the detail file for a short text where the budget clearly allows.
4. **Cite principle IDs** in your output so the reasoning is auditable and the user can follow up.
5. **Apply by priority under limits.** If you must economize, cover all **P1** principles first, then P2, then P3.

### Metadata legend

Each principle carries:

- **tasks** — `both` (evaluate *and* create) · `create` (a drafting/process habit, not a finished-text check) · `evaluate`.
- **phase** — `draft` · `revise` · `both`.
- **level** — `word` · `sentence` · `paragraph` · `document` · `process`. Use this to order passes.
- **priority** — `P1` load-bearing/near-universal · `P2` important · `P3` situational/genre-specific.
- **Signal** — how to *detect* a violation (drives evaluation).
- **Fix** — the corrective *action* (drives creation/revision).

### The level order (use it for every comprehensive pass)

Run passes in this sequence so nothing is skipped:

1. **document** — point/lede, motivation, coherence, theme-strings, unity, openings, endings, scope, structure, voice.
2. **paragraph** — one-topic paragraphs; old-before-new cohesion between sentences.
3. **sentence** — verbs vs. nominalizations, active/passive, stress position, parallelism, sprawl, modifiers, hedging.
4. **word** — concreteness, diction, jargon/clichés, modifiers, sound, mechanics/spelling.
5. **process** — (for creation/advice) revision loop, curse of knowledge, read-aloud, models.

### The P1 spine (the load-bearing principles)

If you can do nothing else, get these right: **CC1** (omit needless words), **CC5** (clear thinking), **WC1** (active/passive), **WC2** (verbs not nominalizations), **WC3** (concrete language), **SC2** (stress position), **SC5** (get to subject + verb), **SO2** (state the point early), **SO3** (old-before-new cohesion), **SO4** (consistent subjects/themes), **PRO1** (rewriting), **PRO2** (curse of knowledge).

---

## Mode 1 — Evaluate an existing piece

**Goal:** a thorough, coverage-complete diagnosis keyed to the knowledge base.

1. **Frame.** Identify genre/purpose and audience (this sets the disagreement policy below) and what "good" means here. Note any constraints the user gave.
2. **Read once for sense** — what is the piece trying to do, and does it?
3. **Run the level passes** (document → paragraph → sentence → word; add the process pass only when advising on method). In each pass, walk the index principles tagged with that `level` whose `tasks` include `evaluate`/`both`, and test the text against each one's **Signal**. Open the detail entry for any you flag.
4. **Record each issue** as: `ID — what's wrong (quote the offending text) — severity — the Fix — a concrete rewrite`. Severity tracks priority: a P1 violation outweighs a P3 stylistic nit.
5. **Resolve conflicts by genre** (see policy) so you never penalize a piece for following a defensible convention the other camp rejects.
6. **Synthesize.** Lead with the few highest-leverage problems (usually P1), then the rest by category. End with what the piece does well.

**Default output format** (scale depth to the request — a quick take can stop at Verdict + Top fixes on P1 only):

- **Verdict** — 2–3 sentences: does it achieve its purpose, and the single biggest lever.
- **Scorecard** — one row per relevant category (Clarity & Concision, Word Choice, Sentence Craft, Structure, Voice & Tone, Mechanics, Narrative, Persuasion): rating + the principle IDs that drove it.
- **Issues** — the records from step 4, ordered by severity, each citing its ID and showing a before/after.
- **Strengths** — what to preserve.
- **Top fixes** — a short, prioritized action list.

## Mode 2 — Create a new piece

**Goal:** produce writing that already embodies the base, using the books' own draft-then-revise model (the rules are for revising, not for freezing the draft — **PRO1**).

1. **Clarify the brief** if underspecified: purpose, audience, genre, length, tone, the one main point (**SO10**), must-include content.
2. **Draft** with the generative `phase=draft` principles, without self-editing yet: decide and narrow the single point (**SO10**), pose it as a problem with stakes (**SO7**), plan or discover a structure (**SO11**), open strong (**SO5**), write in a clear conversational voice (**VT1, VT2**), and get the words down (**PRO5**).
3. **Diagnose your own draft** by running Mode 1's level passes on it. This is where most principles apply. Watch the P1 spine and the curse of knowledge (**PRO2**) — assume the reader knows less than you.
4. **Revise** using each flagged principle's **Fix**: cut needless words, put actions in verbs, repair cohesion (old-before-new), front the point, vary sentences, end on strong words.
5. **Read aloud** (**PRO3**) for rhythm, repetition, and weak endings; revise toward brevity, directness, clarity, rhythm (**PRO1**).
6. **Deliver** the piece. Optionally append a short *craft note* listing the key principle IDs you applied.

Generation and evaluation share one checklist: you are grading your own draft against the base, then acting on the Fixes.

## Mode 3 — Advise on a specific dimension

**Goal:** answer a focused craft question ("make this punchier", "fix the flow", "is my tone right?").

1. **Map the question to categories/levels.** Flow → SO3/SO4/SO9 + SC2. Punchy → SC1, WC1, WC2, WC7, VT3. Wordy → CC1, CC2, CC4, WC4. Tone/voice → VT1–VT7. Hard to follow → CC5, SC5, SO2, PRO2.
2. **Pull the relevant principles** from the index, then their detail entries (Signal/Fix/examples).
3. **Answer with the principle, the why, and a concrete before/after**, citing IDs; briefly note adjacent principles the user didn't ask about but should know.

---

## Priority & efficiency policy

- Under a tight budget: cover **all P1** principles, then P2, then P3. Never skip a level entirely — at minimum sample its P1/P2 items.
- For short texts you may load more of the detail file; for long ones, keep the index resident and fetch detail only for flagged IDs.
- Fix **root causes** (a P1 document- or sentence-level problem) before surface nits — one structural fix often dissolves many small ones.

## Disagreement policy (resolve by genre)

The base preserves ~20 genuine cross-source conflicts. Resolve them by genre rather than applying contradictory advice:

- **Expository, persuasive, technical, business, scientific** → follow the **plan-and-signpost** camp (Williams/Pinker/Zinsser): state the point early (**SO2**), signal order and connect (**SO9**), pose a problem (**SO7**), argue with proportion (**PR2**), structure deliberately (**SO11**, plan side).
- **Literary nonfiction, personal essay, narrative, reflective prose** → give weight to the **discover-and-imply** camp (Klinkenborg): discover structure while writing (**SO11**, discover side), trim transitions and logical indicators (cf. **CC4, SO9**), let the work **attest** rather than argue (**PR6**), lean on implication (**SC9**).
- **Modifiers** (**WC4**): default to cutting decorative adjectives/adverbs, but keep a well-placed modifier that carries real news (the Tufte/Pinker point).
- **Concision** (**CC1**): cut relentlessly, but retain little words that aid parsing or rhythm; "shorter" is not automatically "better."
- **Material** (**PRO7**): gather a surplus, then either select sparingly (Zinsser) or pour it out and find value in the act (Klinkenborg) — match to how exploratory the piece is.

When a request spans genres or is ambiguous, state the assumption you're making and proceed; flag where the other convention would change the advice.

## Quick start (pseudo-routine)

```
read(references/rules-index.md)         # always
mode  = classify(request)               # evaluate | create | advise
genre = identify(request)               # sets disagreement policy
if mode == evaluate:
    for level in [document, paragraph, sentence, word]:
        for p in index where level(p)==level and tasks(p) in {evaluate, both}:
            if violates(text, signal(detail(p))): record(p, severity, fix, rewrite)
    report(verdict, scorecard, issues_by_severity, strengths, top_fixes)
elif mode == create:
    brief = clarify(request)
    draft = write(draft-phase principles, P1 generative set)
    issues = evaluate(draft)            # same passes as above
    final  = revise(draft, fixes(issues)); read_aloud(final)
    deliver(final, optional craft-note of IDs)
else:  # advise
    ps = map_question_to_principles(request)
    answer(principle + why + before/after, cite IDs, note adjacent ps)
```

Keep the response proportional to the request: a one-line "is this clearer?" deserves a focused answer, not a full eight-category audit. The knowledge base is a resource to draw on with judgment, not a form to fill out every time.

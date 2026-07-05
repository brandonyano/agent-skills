# Writing Craft Knowledge Base — Tier 1: Quick Rules Index

A consolidated, de-duplicated reference distilled from seven books on writing well. Built for an LLM to use when **evaluating** prose (diagnosing problems), **creating** prose (drafting and revising), and **advising** writers.

The 304 individual rules extracted from the seven sources have been merged into **67 canonical principles**, organized under an 11-category taxonomy. Where the books agree, their advice is synthesized; where they genuinely disagree, the conflict is preserved under **Nuances & Disagreements** rather than resolved.

## How to use these files

This knowledge base is split across three companion files:

- **Tier 1 — Quick Rules Index** (this file, `writing-craft-rules-index.md`): a scannable directive for every canonical principle, grouped by category, each tagged with its ID, the sources that teach it, and a compact metadata tag. Use it for fast lookup, checklists, and evaluation rubrics.
- **Tier 2 — Detailed Principles** (`principles-detail.md`): the full entry for each ID — principle, why it matters, how to apply it, examples, common mistakes, source list, operational metadata, and any cross-source disagreement.
- **Operating Guide** (the skill instructions (SKILL.md)): how an LLM should *use* this base — the evaluate / create / advise playbooks, priority and disagreement policies, and the metadata legend. **Start there for any task.**

Each principle has a stable ID (e.g., `CC1`, `SC2`). In this index, the ID at the start of each line links directly to that principle's full entry in the detail file.

**Metadata tag legend.** Each index line ends with `` `tasks·level·priority` `` (full fields appear in the detail file):

- **tasks** — `both` (applies to evaluating *and* creating) · `create` (a drafting/process habit, not a text-level check) · `evaluate`.
- **level** — `word` · `sentence` · `paragraph` · `document` · `process`. Run evaluation passes level-by-level for full coverage.
- **priority** — `P1` load-bearing/near-universal · `P2` important · `P3` situational or genre-specific. Apply P1 first under any token or attention limit.
- In the detail file each entry also carries **phase** (`draft` / `revise` / `both`), a **Signal** (how to detect a violation), and a **Fix** (the corrective action).

## Sources (with abbreviations)

- **EoS** — William Strunk Jr., *The Elements of Style*
- **OWW** — William Zinsser, *On Writing Well*
- **GoG** — Roy Peter Clark, *The Glamour of Grammar*
- **SoS** — Steven Pinker, *The Sense of Style*
- **SSS** — Verlyn Klinkenborg, *Several Short Sentences About Writing*
- **Style** — Joseph M. Williams (rev. Joseph Bizup), *Style: The Basics of Clarity and Grace*
- **AS** — Virginia Tufte, *Artful Sentences: Syntax as Style*

## Categories

Clarity & Concision (CC) · Word Choice & Diction (WC) · Sentence Craft (SC) · Structure & Organization (SO) · Voice & Tone (VT) · Grammar, Punctuation & Mechanics (GP) · Narrative & Storytelling (NS) · Persuasion & Rhetoric (PR) · Process, Revision & Editing (PRO)

---

# Quick Rules Index

## Clarity & Concision

- **[CC1](principles-detail.md#cc1) — Omit needless words.** Make every word tell; cut whatever does no work — but keep words that aid parsing or rhythm. *(EoS, OWW, Style, SoS, SSS)*  `both·sentence·P1`
- **[CC2](principles-detail.md#cc2) — Replace wordy phrases and empty abstraction-words with plain words.** *the fact that → that/since; case, character, nature, factor → cut.* *(EoS, OWW, Style, SoS)*  `both·word·P2`
- **[CC3](principles-detail.md#cc3) — Prefer affirmatives; state things positively.** Negation costs the reader an extra mental step; set up a belief before denying it. *(EoS, Style, SoS)*  `both·sentence·P2`
- **[CC4](principles-detail.md#cc4) — Prune metadiscourse and signpost sparingly.** Cut verbiage about verbiage; keep only the guidance the reader actually needs. *(Style, SoS)*  `both·document·P2`
- **[CC5](principles-detail.md#cc5) — Clear thinking precedes clear writing, and clarity is achievable.** Obscurity is usually a failure of the writer, not a virtue. *(OWW, Style, SoS)*  `both·process·P1`

## Word Choice & Diction

- **[WC1](principles-detail.md#wc1) — Prefer the active voice, but choose the passive deliberately.** Default to active; use passive to manage focus, flow, and the unknown agent. *(EoS, OWW, Style, SoS, GoG, AS)*  `both·sentence·P1`
- **[WC2](principles-detail.md#wc2) — Put actions in strong, precise verbs; don't bury them in nominalizations.** Beware zombie nouns, concept nouns, and metaconcepts. *(Style, SoS, OWW, AS, GoG)*  `both·sentence·P1`
- **[WC3](principles-detail.md#wc3) — Prefer concrete, sensory language and the telling detail over abstraction.** Let readers see it; show rather than label. *(SoS, OWW, GoG, EoS, SSS)*  `both·word·P1`
- **[WC4](principles-detail.md#wc4) — Most adjectives and adverbs are unnecessary — but a well-placed modifier carries the news.** Cut decoration and verb-duplicating adverbs; keep modifiers that add information. *(OWW, EoS, Style; AS, SoS)*  `both·word·P2`
- **[WC5](principles-detail.md#wc5) — Hunt for fresh, precise words; shun journalese, jargon, clichés, and fad words.** *(OWW, SoS, GoG, EoS)*  `both·word·P2`
- **[WC6](principles-detail.md#wc6) — Use dictionaries and the thesaurus rightly; know word histories and near-synonym distinctions.** The thesaurus reminds; the dictionary decides. *(OWW, SoS, GoG, SSS)*  `both·word·P2`
- **[WC7](principles-detail.md#wc7) — Weigh the sound and length of words.** Short Anglo-Saxon words land hardest; rhythm and euphony matter. *(OWW, GoG, SSS)*  `both·word·P2`

## Sentence Craft

- **[SC1](principles-detail.md#sc1) — Master the short sentence; vary length and structure for rhythm.** Only a string of choppy sentences sounds choppy. *(SSS, AS, Style, OWW, GoG)*  `both·sentence·P2`
- **[SC2](principles-detail.md#sc2) — Put the emphatic words at the end (the stress position).** Light-before-heavy, given-before-new; control which words land last. *(EoS, Style, SoS, AS, OWW, GoG)*  `both·sentence·P1`
- **[SC3](principles-detail.md#sc3) — Express coordinate ideas in parallel form.** Like things in like syntax. *(EoS, AS, Style, SoS)*  `both·sentence·P2`
- **[SC4](principles-detail.md#sc4) — Keep related words together — and pull apart unrelated phrases that attract.** Position shows relationship; readers attach to the nearest words. *(EoS, SoS, GoG)*  `both·sentence·P2`
- **[SC5](principles-detail.md#sc5) — Get to the subject and verb quickly and keep them close; avoid sprawl and center-embedding; prefer right-branching.** *(Style, SoS, GoG, SSS)*  `both·sentence·P1`
- **[SC6](principles-detail.md#sc6) — Extend a sentence gracefully with free, resumptive, and summative modifiers (cumulative/branching), not stacked relative clauses.** *(Style, AS)*  `both·sentence·P3`
- **[SC7](principles-detail.md#sc7) — Treat syntax as a tool.** A sentence is a tree that turns a web of thought into a string of words. *(SoS, AS)*  `both·sentence·P3`
- **[SC8](principles-detail.md#sc8) — Use the intentional fragment and varied sentence moods purposefully.** Questions, commands, exclamations, and verbless lines for effect. *(GoG, AS)*  `both·sentence·P3`
- **[SC9](principles-detail.md#sc9) — Work at the level of the sentence; know what each says, doesn't say, and implies; write by implication.** *(SSS)*  `both·sentence·P3`

## Structure & Organization

- **[SO1](principles-detail.md#so1) — Make the paragraph a unit of one topic; keep paragraphs short; use the break as a rest.** *(EoS, OWW, SoS)*  `both·paragraph·P2`
- **[SO2](principles-detail.md#so2) — State the point early; don't bury the lede; lead with the point at every level.** *(Style, SoS, OWW, EoS)*  `both·document·P1`
- **[SO3](principles-detail.md#so3) — Cohesion: link sentences old-before-new.** End one sentence with what sets up the next. *(Style, SoS, AS)*  `both·paragraph·P1`
- **[SO4](principles-detail.md#so4) — Coherence: use consistent subjects/topics and run theme-strings through a passage.** *(Style, SoS, AS)*  `both·document·P1`
- **[SO5](principles-detail.md#so5) — Open strong.** The first sentence must pull the reader to the second. *(OWW, SoS, SSS, Style)*  `both·document·P2`
- **[SO6](principles-detail.md#so6) — Finish strong, and stop when you're done.** Give the last sentence as much care as the first. *(OWW, SoS, Style, SSS)*  `both·document·P2`
- **[SO7](principles-detail.md#so7) — Motivate the reader by posing a problem, not just announcing a topic.** Shared context → problem (condition + cost) → solution. *(Style, SoS)*  `both·document·P2`
- **[SO8](principles-detail.md#so8) — Maintain unity of person, tense, and tone.** *(OWW, EoS, GoG)*  `both·document·P2`
- **[SO9](principles-detail.md#so9) — Order material logically and signal the order — but signal a connection only once.** *(Style, SoS, OWW)* — see disagreement with SSS.  `both·document·P2`
- **[SO10](principles-detail.md#so10) — Narrow the scope; make one main point.** Think small. *(OWW)*  `both·document·P2`
- **[SO11](principles-detail.md#so11) — Plan the structure, or discover it as you write.** A genuine split between the books. *(Style, OWW vs. SSS)*  `create·document·P3`

## Voice & Tone

- **[VT1](principles-detail.md#vt1) — Be yourself; develop one recognizable voice.** Style is organic, not a garnish. *(OWW, SSS, SoS)*  `both·document·P2`
- **[VT2](principles-detail.md#vt2) — Write as if in conversation; use *I* and *you*; treat prose as a window onto the world.** *(OWW, SoS, Style)*  `both·document·P2`
- **[VT3](principles-detail.md#vt3) — Be confident; make definite assertions; hedge by choice, not by reflex.** *(OWW, EoS, SoS, Style, SSS)*  `both·sentence·P2`
- **[VT4](principles-detail.md#vt4) — Match register and formality to the occasion; use contractions when they fit.** *(SoS, OWW, GoG)*  `both·document·P3`
- **[VT5](principles-detail.md#vt5) — Use inclusive, non-sexist language smoothly.** *(OWW, GoG)*  `both·sentence·P3`
- **[VT6](principles-detail.md#vt6) — Don't overstate; protect credibility; drop scare quotes; favor restraint.** *(OWW, SoS)*  `both·sentence·P2`
- **[VT7](principles-detail.md#vt7) — Enact sincerity; be the narrator as a deliberate dramatic role.** *(SSS)*  `both·document·P3`

## Grammar, Punctuation & Mechanics

- **[GP1](principles-detail.md#gp1) — Treat rules as tools: master them, then break them with purpose; tell real rules from myths.** *(SoS, GoG, OWW, SSS, EoS)*  `both·process·P3`
- **[GP2](principles-detail.md#gp2) — Form the possessive singular with *'s*; let the ear guide awkward sibilants.** *(EoS, GoG)*  `both·word·P2`
- **[GP3](principles-detail.md#gp3) — Use the serial (Oxford) comma** (knowing your house style). *(EoS, GoG)*  `both·word·P2`
- **[GP4](principles-detail.md#gp4) — Master restrictive vs. nonrestrictive (commas; *that* vs. *which*).** *(EoS, OWW, GoG, SoS, Style)*  `both·sentence·P2`
- **[GP5](principles-detail.md#gp5) — Avoid comma splices, run-ons, and the few "unforgivable" punctuation errors.** *(EoS, SoS, GoG)*  `both·sentence·P2`
- **[GP6](principles-detail.md#gp6) — Use the punctuation toolkit to control pace and emphasis** (period, semicolon, dash, colon, exclamation, ellipsis, question mark, quotation marks). *(OWW, GoG, SoS)*  `both·sentence·P2`
- **[GP7](principles-detail.md#gp7) — Place modifiers next to what they modify; avoid danglers.** Often an ambiguity risk rather than an outright error. *(EoS, GoG, Style, SoS)*  `both·sentence·P2`
- **[GP8](principles-detail.md#gp8) — Make subject and verb agree across intervening phrases.** Strip to the head and test. *(SoS, GoG)*  `both·sentence·P2`
- **[GP9](principles-detail.md#gp9) — Honor real word-distinctions and confusables; mind *lie/lay*, *who/whom*, the subjunctive, and tense.** *(EoS, OWW, GoG, SoS)*  `both·word·P2`
- **[GP10](principles-detail.md#gp10) — Spell accurately; a misspelling is a speed bump.** *(GoG)*  `both·word·P2`

## Narrative & Storytelling

- **[NS1](principles-detail.md#ns1) — Get people talking; find the human element; quote well.** *(OWW)*  `both·document·P2`
- **[NS2](principles-detail.md#ns2) — Show with the telling detail and the power of names; pursue particularity.** *(GoG, OWW, SoS, SSS)*  `both·document·P2`
- **[NS3](principles-detail.md#ns3) — Drive narrative with a question or quest; tension pulls the reader along.** *(OWW, GoG, AS)*  `both·document·P2`
- **[NS4](principles-detail.md#ns4) — Use figurative language sparingly and accurately; avoid clichés and mixed metaphors.** *(GoG, SoS, SSS, OWW)*  `both·sentence·P2`
- **[NS5](principles-detail.md#ns5) — Render dialect and slang with a light, accurate touch.** *(GoG)*  `both·document·P3`

## Persuasion & Rhetoric

- **[PR1](principles-detail.md#pr1) — Style is an ethical choice: write honestly; write to others as you'd have them write to you.** *(Style, OWW, SoS)*  `both·document·P2`
- **[PR2](principles-detail.md#pr2) — Keep proportion; give substantial counterarguments their own space.** *(SoS)*  `both·document·P3`
- **[PR3](principles-detail.md#pr3) — Take a clear stand; express opinion firmly.** *(OWW)*  `both·document·P2`
- **[PR4](principles-detail.md#pr4) — Humor is a secret weapon: heighten a crazy truth.** *(OWW)*  `both·document·P3`
- **[PR5](principles-detail.md#pr5) — Let allusion, resonance, and the unadorned fact do the persuading.** *(OWW)*  `both·document·P3`
- **[PR6](principles-detail.md#pr6) — Writing attests and witnesses more than it proves** (a counter-view on argument). *(SSS)*  `both·document·P3`

## Process, Revision & Editing

- **[PRO1](principles-detail.md#pro1) — Rewriting is the essence; the rules are for revising, not drafting.** Revise toward brevity, directness, clarity, and rhythm. *(OWW, SoS, Style, SSS)*  `create·process·P1`
- **[PRO2](principles-detail.md#pro2) — Beat the curse of knowledge: show drafts, get feedback, become a stranger to your own work.** *(SoS, Style, SSS)*  `create·process·P1`
- **[PRO3](principles-detail.md#pro3) — Read your work aloud.** The ear catches what the eye misses. *(OWW, SSS, SoS, Style)*  `create·process·P2`
- **[PRO4](principles-detail.md#pro4) — Become a good reader; learn by imitation and reverse-engineering.** *(OWW, SoS, SSS)*  `create·process·P2`
- **[PRO5](principles-detail.md#pro5) — Writing is hard craft, not a gift or "flow"; focus on process and keep at it.** *(OWW, SSS, Style)*  `create·process·P3`
- **[PRO6](principles-detail.md#pro6) — Use concrete self-editing techniques** (bracket/delete tests, underline sentence openings, ask "do I need it?"). *(OWW, Style, SSS)*  `create·process·P2`
- **[PRO7](principles-detail.md#pro7) — Gather more material than you use, then select ruthlessly.** *(OWW, SSS)*  `create·process·P3`

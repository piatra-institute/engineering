# Engineering: voice and style

This is a writing guide for the book. It exists because the book's credibility depends on sentences that sound like a working engineer thinking, not like a well-meaning explainer that has been made to look formal with Latinate nouns.

The book is formal but not stiff. Technical without being anaesthetised. Its authority comes from the density of specific evidence, the clarity of derivation, the discipline of estimation, and the visibility of failure, not from hedging, portentousness, or vocabulary.

A linter (planned: `tools/eng.py voice`) will scan for the violations below mechanically. The linter catches what regex can catch. It does not replace the diagnostic read in `release-checklist.md`.

## The voice in one paragraph

The prose sounds like a working engineer who has read the primary sources, derived the model, run the experiment, and is now writing for a serious adult learner who is willing to do the work. Sentences carry weight by specificity and by structure, not by emphasis. Hedging is used only where the evidence genuinely warrants it and the hedge is doing analytical work. The reader is treated as a peer in training. Definitions are motivated before they are stated; results are preceded by the derivation and followed by the failure mode. Estimation comes before calculation. Dimensions come before equations. Failure is named. Numbers carry their year.

## What the voice is

**The authorial "we".** Settled in question 21. We address the reader directly, with an implied single guiding intelligence. Not first-person memoir ("I"); not committee voice; not faceless third-person ("the student should observe"). Use:

> We begin with measurement.

Not:

> I will show you...

And not:

> The student should observe...

**Confident.** Where the evidence supports a claim, state it. Avoid "it could be argued," "perhaps," "some might say" when the sentence has no genuine uncertainty to express. As filler, these phrases are doubt cosplay.

**Formally precise.** Variables are defined on first use. Every $\alpha$, $\beta$, $\mu$ has a named referent. Formal claims sit in `\begin{theorem}`, `\begin{principle}`, `\begin{archetype}`; conjectural ones in `\begin{remark}` or flagged with a footnote and a half-life tag.

**Estimation-first.** Before any calculation, the reader is asked to estimate. The `\begin{estimation}` environment is the formal home of this habit; it appears in every chapter (settled question 20).

**Dimensions-first.** Before any equation, the dimensions are stated. A reader who finishes the book without internal dimensional analysis has not finished the book.

**Failure-visible.** Every chapter has a failure section (settled question 29). Models break. Materials fatigue. Software fails differently from hardware. Engineers who do not name the failure mode have not described the system.

**Half-life-honest.** Every chapter and section carries a half-life tag (settled question 43). Maxwell's equations age differently from current AI tooling. The text says so.

**Rhythmically varied.** Long sentences build; short sentences land. A definition followed by a one-sentence gloss is better than a definition surrounded by four more sentences of restatement.

**Honest about its status.** The book disclaims any pretence of disciplinary completeness. Engineering depth, not science-undergraduate depth (settled question 9). Working power, not specialist mastery.

## What the voice is not

**Not hyped.** "This framework reveals...," "remarkably," "fascinatingly," "strikingly," "a profound insight": all cut. If the result is striking, the result does the striking. The adjective adds nothing the reader could not see.

**Not pedagogical in the bad sense.** The reader does not need to be told what is coming ("In this section we will examine..."), told what was just said ("What we have just shown is..."), or invited to feel clever ("As the reader has no doubt already inferred..."). State the content.

**Not breathless.** "Here's where it gets interesting," "this is where the argument really begins," "and crucially," "let us pause to note." If the material needs announcement to signal importance, it has not earned the importance.

**Not equivocating.** "It could be argued," "some would say," "one might think that" when the writer has a position and the evidence supports it. Equivocation is honest only when the writer is genuinely uncertain.

**Not performatively humble.** "Of course, the picture is more complicated than we can address here," "a full treatment would require...," "limitations of space prevent us from..." Used as default filler they become a tic. Prefer concrete statement: "A full treatment of X is in Volume Y, Chapter Z" or "The model does not address Z; see \\textcite{...}."

**Not generically male.** Generic agents, readers, citizens, workers, engineers are not "he." Use plural constructions or singular "they" unless the historical actor is specifically male and that fact matters.

## Patterns to kill

These constructions make prose sound machine-generated. Cut on sight.

### The em-dash

Banned outside primary-source quotations. Settled in editorial decisions, applied across all source files.

Replacement rules:

- **Appositive / parenthetical insertion**: comma pair.
- **Pivot / amplification**: period plus new sentence.
- **Compressed definition-by-apposition**: comma pair, or rewrite if awkward.
- **Enumeration**: comma, or "and."

If the sentence depended on the em-dash for emphasis, rewrite the sentence. The replacement has to read naturally. If the comma flattens a load-bearing contrast, the sentence was built around the dash and needs a different structure.

**Preserved**: em-dashes inside `\\begin{verbatim}`, inside quoted primary-source text, and inside math environments.

**Note**: the LaTeX source may contain `---` (three hyphens, rendered as em-dash by TeX). The linter flags both `---` and the Unicode `—`.

### The negate-first-then-pivot construction

The most overused construction in AI-assisted academic writing.

**Forms to cut:**

- "X is not Y. It is Z."
- "X is not just Y, but Z."
- Inline "not X but Y."
- Triple negation: "not A, not B, not C, but D."

**The test**: does the sentence state the positive directly, or does it reject an alternative first? If the alternative is rejected, rewrite. State both halves positively.

*Bad:* "Engineering is not applied science. It is disciplined intervention."

*Better:* "Engineering is the discipline by which measured reality becomes reliable intervention." (The contrast is in the prose, not the syntax.)

The thesis sentence in the editorial-decisions log is allowed to break this rule because it is the thesis. Body chapters do not.

### AI-tic vocabulary

These words and phrases recur in AI-generated prose and hollow out sentences:

- **Generic intensifiers**: "fundamentally," "essentially," "at its core," "in many ways," "in a very real sense," "quite literally."
- **Generic hedges used as filler**: "it is worth noting," "it is important to note," "interestingly," "notably," "crucially," "it should be emphasized."
- **Transitional clichés**: "Furthermore," "Moreover," "Ultimately," "In essence," "In fact," "That said."
- **Abstract flourishes**: "landscape" as metaphor ("the engineering landscape"), "tapestry," "lens" (as in "through the lens of"), "nuanced," "multifaceted," "intricate web," "delve," "unpack."
- **Over-explanation tails**: "which tells us something about," "which is another way of saying," "in other words," "simply put," "put differently," "what this means is."
- **Self-announcing topic sentences**: "This section will examine," "In this chapter we show," "In what follows, we demonstrate."
- **Meta-explanation tails**: "Having shown X, we now turn to Y," "As we have seen," "This completes our treatment of..."
- **Performative qualifiers**: "in some sense," "to some extent," "up to a point," "broadly speaking" when the writer has a sharp point to make.
- **Engineering-flavoured hype**: "robust," "novel," "leveraging," "synergy," "best-in-class," "cutting-edge," "revolutionary," "breakthrough."

### Rhetorical questions immediately answered

*Bad:* "So what happens when a beam buckles? It collapses."

*Better:* "When a beam buckles, the load path collapses." (Use the phenomenon, not the rhetoric.)

A rhetorical question earns its place when the answer is genuinely surprising or when the pause creates productive tension. When the answer follows immediately and predictably, the question is wasted motion.

### "Now," as paragraph opener

One per chapter maximum. It is a useful gear-shift when used sparingly. When every section starts with "Now," it becomes tic.

### The triple declarative as default

"The system fails. The system warns. The system recovers." The restatement-that-sharpens is a legitimate tool. It becomes a tic when it appears in every section.

### Thesis restatement

Each chapter has a structural thesis. State it once in the body, compress it in the chapter's closing paragraph, and move on. Restating with different vocabulary signals distrust of the reader.

### Footnote-as-soapbox

Footnotes are for citations, qualifications, and digressions too narrow for the main text. Not a place to resume an argument the main text decided to leave alone.

## Patterns that work

### The flat declarative

> A balance is an accounting equation.

No emphasis. No signposting. The sentence carries its own weight because the concept is precise.

### The motivation sentence before the definition

Every `\\begin{definition}` earns its box by what comes before it. A single sentence of motivation that names the question the definition answers, followed by the formal statement.

### The estimation that earns the calculation

Every worked example is preceded by an estimation. The estimation may be wrong by a factor of three; the calculation is then pleased to report a closer answer. The reader internalises the order-of-magnitude habit by repeated practice.

### The failure that closes the model

Every model has a failure section. The model breaks at high Reynolds, low Knudsen, near phase transitions, at large amplitude, under non-Gaussian noise, in adversarial deployment. Naming the breakage IS the engineering.

### Cross-reference that actually pays off

`\\cref{book03:ch07}`, `\\autoref{prop:conservation-of-mass}` — when the referenced item genuinely extends or underwrites the current claim. Avoid decorative cross-references.

## Rhythm and register

**Read aloud.** If you stumble, the reader will stumble. If a sentence cannot be said in one breath, split it.

**Latinate when Latinate is correct.** The book's subject requires a Latinate register at moments: "infrastructure," "institution," "regulation," "constraint." Prefer the shorter word when it is the right word; do not strip Latinate from false populism.

**Technical terms define themselves through use.** Once `archetype` or `failure section` is introduced, use them as working vocabulary without re-defining.

**Acronyms**: expand on first use in each chapter. Permanent vocabulary (SI, PDE, ODE, FBD, FEM, MTBF) lives in `frontmatter/notation.tex`.

**Numbers**: spell out under ten; use digits from 10 upward; always use digits when the figure is the point.

## Dated statistics

Contemporary statistics are time-stamped with their year in the sentence, not only in the citation. A figure without its year ages silently.

> Annual global cement production, current as of 2025, is approximately 4.2 Gt.

Not:

> Annual global cement production is approximately 4.2 Gt.

The book's shelf life is decades; figures that read as present-tense will not age well. The half-life tag on each chapter and section gives the reader an additional honesty about what to re-derive in 2046 and what to trust.

## No invented scenes or figures

The book makes formal and empirical claims. Every dated claim, named actor, numerical figure, court decision, accident name, regulatory ruling, and institutional fact traces to the bibliography. If a detail is inferred rather than sourced, either cite the inference and its grounds or cut the detail. Attractive-but-invented detail erodes the whole apparatus.

## The test

Before a chapter is marked final, read it through this lens: could an informed critical reader (a domain reviewer) find a sentence that reads as AI-generic or hyped rather than as the author's worked position? If yes, fix the sentence. The book's credibility lives in whether every paragraph sounds like it came from someone who measured the thing, derived the model, broke the prototype, and recovered.

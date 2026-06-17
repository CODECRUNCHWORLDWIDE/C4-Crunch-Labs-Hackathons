# Lecture 1 — Rubrics and the Two Judging Mindsets

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can name the five rubric dimensions used by most public hackathons, cite at least one public rubric source per dimension, distinguish *judge-as-engineer* from *judge-as-investor* in the room within 20 seconds, and self-score your team's submission on the five dimensions with one-line evidence per score.

If you only remember one sentence from this lecture, remember this:

> **The rubric is the bench, the judge is the runner, the score is the measurement. The team that prepares for the rubric prepares for the right exam; the team that prepares for "wow factor" prepares for an exam that does not exist on any rubric.**

Weeks 7 and 8 ran the dry-run from kickoff to retro. The team's submission is committed, the demo video is published, the retro is logged, the follow-up issue is filed. Now the demo enters the *judging window* — the part of the event where a human (or four humans, or a panel of seven humans) sits across from the team or watches the team across a panel desk, applies a scoring rubric, and produces a number. This week is the rehearsal of the team's part of that interaction.

This lecture has three parts. Part 1 (sections 2-4) covers the five rubric dimensions and the three public rubric samples (MLH, NumFOCUS, Devpost large-event). Part 2 (sections 5-6) covers the two judging mindsets — engineer and investor — and the cues that tell you which one is in the room. Part 3 (section 7) is the lecture's recap.

---

## 1. What judging actually is

Judging is **a human assessment under constraint**, scored against a rubric, performed by a person who has 3-7 minutes per team and is scoring 20-80 teams in a 2-4 hour window. It is not a measurement (a measurement implies repeatability); it is an *assessment* (an assessment implies judgment).

Three properties of that assessment shape every other decision the team makes this week:

- **The rubric is the constraint.** A judge cannot score a team well on a dimension the rubric does not name. If the rubric does not include "originality" and the team's strongest dimension is originality, the team will be under-scored. The team's job is to maximise the *named* dimensions, not the *unnamed* impressive properties.
- **The time is the constraint.** A judge has 3-7 minutes per team. The judge's *attention* is the scarce resource. The team's job is to make the team's score *easy to assign* — clear narrative, clear evidence, clear ask. A team that requires the judge to *figure out* what is impressive will be under-scored.
- **The consistency is the constraint on the judge.** A judge's job is to score consistently across the 20-80 teams they see. The judge cannot give one team's "originality" a 5 and another team's identical originality a 3. The rubric is what the judge uses to *normalise* their own scoring; the team that fits the rubric cleanly fits the judge's normalisation.

> **C4 voice:** the rubric is not a suggestion. It is the exam. The team that reads the rubric and *scores themselves against it before the judging* prepares for the right exam; the team that arrives with a beautiful demo and discovers at the table-walk that "originality" was never on the rubric arrives at the wrong exam, gets a low score, and writes a Reddit post about "unfair judging." The judging was not unfair; the team prepared for the wrong exam.

### 1.1 What the rubric is not

Three things the rubric is *not*:

- **Not a measurement of the build's intrinsic quality.** Two builds of identical quality can score differently because the rubric names different dimensions or different weights. The score is *relative to the rubric*, not absolute.
- **Not a measurement of the team's effort.** A team that worked 24 hours and a team that worked 14 hours can score identically if the artifact is identical. The judges do not see the effort; they see the artifact.
- **Not a measurement of the team's potential.** The rubric scores *what is in the room*. "We could build X if we had two more weeks" is a Q&A answer, not a rubric data point.

The team that internalises these three "not"s pitches differently — concretely, evidence-first, present-tense. The team that does not internalise them pitches in the subjunctive ("we *would* have built", "if we *had* time, we *would* have"), which does not move the rubric.

---

## 2. The five rubric dimensions

The dimensions that recur across MLH, NumFOCUS, and most public Devpost-event rubrics — the *common floor* — are:

```
┌────────────────────────────────────────────────────────────────────┐
│  THE FIVE C4 RUBRIC DIMENSIONS — THE COMMON FLOOR                   │
│                                                                    │
│  1. Technical complexity   — what was hard to engineer             │
│  2. Design and UX          — how the build feels to use            │
│  3. Originality            — how different from existing work      │
│  4. Polish                 — how finished the build looks          │
│  5. Presentation           — how cleanly the pitch lands            │
└────────────────────────────────────────────────────────────────────┘
```

Each dimension is graded on a 1-5 scale by default. Some events use 1-10. Some events weight (e.g., HackMIT's 25/20/20/20/15); some do not (e.g., the MLH default rubric).

### 2.1 Technical complexity — what was hard to engineer

What is measured: the engineering depth of the build. The non-trivial systems-level decisions. The thing a senior engineer would look at and say "that is not a weekend's worth of off-the-shelf glue."

Evidence the team can offer in the pitch:
- A specific architectural decision and the alternative that was rejected.
- A specific performance trade-off (latency vs accuracy, batch vs stream, etc.).
- A specific integration that required understanding of the integrated system (not just calling its API).

Evidence the team can offer in the Q&A:
- The code path for the most technically-loaded user action.
- The failure mode the team designed against and the recovery path.
- The scale at which the current design breaks.

What it is *not*:
- The number of frameworks used.
- The line count.
- The buzzword density.

> **C4 voice on technical complexity:** the judge-as-engineer (Lecture 1 §5) scores this dimension directly. The judge-as-investor (Lecture 1 §6) scores it indirectly — they want to know "is the team technically credible enough to keep building." Both judges read the same evidence; the difference is what they conclude from it.

A team's technical-complexity score lives or dies on the *one specific decision* the team can name in 15 seconds. If you cannot name the decision, the judge cannot score it.

### 2.2 Design and UX — how the build feels to use

What is measured: the user-facing quality of the build. The screen the user lands on, the flow they walk through, the points where the build either helps them or fights them.

Evidence in the pitch:
- A user walking through the build (the *demo*, beat 2 of the 30-90-45-15 arc — Lecture 2 §2).
- The first impression of the landing screen — the typography, the spacing, the call to action.
- The error state, if surfaced — does the build fail gracefully or yell at the user?

Evidence in the Q&A:
- The user research the team did (even one interview is more than zero).
- The accessibility considerations (alt text, contrast, keyboard navigation).
- The mobile vs desktop trade-off and which one the team optimised for.

What it is *not*:
- The number of screens.
- The amount of custom CSS.
- The fanciness of the animations.

> **C4 voice on design and UX:** a design that the user can *navigate without instruction* scores higher than a design that requires the team to explain what the user is looking at. The demo-first beat (Lecture 2 §2.1) is the team's evidence that the user *can* navigate without instruction; the team simply shows the user doing it.

The dirty secret of design judging: judges are tired, judges are seeing their 12th team in a row, and judges score the build that *looks done* higher than the build that has more features but looks half-baked. Polish (dimension 4) and design (dimension 2) are different but correlated; a high design score requires the polish to be there.

### 2.3 Originality — how different from existing work

What is measured: how the build differs from what the judge has seen before or could find on GitHub in 30 seconds.

Evidence in the pitch:
- The specific user, pain, and verb the build targets — narrowed enough that "the most-similar existing tool" is not an obvious answer.
- The specific feature the team built that does *not* exist in the most-similar existing tool.
- The reason the team chose this specific user/pain/verb (the prompt-fit moment from Week 5).

Evidence in the Q&A:
- The team's awareness of the closest competitor (an honest "the closest existing thing is X, and we differ by Y" is high-signal).
- The reason the team is *not* worried about being duplicated by the closest competitor.
- The team's research depth on the space (one paragraph of research counts more than zero).

What it is *not*:
- "There is nothing like this on the market." (Judges almost never believe this; even if true, the claim erodes trust.)
- "Our combination of features is unique." (Combinations are not the same as originality.)
- A custom framework when a standard one would have worked.

> **C4 voice on originality:** originality is *narrow target* + *specific feature*. The team that targets "students" loses to the team that targets "FIU CS students walking from dorms to morning classes." The narrow target is the originality lever; the specific feature is the proof.

NumFOCUS publishes a "community fit" dimension that some events use as a sixth column. The C4 voice rolls "community fit" into originality at the cohort scale — does this build matter to the community it targets, in a way the next-most-similar build does not.

### 2.4 Polish — how finished the build looks

What is measured: the *finished-ness* of the build. The number of obvious rough edges. The README's quality. The demo video's audio. The submission's typo count.

Evidence in the pitch:
- A demo that runs from a live deploy URL (not localhost, not a fake screen-share).
- A README with a clear opening paragraph, a how-to-run, and a links section.
- A submission cover sheet (`SUBMISSION.md`) with the six sections from Week 8 Lecture 3 §3.

Evidence in the Q&A:
- The team's awareness of the *one* thing they would polish next.
- The team's specific cut decisions from hour 18 (Week 8 Lecture 2) — "we cut X because of Y" reads as polish discipline, not as a lack of features.
- The license and the code of conduct in the repo (judges check; some events score this directly).

What it is *not*:
- The amount of work the team did.
- The number of features.
- The custom-illustrated empty-state screen (sometimes helpful, often a distraction).

> **C4 voice on polish:** polish is the *absence of rough edges* more than the *presence of fancy edges*. The team that has zero obvious rough edges and zero fancy edges scores higher on polish than the team that has six fancy edges and four obvious rough ones.

The polish score correlates strongly with the team's hour-22 submission discipline (Week 8 Lecture 3 §3). The team that polished the README at hour 22 and stopped at hour 23 typically scores higher on polish than the team that kept pushing code through hour 23:55.

### 2.5 Presentation — how cleanly the pitch lands

What is measured: the team's *live delivery* of the pitch. The cadence, the timing, the visual aid, the Q&A handling.

Evidence in the pitch:
- The 3-minute cap respected (or exceeded by no more than 15 seconds).
- The 30-90-45-15 arc respected — problem named in the first 30 seconds; demo started by 0:30.
- The team's pacing — neither rushed nor lethargic.
- Eye contact with the judge — or, in a panel, with at least three of the panel members.

Evidence in the Q&A:
- The five-most-asked answers ready and surfacing in <2 seconds (Lecture 3 §3).
- The bridge sentence used at least once to recover a hard question (Lecture 3 §3.4).
- The "I don't know" sentence used at least once if the team genuinely does not know an answer (Lecture 3 §3.5).

What it is *not*:
- The slide deck's design quality (most hackathon pitches do not use slides).
- The team's clothing.
- The team's number of people on stage.

> **C4 voice on presentation:** the presentation dimension is the only one of the five that has no artifact the judges can read after the pitch. The pitch *is* the artifact. The team that rehearses the pitch (this week's mini-project) scores higher on presentation than the team that improvises.

The five dimensions are the floor. Events add: community fit (NumFOCUS), prize-track fit (most sponsor prizes), reproducibility (research-leaning events). The C4 voice teaches the floor; the team scales up to the event's specific overlay on the day.

---

## 3. Three public rubric samples

### 3.1 MLH organizer guide — the default rubric

Major League Hacking publishes the organizer guide as a free resource for events affiliated with the MLH circuit. The default rubric in the guide:

```
┌────────────────────────────────────────────────────────────────────┐
│  MLH DEFAULT RUBRIC — 5 DIMENSIONS, 1-5 SCALE, UNWEIGHTED          │
│                                                                    │
│  Technical Difficulty     | 1 2 3 4 5  (1=trivial; 5=very hard)    │
│  Originality              | 1 2 3 4 5  (1=common; 5=novel)         │
│  Design                   | 1 2 3 4 5  (1=rough; 5=polished)       │
│  Completion               | 1 2 3 4 5  (1=partial; 5=fully working)│
│  Learning Experience      | 1 2 3 4 5  (1=little; 5=substantial)   │
│                                                                    │
│  Total possible: 25.  Sum is the team's score.                     │
└────────────────────────────────────────────────────────────────────┘
```

Notes for the team:
- "Completion" maps to C4's *polish*.
- "Learning Experience" is unique to MLH and reflects the educational mission of the events; some events drop this dimension.
- *Presentation* is not a separate MLH dimension — MLH events fold it into the other four indirectly. This means at an MLH event, a great pitch with a thin build can lose to a clunky pitch with a stronger build. Read the event's specific rubric before pitching.

Source: <https://organize.mlh.io/> (judging chapter).

### 3.2 NumFOCUS event playbook — the open-source community rubric

NumFOCUS is the non-profit that supports many open-source scientific computing projects (NumPy, SciPy, Matplotlib, pandas, Jupyter). The NumFOCUS event playbook is freely licensed and used by community-run events:

```
┌────────────────────────────────────────────────────────────────────┐
│  NUMFOCUS RUBRIC — 6 DIMENSIONS, 1-5 SCALE, WEIGHTED               │
│                                                                    │
│  Technical Quality        | 1-5 | weight 25%                        │
│  Innovation               | 1-5 | weight 20%                        │
│  Usability                | 1-5 | weight 20%                        │
│  Community Fit            | 1-5 | weight 15%                        │
│  Presentation             | 1-5 | weight 10%                        │
│  Reproducibility          | 1-5 | weight 10%                        │
│                                                                    │
│  Weighted total: max 5.0; reported to 1 decimal.                   │
└────────────────────────────────────────────────────────────────────┘
```

Notes:
- "Community Fit" is the NumFOCUS-specific dimension. It asks: does this build serve a real community, or is it an isolated demo?
- "Reproducibility" reflects the scientific-computing context. A reproducible build (deterministic dependencies, documented data sources, test coverage) scores higher than a one-off demo.
- "Presentation" is named explicitly, weighted at only 10%. At community events, the rubric is more forgiving of clunky delivery if the work is strong.

Source: <https://numfocus.org/community/projects> (event playbook).

### 3.3 Large public Devpost-event rubric — HackMIT example

HackMIT publishes its participant guide each year, including the rubric. The 2023/2024-era rubric (as of public records; the team should verify against the current year):

```
┌────────────────────────────────────────────────────────────────────┐
│  HACKMIT-STYLE RUBRIC — 5 DIMENSIONS, 1-5 SCALE, WEIGHTED          │
│                                                                    │
│  Technical Complexity     | 1-5 | weight 25%                        │
│  Design / UX              | 1-5 | weight 20%                        │
│  Originality              | 1-5 | weight 20%                        │
│  Practicality             | 1-5 | weight 20%                        │
│  Presentation             | 1-5 | weight 15%                        │
│                                                                    │
│  Weighted total: max 5.0; reported to 2 decimals for ranking.      │
└────────────────────────────────────────────────────────────────────┘
```

Notes:
- "Practicality" replaces MLH's "Completion." It asks not "is it finished" but "could this actually be used."
- The 25/20/20/20/15 distribution gives technical complexity the largest single weight; HackMIT historically attracts strong technical teams and the rubric reflects that.
- Some HackMIT prize tracks layer additional dimensions (best AI/ML hack, best beginner hack, best hardware hack). Track rubrics are published with the prize description.

Source: <https://hackmit.org/> (search past-event archives).

### 3.4 What the comparison teaches

Three rubrics, three weights, three slightly different dimension names. The pattern: *the five C4 dimensions are present in every public rubric*. The names differ; the weights differ; the underlying structure is the same.

The team's preparation strategy:
- **Default-prep** against the five C4 dimensions. Cover the floor.
- **Read the event's specific rubric the morning of judging.** Note the weight differences.
- **Adjust emphasis in the 3-minute pitch by the weights.** If "originality" is weighted 25%, lead the pitch with the originality angle. If "polish" is weighted 25%, lead with the polish.
- **Read the prize track rubrics for any prize the team is targeting.** Sponsor prizes often have different rubrics from the general prize; the team's *primary* and *secondary* targets may require different pitch emphases.

The team that ignores the event-specific rubric is preparing for the C4 default; the team that reads it adjusts for the actual exam.

---

## 4. Scoring discipline

The 1-5 scale is universal across the three samples. The scale's anchor points matter; without anchors, "3 of 5" varies across judges by up to a full point.

### 4.1 The 5-point scale anchors

```
5 — outstanding. The top of what the judge has seen across the day.
    The team that scores a 5 on a dimension is the team the judge
    will remember tomorrow. ~5-10% of teams reach this on any dimension.

4 — strong. Above the median. The team has a clear lever in this
    dimension and applied it well. ~20-25% of teams reach this.

3 — solid. The expected baseline for the event. Most teams default
    here when the team did the work but did not push the dimension.
    ~40-50% of teams. Most C4 dry-run scores will land here.

2 — partial. The team did some work in this dimension but it is
    visibly incomplete or unconsidered. ~15-20% of teams.

1 — minimal or absent. The team did not address this dimension in
    any visible way. ~5-10% of teams.
```

The anchors come from the C4 voice's pattern-match across MLH, NumFOCUS, and Devpost public rubric guidance. The percentages are illustrative, not absolute; they sketch the *expected distribution* a judge should produce across a day of judging.

### 4.2 The "all 5s" anti-pattern

A new judge sometimes scores every team's every dimension at 4 or 5 to "be kind." The C4 voice rejects this — the rubric stops working when the scale compresses. If every team's polish is a 4 or 5, polish is no longer measured.

When self-scoring (Exercise 1), the team should expect to see scores across the 2-4 range, with one or two 5s if the team is honestly strong on a dimension and one or two 2s if the team is honestly weak. A self-score of all 4s and 5s indicates the team is grading on effort, not artifact.

> **C4 voice on self-scoring:** be harder on yourself than the average judge would be. A self-score of 17/25 with honest evidence is more useful than a self-score of 23/25 with rationalised evidence. The honest score lets the team see what to improve; the rationalised score lets the team feel good without changing anything.

### 4.3 The evidence-per-score rule

Every score in the team's self-score (Exercise 1) carries a one-line evidence cite. Format:

```
Dimension: Technical Complexity
Score: 3 of 5
Evidence: "The team integrated the GitHub API with a polling fallback when
           webhooks failed. The fallback is the engineering-tradeoff the
           team can name in the Q&A."
```

The one-line evidence is the *defence* of the score. If the team cannot write the one-line evidence, the team cannot defend the score, and the score is not defensible.

The judges in a real event do the same exercise mentally — they assign a score and they have to be ready to defend it to other judges in the consensus discussion. The team that mirrors that exercise in their self-score prepares for the *judge's discipline*, not just the team's own self-image.

---

## 5. Judge-as-engineer

A *judge-as-engineer* is a judge whose dominant lens is technical depth. Most engineer-judges are working engineers or engineering managers; some are CS faculty; some are technical founders.

### 5.1 What engineer-judges ask

The engineer-judge's typical questions (a representative sample, not exhaustive):

```
"What does the code path look like for [user action X]?"
"How does the build handle [load condition Y]?"
"What was the hardest technical decision and what did you reject?"
"How does the [external dependency Z] failure mode propagate?"
"What is the team's test coverage / monitoring / error handling?"
"What would break if you 10x'd the users?"
"How did you choose [framework / language / database] over [alternative]?"
```

The engineer-judge reads the team's *technical credibility* through the answers. The judge is not necessarily looking for the *right* answer; the judge is looking for *engineering judgment*. A team that names the trade-off and the reasoning scores higher than a team that names only the chosen path.

### 5.2 Cues that the engineer-judge is in the room

The team can read the engineer-mindset within the first 20 seconds of the pitch:

- **The judge picks up the rubric and writes immediately when the team names the build's tech stack.** Engineer-judges score technical complexity on the stack mention.
- **The judge asks a technical question before the demo ends.** Engineer-judges interrupt for clarification on the stack or the architecture.
- **The judge looks at the screen, not at the team.** Engineer-judges read the build's affordances; investor-judges read the team's affect.
- **The judge's first question after the pitch is "what does the [X] do under the hood."** This is the canonical engineer-judge opener.

If the team reads 2+ of these cues in the first 30 seconds, the judge is engineer-mindset. Adjust the pitch's emphasis accordingly (Lecture 1 §5.3).

### 5.3 Adjusting the pitch for an engineer-judge

The pitch's *structure* does not change — the 30-90-45-15 arc holds. The pitch's *emphasis* shifts:

- **In the problem beat (30s):** keep the user/pain/verb framing but add a one-line technical framing — "we needed a real-time data layer that survives intermittent connectivity." The technical framing is the hook for the engineer-judge.
- **In the demo beat (90s):** show the build but narrate the technical layer briefly — "this list updates from a webhook; the polling fallback you see in the bottom-right is the engineering trade-off we made." Twenty extra seconds of technical narration in the demo is the right ratio.
- **In the tech beat (45s):** lean into this. The 45 seconds is where the engineer-judge's score is decided. Name one specific decision and the alternative rejected. Do not summarise the whole stack; name the one decision that mattered.
- **In the ask beat (15s):** unchanged. The ask is the same for both mindsets.

The team that *talks technical* to an engineer-judge from the first beat scores higher on technical complexity than the team that holds the technical detail for the tech beat alone. The engineer-judge has already started scoring by 0:30; the team needs to give them the evidence before that mark.

---

## 6. Judge-as-investor

A *judge-as-investor* is a judge whose dominant lens is product-market-fit and team-to-pursue-it. Most investor-judges are venture investors, angel investors, founders, or product managers. Some are sponsor-company representatives whose mandate is "find teams we want to keep talking to."

### 6.1 What investor-judges ask

The investor-judge's typical questions:

```
"Who is the user, specifically?"
"How big is this market?"
"Would you keep building this after the hackathon?"
"What is the retention story? Who comes back?"
"Who is the closest existing tool that does this, and why don't they win?"
"What do you do for distribution? How do users find you?"
"How does this make money, eventually?"
"What is the team going to do next week if you win?"
```

The investor-judge reads the team's *commercial credibility* and the team's *commitment* to the build past the event window. The judge is not necessarily looking for a real business; the judge is looking for *commercial judgment* and *follow-through intent*.

### 6.2 Cues that the investor-judge is in the room

- **The judge writes on the rubric when the team names the *user*, not the *stack*.** Investor-judges score originality and practicality on the user-pain framing.
- **The judge asks a market-size question before the demo ends.** Investor-judges interrupt for clarification on the addressable market or the closest competitor.
- **The judge looks at the team, not at the screen.** Investor-judges read team affect; engineer-judges read build affordances.
- **The judge's first question after the pitch is "would you keep building this."** This is the canonical investor-judge opener.

If the team reads 2+ of these cues in the first 30 seconds, the judge is investor-mindset.

### 6.3 Adjusting the pitch for an investor-judge

- **In the problem beat (30s):** lean into the user-pain framing. Spend the full 30 seconds on the user. The investor-judge is scoring originality and practicality on this beat.
- **In the demo beat (90s):** show the build *and* tell a one-sentence user story — "this is Maya, a junior CS student at FIU, two minutes before her 8am class." The story-frame is the investor-judge's hook.
- **In the tech beat (45s):** lighter. Mention the stack in one sentence and move on. The investor-judge does not score this beat as heavily; spending the full 45 seconds here is wasted.
- **In the ask beat (15s):** make the ask more concrete for investor-judges. "We will spend the next two weeks talking to ten more FIU students and shipping the saved-items feature." A specific next step beats a vague "we hope you like it."

The team's pitch becomes ~10 seconds longer on the problem beat and ~10 seconds shorter on the tech beat for the investor-judge. The total stays at 3:00.

### 6.4 Mixed-mindset judging panels

Real panels are usually mixed. A panel of 4 judges might have 1 engineer, 2 investors, and 1 mixed-mindset (often a sponsor representative). The team's adjustment strategy:

- **Default-prepare for the mixed case.** The 30-90-45-15 arc is the default; do not over-tilt to one mindset.
- **Read the room within the first 60 seconds.** Note which judges write at the problem beat (investors) and which write at the tech beat (engineers).
- **In the Q&A, tilt answers to the asker.** The engineer-judge asking a technical question gets a technical answer; the investor-judge asking a user-story question gets a user-story answer.
- **Do not adjust the pitch *during* a 3-minute slot.** Adjust the *Q&A*; the pitch is committed by the time you start.

The mixed-panel reality is why the C4 default is the 30-90-45-15 ratio rather than an engineer-skewed or investor-skewed default. The default optimises for the mixed case; the team adjusts up or down depending on what the room reveals.

---

## 7. Recap and exit criteria

This lecture covered three things: the five rubric dimensions (technical complexity, design and UX, originality, polish, presentation); three public rubric samples (MLH default, NumFOCUS, HackMIT-style); the two judging mindsets (judge-as-engineer and judge-as-investor) and the cues to read them.

### 7.1 Recap

- The rubric is the constraint; the team that prepares against the rubric prepares for the right exam.
- The five C4 dimensions are the *common floor*; every event customises on top.
- The 1-5 scale has anchors at each point; honest self-scoring uses the full range.
- Every score in the team's self-score carries a one-line evidence cite.
- The two mindsets read different cues; the team can identify which mindset within 20 seconds.
- Adjust emphasis (not structure) of the pitch by the mindset; the 30-90-45-15 ratio stays.
- Mixed panels are the realistic default; the C4 ratio is tuned for the mixed case.

### 7.2 What "I read this lecture" means

After reading this lecture, the team should be able to:

- Name the five C4 dimensions in order, from memory.
- Cite at least one public rubric source (MLH, NumFOCUS, or HackMIT) and name one weight from that rubric.
- Distinguish judge-as-engineer from judge-as-investor by at least two cues each.
- Apply the 5-point scale's anchors to a single dimension of their own submission and produce a defensible 1-line evidence cite.

The lecture's deliverable is the team's preparation for Exercise 1 (self-score the team's Week 8 submission) and the mini-project (mock pitch + mock Q&A). The lecture is the *map*; the exercises and the mini-project are the *terrain*.

### 7.3 Exit criteria

- [ ] You can name the five rubric dimensions in order.
- [ ] You can cite at least one public rubric source.
- [ ] You can name the two judging mindsets and at least two cues per mindset.
- [ ] You can apply the 1-5 scale's anchors to one of your team's submission dimensions.
- [ ] You can describe the difference between "structure" and "emphasis" in the pitch arc (the structure does not change between mindsets; the emphasis does).

When all five are checked, continue to Lecture 2 (the 3-minute arc and the live-coding trap).

---

*The rubric is the bench. The judge is the runner. The score is the measurement. The team that prepares for the rubric prepares for the right exam.*

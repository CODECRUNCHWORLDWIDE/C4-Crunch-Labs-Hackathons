# Exercise 2 — The Q&A Drill

> **Time:** ~1 hour.
> **When in the week:** Friday.
> **Deliverable:** `EXERCISE-02-QNA-DRILL.md` committed to your `week-09/` working folder.
> **Prerequisite:** Lecture 3 read; team's Week 8 demo video re-watched once.

## What this exercise is

You will apply the five-archetype Q&A drill (Lecture 3 §3) to your team's specific build. For each archetype, you will:

- Write the specific question a real judge would ask about *your* build.
- Write the 30-second answer using the structure from Lecture 3 §3.7 (direct answer / supporting evidence / concrete close).
- Time the answer aloud (use a timer; aim for 25-30 seconds; reject answers under 20 or over 35 seconds).

Then write *one* bridge sentence on a fake hard question (Lecture 3 §3.8) and *one* "I don't know" answer on a fake genuinely-out-of-scope question (Lecture 3 §3.9).

The exercise is solo. You are role-playing both judge and team. The output is the kind of Q&A prep sheet the team would print on a single piece of paper and clip to the pitch script before the judge-room slot.

## What this exercise is not

This is not a team activity (yet — the team-level consensus on the five answers happens in the mini-project). The exercise is your individual draft of the five answers. The team will harmonise the wording later; the exercise is the *content*.

The exercise is also not a writing exercise. You will be *reading aloud* into a timer. Written-only Q&A prep is not the same skill as the aloud Q&A.

## What you will need

- Your team's Week 8 submission, fresh in mind: the user, the pain, the verb, the tech stack, the cuts you made at hour 18.
- A 30-second timer (the `pitch_timer.py` helper is overkill for this; a phone timer is enough).
- A paper notebook or a Markdown scratch file.
- A 60-minute focus window.

## The five archetypes

Per Lecture 3 §3.1:

```
Q1 — The user question
Q2 — The closest-competitor question
Q3 — The technical question
Q4 — The follow-through question
Q5 — The challenge question
```

For each, you will write *the specific question* a real judge would ask about your build (not a generic placeholder; the actual sentence the judge would say).

## The deliverable — five archetypes

For each of Q1 through Q5:

```markdown
## Q[N] — [Archetype name]

**Specific question for our build:**
[The actual sentence the judge would say.]

**30-second answer (written):**

[The direct answer — one sentence.]

[The supporting evidence or reasoning — 2-3 sentences.]

[The concrete close — a fact, a number, or a commitment.]

**Timing check (aloud):**
- Time spent on the aloud read: [N] seconds (aim 25-30).
- Notes on what to tighten: [one line; usually about a phrase that ran long].

**Mindset tilt:**
[engineer / investor / neutral] — [one sentence on which mindset is most likely to ask this version of the question for our build]
```

Five blocks. About 8-10 minutes per block: 2-3 minutes writing the answer, 30 seconds reading aloud, 1-2 minutes timing, 2-3 minutes tightening.

## The deliverable — bridge sentence

```markdown
## Bridge sentence — fake hard question

**Fake hard question:**
[A question the team did not anticipate. Pick one that is genuinely
adjacent to the build but outside the team's prep. Examples: GDPR
compliance, ADA accessibility, the build's behaviour at 100x scale,
a specific edge case from a user demographic the team didn't target.]

**Bridge sentence (full 25-30 seconds):**

"[Acknowledge the question briefly]
 — [bridge phrase: "what we focused on was" / "the related question
   we did spend time on was" / "the way we think about that family of
   problem is" / "the specific case we built for is"]
 — [pivot to stronger answer the team did prepare]."

**Timing check (aloud):**
- Time spent: [N] seconds.
- Notes: [one line on whether the bridge felt forced or natural].
```

## The deliverable — "I don't know"

```markdown
## "I don't know" — fake genuinely-out-of-scope question

**Fake question:**
[A question the team genuinely does not know the answer to. Pick
one that is clearly outside the team's preparation window — an
academic-research question, a regulatory question, a question
about a specific historical or technical fact the team would not
have looked up.]

**"I don't know" answer (full 15 seconds):**

"I don't know.
 The closest answer I can give is [closest related answer].
 If we had two more weeks, we would investigate [direction]."

**Timing check (aloud):**
- Time spent: [N] seconds (aim 12-18).
- Notes: [one line on whether the answer felt honest or evasive].
```

## Acceptance checklist

- [ ] All five archetype answers are written with the three-beat structure (direct / evidence / close).
- [ ] All five answers' aloud reads are timed and within 20-35 seconds.
- [ ] The bridge sentence uses one of the four bridge phrases verbatim.
- [ ] The "I don't know" answer uses the three-sentence pattern verbatim.
- [ ] Each answer's mindset tilt is named.
- [ ] The committed file is under 300 lines.

## Why this exercise

The Q&A is half the judging slot (Lecture 3 §1). Most teams rehearse the pitch (the 3 minutes) and improvise the Q&A. The improvised Q&A is the most reliable source of low presentation scores in the cohort's collective experience. The exercise converts the improvisation risk into prepared content.

By Saturday's mock Q&A in the mini-project, the team should be able to:
- Hear any of the five archetype questions and produce the 30-second answer in <2 seconds of latency.
- Hear a hard question and produce the bridge sentence in <3 seconds of latency.
- Hear a genuinely-out-of-scope question and produce the "I don't know" answer in <3 seconds of latency.

The latency is the muscle. The exercise warms it.

## A note on what answers are "right"

Two metrics:

- **Honesty.** The answer reflects what the team *actually* did, not what the team *wishes* they had done. The investor-judge specifically scores follow-through honesty; the engineer-judge specifically scores technical honesty.
- **Specificity.** The answer names a specific decision, a specific number, a specific user, a specific competitor — not a generic abstraction. "We talked to 6 FIU CS students" beats "we did some user research."

When scoring yourself against the solutions in [SOLUTIONS.md](./SOLUTIONS.md), the metric is not whether your answers match the sample's wording — your build is different. The metric is whether your answers are *honest* and *specific*.

## Optional — pair-run

If you can pair with a teammate or peer, the Q&A drill becomes a *role-play*: the partner asks the question, you produce the answer aloud, the partner times it and notes the latency. The pair-run is the closest analogue to the mock Q&A in the mini-project; the solo version is the bench, the pair version is the run.

If you pair, log the partner's name and the pair-session timestamp in the committed file.

# Exercise 1 — Write the Hook

**Goal:** Draft three candidate hooks for your Week-3 solo build, run the first-sentence audit on each, pick one, and read all three aloud. By the end of the exercise, you have one committed 30-second hook that names a user and a verb, plus a written record of the two alternatives you cut.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

Lecture 1 §2 said it: the hook is the single most-rewritten beat in any C4 pitch. Most learners write one hook, like it, and ship it — and discover at the recording session that it does not land. The defense is *three* candidate hooks, written before any is rehearsed, and the first-sentence audit run on each one. Three hooks in 15 minutes is the muscle; one hook in 30 minutes is the trap.

The hook is the beat where most pitches fail. Tuesday-you can write the hook calmly; Thursday-you-on-camera cannot.

---

## What to produce

A file at `week-06-prep/exercise-01-hooks.md` (in your `hackathon-template` repo or a new `c4-week-06-prep-<yourhandle>` repo) with:

- A one-line summary of your Week-3 solo build (the prompt sentence and the MUST verb).
- Three candidate 30-second hooks. Each hook is 3 lines: scene, pain, verb-handoff.
- The first-sentence audit run on each hook (does sentence 1 name a user AND a pain?).
- A picked-hook section: which of the three you will record with, and why.
- A "read aloud" note on each hook — what felt awkward, what landed.

---

## Step-by-step

### 1. Re-state your Week-3 build in one line

At the top of `exercise-01-hooks.md`, write the prompt sentence and the MUST verb from your Week-3 solo build:

```
WEEK-3 BUILD UNDER PITCH

Prompt sentence: <one user> can <one verb> to relieve <one pain>.
MUST verb:       <the single most demo-able action on the live URL>
Live URL:        <paste your deploy URL>
```

If your Week-3 build's URL is no longer reachable, note it — and either re-deploy before Thursday or pick a more recent build with a live URL. Exercise 2's recording requires the URL to work; do not start the hook for a build whose URL is dead.

### 2. Draft hook A — the scene-led hook

A scene-led hook opens with a moment in a user's day. Use Lecture 1 §2.2's three-line scaffold:

```
HOOK A — scene-led

Line 1 (8-12 sec): A <specific user> at <specific time> with
  <specific pain>...
Line 2 (8-12 sec): ...and <the cost or missing alternative>.
Line 3 (6-10 sec): <Build name> <does the MUST verb> in <time
  or scale>. Let me show you.
```

Write 3 lines. Read each aloud as you write it. Total spoken time: aim for 25–28 seconds.

### 3. Draft hook B — the cost-led hook

A cost-led hook opens with the cost of the pain, not the scene. Same scaffold, different opener:

```
HOOK B — cost-led

Line 1 (8-12 sec): <Specific number> of <specific user> spend
  <specific time> on <specific friction> every <period>.
Line 2 (8-12 sec): The cost is <specific outcome — missed,
  abandoned, lost>.
Line 3 (6-10 sec): <Build name> <does the MUST verb> in <time
  or scale>. Let me show you.
```

The cost-led opener is harsher than the scene-led opener. It works better for builds where the audience already understands the user.

### 4. Draft hook C — the contrast-led hook

A contrast-led hook opens with the *current* user behavior and contrasts it with the build's verb. Same scaffold, different opener:

```
HOOK C — contrast-led

Line 1 (8-12 sec): Today, a <specific user> who needs <specific
  thing> has to <current friction-heavy alternative>.
Line 2 (8-12 sec): <The friction's cost or absurdity>.
Line 3 (6-10 sec): <Build name> <does the MUST verb> in <time
  or scale>. Let me show you.
```

The contrast-led opener works best when the current alternative is familiar enough that the audience nods immediately ("yeah, that *is* what students do today").

### 5. Run the first-sentence audit on each hook

For each of the three hooks, run the audit from Lecture 1 §2.1:

```
FIRST-SENTENCE AUDIT — Hook <A/B/C>

Q1. Does sentence 1 name a USER?              (yes / no)
Q2. Does sentence 1 name a PAIN?               (yes / no)
Q3. Does sentence 2 (or 3) name the demo VERB? (yes / no)

Three yeses = audit passes. Any no = re-write the line.
```

If a hook fails the audit on any question, re-write the failing line in place. Three rounds of audit + re-write should bring all three hooks to passing.

### 6. Read each hook aloud and time it

Open a timer. Read each hook out loud at a normal pace — not rushed, not slowed. Note the seconds spoken.

```
TIMING + READ-ALOUD NOTE — Hook <A/B/C>

Spoken time: <minutes:seconds>   (target: 25-28 seconds)
What felt awkward: <one sentence on the line that stumbled or
  the word that did not sit right>.
What landed: <one sentence on the strongest moment>.
```

A hook that times to 35 seconds is over the cap and will push the problem beat down. A hook that times to 18 seconds is under the cap and is missing a line — usually the scene-narrowing in line 1.

### 7. Pick one hook for the recording

Pick the hook with:

1. **The strongest first-sentence audit.** If only one of three passes all three audit questions, pick that one.
2. **The most natural read-aloud.** The hook that felt least awkward in step 6 is the hook that will land on take 1.
3. **The clearest verb handoff.** Line 3 should make it obvious what the live URL is about to show. The hook with the clearest handoff is the easiest to record.

Write a 3–5 sentence pick paragraph naming the hook (A, B, or C) and the reasons.

### 8. Write a cut-list for the other two

The two un-picked hooks are not deleted. For each, write a one-sentence note on *why* it was not picked. Common reasons:

- "Hook A's scene was too long; line 1 ran past 12 seconds even after a re-write."
- "Hook B's cost number was hypothetical and the audit's Q2 felt weak."
- "Hook C's contrast worked but the verb handoff in line 3 was vague."

The cut-list is the discipline; the un-picked hooks may be the right pick for a different audience (sponsors vs judges vs internal team), and naming the cut reason makes the re-use possible.

### 9. Commit

```
git add week-06-prep/exercise-01-hooks.md
git commit -m "week 6 exercise 1: three candidate hooks; picked Hook <A/B/C>"
git push
```

---

## Acceptance criteria

- [ ] `week-06-prep/exercise-01-hooks.md` exists in a committed repo.
- [ ] The Week-3 build prompt sentence and live URL are at the top.
- [ ] Three candidate hooks are drafted, each with 3 lines following the scaffold.
- [ ] The first-sentence audit is run on each hook with pass/fail per question.
- [ ] Each hook has a timing note with a real spoken-seconds number.
- [ ] Each hook has a read-aloud note with one specific awkwardness and one specific landing.
- [ ] One hook is picked, with 3–5 sentences naming the choice.
- [ ] The two un-picked hooks have a one-sentence cut-list note each.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Write the verb handoff first.** Line 3 is the easiest to write because it is the most-constrained. Write it for each of the three hooks first, then work backwards to lines 1 and 2.
- **Use the prompt sentence words verbatim when possible.** If your prompt sentence says "freshman," your hook says "freshman" — not "first-year student." Vocabulary consistency makes the hook feel like the same build as the worksheet.
- **Read aloud, not silently.** The hook is delivered out loud, not read on a page. Awkwardness shows up in the mouth, not in the eye. Two minutes of out-loud reading beats ten minutes of silent re-reading.
- **Time it on a phone, not in your head.** Your head estimates 22 seconds for a 30-second hook. The phone timer is the bench.
- **Cut the pitcher's name.** The hook is about the user, not the pitcher. "Hi, my name is Pat" is sentence 0; cut it. If you must credit the team, credit them at the *end* of the hook ("Team: Pat, Sam, Jordan — let me show you").

---

## What to do if all three hooks fail the audit

You have three options:

1. **Re-state the prompt sentence.** Often the audit fails because the prompt sentence itself is vague. Re-write the prompt sentence (Week 5 §6.1) to name a specific user and a specific verb, then re-draft the three hooks against the sharper prompt.
2. **Cut to a smaller user.** "Students" fails the user-naming test because students is a class, not a person. "Freshmen who live alone in a dorm and take intro CS" passes. Cut to the smaller user; the hook tightens.
3. **Re-watch a Week 3 retro out loud.** Read your Week-3 retro aloud. The user you named there is usually a sharper user than the one in your current hook draft. Copy the framing.

If none of these works, the build may be at the wrong stage for a pitch — the build might lack a clear MUST verb. Re-read Lecture 1 §4.1 (the 3-click structure) and confirm the build has 3 demo-able verbs before continuing.

---

## What is next

Move on to [Exercise 2 — Record v1](./exercise-02-record-v1.md), where you record the first three-minute take against the live URL, watch it four times, and write the three notes that drive Friday's re-record.

# Exercise 3 — Cut-List Rehearsal

**Goal:** Pre-write the three named cuts for hour 2, hour 12, and hour 24 against the Campus Quick-Help prompt you scoped in Exercise 2. Read each one aloud. Commit. By the end of the exercise, you have a written cut-list that names specific items, not vague intentions.

**Estimated time:** 60 minutes (15 min reading + 30 min writing + 15 min reading aloud and commit).

---

## Why this exercise exists

Lecture 1 §2 said it: a cut-list with names attached is the difference between an *improvised cut at hour 24* (which produces a wound) and a *pre-agreed cut at hour 0* (which produces a decision). Most learners arrive at hour 24, find a failing MUST, and freeze. The defense is a *pre-written* cut for each of the three predictable moments. Tuesday-you can write the cut calmly; hour-24-you cannot.

Reading the cut-list is not enough. The vocal cords catch the awkwardness that the eyes skip. Two minutes of out-loud read beats ten minutes of silent re-reading. Run the read.

---

## What to produce

A file at `week-05-prep/exercise-03-cut-list.md` with:

- The Campus Quick-Help MoSCoW board from Exercise 2 (re-paste or link to it).
- Three pre-written cut paragraphs, one each for hour 2, hour 12, hour 24.
- A named item in each paragraph — not a vague protocol.
- A one-paragraph reflection on which moment was hardest to write the cut for, and why.
- A note on whether you read each cut aloud, and what was awkward.

---

## Step-by-step

### 1. Re-load the Campus Quick-Help board

Open Exercise 2's `exercise-02-scope-stress.md`. Copy the MUST / SHOULD / COULD / WON'T board into the top of the new file `exercise-03-cut-list.md`. The cut-list references the board's specific items — you cannot write the cuts without the board in front of you.

If you did not do Exercise 2 (you should — do it first), at minimum write a 3-item MUST list and a 4-item WON'T list against the Campus Quick-Help prompt before starting this exercise.

### 2. Write the hour-2 cut

The hour-2 trigger (Lecture 1 §2.2 and Week 4 Lecture 2 §3.1) is "while we're in there" — a teammate proposes a quick add to a card they are already working on. The cut is the *first SHOULD-list item that gets downgraded* if a new add appears.

Use this format:

```
HOUR-2 CUT — "while we're in there"

Triggering shape: a teammate proposes a quick add (~1-2 points)
  on a MUST card they are mid-build.

Pre-written cut: if the add is ≤2 points and serves the target
  demo, it goes to SHOULD as a replacement for <NAMED SHOULD ITEM>.
  If the add is >2 points or does not serve the target demo,
  it goes to WON'T with a one-sentence reason.

Named cut: <the first SHOULD-list item from your Campus Quick-Help
  board that you would downgrade>. Reason this is the right
  downgrade target: <one sentence>.
```

The "named cut" line is the key. "We will cut SHOULD-3 if anyone adds at hour 2" is a decision; "we will cut something from SHOULD" is a vague intention. Name the item.

### 3. Write the hour-12 cut

The hour-12 trigger is "we have time for one more" — MUST appears clean and the team is tempted to promote a SHOULD up to MUST, or a COULD up to SHOULD. The cut is the *first MUST item that does not pass the demo-ability test* (Lecture 2 §3.1) at hour 12.

```
HOUR-12 CUT — "we have time for one more"

Triggering shape: at hour 12, MUST appears clean; team proposes
  promoting a SHOULD or COULD up one column.

Pre-written cut: only allow promotion if the current column is
  fully clickable on the live URL. If MUST is not fully clickable,
  the failing MUST item is cut to SHOULD or WON'T.

Named cut: <the MUST item from your board most likely to fail the
  demo-ability test at hour 12 — typically the one with the most
  moving parts or external dependencies>. Reason this is the right
  candidate: <one sentence>. Where it goes: <SHOULD or WON'T>.
```

The named candidate is your honest assessment of *which* of the three MUSTs is most likely to be the one failing at hour 12. There is always a most-likely candidate; name it.

### 4. Write the hour-24 cut

The hour-24 trigger is "we have to add X or the demo dies" — late-stage demo anxiety produces a request to add a feature that "feels missing." The cut is the *no-additions, only-cuts* rule, plus a named feature that becomes a README paragraph instead of a build.

```
HOUR-24 CUT — "we have to add X or the demo dies"

Triggering shape: at hour 24, a teammate names a feature that
  "feels missing" and proposes building it in the remaining 9 hours.

Pre-written cut: at hour 24, the build window is closed for new
  scope. Any feature that "feels missing" becomes a README paragraph
  or a static fake — not a build. The cut is named in advance.

Named cut: <the feature most likely to be requested at hour 24 —
  typically a feature from your WON'T list that judges might
  expect>. What it becomes instead: <a README paragraph, a static
  image, a hand-coded fake, or a clear "future work" line>.
  Reason this is the right named cut: <one sentence>.
```

The hour-24 cut is the hardest of the three because it requires predicting late-stage anxiety. The two most common: auth ("but how do we show login?") and notifications ("but how do they get reminded?"). Pick one; write the cut.

### 5. Read each cut aloud

Set a quiet 2 minutes. Read each cut paragraph aloud. Note what is awkward. Common awkwardness:

- The "named cut" feels arbitrary ("why this SHOULD item and not the other?"). That is fine — the act of naming is what matters; the choice can shift event-to-event.
- The pre-written cut feels prescriptive ("we cannot possibly know what the team will need"). That is also fine — the script is a *default*, not a contract. The team can override; the default exists so the override is *deliberate*.
- The hour-24 cut feels brutal. It is brutal. That is the point.

Write a 2–4 sentence note on what was awkward in each read.

### 6. Reflect on the hardest cut

Below the three cuts, write a 4–6 sentence reflection on:

- Which cut was hardest to write, and why.
- Which named cut you are least confident about (and which event-specific data would sharpen it).
- One past project — not necessarily a hackathon — where pre-writing a cut at the equivalent of hour 12 or hour 24 would have helped.

This last bullet is the muscle. The cut-list is not just a hackathon skill; it transfers to any time-boxed project.

### 7. Commit

```
git add week-05-prep/exercise-03-cut-list.md
git commit -m "week 5 exercise 3: pre-written cut-list, hours 2/12/24"
git push
```

---

## Acceptance criteria

- [ ] `week-05-prep/exercise-03-cut-list.md` exists in a committed repo.
- [ ] The Campus Quick-Help MoSCoW board is at the top (re-pasted or linked).
- [ ] Three cut paragraphs, one each for hour 2, hour 12, hour 24.
- [ ] Each cut paragraph names a *specific item* from the board (not a vague intention).
- [ ] Each cut paragraph has a one-sentence reason for the named choice.
- [ ] The aloud-read note is present, with at least one specific awkwardness per cut.
- [ ] The reflection paragraph names a past non-hackathon project where pre-writing a cut would have helped.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Pick the most-painful item to name as the cut.** The cut you would not want to make is the cut most likely to be the right one. The pain is the signal.
- **The hour-24 "becomes a README paragraph" is the gold pattern.** Most "must-add" features at hour 24 can be solved with one paragraph in the README that names the future work. The judge sees the paragraph; the team saves 8 hours of build.
- **Reference the contract's "no" script.** The hour-2 cut is also the moment when Week 4's three-sentence "no" script runs. The two artifacts thread together. If the cut-list cannot reference the contract, one of the two is incomplete.
- **Cite your specific MUST items by their position in the board.** "MUST-2 (the matching algorithm)" is sharper than "the matching algorithm." Position-naming makes the cut-list a *protocol*, not a paragraph.

---

## What to do if you cannot pick the named cut

You have three options:

1. **Pick the largest item in the relevant column.** Largest in points, largest in surface area, largest in moving parts. Largest is usually the right candidate.
2. **Pick the item with the most external dependencies.** External APIs, third-party auth, payment gateways, anything that can be down for reasons outside the team's control. External dependencies fail at the worst time.
3. **Pick the item the team is least excited about.** The team's energy is a real signal. The item nobody wants to build is the item most likely to fail the demo-ability test. Cut it preemptively.

If all three feel arbitrary, the issue is not the choice — the issue is the worksheet's MUST list is too vague. Re-read Lecture 1 §5.1 (the MUST definition tests) and tighten the MUST list. Then re-name the cut.

---

## What is next

Saturday: draft the [mini-project — 36-hour scoping worksheet](../mini-project/README.md). The three exercises feed into the worksheet: Exercise 1's audit informs the demo-ability checklist section, Exercise 2's pass informs the MoSCoW board section, Exercise 3's cut-list informs the bottom-half cut-list section. The worksheet is the artifact that holds all three.

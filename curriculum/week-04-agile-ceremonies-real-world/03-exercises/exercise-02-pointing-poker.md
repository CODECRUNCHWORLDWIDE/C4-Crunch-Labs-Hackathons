# Exercise 2 — Planning-Poker Round

**Goal:** Point a 10-item backlog using the 1-2-3-5 scale, in 10 minutes, against a real clock. By the end of the exercise, you have a committed pointing log and a one-paragraph note on where the round was hardest.

**Estimated time:** 60 minutes (15 min reading + 10 min round + 35 min notes and commit).

---

## Why this exercise exists

Lecture 2 §2 said it: 10 items in 10 minutes is the C4 pointing pace. Most learners run their first planning-poker round at the real event, take 30 minutes on 5 items, and produce a backlog half-pointed and a team half-frustrated. The defense is a *practiced* round, run alone against a timer (or with a partner), before the event. The skill is the 50-second-per-item cadence; the cadence is built by reps, not by reading.

---

## What to produce

A file at `week-04-prep/exercise-02-pointing.md` with:

- The 10-item backlog (use the one provided below, or substitute your own).
- Your point estimate for each item (1, 2, 3, 5, or ?).
- A one-sentence rationale per item (what you compared it to).
- A note on the time you got for the full round (target: 10 minutes; acceptable: 8–12).
- A one-paragraph note on which item was hardest to point and why.

---

## Step-by-step

### 1. Use the provided backlog

This backlog is a fictional study-buddy matcher MVP. Use it as-is for the round. (If you want to do a second round later with your own backlog, fine — but commit the first round on this one for comparability with cohort-mates.)

```
THE FAKE BACKLOG — STUDY-BUDDY MATCHER

 1. Email signup form (no password reset)
 2. Profile page with name, year, three subjects
 3. "Find a buddy" button on the profile page
 4. Matching algorithm: same-subject, opposite year
 5. Match results page with three suggested buddies
 6. Send a "study request" to a matched buddy (one-way)
 7. Notification when you receive a study request
 8. Calendar view of accepted study sessions
 9. Light/dark theme toggle in the navbar
10. Email digest of new matches every Friday morning
```

Ten items, ranging from a clear 1 to a probable 5 or "?". Do not pre-rank them; point each one in order.

### 2. Set the timer and run the round

Set a phone timer for 10 minutes. Open `exercise-02-pointing.md`. For each item, in order:

- Read the item aloud (5 sec).
- Think silently (15 sec).
- Decide your point (1, 2, 3, 5, ?). Write it in the file (5 sec).
- Write your one-sentence rationale (15 sec). Keep it short — "same size as item 2," or "needs a new DB table, like item 8."
- Move on (5 sec).

Target: 45–55 seconds per item, 7.5–9 minutes total. Cap: 10 minutes hard.

If you blow through 10 minutes, *stop pointing* and write "?" for the remaining items. Note in the file how many you ran out of time on. Honesty here is more valuable than completionism.

### 3. Identify the hardest item

After the round, write a one-paragraph note (3–5 sentences) on:

- Which item was hardest to point, and why.
- What you compared it to.
- Whether a teammate-disagreement would have surfaced on that item.

The hardest item is usually one of: item 4 (matching algorithm — unknown complexity), item 7 (notifications — depends on stack), or item 10 (email digest — sounds simple but needs a cron and an email service).

### 4. Reflect on the calibration

Below the note, write one sentence answering: **what does "1 point" mean in this round's vocabulary?** Look at the 1s you assigned. Is the smallest item really 1, or is it actually a 2? Calibrating downward is normal; the round taught you what "1" really means for your hand.

### 5. Commit

```
git add week-04-prep/exercise-02-pointing.md
git commit -m "week 4 exercise 2: pointing-poker round, 10 items"
git push
```

---

## Acceptance criteria

- [ ] `week-04-prep/exercise-02-pointing.md` exists in a committed repo.
- [ ] All 10 items have a point estimate (1, 2, 3, 5, or ?) and a one-sentence rationale.
- [ ] The time-of-round note is present, with a real number in minutes.
- [ ] No item is pointed above 5. If you wrote 8 or 13, change it to "?" and split the card (Lecture 2 §1.2).
- [ ] The "hardest item" paragraph is 3–5 sentences and names a specific item by number.
- [ ] The calibration sentence on "what 1 point means" is present.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Compare to other items in the same backlog.** "Item 9 is 1 because it's the same size as item 3" is a calibrated point. "Item 9 is 1 because it feels small" is not.
- **Use "?" generously on first read.** A "?" is not a failure; it is a flag for "this needs a 30-second discussion or a card-split." Expect at least one "?" per round.
- **Do not look up answers.** This exercise has no correct answers. The skill is the cadence and the comparison, not the final number.
- **If item N takes more than 90 seconds, force a "?" and move on.** Better to flag two items as "?" than to blow the 10-minute cap on one card.

---

## What to do if 10 minutes is not enough

You have three options:

1. **Run it again, slower.** First rounds are slow. The second round on the same backlog is usually 60–70% of the first round's time. Run round 2 on a different day; commit both rounds and note the speedup.
2. **Cut the discussion budget.** If you spent 90 seconds rationalizing each item, that is your bottleneck. Cap the rationale at one short sentence. Move on.
3. **Realize the scale is too fine.** If five items keep coming up as 2.5 and you cannot decide between 2 and 3, the 1-2-3-5 scale is too coarse for your hand right now — that is fine, force-pick the nearer number, and note it.

---

## What is next

Move on to [Exercise 3 — The "saying no" script](./exercise-03-saying-no-script.md), where you write your three-sentence "no" for each of the three scope-creep shapes.

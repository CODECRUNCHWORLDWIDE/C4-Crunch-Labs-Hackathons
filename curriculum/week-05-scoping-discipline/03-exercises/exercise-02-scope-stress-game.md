# Exercise 2 — Scope Stress Game

**Goal:** Run a 20-minute MoSCoW pass on a fake event prompt, against a real clock, and force the MUST list to exactly 3 items. By the end of the exercise, you have a committed four-column board with a 3-item MUST and a 4+ item WON'T — the C4 default proportions.

**Estimated time:** 60 minutes (15 min reading + 20 min pass + 25 min commit and reflection).

---

## Why this exercise exists

Lecture 1 §1.4 said it: the 20-minute MoSCoW pass at hour 0 is the C4 scoping default. Most learners run their first pass at the real event, take 45 minutes, end up with a MUST list of 5 items, and a WON'T list of 1 item — and pay for both at hour 24. The defense is a *practiced* pass, run alone against a timer (or with a partner), before the event. The cap on MUST is the muscle; the muscle is built by reps, not by reading.

The "stress" in the title is the timer. Twenty minutes is short on purpose. The pressure forces real cuts.

---

## What to produce

A file at `week-05-prep/exercise-02-scope-stress.md` with:

- A fake event prompt (use the one provided below, or substitute your own).
- The four-column MoSCoW board with 12–16 items total, 3-item MUST cap, 4+ item WON'T.
- One-sentence reasons on every WON'T item.
- A note on the time you got for the full pass (target: 20 min; acceptable: 15–25).
- A one-paragraph reflection on which item was hardest to place, and why.

---

## Step-by-step

### 1. Use the provided fake prompt

This prompt is a fictional 36-hour hackathon brief. Use it as-is for the pass. (If you want to do a second pass later with your own prompt, fine — but commit the first one on this prompt for comparability with cohort-mates.)

```
FAKE EVENT PROMPT — "CAMPUS QUICK-HELP"

A 36-hour hackathon for a campus tool that lets students ask quick
help questions (homework, schedules, mental-health office hours) and
get a same-day reply from a peer or staff member. Target demo: a
freshman on a phone, signed up in 60 seconds, posting a question and
getting one peer reply visible in under 3 minutes of demo time.

Constraints:
- 36-hour build window.
- Free tier deploy only (Vercel + Supabase free, or equivalent).
- Team of 4. One frontend, one backend, one design/PM, one floater.
- Judges open the demo URL on phones first.
```

The prompt is rich enough to invite 30 candidate items. Your job is to cut to 12–16.

### 2. Set the timer and run the 20-minute pass

Set a phone timer for 20 minutes. Open `exercise-02-scope-stress.md`. Run the five-step pass from Lecture 1 §1.4:

```
Min  0 — 3   Brainstorm 6+ candidate items, by yourself, on the
             fake prompt. No filtering. ~6 items minimum.
Min  3 — 8   Cluster: group obvious duplicates. Aim for 12–16
             unique items in your list.
Min  8 —15   Sort: place each item into MUST / SHOULD / COULD /
             WON'T. Force-pick if uncertain.
Min 15 —18   Cut: MUST > 3? Force-cut to 3. WON'T < 4? Add the
             cuts as WON'T items with one-sentence reasons.
Min 18 —20   Commit: write the four-column board to the file in
             the format below.
```

The hard parts are minutes 15–18 (the forcing) and minutes 18–20 (the writing without drift).

### 3. Format the board in the file

Use this format. Each WON'T item gets a one-sentence reason — that is the C4 voice's requirement, and Lecture 1 §5.4 explains why.

```
SCOPING PASS — Campus Quick-Help
Pass time: <minutes:seconds>
Total items: <number>

MUST (3 items max — what ships or the demo dies):
  1. <one-phrase item>
  2. <one-phrase item>
  3. <one-phrase item>

SHOULD (2-3 items — ships if MUST is clean by hour 24):
  - <item>
  - <item>

COULD (1-2 items — almost never ships):
  - <item>

WON'T (4+ items — does not ship; reason required):
  - <item> — <one-sentence reason>
  - <item> — <one-sentence reason>
  - <item> — <one-sentence reason>
  - <item> — <one-sentence reason>
```

If you finish at 18 minutes with one MUST and a panic at the cap, that is fine — note it in the time field. If you finish at 30 minutes, also fine — note it. Honesty is more valuable than completionism.

### 4. Identify the hardest item to place

After the pass, write a 4–6 sentence note on:

- Which item was hardest to place (MUST vs SHOULD vs WON'T) and why.
- What you compared it to in deciding.
- Whether a teammate-disagreement would have surfaced on that item.

The hardest item is usually one of: a "signup flow" (MUST or SHOULD?), a "search across questions" (SHOULD or WON'T?), or a "real-time chat" (WON'T or COULD?). Each is a meaningful judgment; name yours.

### 5. Test against the four failure modes

Below the hardest-item paragraph, check your board against the four failure modes from Lecture 1 §4:

```
FAILURE MODE CHECK

- MUST-of-five:        MUST has 3 items. Pass / Fail (note if fail)
- Empty WON'T:         WON'T has 4+ items with reasons. Pass / Fail
- Aspirational COULD:  COULD has ≤2 items, both honestly possible. Pass / Fail
- Verbal-only MoSCoW:  All four columns are in this committed file. Pass / Fail
```

A failing failure-mode check is fine — you noted it, you committed it, you can fix it on the next pass. The check itself is the discipline.

### 6. Commit

```
git add week-05-prep/exercise-02-scope-stress.md
git commit -m "week 5 exercise 2: 20-min MoSCoW pass on Campus Quick-Help prompt"
git push
```

---

## Acceptance criteria

- [ ] `week-05-prep/exercise-02-scope-stress.md` exists in a committed repo.
- [ ] The fake event prompt is at the top.
- [ ] The four columns each have items in the C4 ratios (MUST = 3, SHOULD = 2–3, COULD = 1–2, WON'T = 4+).
- [ ] Every WON'T item has a one-sentence reason.
- [ ] The time-of-pass note is present, with a real number in minutes:seconds.
- [ ] The hardest-item paragraph is 4–6 sentences and names a specific item.
- [ ] The four failure-mode check is present with pass/fail per mode.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Force MUST to exactly 3. Not 4. Not "3 plus a tiny one."** The cap is the discipline. If you cannot cut to 3, you have not yet faced the refusal — re-read Lecture 1 §1.3 (WON'T is the most-important column) and try again.
- **Write WON'T reasons in the voice of the next event.** "WON'T: real-time chat — last event we tried sockets and ate 8 hours" is gold for future reuse. "WON'T: real-time chat — too hard" is not.
- **Use the prompt's *specific* phrases.** "Freshman on a phone" is in the prompt; your MUST list should reflect "mobile-clickable" not just "responsive." The prompt is the third party that holds the line.
- **Do not pre-rank the items before sorting.** Each item gets placed once. If you find yourself rearranging the list at minute 15, you are blurring the columns. Force-pick and move on.
- **Time-box ruthlessly.** If you blow 20 minutes, *stop the pass* and write the failure as a finding. A 25-minute pass with a "I blew it by 5" note is more valuable than a 35-minute pass without one.

---

## What to do if MUST keeps wanting to be 5

You have three options, in order:

1. **Combine two MUST items into one.** "Signup + posting a question" combines into "first-question flow." That is one MUST verb, one demo beat, one card. Re-read Lecture 1 §5.1 (the stranger test).
2. **Cut the smallest MUST to SHOULD.** The item you can live without is in SHOULD, not MUST. The pain of the cut is the discipline.
3. **Re-read the prompt's "target demo" line and grade each MUST against it.** Items that do not serve the target-demo sentence are not MUSTs; they are SHOULDs. The prompt is the bench.

If none of these works, you may have an over-rich prompt. Note it in the reflection. Some real prompts will need a MUST of 2 in 36 hours.

---

## What is next

Move on to [Exercise 3 — Cut-list rehearsal](./exercise-03-cut-list-rehearsal.md), where you pre-write the three named cuts for hour 2, hour 12, and hour 24 against the same fake prompt you just scoped.

# Week 5 Homework

Six practice problems that revisit the week's topics. The full set should take about **2 hours** in total. Work in your `week-05-prep` folder (or the build repo, where the prompt says) so each problem produces at least one commit you can point to later.

Each problem includes:

- A short **problem statement**.
- **Acceptance criteria** so you know when you are done.
- A **hint** if you get stuck.
- An **estimated time**.

The homework is meant to be done *around* the exercises and the mini-project. Most problems pair naturally with a specific lecture section; the order below mirrors the order you encountered the material.

---

## Problem 1 — Rewrite a bad MUST list

**Problem statement.** Take this deliberately bad MUST list for a 36-hour hackathon: *"MUST: signup, profile pages, matching algorithm, real-time chat, leaderboard, light/dark theme, email digest, mobile-friendly landing page."* Rewrite it as a C4-compliant MUST + SHOULD + COULD + WON'T board with the correct item-count caps (MUST = 3, WON'T ≥ 4). For each item that moves to a non-MUST column, write a one-sentence reason.

**Acceptance criteria.**

- File at `week-05-prep/homework-01.md`.
- The original bad MUST list is at the top.
- The rewritten four-column board has MUST = 3, WON'T ≥ 4, each WON'T item with a one-sentence reason.
- Each demoted item has a justification (which column, why).
- Voice is team-room; no banned voice.
- Committed.

**Hint.** The bad list is bad on three axes: too many MUSTs, no WON'Ts, no reasoning. Fix each in turn. The fix is what produces a C4 worksheet.

**Estimated time.** 15 minutes.

---

## Problem 2 — The "MoSCoW failure mode" diagnosis drill

**Problem statement.** Below are four hackathon scoping scenarios. For each, name which of the four MoSCoW failure modes (Lecture 1 §4) is happening, and write the one-sentence fix.

1. The team finishes the scoping pass with a MUST list of 6 items. "We can do all of them — we're fast."
2. The team's worksheet has 0 items in WON'T. "We don't want to write anything off yet."
3. The team's COULD column has 5 items. Each one is "if we have time."
4. The team talked through scope for 20 minutes; the worksheet file is empty.

**Acceptance criteria.**

- File at `week-05-prep/homework-02.md`.
- Each scenario is reproduced.
- Each scenario is diagnosed with the named failure mode.
- Each scenario has a one-sentence fix.
- No banned voice.
- Committed.

**Hint.** The fixes are mostly *systemic*: re-read the four MoSCoW failure modes in Lecture 1 §4 and the test for each. The fix is rarely "be better"; it is almost always "force the cap / require the reason / commit the file."

**Estimated time.** 15 minutes.

---

## Problem 3 — A second MoSCoW pass on a new prompt

**Problem statement.** Run a second 20-minute MoSCoW pass on a *new* fake prompt — not the Campus Quick-Help prompt from Exercise 2. Use one of the three prompts below, or write your own. Same five-step pass (Lecture 1 §1.4), same four-column board, same 3-item MUST cap and 4+ item WON'T.

```
PROMPT A — "DorMate"
A 36-hour build for a dorm-room roommate matching tool for incoming
freshmen. Target demo: a freshman fills a 4-question profile and
sees three candidate matches.

PROMPT B — "TextbookSwap"
A 36-hour build for a campus textbook-trading platform. Target
demo: a learner lists a book and sees a buyer's contact info.

PROMPT C — "Office Hours Finder"
A 36-hour build for a real-time office-hours finder. Target demo:
a learner opens the URL and sees which professors are currently in
office hours, with a knock-on-the-door style "I'm coming" button.
```

**Acceptance criteria.**

- File at `week-05-prep/homework-03.md`.
- The prompt is at the top.
- The four-column board with the C4 ratios (MUST = 3, SHOULD = 2–3, COULD = 1–2, WON'T = 4+).
- One-sentence reasons on every WON'T item.
- The time of the pass is noted.
- A one-sentence comparison to your Exercise 2 pass time is present.
- Committed.

**Hint.** The second pass should be faster than the first. If it is not, you are over-rationalizing — cap the brainstorm and force the cuts.

**Estimated time.** 25 minutes.

---

## Problem 4 — Run the pre-event walk-through

**Problem statement.** Run the 30-minute pre-event walk-through (Lecture 2 §2) on your `hackathon-template` repo from Week 2. The walk-through has five steps; commit the findings.

**Acceptance criteria.**

- File at `week-05-prep/homework-04.md`.
- The walk-through follows the five-step structure: clone fresh, confirm live URL, click through seeded paths, incognito pass, write findings.
- 3 gaps are named (1 sentence each).
- Each gap has a one-sentence proposed fix.
- The "incognito pass" is run on a fresh browser session (note this in the file).
- If your `hackathon-template`'s live URL is broken: that *is* the first gap. Note it; propose the fix.
- Committed.

**Hint.** The most-common gaps: a seeded record missing on prod, a CORS error on a form, a slow first-paint on cold cache. If you find zero gaps, you did not run the walk-through honestly — try again on a phone.

**Estimated time.** 30 minutes.

---

## Problem 5 — Reverse-engineer three public hackathon READMEs

**Problem statement.** Find three pieces of writing about real hackathon submissions — not the C4 lectures, not generic Agile pages. Sources, in order of preference: (a) Devpost submissions from past major events (MLH, TreeHacks, HackMIT), (b) any GitHub repo with a `hackathon` topic that has a thoughtful README, (c) C4's `SPRING-2025/` archive in this repo. For each, write a 50-word "reverse-engineered MoSCoW" — what you can infer about the team's MUST, SHOULD, and WON'T from the README alone.

**Acceptance criteria.**

- File at `week-05-prep/homework-05.md`.
- 150–250 words total across the three submissions.
- Three sources are named (URLs).
- For each: an inferred MUST (1 item), an inferred SHOULD (1–2 items), an inferred WON'T (1–2 items, often from the "future work" section).
- One sentence per source on *which* of those three inferences was hardest to make from the README and why.
- A closing sentence: which one of the three READMEs you would steal a pattern from for your own worksheet, and which pattern.
- No banned voice.
- Committed.

**Hint.** The most useful reads are short README files by working teams, not consulting-firm whitepapers. Look for an explicit "future work" or "not in scope" section — those are gold for inferring WON'T.

**Estimated time.** 25 minutes.

---

## Problem 6 — The worksheet-section pre-write

**Problem statement.** Before the Saturday mini-project session, pre-write three of the five worksheet sections in rough draft form. Pick from: section 2 (MoSCoW board defaults — e.g., what items appear in WON'T for *every* hackathon), section 3 (points budget format), section 4 (cut-list defaults at hour 2 / 12 / 24), section 5 (demo-ability checklist defaults). Section 1 (the prompt sentence) is event-specific; do not pre-write it. The point is to arrive at Saturday with three sections already drafted, so the mini-project session is editing and polishing, not drafting from scratch.

**Acceptance criteria.**

- File at `week-05-prep/homework-06.md`.
- Three worksheet sections drafted, each clearly labeled with its section number from the mini-project README.
- Each section is 3–8 lines of prose or a structured block (table, bulleted list).
- Each section is *yours* — written in your voice, not copy-pasted from the lectures.
- Committed by Friday night.

**Hint.** The easiest sections to pre-write are 4 (cut-list defaults, drawn from Exercise 3) and 5 (demo-ability checklist, drawn from Lecture 2 §3.1). Section 2's defaults (what *always* lives in WON'T) is the most personal and the most useful to commit early.

**Estimated time.** 20 minutes.

---

## Time budget recap

| Problem | Estimated time |
|--------:|---------------:|
| 1 | 15 min |
| 2 | 15 min |
| 3 | 25 min |
| 4 | 30 min |
| 5 | 25 min |
| 6 | 20 min |
| **Total** | **~2 hours 10 min** |

If your time is strict, drop Problems 3 and 5. Keep 1, 2, 4, and 6 — those are the muscles the worksheet itself relies on. Problem 4 (the walk-through) is the single most valuable problem of the week; do not skip it.

When you have finished, push your repo and finalize the [mini-project](./mini-project/README.md) — the one-page 36-hour scoping worksheet template.

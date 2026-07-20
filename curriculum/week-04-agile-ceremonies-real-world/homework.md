# Week 4 Homework

Six practice problems that revisit the week's topics. The full set should take about **2 hours** in total. Work in your `week-04-prep` folder (or the build repo, where the prompt says) so each problem produces at least one commit you can point to later.

Each problem includes:

- A short **problem statement**.
- **Acceptance criteria** so you know when you are done.
- A **hint** if you get stuck.
- An **estimated time**.

The homework is meant to be done *around* the exercises and the mini-project. Most problems pair naturally with a specific lecture section; the order below mirrors the order you encountered the material.

---

## Problem 1 — Rewrite a bad stand-up update

**Problem statement.** Take this deliberately bad stand-up update: *"Yesterday I worked on a few things — the API, mostly, and some bug fixes here and there. Today I'm going to keep going on the API and start the frontend if I have time. No blockers really, just busy."* Rewrite it into a 60-second-compatible four-question update from Lecture 1 §2.1. Be honest about the blocker.

**Acceptance criteria.**

- File at `week-04-prep/homework-01.md`.
- The original bad update is at the top.
- The rewritten update follows the four-question format (shipped / next / blocker, plus the team Q4 line).
- Each line is one phrase, no filler.
- The blocker line is a real blocker (you may invent a plausible one for the fake-context).
- Committed.

**Hint.** The bad update is bad on three axes: vague ("a few things"), filler-heavy ("here and there"), and dishonest about blockers ("no blockers really"). Fix each in turn. The fix is what produces a 60-second-compatible update.

**Estimated time.** 15 minutes.

---

## Problem 2 — The "ceremony failure mode" diagnosis drill

**Problem statement.** Below are four hackathon scenarios. For each, name which of the four ceremony failure modes (Lecture 1 §5 + Lecture 2 §2.2) is happening, and write the one-sentence fix.

1. The team's hour-12 stand-up takes 9 minutes. Everyone reports status; no one asks anyone else a question.
2. The team's hour-24 internal demo ends with applause and the phrase "let's keep going as-is."
3. The team's retro contains the sentence "Pat broke the deploy at hour 20."
4. A teammate says "you said this was 3 points and it took all day."

**Acceptance criteria.**

- File at `week-04-prep/homework-02.md`.
- Each scenario is reproduced.
- Each scenario is diagnosed with the named failure mode.
- Each scenario has a one-sentence fix.
- No banned voice.
- Committed.

**Hint.** The fixes are mostly *systemic*: re-read the four-question stand-up format, the cut-or-keep call, the blameless-translation table, the points-vs-hours language test. The fix is rarely "be better"; it is almost always "use the format / the test / the script."

**Estimated time.** 20 minutes.

---

## Problem 3 — A second pointing round on a new backlog

**Problem statement.** Run a second planning-poker round on a new fake backlog — not the one from Exercise 2. Use a 10-item backlog of your own invention (or steal one from a public GitHub repo's Issues). Point each item on the 1-2-3-5 scale, time the round at 10 minutes, and compare your speed against your Exercise 2 time.

**Acceptance criteria.**

- File at `week-04-prep/homework-03.md`.
- The 10-item backlog is listed.
- Each item has a point and a one-sentence rationale.
- The round time is noted.
- A one-sentence comparison to your Exercise 2 round time is present.
- No item is pointed above 5.
- Committed.

**Hint.** The second round should be faster than the first. If it is not, you are over-rationalizing — cap the rationale at one short phrase and force the cadence.

**Estimated time.** 20 minutes.

---

## Problem 4 — The "yes-with-cut" rewrite

**Problem statement.** Take these three scope-addition requests and write the "yes, with an equal-points cut" response from Lecture 2 §3.5 for each:

1. (Hour 2) "Let me add a profile picture upload — it's quick."
2. (Hour 12) "We have time for a real-time chat between matched users."
3. (Hour 24) "We have to add email notifications or the demo won't feel real."

For each, you must (a) point the new ask (1, 2, 3, or 5), (b) name a same-points cut from MUST, (c) write the response sentence.

**Acceptance criteria.**

- File at `week-04-prep/homework-04.md`.
- Each scope-addition request is reproduced.
- Each has a point estimate for the new ask.
- Each has a named same-points cut from MUST.
- Each has the one-sentence "yes-with-cut" response.
- Voice is team-room. Refusals reference the contract, not personal preference.
- Committed.

**Hint.** The "yes with cut" is harder than the flat "no" because you have to know the MUST list well enough to name a same-points cut. If you cannot name a cut, the scope-addition is a flat "no" — write it that way and note the difference.

**Estimated time.** 20 minutes.

---

## Problem 5 — Read three real Agile-ceremony posts

**Problem statement.** Find three pieces of writing about real Agile ceremonies — not the C4 lectures, not Atlassian's pages. Sources, in order of preference: (a) Martin Fowler's "It's not just standing up", (b) any working developer's blog post on retros, (c) any public GitHub team's `WAYS-OF-WORKING.md` or equivalent. Write a 150–250 word summary at `week-04-prep/homework-05.md` covering: one practice that appeared in two or more pieces, one practice unique to one piece, and one practice you are adopting for your team contract.

**Acceptance criteria.**

- File at `week-04-prep/homework-05.md`.
- 150–250 words.
- Three sources are named (URLs or repo paths).
- The "one practice I am adopting" line is specific and references which contract section it goes into.
- No banned voice.
- Committed.

**Hint.** The most useful reads are short blog posts by working developers, not consulting-firm whitepapers. The C4 voice is closer to a developer's blog than to a corporate Agile playbook for a reason.

**Estimated time.** 25 minutes.

---

## Problem 6 — The contract-section pre-write

**Problem statement.** Before the Saturday mini-project session, pre-write three of the eight contract sections in rough draft form. Pick from: section 2 (stand-up format), section 3 (cut decision protocol), section 4 (internal demo schedule), section 6 (story-pointing scale), section 7 ("saying no" script), section 8 (conflict-de-escalation). The point is to arrive at Saturday with three sections already drafted, so the mini-project session is editing and polishing, not drafting from scratch.

**Acceptance criteria.**

- File at `week-04-prep/homework-06.md`.
- Three contract sections drafted, each clearly labeled with its section number from the mini-project README.
- Each section is 3–8 lines of prose or a structured block (table, bulleted list).
- Each section is *yours* — written in your voice, not copy-pasted from the lectures.
- Committed by Friday night.

**Hint.** The easiest sections to pre-write are 6 (pointing scale, mostly the C4 default) and 7 ("no" script, drawn from Exercise 3). Section 8 (conflict de-escalation) is the hardest because the lectures only sketched it — that is fine, draft what you can, refine on Saturday.

**Estimated time.** 25 minutes.

---

## Time budget recap

| Problem | Estimated time |
|--------:|---------------:|
| 1 | 15 min |
| 2 | 20 min |
| 3 | 20 min |
| 4 | 20 min |
| 5 | 25 min |
| 6 | 25 min |
| **Total** | **~2 hours** |

If your time is strict, drop Problems 3 and 5. Keep 1, 2, 4, and 6 — those are the muscles the contract itself relies on.

When you have finished, push your repo and finalize the [mini-project](./mini-project/README.md) — the one-page team contract template.

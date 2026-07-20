# Week 1 Homework

Six practice problems that revisit the week's topics. The full set should take about **2 hours** in total — much shorter than later weeks, because Week 1 is the mental-model week. Work in your Week 1 Git repository so each problem produces at least one commit you can point to later.

Each problem includes:

- A short **problem statement**.
- **Acceptance criteria** so you know when you're done.
- A **hint** if you get stuck.
- An **estimated time**.

---

## Problem 1 — Research one real upcoming hackathon you could attend

**Problem statement.** Pick one real, public hackathon that takes place within the next 6 months and that you could plausibly attend (in person or virtual). It must be a real listed event — MLH-affiliated, Devpost-listed, college, sponsor, or themed.

Write a short brief at `notes/event-research.md` covering:

- **Event name, dates, format** (24h / 36h / 48h / week-long; in-person / virtual / hybrid).
- **Where you found it** (URL).
- **The judging rubric they publish** (or "no rubric published" if they do not).
- **Three sponsor prizes you could plausibly target**, each with a one-sentence reason.
- **Two reasons you would attend.**
- **One reason you might not.**

**Acceptance criteria.**

- File at `notes/event-research.md`.
- All seven bullets above are present.
- The event is real and the link works at the time of writing.
- Committed.

**Hint.** Start at <https://mlh.io/seasons> for college hackathons, or <https://devpost.com/hackathons> for everything else. Filter by location or "online."

**Estimated time.** 25 minutes.

---

## Problem 2 — Draw a MoSCoW chart for an invented prompt

**Problem statement.** Imagine a 36-hour hackathon with the theme *"a tool that helps a small group of people coordinate something."* You have a four-person team (two builders, one designer/pitch-lead, one PM/scope-keeper).

Draw a MoSCoW chart for a project of your invention. Save it at `notes/invented-moscow.md`. Follow the C4 rules:

- MUSTs cap at three.
- Every MUST is annotated with its 30-second demo moment.
- The WON'T column has at least three items, named explicitly.
- A deploy URL is one of the MUSTs.

**Acceptance criteria.**

- File at `notes/invented-moscow.md`.
- Project name and one-sentence description at the top.
- The chart renders as a code block (ASCII), matching the C4 brand-book style.
- Three MUSTs, no more. Each annotated with a demo moment.
- At least three WON'Ts.
- A deploy URL appears as a MUST.
- Committed.

**Hint.** Look at the worked example in [Lecture 2 §8](./lecture-notes/02-the-12-hour-rule-and-demo-or-die.md) for shape. Do not copy the example; invent.

**Estimated time.** 20 minutes.

---

## Problem 3 — Simulate a 12-hour stand-up on paper

**Problem statement.** Using the MoSCoW chart you drew in Problem 2, simulate the 12-hour stand-up. Write it as a short script at `notes/stand-up-simulation.md`.

The script must include:

- Each of the four imagined teammates' two-minute updates (what they shipped, what is blocked, what is next).
- The PM reading the chart out loud and identifying status per item.
- The PM applying the 12-hour rule: is remaining work ≤ 70% of remaining time?
- An actual cut — at least one item moves from MUST or SHOULD down to WON'T, with a one-sentence reason.
- The new chart at the bottom of the file, post-cut.

**Acceptance criteria.**

- File at `notes/stand-up-simulation.md`.
- Four teammate updates, each with three sub-points.
- A PM section that applies the 12-hour rule with a visible calculation.
- A real cut is named, with a reason.
- The post-cut chart is rendered at the end.
- Committed.

**Hint.** Make the teammates a bit messy. One is behind on a MUST, one is over-engineered on a SHOULD, one has not started the deploy. Real teams look like this.

**Estimated time.** 25 minutes.

---

## Problem 4 — Rate one project from the Code Crunch archive

**Problem statement.** Open the [`SPRING-2025/`](../../SPRING-2025/) folder of this repository (or a later archived Code Crunch event if one exists). Pick one project — any one. Score it against the four-axis rubric.

Write the scoring at `notes/code-crunch-archive-rating.md` using the same format as Exercise 2.

**Acceptance criteria.**

- File at `notes/code-crunch-archive-rating.md`.
- One project named, with the path to it inside the archive.
- Four scores (1–5) plus a total out of 20.
- A two-to-three sentence "my read" paragraph.
- Committed.

**Hint.** If the archive is sparse at the moment you do this homework (Spring 2025 is the first archived event), pick any submission file you can find and score it as best you can. If the archive is genuinely empty, score a project from a *past* event hosted by your own club or university instead, and note the substitution at the top of the file.

**Estimated time.** 15 minutes.

---

## Problem 5 — Write a 200-word "anti-pattern" essay

**Problem statement.** Write a short essay at `notes/anti-pattern-essay.md` (200–250 words) on **one** hackathon anti-pattern you have either witnessed or could imagine yourself committing.

Suggested anti-patterns (pick one or invent):

- The "we will trim later" trap.
- The hour-30 framework switch.
- The MoSCoW chart that nobody updates.
- The pitch lead nobody picked.
- The localhost-only demo.
- The blame-loop retro.

The essay must:

- Describe the anti-pattern concretely (one paragraph).
- Explain *why* it happens (one paragraph).
- Propose **one specific rule** a team could write into their contract to prevent it (one paragraph).

**Acceptance criteria.**

- File at `notes/anti-pattern-essay.md`.
- 200–250 words.
- Three paragraphs as described.
- The proposed rule is concrete enough to put on a printed contract.
- Committed.

**Hint.** This is for you and your future teammates, not for a hiring committee. Be honest. The best essays describe an anti-pattern you have personally been on the wrong side of.

**Estimated time.** 25 minutes.

---

## Problem 6 — Mini reflection

**Problem statement.** Write a 250-word reflection at `notes/week-01-reflection.md` answering:

1. Which idea from Lecture 1 or 2 most changed your mental model? Why?
2. Which of the four canonical roles do you suspect you will actually want to play, after writing the personal brief? Was it different from what you would have guessed on Monday?
3. What is one specific behavior you want to take into the next event you attend?

**Acceptance criteria.**

- File at `notes/week-01-reflection.md`.
- 200–300 words.
- Each numbered question answered in its own paragraph.
- Committed.

**Hint.** This is the only homework that is not graded against the rubric. It is *yours*. Future-you reading it after Week 10 will be grateful you wrote it specifically and honestly.

**Estimated time.** 20 minutes.

---

## Time budget recap

| Problem | Estimated time |
|--------:|---------------:|
| 1 | 25 min |
| 2 | 20 min |
| 3 | 25 min |
| 4 | 15 min |
| 5 | 25 min |
| 6 | 20 min |
| **Total** | **~2 hours 10 min** |

When you've finished all six, push your repo and finalize the [mini-project](./mini-project/README.md) — your personal Hackathon Operating Document.

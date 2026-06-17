# Week 3 Homework

Six practice problems that revisit the week's topics. The full set should take about **2 hours** in total. Work in your `week-03-prep` folder (or the build repo, where the prompt says) so each problem produces at least one commit you can point to later.

Each problem includes:

- A short **problem statement**.
- **Acceptance criteria** so you know when you are done.
- A **hint** if you get stuck.
- An **estimated time**.

The homework is meant to be done *around* the build — most problems before Saturday, two after. The build is the week's center; the homework sharpens its edges.

---

## Problem 1 — Re-write a vague prompt into a one-sentence prompt

**Problem statement.** Take this deliberately bad prompt: *"An app to help students with their lives."* Re-write it into a one-sentence prompt in the `<user> can <verb> to relieve <pain>` shape, with one specific named human in mind (you, a roommate, a classmate). Then write the two-sentence demo-screen description.

**Acceptance criteria.**

- File at `week-03-prep/homework-01.md`.
- A one-sentence prompt in the correct shape.
- A specific named human mentioned (initials are fine).
- A two-sentence demo-screen description.
- Committed.

**Hint.** The bad prompt is bad on three axes (user, verb, pain). Fix each in turn. The point is the practice of cutting an over-scope prompt down to a buildable one.

**Estimated time.** 15 minutes.

---

## Problem 2 — The "WON'T smuggle test"

**Problem statement.** Open your Exercise 2 MoSCoW chart. Read each of your WON'T items out loud. For each one, write down — in `week-03-prep/homework-02.md` — the one sentence that explains *why your Saturday brain will try to smuggle it back in*. The point is to identify the rationalization in advance so you recognize it on Saturday.

**Acceptance criteria.**

- File at `week-03-prep/homework-02.md`.
- Each WON'T item has a one-sentence "Saturday rationalization" line.
- At least five WON'T items reviewed.
- No banned voice.
- Committed.

**Hint.** The rationalizations are predictable: "it's quick," "the judges will love it," "everyone has this," "I already know how." Naming them ahead of time makes them visible at hour two.

**Estimated time.** 15 minutes.

---

## Problem 3 — The crash-safe path drill

**Problem statement.** Pre-record a 5-second clip of yourself manually clicking through one happy path on a static placeholder page (any project will do — a personal website, a previous lab). Save it as `week-03-prep/crash-safe-clip.mp4` (or `.mov`, `.webm`). The point is to practice the fallback recording before Saturday, when you will not want to learn OBS for the first time.

**Acceptance criteria.**

- File at `week-03-prep/crash-safe-clip.<ext>`.
- The clip is 3–10 seconds long.
- The clip shows a real URL bar and at least one click.
- File size is reasonable (under 20 MB; trim or compress otherwise).
- Committed (Git LFS if your repo policy requires it; otherwise small files only).

**Hint.** This problem is half about learning your recording tool — OBS, QuickTime, Game Bar, Loom — and half about realizing that a 5-second clip is short. You will be tempted to over-produce. Don't.

**Estimated time.** 20 minutes.

---

## Problem 4 — Read three past C4 retros (or proxies)

**Problem statement.** Find three retros to read. Sources, in order of preference: (a) cohort-mate retros from this week, (b) any past C4 hackathon archive (`SPRING-2025/` and following), (c) any public hackathon post-mortem you can find online. Write a 150–250 word summary at `week-03-prep/homework-04.md` covering: one behavior that appeared in two or more retros, one behavior unique to a single retro, and one behavior you are adopting for your own list.

**Acceptance criteria.**

- File at `week-03-prep/homework-04.md`.
- 150–250 words.
- Three retros are named (URLs or repo paths).
- The "one behavior I am adopting" line is specific (has a *when* and a *what*).
- No banned voice.
- Committed.

**Hint.** If no cohort retros exist yet, read the C4 SPRING-2025 archive submissions' READMEs as proxies. The "what we cut" lines are early retros in disguise.

**Estimated time.** 25 minutes.

---

## Problem 5 — The "blameless translation" drill

**Problem statement.** Take each of the following self-blame statements and translate them into blameless retro voice in the style of Lecture 2 §2.2. Put your answers in `week-03-prep/homework-05.md` as a two-column table.

1. "I wasted an hour on the deploy."
2. "I am too slow at scaffolding."
3. "I always over-scope on Saturdays."
4. "I should have known about the CORS error."
5. "I am bad at recording demos."

**Acceptance criteria.**

- File at `week-03-prep/homework-05.md` with a two-column markdown table.
- Each row has the original self-blame line and a blameless translation.
- Each blameless translation names a *system* (a chart, a check, a script, a timer), not a person.
- Committed.

**Hint.** The pattern is: identify what *would have caught* the problem if it had existed. "The hourly stand-up did not include a deploy check." "The MoSCoW chart did not name CORS in WON'T's safety-net." "The Friday OBS rehearsal was skipped."

**Estimated time.** 20 minutes.

---

## Problem 6 — The three-behavior pre-write

**Problem statement.** Before Saturday's build, write three *predicted* behaviors you will want to change after the build. This is a pre-mortem: name what you think will go wrong. After the build, compare against the real three-behaviors line in your retro. Put both in `week-03-prep/homework-06.md` (the pre-build column on Friday, the post-build column on Sunday).

**Acceptance criteria.**

- File at `week-03-prep/homework-06.md`.
- Three pre-build predicted behaviors, each with a *when* and a *what*.
- Three post-build actual behaviors from your retro, copied in.
- A one-paragraph "what overlapped, what surprised me" note at the bottom.
- Committed by Sunday night.

**Hint.** The interesting outcome is *overlap*: the behaviors you predicted *and* hit are the ones you already know about but have not yet changed. The behaviors you did not predict are the ones the build itself taught you. Both groups are useful; the surprise group is gold.

**Estimated time.** 25 minutes.

---

## Time budget recap

| Problem | Estimated time |
|--------:|---------------:|
| 1 | 15 min |
| 2 | 15 min |
| 3 | 20 min |
| 4 | 25 min |
| 5 | 20 min |
| 6 | 25 min |
| **Total** | **~2 hours** |

If your time is strict, drop Problems 3 and 4. Keep 1, 2, 5, and 6 — those are the muscles the build itself relies on.

When you have finished, push your repo and finalize the [mini-project](./07-mini-project/00-overview.md) — the six-hour solo build, the recorded demo, and the committed retro.

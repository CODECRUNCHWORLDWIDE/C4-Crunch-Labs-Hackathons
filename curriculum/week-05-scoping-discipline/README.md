# Week 5 — Scoping Discipline

Welcome to **Week 5** of **C4 · Crunch Labs Hackathons**. Week 4 gave your team a *contract* — how the team runs stand-ups, cuts scope, points stories, refuses additions. Week 5 gives your team a *worksheet* — what the team actually ships in 36 hours, in writing, before the event starts. The contract is the rhythm; the worksheet is the map. A team with a contract and no worksheet still drifts; a team with a worksheet and no contract still bickers. You need both, and this week's job is to make the worksheet sharp enough to survive contact with a real event prompt.

If Week 4 was the team-room rehearsal, Week 5 is the *cut-list rehearsal*. You will deepen the MoSCoW chart pattern from BRAND.md into a five-section, one-page scoping worksheet — the artifact that turns the contract you wrote last week into a cut-list you can hold under the real clock. The ceremonies you compressed last week are the cadence; the scoping you sharpen this week is the discipline that lets the cadence survive contact with a hard deadline.

The deliverable is a **36-hour scoping worksheet template** committed to your repo — the artifact you bring to the next event and fill in with the team in the first hour. Every following week — and every future event — leans on this template being honest about what the team is *not* building, in writing, before fatigue corrupts the conversation.

## Learning objectives

By the end of this week, you will be able to:

- **Defend** MoSCoW (MUST / SHOULD / COULD / WON'T) as a *cut-list with names attached*, not a corporate four-column grid. Each column has a length cap and a failure mode if you blur it.
- **Run** a 20-minute MoSCoW pass at hour 0 of an event that produces 12–16 named items across the four columns and a 3-item MUST cap.
- **Defend** the WON'T list as the most-important column — the one that holds the refusal and protects the MUST. The asymmetry is the discipline.
- **Pre-write** a three-paragraph cut-list — what gets cut at hour 2, hour 12, hour 24 — before the event starts, with *named* cuts, not vague intentions.
- **Run** the five-question demo-ability test on any MUST item in 60 seconds, against the live URL — not localhost, not the staging branch, not a screenshot.
- **Run** the 30-minute pre-event walk-through on your `hackathon-template` repo from Week 2, and write down three gaps with one-sentence fixes.
- **Detect** the four most common MoSCoW failure modes — MUST-of-five, empty WON'T, aspirational COULD, verbal-only MoSCoW — and the four demo-ability failure modes — localhost demo, seeded-data ghost, polishing trap, "we'll fix it" delusion.
- **Commit** a one-page scoping worksheet template with five sections: prompt sentence, MoSCoW board, points budget, cut-list, demo-ability checklist. Reusable. Bring to every event from Week 10 onward.

## Prerequisites

- **Week 1 completed.** Your Hackathon Operating Document is committed, you know your default role, and the demo-or-die doctrine is familiar.
- **Week 2 completed.** Your `hackathon-template` repo is public and `bootstrap.sh` produces a live deploy URL. Week 5 *exercises this URL* — if it is broken, Week 5 surfaces it.
- **Week 3 completed.** You have shipped one solo build, recorded one demo, and written one structured retro. You know what MoSCoW feels like under a personal clock.
- **Week 4 completed.** Your `TEAM-CONTRACT.md` is committed. Week 5 *extends the contract* — the contract's WON'T list and "no" script reference the worksheet you build this week.
- **A scratch file or notebook.** You will draft cut-lists, demo-ability checklists, and worksheet drafts on paper before committing. Do not write the worksheet for the first time in your editor.

You do not need a team this week. Most of the drills work solo with imagined teammates. The optional challenge (Challenge 1) adds a partner for a 30-minute "scope a friend's idea" exercise if you can find one; the mini-project does not require it.

## Topics covered

- The four MoSCoW columns under hackathon compression — what each is *for* at 36 hours, with item-count caps
- The 20-minute MoSCoW pass at hour 0 — brainstorm, cluster, sort, cut, commit
- The WON'T list as the most-important column — the asymmetric truth of hackathon scoping
- The pre-written cut-list — three named cuts, one each at hour 2, hour 12, hour 24
- The five-question demo-ability test — URL, setup, stranger verb, prod result, seeded data
- The 30-minute pre-event walk-through — exercising your `hackathon-template` for deploy and seed gaps
- The cut-or-keep decision tree at hour 12 and hour 24 — default-cut bias, the trap of extension
- The four MoSCoW failure modes — MUST-of-five, empty WON'T, aspirational COULD, verbal-only
- The four demo-ability failure modes — localhost demo, seeded-data ghost, polishing trap, fix-it delusion
- Why the scoping worksheet is the most under-valued artifact a hackathon team brings to the room — alongside the contract
- The one-page worksheet template — five sections, voice, what to pre-fill vs leave blank
- Reading other teams' MoSCoW boards (in public READMEs) — what to look for, what to ignore
- The bridge from contract to worksheet — what the worksheet adds, why the two together are the team-mode preparation for Week 7's dry-run

## Weekly schedule

The schedule below adds up to approximately **10 hours**. Treat it as a target. Like Week 4, no single day is a six-hour build — this week is conceptual and rehearsal-heavy. The mini-project is a one-page worksheet template, which takes one focused session, not a Saturday block.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Lecture 1 — MoSCoW and the cut-list         |    1h    |    0h     |     0h     |    0h     |   0.5h   |     0h       |    0.5h    |     2h      |
| Tuesday   | Exercise 1 — Rate your prior builds         |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Wednesday | Lecture 2 — The demo-ability test           |    1h    |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Thursday  | Exercise 2 — Scope stress game              |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Friday    | Exercise 3 — Cut-list rehearsal             |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Saturday  | **Mini-project — 36-hour scoping worksheet**|    0h    |    0h     |     0h     |    0h     |   0h     |     2h       |    0h      |     2h      |
| Sunday    | Quiz + challenge (optional) + polish        |    0h    |    0h     |     1h     |    0.5h   |   0.5h   |     0.5h     |    0h      |     2.5h    |
| **Total** |                                             | **2h**   | **3h**    | **1h**     | **1.5h**  | **2h**   | **3.25h**    | **0.5h**   | **~13.25h** |

The base ten-hour target excludes Challenge 1 (Scope a Friend's Idea). If you do the challenge, expect 11–12 hours total. The mini-project is the artifact you keep; the exercises are the drills that make the worksheet honest.

The optional **Challenge 1 — Scope a Friend's Idea** lives outside the ten-hour target. Pair it with a non-C4 partner — a friend with a startup idea, a sibling with a side project, a club-mate with a class project — and run the 30-minute MoSCoW + cut-list pass on *their* idea. The point is to practice scoping a build you do not personally own.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | MoSCoW primers, free planning tools, real hackathon project READMEs to study |
| [lecture-notes/01-moscow-and-the-cut-list.md](./lecture-notes/01-moscow-and-the-cut-list.md) | The four columns; the 20-minute pass; the WON'T-list asymmetry; the cut-list at hour 2/12/24 |
| [lecture-notes/02-the-demo-ability-test.md](./lecture-notes/02-the-demo-ability-test.md) | The live-URL bench; the five-question test; the pre-event walk-through; the cut-or-keep tree |
| [exercises/exercise-01-rate-your-prior-builds.md](./exercises/exercise-01-rate-your-prior-builds.md) | Rate your Week 3 solo build (and any past hackathon work) against the demo-ability test |
| [exercises/exercise-02-scope-stress-game.md](./exercises/exercise-02-scope-stress-game.md) | Run the MoSCoW pass on a fake prompt under a 20-minute clock; cut MUST to 3 |
| [exercises/exercise-03-cut-list-rehearsal.md](./exercises/exercise-03-cut-list-rehearsal.md) | Pre-write the three named cuts for hour 2, 12, 24 against the fake prompt |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-scope-a-friends-idea.md](./challenges/challenge-01-scope-a-friends-idea.md) | A 30-minute paired exercise on a non-C4 partner's real idea |
| [quiz.md](./quiz.md) | 10 multiple-choice questions |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | The one-page 36-hour scoping worksheet template |

## Stretch goals

If you finish the worksheet on Saturday and want to push further, try any of the following. None substitute for the worksheet — write the worksheet first, every time.

- **Run Exercise 1 against a Week 1 hackathon you previously attended.** Pull the project README. Reverse-engineer the MUST / SHOULD / WON'T list. Note one item that would have moved if you had this worksheet on hand at the time.
- **Trade worksheets with another C4 learner.** Read theirs. Note one cut-list paragraph yours is missing. The worksheet you would bring to a real event is the union of three good worksheets you read, not the first draft you wrote alone.
- **Find a public hackathon submission with a thoughtful "future work" section.** Read it. Identify the implicit WON'T list. Note one item the team explicitly *did not* build, and the reason. That is the muscle most teams skip in their public writing — find the teams that did it well.
- **Re-read your Week 3 retro alongside Lecture 1 §4 (the four MoSCoW failure modes).** Which of the three retro behaviors you named is *really* a scoping behavior in disguise? "Stayed on auth too long" reads as a tech behavior; it is almost always a MoSCoW behavior — auth was a MUST that should have been a WON'T.
- **Run the pre-event walk-through (Lecture 2 §2) on a teammate's `hackathon-template` repo.** Their template will have different rot from yours. Note one gap their template has and yours does not. Open an issue on their repo; offer the fix.

## Up next

Continue to **Week 6 — Pitch Craft** once your scoping worksheet is committed, your three exercises are complete, and your quiz is at 9/10 or better. In Week 6 you will turn the *clean MUST list* you committed this week into a *three-minute demo script* — the artifact that fits inside the demo strip from BRAND.md. The contract is the rhythm; the worksheet is the map; the pitch is the delivery. The three together are what your team brings to the event.

---

*The win is shipping. You shipped one alone. You wrote the words that let a team ship together. Now you are writing the map that says which features ship — and which features the team agreed, in writing, before the event, would not.*

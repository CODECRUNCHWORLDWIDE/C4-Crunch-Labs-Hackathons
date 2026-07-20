# Week 7 — Team-Mode Dry-Run, Day 1

Welcome to **Week 7** of **C4 · Crunch Labs Hackathons**. Week 4 gave the team a *contract* — how the team runs. Week 5 gave the team a *worksheet* — what the team ships. Week 6 gave the team a *script* — how the team's three MUST items are walked through in three minutes. Week 7 is the first 24 hours where all three artifacts are *enacted at the same time, in real time, with other humans in the room or on the call*. The contract is the rhythm; the worksheet is the map; the pitch is the delivery; the dry-run is the *load test* of all three under the conditions of a real hackathon's opening day.

If Week 6 was the recording rehearsal, Week 7 is the *kickoff rehearsal*. You will assemble a team of three or four (cohort-mates, classmates, a friend who codes, a sibling who designs — the source does not matter, the four-person ceiling does). You will run a 24-hour mock hackathon starting from a written prompt at hour 0 and ending at a written check-in at hour 24. You will hold a kickoff meeting, you will assign three roles, you will scope to a three-MUST worksheet inside hour 2, you will parallelize the build across hours 4 through 22, and you will hold the day-1 close-out at hour 24. The artifact you keep is the team's **DAY-1-LOG.md** — a single committed file with timestamped notes for every named event of the first 24 hours.

Most learners arrive at their first hackathon having *coded with other humans* once or twice in class — a 2-hour pair-programming lab, a group project with a one-week deadline, a study session. None of those are a hackathon. A hackathon's first 24 hours collapse a semester of team formation into a single overnight, and the teams that ship are the ones who treated the kickoff as a *discipline* — written agenda, named roles, named scope, named communication channel — and not as a vibe. The dry-run is the discipline; the log is the artifact.

The deliverable is a **committed `DAY-1-LOG.md`** in your repo from a real (or peer-simulated) 24-hour dry-run with at least one other person. Every following week leans on this log being honest about the kickoff timestamp, the role assignments, the scope cuts made in hour 2, the parallelization between hours 4 and 22, the conflict moments (and how they were resolved), and the hour-24 close-out. The log is the half of teamwork you can write down; the kickoff itself is the half you can only learn by running.

## Learning objectives

By the end of this week, you will be able to:

- **Run** a 60-minute hackathon kickoff meeting from a written agenda — introductions, prompt reading, role assignment, communication-channel setup, scope-pass-one, and a named "we start coding at this timestamp" handoff — without exceeding the 60-minute cap.
- **Assign** three core hackathon roles (Builder Lead, Demo Lead, Comms Lead) to a 3- or 4-person team in under 10 minutes using the role-fit grid from Lecture 1, and rotate the Builder Lead at hour 12 if the team is 4-strong.
- **Scope** a 24-hour build to a 3-MUST / 3-SHOULD / 3-COULD worksheet (re-using the Week-5 template) inside hour 2 of the dry-run, with every team member having read and approved the MUST list aloud.
- **Parallelize** the work across three tracks (build, design+demo, comms+log) such that no track blocks the other for more than 30 minutes between hour 4 and hour 22, and document the parallelization in the log with a named "track owner" per track.
- **Establish** team communication norms — one Slack/Discord channel, one shared doc, one stand-up time, one Slack-DM-vs-channel rule — in under 15 minutes during the kickoff, and reference them in the log every time they are used.
- **Hold** three lightweight stand-ups during the first 24 hours (hour 4, hour 12, hour 22) using a written three-question template (what shipped, what is blocking, what is the next 4 hours) — each stand-up capped at 10 minutes per team member.
- **Detect and resolve** the four most common day-1 team conflicts — the scope-creep request, the silent disagreement, the role-overlap argument, the "I'll just rewrite it" merge fight — using the one-sentence intervention pattern from Lecture 3.
- **Commit** a `DAY-1-LOG.md` to the dry-run's repo with timestamped entries for the kickoff (hour 0), the scope pass (hour 2), each stand-up (hours 4, 12, 22), each named conflict moment, and the hour-24 close-out — with at least one other named teammate as a co-author or named contributor in the file.

## Prerequisites

- **Week 1 completed.** Your Hackathon Operating Document is committed. The demo-or-die doctrine still applies; team mode does not relax it, it amplifies it. A four-person team that does not ship is four times the cost of a solo prototype that does not ship.
- **Week 2 completed.** Your `hackathon-template` repo is public and `bootstrap.sh` produces a live deploy URL. The dry-run runs against this template — the team forks (or clones into a new repo using it as a starter) at hour 0 of the dry-run, and the URL is live by hour 4 at the latest.
- **Week 3 completed.** You have shipped one solo prototype end-to-end. The dry-run is your *second* shipping experience; the cohort-mates you team with should also have a Week 3 build behind them. Mixing one Week-3-complete learner with one Week-3-incomplete learner produces a 4-hour rebuild loop on the kickoff that this week does not have time for.
- **Week 4 completed.** Your `TEAM-CONTRACT.md` is committed. The dry-run team writes a *fresh* `TEAM-CONTRACT.md` in the first 30 minutes of the kickoff — the Week-4 contract was your solo-mode draft, this week's contract is the multi-human enactment of the same template.
- **Week 5 completed.** Your `SCOPING-WORKSHEET.md` is committed. The dry-run team writes a *fresh* `SCOPING-WORKSHEET.md` in hour 2 of the kickoff — the Week-5 worksheet was your solo-mode draft, this week's worksheet is the team-agreed MUST list.
- **Week 6 completed.** Your three-minute recorded demo is committed with a public link. The dry-run team will record a *team* three-minute demo at hour 24 — the Week-6 recording was your solo dress rehearsal, this week's recording is the multi-human pitch.
- **A team of 2 to 4 people, assembled by Tuesday.** The team can be other C4 learners (preferred), classmates, club-mates from gdgatfiu / swiftclubatfiu / ColorStack / CAHSI / Hack University, or non-cohort friends who code. Solo is not an option this week; the entire point is multi-human coordination. If you cannot recruit one other person by Tuesday, message the C4 channel and the cohort coordinator will pair you.
- **A four-hour block on Saturday plus a four-hour block on Sunday.** The dry-run is 24 wall-clock hours but only ~8 of those need to be synchronous active work; the rest is asleep, eating, or async build. Block the two four-hour windows on the calendar before Friday. Do not start the dry-run if the team cannot agree on the eight synchronous hours.

A scope warning: the dry-run is **not** a real hackathon. It is a *day-1 simulation*. The team does not need to win anything; the team does not need to ship a polished demo; the team does need to *run the kickoff, the three stand-ups, the conflict-resolution drills, and the close-out* with the same discipline a real event would demand. The deliverable is the log of the discipline, not the polish of the build.

## Topics covered

- **Why day 1 is a separate skill from day 2 onward.** The kickoff sets the cadence for the next 23 hours; a botched kickoff usually surfaces as a missed demo on day 2, and the team blames the wrong cause.
- **The 60-minute kickoff meeting.** Six 10-minute segments — introductions, prompt reading, role assignment, scope pass one, comms-channel setup, "we start coding at" handoff — and the discipline of not exceeding the cap.
- **The three core hackathon roles — Builder Lead, Demo Lead, Comms Lead.** Definitions, fit-grid, rotation rule for 4-person teams.
- **Scoping inside hour 2.** Re-running the Week-5 worksheet as a *team*, with the MUST list read aloud and approved by every member.
- **The three-track parallelization model.** Build track, design+demo track, comms+log track. Track ownership. The 30-minute block rule (no track waits on another for more than 30 minutes).
- **The hour-by-hour schedule, hours 0 to 24.** A printable timeline with named events, named timestamps, and named log entries.
- **Communication norms during a hackathon.** One channel, one shared doc, one stand-up time, one DM-vs-channel rule. The cost of every extra channel; the cost of side-channel decisions.
- **The three day-1 stand-ups — hour 4, hour 12, hour 22.** Three-question template (what shipped, what is blocking, what is the next 4 hours), 10-minute cap, one designated note-taker.
- **The four day-1 team conflicts and the one-sentence interventions.** Scope-creep, silent disagreement, role-overlap, "I'll just rewrite it" merge fight.
- **The hour-24 close-out.** A 30-minute meeting: what shipped vs what was on MUST, what is on the day-2 plan, the team-health one-word check.
- **The `DAY-1-LOG.md` file format.** Timestamped Markdown, named co-authors, public commit history, the artifact that survives the dry-run.
- **The MLH and Devpost-side norms.** Code of Conduct boundaries, judging-window expectations, what counts as "started during the event," and where the dry-run rehearses the real-event rules.

## Weekly schedule

The schedule below adds up to approximately **12 hours** of structured work, plus the 24 wall-clock hours of the dry-run itself (of which roughly 8 are synchronous active work). Treat the structured hours as a target. The dry-run weekend (Saturday hour 0 to Sunday hour 24, or any other 24-hour window the team agrees on) is the *load test* for the week's learning, not extra hours on top.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Lecture 1 — Kickoff and roles               |    1.5h  |    0h     |     0h     |    0h     |   0.5h   |     0h       |    0.5h    |     2.5h    |
| Tuesday   | Exercise 1 — Write the team charter         |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Wednesday | Lecture 2 — Scoping and parallelization     |    1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     2.25h   |
| Thursday  | Lecture 3 — Comms norms and fixing conflict |    1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     2.25h   |
| Friday    | Exercise 2 + Exercise 3 — Drills            |    0h    |    1.5h   |     0h     |    0.5h   |   0.5h   |     0.5h     |    0h      |     3h      |
| Saturday  | **Mini-project — Dry-run hours 0 to 12**    |    0h    |    0h     |     0h     |    0h     |   0h     |     4h       |    0h      |     4h      |
| Sunday    | **Mini-project — Dry-run hours 12 to 24** + quiz + challenge (optional) | 0h | 0h | 1h | 0.5h | 0.5h | 4h | 0h | 6h |
| **Total** |                                             | **4.5h** | **2.5h**  | **1h**     | **2h**    | **2.25h**| **9.25h**    | **0.5h**   | **~22h**    |

The 22-hour total is heavy. The base ten-hour target for a C4 week is the structured work (lectures + exercises + quiz + homework + self-study), which is around 11.75 hours this week — slightly above the cohort norm because Lecture 1 is 1.5 hours and the three drills add up. The mini-project's 8 hours of active work happen *during* the 24-hour dry-run window, not in addition to it; you are not asked to spend 22 wall-clock hours on C4 this week, you are asked to spend ~11.75 hours of structured prep then run a 24-hour calendar-blocked dry-run where ~8 of those 24 are synchronous active work.

The optional **Challenge 1 — Run a Cross-Track Dry-Run** lives outside the structured target. Pair with a C4 learner from a different track (a C1 learner doing Python, a C7 learner doing the wire bootcamp, a C8 learner doing data engineering) and run the dry-run with mixed prompts. The point is to practice scoping when the team has uneven skill profiles. The skill is the kickoff; the kickoff does not care which tracks the team is from.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | MLH organizer handbook, Atlassian agile guides, devpost help, GitHub learner dev pack tools, public team-charter templates |
| [lecture-notes/01-kickoff-and-roles.md](./lecture-notes/01-kickoff-and-roles.md) | The 60-minute kickoff meeting; the three core roles; the role-fit grid; rotation rules |
| [lecture-notes/02-scoping-and-parallelization.md](./lecture-notes/02-scoping-and-parallelization.md) | Re-running the Week-5 worksheet as a team; the three-track parallelization model; the hour-by-hour schedule |
| [lecture-notes/03-comms-norms-and-fixing-conflict.md](./lecture-notes/03-comms-norms-and-fixing-conflict.md) | One channel, one doc, one stand-up rule; the four day-1 conflicts and the one-sentence interventions |
| [exercises/exercise-01-team-charter-for-fake-event.md](./exercises/exercise-01-team-charter-for-fake-event.md) | Draft a `TEAM-CONTRACT.md` for a fake 24-hour event prompt in 45 minutes |
| [exercises/exercise-02-hour-by-hour-schedule.md](./exercises/exercise-02-hour-by-hour-schedule.md) | Build a printable hour-by-hour day-1 schedule from a written prompt |
| [exercises/exercise-03-conflict-intervention-drill.md](./exercises/exercise-03-conflict-intervention-drill.md) | Write one-sentence interventions for the four named conflicts |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-clean-24-hours.md](./challenges/challenge-01-clean-24-hours.md) | Acceptance criteria for "did the team run a clean 24 hours?" |
| [quiz.md](./quiz.md) | 10 multiple-choice questions on team dynamics and time-boxed project management |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | The full 24-hour dry-run spec, log template, and acceptance criteria |

## Stretch goals

If the dry-run closes on Sunday and the team wants to push further, try any of the following. None substitute for the dry-run log — commit the log first, every time.

- **Run a second dry-run with the same team, different prompt.** The same team running two dry-runs back-to-back surfaces which parts of the kickoff are *team-specific* (the role fit, the comms norms) and which are *prompt-specific* (the scope, the parallelization). Two dry-runs is the minimum to separate the two.
- **Trade `DAY-1-LOG.md` files with another C4 team and run a peer review.** A team reviewing another team's log catches the entries that look fine to the writer but read as ambiguous to a stranger. The review is the next layer of discipline.
- **Re-read Atlassian's "Agile retrospective" guide alongside your hour-24 close-out.** The close-out is a retrospective in disguise; the Atlassian guide names the four-quadrant format (start / stop / continue / more of) that maps cleanly to the close-out's three named outputs.
- **Watch a public hackathon kickoff recording (MLH or a major university event).** Note the kickoff's hour-1 cadence. Compare to your dry-run's kickoff timestamps. The delta is the discipline gap you can close in the next dry-run.
- **Run the four-conflict drill (Exercise 3) with three different teammates.** The interventions read differently when delivered to different humans; the muscle is the *delivery*, not the wording. Same script, different rooms, different feel.
- **Write a one-page "lessons from the dry-run" memo and append it to the log.** One page, three sections: what surprised the team, what the team would change, what the team kept. The memo is a stronger artifact than the log alone.

## Up next

Continue to **Week 8 — Team-Mode Dry-Run, Day 2 and Demo** once your `DAY-1-LOG.md` is committed, your three exercises are complete, your quiz is at 9/10 or better, and the dry-run team is named in your repo README. In Week 8 you will close the *second* 24 hours of the dry-run — the demo prep, the second-day stand-up cadence, the hour-44 freeze, the hour-46 dress rehearsal, and the hour-48 team demo recording using the Week-6 strip. The contract is the rhythm; the worksheet is the map; the pitch is the delivery; the dry-run is the load test. Week 7 loads the test; Week 8 measures the result.

---

*The win is shipping. You shipped one alone. You wrote the words that let a team ship together. You wrote the map that says which features ship. You wrote the script that says how the build is seen. Now you have the log — and the team — that says how the first 24 hours run when there is more than one human in the room.*

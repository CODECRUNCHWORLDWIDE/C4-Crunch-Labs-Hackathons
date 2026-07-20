# Week 8 — Team-Mode Dry-Run, Day 2 (Hours 12 to 24)

Welcome to **Week 8** of **C4 · Crunch Labs Hackathons**. Week 7 took the team from hour 0 of a 24-hour simulated hackathon to hour 12 — kickoff, role assignment, hour-2 scope lock, the first three stand-ups, the first commit to main, the first conflict resolution. Week 8 picks up at hour 12 and runs the team to hour 24: the midnight slump, the "should we pivot" decision point at hour 14, the integration-friction window at hour 16, the demo-cut conversation at hour 18, the recording window at hour 20, the submission package at hour 22, and the hour-24 retrospective. The contract is still the rhythm; the worksheet is still the map; the pitch is still the delivery; this week is the *second half of the load test*.

Week 7 taught the team to *start*. Week 8 teaches the team to *finish*. The skills are different — opening discipline is mostly about agenda-and-roles, closing discipline is mostly about *triage, conflict-management at low energy, and the difference between a demo that is finished and a demo that is merely "almost finished."* The two halves are not interchangeable; a team that aces day 1 can still implode in the midnight slump if they have not rehearsed the day-2 protocols. The dry-run from Week 7 was the rehearsal of the opening; this week is the rehearsal of the *closing*.

The deliverable is a **committed `DAY-2-LOG.md`** in the same repo as `DAY-1-LOG.md` from Week 7, with timestamped entries for the hour-12 handoff, the hour-14 pivot-decision moment (even if the answer was "no pivot"), the integration-friction window between hours 14 and 18, the hour-18 demo-cut, the hour-20 dress rehearsal, the hour-22 submission package, and the hour-24 retrospective. The log is the audit trail; the retro is the meta-learning; the submission package is the artifact that, in a real event, the judges actually see.

Most learners who reach Week 8 already passed the technical bar in Weeks 1 through 3. The barrier here is not coding; it is *judgment under fatigue*. At hour 16, the team is six hours into a slump and the Builder Lead has a 500-line pull request that does not compile. At hour 18, the Demo Lead realises MUST 2 is not screen-recordable yet. At hour 20, the team is recording take six and the third teammate suggests re-recording from scratch. Each of those is a *decision point*, not a technical problem. The lectures, the exercises, and the homework rehearse the decision points so that on a real Saturday night the team's body knows what to do before the brain re-derives it.

## Learning objectives

By the end of this week, you will be able to:

- **Run** the hour-12 stand-up as a *handoff stand-up* — not a status check — with explicit role rotation (Builder Lead swaps on a 4-person team, the rotating-off lead takes a 2-hour structured rest), explicit MUST-status table with a yes/no done-row per item, and explicit naming of the team's remaining synchronous hours.
- **Execute** the "should we pivot" decision protocol — a 15-minute structured conversation, a written 2-question rubric, and a single committed log entry that names *both* the decision and the considered alternative — so that the question "should we pivot?" never consumes more than 15 wall-clock minutes regardless of the answer.
- **Manage** the integration-friction window between hours 14 and 18 — the period when two or three teammates' branches must merge to main and the build first becomes a *team build* — using a written merge protocol, a 30-minute branch-freeze rule, and a one-paragraph commit-message template per MUST.
- **Convert** a SHOULD/COULD overrun into a *cut*, not a *late-night marathon*, by applying the hour-18 demo-cut rubric — a 3-line checklist that converts "we are running long" into "we cut feature X at hour 18 and the log notes the cut and the recording proceeds at hour 20."
- **Rehearse** the team's three-minute demo at hour 20 against the live deploy URL — at least two takes, with the Demo Lead as director and the Builder Lead as technical operator and the Comms Lead as audience proxy — without re-litigating the script at the recording stage.
- **Package** the submission at hour 22 — public repo URL, live deploy URL, three-minute demo video URL, `DAY-2-LOG.md` link, and the team's `SUBMISSION.md` cover sheet — and the discipline of *stopping work* at hour 23 even if the team feels there is more to polish.
- **Run** the hour-24 retrospective as a 30-minute meeting with a written template — three sections (kept, changed, dropped), one teammate as scribe, one team-health one-word check, and a commit-pointer line in the log — and a single follow-up issue filed in the repo within 24 hours of the retro.
- **Recognise** the seven day-2 conflict patterns — the midnight death-march, the surprise scope-creep at hour 16, the silent stalemate during a pivot decision, the "I'll just rewrite it" merge fight at hour 17, the demo-lead-versus-builder-lead recording dispute at hour 20, the burnout-by-attrition pattern, and the over-polished-but-late submission — and the named intervention pattern for each.

## Prerequisites

- **Week 7 completed.** `DAY-1-LOG.md` is committed; the dry-run team is named in the repo README; the kickoff timestamps are in the log. Week 8 cannot start without Week 7's log because Week 8 *extends the same log file*. If your Week 7 dry-run did not commit a log, run it again before starting Week 8 — there is nothing to add hours 12-24 onto without it.
- **Weeks 1 through 6 completed.** The Hackathon Operating Document, the template repo, the solo prototype, the team contract, the scoping worksheet, and the three-minute solo demo recording. The team-mode work this week assumes you already shipped solo once.
- **The same team from Week 7.** Different team is a different dry-run. Switching teams mid-dry-run resets the rapport gains from day 1 and makes day 2 into a second day-1 — which is *not* what this week is rehearsing. If a teammate dropped between Week 7 and Week 8, log the drop in `DAY-1-LOG.md` first; then run a *3-person Week 8* with the remaining team.
- **Four hours of synchronous active work on Sunday plus a two-hour retro window.** The dry-run window is hours 12-24 of the original 24-hour clock; about 4 of those 12 hours are synchronous active work (the hour-12 handoff stand-up, the hour-16 integration window, the hour-20 dress rehearsal, the hour-24 retro). The other 8 are async build, rest, or the sleep window.
- **The deploy URL is live.** If `bootstrap.sh` is not producing a live URL by hour 12, the day-2 plan is "fix the deploy first; everything else after." The dress rehearsal at hour 20 records against the live URL; localhost recordings are disallowed.

A reminder: the dry-run is **not** a real hackathon. It is a *day-2 simulation*. The team is not trying to win; the team is rehearsing the closing protocols so the real event's closing feels practiced. The deliverable is the log of the discipline plus the retrospective, not the polish of the demo.

## Topics covered

- **Why day 2 is a separate skill from day 1.** Day 1 is about agenda discipline; day 2 is about judgment under fatigue. The two skills do not transfer.
- **The hour-12 handoff stand-up.** Role rotation on 4-person teams; structured 2-hour rest for the rotating-off lead; the MUST-status table; the team-health midpoint check.
- **The midnight slump and the four named coping protocols.** Caffeine-and-water rule, two-person-pair work, the 90-minute focus block, the 20-minute walk-or-sleep rule.
- **The "should we pivot" decision protocol.** The 15-minute cap; the 2-question rubric; the written log entry; what "pivot" actually means at hour 14 (it never means "throw out the build").
- **The integration-friction window (hours 14 to 18).** The merge protocol; the 30-minute branch-freeze; the commit-message template; the one-PR-at-a-time rule.
- **The hour-18 demo-cut.** Converting an overrunning SHOULD/COULD into a cut; the 3-line checklist; the log entry; the conversation pattern with the teammate who proposed the SHOULD.
- **The hour-20 dress rehearsal.** Two takes minimum; roles during the recording (director, operator, audience proxy); the no-re-litigation rule; recording against the live deploy URL.
- **The hour-22 submission package.** The five artifacts (repo, deploy, demo video, log, `SUBMISSION.md`); the cover-sheet template; the *stop work at hour 23* rule.
- **The hour-24 retrospective.** Kept, changed, dropped; one-word team-health check; the follow-up issue; the difference between a retro that is honest and a retro that is comfortable.
- **The seven day-2 conflict patterns and the named interventions.** Midnight death-march, hour-16 scope creep, pivot stalemate, "I'll just rewrite it," recording dispute, attrition burnout, late submission.
- **The `DAY-2-LOG.md` file format.** Extends `DAY-1-LOG.md`; same timestamp convention; the retro template at the bottom; the follow-up-issue link.
- **The Devpost-side submission norms.** What "started during the event" means in the submission rules; the 3-minute video cap; the public-repo requirement; where the dry-run rehearses the real-event submission discipline.
- **The NumFOCUS event playbook on closing protocols.** A public reference for open-source community events; the hour-24 retro pattern in NumFOCUS-style events; how the C4 retro template aligns.

## Weekly schedule

The schedule below adds up to approximately **12 hours** of structured work, plus the 12 wall-clock hours of the dry-run's day-2 window (of which roughly 4 are synchronous active work). The structured hours are the target; the dry-run continuation is the load test.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Lecture 1 — Midnight slump and pivot protocol |    1.5h  |    0h     |     0h     |    0h     |   0.5h   |     0h       |    0.5h    |     2.5h    |
| Tuesday   | Exercise 1 — Pivot decision drill           |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Wednesday | Lecture 2 — Integration friction and demo cut |    1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     2.25h   |
| Thursday  | Lecture 3 — Submission, recording, retro    |    1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     2.25h   |
| Friday    | Exercise 2 + Exercise 3 — Drills            |    0h    |    1.5h   |     0h     |    0.5h   |   0.5h   |     0.5h     |    0h      |     3h      |
| Saturday  | **Mini-project — Dry-run hours 12 to 20**   |    0h    |    0h     |     0h     |    0h     |   0h     |     3h       |    0h      |     3h      |
| Sunday    | **Mini-project — Dry-run hours 20 to 24** + retro + quiz + challenge (optional) | 0h | 0h | 1h | 0.5h | 0.5h | 3h | 0h | 5h |
| **Total** |                                             | **4.5h** | **2.5h**  | **1h**     | **1.75h** | **2.25h**| **7.25h**    | **0.5h**   | **~19.75h** |

The ~20-hour total is dense. The structured prep target (lectures + exercises + quiz + homework + self-study) is around 11.5 hours; the dry-run continuation adds the rest. As in Week 7, the wall-clock hours of the dry-run overlap with the calendar — you are not adding the 7.25 mini-project hours on top of normal life, you are running them during a pre-blocked Saturday-into-Sunday window.

The optional **Challenge 1 — Submission Package Polish** lives outside the structured target. Run a public-facing version of the submission package — a `SUBMISSION.md` cover sheet with hooks linking to the repo, the deploy, the video, and the log — at production quality, as if the team were actually entering a Devpost event. The skill is the *finishing polish*, not new technical content.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | Devpost help, MLH judging guidance, NumFOCUS event playbook, Atlassian retrospective guides, public hackathon retrospectives |
| [lecture-notes/01-midnight-slump-and-pivot.md](./lecture-notes/01-midnight-slump-and-pivot.md) | The hour-12 handoff stand-up; the midnight slump coping protocols; the 15-minute pivot decision protocol |
| [lecture-notes/02-integration-and-demo-cut.md](./lecture-notes/02-integration-and-demo-cut.md) | The integration-friction window hours 14-18; the merge protocol; the hour-18 demo cut; conflict-resolution rubrics |
| [lecture-notes/03-submission-and-retro.md](./lecture-notes/03-submission-and-retro.md) | The hour-20 dress rehearsal; the hour-22 submission package; the hour-24 retro template; the follow-up issue |
| [exercises/exercise-01-pivot-decision-drill.md](./exercises/exercise-01-pivot-decision-drill.md) | Apply the 15-minute pivot protocol to three fake scenarios |
| [exercises/exercise-02-integration-friction-drill.md](./exercises/exercise-02-integration-friction-drill.md) | Run a merge-conflict resolution on a fake repo state |
| [exercises/exercise-03-retro-from-fake-log.md](./exercises/exercise-03-retro-from-fake-log.md) | Write a retro from a fake `DAY-2-LOG.md` and produce a follow-up issue |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-submission-polish.md](./challenges/challenge-01-submission-polish.md) | Acceptance criteria for a public-facing submission package |
| [quiz.md](./quiz.md) | 10 multiple-choice questions on day-2 protocols and decision frameworks |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | The full hours-12-to-24 dry-run spec, retro template, and acceptance criteria |

## Stretch goals

If the dry-run closes on Sunday and the team wants to push further, try any of the following. None substitute for the retro — commit the retro first, every time.

- **Run a peer-review pass on another team's `DAY-2-LOG.md`.** Trade logs with another C4 team and write a one-page review: what surprised you, what is missing, what reads as ambiguous. The peer review is the layer above self-grading.
- **Re-record the demo with a fresh camera or fresh framing 24 hours after the dry-run.** The recording window's adrenaline pushes the demo into a particular voice; recording again the next day with rested eyes surfaces the parts of the script that did not actually land.
- **Read three public hackathon retrospectives on Devpost and Reddit and write a one-page comparison.** The Devpost retros are usually polished; the Reddit retros are usually honest; the contrast is instructive. The comparison sharpens your own retro voice.
- **Run the four-conflict drill (Exercise 3) with a different teammate at a different fatigue level.** The interventions read differently when delivered at hour 18 versus hour 0; the muscle is the *delivery under fatigue*, not the wording.
- **Write a one-page "lessons from day 2" memo and append it to the log.** One page; three sections: what surprised, what the team would change, what the team kept. The memo distills the retro into a re-readable artifact.
- **Compare the team's day-1 and day-2 logs side by side.** The deltas between the two halves of the dry-run reveal which discipline the team built during the run versus what they brought in already.

## Up next

Continue to **Week 9 — Judging, Pitching, and Live Q&A** once your `DAY-2-LOG.md` is committed, the retro entry is in place, the submission package is in the repo, your three exercises are done, your quiz is at 9/10 or better, and the follow-up issue is filed. Week 9 takes the demo recording (from Week 6 solo plus Week 8 team) and rehearses *live* delivery — judge-room pitch, the 60-second elevator version, the live Q&A pattern, and the panel-vs-table-judge dynamics. The dry-run loaded the test; the retrospective measured the result; Week 9 takes the measurement *into the room with judges*.

---

*The win is shipping. You shipped one alone in Week 3. You wrote the contract in Week 4, the map in Week 5, the script in Week 6. In Week 7 the team ran the first 12 hours. This week the team ran the second 12. The log is the audit; the retro is the lesson; the lesson is the discipline you carry into the real event.*

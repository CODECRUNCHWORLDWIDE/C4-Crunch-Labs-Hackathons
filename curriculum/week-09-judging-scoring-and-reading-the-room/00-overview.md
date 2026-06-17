# Week 9 — Judging, Scoring, and Reading the Room

Welcome to **Week 9** of **C4 · Crunch Labs Hackathons**. Weeks 7 and 8 ran the 24-hour team-mode dry-run end to end — kickoff to retro, opening to closing, the contract to the follow-up issue. The team shipped a build, recorded a demo, packaged a submission, and committed a retrospective. Week 9 takes everything that happens *after* the team hits "submit" and rehearses it: the judging window, the live judge-room pitch, the live Q&A, the panel-vs-table judging dynamics, and the part most learners under-rehearse — the *reading-the-room* skill that separates a pitch the judges remember from a pitch they politely tolerate.

Week 9 is the *delivery layer* of the C4 stack. The build was Week 3. The contract was Week 4. The scope was Week 5. The script was Week 6. The first 12 hours of the team-mode run was Week 7. The closing was Week 8. This week is the *minute the judges walk up to your table*. Everything you built before this week is only as good as the four minutes you get with the judging panel. Four minutes is not a lot; the lectures and the exercises rehearse it until it is enough.

The deliverable is a **committed `JUDGE-ROOM-LOG.md`** in the same repo as `DAY-1-LOG.md` and `DAY-2-LOG.md`, with three signed entries: a *self-scored rubric* applied to the team's own demo, a *mock pitch* recording (two takes) timed at exactly 3 minutes, and a *mock Q&A* transcript covering the 5 most-asked questions for the team's specific build. Plus a written reflection on which of the two judging mindsets the team's pitch actually leans into — *engineer* or *investor* — and what changes if the team gets the other kind of judge.

Most learners reach Week 9 with the build in their hands and zero rehearsed minutes of live delivery. The Week 6 solo demo was *recorded*; the Week 8 dress rehearsal was *recorded*. Recording is forgiving — the team can cut, reshoot, re-record. The judge-room is unforgiving — three minutes, one camera-less take, four humans staring at you with a clipboard and a timer. The two delivery modes are not the same skill. The recording rehearses the script; the judge-room rehearses the *delivery under live observation*. Week 9 names the difference, rehearses the second mode, and arms the team for both judge profiles (engineer and investor) and both judging formats (table-walk and panel).

## Learning objectives

By the end of this week, you will be able to:

- **Read** the five rubric dimensions used by most public hackathons — technical complexity, design and UX, originality, polish, and presentation — name what each one is actually measuring, and self-score the team's submission against each dimension on a 1-5 scale with a one-line evidence cite per score.
- **Recognise** the two judging mindsets — *judge-as-engineer* (asks: "what did you build, how hard was the engineering, what would break under load") and *judge-as-investor* (asks: "who is this for, is there a market, would you keep building it") — and switch the pitch's emphasis in the first 20 seconds based on the cues the judge gives.
- **Deliver** a 3-minute judge-room pitch using the four-beat arc — **problem (30s) → demo first (90s) → tech briefly (45s) → ask (15s)** — without re-reading from notes, without live-coding-in-the-demo, and without exceeding 3:15 even with stumbles.
- **Anticipate** the five most-asked questions for the team's specific build, write a 30-second answer to each before the judging starts, and rehearse each answer aloud once so the answer surfaces from memory in the room.
- **Manage** the Q&A pattern — the *one-clarification-question* default, the *one-followup* expected, the rare *gotcha* — using the three named patterns from Lecture 3 (the technical gotcha, the market gotcha, the "but what about" stack), and the bridge sentence pattern that returns the conversation to the team's strongest answer.
- **Read** the room — the audience attention curve over a 3-minute pitch, the four named judge body-language cues (clipboard pickup, eye-contact loss, lean-back, side-glance), and the named recovery move for each cue.
- **Recover** from judging that feels unfair — the cohort-known patterns of bias (the demo went wrong, the judge missed the technical depth, the rubric weighted polish over substance), the C4 voice on what is fair to push back on and what is not, and the post-event channel for filing a *result review request* without burning bridges.
- **Be** a judge yourself when invited later — the sidebar on first-time judging (rubric pre-read, the table-walk rhythm, scoring discipline, the "do not coach" rule, the panel etiquette) — so the judging seat is not a surprise the first time it happens.

## Prerequisites

- **Week 8 completed.** `DAY-2-LOG.md` is committed; the submission package is in the repo; the demo video URL is live; the retro is logged; the follow-up issue is filed. Week 9 cannot start without the Week 8 artifacts because the rubric self-score and the mock pitch both run against the team's own real submission.
- **Weeks 1 through 6 completed.** The Hackathon Operating Document, the template repo, the solo prototype, the team contract, the scoping worksheet, and the three-minute solo demo recording. The mock pitch in Week 9 builds on the Week 6 solo script and the Week 8 team script.
- **A 3-minute timer.** Phone timer, kitchen timer, watch — anything that ticks visibly. The 3-minute cap is the binding constraint of the entire week. Rehearsing *without* a timer rehearses a different skill.
- **A camera-less or muted-camera rehearsal mode.** The judge-room is unrecorded. Rehearsing under recording is a different psychology than rehearsing under live unforgiving observation. The mini-project specifies how to simulate the unrecorded mode (camera-off video call with one teammate as judge proxy; or in-person with a chair-pointed-at-empty-chair if you have to).
- **A printed or screen-visible copy of three public rubrics.** Major League Hacking organizer guide rubric, NumFOCUS event playbook scoring rubric, and a Devpost public-event rubric from a past large hackathon (HackMIT, TreeHacks, PennApps, or any other event whose rubric is public). Links are in `resources.md`.

A reminder: the judge-room is **not** a real event. It is a rehearsal of the judge-room with the team's own submission. The judge proxy is a teammate or peer, not a real judge. The judging script is the *muscle*, not the verdict.

## Topics covered

- **The five rubric dimensions.** Technical complexity, design and UX, originality, polish, presentation. What each one is actually measuring; how public hackathons weight them; the unweighted-versus-weighted distinction.
- **Public rubric samples.** MLH organizer guide; NumFOCUS event playbook; Devpost public-event rubrics; GitHub Education's student-hackathon rubric pattern. The samples are the floor; events customise upward.
- **The two judging mindsets.** *Judge-as-engineer* (technical depth, scalability, code quality, engineering tradeoffs). *Judge-as-investor* (user pain, market size, would-you-pay, retention, the "would you keep building this" test). How to read which mindset is in the room within the first 20 seconds.
- **The 3-minute pitch arc that wins.** Four beats — problem (30s), demo first (90s), tech briefly (45s), ask (15s). The 30-90-45-15 distribution is the named C4 ratio. Why "demo first" matters more than "demo eventually."
- **The live-coding-in-the-demo trap.** Why almost no judging room rewards live coding mid-pitch; the named failure modes (the typo cascade, the API rate-limit, the localhost-not-deployed surprise); the C4 voice's directive — *do not live-code in a 3-minute pitch*.
- **The Q&A drill.** The five-question anticipation exercise. The 30-second answer cap. The bridge sentence pattern. The "I don't know" sentence pattern (it is allowed; it is sometimes the right answer).
- **Reading the room.** The audience attention curve over 3 minutes. The four judge body-language cues (clipboard pickup, eye-contact loss, lean-back, side-glance). The named recovery move per cue.
- **The unfair-judging conversation.** Cohort-known patterns; the C4 voice on what is fair to push back on; the *result review request* channel (where it exists); when to drop it and move on.
- **The sidebar — being a judge yourself.** First-time judging etiquette; the rubric pre-read; the table-walk rhythm; scoring discipline; the "do not coach" rule; panel-versus-table judging differences.
- **Panel-versus-table judging.** Two formats. Table-walk (judges rotate through team tables, ~4-minute slots, often 3 rotations of judges). Panel (team presents to a single seated panel, ~5-7 minutes, one rotation). Different cadence, different prep, different recovery moves.
- **The C4 voice on judging.** Judging is a *human assessment under constraint*, not a measurement. The team's job is to make the judge's job easy — clear narrative, clear evidence, clear ask. The judge's job is to score consistently across teams; the *consistency* is what the rubric is for.
- **The `JUDGE-ROOM-LOG.md` file format.** Three sections: rubric self-score, mock pitch take notes, mock Q&A transcript. Plus the engineer-versus-investor reflection paragraph.

## Weekly schedule

The schedule below adds up to approximately **11 hours** of structured work, plus an optional ~1 hour of stretch work in Challenge 1. The structured hours are the target; the mock-pitch rehearsals are the load test.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Lecture 1 — Rubrics and the two mindsets    |    1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0h       |    0.5h    |     2.5h    |
| Tuesday   | Exercise 1 — Self-score the team's submission |   0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Wednesday | Lecture 2 — The 3-minute arc and the live-coding trap |  1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     2.25h   |
| Thursday  | Lecture 3 — Q&A, reading the room, unfair judging |   1.5h  |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     2.25h   |
| Friday    | Exercise 2 + Exercise 3 — Q&A drill + cue drill |  0h    |    1.5h   |     0h     |    0.5h   |   0.5h   |     0.5h     |    0h      |     3h      |
| Saturday  | **Mini-project — Mock pitch + mock Q&A (take 1 and take 2)** |   0h    |    0h     |     0h     |    0h     |   0h     |     2.5h     |    0h      |     2.5h    |
| Sunday    | **Mini-project — Self-score + reflection** + quiz + challenge (optional) | 0h | 0h | 1h | 0.5h | 0.5h | 1.5h | 0h | 3.5h |
| **Total** |                                             | **4.5h** | **2.5h**  | **1h**     | **2h**    | **2h**   | **5.25h**    | **0.5h**   | **~17.75h** |

The ~18-hour total is dense but lighter than Week 7 or Week 8 because there is no 24-hour wall-clock dry-run. The mini-project this week is bounded — about 5 hours over a weekend, not a continuous overnight run. The lectures and exercises remain the bulk of the prep; the mock pitch is the load test that confirms the prep worked.

The optional **Challenge 1 — Be a Judge for Another Team's Submission** lives outside the structured target. Trade `DAY-2-LOG.md` and demo video links with another C4 team or cohort peer, apply the five-dimension rubric, write a one-page scoring sheet, and (if the other team consents) deliver the score with one positive note and one growth note. The skill is *being a judge*, not just *being judged*.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./00-overview.md) | This overview (you are here) |
| [resources.md](./01-resources.md) | MLH organizer guide, NumFOCUS playbook, Devpost help, public rubrics, public judge memoirs, the GitHub student dev pack list |
| [lecture-notes/01-rubrics-and-mindsets.md](./02-lecture-notes/01-rubrics-and-mindsets.md) | The five rubric dimensions; public rubric samples (MLH, NumFOCUS, Devpost); judge-as-engineer vs judge-as-investor |
| [lecture-notes/02-the-three-minute-arc.md](./02-lecture-notes/02-the-three-minute-arc.md) | The 30-90-45-15 pitch arc; demo-first; the live-coding trap; the named failure modes; how to lock the script under fatigue |
| [lecture-notes/03-qna-room-and-unfair-judging.md](./02-lecture-notes/03-qna-room-and-unfair-judging.md) | The Q&A drill (5 anticipated questions, 30-second cap, bridge sentence); reading the room (attention curve, four cues, recovery moves); the unfair-judging conversation; the be-a-judge sidebar |
| [exercises/exercise-01-self-score.md](./03-exercises/exercise-01-self-score.md) | Apply the five-dimension rubric to the team's own Week 8 submission |
| [exercises/exercise-02-qna-drill.md](./03-exercises/exercise-02-qna-drill.md) | Generate and answer the five most-asked questions for the team's build |
| [exercises/exercise-03-cue-drill.md](./03-exercises/exercise-03-cue-drill.md) | Match four judge body-language cues to the four named recovery moves |
| [exercises/SOLUTIONS.md](./03-exercises/SOLUTIONS.md) | One defensible solution per exercise |
| [exercises/pitch_timer.py](./03-exercises/pitch_timer.py) | A small CLI timer with the 30-90-45-15 beats baked in |
| [exercises/rubric_score.py](./03-exercises/rubric_score.py) | A small CLI scorer that adds five dimensions and prints the weighted total |
| [challenges/README.md](./04-challenges/00-overview.md) | Index of optional challenges |
| [challenges/challenge-01-be-a-judge.md](./04-challenges/challenge-01-be-a-judge.md) | Acceptance criteria for scoring another team's submission |
| [quiz.md](./05-quiz.md) | 10 multiple-choice questions on rubrics, the 3-minute arc, and the Q&A drill |
| [homework.md](./06-homework.md) | Six practice problems for the week |
| [mini-project/README.md](./07-mini-project/00-overview.md) | The mock-pitch-and-Q&A spec, the `JUDGE-ROOM-LOG.md` template, and the acceptance criteria |

## Stretch goals

If you finish the mini-project on Sunday and want to push further, try any of the following. None substitute for the mock pitch — commit the mock-pitch take notes first, every time.

- **Run the mock pitch with a stranger as judge proxy.** A friend who has not heard the build before is the closest analogue to a real judge. The first-time-listener reactions surface the parts of the script that assume insider context.
- **Re-record the demo video using the Week 9 arc.** The Week 8 demo was a screen-recording; some learners' Week 8 demos do not follow the 30-90-45-15 ratio. Re-record once, with the timer in shot, using the arc — the second version is usually noticeably tighter even when the build is identical.
- **Read three public hackathon retrospectives, this time looking only at the judging paragraphs.** Most Devpost retros mention the judges by role (table judges, panel judges, sponsor judges) and the lessons the team drew. Pattern-match three retros' judging takeaways into a one-page memo.
- **Run a mock Q&A with five anticipated questions plus three surprise questions.** The surprise questions test the *bridge sentence pattern* (Lecture 3 §3). The team's recovery move on a question they did not anticipate is the muscle that matters most.
- **Apply the Lecture 3 sidebar — be a judge — to a public Devpost gallery.** Browse three public submissions from a recent Devpost hackathon; score each with the five-dimension rubric; identify which one you would shortlist. The exercise sharpens the *grader's eye*.
- **Compare the team's Week 6 solo recording, Week 8 team recording, and Week 9 mock pitch.** Three takes of approximately the same content across three different rehearsal modes. The deltas tell the team where their delivery has improved and where it has not.

## Up next

Continue to **Week 10 — Post-Event Carry-Out and Open-Source Follow-Through** once your `JUDGE-ROOM-LOG.md` is committed, the rubric self-score is in place, the mock-pitch take notes are logged, your three exercises are done, your quiz is at 9/10 or better, and (if you ran Challenge 1) the be-a-judge scorecard is shared. Week 10 takes the *finished hackathon artifact* and treats it as a *starting point for ongoing work* — the post-event PR pass, the issue triage, the README-for-the-internet edit, the open-source contribution rhythm. Week 9 took the demo into the room; Week 10 takes it back out of the room and into the long term.

---

*The win is shipping. You shipped solo in Week 3. You wrote the contract in Week 4, the map in Week 5, the script in Week 6. The team ran the first 12 hours in Week 7 and the closing 12 in Week 8. Week 9 puts the demo in front of judges. Four minutes. One ask. The rubric is the bench; the pitch is the run; the score is the measurement; the lesson is what you bring to the next event.*

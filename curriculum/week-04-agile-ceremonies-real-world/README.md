# Week 4 — Agile Ceremonies, Real-World Version

Welcome to **Week 4** of **C4 · Crunch Labs Hackathons**. Week 3 made you feel the rhythm of a six-hour build alone. Week 4 puts three to five people in the room with you and asks: can that rhythm survive contact with other humans? The job this week is to compress the three Agile ceremonies — stand-up, demo, retro — into shapes that fit *inside* a 36-hour event, learn to point a story under deadline pressure, and rehearse the single most under-practiced skill on a hackathon team: saying "no" to scope without breaking the room.

If Week 3 was the first lap on the track, Week 4 is the first lap with a partner on the inside of the lane. You will not yet be running a 36-hour event — that is Week 7. You will not yet be in the real event — that is Week 10. This week is the team-mode rehearsal: the loop you already ran alone, now run with witnesses, with a written contract, and with the muscle of saying no.

The deliverable is a **one-page team contract template** committed to your repo — the artifact you bring to the next event and hand to a team of strangers in the first hour. Every following week — and every future event — leans on this template being honest about how your team will run stand-ups, cut scope, and disagree.

## Learning objectives

By the end of this week, you will be able to:

- **Defend** the three Agile ceremonies — stand-up, demo, retro — as *compression targets*, not as ceremonies-for-their-own-sake. Each has a job, a length cap, and a failure mode if you stretch it.
- **Run** a 60-second team stand-up that produces a written board update and a named cut decision, with a rotating timekeeper, not a manager.
- **Run** a 15-minute mid-event team demo to your own teammates (not judges) at the 12-hour and 24-hour marks. Internal demos are where scope dies cleanly; do them.
- **Run** a 30-minute team retro at hour 36 (or the end of any sprint) that produces a written three-behavior change list per teammate.
- **Story-point** a backlog under time pressure using a simple 1-2-3-5 scale (no Fibonacci theatre) and a planning-poker round that fits in 10 minutes for ten items.
- **Apply** the "saying no" script: three concrete sentences that cut a scope request *without* breaking the room or making a teammate feel stupid for asking.
- **Detect** the four most common ceremony failure modes — the silent stand-up, the demo-as-showcase, the blame retro, the points-as-promises — and name them when you see them happen.
- **Commit** a one-page team contract template that names how *your* team runs stand-ups, decides cuts, points stories, and handles disagreement. The template is reusable. You bring it to every event from Week 10 onward.

## Prerequisites

- **Week 1 completed.** Your Hackathon Operating Document is committed, you know your default role, and the demo-or-die doctrine is familiar.
- **Week 2 completed.** Your `hackathon-template` repo is public and `bootstrap.sh` produces a live deploy URL.
- **Week 3 completed.** You have shipped one solo build, recorded one demo, and written one structured retro. You know what the loop *feels* like alone.
- **A scratch file or notebook.** You will draft contract language, practice scripts, and pointing rounds on paper before committing. Do not write the contract for the first time in your editor.

You do not need a team this week. Most of the drills work solo with imagined teammates. The optional challenge (Challenge 1) adds a real partner for a 30-minute scope-stress drill if you can find one; the mini-project does not require it.

## Topics covered

- The three Agile ceremonies under hackathon compression — what each is *for* at 36 hours, not at three weeks
- The 60-second team stand-up — the four questions, the rotating timekeeper, the written board update
- The internal mid-event demo — the 12h and 24h checkpoints, the "what would a stranger see" test, the cut-or-keep call
- The 30-minute team retro — the keep / start / stop columns at team scale, the three-behavior list per teammate
- Story-pointing under time pressure — the 1-2-3-5 scale, planning-poker in ten minutes, points-as-relative-size not as time
- The "saying no" script — three concrete sentences that cut scope without breaking the room
- Scope creep at hour 2, hour 12, hour 24 — the predictable shapes and the script that meets each one
- The four ceremony failure modes — silent stand-up, demo-as-showcase, blame retro, points-as-promises
- Why the team contract is the most under-valued artifact a hackathon team brings to the room
- The one-page contract template — sections, voice, what to leave blank vs what to fill before the event
- Reading a teammate's stand-up update — what to look for, what to ignore, when to call a sync
- The bridge from solo loop to team loop — what transfers cleanly, what does not, what needs new muscle

## Weekly schedule

The schedule below adds up to approximately **10 hours**. Treat it as a target. Unlike Week 3, no single day is a six-hour build — this week is conceptual and rehearsal-heavy. The mini-project is a one-page contract template, which takes one focused session, not a Saturday block.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | Lecture 1 — Stand-up, demo, retro compressed |    1h    |    0h     |     0h     |    0h     |   0.5h   |     0h       |    0.5h    |     2h      |
| Tuesday   | Exercise 1 — The 60-second stand-up          |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Wednesday | Lecture 2 — Story pointing and saying no     |    1h    |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Thursday  | Exercise 2 — Planning-poker round            |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Friday    | Exercise 3 — The "saying no" script          |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Saturday  | **Mini-project — Team contract template**    |    0h    |    0h     |     0h     |    0h     |   0h     |     2h       |    0h      |     2h      |
| Sunday    | Quiz + challenge (optional) + polish         |    0h    |    0h     |     1h     |    0.5h   |   0.5h   |     0.5h     |    0h      |     2.5h    |
| **Total** |                                             | **2h**   | **3h**    | **1h**     | **1.5h**  | **2h**   | **3.25h**    | **0.5h**   | **~13.25h** |

The base ten-hour target excludes Challenge 1 (Scope Stress Drill). If you do the challenge, expect 11–12 hours total. The mini-project is the artifact you keep; the exercises are the drills that make the contract honest.

The optional **Challenge 1 — Scope Stress Drill** lives outside the ten-hour target. Pair it with a Week 3 partner if you have one; otherwise simulate solo and note the limitation in the retro.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | Atlassian, Scrum.org, planning-poker tools, retro templates, free MoSCoW refreshers |
| [lecture-notes/01-stand-up-demo-retro-compressed.md](./lecture-notes/01-stand-up-demo-retro-compressed.md) | The three ceremonies, compressed to hackathon time; failure modes; the rotating timekeeper |
| [lecture-notes/02-story-pointing-and-saying-no.md](./lecture-notes/02-story-pointing-and-saying-no.md) | The 1-2-3-5 scale; planning-poker under 10 minutes; the three-sentence "no" script |
| [exercises/README.md](./exercises/README.md) | Index of short exercises |
| [exercises/exercise-01-60-second-standup.md](./exercises/exercise-01-60-second-standup.md) | Draft and dry-run a 60-second stand-up update |
| [exercises/exercise-02-pointing-poker.md](./exercises/exercise-02-pointing-poker.md) | Point a 10-item backlog with the 1-2-3-5 scale in 10 minutes |
| [exercises/exercise-03-saying-no-script.md](./exercises/exercise-03-saying-no-script.md) | Write your three-sentence "no" script for the three scope-creep shapes |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-scope-stress-drill.md](./challenges/challenge-01-scope-stress-drill.md) | A 30-minute paired drill that injects scope requests on a clock |
| [quiz.md](./quiz.md) | 10 multiple-choice questions |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | The one-page team contract template |

## Stretch goals

If you finish the contract on Saturday and want to push further, try any of the following. None of these substitutes for the contract — write the contract first, every time.

- **Run the Exercise 1 stand-up against a real human.** A roommate, a sibling, a club-mate. Ask them to time you at 60 seconds and stop you at the dot. Their feedback on whether your update was a status report or an actual stand-up is gold.
- **Trade contracts with another C4 learner.** Read theirs. Note one section yours is missing. The contract you would bring to a real event is the union of three good contracts you read, not the first draft you wrote alone.
- **Watch a real Scrum master run a stand-up on YouTube at 1.5x speed.** Note where they cut someone off. The cut is the skill, not the listening.
- **Re-read your Week 3 retro alongside Lecture 2 §3 (saying no).** Which of the three retro behaviors you named is *really* a "I needed to say no earlier" behavior in disguise? That is a Week 4 insight applied to last week's data.
- **Build a planning-poker round with three friends over a 15-minute video call.** Use the backlog from Exercise 2 or steal a real one from a public GitHub repo's Issues. The first round is awkward; the second is calmer; the third is fast. The skill is the calmer.

## Up next

Continue to **Week 5 — Scoping Discipline** once your team contract is committed, your three exercises are complete, and your quiz is at 9/10 or better. In Week 5 you will deepen MoSCoW into a *36-hour scoping worksheet* — the artifact that turns the contract you wrote this week into a cut-list you can hold under the real clock. The ceremonies you compressed this week are the rhythm; the scoping you sharpen next week is the discipline that lets the rhythm survive contact with a hard deadline.

---

*The win is shipping. You shipped one alone. Now you are learning the words that let a team ship together.*

# Week 3 — Solo Prototype Sprint

Welcome to **Week 3** of **C4 · Crunch Labs Hackathons**. Week 1 changed how you *see* the event. Week 2 changed what is *on your laptop* before the event opens. Week 3 changes the rhythm in your hands. The job this week is simple to describe and uncomfortable to live: pick a tiny real prompt, run a six-hour solo build on top of your `hackathon-template`, ship a deployed URL, and write a structured retro that names three behaviors you will change at the next event.

If Week 2 was the toolkit, Week 3 is the **first lap on the track**. You will not have a team. You will not have a sponsor track. You will not be allowed to extend the clock. You will ship something small, end-to-end, and the only thing that matters is whether a stranger can click your link and see it work. This week is when the words "the win is shipping" stop being a slogan and start being a feeling.

The deliverable is a public, live-deployed solo prototype, a recorded three-minute demo, and a written retro committed alongside it. Every following week — and every future event — rides on this loop being honest. If you fake a green deploy here, you will fake it under real pressure too, and the team will notice.

## Learning objectives

By the end of this week, you will be able to:

- **Defend** the six-hour solo build as a *rehearsal*, not a performance: the point is to feel the rhythm of "demo or die," not to impress anyone.
- **Pick** a real, narrow prompt — a single user pain you can name in one sentence — and resist the urge to broaden it.
- **Scope** a solo build into MoSCoW on a six-hour clock, where "MUST" is one feature you can demo, not three.
- **Apply** the **hourly cut reflex**: every hour, on the hour, you ask "what do I cut to still ship?" and you actually cut.
- **Run** `./bootstrap.sh` from your Week 2 template into a fresh event repo and have a live deploy URL by the end of hour one.
- **Record** a credible three-minute demo of your own work — hook, problem, solution, ask — with a working live URL on screen.
- **Run** a structured blameless retro on yourself: what worked, what hurt, what the next event needs you to do differently.
- **Name** three specific behaviors — not goals, not vibes — that you will change at the next build, and write them down where you will see them.

## Prerequisites

- **Week 1 completed.** Your Hackathon Operating Document is committed and you know which of the four roles you default to.
- **Week 2 completed.** Your `hackathon-template` repo is public, `./bootstrap.sh` produces a live deploy URL, and the CI badge is green.
- **A six-hour block of time.** Continuous. Phone face-down. No meetings. The clock is the lecture.
- **A free OBS Studio (or Loom) install.** You will record a three-minute demo on Saturday. Install before Wednesday.

You do not need a team this week. You do not need a sponsor prompt. You need your laptop, your template, and one honest sentence about who hurts.

## Topics covered

- The six-hour solo build as a rehearsal — why the clock is the lecture
- The "demo or die" doctrine, applied alone: if the URL is not live at hour six, the project does not exist
- Picking a real prompt: one user, one pain, one sentence, one demo path
- Scoping a solo build into MoSCoW where MUST has one item
- The opening-hour ritual: `./bootstrap.sh`, deploy, blank page live, then *and only then* feature code
- The hourly cut reflex: a 60-second self stand-up every hour, on the hour
- The hour-five freeze: the last hour is for the demo path, not for new code
- The three-minute solo demo: hook (30s) → problem (45s) → solution (90s) → ask (15s)
- The structured post-build retro: keep / start / stop, plus the three-behaviors-to-change line
- Blameless retro voice, applied to yourself: "the sprint board didn't catch X" not "I am bad at X"
- Common solo-build failure modes: scope creep at hour two, polish before deploy, no demo recording, no retro
- Why the retro is the most under-valued artifact in the week — and the most valuable for Week 4 onward

## Weekly schedule

The schedule below adds up to approximately **10 hours**. Treat it as a target. The six-hour solo build is one continuous block on Saturday — do not split it across two evenings or you will lose the rhythm the lecture is teaching you.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | The six-hour solo build doctrine             |    1h    |    0h     |     0h     |    0h     |   0.5h   |     0h       |    0.5h    |     2h      |
| Tuesday   | Pick a real prompt (Exercise 1)              |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Wednesday | The six-hour clock (Exercise 2)              |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Thursday  | The post-build retro doctrine                |    1h    |    0h     |     0h     |    0.25h  |   0.25h  |     0.25h    |    0h      |     1.75h   |
| Friday    | The three-minute demo (Exercise 3) prep      |    0h    |    1h     |     0h     |    0h     |   0.25h  |     0.25h    |    0h      |     1.5h    |
| Saturday  | **The six-hour solo build (mini-project)**   |    0h    |    0h     |     0h     |    0h     |   0h     |     6h       |    0h      |     6h      |
| Sunday    | Quiz, retro, record demo, polish submission  |    0h    |    0h     |     0h     |    0.5h   |   0.5h   |     1h       |    0h      |     2h      |
| **Total** |                                             | **2h**   | **3h**    | **0h**     | **1.25h** | **2h**   | **8h**       | **0.5h**   | **~16.75h** |

The week's hour budget is genuinely larger than ten because the mini-project *is* a six-hour solo build. The build replaces the homework slot, not adds to it. If your time budget is strict ten hours, drop two homework problems and keep the build full-length. The build is the week. Everything else is supporting cast.

The optional **Challenge 1 — Pair Prototype** lives outside the ten-hour target. Do it next week or next event if you cannot fit it in. Do not skip the solo build to make room for the pair build.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | OBS Studio, Loom, MoSCoW reminders, free retro templates |
| [lecture-notes/01-the-six-hour-solo-build.md](./lecture-notes/01-the-six-hour-solo-build.md) | The solo build doctrine; scope; hourly cut reflex; demo or die |
| [lecture-notes/02-the-post-build-retro.md](./lecture-notes/02-the-post-build-retro.md) | The structured retro; blameless voice; three behaviors to change |
| [exercises/README.md](./exercises/README.md) | Index of short exercises |
| [exercises/exercise-01-pick-a-real-prompt.md](./exercises/exercise-01-pick-a-real-prompt.md) | Pick the one-sentence prompt your solo build will answer |
| [exercises/exercise-02-the-six-hour-clock.md](./exercises/exercise-02-the-six-hour-clock.md) | Pre-build the MoSCoW chart and the hourly clock on paper |
| [exercises/exercise-03-the-three-minute-demo.md](./exercises/exercise-03-the-three-minute-demo.md) | Draft the three-minute demo script before you write the code |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-pair-prototype.md](./challenges/challenge-01-pair-prototype.md) | Run the same six-hour build paired with another C4 learner |
| [quiz.md](./quiz.md) | 10 multiple-choice questions |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | The six-hour solo build + recorded demo + written retro |

## Stretch goals

If you finish the build with time to spare on Saturday and want to push further, try any of the following. None of these substitutes for the retro — write the retro first, every time.

- **Re-record the demo once.** The first take is rehearsal. The second take is the take. Most learners watch their first take and immediately know two things to fix.
- **Show the demo to one person who has not been in your build.** A roommate, a sibling, a club-mate. Ask them: "what is the problem this solves?" If they cannot answer in one sentence, your hook is broken — fix it in the retro.
- **Read another C4 learner's retro alongside yours.** Notice which "behaviors to change" overlap. Patterns across solo builds are signal about what the team-mode weeks (4–8) will need to teach you.
- **Re-run `bootstrap.sh` with the lessons you learned.** Found one friction point in the template during the build? Fix it Sunday night and version-log the change. Your template gets sharper every week.
- **Watch one Devpost winner's three-minute demo at 0.5x speed** with your own demo script open in another tab. Note where they put the live URL on screen and how long the demo crash-safe-paths are.

## Up next

Continue to **Week 4 — Agile Ceremonies, Real-World Version** once your solo build is live, your demo is recorded, and your retro is committed. In Week 4 you will take the same loop — scope, build, demo, retro — and learn how a team of three to five compresses it inside a 36-hour event. The solo loop you just felt this week is the loop you will run *together* there.

---

*The win is shipping. You are about to ship one alone. Then we ship together.*

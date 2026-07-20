# Week 1 — The Hackathon Mental Model

Welcome to **C4 · Crunch Labs Hackathons**, a free, open-source ten-week prep cycle for hackathons. Week 1 is the cheap week — no stack setup, no code under deadline, no team contract negotiation. It is the week you change how you see the event format itself.

If you have never been to a hackathon, you probably picture it like this: "smart people sit in a room for 36 hours, invent something brilliant, and judges hand out prizes for the most innovative idea." That is wrong on every clause. By Sunday you will hold a different and far more useful model: hackathons reward **clarity, scope discipline, and demo-ability** far more than novelty, and the teams that win are the teams that obey the 12-hour rule and the demo-or-die doctrine. We will spend the week pressure-testing that model against real past projects, against your own strengths, and against the team you will eventually walk into the event with.

The deliverable for the week is a single one-page personal brief — your strengths, your default role on a team, your preferred stack — that you will reference at every event you attend from this point forward.

## Learning objectives

By the end of this week, you will be able to:

- **State** the four-axis judging rubric most real hackathons use (problem clarity, technical depth, demo-ability, polish) and explain why "innovative idea" rarely wins.
- **Apply** the **12-hour rule** to a hypothetical 36-hour project: at hour 12, the remaining scope must fit in the remaining time *plus a 30% buffer*, or you cut.
- **Apply** the **demo-or-die doctrine**: if it does not appear in the three-minute demo, it does not exist in the judges' eyes.
- **Draw** a **MoSCoW** scoping chart (Must, Should, Could, Won't) for a real or hypothetical hackathon prompt.
- **Identify** the four canonical team roles (PM / scope-keeper, full-stack builder, designer, pitch lead) and place yourself on that map honestly.
- **Distinguish** hackathon formats — 24h vs 36h vs 48h vs week-long, in-person vs virtual, college vs sponsor vs themed — and explain how the format changes the optimal strategy.
- **Reason** about the **sponsor-prize layer** as game theory: which prize tracks are crowded, which are under-attended, which fit your team's actual skill.
- **Rate** any past Devpost project against the rubric in under five minutes.

## Prerequisites

- **C1 Weeks 1–7** (or equivalent Python).
- **Comfortable Git / GitHub** — you can branch, push, open a PR.
- **Willingness to attend a hackathon.** This is non-negotiable; the capstone is event-driven.

You do not need to know React, FastAPI, or any specific stack yet. Week 2 sets up the stack.

## Topics covered

- What hackathons actually reward — the real rubric vs the imagined one
- Why "boring idea, demoed flawlessly" beats "novel idea, half-broken"
- The four-axis judging model: problem clarity, technical depth, demo-ability, polish
- The sponsor-prize layer — read the prizes before you pick a project
- The four canonical roles: PM / scope-keeper, full-stack builder, designer, pitch lead
- Hackathon formats: 24h, 36h, 48h, week-long; in-person vs virtual; college vs sponsor vs themed
- The **12-hour rule**: feasibility check at the midpoint, scope cuts in the second half
- The **demo-or-die doctrine**: every feature must appear in the three-minute demo or it does not exist
- The **MoSCoW chart** (Must, Should, Could, Won't) as the team's operating document
- The "what do we cut?" reflex — applied hourly, not at the deadline
- Ceremonies under time pressure: the 12-hour stand-up, the 24-hour mid-event retro, the final-3-hour freeze
- Reading past Devpost winners and reverse-engineering the win

## Weekly schedule

The schedule below adds up to approximately **10 hours**. Treat it as a target. Some sections will click in 20 minutes, others will take longer. That's fine.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | What hackathons actually reward             |    1h    |    0.5h   |     0h     |    0h     |   0.5h   |     0h       |    0h      |     2h      |
| Tuesday   | Rate five real Devpost projects             |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0h       |    0.25h   |     1.75h   |
| Wednesday | The 12-hour rule + demo-or-die              |    1h    |    0h     |     0h     |    0.25h  |   0.5h   |     0.25h    |    0h      |     2h      |
| Thursday  | Team contract draft + role assessment       |    0h    |    1h     |     0h     |    0h     |   0.5h   |     0.5h     |    0h      |     2h      |
| Friday    | The 12-hour solo build (optional)           |    0h    |    0h     |     1.5h   |    0h     |   0h     |     0.25h    |    0.25h   |     2h      |
| Saturday  | Personal brief deep work                    |    0h    |    0h     |     0h     |    0h     |   0.25h  |     1h       |    0h      |     1.25h   |
| Sunday    | Quiz, review, polish the brief              |    0h    |    0h     |     0h     |    0.5h   |   0h     |     0.25h    |    0h      |     0.75h   |
| **Total** |                                             | **2h**   | **2.5h**  | **1.5h**   | **1h**    | **2h**   | **2.25h**    | **0.5h**   | **~12h**    |

If you only have a strict 10 hours, drop the optional **Challenge 1** (the 12-hour solo build). It is the most valuable single thing you can do this week if you can afford the time, but it is genuinely optional.

## How to navigate this week

| File | What's inside |
|------|---------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | Major League Hacking, Devpost, free MoSCoW references |
| [lecture-notes/01-what-hackathons-actually-reward.md](./lecture-notes/01-what-hackathons-actually-reward.md) | The real rubric, roles, formats, sponsor-prize layer |
| [lecture-notes/02-the-12-hour-rule-and-demo-or-die.md](./lecture-notes/02-the-12-hour-rule-and-demo-or-die.md) | Mid-event feasibility, demo-or-die, MoSCoW, the cut reflex |
| [exercises/README.md](./exercises/README.md) | Index of short exercises |
| [exercises/exercise-01-personal-brief.md](./exercises/exercise-01-personal-brief.md) | Draft your one-page personal brief |
| [exercises/exercise-02-rate-five-real-hackathon-projects.md](./exercises/exercise-02-rate-five-real-hackathon-projects.md) | Score five Devpost winners against the rubric |
| [exercises/exercise-03-team-contract-draft.md](./exercises/exercise-03-team-contract-draft.md) | Adapt a team contract template for your next event |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-12-hour-solo-build.md](./challenges/challenge-01-12-hour-solo-build.md) | The canonical small solo build, to feel the rhythm |
| [quiz.md](./quiz.md) | 10 multiple-choice questions |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | Your personal Hackathon Operating Document |

## Stretch goals

If you finish early and want to push further, try any of the following:

- Read Major League Hacking's [Guide to Your First Hackathon](https://hackp.ac/mlh-guidebook) end to end and note one habit you want to copy.
- Pick any Code Crunch hackathon from the [SPRING-2025/](../../SPRING-2025/) archive (or any future archived event) and read every submission's README in one sitting. You will see patterns immediately.
- Skim the original MoSCoW paper by Dai Clegg (1994). You do not need the original, but seeing the framework's origins outside of agile-blog rewrites is grounding: <https://en.wikipedia.org/wiki/MoSCoW_method>
- Watch any DevPost winner's three-minute demo at 0.5x speed and write down every second they "show, don't tell." You will learn more from one demo at half-speed than from ten at normal speed.

## Up next

Continue to **Week 2 — Rapid-Prototyping Toolkit Setup** once your personal brief is pushed to GitHub. In Week 2 you will install the team stack (React + FastAPI or Express + Postgres or SQLite + Vercel/Railway) and turn your laptop into a one-command project-scaffold machine.

---

*The win is shipping, not innovating. Bring this sentence to every hackathon you attend.*

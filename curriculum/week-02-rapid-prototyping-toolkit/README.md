# Week 2 — Rapid-Prototyping Toolkit Setup

Welcome to **Week 2** of **C4 · Crunch Labs Hackathons**. Week 1 changed how you *see* the event. Week 2 changes what is *on your laptop* before the next event opens. The job this week is unglamorous and decisive: turn your machine into a one-command project-scaffold machine, so the first six hours of an event are not spent on `npm create`, `pip install`, deploy-config, and "wait, who has the env var?"

If Week 1 was the mental model, Week 2 is the **toolkit**. Specifically: a personal `hackathon-template` repo on your GitHub, a tested `./bootstrap.sh new-event-name` script, a pre-tuned deploy pipeline, and a stack you already know cold. You will write almost no product code this week. You will instead pay down all the setup tax that every hackathon team usually pays *during* the event.

The deliverable is your personal `hackathon-template` repo, polished and on GitHub, with a one-command scaffold script that gets you from "I just heard the prompt" to "live deploy URL with my name on it" in under thirty minutes. Every subsequent week — and every subsequent event — leans on this.

## Learning objectives

By the end of this week, you will be able to:

- **Defend** the "boring stack" doctrine: pick technology your team already knows, never the new shiny one, and explain *why* in scope-discipline terms.
- **Stand up** the default Code Crunch stack (React + Vite, FastAPI, SQLite or Supabase free tier, Vercel + Railway deploy) from a cold machine in under thirty minutes.
- **Identify** the stack alternates (Next.js full-stack, T3, Astro + SQLite) and reason about when each is the right pick instead of the default.
- **Apply** the **30-minute scaffold-to-first-route rule**: from `git clone` to a live deploy URL returning a real HTTP response should not exceed thirty minutes.
- **Build** a personal `hackathon-template` GitHub repo containing a pre-tuned `.gitignore`, `.env.example`, README skeleton, deploy config, and minimal CI.
- **Run** a `./bootstrap.sh <new-event-name>` script that clones, renames, configures, and pushes a new event repo in a single command.
- **Refuse** the "we'll learn $newtech during the event" pitch when a teammate proposes it, and explain why it loses.
- **Iterate** the template after each event, leaving versioned notes for the next iteration.

## Prerequisites

- **Week 1 completed.** Your Hackathon Operating Document is committed and Section 3 (stack defaults) is filled in.
- **A GitHub account.** Free is fine. SSH or HTTPS push working.
- **Node.js 20+ and Python 3.11+ installed.** If either is missing, fix that before Tuesday.
- **A Vercel account and a Railway (or Fly.io) account.** Both free tiers. Sign up Monday, do not wait until Friday.

You do not need to have built a React app from scratch before. You do not need to be fluent in FastAPI. You need to be willing to wire scaffolding, not write product features.

## Topics covered

- The "boring stack" doctrine: why the team's known tools beat the conference's hot tools
- The default Code Crunch stack: React (Vite) + FastAPI + SQLite or Supabase + Vercel + Railway
- Stack alternates: Next.js full-stack; the T3 stack; Astro + SQLite for content-heavy events
- The "we'll learn $newtech at the event" anti-pattern and why it loses
- The 30-minute scaffold-to-first-route rule
- The `hackathon-template` repo as a personal artifact, versioned across events
- One-command spin-up: `./bootstrap.sh <new-event-name>` and what it must do
- Pre-tuned files: `.gitignore`, `.env.example`, README skeleton, deploy config, CI
- Pre-installed UI scaffolding: Tailwind, shadcn/ui, react-query, FastAPI auth shell
- The "live blank page at hour 2" rule, instantiated as a deploy-on-first-commit pipeline
- Versioning the template: every event leaves a note in the next iteration
- Common newcomer setup mistakes: secrets in commits, missing `.env.example`, hard-coded localhost URLs, untested deploys

## Weekly schedule

The schedule below adds up to approximately **10 hours**. Treat it as a target. Some sections will click in 20 minutes, others will take longer. That is fine.

| Day       | Focus                                       | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Self-Study | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|-----------:|------------:|
| Monday    | The boring stack doctrine                    |    1h    |    0h     |     0h     |    0h     |   0.5h   |     0h       |    0.5h    |     2h      |
| Tuesday   | Stand up the template repo                   |    0h    |    1h     |     0h     |    0.25h  |   0.25h  |     0.5h     |    0h      |     2h      |
| Wednesday | The template-repo pattern                    |    1h    |    0h     |     0h     |    0.25h  |   0.25h  |     0.5h     |    0h      |     2h      |
| Thursday  | One-command spinup (`bootstrap.sh`)          |    0h    |    1h     |     0h     |    0h     |   0.5h   |     0.5h     |    0h      |     2h      |
| Friday    | Deploy to staging on first commit            |    0h    |    1h     |     0h     |    0h     |   0.25h  |     0.25h    |    0h      |     1.5h    |
| Saturday  | Shave 30 minutes off your spinup (optional)  |    0h    |    0h     |     1.5h   |    0h     |   0.25h  |     0.25h    |    0h      |     2h      |
| Sunday    | Quiz, polish the template, version the notes |    0h    |    0h     |     0h     |    0.5h   |   0.25h  |     0.25h    |    0h      |     1h      |
| **Total** |                                             | **2h**   | **3h**    | **1.5h**   | **1h**    | **2.25h**|  **2.25h**   | **0.5h**   | **~12.5h**  |

If you only have a strict 10 hours, drop **Challenge 1** (the 30-minute shave). It is the most valuable single thing you can do this week if you can afford the time, but it is genuinely optional. The mini-project is not optional.

## How to navigate this week

| File | What is inside |
|------|----------------|
| [README.md](./README.md) | This overview (you are here) |
| [resources.md](./resources.md) | Vite, FastAPI, Vercel, Railway, Supabase, shadcn/ui — the free reading list |
| [lecture-notes/01-the-hackathon-stack-choice.md](./lecture-notes/01-the-hackathon-stack-choice.md) | The boring stack doctrine; default + alternates; the 30-minute rule |
| [lecture-notes/02-the-template-repo-pattern.md](./lecture-notes/02-the-template-repo-pattern.md) | The personal template repo; `bootstrap.sh`; versioning across events |
| [exercises/README.md](./exercises/README.md) | Index of short exercises |
| [exercises/exercise-01-stand-up-the-template.md](./exercises/exercise-01-stand-up-the-template.md) | Create the `hackathon-template` repo and push a working scaffold |
| [exercises/exercise-02-one-command-spinup.md](./exercises/exercise-02-one-command-spinup.md) | Write and test `./bootstrap.sh new-event-name` |
| [exercises/exercise-03-deploy-to-staging.md](./exercises/exercise-03-deploy-to-staging.md) | Wire Vercel + Railway so the first push goes live |
| [challenges/README.md](./challenges/README.md) | Index of optional challenges |
| [challenges/challenge-01-shave-30-min-off-spinup.md](./challenges/challenge-01-shave-30-min-off-spinup.md) | Profile and shave 30 minutes off your end-to-end spinup |
| [quiz.md](./quiz.md) | 10 multiple-choice questions |
| [homework.md](./homework.md) | Six practice problems for the week |
| [mini-project/README.md](./mini-project/README.md) | The mini-project: your `hackathon-template` repo, polished and public |

## Stretch goals

If you finish early and want to push further, try any of the following:

- Mirror the same template for a **second stack** (e.g., Next.js full-stack) on a side branch. You may run into an event where the team picks differently than your default; the cost of switching should be one branch swap.
- Add a one-line **observability hook** (a logging line that prints request count to stdout). Hackathon teams almost never have logging; you can ship two demos with the same effort.
- Write a **post-mortem of your last yak-shaving session** at any earlier hackathon or class project. What did you waste time on? Add that lesson to the template.
- Read one well-organized open-source starter (e.g. [`create-t3-app`](https://create.t3.gg/), [`vite-react-ts-tailwind-starter`](https://github.com/wtchnm/Vitamin), or any FastAPI starter on the FastAPI docs site) and steal exactly one good idea.

## Up next

Continue to **Week 3 — Solo Prototype Sprint** once your `hackathon-template` repo is public and `./bootstrap.sh` produces a live deploy URL in under thirty minutes. In Week 3 you will run a six-hour solo build *on top of this template*, which is the first time the week's investment pays back with interest.

---

*The win is shipping. Setup is half the ship. Pay the tax once, on a calm day, and never pay it again at hour two of an event.*

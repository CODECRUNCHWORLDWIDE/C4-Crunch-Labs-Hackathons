# Challenge 1 — The 12-Hour Solo Build

**Time estimate:** ~12 hours, ideally split across a single weekend day (8 hours) and one evening (4 hours), or two Saturdays.

> This is the canonical Week 1 challenge in C4: a deliberately small project, alone, on a 12-hour clock, with a MoSCoW chart drawn at hour zero and a recorded demo at the end. The point is to *feel the rhythm* of a hackathon before you ever attend one with strangers.

---

## Problem statement

Pick a small, doable project. Build it solo. Apply the 12-hour rule and the demo-or-die doctrine. Ship a working deploy URL, a recorded 90-second demo, and a written micro post-mortem.

**You are not trying to win anything.** You are trying to internalize the clock.

### Example projects (pick one or invent your own)

- A todo app with one creative twist (drag-to-reorder, weekly review prompt, single-button "today" mode).
- A weather widget for one city with a 7-day forecast and a polished landing page.
- A meme generator that pairs an uploaded image with a caption.
- A "what should I read tonight" recommender backed by a small static JSON file.
- A book/movie tracker that lets you log one item and shows a list.

Whatever you pick must be **small enough that the MUSTs cap at three**. If you cannot describe it with three musts, pick a smaller project.

---

## Acceptance criteria

- [ ] A public GitHub repo named `c4-week-01-solo-build-<yourhandle>`.
- [ ] A MoSCoW chart in the repo's `README.md`, drawn before any code was written. (Commit the chart in your *first* commit.)
- [ ] A working deploy URL — Vercel, Railway, Netlify, Fly.io free tier — that loads in under 3 seconds and works on a mobile browser.
- [ ] A 90-second screen recording of the demo (OBS, Loom, QuickTime — any free tool) saved to the repo or linked from the README.
- [ ] A micro post-mortem at `POST-MORTEM.md` with the three sections below.
- [ ] At least **eight commits** across the 12 hours, not one giant "final commit." The commits should tell the story of the build.
- [ ] The first commit timestamp and the last commit timestamp are within 14 hours of each other (12 hours of work + reasonable breaks).

---

## How to run the 12 hours

```
┌────────────────────────────────────────────────────────────┐
│  THE 12-HOUR SOLO RUN                                      │
│                                                            │
│  Hour 0    │ Draw the MoSCoW chart. Commit it.             │
│            │ Pick the stack. Commit empty deploy.          │
│  Hour 1–4  │ Build MUST #1 and MUST #2.                    │
│  Hour 4    │ Self-stand-up. Status check.                  │
│  Hour 4–7  │ Build MUST #3. Start a SHOULD if there.       │
│  Hour 7    │ Self-stand-up. Apply the 12-hour-rule         │
│            │ (scaled): is remaining work ≤ remaining       │
│            │ time × 0.7? If not, cut.                      │
│  Hour 7–10 │ Polish. Color, typography, empty states.      │
│  Hour 10   │ FREEZE. No new features.                      │
│  Hour 10–11│ Demo rehearsal. Three takes.                  │
│  Hour 11–12│ Demo recording. Two takes minimum.            │
│            │ Write the README and the post-mortem.         │
│            │ Push.                                         │
└────────────────────────────────────────────────────────────┘
```

The 7-hour stand-up is the analog of the 12-hour stand-up on a 36-hour event. You apply the same rule (≤ 70% of remaining time), you cut the same way.

---

## The post-mortem

Save as `POST-MORTEM.md` in the repo:

```markdown
# Post-mortem — 12-hour solo build

## What I shipped
One paragraph describing the final product.

## What I cut, and when
List the items you moved from MUST/SHOULD to WON'T during the run.
For each cut: at which hour? Why?

## Three things to do differently next time
1. ...
2. ...
3. ...
```

The post-mortem must be blameless even when you are the only person on the team — "the deploy step was not in my hour-zero checklist" is fine; "I am bad at deploying" is not.

---

## Constraints (these are the point)

- **Solo only.** Resist asking a friend for help. The point is to feel the clock alone.
- **You may use any stack you already know.** This is not the stack-setup week (that is Week 2). Use whatever lets you get to a deploy URL fastest.
- **You may use AI assistants** — Claude Code, Copilot, ChatGPT — exactly as you would at a real hackathon. Track what you used in the post-mortem.
- **You may not** restart the project once the clock starts. The MoSCoW chart you wrote at hour zero is the only chart for the run. Cuts only move down, never sideways.
- **The clock counts wall-time, not focused-time.** Breaks are fine, but they consume the 12 hours.

---

## Why these particular constraints

| Constraint | Why |
|------------|-----|
| Solo | You need to feel scope discipline without the buffer of a team |
| MoSCoW at hour 0 | If you can write three musts, you can run a hackathon. If you cannot, your project is too big |
| 8+ commits | A commit graph that tells a story is itself a portfolio piece |
| Deploy URL | The single most cut feature on real teams. Practice it now |
| 90-second demo | Half the real demo time, forcing brutal editing |
| Wall-time clock | Real hackathons do not pause when you take a break |

---

## Rubric (for self-grading)

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Deploy URL reachable | 25% | Loads on someone else's phone, in under 3 seconds |
| Demo recording lands the structure | 20% | Hook, problem, walkthrough, ask — visible in 90 seconds |
| MoSCoW chart was real, not retrofitted | 20% | First commit contains it; later commits show cuts |
| Post-mortem identifies three real lessons | 15% | Specific, blameless, actionable |
| Commit history tells a story | 10% | Not just "wip" and "final" |
| Polish proportional to the build | 10% | One thoughtful design choice visible |

---

## Stretch (only if you finish under 10 hours)

- Add a working empty state for every screen. No "no data yet" defaults.
- Write a one-paragraph "what I would build in the next 12 hours" at the end of the post-mortem.
- Compare your demo recording to one of the five Devpost projects you rated in Exercise 2. What does theirs do that yours did not?

---

## Submission

When done:

1. Push the repo to GitHub. Make it public.
2. Make sure the deploy URL is in the README and is live at the time you submit.
3. Drop the repo link into your Code Crunch club channel (or, if you are working through C4 solo, in the public tracker).

You will reference this repo at Week 3 (the team-mode solo prototype sprint) and again at Week 10 (the real event). Treat the README and the post-mortem as portfolio artifacts; they are.

# Exercise 2 — Rate Five Real Hackathon Projects

**Goal:** Find five past hackathon winners on Devpost, watch their demo videos, and score each one against the four-axis rubric from Lecture 1. By the end you will be able to rate any hackathon project in under five minutes.

**Estimated time:** 60 minutes (10–12 min per project).

---

## Why this exercise exists

You cannot internalize the rubric by reading about it. You internalize it by *applying* it. Five projects is the smallest number that breaks the "every project is great" reaction newcomers have when they first see Devpost winners.

After this exercise you will see that even winning projects vary widely on each axis — and the winning project is rarely the most novel or the most technically deep.

---

## What to produce

Create a file `exercises/exercise-02-rate-five-real-hackathon-projects.md` in your Week 1 repo with the structure below.

```markdown
# Five hackathon projects rated against the rubric

## Project 1 — <name>
- **Event:** (which hackathon, which year)
- **Devpost URL:** (link)
- **Demo video:** (link, if separate)
- **One-sentence summary of what they built:**

### Scores (1–5, 5 = strong)
| Axis | Score | One-sentence reason |
|------|------:|---------------------|
| Problem clarity   | _ | |
| Technical depth   | _ | |
| Demo-ability      | _ | |
| Polish            | _ | |
| Total (out of 20) | _ | |

### My read
Two to three sentences. What did this team get right? What did they get wrong? Would I have voted for it?

---
(repeat for projects 2 through 5)
```

After all five, add a final summary section:

```markdown
## What I noticed across the five

Three to five bullet points. Patterns that surfaced. For example:
- Every winning team had a working demo URL at the time of judging.
- The most novel project I picked was NOT the highest-scoring on demo-ability.
- ...
```

---

## How to pick the five projects

Use **at least three different events** to avoid sampling from a single judge culture.

Easiest starting points (all free, public):

- **Devpost winners gallery** — browse by prize amount: <https://devpost.com/hackathons?challenge_type=in-person%2Conline&order_by=prize-amount>
- **MLH-affiliated events** — TreeHacks (Stanford), HackMIT, PennApps, HackHarvard, all linked in [resources.md](../01-resources.md).
- **Past Code Crunch hackathons** — the [SPRING-2025/](../../../SPRING-2025/) folder in this repo, and any later archived events.

Rules:

1. **At least one project must have a working demo URL you can click.** This is non-negotiable for scoring "demo-ability" honestly.
2. **At least one project must be from a niche/sponsor track**, not the grand-prize winner.
3. **At least one must be from a hackathon you have actually heard of** or could plausibly attend.
4. Avoid projects with broken Devpost pages or dead video links — they exist, skip them.

---

## How to score each axis

Use these rough anchors:

### Problem clarity (1–5)
- **1** — I do not understand what problem this solves.
- **3** — The problem is stated but generic ("help students study better").
- **5** — A specific, named user with a specific pain. "Pre-med students at large universities cannot find a quiet study room within a 5-minute walk after 8 PM."

### Technical depth (1–5)
- **1** — A static landing page or three-screen wireframe with no working backend.
- **3** — A CRUD app that works for one user. Standard stack, standard patterns.
- **5** — A genuinely hard piece of engineering: a non-trivial algorithm, a sponsor API integrated well, a real-time component, or a creative use of constrained hardware.

### Demo-ability (1–5)
- **1** — The demo video is just slides or talking heads. No working product visible.
- **3** — The demo shows the product working but with awkward gaps or visible bugs.
- **5** — The demo is a tight three-minute walkthrough where every claim is shown on screen.

### Polish (1–5)
- **1** — The product looks like a half-finished assignment. Default theme, ugly fonts, broken layout.
- **3** — The product looks like a hackathon project — clean enough, not embarrassing.
- **5** — The product looks shippable. A real landing page, real typography, real attention to empty states.

Add the four numbers. The total is out of 20.

---

## Acceptance criteria

- [ ] File exists at `exercises/exercise-02-rate-five-real-hackathon-projects.md`.
- [ ] Exactly five projects rated.
- [ ] Projects come from **at least three different events**.
- [ ] **At least one** project has a clickable, working demo URL.
- [ ] **At least one** project is from a niche/sponsor track, not a grand-prize winner.
- [ ] Each project has all four scores plus a total.
- [ ] Each project has a 2–3 sentence "my read."
- [ ] The closing "what I noticed across the five" has at least three bullet points.
- [ ] Committed.

---

## Hints

- **Watch the demo video first, then read the write-up.** Judges saw the demo, not the write-up. You should too.
- **Time-box each project to 12 minutes.** Five projects × 12 minutes = 60 minutes. If you find yourself going down a rabbit hole on one project, score it imperfectly and move on.
- **Be skeptical of high-vote projects.** Devpost's "popular vote" is not the same as judge scores. Some of the most-loved Devpost projects are heavy on polish and light on depth, and that is fine — your job is to *see* that pattern, not to judge it.
- **Be generous with "polish" only when you would actually use the product.** "It has a logo" is not 5/5 polish.

---

## What's next

The patterns you spot in this exercise feed directly into your Week 1 mini-project (the Hackathon Operating Document). Keep this file open when you draft the operating doc.

Move on to [Exercise 3 — Team contract draft](./exercise-03-team-contract-draft.md).

# Lecture 1 — What Hackathons Actually Reward

> **Duration:** ~1 hour of reading.
> **Outcome:** You can describe the real four-axis judging rubric, place yourself on the four-role map, distinguish hackathon formats, and reason about the sponsor-prize layer as game theory.

If you only remember one thing from this lecture, remember this:

> **The win is shipping, not innovating.** Most hackathon judging weights "did it work in 36 hours, and did the demo land" higher than "is the idea conceptually novel." The teams that internalize this first are the teams that win first.

---

## 1. The imagined rubric vs the real one

When you have never been to a hackathon, you imagine the judging looks like this:

```
┌────────────────────────────────────────────────────────────┐
│  IMAGINED RUBRIC                                           │
│                                                            │
│    Most innovative idea          ← lots of weight          │
│    Most technically impressive   ← lots of weight          │
│    Most ambitious vision         ← lots of weight          │
│    Polish                        ← afterthought            │
└────────────────────────────────────────────────────────────┘
```

The real rubric — the one judges actually use at MLH events, sponsor events, and most college hackathons — looks much more like this:

```
┌────────────────────────────────────────────────────────────┐
│  ACTUAL RUBRIC (4 axes, roughly equal weight)              │
│                                                            │
│    Problem clarity     | "Do I understand who hurts?"      │
│    Technical depth     | "Did they actually build it?"     │
│    Demo-ability        | "Did it work in front of me?"     │
│    Polish              | "Is it pleasant to look at?"      │
│                                                            │
│  Implicit fifth axis (you cannot opt out of it):           │
│    Team chemistry      | "Did this team enjoy each other?" │
└────────────────────────────────────────────────────────────┘
```

Notice "innovative idea" is not on the list. **Most winning projects are not novel.** They are clear, working, demoable, polished versions of a problem the judge can see themselves having. Devpost's own judging-criteria explainer says this plainly: judges are told to score on impact, feasibility, design, and execution — not on whether the idea has been done before.

The judge spends about three to seven minutes at your table or on your demo call. They are not your investor. They are not running a patent search. They are tired, possibly hungry, and they have eight more teams to see. What they remember is: did this team show me something working, did I understand the problem, did the demo flow.

> **C4 voice:** boring idea, demoed flawlessly, beats novel idea, half-broken. Every time. Internalize this in Week 1 and the next nine weeks will make sense.

---

## 2. Why "innovative idea" usually loses

A few mechanical reasons "novel idea, half-broken" gets less reward than its champions hope:

1. **Novelty is invisible to a tired judge.** Without context, "the first X to do Y" reads as just "another X." The judge does not have the comparison shelf in their head.
2. **Half-broken is half-broken.** If your demo crashes, hangs, or skips the climactic feature, the judge cannot mentally backfill. They saw what they saw.
3. **Polish is a credibility signal.** A clean landing page, a working sign-up flow, a Vercel URL that loads in under two seconds — these tell the judge "this team finishes things." That signal transfers to "the rest of the project is probably also finished."
4. **The team that built the working boring thing learned more.** Hackathons are a learning surface; the team that completed a small loop end-to-end made more compounding decisions than the team that wireframed a moonshot.

This is not a critique of ambition. Ambition is fine. But ambition without scope discipline does not win hackathons; it ships a half-built screenshot. Lecture 2 is entirely about the discipline that lets ambition survive contact with a 36-hour clock.

---

## 3. The four canonical roles

Most working hackathon teams of three to five people stabilize into four roles. You will rarely have one person per role; usually one person covers two, and someone reluctantly takes a third. But the *roles* exist on every team that ships.

### 3.1 PM / Scope-keeper

The person whose primary job is to **say no**. They own the MoSCoW chart, run the 12-hour stand-up, and ask "what do we cut?" hourly. They write almost no code. On a four-person team, this is often the most senior engineer (because saying no requires confidence) or the least technically-confident person (because they are not pulled into a build distraction).

The PM is the *only* role that is non-optional. A team without a scope-keeper builds a feature wishlist and ships zero of it.

### 3.2 Full-stack builder

The person who can stand up the entire app skeleton in the first three hours. Frontend route, backend endpoint, database table, a deploy that comes back green. They are not necessarily the *best* at any one layer — they are the fastest end-to-end. On many small teams there are two of these and they split frontend-heavy / backend-heavy, but neither refuses to cross the line.

### 3.3 Designer

The person who makes the demo look like the team finishes things. Logo, hero image, color palette, typography, the empty-state copy. On a team with no formal designer, this is whoever has the best taste — and they should be empowered, not asked to "wait until the build is done." Polish in the last two hours is too late; the design pass should happen *alongside* the build.

A good designer at a hackathon does about 30 percent design and 70 percent UX-tightening of the build the engineers wrote. They are not making Figma comps for things that will never ship.

### 3.4 Pitch lead

The person who will hold the laptop, click through the demo, and deliver the three-minute pitch. They are not necessarily the team's strongest engineer. They are the team's strongest *narrator*. They start writing the pitch around hour 18, not hour 35.

A surprising truth: on a team where one person can clearly out-present the others, **everyone else should defer**. The pitch is a single, indivisible artifact. It is better to have one practiced pitch lead than four engineers who each want to say "the part I built."

### 3.5 The role map

```
┌────────────────────────────────────────────────────────────┐
│  TEAM OF 4                                                 │
│                                                            │
│  ┌─────────────┐  ┌─────────────────────┐                  │
│  │ PM /        │  │ Full-stack builder 1│                  │
│  │ Scope-keeper│  │  (front-leaning)    │                  │
│  └─────────────┘  └─────────────────────┘                  │
│  ┌─────────────┐  ┌─────────────────────┐                  │
│  │ Designer    │  │ Full-stack builder 2│                  │
│  │ + pitch lead│  │  (back-leaning)     │                  │
│  └─────────────┘  └─────────────────────┘                  │
└────────────────────────────────────────────────────────────┘
```

On a team of three, designer and pitch-lead collapse into one person and one builder covers both layers. On a team of five, you usually add a second designer or a research-lead who reads sponsor docs.

> **C4 voice:** there is no rockstar, ninja, or 10x role on a hackathon team. There is the person who picks up the API doc when no one else wants to. They are worth more than the rockstar.

---

## 4. Hackathon formats — pick the format before you pick the project

Not all hackathons are the same shape. The format dictates the strategy.

### 4.1 By length

| Length | Vibe | Optimal strategy |
|--------|------|------------------|
| **24h** | Sprint. Single feature, single demo. | One must-have. Zero shoulds. Pitch is half your remaining time. |
| **36h** | The classic. MLH default. | Three musts, one or two shoulds, MoSCoW chart from hour one. |
| **48h** | Slightly more design budget. | Same as 36h, but you can afford one polished onboarding flow. |
| **Week-long** | Async, virtual, lots of submissions. | Different game entirely. Polish, repo quality, and write-up matter more than demo. |

### 4.2 By location

| Format | What changes |
|--------|--------------|
| **In-person** | Team chemistry visible, sleep deprivation real, sponsor reps wander the room, the demo is at a table |
| **Virtual** | Polish of submission matters more, demo is a recording (not live), team-finding is harder, judges may not interact at all |
| **Hybrid** | Worst of both unless tightly run; assume the in-person rules and add a backup recording |

### 4.3 By organizer type

| Organizer | What they reward |
|-----------|------------------|
| **College / MLH-affiliated** | Learning, polish, "first hackathon" stories. Generous to beginners. |
| **Sponsor / corporate** | Use of the sponsor's API or platform. Often narrower theme, often better prize money. |
| **Themed** (climate, civic tech, education) | Theme fit > technical depth. Judges include domain experts, not just engineers. |
| **Internal company hackathons** | Politics. Out of scope for this course. |

> **C4 voice:** read the about-page *and* the prizes page before deciding to attend. The about-page tells you the vibe; the prizes page tells you the strategy.

---

## 5. The sponsor-prize layer as game theory

Most hackathons publish two layers of prizes:

1. **The grand prize(s)** — large purse, all teams compete, judging is broad.
2. **The sponsor prizes** — smaller purses, narrower criteria, often "best use of [SponsorTool]."

Naïve teams ignore sponsor prizes and only chase the grand prize. This is bad game theory.

### 5.1 Why sponsor prizes are often easier to win

- The pool is smaller. If 200 teams compete for the grand prize and only 30 of them try a sponsor's API, the per-team probability of winning the sponsor prize is roughly **6 to 7 times higher**.
- The judges for a sponsor prize are sometimes a single sponsor engineer who is mostly checking "did they use our thing in a non-trivial way."
- Sponsor prizes often pay in usable goods — credits, hardware, internships — that have higher *real* value than the cash equivalent suggests.

### 5.2 Why you do not just chase sponsor prizes

- If a sponsor's tool is wrong for your project, forcing it shows.
- Stacking 5 sponsor APIs into one demo dilutes everything.
- A team that wins three small prizes but no grand prize is not necessarily *better* than a team that wins the grand prize, but it usually *learned* more about the sponsor-prize game.

### 5.3 A heuristic

```
┌────────────────────────────────────────────────────────────┐
│  TEAM SPONSOR-PRIZE HEURISTIC                              │
│                                                            │
│  Pick ONE sponsor prize you can win without distorting     │
│  your project. Pick ZERO if forcing one would.             │
│                                                            │
│  Never pick more than two unless your project is genuinely │
│  about chaining tools (e.g. an "agent" project).           │
└────────────────────────────────────────────────────────────┘
```

You will do this analysis formally in Week 9 (Event Recon). For now, the only goal is to know that the layer exists.

---

## 6. What this means for Week 1

You are not building anything large this week. The week's work is **mental**:

- Read Lecture 2 — the 12-hour rule and demo-or-die doctrine.
- Do Exercise 1 — write your one-page personal brief.
- Do Exercise 2 — rate five real Devpost winners against the rubric.
- Do Exercise 3 — draft a team contract for the event you will attend.
- Optional: Challenge 1 — a 12-hour solo build, to feel the rhythm.
- Then ship the mini-project: your personal Hackathon Operating Document.

By the end of the week you will not be a better engineer than you were on Monday. You will be a better *teammate*, which compounds.

---

## 7. Common newcomer mistakes (forewarned)

These come up at every event. Read them now; recognize them at the event.

1. **"Let's pick an ambitious idea and trim later."** You will not trim later. You will run out of time. Pick a small idea and *grow* later if there is time.
2. **"We can do polish in the last two hours."** No, you cannot. The build will eat those two hours. Polish in parallel.
3. **"The judges will love this idea."** The judges will love it if it demos. Not before.
4. **"We do not need a pitch lead — we will all present."** You will all present poorly. Pick one.
5. **"Sponsor prizes are corporate fluff."** Sponsor prizes are 70 percent of the prize money at most college events. Read them.
6. **"We will sleep at hour 24."** Some of you will not. Plan for that; do not pretend it will not happen.

---

## 8. Recap

- Hackathons reward problem clarity, technical depth, demo-ability, polish — roughly equally — and "novelty" is implicit at best.
- Boring-but-working beats novel-but-broken every time.
- Four canonical roles: PM / scope-keeper, full-stack builder, designer, pitch lead. The PM is the only non-optional one.
- Format dictates strategy: 24h vs 36h vs week-long, in-person vs virtual, college vs sponsor vs themed.
- The sponsor-prize layer is a separate game; pick one prize to fit, do not force tools, do not ignore the layer.
- This week is mental. The deliverable is your one-page personal brief.

Continue to [Lecture 2 — The 12-hour rule and demo-or-die doctrine](./02-the-12-hour-rule-and-demo-or-die.md).

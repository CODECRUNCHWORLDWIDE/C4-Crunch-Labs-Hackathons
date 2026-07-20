# Exercise 1 — Personal Brief

**Goal:** Write a one-page brief of who *you* are at a hackathon. Strengths, default role, stack preference, sleep pattern, dealbreakers. This brief will travel with you to every event and gets handed (literally or in spirit) to the team you join.

**Estimated time:** 45 minutes.

---

## Why this exercise exists

When you walk into a hackathon team of strangers, the first 90 minutes are spent figuring out who does what. Most teams burn this time poorly because nobody can describe themselves clearly under pressure. A pre-written brief solves this.

You will also use this brief in the Week 1 mini-project (the Hackathon Operating Document). Treat it as the first draft.

---

## What to produce

Create a file `exercises/exercise-01-personal-brief.md` in your Week 1 repo with the headings below. Fill in each section with **one to three honest sentences**. No essays. The whole document should fit on a single printed page (~400 words).

```markdown
# Hackathon brief — <your name>

## What I am genuinely good at
(One to three things. Be specific. "I write CSS quickly" beats "I am a frontend developer.")

## What I am bad at, or will avoid if I can
(Honesty. "I have never deployed anything to production." "I freeze when pitching live.")

## My default role on a four-person team
(Pick ONE: PM/scope-keeper, full-stack builder, designer, pitch lead. Two-sentence reason.)

## Roles I can cover in a pinch
(Up to two more. Be honest about which you actually can.)

## Stack preferences
- **Frontend:** (React / Next / Svelte / plain HTML / "I would rather not")
- **Backend:** (FastAPI / Express / Flask / Django / "I would rather not")
- **DB:** (SQLite / Postgres / Supabase / Firebase / "I would rather not")
- **Deploy:** (Vercel / Railway / Fly / Netlify / "I would rather not")

## How I work under sleep deprivation
(One sentence. Are you the person who pushes through hour 30, or the person who needs a real two-hour nap?)

## Dealbreakers
(One to three. "I will not commit code I have not tested." "I will not skip the demo recording." "I will not work with someone who is rude to teammates.")

## What I want to learn at this event
(One sentence. Not "win the grand prize." A learning goal.)
```

---

## Worked example (use for shape, not for content)

```markdown
# Hackathon brief — Sam

## What I am genuinely good at
- Wiring up CRUD APIs quickly in FastAPI.
- Writing a clean README a stranger can run from.
- Saying "let's cut that" without taking it personally.

## What I am bad at, or will avoid if I can
- Pixel-pushing in CSS. Will hand the design pass to anyone willing.
- Speaking live to a room. I can pre-record, not present.

## My default role on a four-person team
PM / scope-keeper. I am happy to write less code in exchange for keeping the MoSCoW chart honest and the deploy URL live.

## Roles I can cover in a pinch
- Full-stack builder (backend-heavy).
- Not a designer. Not a pitch lead unless absolutely no one else can.

## Stack preferences
- **Frontend:** React with Vite. Will write Next.js if the team prefers.
- **Backend:** FastAPI. Strongly.
- **DB:** SQLite for the first 12 hours, Postgres on Supabase if we need to scale demo data.
- **Deploy:** Vercel for the frontend, Railway for the backend.

## How I work under sleep deprivation
I am useless after hour 28 without a real two-hour nap. I will tell the team in advance.

## Dealbreakers
- We will not skip the deploy step on hour one.
- We will not blame teammates in the retro.
- We will not commit secrets to the repo.

## What I want to learn at this event
How to negotiate scope when the most senior engineer disagrees with the PM.
```

Notice: every section is *specific*. There is no "team player" or "fast learner." Those phrases mean nothing on a hackathon team.

---

## Acceptance criteria

- [ ] File exists at `exercises/exercise-01-personal-brief.md` in your Week 1 repo.
- [ ] All eight sections are present and filled in.
- [ ] No section is longer than three sentences.
- [ ] The role you pick as your default is one of: PM/scope-keeper, full-stack builder, designer, pitch lead.
- [ ] You have included at least one honest "what I am bad at."
- [ ] You have included at least one dealbreaker.
- [ ] The whole file fits on one printed page (~400 words).
- [ ] Committed.

---

## Hints

- **Do not pick "full-stack builder" because it sounds prestigious.** Pick what is actually true. Most teams need a scope-keeper more than a fifth builder.
- **Re-read it on Sunday before the quiz.** If a sentence feels untrue, change it. The brief is for you, not for a hiring committee.
- **Share it with one trusted person.** A teammate, a roommate, a club organizer. Ask: "Does this sound like me?" Adjust.

---

## What's next

You will reference this brief in:
- Exercise 3 (team contract) — match your dealbreakers to the team's norms.
- The mini-project (Hackathon Operating Document) — this brief is its anchor section.
- Every team-forming conversation at every event you ever attend.

Move on to [Exercise 2 — Rate five real hackathon projects](./exercise-02-rate-five-real-hackathon-projects.md).

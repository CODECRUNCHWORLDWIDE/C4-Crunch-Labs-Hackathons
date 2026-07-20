# Exercise 1 — Write the Recruiter-Grade README

## Goal

Convert the team's hackathon submission from Weeks 7–9 into a recruiter-grade README committed at the team repo root as `README-FOR-RECRUITERS.md`. Use the seven-section template from Lecture 1 §2. The exercise is the single most-leveraged deliverable of Week 10: it is the artifact every recruiter clicks before reading anything else.

## Time-box

60–90 minutes. If you spend more than 90, your sections are too long — return and prune.

## Pre-flight

- The team build is committed to a GitHub repo.
- The team has a screen-record demo video from Week 8 (the 3-minute version).
- The team has access to the Devpost submission (or equivalent) URL.
- The team's `DAY-2-LOG.md` from Week 8 is in the repo.
- The team's `JUDGE-ROOM-LOG.md` from Week 9 is in the repo.

## Instructions

### Step 1 — Open a new file in the team repo

At the repo root, create `README-FOR-RECRUITERS.md`. Do not edit the existing `README.md` — the build README stays technical. Add a one-line pointer at the top of `README.md`:

```markdown
> **For recruiters:** see [README-FOR-RECRUITERS.md](./README-FOR-RECRUITERS.md).
```

### Step 2 — Write Section 1 (Problem statement, one paragraph)

Open with the user pain. Name the user. Name the moment. Three to five sentences. Do not start with the tech stack. Do not start with "For HackXYZ 2026 we built..." — the recruiter does not care which hackathon.

Format:

```markdown
# <Project Name>

<3–5 sentences naming the user pain, the user, the moment, and the named outcome the project produces.>

> Built by <Team Name> at <Hackathon Name>, <Date>.
```

### Step 3 — Write Section 2 (Demo link, video first, repo second)

```markdown
## Demo

[![<Project Name> — 90-second demo](./docs/screenshots/title-card.png)](<YouTube unlisted URL>)

> **Watch the 90-second demo above.** Repo: [github.com/<org>/<repo>](https://github.com/<org>/<repo>) · Devpost: [<event>.devpost.com/projects/<project>](<URL>)
```

The 90-second demo URL comes from Exercise 2 (do that exercise first or in parallel; this section can link a placeholder and be updated when the video uploads). The `./docs/screenshots/title-card.png` is the captioned title-card screenshot from the 90-second video.

### Step 4 — Write Section 3 (Tech stack, a list, no version numbers unless load-bearing)

```markdown
## Stack

- **Frontend:** <Next.js / React / Vue / SvelteKit / vanilla HTML — name the framework, not the language>
- **Backend:** <FastAPI / Express / Django / Rails / Go — name the framework>
- **Database:** <Postgres / MySQL / MongoDB / SQLite — name the engine>
- **Deploy:** <Vercel / Railway / Render / Fly.io — name the deploy target>
- **Third-party APIs:** <Twilio (SMS) · Stripe (payments) · Auth0 (auth) · OpenAI (LLM) — name and parenthetical purpose>
- **Other notable choices:** <a Redis cache / a Cloudflare edge function / a Postgres trigger / a custom auth flow — one line each, only if load-bearing>
```

### Step 5 — Write Section 4 (How to run locally, three to six commands)

```markdown
## Run locally

```bash
git clone https://github.com/<org>/<repo>.git
cd <repo>
cp .env.example .env  # then fill in API keys
npm install           # or: pip install -r requirements.txt
npm run dev           # or: python manage.py runserver
```

Open `http://localhost:3000` (or the printed port).
```

If the project cannot start in six commands, fix the project or write a Dockerfile and link to the Docker docs in this section.

### Step 6 — Write Section 5 (Screenshots, three to five images)

```markdown
## Screenshots

### Hero
![Hero screen](./docs/screenshots/01-hero.png)
*The first screen a user sees: the application starts with the eligibility check.*

### Interaction
![Eligibility result](./docs/screenshots/02-eligibility.png)
*The named eligibility check returns a decision in under 2 seconds for 90% of inputs.*

### Evidence
![Deploy URL screenshot](./docs/screenshots/03-deploy.png)
*The deployed project at fundflow.vercel.app, serving live traffic during the hackathon weekend.*
```

Host the screenshots in the repo under `docs/screenshots/`. Use relative paths. Caption each one with a single sentence.

### Step 7 — Write Section 6 (Team and credits, named role per member)

```markdown
## Team

| Name | Role | GitHub | LinkedIn |
|------|------|--------|----------|
| <Name 1> | Backend + deployment | [@handle](https://github.com/handle) | [linkedin.com/in/handle](https://www.linkedin.com/in/handle) |
| <Name 2> | Frontend + UX | [@handle](https://github.com/handle) | [linkedin.com/in/handle](https://www.linkedin.com/in/handle) |
| <Name 3> | API integrations + judging-day pitch | [@handle](https://github.com/handle) | [linkedin.com/in/handle](https://www.linkedin.com/in/handle) |
| <Name 4> | Design + demo video | [@handle](https://github.com/handle) | [linkedin.com/in/handle](https://www.linkedin.com/in/handle) |
```

The role *matters*; recruiters use the row-by-row breakdown to map who built what. Do not list everyone as "full-stack."

### Step 8 — Write Section 7 (License, one line)

```markdown
## License

MIT — see [LICENSE](./LICENSE).
```

(Or `Apache-2.0`, or `All rights reserved` if the team is not ready to open-source. Pick one explicitly.)

### Step 9 — Length audit

Run a word count on the file. Target: 200–400 lines of markdown (approximately 800–1,600 words). If you are below 200, the sections are too thin; if you are above 400, sections have wandered into build-README territory.

## Acceptance criteria

- [ ] `README-FOR-RECRUITERS.md` exists at the repo root.
- [ ] All seven sections present and named: Problem, Demo, Stack, Run locally, Screenshots, Team, License.
- [ ] Demo section links the 90-second video URL (from Exercise 2; placeholder OK if Exercise 2 not yet complete).
- [ ] Run-locally section has between 3 and 6 commands.
- [ ] At least three screenshots are committed under `docs/screenshots/`.
- [ ] Every team member is listed in the Team table with name, role, GitHub, LinkedIn.
- [ ] License section names a specific license.
- [ ] Build `README.md` has the one-line pointer to the recruiter-grade README at the top.
- [ ] File length is between 200 and 400 lines.

## Common pitfalls

- **Starting with the tech stack.** Section 1 is the user pain, not the framework. Reorder if you find yourself opening with "We built a Next.js app that..."
- **A 50-command setup.** If `npm install` requires Java, Postgres, Redis, and a custom CLI tool, write a Dockerfile and reduce the section to `docker compose up`.
- **Generic screenshots.** "Login page" and "Settings page" are not the screenshots. The *hero shot*, the *interaction shot*, and the *evidence shot* are.
- **Anonymous team.** "Built by Team Awesome" is not credits; named humans with handles are.

## Submission

Commit `README-FOR-RECRUITERS.md`, the updated `README.md`, and the screenshots under `docs/screenshots/` in a single PR titled `recruiter-grade README — Week 10`. Note the PR link in `POST-EVENT-LOG.md` under Day 2.

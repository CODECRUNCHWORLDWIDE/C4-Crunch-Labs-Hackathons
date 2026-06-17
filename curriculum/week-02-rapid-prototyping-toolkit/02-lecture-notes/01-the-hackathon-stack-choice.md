# Lecture 1 — The Hackathon Stack Choice

> **Duration:** ~1 hour of reading.
> **Outcome:** You can defend the "boring stack" doctrine, name the default Code Crunch stack and its alternates, apply the 30-minute scaffold-to-first-route rule, and refuse the "we'll learn $newtech at the event" pitch in plain language.

If you only remember one sentence from this lecture, remember this:

> **Pick the technology your team has already shipped with. Never the one you read about last week.** Hackathon scope discipline starts the moment you choose a stack — not the moment the prompt is announced.

Lecture 1 of Week 1 told you what hackathons reward: clarity, demo-ability, polish. Lecture 1 of Week 2 tells you how to *not* burn six of your thirty-six hours on `npm install` and `pip install`. The stack choice is the first scope decision of every event.

---

## 1. The "boring stack" doctrine

Dan McKinley's essay *Choose Boring Technology* (a free read, in the resources page) made the argument for production engineering. C4 takes it further for hackathons: at an event, "boring" is not a preference, it is a survival rule.

> **C4 voice:** the boring stack is the stack your team already knows. The exciting stack is the one your teammate suggests at hour two because he watched a YouTube video on the train down.

### 1.1 Why the boring stack wins

Three mechanical reasons:

1. **You amortize the learning cost.** A stack you have shipped twice before takes minutes to scaffold. A stack you have never touched takes hours just to get the dev server to reload.
2. **You stay in the demo-or-die loop faster.** Every minute you spend on a webpack config or a Vite plugin issue is a minute the demo path is not visibly working.
3. **Your team's debug skill compounds.** When the deploy errors out at hour 30, the person who knows the stack fixes it in five minutes. The person who is "learning" fixes it never.

### 1.2 The "boring stack" is not anti-modern

To be clear, C4 does *not* mean "use jQuery and PHP from 2010." Boring is a *team-specific* word. If your whole team is fluent in Next.js + tRPC + Prisma, that is *your* boring stack. If your whole team is fluent in Django + HTMX, *that* is your boring stack. The doctrine is "known, shipped, debuggable" — not "old."

The crime is **adopting unfamiliar tech because it sounds impressive at a demo**. You will not impress the judges with your choice of framework. You will impress them with a working URL.

---

## 2. The default Code Crunch stack

When you have *no* prior shipped stack — which is true for some Week 2 readers — C4 picks one for you. Not because it is the only right answer, but because pre-deciding closes a debate you do not have time for.

```
┌────────────────────────────────────────────────────────────┐
│  C4 DEFAULT STACK                                          │
│                                                            │
│  Frontend     React (via Vite)                             │
│  Styling      Tailwind CSS + shadcn/ui                     │
│  Data layer   TanStack Query (a.k.a. react-query)          │
│                                                            │
│  Backend      FastAPI (Python 3.11+)                       │
│  ASGI server  Uvicorn                                      │
│  Auth         FastAPI auth scaffolding (JWT, simple)       │
│                                                            │
│  DB           SQLite for first 12 hours                    │
│               Supabase Postgres free if scaling demo data  │
│                                                            │
│  Deploy FE    Vercel free                                  │
│  Deploy BE    Railway free  (Fly.io free as alternate)     │
└────────────────────────────────────────────────────────────┘
```

### 2.1 Why these choices, briefly

- **React + Vite.** Vite gives you a dev server that reloads in milliseconds. React has the largest free component ecosystem. Together: zero learning friction for anyone who has touched modern frontend.
- **Tailwind + shadcn/ui.** Tailwind ends the "what do I name this CSS class" debate. shadcn/ui gives you copy-paste accessible components with no `npm install` weight. Demo polish in twenty minutes, not eight hours.
- **TanStack Query.** Replaces ten patterns of `useEffect` with one. Loading, error, refetch, caching — all built in. Saves you from re-inventing it at hour 14.
- **FastAPI.** Auto-generated OpenAPI docs at `/docs`. Two-line route definitions. Pydantic models do request validation for free. The fastest "from zero to a typed HTTP route" framework in Python.
- **SQLite first, Supabase second.** SQLite is a file. You commit a migration, the database exists. No service to configure. When (rarely) you need real multi-user persistence, Supabase free has Postgres + auth + storage in a single dashboard.
- **Vercel + Railway.** Both deploy on `git push`. Both have working free tiers. Vercel for the React app (static + edge), Railway for the FastAPI service (a real long-running server). Fly.io is the slightly more durable Railway alternative if you have a project you want to keep alive for months.

### 2.2 What the default stack costs you

- It is **not** the best stack for ML/AI-heavy demos. For those you may want a Python-only Streamlit or Gradio app.
- It is **not** ideal for events that explicitly reward "use SponsorCorp's no-code platform."
- It is **not** the world's fastest path to a static marketing site. For that, Astro is better.

If your event prompt or your team falls into one of those buckets, switch. The *default* is for the median 36-hour college hackathon prompt where a "build a tool that does X" theme dominates.

---

## 3. Stack alternates worth knowing

You should be able to name three alternates and the one-sentence "when to use" for each. Memorize these.

### 3.1 Next.js full-stack

```
Use when the team is all-TypeScript and wants frontend + API
routes in one repo, one deploy target (Vercel handles both).
```

- **Pro:** single deploy, single language, fewer env var headaches.
- **Con:** Vercel function timeouts for long-running backend work. Not great for a backend that needs a real persistent server.
- **Looks like:** `pages/api/foo.ts` next to `pages/foo.tsx`. One repo, one `vercel.json`.

### 3.2 The T3 stack

```
Use when the whole team is genuinely TS-fluent and you want
type-safe end-to-end RPC out of the box.
```

- The T3 stack: **Next.js + tRPC + Prisma + Tailwind + NextAuth.** All TypeScript, fully typed from DB to component.
- **Pro:** the typing safety net catches a lot of "it crashed in prod" bugs at compile time. The auth is bundled.
- **Con:** dense for a beginner. The first time a non-T3-native joins your team, they will be lost for two hours. Do not pick T3 if anyone on the team has not used it before.

### 3.3 Astro + SQLite

```
Use when the prompt is content-heavy: a landing-page-as-a-product,
a directory, a "build a microsite for X" theme.
```

- Astro renders static at build time, optionally hydrates components on the client.
- **Pro:** fastest static deploys you will ever see. SEO + load time both great. SQLite or a JSON file is enough.
- **Con:** wrong tool for a real database-backed multi-user app.

### 3.4 The choice matrix

```
┌────────────────────────────────────────────────────────────┐
│  IF THE PROMPT IS...           USE...                      │
│                                                            │
│  Tool / CRUD / "build a thing"  C4 default (React+FastAPI) │
│  All-TS team, single deploy     Next.js full-stack         │
│  All-TS team, type-safety love  T3                         │
│  Content / marketing / static   Astro + SQLite             │
│  ML/AI demo, no real frontend   Streamlit or Gradio        │
└────────────────────────────────────────────────────────────┘
```

You will not memorize all of this in one read. The choice matrix lives on your Hackathon Operating Document.

---

## 4. The "we'll learn $newtech during the event" anti-pattern

Every hackathon team has at least one person who, around hour 2 to 3, suggests:

> "Hey, what if we used [unfamiliar framework] for this? I've been meaning to learn it, and it'd be perfect for [feature]."

This is one of the most common ways teams lose. Here is why, formally.

### 4.1 The cost ledger

```
┌────────────────────────────────────────────────────────────┐
│  COST OF LEARNING NEW TECH AT THE EVENT                    │
│                                                            │
│  Initial install:        30–90 minutes                     │
│  First "hello world":    30 minutes                        │
│  First real feature:     2–4 hours                         │
│  First real bug:         1–3 hours (you cannot Google      │
│                          your stack-specific error well    │
│                          when you do not know the stack)   │
│  Deploy config:          2–4 hours                         │
│                          (or "never" if you skip it)       │
│  ────────────────────────────────────────────────────      │
│  TOTAL TAX                up to half your 36 hours         │
└────────────────────────────────────────────────────────────┘
```

The teammate who proposes this is not malicious. They are excited. They imagine the demo will look cooler with the new tool. They are wrong about the demo, and they are wrong about the time budget.

### 4.2 How to refuse, in C4 voice

You will need a script. The script is:

> "Cool — let's bookmark it for the post-mortem. For this event, we ship in the boring stack and we use the time we saved on rehearsal."

Notice what the script does:

- It validates the curiosity ("let's bookmark it").
- It defers, it does not reject ("for the post-mortem").
- It re-anchors on the win condition ("the time we saved on rehearsal").
- It is short. Three sentences, total.

The PM / scope-keeper from Week 1 is the person who says this. Quietly. Once. Move on.

### 4.3 The one exception

There is one exception: **a sponsor track that explicitly requires a specific tool.** If you are competing for "Best use of [Vendor X]," you need to use Vendor X's tool. That is not "learning $newtech for fun" — that is reading the rubric and serving it. Even then, you should have at least *touched* Vendor X's tool before the event. Week 9 (Event Recon) tells you how to do that pre-game.

---

## 5. The 30-minute scaffold-to-first-route rule

The single quantitative target for Week 2:

```
┌────────────────────────────────────────────────────────────┐
│  THE 30-MINUTE SCAFFOLD-TO-FIRST-ROUTE RULE                │
│                                                            │
│  From `git clone <your hackathon-template>` to a live      │
│  deploy URL returning a real HTTP response,                │
│                                                            │
│  TOTAL ELAPSED TIME ≤ 30 MINUTES.                          │
│                                                            │
│  If yours is longer, you have not pre-tuned enough.        │
│  Week 2 is the week to fix that.                           │
└────────────────────────────────────────────────────────────┘
```

This is *not* the same as the "blank page live at hour 2" rule from the team contract. That rule was about the team executing during the event. The 30-minute rule is about *your laptop, your template, your scripts*, with no team involved.

### 5.1 What the 30 minutes must cover

1. Clone the template (or run `./bootstrap.sh new-event-name`).
2. Install dependencies (Node + Python).
3. Confirm the frontend dev server runs locally (`pnpm dev`).
4. Confirm the backend dev server runs locally (`uvicorn main:app --reload`).
5. Push the new repo to GitHub.
6. Trigger the Vercel deploy (frontend).
7. Trigger the Railway deploy (backend).
8. Visit both URLs in a browser, confirm a non-error response.

Eight steps in 30 minutes is roughly 3.75 minutes per step. That is *generous* if your template is well-pre-tuned. Most of the 30 minutes will be `npm install` and `pip install` waiting; the human work is closer to ten minutes of focused activity.

### 5.2 Why 30 minutes, not 10

You could in principle hit ten minutes if every cache is warm and every config is perfect. C4 picks 30 because:

- The hackathon laptop is often not your daily laptop (you cleaned dependencies for the trip).
- The hackathon Wi-Fi is often slower than home.
- The hackathon clock starts when *everyone* is at hour zero, not when you are.

A 30-minute target survives real conditions. A 10-minute target survives only on a perfect day.

### 5.3 What "first route" means

"First route" means: a real HTTP response from a real deployed URL, not localhost. Concretely:

- The frontend Vercel URL loads a page that does *not* say "404 — file not found" or "framework error."
- The backend Railway URL, at `/health` or `/`, returns `200 OK` with a JSON or text body.

This is the minimum credible evidence that your stack is alive. It is also the moment your team can plausibly write feature code, because the deploy is no longer a future task.

---

## 6. Sequencing: what you do this week, in order

Lecture 1 told you why. The rest of the week tells you how. The sequence:

1. **Tuesday — Exercise 1.** Stand up the `hackathon-template` repo on your GitHub. Pre-tuned `.gitignore`, README skeleton, `.env.example`, deploy config, minimal CI.
2. **Wednesday — Lecture 2.** Read the template-repo pattern in depth: what every file is for, and how `bootstrap.sh` ties them together.
3. **Thursday — Exercise 2.** Write `./bootstrap.sh new-event-name`. The single command that produces a renamed, configured, ready-to-commit new repo.
4. **Friday — Exercise 3.** Wire Vercel + Railway. Confirm the first push to a new event repo produces a working deploy URL.
5. **Saturday — Challenge 1 (optional).** Profile your end-to-end spinup. Find and shave 30 minutes off the clock-time.
6. **Sunday — Quiz + mini-project polish.** Take the quiz. Then iterate the template one more time, with the notes from this week's work versioned into the template's own README.

By Sunday night, your `hackathon-template` repo is public, has a green CI badge, and the README contains a Sprint Coral "30 min spinup, last measured Sunday" timestamp.

---

## 7. Common newcomer setup mistakes (forewarned)

These come up at every event. Recognize them in your template *now*, not at hour 4 of the event.

1. **Secrets in commits.** Someone commits `OPENAI_API_KEY=sk-...` to the repo. GitHub flags it, you spend an hour rotating keys. Fix: `.env.example` only, real `.env` in `.gitignore`, a `.gitignore` that exists *before* the first commit.
2. **Missing `.env.example`.** Your `main.py` reads `os.environ["DATABASE_URL"]`, but there is no `.env.example` listing it. A new teammate joins and cannot run the app. Fix: every env var your app reads is named in `.env.example` with a placeholder.
3. **Hard-coded `http://localhost:8000`.** Your frontend works locally; on deploy, the calls go to a nonexistent host. Fix: read the backend URL from an env var (`VITE_API_URL`), set it in Vercel's dashboard.
4. **Untested deploy.** You configured deploys at hour zero but never visited the URL. The deploy errored out silently. Fix: hit both URLs *before* you write feature code.
5. **No `.nvmrc` / no `.python-version`.** Teammate has Node 18, you have Node 20, the build breaks for one of you. Fix: pin the version in your template, document it in the README.
6. **No README skeleton.** When you submit at hour T-1, you scramble to write a README. Fix: the template's README has a `<one-line description>` placeholder and a "How to run" section already written.
7. **`npm install` from scratch on the event Wi-Fi.** Five minutes of waiting on a busy network. Fix: pre-warm your package cache, or use `pnpm` (faster + content-addressable cache).
8. **Vercel build failing because `pnpm-lock.yaml` is missing.** You committed `node_modules` instead of the lockfile. Fix: `node_modules` in `.gitignore`, lockfile *not* in `.gitignore`. The template enforces this.

You will see every one of these at a real event. The template prevents all of them.

---

## 8. Recap

- The boring stack doctrine: pick technology your team has already shipped with.
- The default Code Crunch stack: React + Vite + Tailwind + shadcn/ui + FastAPI + SQLite/Supabase + Vercel + Railway.
- Alternates worth knowing: Next.js full-stack, T3, Astro + SQLite. Choose by team and prompt.
- The "we'll learn $newtech at the event" pitch is the most common stack-discipline failure. Defer, do not adopt.
- The 30-minute scaffold-to-first-route rule is Week 2's single quantitative target.
- Eight common newcomer setup mistakes — your template prevents all of them.

Continue to [Lecture 2 — The Template Repo Pattern](./02-the-template-repo-pattern.md), where the abstract becomes concrete: what files live in your `hackathon-template` repo, why each one exists, and how `bootstrap.sh` ties them into a one-command spin-up.

# Week 2 — Resources

Every resource on this page is **free** and **publicly accessible**. No paywalled books, no signups beyond the free tier of the deploy hosts. If a link breaks, please open an issue.

## Required reading (work it into your week)

- **Vite — Getting Started.** The one place to learn the Vite dev server in 15 minutes flat: <https://vitejs.dev/guide/>
- **FastAPI — First Steps.** The whole "hello world" through "your first route" path: <https://fastapi.tiangolo.com/tutorial/first-steps/>
- **Vercel — Deploying a React app.** What "deploy from a Git push" actually looks like: <https://vercel.com/docs/frameworks/vite>
- **Railway — Deploying from GitHub.** The Python-backend equivalent: <https://docs.railway.app/guides/python>

If you only have time for one, read the Vite guide. The dev-server reload story is the single biggest hour-saver during a 36-hour event.

## The default Code Crunch stack — official docs

| Layer | Tool | Docs |
|-------|------|------|
| Frontend build | Vite | <https://vitejs.dev/> |
| UI framework | React | <https://react.dev/learn> |
| UI components | shadcn/ui | <https://ui.shadcn.com/docs> |
| Styling | Tailwind CSS | <https://tailwindcss.com/docs/installation> |
| Data fetching | TanStack Query (a.k.a. react-query) | <https://tanstack.com/query/latest/docs/framework/react/overview> |
| Backend | FastAPI | <https://fastapi.tiangolo.com/> |
| Backend ASGI server | Uvicorn | <https://www.uvicorn.org/> |
| DB (small) | SQLite | <https://www.sqlite.org/docs.html> |
| DB (managed) | Supabase free | <https://supabase.com/docs> |
| Frontend deploy | Vercel | <https://vercel.com/docs> |
| Backend deploy | Railway | <https://docs.railway.app/> |
| Backend deploy alt | Fly.io | <https://fly.io/docs/> |

## Stack alternates worth knowing

- **Next.js full-stack** — when your team wants frontend and API routes in one repo, one deploy target: <https://nextjs.org/docs>
- **The T3 stack** (Next.js + tRPC + Prisma + Tailwind + NextAuth) — when the whole team is TS-fluent: <https://create.t3.gg/>
- **Astro + SQLite** — for content-heavy or marketing-heavy event prompts: <https://docs.astro.build/>
- **SvelteKit** — when the team is genuinely already in Svelte and has shipped at least one project: <https://kit.svelte.dev/docs/introduction>

C4 does not recommend switching to any of these *for* an event. C4 recommends knowing one of them well enough that, if it is your team's existing stack, you go with it.

## Free reading on the "boring stack" doctrine

- **Choose Boring Technology — Dan McKinley** (the essay that named the doctrine, ~15 min read): <https://boringtechnology.club/>
- **"Speed of Iteration Beats Quality of Iteration" — Karpathy on building under time pressure** (search for the phrase; it has been quoted in many talks): <https://karpathy.ai/>
- **The Twelve-Factor App.** Not gospel, but the env-var and config-as-data sections are worth thirty minutes when designing `.env.example`: <https://12factor.net/>

## Tools you will install this week

- **Node.js 20+** — install via [nvm](https://github.com/nvm-sh/nvm) or [fnm](https://github.com/Schniz/fnm), never the system installer.
- **Python 3.11+** — install via [pyenv](https://github.com/pyenv/pyenv) on macOS/Linux or the official installer on Windows.
- **pnpm** — fast Node package manager, recommended over npm for hackathon repos: <https://pnpm.io/installation>
- **uv** — fast Python package manager from the makers of Ruff, optional but worth trying: <https://docs.astral.sh/uv/>
- **gh CLI** — GitHub from the terminal, dramatically speeds up the "create repo and push" step: <https://cli.github.com/>
- **Vercel CLI** — `vercel` from the terminal: <https://vercel.com/docs/cli>
- **Railway CLI** — `railway` from the terminal: <https://docs.railway.app/develop/cli>

## Free tier limits worth knowing

- **Vercel free** — 100GB bandwidth/month, hobby projects only, unlimited static; serverless function execution limited but plenty for a hackathon demo.
- **Railway free** — $5/month of usage credit when you start, then a paid trial; works for the duration of a hackathon but plan to migrate or upgrade after an event.
- **Fly.io free** — generous hobby tier; arguably more durable than Railway for "I want this demo URL to stay up for six months."
- **Supabase free** — 500MB database, 2 free projects; do not store user uploads here on a hackathon, use Supabase storage which has its own free tier.

## Glossary cheat sheet

| Term | Plain English |
|------|---------------|
| **The boring stack** | Whatever your team has already shipped with. The "exciting" stack is the one they read about on Hacker News last week. |
| **Scaffold** | The pre-built skeleton of a project: routing, build, deploy, env-var pattern, README. Not features. |
| **Bootstrap script** | A shell script that creates a new repo from your template in one command. |
| **Deploy target** | The public URL the judges will click. Vercel, Railway, Fly.io free tier, etc. |
| **`.env.example`** | A committed file listing every env var your app needs, with placeholder values. The actual `.env` is gitignored. |
| **CI** | Continuous Integration. A linter and a unit-test run on every push. At a hackathon, "did it build?" is enough. |
| **Yak-shaving** | The sin of fixing dependencies-of-dependencies during an event. The thing this week prevents. |
| **shadcn/ui** | A React component library you copy into your project rather than `npm install`. Tailwind-based. |
| **react-query / TanStack Query** | The data-fetching library that handles caching and loading states. Saves you from re-inventing `useEffect` patterns. |
| **uvicorn** | The ASGI server FastAPI runs on. You will type `uvicorn main:app --reload` more than any other command this week. |

---

*If a link 404s, please open an issue so a future learner has a working version.*

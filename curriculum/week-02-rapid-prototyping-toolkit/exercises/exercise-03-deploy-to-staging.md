# Exercise 3 — Deploy to Staging

**Goal:** Wire Vercel (for the frontend) and Railway (for the backend) to your `hackathon-template`. Prove that the first push from a freshly bootstrapped event repo produces a live, public URL returning a real HTTP response, with frontend and backend talking to each other.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

The brand book is uncompromising on this point: the demo URL is always a MUST, and at the event, the deploy goes live by hour 2 — even as a blank page. That rule is only enforceable if your *template* has already shaken out the deploy. If you have never deployed your scaffold before, "hour 2 with a blank page live" becomes "hour 6 with a half-broken deploy."

This exercise removes the deploy as a future task. After today, "wire the deploy" at an event is "click two buttons on Vercel and Railway."

---

## What to produce

A new public repo, spun up from your `hackathon-template` via `bootstrap.sh`, called `c4-week-02-deploy-drill-<yourhandle>`, with **both**:

- A live Vercel URL for the frontend.
- A live Railway URL (or Fly.io URL) for the backend.

And:

- The Vercel-hosted frontend calls the Railway-hosted backend `/health` and renders the response.
- The README of the drill repo links to both URLs and shows a screenshot.

---

## Step-by-step

### 1. Spin up a new event repo with `bootstrap.sh`

```
cd ~/code
git clone <your hackathon-template> deploy-drill
cd deploy-drill
./bootstrap.sh deploy-drill
```

Note the elapsed-time output. Write it down (you will compare to the post-deploy total).

### 2. Push to GitHub

```
gh repo create c4-week-02-deploy-drill-<yourhandle> --public --source=. --push
```

Confirm the GitHub repo is reachable and public.

### 3. Connect Vercel

If you have not used Vercel before, sign up free at <https://vercel.com>. Install the CLI:

```
pnpm add -g vercel
```

From inside the drill repo:

```
cd frontend
vercel link
vercel --prod
```

When asked for the framework, pick **Vite**. When asked for the build command, accept the default (`pnpm build`). When asked for the output directory, accept `dist`.

In the Vercel dashboard, go to **Project Settings → Environment Variables** and add:

- `VITE_API_URL=<your-railway-url>` (you will fill this in after step 4)

### 4. Connect Railway

If you have not used Railway before, sign up free at <https://railway.app>. Install the CLI:

```
brew install railway     # or curl-pipe-sh per the Railway docs
```

From the drill repo root:

```
railway login
railway init
railway link
```

In the Railway dashboard, create a new service from your GitHub repo, point it at the `backend/` directory, and set the start command:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Add environment variables in the Railway dashboard:

- `DATABASE_URL=sqlite:///./dev.db` (good enough for a drill; real events use Postgres)
- `JWT_SECRET=<a long random string>` (use `openssl rand -hex 32`)

Deploy. Visit the public URL. Append `/health`. Confirm `{"status":"ok"}`.

### 5. Wire the frontend to the backend in production

Back in the Vercel dashboard, set `VITE_API_URL` to the Railway URL (no trailing slash). Re-deploy by pushing any commit (a comment in the README is fine) or use **Redeploy** from the Vercel UI.

Visit the Vercel URL. Confirm the placeholder UI shows the health response from the *Railway* backend, not localhost.

### 6. Tighten CORS

In `backend/main.py`, change `allow_origins=["*"]` to `allow_origins=["<your-vercel-url>"]`. Commit. Push. Confirm the deploy still works.

### 7. Document in the drill repo's README

Add a section to the drill repo's README:

```markdown
## Deploy URLs

- Frontend: https://<vercel-url>
- Backend health: https://<railway-url>/health

## Time-to-live (Exercise 3, deploy-drill)

- bootstrap.sh:     <N> seconds
- gh repo create:   <N> seconds
- Vercel connect:   <N> minutes
- Railway connect:  <N> minutes
- CORS tighten + redeploy: <N> minutes
- **Total elapsed:  <N> minutes**

Target: ≤ 30 minutes (the 30-minute scaffold-to-first-route rule).
```

### 8. Carry the lesson back to the template

Look at the things that made the deploy slow. For each one, decide: does this go into the template now, so the *next* deploy is faster? Common candidates:

- A `vercel.json` at the right place. (Already in `deploy/`.)
- A `railway.toml` or `Procfile` at the right place.
- Documentation in the template's README about the env vars Railway and Vercel each need.
- A pinned `engines.node` in `frontend/package.json` so Vercel picks the right Node version.

Make those changes in the *template* repo, not in the drill repo. Commit. Push. Add a version-log row to the template's README:

```
| v1.1 | <today> | Tightened deploy: pinned Node, documented env vars. | C4 Week 2 — deploy drill |
```

---

## Acceptance criteria

- [ ] A new public repo `c4-week-02-deploy-drill-<yourhandle>` exists, created via `bootstrap.sh`.
- [ ] The Vercel frontend URL is live and loads in under three seconds.
- [ ] The Railway (or Fly.io) backend URL is live and `/health` returns `200 OK`.
- [ ] The deployed frontend successfully calls the deployed backend and renders the response.
- [ ] CORS is **tightened** to your specific Vercel origin (not `*`).
- [ ] The drill repo's README contains both URLs and a measured time-to-live breakdown.
- [ ] The template repo has at least one improvement committed back, with a version-log row.
- [ ] Total elapsed time from `bootstrap.sh` to working live URL is **≤ 30 minutes** (target). If yours is longer, log it honestly — the template will eat into that number over the next week.

---

## Hints

- **Do not connect Vercel and Railway in *parallel* the first time.** You will get confused about which env var goes where. Frontend first, see it live (talking to nothing), then backend, then wire them.
- **The first Vercel deploy will fail if you forgot `pnpm-lock.yaml`.** Confirm the lockfile is committed. The Vercel UI tells you this clearly if it is the cause.
- **Railway free tier is $5 of credit, not unlimited.** A drill costs cents. Do not leave the service running indefinitely if you are tight on budget — the drill repo can be paused after this exercise.
- **`VITE_*` env vars are baked at build time.** If you change `VITE_API_URL`, you must trigger a Vercel re-deploy. The deploy is fast, but the surprise is common.
- **Use `gh secret set` for any secret you set in the GitHub repo.** If you have CI that needs to know `VITE_API_URL`, set it in GitHub Actions secrets, not in the repo file.
- **CORS errors look like network errors.** If the Vercel frontend cannot talk to the Railway backend after both deploys are green, open browser devtools → Network tab and look for the CORS error. The fix is in `main.py`.

---

## What to do if a step fails

- **Vercel build fails: "command not found: pnpm."** In Vercel's build settings, set the install command explicitly to `npm install -g pnpm && pnpm install`. Or use `corepack enable` if your Node is recent enough. Pinning Node 20+ in `engines` usually fixes this for free.
- **Railway deploy fails: "no `requirements.txt` found."** Railway's Python builder defaults to looking for `requirements.txt`. You are using `pyproject.toml`. Add a buildpack hint via `railway.toml` or generate a `requirements.txt` from `pyproject.toml` and commit it.
- **The deployed frontend renders, but the health response never arrives.** Two likely causes: (a) `VITE_API_URL` is wrong (most likely), or (b) CORS is rejecting the origin (less likely if you set `allow_origins=["*"]` first). Check devtools.
- **You exceed 30 minutes.** Note it honestly. Carry the slowest step back into the template. The 30-minute rule is a *target*, not a pass/fail this week. Week 2's Challenge 1 is dedicated to shaving the time down.

---

## What is next

You have shipped the deploy. The mandatory work of Week 2 is done. Continue to:

- **Challenge 1 (optional)** — [shave 30 minutes off your spin-up](../challenges/challenge-01-shave-30-min-off-spinup.md).
- **The mini-project** — [polish your `hackathon-template` repo into the deliverable](../mini-project/README.md) that earns the week.
- **The quiz** — once Friday's work is committed.

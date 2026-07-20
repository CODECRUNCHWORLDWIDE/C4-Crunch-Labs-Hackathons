# Exercise 1 — Stand Up the Template

**Goal:** Create your personal `hackathon-template` repo on GitHub with the file shape from Lecture 2. By the end of the exercise, the repo is public, the frontend dev server runs, the backend dev server runs, and the placeholder UI calls the backend `/health` route and displays the response.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

The template is the artifact every following exercise and challenge builds on. If the scaffold is not real and on GitHub by Tuesday night, the rest of Week 2 has no foundation. You are not optimizing yet. You are paying setup tax on a calm day, exactly so the event-day version of you does not pay it.

---

## What to produce

A public GitHub repository named `hackathon-template` (or `c4-hackathon-template-<yourhandle>` if your account already has a `hackathon-template` repo) with this top-level shape:

```
hackathon-template/
├── .github/workflows/ci.yml
├── .gitignore
├── .env.example
├── .nvmrc
├── .python-version
├── README.md
├── LICENSE
├── frontend/
│   ├── package.json
│   ├── pnpm-lock.yaml
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   ├── index.html
│   ├── src/main.tsx
│   ├── src/App.tsx
│   ├── src/lib/api.ts
│   ├── src/components/ui/button.tsx
│   ├── src/components/ui/card.tsx
│   └── .env.example
├── backend/
│   ├── pyproject.toml
│   ├── main.py
│   ├── auth.py
│   ├── db.py
│   └── .env.example
└── deploy/
    ├── vercel.json
    └── railway.toml
```

`bootstrap.sh` is *not* part of this exercise. You write that in Exercise 2.

---

## Step-by-step

You do not have to follow this exact order, but it works.

### 1. Create the repo

```
gh repo create hackathon-template --public --clone
cd hackathon-template
```

If you do not have the `gh` CLI, use the GitHub web UI and `git clone` after.

### 2. Add the root files

- `.gitignore` — copy the entries from Lecture 2 §4.1.
- `.env.example` — list every env var your code will read.
- `.nvmrc` — one line, e.g. `20`.
- `.python-version` — one line, e.g. `3.11`.
- `LICENSE` — pick MIT, paste the standard text with your name + year.
- `README.md` — start with the template README shape from Lecture 2 §3.

Commit. Push.

### 3. Scaffold the frontend

```
cd frontend
pnpm create vite@latest . --template react-ts
pnpm install
pnpm add @tanstack/react-query
pnpm add -D tailwindcss postcss autoprefixer
pnpm dlx tailwindcss init -p
pnpm dlx shadcn-ui@latest init
pnpm dlx shadcn-ui@latest add button card
```

Edit `src/main.tsx` to wrap the app in `QueryClientProvider`. Edit `src/App.tsx` so it calls the backend `/health` endpoint via a `useQuery` hook from `src/lib/api.ts` and displays the response. Commit small.

### 4. Scaffold the backend

```
cd ../backend
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
```

Create `pyproject.toml` with `fastapi`, `uvicorn[standard]`, `sqlalchemy`, `pyjwt`, `python-dotenv`. Write `main.py`, `auth.py`, `db.py` per Lecture 2 §4.6. Run:

```
uvicorn main:app --reload
```

Visit `http://localhost:8000/health`. Confirm `{"status":"ok"}`. Visit `http://localhost:8000/docs`. Confirm FastAPI's auto-generated docs page renders. Commit.

### 5. Wire the frontend to the backend (locally)

Run *both* dev servers — frontend on `localhost:5173`, backend on `localhost:8000`. Confirm the placeholder UI shows the response from the backend. This is the demoable evidence that the stack is wired.

### 6. Write the CI

`.github/workflows/ci.yml` — Lecture 2 §4.4. Three jobs at most. Push. Confirm green.

### 7. Write the deploy configs

`deploy/vercel.json` and `deploy/railway.toml`. Reference: Lecture 2 §4.7. You will not connect Vercel and Railway in this exercise — that is Exercise 3. You are only writing the config files.

### 8. Update the README

Fill in the "What is in here" and "How to use" sections. Leave a placeholder line that says "Last measured spin-up: not yet measured (will be set after Exercise 2)."

### 9. Push

```
git push
```

Confirm the CI is green. Confirm the README renders correctly on the GitHub repo page.

---

## Acceptance criteria

- [ ] Repo exists at `github.com/<your-handle>/hackathon-template` (or your chosen name) and is **public**.
- [ ] All files in the file tree above exist and are non-empty.
- [ ] `pnpm dev` in `frontend/` starts the dev server without errors.
- [ ] `uvicorn main:app --reload` in `backend/` starts the dev server without errors.
- [ ] Visiting the frontend with both servers running shows the response from the backend `/health` endpoint on screen.
- [ ] CI is green on the default branch.
- [ ] `.env` files are **not** committed. `.env.example` files **are** committed.
- [ ] LICENSE is set (MIT or your preference).
- [ ] README has the "What is in here" and "How to use" sections filled in.
- [ ] At least **five commits** for this exercise, telling the story of the scaffold. Not one giant "initial commit."

---

## Hints

- **Resist the urge to add features.** No charts, no animations, no extra routes. The point of the template is *not* a beautiful demo; it is a clean *starting point*.
- **Pin every version.** `"react": "^18.3.1"` is fine; `"react": "*"` is not. The template will rot if you do not pin.
- **The two `.env.example` files are intentional.** The root one is a *summary*; the per-service ones are the *actual* files each service reads. Yes, it is mild duplication. Yes, it is worth it — when a teammate clones the new event repo they go to `frontend/.env.example` and `backend/.env.example`, not the root.
- **Do not skip the LICENSE.** A repo with no LICENSE is legally "all rights reserved." That is fine for private use, but you cannot share it as a portfolio piece without one.
- **Commit messages matter.** "scaffold frontend with vite + tailwind" beats "stuff." Your future-self reads these.

---

## What to do if a step fails

- **Vite refuses to start with a TypeScript error.** Run `pnpm install` again, then check the Node version matches `.nvmrc`. Most Vite-start failures are wrong Node major version.
- **FastAPI cannot find `uvicorn`.** Activate the virtualenv first. `which uvicorn` should point at `backend/.venv/bin/uvicorn`.
- **shadcn/ui init fails.** Make sure Tailwind is configured first. Run `pnpm dlx tailwindcss init -p` before `shadcn-ui init`.
- **CORS error from the frontend.** `main.py` includes `CORSMiddleware` with `allow_origins=["*"]`. Confirm it is present and the backend has reloaded.
- **CI failing.** Read the error carefully. Most first-time CI failures are missing `pnpm-lock.yaml` (committed) or wrong cache key.

---

## What is next

Move on to [Exercise 2 — One-command spin-up](./exercise-02-one-command-spinup.md), where you write `./bootstrap.sh new-event-name` and prove it produces a renamed, configured, deploy-ready repo in a single command.

# Week 2 Homework

Six practice problems that revisit the week's topics. The full set should take about **2 hours 15 min** in total. Work in your `hackathon-template` repo (or its `c4-week-02-deploy-drill-<yourhandle>` sibling, where the prompt says) so each problem produces at least one commit you can point to later.

Each problem includes:

- A short **problem statement**.
- **Acceptance criteria** so you know when you are done.
- A **hint** if you get stuck.
- An **estimated time**.

---

## Problem 1 — Pin your toolchain

**Problem statement.** Pin the Node, pnpm, and Python versions your template uses, in three places: `.nvmrc`, `package.json`'s `engines` field, and `.python-version`. Document the chosen versions in the template README's "What is in here" section.

**Acceptance criteria.**

- `.nvmrc` contains exactly the Node major version (e.g. `20`).
- `frontend/package.json` has an `"engines": { "node": ">=20.0.0" }` entry.
- `.python-version` contains the Python major.minor (e.g. `3.11`).
- README mentions the three pinned versions in plain language.
- Committed.

**Hint.** Vercel and Railway both honor these files. Pinning prevents the "works on my laptop" failure when a teammate has Node 21 and you have Node 20.

**Estimated time.** 15 minutes.

---

## Problem 2 — Write the smallest plausible CI

**Problem statement.** In `.github/workflows/ci.yml`, write a CI that (a) installs `pnpm` and runs `pnpm install + pnpm typecheck` in `frontend/`, (b) installs Python and runs `ruff check` (or `python -c "import main"`) in `backend/`. Push and confirm the workflow goes green.

**Acceptance criteria.**

- The workflow file exists at `.github/workflows/ci.yml`.
- It runs on `push` to the default branch.
- It has two jobs: `frontend` and `backend`.
- Both jobs pass on the default branch.
- Total wall time is ≤ 3 minutes (for the median run).
- Committed.

**Hint.** Use GitHub's official `setup-node` and `setup-python` actions, plus `pnpm/action-setup`. Cache `pnpm-store` and `pip` to keep wall time down.

**Estimated time.** 25 minutes.

---

## Problem 3 — A `.env.example` audit

**Problem statement.** Open every file in `backend/` and `frontend/src/` and grep for any reference to `os.environ`, `os.getenv`, or `import.meta.env`. For each env var you find, confirm it is named in the appropriate `.env.example` with a placeholder value. Add any missing entries.

**Acceptance criteria.**

- `backend/.env.example` lists every env var the backend reads.
- `frontend/.env.example` lists every env var (`VITE_*`) the frontend reads.
- The root `.env.example` mentions both as a *summary* and points to the per-service files.
- No real secrets in any of these files. Placeholders only.
- Committed.

**Hint.** Run `grep -r 'os.environ' backend` and `grep -r 'import.meta.env' frontend/src`. The grep output is your work list.

**Estimated time.** 20 minutes.

---

## Problem 4 — Add a deploy section to the template README

**Problem statement.** In the template's README, add a `## Deploying` section that documents exactly the commands a new event repo runs to connect Vercel and Railway, with the env vars each needs. Use the wording from Exercise 3 §3 and §4 as a starting point.

**Acceptance criteria.**

- A `## Deploying` section exists in the template's `README.md`.
- It contains, in order: the Vercel link step, the Railway link step, the env vars each needs by name (with a comment about which is a secret), the CORS-tighten step.
- A reader could follow it linearly without consulting Lecture 2 or Exercise 3 again.
- Committed.

**Hint.** Write it as a *checklist* of commands, not prose. Teammates at hour 2 want copy-paste, not paragraphs.

**Estimated time.** 20 minutes.

---

## Problem 5 — Versioning the template

**Problem statement.** At the bottom of the template's `README.md`, add a version-log table. Seed it with one row representing the work you have done this week. Add a `CHANGELOG.md` file at the repo root that points to the README's version log and says "the canonical version log lives in README.md."

**Acceptance criteria.**

- A version-log table exists at the bottom of `README.md` with columns: Version, Date, What changed, Trigger event.
- At least one row is filled in with today's date and "C4 Week 2 — initial scaffold."
- `CHANGELOG.md` exists and links to the README section.
- Committed.

**Hint.** Future-you cares about *what changed and why*. A row that just says "v1.1" with no reason is dead text. Always include a one-sentence trigger.

**Estimated time.** 15 minutes.

---

## Problem 6 — A 200-word "boring stack" essay

**Problem statement.** Write a 200–250-word essay at `notes/boring-stack-essay.md` (in your `hackathon-template` repo) on one of the following prompts:

- A time you personally adopted unfamiliar tech under deadline pressure and what it cost you.
- The strongest objection you have to the C4 default stack, and the strongest defense of it.
- Why "we'll learn $newtech during the event" appeals to teammates, and one specific phrase you will use to deflect it.

The essay must:

- Be 200–250 words.
- Be three paragraphs.
- Be in C4 voice — blameless, scope-discipline-first, no "rockstar" / "ninja" / "10x."

**Acceptance criteria.**

- File at `notes/boring-stack-essay.md`.
- 200–250 words (run a quick word count).
- Three paragraphs.
- No banned voice words. (Lecture 1 §4.2 gives you the deflection phrase if you pick prompt 3.)
- Committed.

**Hint.** The strongest essays describe a specific event, a specific teammate (anonymized), a specific cost. Avoid generic platitudes.

**Estimated time.** 30 minutes.

---

## Time budget recap

| Problem | Estimated time |
|--------:|---------------:|
| 1 | 15 min |
| 2 | 25 min |
| 3 | 20 min |
| 4 | 20 min |
| 5 | 15 min |
| 6 | 30 min |
| **Total** | **~2 hours 5 min** |

When you have finished all six, push your repo and finalize the [mini-project](./mini-project/README.md) — your `hackathon-template` repo, polished into the deliverable for the week.

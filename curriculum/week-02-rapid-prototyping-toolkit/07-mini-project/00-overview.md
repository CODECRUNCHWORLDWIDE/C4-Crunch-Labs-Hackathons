# Mini-Project — Your `hackathon-template` Repo, Polished

> Take the scaffold from Exercises 1–3 and ship it as a polished public artifact: a personal `hackathon-template` repo on your GitHub that earns the "30-minute scaffold-to-first-route" rule, that a stranger could fork and use, and that you will iterate after every event from Week 10 onward.

This is the only Week 2 deliverable meant to outlive the week. The exercises produced the scaffold, the homework filled in the corners, the challenge cut the time down. They all collapse into one artifact: a **`hackathon-template`** repository, polished, public, versioned, and benchmarked. One repo. One source of truth for "what I bring to every event."

**Estimated time:** ~2.25 hours, split across the suggested schedule (Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday — small polish passes each day).

---

## What you will produce

A single public GitHub repository named `hackathon-template` (or `c4-hackathon-template-<yourhandle>` if your account already has one). It will be linked from your Hackathon Operating Document, Section 3 (My stack defaults), and from any portfolio README you have.

The repository's surface area must include the file shape from Lecture 2, the `bootstrap.sh` from Exercise 2, the deploy configs proven in Exercise 3, the pinned toolchain + CI + `.env.example` audit from the homework, and the `BENCHMARKS.md` from Challenge 1 (or a stub if you skipped the challenge).

---

## Required surfaces

Every item below must appear, in the place specified, with the exact filename shown.

### 1. The README

Lives at `README.md`. Required sections, in order:

- **Title + one-line tagline.** "A pre-tuned full-stack scaffold I bring to every hackathon." Use your own words.
- **Last measured spin-up.** A bold line with a real number from your most recent drill: `> Last measured spin-up: **22 minutes** (Sunday 2025-09-14).`
- **What is in here.** Bulleted summary of the stack (React + Vite + Tailwind + shadcn/ui + react-query frontend; FastAPI + SQLite + JWT auth backend; Vercel + Railway deploy configs; `bootstrap.sh`).
- **How to use.** A 5-step ordered list, copy-pasteable, that ends with "confirm both deploy URLs return 200 OK."
- **Pinned toolchain.** A small table or list of Node version, pnpm version, Python version.
- **Deploying.** The Vercel + Railway connect steps from homework Problem 4.
- **Versioned notes.** The version-log table from homework Problem 5, with at least one row filled in.
- **License.** A short line pointing to `LICENSE`.

### 2. The file tree

The shape from Lecture 2 §2, complete:

```
hackathon-template/
├── .github/workflows/ci.yml
├── .gitignore
├── .env.example
├── .nvmrc
├── .python-version
├── README.md
├── LICENSE
├── bootstrap.sh
├── BENCHMARKS.md
├── CHANGELOG.md
├── frontend/    (full Vite + Tailwind + shadcn/ui + react-query scaffold)
├── backend/     (full FastAPI + SQLite + JWT auth scaffold)
└── deploy/      (vercel.json, railway.toml)
```

Every file is non-empty. Every directory has at least the minimum files documented in Lecture 2 §4.

### 3. `bootstrap.sh`

The script from Exercise 2, in the repo root, executable, with `set -euo pipefail`. It must:

- Validate the first argument.
- Rename project references in three files.
- Seed `.env` files from `.env.example`.
- Install dependencies.
- Reset Git history.
- Print clear next-step instructions.

The script's output ends with the elapsed-time message (`Spin-up took Ns`).

### 4. The deploy proof

The `c4-week-02-deploy-drill-<yourhandle>` repo from Exercise 3 stays public and live, **and** is linked from the template README's "Last measured spin-up" line as evidence:

```markdown
> Last measured spin-up: **22 minutes** ([proof](https://github.com/<you>/c4-week-02-deploy-drill-<you>))
```

A reader can click that link, see the drill repo, and visit the Vercel + Railway URLs that the drill produced.

### 5. The CI badge

The README contains a GitHub Actions status badge at the top:

```markdown
![CI](https://github.com/<you>/hackathon-template/actions/workflows/ci.yml/badge.svg)
```

The badge must be **green** on the default branch at submission time. A red CI badge on the artifact you wrote *this exact week* is the most undermining detail you could ship.

### 6. The benchmarks file

`BENCHMARKS.md` lives at the repo root and contains at least two rows: the "before" run from Exercise 3 and either the "after" run from Challenge 1 or a stub with `not yet measured` if you skipped the challenge.

### 7. A version-log row

The README's version-log section has at least one row, today's date, listing what this scaffold contains and naming "C4 Week 2 — initial scaffold" as the trigger event.

---

## Rules

- **You may** copy text and snippets from Lecture 2, Exercise 1, Exercise 2, Exercise 3, the homework, and Challenge 1. They were always going to feed into here.
- **You may** keep this template in your personal GitHub rather than the C4 fork — but you must link the URL from your Week 2 submission and from your Week 1 Hackathon Operating Document.
- **You may** evolve the format over time. The structure above is the *starter*; later events will add rows, swap libraries, or trim files.
- **You will not** include real secrets in any committed file. Placeholders only.
- **You will not** make the repo private. The template is a portfolio piece.

---

## Acceptance criteria

- [ ] Repo exists at `github.com/<your-handle>/hackathon-template` (or your chosen public name) and is **public**.
- [ ] All seven required surfaces above are present in the form specified.
- [ ] The README's "Last measured spin-up" line is filled in with a real, recent number and links to the deploy-drill repo as proof.
- [ ] The CI badge in the README is **green** on the default branch.
- [ ] `bootstrap.sh` is executable and has been run end-to-end at least once on a scratch event name, with the resulting drill repo public.
- [ ] The Vercel + Railway URLs from the deploy drill are **still live** at submission time.
- [ ] `.env` files are **not** committed to either repo. `.env.example` files **are** committed.
- [ ] License is set (MIT or your preference).
- [ ] At least one version-log row exists in the README.
- [ ] Voice in any README copy is team-room, blameless, scope-discipline-first. No "rockstar" / "ninja" / "10x" / "crush it."
- [ ] Committed to GitHub. Linked from your Hackathon Operating Document, Section 3.

---

## Rubric

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Working scaffold | 25% | Both dev servers run from `bootstrap.sh` output; the deployed frontend talks to the deployed backend |
| 30-minute rule honored | 20% | "Last measured spin-up" is at or under 30 minutes, with a deploy-drill repo as proof |
| Pre-tuning is real, not advertised | 15% | `.gitignore`, `.env.example`, `.nvmrc`, `.python-version`, deploy configs all present and correct |
| CI is green | 10% | The badge in the README is green at submission |
| Documentation a stranger could follow | 10% | README's "How to use" and "Deploying" sections are copy-pasteable, in order |
| Versioning the artifact | 10% | Version-log table exists with at least one honest row; `BENCHMARKS.md` exists |
| Voice | 10% | The README reads like a team-room sticky note, not a marketing page |

---

## What this prepares you for

- **Week 3 — Solo Prototype Sprint.** You will run `bootstrap.sh` against the template to create the Week 3 repo, then *build features* — the first time the week's investment compounds.
- **Week 4 — Agile ceremonies.** The template removes the "we don't have time to set up" excuse; the team can spend its first hour scoping, not yak-shaving.
- **Weeks 7–8 — Team-mode dry-runs.** Your teammates will look at this template when they meet you. The README is your handshake.
- **Week 10 — The real event.** You will fork the template into your team's event repo at hour zero. The team will write product code at hour zero+5 minutes. That is the entire point of Week 2.
- **Every future event.** The template is the longest-lived artifact in C4. The Week 10 repo will be public for years; the template will be edited for years. Treat it accordingly.

---

## Submission

When done:

1. Push the `hackathon-template` repo to GitHub. Public. Default branch.
2. Confirm the CI badge is green and the deploy-drill URLs are still live.
3. Add a link to the template repo in your Hackathon Operating Document (Week 1 mini-project), Section 3 (My stack defaults).
4. In the Code Crunch club channel (or wherever the cohort gathers), post: "Week 2 template is up at [URL]. Spin-up: <N> min." Read one other person's template that day and leave one specific comment — about a *file*, not a generic compliment.

You are now ready for [Week 3 — Solo Prototype Sprint](../../week-03/). In Week 3 you will run `./bootstrap.sh week-03-solo-build` against this exact template and ship a small project, alone, on a six-hour clock, on top of the foundation you just built.

---

*The win is shipping. Setup is half the ship. You shipped the setup. Next week you ship a thing.*

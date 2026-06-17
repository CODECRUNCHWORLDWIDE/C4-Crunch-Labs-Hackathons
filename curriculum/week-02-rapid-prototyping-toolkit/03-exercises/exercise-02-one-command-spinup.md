# Exercise 2 — One-Command Spin-up

**Goal:** Write `./bootstrap.sh <new-event-name>` in your `hackathon-template` repo so that a single command takes the freshly-cloned template to a renamed, configured, deploy-ready new event repo. Prove it works by running it on a scratch event name and checking the output.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

The template repo from Exercise 1 is useful but incomplete. A teammate (or future-you) still has to remember which strings to rename, which files to copy, which directories to `pnpm install` in. That is the work that gets skipped at hour zero of an event, when everyone is talking and nobody owns the scaffold.

`bootstrap.sh` removes the remembering. One command. One new event repo. Always the same.

---

## What to produce

A file `bootstrap.sh` in the root of your `hackathon-template` repo, executable (`chmod +x bootstrap.sh`), that does the following when called as `./bootstrap.sh <new-event-name>`:

1. **Validate input.** If no argument is given, print `usage: ./bootstrap.sh <new-event-name>` and exit non-zero.
2. **Confirm working directory.** If `bootstrap.sh` is not in the current directory (i.e., the user ran it from the wrong place), print a clear error and exit non-zero.
3. **Rename project references.** In `README.md`, `frontend/package.json`, and `backend/pyproject.toml`, replace the string `hackathon-template` with `<new-event-name>`.
4. **Seed `.env` files.** Copy `frontend/.env.example` → `frontend/.env` and `backend/.env.example` → `backend/.env`. Do **not** overwrite an existing `.env`.
5. **Install dependencies.** Run `pnpm install` in `frontend/` and `pip install -e .` (inside a venv) in `backend/`. These can run in parallel.
6. **Reset Git history.** Remove `.git`, run `git init`, stage everything, and create one commit with the message `scaffold <new-event-name> from hackathon-template`.
7. **Print next-step instructions.** A friendly block that names exactly the commands to create the GitHub repo and connect Vercel + Railway. Use the same shape as Lecture 2 §5.

Use the skeleton in Lecture 2 §5 as your starting point. Add comments. Use `set -euo pipefail` at the top.

---

## Step-by-step

### 1. Draft the script

In the root of your `hackathon-template` repo, create `bootstrap.sh` from the skeleton in Lecture 2 §5. Copy carefully; type each line; do not paste a snippet you have not read.

### 2. Make it executable

```
chmod +x bootstrap.sh
```

### 3. Test on a scratch directory

```
cd ..
git clone <your hackathon-template repo> drill-run
cd drill-run
./bootstrap.sh drill-run
```

Confirm each of the seven behaviors above happened:

- README, `package.json`, `pyproject.toml` say `drill-run`, not `hackathon-template`.
- `frontend/.env` and `backend/.env` exist.
- `node_modules/` and `.venv/` exist.
- `git log` shows one commit with the expected message.
- The script printed clear next-step instructions.

### 4. Test the dev servers still work

After `bootstrap.sh` has run on `drill-run`:

```
cd frontend && pnpm dev    # in one terminal
cd backend && source .venv/bin/activate && uvicorn main:app --reload    # in another
```

Confirm the frontend loads, the backend `/health` responds, the placeholder UI displays the response.

### 5. Test the failure cases

Run each of these in a fresh terminal and confirm the script fails *gracefully*:

```
./bootstrap.sh                                 # no argument
./bootstrap.sh some-name                       # from the wrong directory
./bootstrap.sh "name with spaces"              # invalid name
```

Each should print a useful error and exit non-zero. None should leave the repo in a half-modified state.

### 6. Clean up the drill

Delete the `drill-run` directory (`rm -rf ../drill-run`). It was scratch.

### 7. Commit the script

Back in the `hackathon-template` repo:

```
git add bootstrap.sh
git commit -m "add bootstrap.sh: one-command spin-up for new event repo"
git push
```

### 8. Update the README

In the template's README, replace the "Last measured spin-up" placeholder with the actual elapsed time you observed during the drill, with today's date. Commit. Push.

---

## Acceptance criteria

- [ ] `bootstrap.sh` exists in the root of the `hackathon-template` repo.
- [ ] It is executable (`chmod +x` applied).
- [ ] All seven behaviors above are implemented and tested.
- [ ] The script uses `set -euo pipefail`.
- [ ] The script handles the three failure cases above with clear, non-zero exits.
- [ ] You have run the script end-to-end on a scratch event name and confirmed the dev servers start cleanly afterward.
- [ ] The template README's "Last measured spin-up" line is filled in with a real number.
- [ ] At least **three commits** for this exercise (skeleton → tested → README update).

---

## Hints

- **`sed -i` differs between macOS and Linux.** On macOS, `sed -i ''` requires an empty string argument; on Linux, `sed -i` does not. Two portable workarounds: (a) `sed -i.bak '...' && rm *.bak`, or (b) write a tiny Node script `scripts/rename.mjs` and call it from `bootstrap.sh`. Either is fine; the bak-file approach in the Lecture 2 skeleton works on both.
- **Parallel installs save time, but be careful.** If `pnpm install` and `pip install` both error, you want both errors visible, not just the first. The `wait` after `&` only returns the last exit code; consider running serially the first few times you debug.
- **Do not let `bootstrap.sh` push to GitHub for you.** The user wants to inspect the new repo before pushing. Print the `gh repo create` command, do not run it.
- **Idempotency is a stretch goal, not a requirement.** It is fine if running `bootstrap.sh` twice in the same directory breaks. The user clones fresh each time.
- **Print the elapsed time at the end.** Add a `START=$SECONDS` at the top and `echo "Spin-up took ${SECONDS}s"` at the bottom. That number becomes the "Last measured spin-up" entry in your README.

---

## What to do if a step fails

- **`sed` errors with "extra characters at the end of command."** You are on macOS using GNU-`sed` syntax. Use `sed -i.bak` and clean up the `.bak` files.
- **`pnpm: command not found` when running the script.** The script inherits your shell's PATH. Confirm `pnpm` is on your PATH (`which pnpm`) before running.
- **`pip install -e .` fails on a fresh venv.** Confirm you are running from inside the venv (`source .venv/bin/activate`). Some shells deactivate between commands; in shell scripts, you must re-source.
- **`git init` in a directory that already has `.git`.** Fine if you removed `.git` first. If you forgot, the script will fail; that is the correct failure.
- **The new repo's CI is failing.** Likely your CI workflow has hard-coded the old name somewhere (e.g. a job name like `lint-hackathon-template`). Fix it generically — use `${{ github.event.repository.name }}` or just drop the name from the job.

---

## What is next

Move on to [Exercise 3 — Deploy to staging](./exercise-03-deploy-to-staging.md), where you wire Vercel + Railway and prove that pushing a new event repo from `bootstrap.sh` produces a working public URL in under thirty minutes.

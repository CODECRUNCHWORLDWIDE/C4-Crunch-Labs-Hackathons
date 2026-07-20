# Challenge 1 — Shave 30 Minutes Off Your Spin-up

**Time estimate:** ~90 minutes, ideally on a Saturday morning with a clear head.

> This is the canonical Week 2 challenge in C4: profile your end-to-end spin-up, find the slowest steps, change the template to remove or shorten them, and re-drill. The point is to *feel the 30-minute rule* before you ever apply it under pressure.

---

## Problem statement

You ran `bootstrap.sh` and the deploy drill in Exercise 3 and recorded an end-to-end time. Most readers land between **35 and 70 minutes** the first time. That is fine for Exercise 3 — the rule is a target.

For this challenge, you cut at least **30 minutes** off the time and re-drill to prove it. If you started under 30 minutes, you cut the time by half. If you started under 15 minutes, congratulations — pick a stretch goal at the end instead.

You are not allowed to game the metric by skipping steps. The drill must still:

- Run `bootstrap.sh` on a freshly cloned template.
- Push a new public GitHub repo via `gh repo create`.
- Produce a live Vercel URL and a live Railway/Fly URL.
- Have the deployed frontend call the deployed backend and render the response.
- End with you visiting both URLs and confirming a real HTTP response.

---

## Acceptance criteria

- [ ] A `BENCHMARKS.md` file in the `hackathon-template` repo with at least **two** drill runs recorded — the "before" (Exercise 3) and the "after" this challenge.
- [ ] The "after" time is **at least 30 minutes faster** than the "before" (or half, whichever is smaller), or you have hit the 10-minute floor and the file documents that.
- [ ] At least **three template changes** committed and version-logged in the template README, each with a one-sentence reason that names the time saved.
- [ ] A new event repo `c4-week-02-shave-drill-<yourhandle>` that proves the post-shave drill works end-to-end.

---

## How to run the 90 minutes

```
┌────────────────────────────────────────────────────────────┐
│  THE 90-MINUTE SHAVE                                       │
│                                                            │
│  Min 0–10   │ Profile. Drill once, record every step.      │
│  Min 10–20  │ Rank steps by elapsed time, descending.      │
│  Min 20–60  │ For each of the top three steps, ask:        │
│             │   "what does the template need to remove,    │
│             │    pre-install, or pre-configure to make     │
│             │    this step faster or vanish?"              │
│             │ Make the change. Commit. Move on.            │
│  Min 60–80  │ Re-drill on a new event repo.                │
│             │ Record elapsed time per step.                │
│  Min 80–90  │ Write BENCHMARKS.md. Add version-log rows.   │
│             │ Push.                                        │
└────────────────────────────────────────────────────────────┘
```

---

## Where the minutes usually hide

You will know after profiling. As a hint, these are the most common findings in first-time C4 drills:

| Hiding place | Typical fix | Time saved |
|--------------|-------------|------------|
| `pnpm install` on cold cache | Switch to `pnpm` with `corepack`, commit `pnpm-lock.yaml`, use Vercel's cache by default | 2–5 min |
| `pip install` on cold venv | Use `uv pip install` instead of plain `pip` | 1–3 min |
| Manual Vercel project link in the UI | Pre-commit a `vercel.json` and use `vercel --prod` from CLI | 5–10 min |
| Manual Railway service config in the UI | Commit `railway.toml` with start command + buildpack | 5–10 min |
| Manual env-var entry per deploy | Use `vercel env add` and `railway variables set` in the script | 3–5 min |
| Wrong Node version, build re-deploys | Pin in `engines.node` and `.nvmrc` | 5–8 min |
| CORS error, re-deploy backend | Hard-code a *list* of allowed origins, including a localhost entry | 2–4 min |
| Re-typing the same `gh repo create` flags | Add a `.template` line in the README the user copy-pastes | 1–2 min |

You will find your own. The list above is a hint, not a checklist.

---

## The `BENCHMARKS.md` format

```markdown
# hackathon-template — benchmarks

| Date       | Run name           | bootstrap.sh | gh push | Vercel | Railway | wired? | Total |
|------------|--------------------|-------------:|--------:|-------:|--------:|:------:|------:|
| 2025-09-12 | deploy-drill (E3)  | 4:30         | 0:30    | 12:00  | 14:00   |   y    | 31:00 |
| 2025-09-13 | shave-drill (C1)   | 2:10         | 0:30    | 4:00   | 5:30    |   y    | 12:10 |

## Notes
- 2025-09-13: switched `pip` → `uv pip`; committed railway.toml; pre-set Vercel env via `vercel env add`. The Vercel UI clicks are now zero.
```

The file is for *you*, future-you. Be honest. If the second drill was 28 minutes, write 28 minutes. The point of measuring is to see drift.

---

## Constraints (these are the point)

- **The post-shave template must still work for a teammate.** No undocumented shortcuts that depend on your shell aliases. Anything that saved you time at this drill must save a stranger time at the next event.
- **The post-shave drill is on a fresh event name.** Re-using the deploy-drill repo does not count — that one has warm caches.
- **You may use AI assistants** as you would at a real event. Track which steps were assisted; that information is useful in the post-mortem.
- **You may not** install paid tooling. Free tier only.
- **The wall clock counts.** Coffee breaks are fine, but they consume the 90 minutes.

---

## Rubric (for self-grading)

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Real time saved | 30% | At least 30 minutes faster, or ≤ 15 minutes total and held |
| Template changes survive a stranger | 25% | A teammate could read the README and reproduce the time |
| BENCHMARKS.md exists and is honest | 15% | Both runs recorded with sub-times, not just totals |
| Version-log rows added | 15% | Each template change has a row with a one-sentence reason |
| Post-shave drill is real end-to-end | 15% | Frontend talks to backend, CORS tightened, URL public |

---

## Stretch (only if you finish under 60 minutes)

- **Try Fly.io as a Railway alternate.** Fly's free tier is more durable for "I want this demo URL to stay live for six months." Add it as an alternate deploy path in your template, with a `deploy/fly.toml`.
- **Add an observability hook.** Two lines in `main.py` that log every request to stdout. Hackathon teams almost never have logging.
- **Make `bootstrap.sh` print the *gh*, *vercel*, and *railway* commands as a checklist.** Paste-able into a teammate's terminal in order.
- **Write a 200-word post-mortem at `BENCHMARKS.md`'s bottom.** What surprised you about where the minutes lived?

---

## Submission

When done:

1. Push both repos (template + shave-drill).
2. Make sure both deploy URLs from the shave-drill are live at the time you submit.
3. Drop the template repo link and the new "Last measured spin-up" number into your Code Crunch club channel.

You will reference this benchmark at Week 3 (the solo prototype sprint, where you will discover whether the time you saved survives a real build) and at Week 7 (the team-mode dry-run, where your template meets other people's expectations).

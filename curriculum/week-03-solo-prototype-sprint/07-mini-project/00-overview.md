# Mini-Project — The Six-Hour Solo Build + Recorded Demo + Written Retro

> Run the six-hour solo build on Saturday on top of your Week 2 `hackathon-template`, ship a live deploy URL, record a three-minute demo, and commit a structured blameless retro. Three artifacts, one repo, one Saturday. This is the week.

This is the only Week 3 deliverable that matters. Exercises 1–3 prepared the artifacts; the homework sharpened the edges; the challenge (optional) added a partner. They all collapse into one repository on Saturday afternoon: a **solo prototype** with a live URL, a recorded demo, and a `retro/RETRO.md` that names three behaviors you will change at the next build.

**Estimated time:** ~8 hours, structured as the six-hour Saturday build plus ~2 hours of Sunday polish (demo re-take if needed, retro polish, submission).

---

## What you will produce

A single public GitHub repository named `c4-week-03-solo-build-<yourhandle>` (or any public name; the slug just makes it easy for the cohort to find each other's). It will be linked from your Hackathon Operating Document (Week 1 mini-project) and from your `hackathon-template` repo's "Last measured" log.

The repository's surface area must include the built scaffold from your Week 2 template, the MUST feature shipped end-to-end, the deployed frontend and backend URLs, the recorded demo file, the committed `retro/RETRO.md`, and a README a stranger could read and understand in two minutes.

---

## Required surfaces

Every item below must appear, in the place specified, with the exact filename shown.

### 1. The README

Lives at `README.md` in the build repo. Required sections, in order:

- **Title + one-line tagline.** Use your prompt sentence from Exercise 1.
- **Who hurts.** One sentence naming the human (initials or first name fine).
- **Live URL.** The deployed frontend URL, in bold. The deployed backend URL or `/health` URL below it.
- **The demo.** A link to the recorded `.mp4`, `.mov`, `.webm`, or Loom URL. The three-minute strip labels (hook / problem / solution / ask) with their timestamps.
- **What is in here.** Bulleted summary of the stack inherited from `hackathon-template`, with anything you swapped.
- **How to run.** A 5-step ordered list, copy-pasteable, that ends with "both dev servers running and the MUST screen visible at `localhost:5173`."
- **Build clock — what actually happened.** A table of the seven hour-rows, with one line per hour summarizing what you shipped and any cut. Honest reporting, including hours where you fell behind.
- **Retro.** A link to `retro/RETRO.md` and a one-sentence summary of the three-behaviors line.
- **License.** A short line pointing to `LICENSE` (MIT or your preference).

### 2. The file tree

```
c4-week-03-solo-build-<yourhandle>/
├── README.md
├── LICENSE
├── frontend/        (inherited from hackathon-template, with MUST feature wired)
├── backend/         (inherited from hackathon-template, with MUST route)
├── deploy/          (vercel.json, railway.toml — already there from template)
├── demo/
│   └── demo-take-final.<ext>
└── retro/
    ├── RETRO.md
    └── screenshots/
        ├── hour-1-deploy.png
        ├── hour-3-checkpoint.png
        └── hour-6-final.png
```

Every file is non-empty. The `demo/` directory contains the take you submit; you may keep `demo-take-1.<ext>` and `demo-take-2.<ext>` if you want, but `demo-take-final.<ext>` is the canonical one. If the file is over 50 MB, link to a Loom or YouTube unlisted URL instead and put a `demo/README.md` with the link.

### 3. The MUST feature, end to end

The single MUST feature from your Exercise 2 MoSCoW chart is wired end to end:

- The frontend has a route or component that renders the MUST screen.
- The backend has at least one route the MUST screen calls (or, if pure-frontend, the MUST screen handles its own state with hardcoded seed data).
- The deployed frontend talks to the deployed backend (CORS configured, env vars set).
- A reader visiting the live frontend URL can perform the MUST verb and see the result.

### 4. The live deploy URLs

Both URLs are reachable from the public internet at the time of submission. The frontend URL ends with `.vercel.app` (or your custom domain). The backend `/health` URL returns 200 with a JSON body. Both are linked from the README.

If your backend is sleeping on Railway free tier at submission time, that is acceptable as long as the URL responds with 200 within 30 seconds of being hit. Note the cold-start behavior in the README so a reader is not surprised.

### 5. The three-minute demo recording

The recording is:

- Three minutes long, give or take 10 seconds.
- In the four-band structure (hook 0:30, problem 0:45, solution 1:30, ask 0:15).
- Shows the live URL on screen for at least 60 seconds inside the solution band, with the URL bar visible.
- Has audible narration (your voice). Captions optional but appreciated.
- Committed to `demo/demo-take-final.<ext>` or linked from `demo/README.md`.

### 6. The committed retro

`retro/RETRO.md` exists and follows the template from Lecture 2 §7:

- The metadata block (build repo URL, live URL, demo URL, total build time, MUST line, MUST shipped Y/N/Partial with one-sentence evidence).
- Keep / Start / Stop columns, each with 1–4 evidence-anchored bullets.
- The **three behaviors I will change at the next build** section, each with a *when* and a *what*.
- An optional "Notes for the next iteration of `hackathon-template`" section if you found friction in your template during the build.

Total retro length: 300 to 600 words.

### 7. The screenshots

At least two screenshots committed to `retro/screenshots/`:

- One screenshot of the live URL at submission (proof of "still live").
- One screenshot of either a broken state during the build (good — the retro discusses it) or the green deploy at hour one.

---

## Rules

- **You will** build on top of your Week 2 `hackathon-template`. You may use a different stack if you have a working alternate template, but you will not "scaffold from scratch" — the whole point of Week 2 is that you do not.
- **You may** use AI coding assistants the way you would at a real event. Note in the retro which steps were assisted; that information is useful.
- **You may** keep the build repo in your personal GitHub. Public is required; private is a failed mini-project.
- **You will not** ship a build that depends on a localhost-only URL. The MUST feature lives on the deployed frontend, period.
- **You will not** improvise the retro. Use the Lecture 2 §7 template until you outgrow it (which is after Week 8 at the earliest).
- **You will not** skip the recording. The demo is non-negotiable. If OBS is broken, use Loom. If Loom is broken, use your phone pointed at your screen. Some recording. Three minutes. The recording is the artifact.
- **You will not** edit the prompt during the build. Saturday-you does not override Wednesday-you. The prompt is locked at Exercise 1.

---

## Acceptance criteria

- [ ] Repo exists at `github.com/<your-handle>/c4-week-03-solo-build-<your-handle>` (or your chosen public name) and is **public**.
- [ ] All seven required surfaces above are present in the form specified.
- [ ] The frontend live URL is reachable and returns the MUST screen.
- [ ] The backend `/health` URL (or equivalent) returns 200.
- [ ] The recorded demo is committed (or linked) and is between 2:45 and 3:15 long.
- [ ] `retro/RETRO.md` exists, follows the Lecture 2 §7 template, and contains exactly three behaviors with a *when* and a *what* each.
- [ ] At least two screenshots are committed in `retro/screenshots/`.
- [ ] The README's "Build clock — what actually happened" table has all seven hour-rows filled in honestly (including hours where you fell behind or rolled back).
- [ ] No real secrets are committed. `.env.example` only.
- [ ] License is set.
- [ ] Voice in any README or retro copy is team-room, blameless, scope-discipline-first. No "rockstar" / "ninja" / "10x" / "crush it." No emojis.
- [ ] Linked from your Hackathon Operating Document (Week 1 mini-project) and noted in your `hackathon-template` repo's version log.

---

## Rubric

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| MUST shipped on a live URL | 25% | Frontend live, backend live, MUST verb performable from the public internet at submission |
| Recorded three-minute demo | 20% | Four-band structure, live URL visible, audible narration, between 2:45 and 3:15 |
| Retro is structured, blameless, behavior-producing | 20% | Lecture 2 §7 template followed, three behaviors with *when* + *what*, evidence-anchored |
| The build clock table is honest | 10% | Includes the hour the deploy broke, the cut that saved hour 5, the roll-back at 5:55 — if any happened |
| README a stranger could follow | 10% | Live URL bold at top, "How to run" copy-pasteable, "Who hurts" sentence specific |
| The repo is publicly reachable + license set | 5% | Public repo, MIT or equivalent LICENSE file |
| Voice (blameless, team-room, no banned words) | 10% | Reads like a sticky note from a tired but proud team-room, not marketing copy |

---

## What this prepares you for

- **Week 4 — Agile ceremonies, real-world version.** The hourly stand-up, the cut reflex, and the demo recording become *team* rituals. You bring the rhythm from Week 3.
- **Week 5 — Scoping discipline.** Your MoSCoW chart from Exercise 2 is the prototype of the team MoSCoW. Your WON'T list is the prototype of the team's WON'T list.
- **Week 6 — Pitch craft.** You will re-record the Week 3 demo with the Week 6 lecture's polish notes. The Saturday recording is the *before*; the Week 6 take is the *after*.
- **Week 7 — Team-mode dry-run, day 1.** You bring this template plus the MUST-feature rhythm to a six-hour mock event with teammates. The solo loop becomes a team loop.
- **Week 10 — The real event.** The retro you write this week is the prototype of the retro you write 72 hours after the real hackathon. Your three-behaviors line for Week 10 may directly cite the Week 3 retro as evidence of how your habits have changed.

---

## Submission

When done:

1. Push the build repo to GitHub. Public. Default branch. CI badge green if you copied CI from the template.
2. Confirm the frontend URL and backend `/health` URL are both live.
3. Confirm the recorded demo is committed (or linked from `demo/README.md`).
4. Confirm `retro/RETRO.md` is committed and follows the template.
5. Add a link to the build repo in your Hackathon Operating Document, Week 1 mini-project, alongside your stack defaults.
6. Add a row to your `hackathon-template` repo's version-log table: "C4 Week 3 — first solo build; \<one-line lesson for the template\>."
7. In the Code Crunch club channel (or wherever the cohort gathers), post: "Week 3 solo build is up at [URL]. Live demo: [URL]. Three-behavior change: \<paste your three behaviors\>." Read one other person's retro that day and leave one specific comment — about a *behavior*, not a generic compliment.

You are now ready for [Week 4 — Agile Ceremonies, Real-World Version](../../week-04/). In Week 4 you will run a stand-up, a demo, and a retro with a *team* — and the rhythm you just felt alone is the rhythm you will help a team hold.

---

*The win is shipping. You shipped one alone. The retro is in the repo. Now we go ship together.*

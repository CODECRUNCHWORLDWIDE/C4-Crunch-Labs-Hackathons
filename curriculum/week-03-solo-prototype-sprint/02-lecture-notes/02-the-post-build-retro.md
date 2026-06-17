# Lecture 2 — The Post-Build Retro

> **Duration:** ~1 hour of reading.
> **Outcome:** You can run a structured blameless retro on yourself, fill in keep / start / stop columns with specific evidence, and name three behaviors — not goals, not vibes — that you will change at the next build. You can distinguish a retro from a journal and from a brag-doc.

If you only remember one sentence from this lecture, remember this:

> **A retro that does not change a behavior is a journal entry.** The point of the retro is not to feel things about the build; it is to name the next concrete change. Three behaviors, written down where future-you sees them, before the next build.

Lecture 1 taught you the rhythm of the build. Lecture 2 teaches you the rhythm of what comes after — the structured, blameless, behavior-changing retro. The build is the rehearsal. The retro is the performance review of the rehearsal, written by future-you, for future-you, on the same evening as the build.

---

## 1. What a retro is, and what it is not

A retro is a **structured reflection that produces a list of behaviors to change.** Not a feeling. Not a recap. A list.

### 1.1 What it is

- **Structured.** It has columns or sections you fill in the same way every time. Structure is the only defense against vibes.
- **Evidence-based.** Every claim is anchored to something specific from the build: a commit, a screenshot, a deploy URL, an hour-of-day note from your scratch file.
- **Blameless.** Even when you are the only person in the build, you do not call yourself names. "The sprint board did not catch X" — not "I am bad at X."
- **Action-producing.** It ends with three specific behaviors to change at the next build. If it does not, it is not done.

### 1.2 What it is not

- It is not a **journal**. A journal is "today I felt frustrated." A retro is "at hour three, I felt frustrated *because* the deploy URL had drifted from the localhost, and the next behavior is to add a deploy-check to the hourly stand-up."
- It is not a **brag doc**. "I shipped a working app in six hours" is fine to say in the cohort channel; it is not the retro. The retro asks what went wrong, not what went right.
- It is not a **post-mortem**. A post-mortem is for an event with a clear failure (a downed service, a missed deadline). A retro is for any iteration whether it succeeded or not.
- It is not a **roadmap**. "Next time I will add user accounts" is a feature wish, not a behavior. The retro changes behaviors, not feature lists.

> **C4 voice:** the retro is not where you process your feelings. The retro is where you write the three sentences that change what you do at hour two of the next build.

---

## 2. The blameless voice, applied to yourself

Week 1 introduced the blameless retro at the team scale: "the sprint board did not catch the API rate limit" — not "Pat broke the rate limit." On a solo build, the blameless voice is harder because the only "Pat" in the room is you.

### 2.1 Why blameless matters when the team of one is you

Two reasons, both mechanical:

1. **Self-blame produces less behavior change than blameless analysis.** "I am bad at scoping" terminates the inquiry. "The MoSCoW chart I wrote on Wednesday did not list deploy as a MUST" continues it.
2. **The retro is a public artifact.** You will commit it to a repo. A teammate at the next event might read it. The voice you use to describe yourself in your own retro is the voice that teammate will hear.

### 2.2 The translation table

```
┌────────────────────────────────────────────────────────────┐
│  SELF-BLAME VOICE          →   BLAMELESS RETRO VOICE       │
│                                                            │
│  "I am bad at scoping."    →   "The MoSCoW from Wed did    │
│                                not list deploy as a MUST." │
│                                                            │
│  "I wasted hour 3 on a    →   "The hourly stand-up did     │
│   stupid framework bug."       not catch the framework bug │
│                                early because I had not     │
│                                added 'is the deploy still  │
│                                green' as a check."         │
│                                                            │
│  "I am too slow."         →   "The opening-hour ritual     │
│                                took 75 minutes, not 60,    │
│                                because pnpm install hit a  │
│                                cold cache; pre-warm next   │
│                                time."                      │
│                                                            │
│  "I will do better."      →   "Behavior change: add        │
│                                'deploy URL still 200?' to  │
│                                the hourly stand-up sheet." │
└────────────────────────────────────────────────────────────┘
```

The right column is harder to write. It is also the column that changes the next build. Practice it.

### 2.3 What blameless is not

Blameless is not "everything is fine." It names problems forcefully. It just does not assign them to a person; it assigns them to a *system* — the MoSCoW chart, the timer, the hourly check, the template, the scratch file, the freeze rule. Systems can be changed. "Pat" — or "me" — cannot be changed by a retro line. A check on the hourly stand-up sheet can.

---

## 3. The keep / start / stop structure

C4's default retro shape is three columns: **keep, start, stop**. One to four bullets each. Each bullet is one to two sentences, evidence-anchored.

```
┌────────────────────────────────────────────────────────────┐
│  RETRO — SOLO BUILD, SAT <DATE>                            │
│                                                            │
│  KEEP                                                      │
│  - The opening-hour ritual ended with a green deploy at    │
│    minute 52. Carry the ritual to every build.             │
│  - The MoSCoW chart from Wed listed two clear WON'T lines  │
│    (auth, real-time) and I held them both.                 │
│                                                            │
│  START                                                     │
│  - Adding a "deploy still 200?" check to the hourly        │
│    stand-up sheet. Hour 3 deploy was broken; I noticed at  │
│    hour 4.                                                 │
│  - Writing the demo script in the README *before* the      │
│    build. I improvised on Saturday and the hook was weak.  │
│                                                            │
│  STOP                                                      │
│  - Touching CSS after hour 4. I spent 25 min on a card     │
│    radius that did not appear in the demo recording.       │
│  - Adding "small SHOULDs" mid-build. I added a second      │
│    seeded example at hour 3 that pushed the MUST screen    │
│    to hour 5:10.                                           │
└────────────────────────────────────────────────────────────┘
```

### 3.1 KEEP — what worked, with evidence

"Keep" is not a brag column. It is a *carry-forward* column. The point is to remember the small things that worked so you replicate them — not to feel good about yourself. Each KEEP bullet should be a habit, ritual, or artifact that the next build needs to inherit.

Bad KEEP: "Worked hard."
Good KEEP: "Set the kitchen timer at hour zero and obeyed every ding. Carry the exact ringtone forward."

### 3.2 START — what was missing

"Start" is the column of new habits or artifacts you need. Each bullet should name a *behavior* and an *anchor* — when in the next build it will fire. "Start journaling more" is not a behavior. "Start writing one line in the scratch file at every hourly stand-up about whether the deploy is still 200" is a behavior.

The most common Week 3 START bullets, across past cohorts:

- Start running the deploy check inside the hourly stand-up.
- Start writing the demo script in the README on Wednesday, not on Saturday at hour 5:30.
- Start setting an actual kitchen-timer ringtone, not a silent phone notification.
- Start naming the WON'T list out loud during the opening-hour ritual.

### 3.3 STOP — what cost time without value

"Stop" is the most uncomfortable column. It names the thing you *did* that hurt the ship. Self-blame is forbidden; behavior naming is required.

Bad STOP: "Stop being a perfectionist."
Good STOP: "Stop adding 'just one more' SHOULD bullet to MUST mid-build. At hour 3, the second seeded example pushed MUST to hour 5:10."

STOP bullets often correspond to one of the eight failure modes from Lecture 1 §8. That is fine — name the specific one you hit and the specific cost.

---

## 4. The three-behaviors-to-change line

Keep / start / stop is the analysis. The **three-behaviors-to-change** line is the payload. It is the line that, six weeks from now, you will copy into the next event's pre-game checklist. The grade of this week's retro turns on whether this line is sharp.

### 4.1 The shape

```
┌────────────────────────────────────────────────────────────┐
│  THREE BEHAVIORS I WILL CHANGE AT THE NEXT BUILD           │
│                                                            │
│  1. At hour 0:00, I will set a real kitchen-timer with a   │
│     loud ringtone, not a silent phone vibration.           │
│                                                            │
│  2. At every hourly stand-up, I will curl my deploy URL    │
│     and write the HTTP status in the scratch file before   │
│     answering the four questions.                          │
│                                                            │
│  3. By Wednesday, the demo script will be in the README of │
│     the build repo, three short paragraphs, before I write │
│     the first line of feature code on Saturday.            │
└────────────────────────────────────────────────────────────┘
```

Each behavior has three components:

- **When** — the anchor in time. "At hour 0:00," "by Wednesday," "at every hourly stand-up." A behavior without a when is a wish.
- **What** — the specific action. "Set a kitchen-timer," "curl the deploy URL," "write the demo script."
- **Why it survives** — implicit in the specificity. Specific behaviors survive Saturday morning grogginess. "Be more disciplined" does not.

### 4.2 Why exactly three

Not one (you will not change a habit if you only name one — you will forget it). Not five (you cannot hold five new behaviors at the next build — you will hold zero). Three is the working number. It is also the number the capstone rubric grades on (see SYLLABUS §"Capstone rubric": "Post-mortem identifies 3 specific behaviors to change for the next event").

### 4.3 Behaviors vs goals — the test

```
┌────────────────────────────────────────────────────────────┐
│  BEHAVIOR (good)             GOAL (bad)                    │
│                                                            │
│  "Curl deploy URL each       "Be more disciplined about    │
│   hourly stand-up."           deploys."                    │
│                                                            │
│  "Write demo script in      "Practice my demo more."       │
│   README by Wednesday."                                    │
│                                                            │
│  "Run bootstrap.sh on a     "Be better at the toolkit."    │
│   scratch event name        ·                              │
│   Friday night."                                           │
└────────────────────────────────────────────────────────────┘
```

If your line passes the "I could film myself doing it" test, it is a behavior. If it does not, rewrite it.

---

## 5. Evidence is the glue

A retro without evidence is a vibes retro. Every bullet in keep / start / stop and every behavior in the three-behavior list must be tied to a specific artifact from the build. Concretely, your retro should reference:

- **Commit hashes** — "commit `a3f2d1c` at minute 47 was the first green deploy."
- **Timestamps from your scratch file** — "the hourly stand-up at 13:00 noted MUST was still on localhost."
- **Screenshots** — one of the live URL, one of the broken state if relevant. Drop them in `retro/screenshots/`.
- **Lines from the demo recording** — "at 1:34 in the recording, the page hangs for 2 seconds; that is the loading-state bug the retro should name."
- **Specific files** — "the `frontend/.env.example` was missing `VITE_API_URL` and I rediscovered that at hour 1:15."

You will not write evidence-rich retros the first time. That is fine. Start with one evidence anchor per bullet by Week 5 and you are well ahead of most cohorts.

### 5.1 The scratch file is the evidence

You wrote a one-line answer to each hourly stand-up's four questions during the build. That scratch file is the primary source for the retro. Read it once before you write a single bullet. Most of the retro is already in the scratch file; the retro is the synthesis.

If you did not keep a scratch file during the build, the first behavior on your three-behavior list is **"Keep a scratch file at every hourly stand-up."** Welcome to the club. Most learners hit this in Week 3.

---

## 6. Writing the retro: when, where, how long

### 6.1 When

The retro starts **during** the build, in your scratch file. The retro draft is written **at hour 5:30–6:00** inside the freeze, while the build is still hot. The retro is polished and committed **on Sunday morning**, after one night of sleep.

Drafting during the freeze captures specifics that fade. Polishing on Sunday lets you see the build with sleep-distance. Both passes matter. Skipping either one weakens the retro.

### 6.2 Where

The retro lives in the solo-build repo at `retro/RETRO.md`. Not at the top of the README. Not in a Notion page. Not in a private journal. A committed file in the public repo so a teammate at the next event can read it.

```
solo-build-repo/
├── README.md
├── frontend/
├── backend/
└── retro/
    ├── RETRO.md
    └── screenshots/
        ├── hour-1-deploy.png
        ├── hour-3-broken.png
        └── hour-6-final.png
```

### 6.3 How long

A solo Week 3 retro is **300 to 600 words**. Shorter is suspicious. Longer is usually a journal entry that wandered in. The constraint is the discipline.

---

## 7. The retro template

Use this template until you outgrow it. Most learners outgrow it around Week 8.

```markdown
# Retro — Solo Build, <DATE>

**Build repo:** <URL>
**Live URL:** <URL>
**Demo recording:** <URL or path>
**Total build time:** Xh Ymin (target was 6h 0min)
**MUST line:** <one sentence>
**MUST shipped?** Yes / No / Partial — <one sentence of evidence>

## Keep
- <bullet, evidence-anchored>
- <bullet, evidence-anchored>

## Start
- <bullet, evidence-anchored>
- <bullet, evidence-anchored>

## Stop
- <bullet, evidence-anchored>
- <bullet, evidence-anchored>

## Three behaviors I will change at the next build
1. <when> + <specific action>
2. <when> + <specific action>
3. <when> + <specific action>

## Notes for the next iteration of `hackathon-template`
- <one line, optional>
- <one line, optional>
```

The last section — "Notes for the next iteration of `hackathon-template`" — is the bridge back to Week 2. If you found a friction point in your template during the build, you have a row to add to the template's `CHANGELOG.md` next time you open it.

---

## 8. Reading other people's retros

The retro is a public artifact partly because reading other learners' retros is the second-most useful thing you do in Week 3. Patterns across solo builds tell you which behavior changes are common (so you can adopt them pre-emptively) and which are personal (so you do not waste effort copying them).

### 8.1 What to look for in another retro

- **Behaviors that show up in three or more retros.** That is a class signal. Promote it to your own list even if you did not hit the issue yourself.
- **Behaviors that are specific to a stack choice.** "Pre-warm pnpm cache" is a Node-stack behavior. If you are on a different stack, the equivalent behavior — not the literal one — is what you need.
- **The honesty of the MUST-shipped line.** A retro that reports "Partial" is more useful than a retro that reports "Yes" with no evidence. Learn from the honest ones.

### 8.2 What to leave alone

- **The build itself.** The retro is the artifact; the build is the rehearsal that produced it. Do not browse other people's builds and feel bad. Read the retros.
- **The voice.** Adopt the structure; keep your own voice. Imitating C4 phrasing one-for-one produces flat retros. Use the columns; speak naturally inside them.

---

## 9. The retro is the Week 3 grade

Re-read the SYLLABUS capstone rubric: "Post-mortem identifies 3 specific behaviors to change for the next event" is worth 15% of the *final capstone grade*. Week 3 is the first time you write one. The artifact you produce this week is the prototype of the artifact you will produce after the real event in Week 10.

If the Week 3 retro is sloppy — feelings, no evidence, three "goals" instead of three behaviors — the Week 10 retro will be sloppy under far worse conditions (post-event exhaustion, team feelings, public eyes). Practice now.

The mini-project's acceptance criteria are explicit: the retro is committed at `retro/RETRO.md`, it follows the template above, it names three behaviors with when-and-what specificity, and it is in blameless voice. A missing retro is a failed mini-project, no matter how good the build was.

---

## 10. Recap

- A retro is structured, evidence-based, blameless, and action-producing. It is not a journal, brag doc, post-mortem, or roadmap.
- Blameless voice applied to yourself: name systems, not selves. The translation table is the practice.
- Keep / start / stop, one to four bullets each, evidence-anchored.
- The three-behaviors-to-change line is the payload. Behaviors have a when and a what.
- Evidence is the glue: commit hashes, timestamps, screenshots, demo lines, file paths.
- Draft during the hour-five freeze, polish Sunday morning. Both passes matter.
- The retro lives in the repo at `retro/RETRO.md` — public, committed, readable.
- Reading other learners' retros is the second-most useful Week 3 activity. Look for patterns.

Return to [Lecture 1 — The Six-Hour Solo Build](./01-the-six-hour-solo-build.md) once more on Friday night, then run the build. The retro is waiting for the build to produce it.

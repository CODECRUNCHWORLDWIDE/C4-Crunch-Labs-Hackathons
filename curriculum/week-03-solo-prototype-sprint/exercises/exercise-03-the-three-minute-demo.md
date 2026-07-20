# Exercise 3 — The Three-Minute Demo

**Goal:** Draft the three-minute demo script *before* you write a single line of feature code. By the end of the exercise, you have a written script in the build repo's README, sectioned into the four C4 demo bands (hook, problem, solution, ask), and a clear plan for what is on screen at every band.

**Estimated time:** 45 minutes.

---

## Why this exercise exists

Lecture 1 §7 said: the recording is the artifact. The single largest cause of weak Week 3 demos is improvising the script on Saturday at hour 5:30. The script is calmer than your Saturday brain. Drafting it on Friday — with the prompt fixed, the MoSCoW fixed, and the hourly clock written — produces a demo script that *steers* the build, not one that *describes* it after the fact.

A demo script written before the code also catches over-scope: if the script reads "and then the user logs in and shares the result," you wrote a script for a build you cannot ship. Cut the script. Then cut the build.

---

## What to produce

A `## Demo Script` section inside the README of the build repo (or, until the build repo exists Saturday, in `week-03-prep/demo-script.md`). The section contains:

1. The four-band breakdown, with one to three sentences per band.
2. A "what is on screen" note for each band.
3. The single "ask" line.
4. A list of crash-safe paths — what you fall back to if the live URL hiccups during recording.

---

## Step-by-step

### 1. Re-read the three-minute strip

From the C4 brand voice (and Lecture 1 §7.1):

```
[ 0:00 — 0:30 ] hook         | who's hurting + the punch
[ 0:30 — 1:15 ] problem      | concrete, narrow, specific
[ 1:15 — 2:45 ] solution     | walkthrough + demo clip
[ 2:45 — 3:00 ] ask          | one ask, one number
```

Mono. Strict. Three minutes is three minutes.

### 2. Draft the hook (0:00–0:30)

Write two to three sentences. Open by naming the human from Exercise 1 and the pain. End with one punchy sentence that names the tool.

> **Example:** "My roommate refreshes the bus app every minute when she is running late. The bus app is one second old and her brain is twenty seconds gone. This is a six-hour build of a bus-time saver that pins the next three departures so she stops refreshing."

What is on screen: your face if you are using a webcam overlay, otherwise the build repo's README scrolling lazily. Not the live URL yet — save it for the solution band.

### 3. Draft the problem (0:30–1:15)

Three to four sentences. Get *more* specific. Time of day, what she does instead, what costs the bad behavior produces. Resist the urge to add features in this band; the problem band is where you earn the demo's right to exist.

What is on screen: a screenshot of the existing bus app on her phone, or a Slack screenshot of her texting you about the problem. Anything that anchors the pain in a real artifact.

### 4. Draft the solution (1:15–2:45)

This is the longest band. Ninety seconds. Walk through the demo path you described in Exercise 1 §4. Two sentences of setup, then the click, the wait, the result. *Show the live URL.*

> **Example walkthrough script:** "Here is the live URL. I paste my home stop and the bus number. I click Save. The next three departures pin to the top. I close the tab, re-open the URL — they are still there. That is the entire scope of the build. Six hours, one user, one verb."

What is on screen: the live URL, the URL bar visible, your cursor doing the demo path slowly enough that the viewer can read what is happening. No live coding. No DevTools panel. The URL bar and the page.

### 5. Draft the ask (2:45–3:00)

One sentence. From Lecture 1 §7.3: on a solo Week 3 demo, the ask points at the retro. Something like:

> "If you've shipped something on a six-hour clock, tell me one cut I should have made earlier. The retro is in `retro/RETRO.md` in this repo."

That is the entire ask. Do not pad. Three minutes is three minutes.

### 6. Write the crash-safe paths

Below the script, add a short list titled **"Crash-safe paths."** What do you do if:

- The live URL hangs during recording? (Have a 5-second pre-recorded clip of the same path queued.)
- The backend is sleeping (Railway free tier)? (Hit the URL once two minutes before recording to warm it.)
- A typo in your script throws you off? (Pause, breathe, restart the sentence. Re-take is cheap.)

You will not use all of these. Having the list means you do not improvise the recovery on Saturday.

### 7. Commit

```
git add week-03-prep/demo-script.md
git commit -m "week 3 prep: 3-min demo script (pre-build)"
git push
```

On Saturday, copy this section into the build repo's README at hour 0:30 (during the opening-hour ritual).

---

## Acceptance criteria

- [ ] A `## Demo Script` section exists in `week-03-prep/demo-script.md` (or build repo README).
- [ ] The four bands are labeled with the exact timestamps `0:00–0:30`, `0:30–1:15`, `1:15–2:45`, `2:45–3:00`.
- [ ] Each band has a one-line "what is on screen" note.
- [ ] The single "ask" line points at the retro, not at users or capital.
- [ ] The crash-safe paths list has at least three entries.
- [ ] The script reads in under three minutes when you say it out loud at a normal pace. (Yes, time yourself before you commit.)
- [ ] No banned voice. No emojis.

---

## Hints

- **Read it out loud and time it.** Most first drafts are 90 seconds, not 180. That is fine — you add detail. Some are 4:30 — you cut. Either way, do not skip the timer.
- **The hook names a human.** "Users" is not a hook. "My roommate" is. "The Tuesday-night photography club" is. Specificity is the hook.
- **One ask, one number.** Lecture 1 §7.3. Two asks is zero asks; the viewer remembers nothing.
- **The URL bar is on screen during the solution band.** Re-read Lecture 1 §7.2 if tempted to cut to a slide. The URL bar is part of the proof.

---

## What to do if you cannot fit it in three minutes

You have three options:

1. **Cut the problem band by 15 seconds.** Most over-long demos over-explain the problem. The hook already sketched it; the problem band is a deepening, not a re-statement.
2. **Cut a feature from MUST.** If your solution band needs more than 90 seconds to walk through, the build is over scope. Go back to Exercise 2 and cut.
3. **Speed up your speech.** Last resort. A faster cadence is fine; a rushed cadence kills the demo. If you sound rushed at 180 seconds, the script is too long, not your mouth.

---

## What is next

Friday night: re-read [Lecture 1](../lecture-notes/01-the-six-hour-solo-build.md) §4 (the opening-hour ritual) and §6 (the hour-five freeze). Pre-warm OBS. Charge your laptop. Set the kitchen timer's ringtone.

Saturday morning: run the build. The script you just wrote is one of the four artifacts that survives the day, alongside the live URL, the recording, and the retro.

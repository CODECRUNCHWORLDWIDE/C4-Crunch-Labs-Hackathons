# Exercise 1 — The 60-Second Stand-up

**Goal:** Draft a 60-second stand-up update against an imagined hour-12 checkpoint of a fake hackathon, time yourself reading it aloud, and commit the script plus a written board-update entry. By the end of the exercise, you have rehearsed the four-question format under a real clock.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

Lecture 1 §2 said it: the 60-second team stand-up is the ceremony you will run most. Most learners run their first one at the real event, ad-lib, and produce a 3-minute "yesterday I worked on…" status report that the team tolerates and ignores. The defense is a *written* update, drafted in calm, read aloud against a kitchen timer, before the event starts. Tuesday-you can scope a stand-up; hour-12-you cannot.

---

## What to produce

A file at `week-04-prep/exercise-01-standup.md` (in your `hackathon-template` repo or a new `c4-week-04-prep-<yourhandle>` repo) with:

- The fake-event setup paragraph (one sentence — what the team is building).
- The four-question stand-up update for *you* (the four answers, no filler).
- The written board-update entry, exactly as it would land in `STANDUPS.md`.
- A note on the time you got when you read the update aloud (target: 60 seconds; acceptable: 50–70).

---

## Step-by-step

### 1. Pick a fake event setup

Use one of these three, or invent your own. The point is to have a believable context, not to design a real build.

```
A. A team of 4 building a study-buddy matcher for a 36-hour hackathon.
   At hour 12, you have a working signup form and a stub matcher route.
B. A team of 3 building a campus event finder.
   At hour 12, the deploy URL has a landing page but no live data yet.
C. A team of 5 building an AI recipe-swap tool.
   At hour 12, the MUST screen works on localhost but not on the deploy.
```

Pick one. Write the setup paragraph as one sentence at the top of `exercise-01-standup.md`.

### 2. Draft your four-question update

Copy this block into the file and fill it in *as if you were teammate 2 of 4*. One phrase per line. No filler. Re-read Lecture 1 §2.1.

```
STAND-UP DRAFT — Hour 12, fake event <A/B/C>
Speaker: <your handle>

1. Shipped (last 6h): <one phrase>
2. Next (next 6h):    <one phrase>
3. Blocker:           <one phrase or "none">
```

The blocker line is the most-skipped line by beginner stand-up speakers. If you write "none" for the blocker, ask yourself: is that true, or did I lose courage at the last second? Write the real blocker even if it is "I'm slower at backend than I thought."

### 3. Read it aloud against a timer

Set a phone timer to 60 seconds. Read your draft aloud. Two outcomes:

- **You finish in 45–55 seconds.** Good — add 5–10 seconds of detail to the blocker line.
- **You finish in 70+ seconds.** Cut. Find the filler phrase ("so basically I was…") and delete it. Re-read.

Note the time you got in the file. Be honest. Most first drafts run 75–90 seconds.

### 4. Write the board-update entry

Below the draft, add the board-update entry — the format from Lecture 1 §2.3. Same content as your spoken update, formatted for the shared note:

```
STAND-UP — Hour 12, <DATE>
Timekeeper: <imagined teammate name>

<your handle>:
  - Shipped: <one phrase>
  - Next: <one phrase>
  - Blocker: <one phrase or "none">

Team cut decision: <imagined one-sentence decision>
```

The team-cut line is the team-scale Q4 from Lecture 1 §2.1. Imagine what your team decided. Common cuts: a SHOULD feature dropped, a styling pass deferred, a second seeded example cut.

### 5. Commit

```
git add week-04-prep/exercise-01-standup.md
git commit -m "week 4 exercise 1: 60-second stand-up draft + board entry"
git push
```

---

## Acceptance criteria

- [ ] `week-04-prep/exercise-01-standup.md` exists in a committed repo.
- [ ] A one-sentence fake-event setup is at the top.
- [ ] The four-question draft has one phrase per line, no filler.
- [ ] The "blocker" line is a real blocker, not "none" (unless your imagined teammate genuinely has no blocker — be honest).
- [ ] The time-aloud note is present, with a real number in seconds.
- [ ] The board-update entry follows the format from Lecture 1 §2.3, including the team-cut line.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Read it out loud at the actual pace you would in a stand-up.** Reading silently or at "speed-skim" pace produces a misleading time. Stand-up pace is calm and clear, not rushed.
- **The four lines are not equal length.** Lecture 1 §2.1 gave you ratios: 10 sec shipped, 15 sec next, 10 sec blocker, 25 sec team cut. The team-cut is the longest, because it includes a decision and not just a description.
- **Avoid "I worked on…" phrasing.** That is status-report voice. Use "shipped" with a concrete artifact: "shipped the login form on the deploy URL" not "I worked on auth."
- **Avoid mentioning hours.** "I spent 4 hours on the API" is hours-talk. Stand-up is about what shipped and what's blocked, not about time accounting.

---

## What to do if you cannot keep it to 60 seconds

You have three options:

1. **Cut filler.** The single most common cause of an over-long stand-up is filler ("so basically," "what I was trying to do was," "I'll get back to that"). Delete it. Speak in phrases.
2. **Cut the "shipped" line to one phrase.** Beginners over-explain what they shipped. The board has the details. The stand-up phrase is the headline only.
3. **Move the explanation to the post-stand-up sidebar.** If your update is over-long because you have a real coordination problem to discuss, that is a sidebar (Lecture 1 §7.3), not a stand-up. Move it.

---

## What is next

Move on to [Exercise 2 — Planning-poker round](./exercise-02-pointing-poker.md), where you point a 10-item backlog with the 1-2-3-5 scale in 10 minutes.

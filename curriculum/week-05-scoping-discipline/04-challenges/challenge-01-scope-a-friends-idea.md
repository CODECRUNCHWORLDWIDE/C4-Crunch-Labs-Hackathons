# Challenge 1 — Scope a Friend's Idea

**Time estimate:** 30 minutes of paired drill + 15 minutes of written debrief. Total ~45 minutes.

> This is the Week 5 challenge in C4: a paired drill where you run the 20-minute MoSCoW pass and the cut-list pre-write on a *non-C4 friend's* real idea. The point is to feel the muscle of scoping when the idea is not yours — when you have to ask clarifying questions, when you cannot fill MUST with your own preferences, when the WON'T list belongs to someone else. Five minutes of out-loud scoping with a real partner produces more behavior change than 30 minutes of solo rehearsal.

---

## Problem statement

You and one non-C4 friend (or sibling, or club-mate, or any person with a half-formed project idea they are willing to share) do a 30-minute paired session in two phases: the **MoSCoW pass** (20 minutes) and the **cut-list pre-write** (10 minutes). You finish with a one-page scoped worksheet *for their idea*, and a 15-minute written debrief.

The non-C4 partner constraint matters. The challenge teaches scoping muscle when the *content* of the idea is unfamiliar. Working with a C4 partner on a shared fake prompt re-rehearses what Exercise 2 already covered.

---

## Why a non-C4 partner

Exercise 2 was the writing. This challenge is the reps with someone whose idea you do not own.

> **C4 voice:** the worksheet reads easy in a markdown file on a fake prompt. It is harder when a real person has a real idea and looks at you while you ask "is that a MUST?" The drill rehearses the *with-a-real-person* part.

Your partner does *not* need to know MoSCoW. Your job, in fact, is to teach them the framework as you apply it together. The teaching is half the muscle.

The partner's idea can be anything that fits "could be built in 36 hours by a team of 4":

- A startup idea they have been kicking around.
- A class project they need to scope.
- A side-project they keep restarting.
- A club initiative ("our team wants to build X for the next showcase").
- A community-organization tool ("our food pantry needs a sign-up sheet that").

It does *not* need to be a hackathon idea. It does need to be a real idea the partner cares about.

---

## Acceptance criteria

- [ ] You and your partner spend 20 minutes on the MoSCoW pass and 10 minutes on the cut-list pre-write.
- [ ] The output is a one-page scoped worksheet for *their* idea, with all five sections from this week's mini-project (prompt, MoSCoW board, points budget, cut-list, demo-ability checklist).
- [ ] You commit the worksheet to your repo as `week-05-prep/challenge-01-friend-worksheet.md` (with the partner's permission; redact the idea if needed).
- [ ] You write a 15-minute debrief at `week-05-prep/challenge-01-debrief.md` covering one moment your MoSCoW worked and one moment it broke.
- [ ] You leave the partner with a printed (or DM'd) copy of the worksheet — the artifact is theirs, even if your debrief is yours.

---

## How to run the 30 minutes

```
┌────────────────────────────────────────────────────────────┐
│  THE 30-MINUTE FRIEND-IDEA SCOPING DRILL                   │
│                                                            │
│  Pre-drill (5 min, async): the partner tells you their     │
│   idea in 3-5 sentences. You ask one clarifying question.  │
│                                                            │
│  Min  0 — 1   Setup. You explain MoSCoW in 60 seconds.     │
│  Min  1 — 4   Brainstorm: together, list 8-12 candidate    │
│               features. No filtering. You write; they talk.│
│  Min  4 —11   Sort: place each candidate into MUST/SHOULD/ │
│               COULD/WON'T. Ask "is this required for the   │
│               demo or for the launch?" for each.           │
│  Min 11 —15   Force the cuts. MUST > 3? Cut. WON'T < 4?    │
│               Add. Read the result aloud to the partner.   │
│  Min 15 —20   Reasons. Write a one-sentence reason on each │
│               WON'T item. Partner approves each reason.    │
│  Min 20 —25   Cut-list: pre-write the hour 2 and hour 12   │
│               cuts as paragraphs. Skip hour 24 if pressed. │
│  Min 25 —30   Read the final worksheet aloud to the partner│
│               in 60 seconds. They approve or amend.        │
│                                                            │
│  Tools: voice or video call. Shared screen or paper.       │
└────────────────────────────────────────────────────────────┘
```

The "you write, they talk" rule is the key. Your partner is the domain expert; you are the framework expert. Their words go in MUST/SHOULD; your discipline forces the cuts.

### The 60-second MoSCoW explainer

Memorize this script for minute 0:

> "MoSCoW is a four-column scoping grid. MUST is what ships or the demo dies — three items max. SHOULD is what ships if MUST is clean. COULD is nice-to-have. WON'T is what we explicitly do not build — and the most-important column. We will spend 20 minutes filling these four columns, then 10 minutes writing cuts for when scope creep hits. Ready?"

That is 60 seconds. Do not over-explain. Apply the framework; the explanation deepens as you work.

### Asking the right clarifying question

Before the drill (minute 0), ask your partner one question to lock the prompt sentence:

> "If a stranger opened your built thing in a browser, what is the one action you want them to be able to do?"

That one verb is the *MUST verb*. Write it down. Every MoSCoW item is graded against that verb. If a candidate feature does not serve the verb, it is not a MUST.

### Forcing the cuts at minute 11–15

This is the hardest part of the drill. Your partner will want a MUST list of 6. Your job is to force MUST to 3. Three concrete moves:

1. **Combine.** "Sign-up + first post" combines to "first-post flow." That is one MUST.
2. **Demote.** "User profile pages" is almost always SHOULD or COULD in a 36-hour build. Demote it.
3. **Cite the verb.** "Does this feature serve the verb we wrote down at minute 0?" If no, it is not a MUST. Move it.

The partner will push back. Run the three-sentence "no" script from Week 4 Lecture 2 §3.2: acknowledge ("good thought"), refuse with a reason ("we have only 36 hours and the verb is the demo"), offer a cheaper alternative ("what if user profiles ship as a static placeholder in the README?").

---

## The midpoint check (minute 11)

At minute 11, pause for 30 seconds and check:

- Is the MUST list still > 3 items? Force-cut to 3 in the next 4 minutes.
- Is the WON'T list at 0 or 1 items? Surface 3+ refusals; ask the partner what they *will not* build, not just what they *will*.
- Does the prompt sentence still match the build? If the partner has drifted, re-read it.

The 30-second check is the difference between a 22-minute drill that drifts and a 30-minute drill that ships.

---

## Pitfalls (forewarned)

The drill fails for predictable reasons. Plan around them.

### 1. The partner falls in love with MUST

Your partner's pet feature is in MUST. Their second pet feature is in MUST. Their third pet feature is in MUST. The MUST list has 6 items and the partner is energized. Cut, kindly, citing the 36-hour clock. The partner will be glad later that you did.

### 2. You become the domain expert

You start telling the partner what their idea *should* be. Stop. You are the framework expert. The idea is theirs. If the partner says "X is a MUST," your role is to test whether X serves the verb, not to disagree with the idea itself.

### 3. The cuts get vague

The partner agrees "we cut something" but cannot name *what*. Force the name. "If your hour-2 cut fires, which specific SHOULD item gets dropped?" If they cannot name it, the cut-list is fiction. Force the name even if it is uncomfortable.

### 4. The 20-minute cap is ignored

The drill goes 35 minutes, then 45 minutes, then the partner has to leave. The cap is the discipline. At minute 20, stop the MoSCoW pass — even if it feels incomplete. The incomplete pass is real data; the over-long pass is theatre.

### 5. The debrief is skipped

"We did the drill, we have the worksheet, we're done." No. The debrief is where the *learning* is captured. The drill is the data; the debrief is the lesson.

---

## The written debrief

After the drill, write `week-05-prep/challenge-01-debrief.md` with three sections:

```markdown
# Friend-Idea Scoping Drill — Debrief

Partner: <handle or pseudonym, with permission>
Date: <YYYY-MM-DD>
Partner's idea (one sentence, redacted if needed): <text>

## One moment my MoSCoW worked
- During <minute N> on the candidate "<one feature>", I <what
  happened — combined two MUSTs / forced a cut / named a WON'T
  reason>. The partner's response: "<their reaction in their words>".

## One moment my MoSCoW broke
- During <minute N> on "<one feature>", I <what happened — let MUST
  bloat / accepted a vague cut / skipped the WON'T reason>. Behavior
  change for next event: <one sentence with a when and a what>.

## One pattern I would adopt for my own worksheet
- <One sentence — usually a specific cut-list pattern or WON'T-list
  reason format that worked here and would translate to my own
  hackathon worksheet template.>
```

Total: 150–250 words. Commit the file. Push.

---

## Rubric (for self-grading)

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| The 20-min MoSCoW pass happened against a real clock | 25% | A timer ran; the pass ended at 20 minutes, even if incomplete |
| MUST was forced to 3 items by minute 15 | 20% | The cut happened; the partner agreed; the worksheet shows MUST = 3 |
| Every WON'T item has a one-sentence reason | 15% | No bare WON'T items; reasons read like next-event memos |
| Cut-list paragraphs for hour 2 and hour 12 were written | 15% | Two pre-written paragraphs, each with a named cut |
| Written debrief committed | 15% | The three-section file, 150–250 words, in the prep repo |
| Voice was team-room and blameless throughout | 10% | Even on a fumbled pass, the debrief stayed scope-disciplined |

---

## Stretch (only if you both finish under 25 minutes)

- **Add the hour-24 cut.** The compressed schedule above skipped hour 24 to fit in 30 minutes. If you finish at minute 25, spend the last 5 minutes on the hour-24 cut paragraph. Same format as Exercise 3.
- **Run the demo-ability checklist on the partner's *imagined* MUST items.** Walk through Lecture 2 §3.1's five questions for each MUST. Note which question is hardest to imagine answering "yes" to. That is the gap to design around.
- **Trade roles.** If your partner has the energy, swap: you bring an idea, they run MoSCoW on it. Most non-C4 partners will *not* have the framework yet — but with you having just walked them through it once, they often can run a recognizable version. Their version teaches you what the framework feels like from the other side.

---

## Submission

When done:

1. Commit `week-05-prep/challenge-01-friend-worksheet.md` and `week-05-prep/challenge-01-debrief.md` to your repo. With permission. Redact if needed.
2. Send the worksheet to your partner. They keep the artifact.
3. Post in the cohort channel: "Did the friend-idea scoping drill with [a non-C4 partner]. One pattern I'm adopting: <one sentence>." Read one cohort-mate's debrief and leave one specific comment on a *moment they named*, not a generic compliment.

You are now meaningfully readier for [Week 6 — Pitch Craft](../../week-06/), where the clean MUST list you have practiced extracting from a real partner's idea becomes the spine of a three-minute demo script. The reps you just ran are the reason that script will not feel theoretical.

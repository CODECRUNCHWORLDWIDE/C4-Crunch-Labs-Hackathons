# Mini-Project — The Mock Pitch and Mock Q&A

> **Time:** ~5 hours over Saturday (2.5h) and Sunday (1.5h + a 1h reflection block).
> **When in the week:** Saturday afternoon for the mock pitch and mock Q&A; Sunday for the rubric self-score, the engineer-versus-investor reflection, and the follow-up issue.
> **Deliverable:** a committed `JUDGE-ROOM-LOG.md` in the same repo as `DAY-1-LOG.md`, `DAY-2-LOG.md`, and the Week 8 `SUBMISSION.md`. The log contains four entries: the rubric self-score (team-consensus version), the mock-pitch take notes, the mock Q&A transcript, and the engineer-versus-investor reflection paragraph.
> **Prerequisite:** Week 8 mini-project complete (`DAY-2-LOG.md` committed, demo video URL live); all three Week-9 lectures read; all three Week-9 exercises complete; quiz at 9/10 or better.

## What this mini-project is

You will rehearse the *judge-room slot* with your team's own Week 8 submission as the artefact and a teammate-or-peer as the judge proxy. The rehearsal has four moving parts:

- **The mock pitch.** Two takes minimum, against the live deploy URL, timed against the 30-90-45-15 arc, *unrecorded*.
- **The mock Q&A.** Six questions minimum: the five archetypes from Lecture 3 §3.1 plus one surprise question from the judge proxy. Each answer capped at 30 seconds.
- **The rubric self-score.** Each teammate's solo self-score from Exercise 1 is the input; the team consensus score is the output.
- **The engineer-versus-investor reflection.** A one-paragraph written reflection on which mindset the team's pitch actually leans into and what changes if the team gets the other kind of judge.

The rehearsal is bounded — about 5 hours of wall-clock work over a weekend, not a continuous 24-hour event. The Week-8 dry-run was the *load test of the build*; this week's mini-project is the *load test of the delivery*.

## What this mini-project is not

This is not a real judging event. The judge proxy is a teammate or peer, not a real judge. No prize is at stake; no actual score is being recorded against the team. The score the team produces is for *calibration*, not for ranking.

The mini-project is also not a re-recording of the Week 8 demo video. The mock pitch is *live and unrecorded*; the recording is the Week 6 and Week 8 skill. The live pitch is what this week rehearses.

## The mock-pitch session structure

```
┌────────────────────────────────────────────────────────────────────┐
│  THE MOCK-PITCH SESSION — SATURDAY (2.5h)                           │
│                                                                    │
│  0:00 — 0:15   Pre-session setup                                    │
│  0:15 — 0:45   Script-lock protocol (Lecture 2 §5.1)               │
│  0:45 — 1:15   Mock pitch — take 1                                  │
│                  - 3-minute pitch (camera off; judge camera on)    │
│                  - 5-minute Q&A                                     │
│                  - 5-minute take-1 debrief                          │
│  1:15 — 1:30   Break                                                │
│  1:30 — 2:00   Mock pitch — take 2                                  │
│                  - 3-minute pitch (with the take-1 adjustments)    │
│                  - 5-minute Q&A (different judge questions)        │
│                  - 5-minute take-2 debrief                          │
│  2:00 — 2:30   Final debrief and log entry                          │
└────────────────────────────────────────────────────────────────────┘
```

Two takes. The break between is non-negotiable; it lets the team's body reset and lets the judge proxy re-read the rubric.

### The pre-session setup (0:00-0:15)

The team gathers (in person or on a single video call). The judge proxy joins (a different teammate, a peer from another C4 cohort team, a friend who has not seen the build).

- The team confirms the live deploy URL is up.
- The team confirms the 3-minute timer is in shot.
- The team confirms the cameras-off configuration (team camera off; judge proxy camera on).
- The judge proxy reads the rubric aloud once.

### The script-lock protocol (0:15-0:45)

The team runs the four-read protocol from Lecture 2 §5.1:

```
0:15 — 0:20   Read 1: notes-out, looking at the script
0:20 — 0:23   Read 2: looking at the screen (live deploy URL)
0:23 — 0:26   Read 3: looking at a teammate (eye contact)
0:26 — 0:29   Read 4: no notes, against the 3-minute timer
0:29 — 0:30   Lock decision: keep, tweak, or rewrite
```

If the team's Week 8 demo script needs significant rewriting, the team may run the protocol twice. Most teams' Week 8 scripts need *tweaking* (one beat re-paced, one sentence cut, one transition smoothed) rather than rewriting.

The locked script is what goes into the mock pitch. Edits *after* the lock are not allowed; the team commits to the locked version.

### Mock pitch — take 1 (0:45-1:15)

- **The 3-minute pitch.** The team's primary speaker delivers the locked script against the live deploy URL. Camera off (team side); camera on (judge proxy side). Timer in shot. The judge proxy does *not* take notes during the pitch (they listen and watch).

- **The 5-minute Q&A.** The judge proxy asks 6 questions — the five archetypes (in any order) plus one surprise question. The team answers each in <30 seconds. The judge proxy is timing the answers using a phone timer.

- **The 5-minute take-1 debrief.** The team and the judge proxy discuss what landed, what stumbled, what to adjust for take 2. The Comms Lead is the scribe; the notes go into the `JUDGE-ROOM-LOG.md`.

### The break (1:15-1:30)

Fifteen minutes. The team walks, drinks water, does not discuss the pitch. The break is the *calibration window* — coming back fresh is part of the load test, not a luxury.

### Mock pitch — take 2 (1:30-2:00)

Same structure as take 1, but:
- The team adjusts the script based on the take-1 debrief.
- The judge proxy asks *different* questions in the Q&A (the judge proxy prepares a second set of 6 questions during the break).
- The team is now under fewer notes — the script is more practiced, the Q&A archetypes are familiar.

### The final debrief (2:00-2:30)

Thirty minutes. The team produces the take-by-take comparison:

| Beat | Take 1 | Take 2 | Choice for the "final" version |
|------|--------|--------|-------------------------------|
| Problem | ... | ... | Take 1 / Take 2 |
| Demo | ... | ... | Take 1 / Take 2 |
| Tech | ... | ... | Take 1 / Take 2 |
| Ask | ... | ... | Take 1 / Take 2 |

The "final" choice per beat is the team's commitment. The mini-project does not require a third take; the final is the cherry-pick across takes 1 and 2.

## The Sunday work — self-score and reflection

```
┌────────────────────────────────────────────────────────────────────┐
│  SUNDAY — 2.5h                                                      │
│                                                                    │
│  0:00 — 1:00   Team-consensus rubric self-score                     │
│  1:00 — 1:30   Engineer-versus-investor reflection                  │
│  1:30 — 2:00   Final log entry + follow-up issue draft              │
│  2:00 — 2:30   Stretch goal or rest                                 │
└────────────────────────────────────────────────────────────────────┘
```

### The team-consensus rubric self-score (0:00-1:00)

Each teammate's Exercise 1 solo self-score is the input. The team comes together to produce a *consensus* score per dimension. The consensus is not the average; it is the *negotiated* score with one-line evidence the whole team endorses.

The discussion follows the pattern from Lecture 1 §4.2 (the "all 5s" anti-pattern): if every teammate scored every dimension at 4 or 5, the team compressed the scale. Push back. The honest consensus score, signed by all teammates, is the deliverable.

### The engineer-versus-investor reflection (1:00-1:30)

A one-paragraph (4-6 sentences) reflection answering:

```
Which judging mindset does the team's pitch — as it stands after
take 2 — actually lean into? The engineer-mindset (technical-decision
foregrounded; user framing supportive) or the investor-mindset (user
pain foregrounded; technical detail supportive)? What would change
in the pitch if the team learned the morning of the event that the
panel is *all* the opposite mindset?
```

The reflection is the team's *meta-awareness* of the pitch's tilt. The reflection becomes the prep note for the morning of a real event: "if we get a panel of all engineers, do X; if we get a panel of all investors, do Y."

### The final log entry + follow-up issue draft (1:30-2:00)

The `JUDGE-ROOM-LOG.md` final pass:
- The rubric self-score with consensus.
- The mock-pitch take-1 and take-2 notes.
- The mock Q&A transcript (the questions asked and the team's answers, paraphrased).
- The engineer-versus-investor reflection paragraph.
- The follow-up issue (one concrete change the team commits to for the next real event).

The follow-up issue is filed as a GitHub issue in the team's repo, labelled `judge-room-followup`, with a 2-sentence scope and a 3-item acceptance checklist. Same mechanism as Week 8's retro follow-up issue.

## The `JUDGE-ROOM-LOG.md` template

```markdown
# Judge-Room Log — [Team name]

(Companion to DAY-1-LOG.md and DAY-2-LOG.md. Same team; same repo;
 same prompt; same submission package.)

## Rubric self-score (team consensus)

| Dimension | Score (1-5) | Evidence (one line) |
|-----------|-------------|---------------------|
| Technical Complexity | | |
| Design and UX | | |
| Originality | | |
| Polish | | |
| Presentation | | |

**Weighted total (HackMIT-style weights):** [N.NN] / 5.00

**Honest gap (one paragraph):**
[The lowest-scored dimension; the reason it is low; the single 4-hour
change that would raise it by 1 point.]

---

## Mock pitch — take 1

**Date and time:** [YYYY-MM-DD HH:MM UTC]
**Judge proxy:** [name, role]
**Format:** [video call / in-person]
**Live URL used:** [URL]

**Pitch duration:** [N:NN] (target 3:00 ± 0:15)
**Beat timing actual:**
- Problem: [N:NN]
- Demo: [N:NN]
- Tech: [N:NN]
- Ask: [N:NN]

**What landed:** [3 bullets]
**What stumbled:** [3 bullets]
**Cues read during the pitch:** [list of cues with second-mark and the
                                  recovery move deployed]

**Q&A — 6 questions:**

Q1 (archetype: user): [question]
A1 (time: N seconds): [paraphrased answer]

Q2 (archetype: closest competitor): [question]
A2 (time: N seconds): [paraphrased answer]

Q3 (archetype: technical): [question]
A3 (time: N seconds): [paraphrased answer]

Q4 (archetype: follow-through): [question]
A4 (time: N seconds): [paraphrased answer]

Q5 (archetype: challenge): [question]
A5 (time: N seconds): [paraphrased answer]

Q6 (surprise): [question]
A6 (time: N seconds): [paraphrased answer + note on whether bridge
                       or "I don't know" was deployed]

**Take-1 debrief — 3 sentences:**
[What to adjust for take 2.]

---

## Mock pitch — take 2

[Same template as take 1; different Q&A questions; the team's
 adjustments visible.]

---

## Take-by-take comparison

| Beat | Take 1 timing | Take 2 timing | Final choice |
|------|---------------|---------------|--------------|
| Problem | [N:NN] | [N:NN] | Take 1 / Take 2 |
| Demo | [N:NN] | [N:NN] | Take 1 / Take 2 |
| Tech | [N:NN] | [N:NN] | Take 1 / Take 2 |
| Ask | [N:NN] | [N:NN] | Take 1 / Take 2 |

**Final version notes:** [one sentence describing the cherry-picked
                          version the team would deliver at a real event]

---

## Engineer-versus-investor reflection

[4-6 sentence paragraph. Which mindset does the pitch lean into?
 What changes if the panel is the other mindset?]

---

## Follow-up issue draft

**Title:** [one-line title]
**Scope (2 sentences):** [what change, why]
**Acceptance checklist:**
- [ ] [item 1]
- [ ] [item 2]
- [ ] [item 3]

**Filed in the repo at:** [issue URL once filed]

---

*Judge-room log closes here. The follow-up issue is filed in the repo
within 24 hours of the Sunday work.*
```

## The minimum entries

The `JUDGE-ROOM-LOG.md` must include, at minimum:

- 1 team-consensus rubric self-score with 5 dimensions and 5 evidence cites.
- 1 take-1 entry with timing, what-landed, what-stumbled, and the 6-question Q&A.
- 1 take-2 entry with the same fields.
- 1 take-by-take comparison table.
- 1 engineer-versus-investor reflection paragraph (4-6 sentences).
- 1 follow-up issue draft with title, scope, and 3-item acceptance checklist.

Total minimum entries: 6. Most teams' logs will have additional notes (specific quotes from the judge proxy, the team's running list of "things to read before the next event," etc.).

## The deliverable

By Sunday evening:

1. **`JUDGE-ROOM-LOG.md`** committed to the repo. Minimum 6 entries; minimum 250 lines of markdown.
2. **One follow-up issue** filed in the repo, labelled `judge-room-followup`, with the title + 2-sentence scope + 3-item acceptance checklist. Filed within 24 hours of the Sunday work (i.e., by Monday end-of-day).
3. **The team's locked pitch script** committed to the repo at `pitch/PITCH-SCRIPT.md` (or wherever the team's pitch artefacts live). This is the "final" version from the take-1-versus-take-2 comparison.

## The acceptance criteria

The mini-project is accepted if all three deliverables are committed/filed and at least 9 of the following 12 quality criteria are satisfied. The optional Challenge 1 lifts the bar from 9/12 to 12/12.

```
1. The team-consensus rubric self-score uses the 1-5 range (not all 3s
   and 4s); at least one dimension is at 2 or below OR the team
   explicitly justifies in the Honest Gap paragraph why every dimension
   genuinely scored 3+.
2. Every score in the self-score has a one-line evidence cite.
3. The mock pitch take 1 was delivered against the live deploy URL
   (not localhost; not the recorded demo video).
4. The mock pitch take 1 was timed; the actual duration is within
   3:00 ± 0:15.
5. The mock pitch take 2 was delivered after the 15-minute break and
   incorporates at least 2 adjustments from the take-1 debrief.
6. The mock Q&A in take 1 covered all five archetypes + one surprise
   question (6 questions total).
7. The mock Q&A in take 2 covered six *different* questions.
8. At least one bridge sentence or "I don't know" was used in the Q&A
   (and the use is noted in the log).
9. The take-by-take comparison names a final choice per beat.
10. The engineer-versus-investor reflection paragraph names the pitch's
    tilt and the alternative-mindset adjustment.
11. The follow-up issue is filed with a concrete title, a 2-sentence
    scope, and a 3-item acceptance checklist.
12. The pitch script is committed to the repo as a separate artefact.
```

## What the mock pitch measures

The mock pitch does *not* measure whether the team would have won the real event, or whether the pitch is polished, or whether the build is impressive. It measures:

- **Whether the team can hold the 3-minute arc under live observation.** Take 1 surfaces the gap; take 2 measures the closing of the gap.
- **Whether the team can deploy the Q&A archetypes from memory.** The 30-second cap is the discipline; the bridge and "I don't know" are the safety nets.
- **Whether the team can read the room.** The cues the team noticed during the pitch and the recovery moves they deployed are the measurement.
- **Whether the team is honest about the pitch's tilt.** The engineer-versus-investor reflection is the meta-skill; the team that says "we lean engineer; we would adjust by X for an all-investor panel" has prepared for both rooms.

## Facilitator notes (for the C4 cohort coordinator)

The cohort coordinator reads this section; learners can skip it.

### What to watch for during a team's mock pitch

The facilitator's job during the mock pitch is *light-touch observation*, not coaching (Lecture 3 §5.5). Three things to watch:

- **The take-1 timing.** If take 1 runs 3:30 or longer, the script-lock protocol did not work; the team needs to re-run the protocol before take 2. Note this in DM, not in the team's call: "your take-1 ran 3:32; consider another script-lock pass before take 2."
- **The Q&A archetype coverage.** If take 1's Q&A covered only 3-4 archetypes, the judge proxy is not pushing hard enough. Coach the judge proxy (not the team) in DM: "the team needs to hear all 5 archetypes; can you cover [missing archetype] in take 2's Q&A?"
- **The engineer-versus-investor reflection's honesty.** A reflection that says "we are balanced for both mindsets" is usually wrong; most teams genuinely lean one way. Ask the Comms Lead, in DM, "your reflection says balanced; which mindset's questions did the team actually answer most cleanly in the Q&A?"

### What not to do

- Do not enter the team's mock pitch call uninvited. The team's rehearsal dynamics are part of what the mini-project measures.
- Do not provide sample answers for the Q&A. The team must own the answers.
- Do not file the follow-up issue for the team.

### Sample facilitator Slack scripts

A cohort coordinator running a multi-team Week-9 weekend uses these scripts.

**Pre-weekend notice (Friday morning):**

```
:wave: Week 9 mini-project — the mock pitch + mock Q&A — is this
weekend.

Per the Week-8 close, your team's submission, demo video, and
DAY-2-LOG.md are committed. The mock pitch rehearses live
delivery against the same submission.

What to have ready by Friday end-of-day:
  - All three Week-9 lectures read.
  - All three Week-9 exercises complete (the SOLUTIONS in
    the exercises folder are available for self-check).
  - The quiz at 9/10 or better.
  - A judge proxy lined up. A peer from another C4 team is the
    strongest signal; a friend who has not seen the build is
    second-best.
  - The live deploy URL up. If the URL has degraded since the
    Week-8 submission, the first hour of Saturday is bring it
    back online.

I am on-call Saturday 12pm-8pm UTC and Sunday 10am-6pm UTC. I will
not enter team calls; ping me in DM with blockers.

Good luck.
```

**Saturday afternoon check-in (during the mock-pitch window):**

```
:bell: mock-pitch check-in.

By now most teams should be in or just past their take-1 debrief.
A take-1 that ran long or had a Q&A gap is normal — that's what
take 2 is for.

Reminder: take 2 is *not* take-1-but-better. Take 2 is take-1's
debrief applied to a fresh delivery. The 15-minute break between
takes is part of the rehearsal, not a luxury.

Ping me in DM if your team's judge proxy backed out; I can match
you with a peer from another cohort team for take 2.
```

**Sunday afternoon check-in (during the reflection block):**

```
:bell: Sunday reflection check-in.

By now most teams should be in the self-score consensus or the
engineer-versus-investor reflection. The most common cohort
mistake is *over-grading* the self-score; if your team is at
22/25 or higher, please re-read Lecture 1 §4.2 and re-check.

The follow-up issue is due by Monday end-of-day. Title, 2-sentence
scope, 3-item acceptance checklist; labelled judge-room-followup.

Once the issue is filed, you are ready for Week 10.
```

**Post-mini-project follow-up (Monday morning):**

```
:wave: Week 9 mini-projects are committed. The follow-up issues
are due in the repos by Monday end-of-day.

I will read each JUDGE-ROOM-LOG.md this week and post one comment
per log in the repo's issue tracker. The comment is feedback, not
grading; the rehearsal is graded by the team's own measurement,
not by me.

Week 10 picks up from here — taking the *finished* hackathon
artefact and treating it as a *starting point* for ongoing
work (post-event PR pass, issue triage, README-for-the-internet
edit, open-source contribution rhythm).

Good work this weekend.
```

## Why this mini-project

Weeks 7 and 8 taught the team to *ship*. Week 9 teaches the team to *be judged*. The two are different muscles; the rehearsal puts the team in the judge-room seat at low stakes so the muscle is warm at high stakes.

A team that finishes the Week 9 mini-project with a clean log, an honest self-score, and a filed follow-up issue has the *infrastructure of a judging slot*. Real events use the same protocols, at the same rhythm, with the same templates. The mock is the bench; the real event is the band; the discipline is the same in both rooms.

> **C4 voice:** the rubric is the bench. The pitch is the run. The score is the measurement. The mock pitch loaded the test; the self-score named the gap; the reflection named the tilt; the follow-up issue carried the lesson into Week 10. Four artefacts; one team; five hours of practice. The next pitch is the real one.

# Challenge 1 — Be a Judge for Another Team's Submission

> **Time:** ~1 hour.
> **When:** Sunday evening or Monday morning of Week 10.
> **Deliverable:** a 12-item scorecard plus a one-positive-one-growth feedback note, appended to your `JUDGE-ROOM-LOG.md`.
> **Prerequisite:** mini-project complete; `JUDGE-ROOM-LOG.md` committed; the other team's consent to be scored.

## What this challenge is

You will play the *other* role from the mini-project. Rather than being the team pitched to a judge, you are the judge scoring another team's submission. The submission can be:

- **Another C4 cohort team's Week 8 submission.** Best signal; the other team is rehearsing the same protocols.
- **A peer's solo submission from outside C4.** Acceptable; the team is unaware of the rubric.
- **A public Devpost submission with a published demo video.** Acceptable as a last resort; the team will not see your feedback.

The challenge mirrors Lecture 3 §5 (the be-a-judge sidebar). You will apply the rubric pre-read, the table-walk-style 4-minute slot (replayed against the other team's recorded video), the scoring discipline, and the post-event feedback note.

## Why this challenge matters

The judge's seat is the *next* seat. Some C4 grads will be invited to judge later cohort dry-runs in Weeks 10-14. The challenge is the *first time* in that seat at low stakes — the judged team consents, the score is feedback rather than a public ranking, the rubric is the C4 default (no surprise event-specific overlay).

The dirty secret of judging: most judges are first-time judges at any given event. The teams scoring most consistently across a day are the teams who *practised* before the event. The challenge is the practice.

## The 12-item scorecard

The scorecard is the *operational deliverable* of the challenge. The 12 items are grouped by phase: pre-read (3), per-slot (5), post-slot (4).

### Pre-read (3 items)

```
1. Rubric pre-read completed.
   Evidence: a one-line note in your log stating "rubric pre-read at
   [timestamp]; the five dimensions were [list]." The pre-read is
   the calibration anchor (Lecture 3 §5.2).

2. The other team's submission artefacts located.
   Evidence: the public repo URL, the live deploy URL (or note if
   missing), and the demo video URL all accessible.

3. The scoring window allocated.
   Evidence: a 4-7 minute slot blocked on your calendar; the slot is
   the simulated table-walk or panel slot.
```

### Per-slot (5 items)

```
4. The pitch was watched in full.
   Evidence: timestamp and duration. The judging does not score from
   half-watched material.

5. Each rubric dimension was scored within 60 seconds of the slot end.
   Evidence: the scores written within 60 seconds of finishing the
   pitch viewing (Lecture 3 §5.3 discipline).

6. Every score has a one-line evidence cite.
   Evidence: 5 scores × 1 line each = 5 evidence lines (Lecture 1 §4.3).

7. The 1-5 scale was used across the range.
   Evidence: not every score is a 3 or a 4. At least one score is at
   2 or below, OR an explicit note in the log explaining why every
   dimension scored 3+ for this submission (rare; usually indicates
   over-grading).

8. The score is anchored to the moment, not retroactively rescored.
   Evidence: no later edits to the scores (commit history clean).
```

### Post-slot (4 items)

```
9. A one-positive-one-growth feedback note was written for the team.
   Evidence: a 4-sentence note per Lecture 3 §5.8 format. One specific
   strength, one specific growth area, one specific follow-on the
   judge would be curious to see, signature.

10. The feedback note was delivered (if the team consented).
    Evidence: a DM, an email, or a comment in the team's repo. If
    the team did not consent (you scored a public Devpost submission
    without their knowledge), document the decision: "no feedback
    delivered — public submission, team unaware."

11. The "do not coach" rule was respected.
    Evidence: the feedback note does not tell the team what they
    "should have built" or "should have done in the pitch." It
    names what they did and what to watch next time.

12. The scoring distribution was reviewed.
    Evidence: a one-line note: "average of my 5 scores: [N.N]; the
    range was [low]-[high]; if I scored a second team today I would
    [calibration note]."
```

## The scorecard format

Append this block to your `JUDGE-ROOM-LOG.md`:

```markdown
## Challenge 1 — Be-a-Judge Scorecard

**Submission scored:** [team name / repo URL / Devpost URL]
**Consent:** [yes / no (public)]
**Slot duration:** [HH:MM-HH:MM]

### Pre-read (3 items)
- [ ] 1. Rubric pre-read completed at [timestamp].
- [ ] 2. Submission artefacts located.
- [ ] 3. Scoring window allocated.

### Per-slot (5 items)
- [ ] 4. Pitch watched in full from [timestamp].
- [ ] 5. Each dimension scored within 60 seconds of slot end.
- [ ] 6. Every score has a one-line evidence cite.
- [ ] 7. Range used (not all 3s and 4s).
- [ ] 8. Score anchored to the moment, no retroactive rescoring.

### Post-slot (4 items)
- [ ] 9. One-positive-one-growth feedback note written.
- [ ] 10. Note delivered (if consent) or documented (if not).
- [ ] 11. Do-not-coach rule respected.
- [ ] 12. Scoring distribution reviewed.

### Scores

| Dimension | Score (1-5) | Evidence (one line) |
|-----------|-------------|---------------------|
| Technical Complexity | | |
| Design and UX | | |
| Originality | | |
| Polish | | |
| Presentation | | |

**Weighted total (if using HackMIT-style weights):** [N.NN] / 5.00

### Feedback note (delivered or documented)

> "[Team name] — your build was strong on [dimension] because [specific
> reason]. The growth area I noticed was [specific dimension]. If you
> build again, I'd be curious to see [specific follow-on]. — [your name]"

### Calibration note

The average of my 5 scores was [N.N]; the range was [low]-[high]. If I
scored a second team today, I would [calibration note: e.g., "score the
technical-complexity dimension more leniently after seeing how high the
event-level median actually is", or "score originality more strictly
because I over-rewarded the narrow-target framing"].
```

## Acceptance criteria

The challenge is accepted if at least 10 of the 12 items are completed honestly. The two items most likely to slip:

- **Item 7 (range used)** — the first-time-judge tendency is to score every dimension at 3-4. Push yourself to score at the 2 or 5 anchor when honestly warranted.
- **Item 10 (note delivered)** — coordinating with the other team takes wall-clock time. If the team consents but does not respond to your DM within 48 hours, document the attempt: "feedback drafted; team contacted at [timestamp]; awaiting response."

The challenge is not graded numerically. Honesty in the scorecard and the calibration note is the bar.

## What this challenge teaches that the mini-project does not

The mini-project rehearses the team's *delivery*. The challenge rehearses the *grading lens* — what a judge sees, how a judge writes evidence, how a judge calibrates across teams.

After the challenge, the team's *own* pitch reads differently. You see the rubric data points you were missing. You see the originality angle that does not land in 30 seconds. You see the technical-complexity claim that does not have evidence. The grading lens is the missing half of the pitching skill.

## Coordinating with the other team

If you are scoring another C4 cohort team's submission, the coordination is:

```
1. DM the team's Comms Lead with a one-paragraph ask:
   "I'm doing Challenge 1 of Week 9 — scoring another team's
    submission. Would you consent to me scoring yours? I'll send
    you a 4-sentence feedback note and the scorecard at the end.
    No comparison or ranking; just feedback."

2. If they consent, set a slot.
3. If they decline (totally fair), find another team or use a
   public Devpost submission.
4. Score; write the feedback note; deliver.

5. Offer to be scored by them in return if they are doing the
   challenge too. Trading scores is a stronger learning loop than
   one-way scoring.
```

The exchange is the *peer-grading habit* that scales beyond the cohort — it is the same habit that runs C4-cohort Week 8 retro reviews and the Week 10 carry-out PR-pass on each other's repos. Build the habit now; it pays compound interest.

## What you commit

By Monday end-of-day of Week 10, the appended scorecard is in `JUDGE-ROOM-LOG.md`. If the feedback note was delivered to a real team, the team's reply (if any) is also logged. If the note was on a public submission with no delivery, the un-delivered note is in the log with the rationale.

The challenge is one hour. The carry-out is one feedback note. The rehearsal is the next seat.

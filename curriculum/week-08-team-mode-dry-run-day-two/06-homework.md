# Week 8 — Homework

Six practice problems. The homework rehearses the lectures with new fake scenarios. Each problem has a deliverable; commit them all to a single file `WEEK-08-HOMEWORK.md` in your week-8 working folder.

The homework is *cumulative-style* — the problems compound. Problem 1 is the easiest; Problem 6 integrates several lectures. Aim for 5/6 problems complete by Sunday morning of Week 8.

| Problem | Skill | Time estimate |
|--------|-------|---------------|
| 1 | Hour-12 stand-up template fill | 15 min |
| 2 | Pivot conversation classification | 20 min |
| 3 | Three retro reviews | 30 min |
| 4 | Merge log entry from a fake state | 25 min |
| 5 | Demo cut decision | 20 min |
| 6 | Cross-skill scenario | 40 min |
| **Total** | | **~2.5h** |

---

## Problem 1 — Hour-12 stand-up template fill

A 3-person team (no rotation; 3-person teams skip the Builder Lead rotation per Lecture 1 §2.3) finishes their hour-12 stand-up. The voice notes:

```
Maya (Builder Lead, original):
  - Shipped: MUST 1 merged at hour 10. MUST 2 started; branch open with
    ~80 lines.
  - Blocking: needs Riley's mock data file for MUST 2's saved-items list.
  - Next 4 hours: pair with Riley for 2 hours on MUST 2; rest from hour 16-18.

Riley (Demo Lead):
  - Shipped: hook draft committed. Script outline drafted in HackMD.
  - Blocking: needs MUST 1 seeded with 10 items to test screen-capture
    angles.
  - Next 4 hours: produce mock data file by hour 13 for Maya; capture 3
    seconds of MUST 1 footage by hour 14.

Jamie (Comms Lead):
  - Shipped: logs through hour 11. 4 channel pins. 1 conflict log entry
    (the hour-8 framework swap that resolved in 7 minutes).
  - Blocking: none.
  - Next 4 hours: hour-12 stand-up note (this one), prep stand-up 3
    template for hour 22.
```

**Deliverable:**

Write the hour-12 stand-up log entry. Use the full template from Lecture 1 §2.6. Skip the Builder Lead rotation segment (3-person team). Fill in the MUST-status table from what the voice notes imply; team-health midpoint (invent reasonable words per teammate); day-2 plan (3 bullets, owners, timestamps).

```markdown
### Problem 1 — Hour-12 stand-up log entry

## Hour 12:00 — Hour-12 handoff stand-up (UTC ...)

**3-question round:**
[Maya, Riley, Jamie blocks]

**MUST-status table:**
[3 rows]

**Team-health midpoint:**
[3 words]

**Day-2 plan (3 bullets):**
[3 bullets with owners and timestamps]

**Scribe:** Jamie.
```

The exercise is the *template fluency*. By Saturday's real dry-run, the template should write itself.

---

## Problem 2 — Pivot conversation classification

For each of the following five proposals (received at the indicated hour of a dry-run), classify the proposal as: **pivot**, **scope cut**, **script rewrite**, or **implementation change**. Provide a one-sentence justification per proposal.

```
Proposal A (hour 13): "What if we switched from FIU students to UM students?"
Proposal B (hour 15): "What if we dropped MUST 3 from the demo entirely?"
Proposal C (hour 16): "What if we rewrote the hook to lead with the
                       pain instead of the user?"
Proposal D (hour 17): "What if we used PostgreSQL instead of SQLite for
                       the saved-items database?"
Proposal E (hour 18): "What if we changed the verb from 'browse' to
                       'subscribe' in the build's core flow?"
```

**Deliverable:**

```markdown
### Problem 2 — Classification table

| Proposal | Classification | Justification (1 sentence) |
|----------|---------------|----------------------------|
| A | [pivot/scope cut/script rewrite/implementation] | [why] |
| B | ... | ... |
| C | ... | ... |
| D | ... | ... |
| E | ... | ... |
```

The exercise is the *taxonomy fluency*. Most "pivot conversations" are actually one of the other three categories; recognising which one prevents 90-minute pivot debates.

---

## Problem 3 — Three retro reviews

Find three publicly committed retrospective-style files (`RETRO.md`, `LESSONS-LEARNED.md`, day-2-style log entries with a retro section, or post-event blog posts). Three sources:

- The C4 cohort archive (if accessible).
- Public GitHub repos with `hackathon` topic and a `RETRO.md` or `LESSONS.md` file.
- Devpost project pages or blog posts where the team wrote a public lessons-learned section.

If none of these are available, use the three retros embedded in:
- Lecture 3 §5.6 (the C4 reference retro entry)
- Exercise 3's expected solution
- The Atlassian "Sprint retrospective" guide's sample output (as a real public reference)

**Deliverable:**

For each retro, identify the *single follow-up commitment* the team named. Three sentences total.

```markdown
### Problem 3 — Three retro reviews

Retro 1: [URL or source]
  Follow-up commitment: [one sentence naming what they committed to change]

Retro 2: [URL or source]
  Follow-up commitment: [one sentence]

Retro 3: [URL or source]
  Follow-up commitment: [one sentence]
```

The exercise is the *evidence recognition*. Reading three retros sharpens the eye for what a real follow-up issue looks like in committed text.

---

## Problem 4 — Merge log entry from a fake state

```
Fake state at hour 15:

  main is at commit f1e2d3c (hour 14:30).
  Branch should-2-darkmode is rebased and approved; ready to merge.
    Author: Sam. Reviewer: Alex (Builder Lead).
    Lines: 142 (under cap).
    Touches: src/styles/globals.css (+78), src/lib/theme.ts (new, 64).
    PR #14, opened hour 13:00, frozen hour 14:30.

  No other PRs open.
  The team is in the slump window; Pat is napping until hour 16.
  The deploy URL is healthy.
```

**Deliverable:**

Write the merge log entry. Use the Lecture 2 §2.4 template. Include a 4-line commit message in the §2.3 format.

The exercise is the *format fluency*. By Saturday, the template should not require re-reading the lecture.

---

## Problem 5 — Demo cut decision

```
Scenario at hour 18:

  The team's SHOULD list:
    SHOULD-1: empty-state illustration (small SVG; ~20 min to polish).
    SHOULD-2: dark-mode toggle (~10 min to polish; mostly done from
              Problem 4's merge).
    SHOULD-3: "leaderboard" of most-saved items across all users
              (~60 min remaining work; the API endpoint exists but
              the UI is half-built; not in the script).

  The team applies the 3-line checklist to each SHOULD.
```

**Deliverable:**

For each of SHOULD-1, SHOULD-2, SHOULD-3:
- Answer each of the 3 checklist questions (yes/no).
- State the decision (keep, cut, escalate).
- Provide a one-sentence justification.

```markdown
### Problem 5 — Demo cut decisions

SHOULD-1: empty-state illustration
  Q1 (recordable in 3 min): [yes/no]
  Q2 (>30 min polish): [yes/no]
  Q3 (script survives without): [yes/no]
  Decision: [keep/cut/escalate]
  Justification: [one sentence]

SHOULD-2: dark-mode toggle
  [same fields]

SHOULD-3: leaderboard
  [same fields]
```

The exercise is the *rubric mechanics*. By hour 18 of the real dry-run, the team should be applying the rubric in <2 minutes per item.

---

## Problem 6 — Cross-skill scenario

A scenario integrating Lectures 1, 2, and 3:

```
Time: hour 20:30 of the dry-run.
Setup: take 1 of the dress rehearsal just finished. The Demo Lead
(Riley) wants to lock take 1 as the final. The Builder Lead (Maya)
disagrees — she thinks the MUST 3 polling fallback was confusing in
take 1 and wants to do a take 2 with a script tweak.

The Comms Lead (Jamie) is the audience proxy. Jamie's take-1 notes:
  - Hook: clean.
  - MUST 1: clean.
  - MUST 2: clean.
  - MUST 3: polling fallback worked, but the script line says "live
    push" without naming the polling. The visual showed the polling
    refresh but the script didn't acknowledge it. A judge would be
    momentarily confused.

The team has ~3.5 hours to submission. The recording window is
typically 30-45 minutes per take. The script update Maya proposes
is 1 line.
```

**Deliverable:**

Write three artifacts:

(a) The 1-paragraph framing Jamie (Comms Lead) posts in #channel to surface the decision, applying the Lecture 3 §6.1 intervention pattern.

(b) The decision Jamie supports — keep take 1, do take 2 with the script tweak, or escalate — with a one-paragraph rationale.

(c) The `DAY-2-LOG.md` entry, written *after* the decision (assume take 2 is shot with the 1-line script tweak; take 2 is the final).

```markdown
### Problem 6 — Dress-rehearsal recording dispute

(a) Framing post in #channel:
[one paragraph]

(b) Jamie's supported decision and rationale:
[one paragraph]

(c) DAY-2-LOG.md entry for take 2:

## Hour [N] — Take 2 dress rehearsal (UTC ...)
[full entry]
```

The exercise is the *integration*. Problem 6 touches the merge protocol (the build is locked, can't merge new code), the dress rehearsal roles (Director, Operator, Audience Proxy), the no-re-litigation rule (but the script tweak is a legitimate factual fix, not a rewrite), and the recording dispute intervention pattern.

---

## Rubric

Each problem is graded on three axes: completeness (deliverable filled), accuracy (matches the lecture taxonomy), and concision (no padding).

| Score | Meaning |
|------|---------|
| 6/6  | Strong. Every problem is concise, accurate, complete. Move to Week 9. |
| 5/6  | Strong. One problem is partial. Identify which one; the muscle for that problem is the weakest. |
| 4/6  | Acceptable. Two problems are partial. Re-read the relevant lectures; iterate. |
| <4/6 | The homework is not warming the muscles. Re-read all three lectures; redo from problem 1. |

## Acceptance checklist

- [ ] All six problems have a deliverable section in `WEEK-08-HOMEWORK.md`.
- [ ] Problem 1's stand-up entry has all six segments (minus the rotation segment for a 3-person team).
- [ ] Problem 2's classification table has 5 rows.
- [ ] Problem 3's three reviews each have a one-sentence follow-up commitment.
- [ ] Problem 4's merge log entry has the §2.4 template and the §2.3 commit message.
- [ ] Problem 5's three SHOULD decisions each have the 3 checklist answers, the decision, and the justification.
- [ ] Problem 6's three artifacts each follow the template provided.
- [ ] The full file is committed to your week-8 working folder.

## What to do with the deliverable

The homework is *practice for the dry-run*. The fluency built here — writing the stand-up entry in 5 minutes, classifying a pivot proposal in 30 seconds, applying the cut rubric in 90 seconds — is the difference between a Saturday-into-Sunday dry-run that feels practiced and one that feels like a first time.

Most cohort learners under-do the homework for Week 8 because Week 7's homework already felt heavy. The dry-run surfaces the under-doing on Sunday afternoon when the Comms Lead is fumbling the retro template at hour 24. Do the six problems; come into the weekend with the muscles warm.

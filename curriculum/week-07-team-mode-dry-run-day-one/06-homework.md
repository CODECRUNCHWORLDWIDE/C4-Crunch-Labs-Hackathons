# Week 7 — Homework

Six practice problems. The homework rehearses the lectures with new fake scenarios. Each problem has a deliverable; commit them all to a single file `WEEK-07-HOMEWORK.md` in your week-7 working folder.

The homework is *cumulative-style* — the problems compound. Problem 1 is the easiest; Problem 6 integrates several lectures. Aim for 5/6 problems complete by Sunday morning of Week 7.

---

## Problem 1 — Role-fit grid

A team of 3 people is about to start a dry-run. Their solo skill profiles:

```
Pat:    strongest at frontend (Vue); decent at backend (Node);
        weak at design copy.
Sam:    strongest at copy + design (Figma); decent at frontend;
        weak at backend.
Jordan: strongest at backend (Python/Flask); decent at infrastructure
        (Render, Railway); weak at copy.
```

**Deliverable:**

Fill out the role-fit grid for this team. Score each teammate's row 0-3 across the three roles. Then assign each role to the highest-scoring teammate. Show your grid:

```markdown
### Problem 1 — Role-fit grid for Pat, Sam, Jordan

|         | Builder | Demo | Comms |
|---------|---------|------|-------|
| Pat     |    ?    |  ?   |   ?   |
| Sam     |    ?    |  ?   |   ?   |
| Jordan  |    ?    |  ?   |   ?   |

**Role assignments:**
- Builder Lead: [name] (score: [N])
- Demo Lead: [name] (score: [N])
- Comms Lead: [name] (score: [N])

**Tie-break notes (if any):**
[one sentence per tie, if any]
```

Three minutes per row of the grid. The exercise is the *fluency* — filling the grid fast and committing to an assignment without re-litigating.

---

## Problem 2 — Hook draft from a prompt

A fake event prompt:

```
Theme: "Public transit timing"

Build a tool that helps a specific commuter group time their travel
better. The commuter group is yours to pick (one named city, one
named line, one named station, one named time of day).
```

**Deliverable:**

Write a 30-second hook for a 3-minute demo using this prompt. Three lines (Lecture 1 voice; refer back to W6 Lecture 1 if needed). Use the first-sentence rule: line 1 names a user *and* a pain; line 2 names the verb the demo will perform; line 3 transitions into the problem beat.

```markdown
### Problem 2 — Hook draft

Line 1 (8-12 sec): [user, in a scene]
Line 2 (8-12 sec): [pain, made concrete]
Line 3 (6-10 sec): [verb the demo will perform]
```

Read it aloud. If it does not name a user, a pain, and a verb, re-write.

---

## Problem 3 — Three sample logs review

Find three publicly committed `DAY-1-LOG.md`-style files. Three sources:

- The C4 cohort archive (if accessible).
- Public GitHub repos with the `hackathon` topic that have day-1 dev logs.
- Any winning Devpost submission whose linked repo has a dev log committed during the event window.

If none of these are available, use the three sample log entries embedded in Lecture 1 §7.3, Lecture 2 §2.5, and Lecture 3 §8.4.

**Deliverable:**

Read each log. Write one sentence per log naming *what the team's hour-2 scope cut was* (i.e., which features were cut from MUST to SHOULD or removed entirely). Three sentences total.

```markdown
### Problem 3 — Three sample logs review

Log 1: [URL or source]
  Hour-2 cut: [one sentence]

Log 2: [URL or source]
  Hour-2 cut: [one sentence]

Log 3: [URL or source]
  Hour-2 cut: [one sentence]
```

The exercise is the *recognition*. Reading three real (or sample) logs sharpens your eye for what a scope cut actually looks like in a committed file.

---

## Problem 4 — Stand-up note template fill

A 4-person team finishes stand-up 2 (hour 12). The note-taker (Comms Lead) is about to write the log entry. The voice notes from the stand-up:

```
Pat (Builder Lead, rotating off at this stand-up):
  - Shipped MUST 1 yesterday; MUST 2 is in PR for the last 90 min;
    MUST 3 not started.
  - No personal block; PR is waiting on review.
  - Next 4 hours: handing Builder Lead off to Alex; will rest for
    2 hours; then pick up MUST 3 backend.

Sam (Demo Lead):
  - Shipped: hook draft, script outline. Full script draft committed.
  - Blocking: need MUST 1 seeded data to do screen-capture rough.
  - Next 4 hours: get seeded data from Alex by hour 13; record
    rough by hour 14; second take by hour 16.

Jordan (Comms Lead):
  - Shipped: hour-0, hour-2, hour-4 log entries; 5 pinned messages;
    one conflict log entry (Pat-Alex MUST-2 PR review delay at hour 9).
  - No block.
  - Next 4 hours: monitor channel; catch the role rotation announcement
    in the log; prep stand-up 3 template for hour 22.

Alex (Floating Builder, rotating into Builder Lead):
  - Shipped: empty-feed state, seeded data for MUST 1 (will publish
    in next 30 min).
  - Blocking: need to formally accept Builder Lead role and confirm
    merge philosophy with the team.
  - Next 4 hours: take over as Builder Lead; review Pat's MUST 2 PR
    by hour 12:30; start MUST 3 frontend.
```

**Deliverable:**

Write the stand-up 2 log entry using the template from Lecture 3 §4.3. Include the cross-track section. Include the role-rotation entry (Lecture 1 §4.3).

```markdown
### Problem 4 — Stand-up 2 log entry

## Hour 12:00 — Stand-up 2 (UTC YYYY-MM-DDTHH:MM)

**Pat (Builder Lead, rotating off):**
  - Shipped: ...
  - Blocking: ...
  - Next 4h: ...

[... fill in all four teammates ...]

**Cross-track:**
[one paragraph naming the cross-track dependencies and the order]

**Role rotation:**
[one paragraph naming the rotation, the effective timestamp, and
the merge-philosophy confirmation]
```

The exercise is the *format fluency*. By the time you do this for real on Saturday, the template should write itself.

---

## Problem 5 — Conflict intervention

A scenario:

```
Time: hour 14:30 of a real dry-run.
Setup: Sam (Demo Lead) has been quiet in #channel for 3 hours.
The last message they posted was a hook draft at hour 11:30.
The team is about to start stand-up 2 (delayed by 30 min due
to a deploy fix). Sam has not joined the call.
Builder Lead (Pat) DMs you (Comms Lead, Jordan) and says:
"Sam's missing the stand-up — should I just start without
them?"
```

**Deliverable:**

Write two messages:

(a) Your one-sentence reply to Pat's DM.

(b) Your one-sentence intervention to Sam (DM or #channel — you decide which, and explain why in one sentence).

```markdown
### Problem 5 — Conflict intervention

Reply to Pat (DM):
[one sentence]

Intervention to Sam:
Channel surface (DM or #channel): [pick one + one sentence rationale]
Message: [one sentence]
```

The exercise is the *judgment* on surface choice (DM vs channel) plus the *delivery* of the intervention. Sam may be sleeping, may be sick, may be stuck on a hard problem, may be silently disagreeing — the intervention does not pre-judge.

---

## Problem 6 — Cross-track decision log

A complex scenario integrating Lectures 1, 2, and 3:

```
Time: hour 17:00 of the dry-run.
Setup: the build track has shipped MUST 1 and MUST 2; MUST 3
(real-time push) is at 30% done. The Builder Lead estimates
MUST 3 needs another 6 hours to finish — putting it at hour 23,
30 minutes before the recording window. The Demo Lead wants
to start the recording rehearsal at hour 22 sharp, with a
buffer for re-takes. The team is deliberating: cut MUST 3
to SHOULD now, or push for the 6 hours?

Three teammates are on the call. The Demo Lead proposes the
cut; the Builder Lead pushes for the build. The fourth
teammate (Floating Builder) has been silent. You are the
Comms Lead.
```

**Deliverable:**

Write three artifacts:

(a) The one-paragraph framing you (as Comms Lead) post in #channel to surface the decision *before* the team starts arguing about it.

(b) The one-sentence intervention to the silent Floating Builder, surfacing their opinion.

(c) The one-paragraph `DAY-1-LOG.md` entry, written *after* the team decides (assume they cut MUST 3 to SHOULD and replace it with a "polling-every-2s" fallback that is already 60% done from Alex's earlier exploratory work).

```markdown
### Problem 6 — Cross-track decision log

(a) Framing post in #channel:
[one paragraph]

(b) Intervention to the silent Floating Builder:
[one sentence]

(c) DAY-1-LOG.md entry for the decision:

## Hour 17:30 — Scope cut: MUST 3 to SHOULD (UTC ...)

**Trigger:** ...
**Discussion:** ...
**Decision:** ...
**Replacement:** ...
**Owner of replacement:** ...
**Next milestone:** ...
```

The exercise is the *integration*. Problem 6 touches the kickoff (roles), the scope (MoSCoW cut), the parallelization (track owners), the comms norms (decisions in channel), the stand-up cadence (which the cut affects), and the close-out (which the cut produces a different MUSTs-shipped table for). One problem; six lectures' worth of muscles.

---

## Acceptance checklist

- [ ] All six problems have a deliverable section in `WEEK-07-HOMEWORK.md`.
- [ ] Problem 1's grid has 9 cells filled with 0-3 scores and 3 role assignments.
- [ ] Problem 2's hook has 3 lines and reads aloud in 22-34 seconds.
- [ ] Problem 3's three log reviews each have a one-sentence cut summary.
- [ ] Problem 4's stand-up entry has 4 teammate blocks, a cross-track section, and a role-rotation paragraph.
- [ ] Problem 5's two messages each fit on one line.
- [ ] Problem 6's three artifacts each fit on the template provided.
- [ ] The full file is committed to your week-7 working folder.

## What to do with the deliverable

The homework is *practice for the dry-run*. The fluency built here — filling the grid in 3 minutes, drafting the stand-up entry in 5, writing the intervention in 30 seconds — is the difference between a Saturday dry-run that feels like a *practiced run* and one that feels like a *first time*.

Most cohort learners under-do the homework. The dry-run surfaces the under-doing on Saturday afternoon when the Comms Lead is fumbling the stand-up template at hour 4. Do the six problems; come into Saturday with the muscles warm.

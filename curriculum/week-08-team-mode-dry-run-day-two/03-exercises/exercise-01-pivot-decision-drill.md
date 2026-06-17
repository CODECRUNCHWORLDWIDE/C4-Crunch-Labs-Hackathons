# Exercise 1 — Pivot Decision Drill

> **Time:** ~1 hour.
> **When in the week:** Tuesday.
> **Deliverable:** `EXERCISE-01-PIVOT-DRILL.md` committed to your week-8 working folder.
> **Prerequisite:** Lecture 1 read.

## What this exercise is

You will apply the 15-minute pivot decision protocol from Lecture 1 §6 to three fake scenarios. For each scenario, you will:

- Identify whether the proposal is *actually* a pivot, a scope cut, or a script rewrite.
- Apply the 2-question rubric (Lecture 1 §6.4).
- Write the log entry that would result from the protocol.
- Time-box each scenario at 15 wall-clock minutes (use a timer; the time-box is part of the muscle).

The exercise is solo. You are role-playing all four positions in each scenario. The output is the kind of log entry the real Comms Lead would commit at hour 14:15 of a real dry-run.

## What this exercise is not

This is not a team activity. You are not gathering three friends and role-playing the conversation. The exercise is the *writing* — converting the scenario into a decision and a log entry, under a 15-minute clock.

## The three scenarios

### Scenario A — The seduction of the alternative (hour 14)

```
Setup: it is hour 14 of a 24-hour dry-run. The team's prompt was:

  "Build a tool that helps a specific user group time their
   travel better."

The team chose, at hour 2, to target FIU students timing their walk to
the 8am classroom from the dorms (an MUST list of: 1) a one-page form
for entering dorm + class building, 2) a calculated walk-time estimate
from a hardcoded Google Maps API call, 3) a "leave by" timestamp).

MUST 1 has shipped at hour 8. MUST 2 is in PR at hour 11; review is
underway at hour 14.

At hour 14:00, Sam (Demo Lead) joins the call and proposes:

  "Hey — what if we changed the target user to *Miami bus commuters*
   instead of FIU students? The seeded data for bus routes is way more
   compelling than the dorm-to-class walking data. We could still ship
   MUST 1 and MUST 2 with minor adjustments."

The team has ~10 hours of build remaining. The pivot conversation is
about to start.
```

### Scenario B — The late-arriving inspiration (hour 16)

```
Setup: it is hour 16 of a 24-hour dry-run. The team's prompt was:

  "Build a single-page web tool that helps a specific user group
   do a specific task in under 30 seconds."

The team chose to target high-school CS club members; the build is a
"pick-a-coding-challenge in 30 seconds" page. MUST list: 1) a 5-card
deck of weekly challenges, 2) a difficulty filter, 3) a localStorage
"already-tried" tracker.

All three MUSTs are merged at hour 14. The team is in the slump window;
Pat (Builder Lead) is on a 2-hour rest from hour 14 to hour 16.

At hour 16:05, Alex (rotating-in Builder Lead) joins the call with an
idea:

  "I just thought of this in the shower: what if instead of a static
   challenge deck, we wired up the GitHub API and pulled live issues
   labeled 'good-first-issue' from open-source repos? It would be way
   more impressive — like a real-time good-first-issue picker. We have
   8 hours left."

Pat is offline; Sam and Jordan are on the call. The team has 8 hours
remaining; the demo recording is at hour 20.
```

### Scenario C — The demo mismatch (hour 18)

```
Setup: it is hour 18 of a 24-hour dry-run. The team's prompt was:

  "Build a tool that helps a specific user group take a specific
   action faster than they could before."

The team built a "queue-of-students-needing-help" page for a fake CS
tutoring center. MUST list: 1) a tutor-side queue view sorted by
wait-time, 2) a student-side "request help" form, 3) a real-time
push notification to the tutor when a new student joins the queue.

All three MUSTs merged at hour 16. Pat (Builder Lead) is on the call.
Sam (Demo Lead) starts the dress-rehearsal prep and discovers:

  "The push notification works, but when I screen-record the tutor
   view, the notification appears as a small browser-OS popup that
   doesn't really show in the recording. It's there for the user but
   not for the camera. The demo script assumes we can SHOW the push
   notification in the recording.

   Do we change the build (e.g., add an in-page banner that mirrors
   the push), or do we change the script (e.g., remove the push beat),
   or do we pivot to a different MUST 3?"
```

## The deliverable

For each scenario, write the 15-minute protocol output:

```markdown
## Scenario A — [your one-line summary]

**Proposed pivot:**
[2-3 sentences: the proposal in your own words]

**Rubric q1 — is it actually a pivot:**
[Yes/no, and reasoning. Reference Lecture 1 §6.1.]

**Rubric q2 — does it ship in remaining time:**
[Yes/no, and reasoning. Reference Lecture 1 §6.4.]

**Decision:**
[NOT PIVOTING / PIVOTING / NOT PIVOTING, CUT A MUST INSTEAD / NOT PIVOTING, SCRIPT REWRITE]

**Alternative considered (and rejected):**
[1-2 sentences]

**Owner of the next step:**
[name + brief description of the next action]

**Time spent:**
[How long this took you to write, in minutes. Aim for <15 per scenario.]
```

Three scenarios × ~15 minutes each + 15 minutes for review = ~1 hour total.

## Acceptance checklist

- [ ] All three scenarios have a complete protocol-output block.
- [ ] Each q1 and q2 answer references the relevant lecture section.
- [ ] Each decision is one of the four allowed values.
- [ ] Each scenario's "time spent" is recorded.
- [ ] The committed file is under 400 lines.

## Why this exercise

The pivot protocol's value is the 15-minute cap. The exercise rehearses the *cap*. By Saturday's real dry-run, you should be able to time-box the conversation at 15 minutes regardless of which scenario surfaces.

Three of the four conflict-pattern interventions from Lectures 1 and 2 — the silent stalemate, the implementation-disguised-as-pivot, the 90-minute pivot debate — fail when the team has not rehearsed the cap. The exercise is the rehearsal.

## A note on what answers are "right"

Two of the three scenarios should resolve as *not* a pivot. The exercise's hidden lesson: most "pivot conversations" are actually scope cuts or script rewrites in disguise. Scoring yourself against the solutions in [SOLUTIONS.md](./SOLUTIONS.md), the metric is *not* whether you matched the same decision but whether your reasoning was clean: rubric q1 answered correctly, rubric q2 answered correctly, the decision following from the rubric.

A scenario that you read as "actually pivot" when the solution says "not a pivot" is a learning moment — re-read Lecture 1 §6.1 on what counts as a pivot, and revisit your reasoning.

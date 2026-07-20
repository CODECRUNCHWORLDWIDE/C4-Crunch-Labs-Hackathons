# Exercise 3 — Conflict-Intervention Drill

> **Time:** ~45 minutes.
> **When in the week:** Friday afternoon.
> **Deliverable:** `EXERCISE-03-INTERVENTIONS.md` committed to your week-7 working folder.
> **Prerequisite:** Lecture 3 read; Exercises 1 and 2 complete.

## What this exercise is

You will write *one-sentence interventions* for the four day-1 conflicts from Lecture 3 §7, applied to *four specific fake scenarios*. The output is a one-sentence intervention per scenario, plus a one-paragraph log entry per scenario, in the C4 voice.

The muscle being built is the *delivery* — the wording of an intervention that surfaces a conflict without escalating it. Lecture 3 gave you the four canonical interventions; this exercise drills variations against scenarios you have not seen.

## Why this exercise matters

The one-sentence intervention is the highest-leverage tool the Comms Lead has during a 24-hour build. It costs 20 seconds to deliver and prevents 4 hours of follow-on conflict. The skill is *not* in the knowing — the canonical interventions are in Lecture 3 — but in the *delivery*. The delivery is the muscle you build by writing variations.

Most learners read Lecture 3 once and assume they have the muscle. They do not. Reading is recognition; writing is recall. Exercise 3 is the writing.

## The four scenarios

Four fake scenarios. Each names the conflict type, the trigger, the affected teammates, and the surface (channel or DM). You write the intervention and the log entry for each.

### Scenario 1 — Scope creep

```
Time: hour 7:30 of the dry-run.
Conflict type: scope creep (Lecture 3 §7.1).
Trigger: Sam (Demo Lead) has opened a PR titled "Add dark-mode toggle"
  while MUST 2 is still in progress. Dark-mode is in the COULD column
  of the worksheet; it was not pulled in at any stand-up.
Affected teammates: Sam (PR author), Pat (Builder Lead, who would have
  to review and merge the PR).
Surface: #channel — Sam posted "Just opened a dark-mode PR — small,
  should merge fast" 5 minutes ago. No reactions yet.
Comms Lead (you): Jordan.

Write:
  (a) Your one-sentence intervention in #channel.
  (b) The one-paragraph DAY-1-LOG.md entry for this conflict moment.
```

### Scenario 2 — Silent disagreement

```
Time: hour 12:00 of the dry-run, during stand-up 2.
Conflict type: silent disagreement (Lecture 3 §7.2).
Trigger: Alex (Floating Builder) has answered the three stand-up
  questions with "shipped: nothing. blocking: nothing. next 4h:
  whatever Pat needs." This is Alex's second clipped stand-up in
  a row.
Affected teammates: Alex (clipped); the team (interpreting the
  clipped answer as "no problem").
Surface: voice on the team call, plus the stand-up note in #channel.
Comms Lead (you): Jordan.

Write:
  (a) Your one-sentence intervention in DM to Alex, sent 5 minutes
      after the stand-up ends.
  (b) The one-paragraph DAY-1-LOG.md entry for this conflict moment,
      written after Alex's response.
```

### Scenario 3 — Role overlap

```
Time: hour 16:00 of the dry-run.
Conflict type: role overlap (Lecture 3 §7.3).
Trigger: Pat (Builder Lead) merged a PR for MUST 2 at hour 15:00.
  Alex (Floating Builder) discovered at hour 15:45 that they had
  also been working on MUST 2 in a separate branch, with a
  different approach. Alex pushed their branch at hour 15:50 with
  a PR titled "MUST 2 — alternate impl." Pat and Alex are now
  arguing in #channel about whose approach to use.
Affected teammates: Pat, Alex; the rest of the team is watching.
Surface: #channel — 14 messages back-and-forth in the last 10
  minutes; tone is rising.
Comms Lead (you): Jordan.

Write:
  (a) Your one-sentence intervention in #channel.
  (b) The one-paragraph DAY-1-LOG.md entry for this conflict moment.
```

### Scenario 4 — "I'll just rewrite it" merge fight

```
Time: hour 19:30 of the dry-run.
Conflict type: merge fight (Lecture 3 §7.4).
Trigger: Sam's MUST 3 frontend PR has been open for 75 minutes
  waiting on Pat's review. Pat is in the middle of debugging
  the deploy URL and has not seen the PR. Sam, frustrated, has
  started re-writing MUST 3's frontend from scratch in a new
  branch and posted in #channel: "Just rewriting MUST 3
  frontend. PR coming."
Affected teammates: Sam (frustrated), Pat (overloaded), the team
  (about to lose 75 minutes of Sam's first PR if the rewrite ships).
Surface: #channel — Sam's post is 2 minutes old.
Comms Lead (you): Jordan.

Write:
  (a) Your one-sentence intervention in #channel, proposing a new
      team norm.
  (b) The one-paragraph DAY-1-LOG.md entry for this conflict moment,
      including the new norm if the team accepts it.
```

## The intervention template

Each intervention follows the Lecture 3 §7.5 pattern:

```
1. Surface the issue without blame.
2. Offer two or more paths.
3. Give the affected teammate the choice.
4. Log the resolution.
```

Steps 1-3 are the *one-sentence intervention*. Step 4 is the *log entry*. Each is a separate deliverable per scenario.

## The log entry template

Each scenario's log entry is one paragraph in `DAY-1-LOG.md`. The format:

```markdown
### Hour HH:MM — [Conflict type] (UTC YYYY-MM-DDTHH:MM)

**Trigger:** [one sentence — what happened]
**Affected:** [named teammates]
**Intervention (Comms Lead):** [the one-sentence intervention, in quotes]
**Resolution:** [what the team decided, in one sentence]
**Follow-up:** [if any norm was added, the new norm in one sentence;
                otherwise "none"]
```

Five fields. Each one short. The log entry is the audit trail for the post-dry-run retrospective.

## Process

1. Open a new file: `exercise-03-interventions.md`.
2. For each scenario (1, 2, 3, 4), write the one-sentence intervention and the one-paragraph log entry using the templates above.
3. Read each intervention aloud. If it sounds like a manager scolding a teammate, re-write it. If it sounds like a teammate surfacing a structural issue, keep it.
4. Commit.

## Sample intervention (for calibration)

Here is a *sample* intervention for a fifth (non-graded) scenario, to calibrate your tone. Do not copy it for scenarios 1-4; write your own.

```
Sample scenario: at hour 10:00, two teammates have been silent in
#channel for 90 minutes while the third is asking for a code review
on a 200-line PR. The third teammate just posted: "Anyone??"

Sample intervention (in #channel):
"Pat, your PR is waiting since 8:30 — Sam and Alex, are you in flow
or available for a 15-min review? Either is fine; if you're in flow,
I'll ping Jordan."

Sample log entry:
### Hour 10:05 — Review SLA stress (UTC 2026-XX-XX-15:05)
**Trigger:** Pat's MUST 1 PR open 90 min without review; Pat
posted "Anyone??" at hour 10:03.
**Affected:** Pat (waiting), Sam and Alex (silent).
**Intervention (Comms Lead):** "Pat, your PR is waiting since 8:30 — Sam
and Alex, are you in flow or available for a 15-min review? Either is
fine; if you're in flow, I'll ping Jordan."
**Resolution:** Sam available; reviewed in 12 min; PR merged at hour 10:35.
**Follow-up:** None; team norm "60-min review SLA" already in TEAM-CONTRACT.md.
```

That sample is *one* style. Your scenarios will have different tones (DM vs channel, mid-conflict vs pre-conflict). Match the surface; keep the structure.

## Acceptance checklist

- [ ] Scenario 1 has one intervention sentence (in #channel) and one log paragraph.
- [ ] Scenario 2 has one intervention sentence (in DM) and one log paragraph.
- [ ] Scenario 3 has one intervention sentence (in #channel) and one log paragraph.
- [ ] Scenario 4 has one intervention sentence (in #channel proposing a norm) and one log paragraph including the norm.
- [ ] Each intervention is a single sentence (not two; not a paragraph).
- [ ] Each intervention surfaces the issue without naming a teammate's fault.
- [ ] Each intervention offers at least two paths.
- [ ] Each intervention gives the affected teammate the choice.
- [ ] Each log entry has the 5 fields (trigger, affected, intervention, resolution, follow-up).
- [ ] Reading each intervention aloud takes 6-10 seconds.
- [ ] No intervention uses the words "you should," "you need to," or "you're." (These shift the structural fix into a personal scolding.)
- [ ] No intervention apologizes ("sorry to interrupt..."). The Comms Lead is doing their job, not interrupting.

## Common failure modes

- **The accusation intervention.** "Sam, you're scope-creeping; please close the PR." The verb "you're" is the tell. *Fix:* re-write as "Is the dark-mode PR a pull-in we agreed to, or a park?" — passive voice on the structural question, no naming of fault.
- **The four-sentence intervention.** The Comms Lead writes a long, explanatory message that re-states the worksheet, the scope-pass agreement, and the team-contract section before naming the choice. *Fix:* one sentence. The context is the channel's pinned messages; the team has read them; do not re-state them in the intervention.
- **The closed intervention.** "Sam, please close the dark-mode PR." One path; no choice. *Fix:* two paths. "Close, park, or formally pull in — which?"
- **The non-logged resolution.** The team resolves the conflict in 5 minutes and moves on; nothing goes in the log. *Fix:* the log entry is *non-optional*. Even if the resolution is trivial, the log captures it. The post-dry-run retrospective can only see what was logged.
- **The cold tone.** The intervention reads like a robot; the team feels managed instead of supported. *Fix:* warmth is fine in the *adjacent* messages (the encouragement after the resolution, the side-channel check-in to the affected teammate). The intervention itself stays structural; the warmth is the wrap.

## What to do with the deliverable

The deliverable is the *Friday-afternoon rehearsal*. On Saturday or Sunday of the real dry-run, the Comms Lead will deliver real interventions (not these four scenarios; whatever the real team surfaces). The Friday version is the practice; the dry-run version is the artifact.

The skill is *not* memorizing the four canonical interventions. The skill is *recognizing* the conflict type within 30 seconds of it surfacing, picking the right template, and delivering it in one sentence. Exercise 3 builds the recognition. Recognition is half the muscle; delivery is the other half.

## Up next

You have completed all three exercises. Continue to:

- [The quiz](../quiz.md) — 10 multiple-choice questions on team dynamics and time-boxed project management.
- [The challenge](../challenges/challenge-01-clean-24-hours.md) — the optional acceptance criteria for "did the team run a clean 24 hours?"
- [The homework](../homework.md) — six practice problems.
- [The mini-project](../mini-project/README.md) — the 24-hour dry-run with real teammates.

The dry-run is the integration test. Exercises 1, 2, and 3 are the unit tests.

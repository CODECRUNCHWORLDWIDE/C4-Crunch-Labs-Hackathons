# Exercise 3 — Retro from a Fake Log

> **Time:** ~30 minutes.
> **When in the week:** Friday.
> **Deliverable:** `EXERCISE-03-RETRO.md` committed to your week-8 working folder.
> **Prerequisite:** Lecture 3 read.

## What this exercise is

You are given a fake `DAY-2-LOG.md` excerpt (below) — the day-2 entries from a hypothetical team's dry-run. You will write the hour-24 retrospective for this team, using the kept/changed/dropped template from Lecture 3 §5, and propose the single follow-up issue the team should file.

The exercise is solo. You are the Comms Lead, drafting the retro entry during the meeting and the follow-up issue afterward. The output is the kind of artifact the real Comms Lead would commit at hour 24:25 of a real dry-run.

## What this exercise is not

You are not running the retro with a team; you are *writing* the retro from a log. The skill being built is *reading a log honestly* and extracting the four KEPT items, four CHANGED items, and four DROPPED items the log actually supports — not the ones you wish the team had.

## The fake log

```markdown
## Hour 12:00 — Hour-12 handoff stand-up (UTC 2026-05-16T03:00)

**3-question round:**

Pat (rotating off Builder Lead):
  - Shipped: MUST 1 merged at hour 9:30. MUST 2 in PR (#7) since hour 11.
  - Blocking: PR #7 needs review.
  - Next 4h: 2-hour rest from hour 12-14; then MUST 3 frontend.

Sam (Demo Lead):
  - Shipped: hook draft, partial script outline.
  - Blocking: needs MUST 1 seeded data.
  - Next 4h: get seeded data; rough recording by hour 16.

Jordan (Comms Lead):
  - Shipped: log entries through hour 11.
  - No block.
  - Next 4h: monitor; prep stand-up 3.

Alex (rotating on Builder Lead):
  - Shipped: empty-feed state.
  - Blocking: accepting role.
  - Next 4h: review PR #7; start MUST 3 frontend.

**MUST-status table:**
  - MUST 1 — DONE.
  - MUST 2 — IN PR.
  - MUST 3 — NOT STARTED.

**Builder Lead rotation:** Pat off, Alex on, both lines logged.

**Team-health midpoint:**
  - Pat: "tired-but-okay"; Sam: "focused"; Jordan: "energised"; Alex: "rested".

**Day-2 plan:**
  1. By hour 16: MUST 2 merged. Owner: Alex.
  2. By hour 18: MUST 3 in PR. Owner: Alex.
  3. By hour 20: dress rehearsal. Owner: Sam.

**Scribe:** Jordan.

---

## Hour 14:30 — Pivot conversation: NOT PIVOTING (UTC 2026-05-16T05:30)

**Proposed pivot:** Sam suggested re-targeting from "freshmen" to "transfer students."

**Rubric q1:** Yes, user change is a pivot.
**Rubric q2:** No; 9.5 hours left and MUST 3 unstarted; re-seed data is 2h alone.

**Decision:** NOT PIVOTING. Script-only adjustment to mention both groups.

**Time spent:** 12 minutes (under 15-min cap).
**Scribe:** Jordan.

---

## Hour 16:15 — Merge: MUST 2 saved-items view (UTC 2026-05-16T07:15)

**MUST:** 2.
**PR:** #7 (opened hour 11, frozen hour 15:45, merged hour 16:15).
**Reviewer:** Alex.
**Conflict:** One; src/lib/storage.ts both touched by PR #7 and a hot-fix
Alex pushed at hour 15:30. Resolved by Pat's rebase at hour 15:45.
**Lines:** 187 (under cap).
**Deploy:** auto-deployed at hour 16:18; verified live at hour 16:22.

---

## Hour 17:30 — Conflict: "I'll just rewrite it" merge fight (UTC 2026-05-16T08:30)

**Trigger:** PR #9 (Alex, MUST 3 frontend, 410 lines, over the 200-line cap).
Pat (off-rotation but on call) proposed rewriting the PR's component structure.
Alex resisted; 4 hours invested.

**Intervention (Jordan, in #channel):**
"The merge needs to happen by hour 18 to ship MUST 3; can we land PR #9
as-is and file a follow-up for the refactor, or is there a non-refactor
fix for the specific concern?"

**Resolution:** PR #9 landed as-is at hour 17:55 after Pat agreed.
Follow-up issue filed: #11 — "Refactor MUST-3 component into smaller files."

---

## Hour 18:00 — Demo cut: COULD-2 cross-device sync (UTC 2026-05-16T09:00)

**Cut:** COULD-2 — Firestore cross-device sync. Dropped.

**3-line checklist:**
1. Screen-recordable: yes.
2. Requires >30 min: yes (90 min remaining).
3. Script survives without it: yes.

**Decision:** CUT.
**Replacement:** None; localStorage saved-items is sufficient.
**Script adjustment:** Sam updated line 6.
**Scribe:** Jordan.

---

## Hour 20:15 — Take 1 dress rehearsal (UTC 2026-05-16T11:15)

**Take 1 notes (Jordan as audience proxy):**
- 0:00-0:10: Hook line 1 — Sam read fast.
- 0:25-0:32: MUST 1 — operator clicked wrong nav link.
- 1:30-2:15: MUST 3 — polling fallback visible but not named in script.

**Plan for take 2:** pace hook line 1; operator practices nav; script names polling fallback.

---

## Hour 20:35 — Take 2 dress rehearsal (UTC 2026-05-16T11:35)

**Take 2 notes (Jordan):** Clean throughout. Polling fallback named.

**Decision:** Take 2 is the final. Sam (Demo Lead) locked.

---

## Hour 22:00 — Submission package committed (UTC 2026-05-16T13:00)

**Artifacts:**
- Public repo: https://github.com/dry-run-mock-7
- Live deploy: https://dry-run-mock-7.vercel.app
- 3-min demo: https://www.youtube.com/watch?v=... (unlisted)
- DAY-1-LOG.md and DAY-2-LOG.md: in repo
- SUBMISSION.md: in repo, 6 sections, 487 words

**Stop-work declared at hour 23:00 by Alex (Builder Lead).**

---

## Hour 23:30 — Pre-retro silence (UTC 2026-05-16T14:30)

**Note (Jordan):** Pat has not posted in #channel since hour 22:10.
DM'd Pat at hour 23:25 — "you have been quiet; the retro is at hour 24
and I want to make sure you have what you need; are you doing okay or
do you need 20 minutes to step away before the retro?"
Pat responded at hour 23:28 — "just zoning out; back in time for retro."
Logged.

---

## Hour 24:00 — Retro entry placeholder

[TO BE FILLED IN]
```

## The deliverable

Write the retro entry. Use the template from Lecture 3 §5.6. The entry replaces the `[TO BE FILLED IN]` placeholder at the bottom of the log.

```markdown
## Hour 24:00 — Hour-24 retrospective (UTC 2026-05-16T15:00)

**Duration:** 30 minutes (hour 24:00 to hour 24:30).
**Scribe:** Jordan.

**One-word team-health check:**
  - Pat: [your word]
  - Sam: [your word]
  - Jordan: [your word]
  - Alex: [your word]

**KEPT (4 items):**
  - [name] [item, sourced from the log]
  - [name] [item, sourced from the log]
  - [name] [item, sourced from the log]
  - [name] [item, sourced from the log]

**CHANGED (4 items):**
  - [name] [item, sourced from the log, with the why]
  - ...

**DROPPED (4 items):**
  - [name] [item]
  - ...

**Follow-up issue:**
[Title and 2-sentence scope of the issue you would file.]

**Time spent:** 30 minutes (on the cap).
```

After the retro entry, in the same file, also write the **GitHub issue body** for the follow-up issue — formatted as you would actually file it:

```markdown
### Follow-up issue body

**Title:** [your title]
**Labels:** retro-followup
**Assignee:** [name from the team]

**Description:**

[2-3 sentences connecting the issue to the DROPPED list, then 1-3
bullets of concrete scope. Total <150 words.]

**Acceptance criteria:**
- [ ] [criterion 1]
- [ ] [criterion 2]
- [ ] [criterion 3]
```

## Acceptance checklist

- [ ] Each KEPT, CHANGED, and DROPPED item is *sourced from the log* — you can point to the log entry it comes from.
- [ ] The team-health words are *not* "fine" or "good."
- [ ] The follow-up issue is one (not four).
- [ ] The follow-up issue's scope is concrete (a file, a setting, a paragraph — not "be better at X").
- [ ] The total deliverable is 80-180 lines.

## Why this exercise

The retro is the most-skipped part of day 2. It is also the most-leveraged: the follow-up issue is the *only* artifact that travels from this dry-run to the next one. Writing the retro from a fake log builds two muscles at once — reading a log for evidence, and converting evidence into a concrete next step.

The exercise also rehearses the *honesty discipline*. The fake log includes a "I'll just rewrite it" merge fight, a too-large PR, a near-attrition moment with Pat at hour 23:30, and a scope cut at hour 18. A retro that picks four "good things" and four "great things" is dishonest; the exercise's lesson is to name the hard parts in the CHANGED and DROPPED rounds.

## Notes on the solutions

The solution in [SOLUTIONS.md](./SOLUTIONS.md) is one defensible retro from this log. Multiple defensible retros are possible. The scoring criterion is the *sourcing*: every item should be traceable to a specific log entry. A KEPT item that is not in the log is invented; an invented KEPT is a sign the team is writing the retro they wish they had, not the one they earned.

The follow-up issue should be the *single most-impactful* DROPPED item. There is more than one defensible choice (the 410-line PR is one candidate; the late-MUST-3 start is another; the partial-script-at-hour-12 is a third). The choice is correct if the scope is concrete and the team can plausibly *close* the issue within a week.

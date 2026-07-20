# Challenge 1 — Clean 24 Hours: Acceptance Criteria

> **Time:** ~1 hour.
> **When:** after the dry-run weekend (Sunday evening or Monday morning of Week 8).
> **Deliverable:** a 20-item acceptance scorecard appended to your `DAY-1-LOG.md`.
> **Prerequisite:** mini-project complete; `DAY-1-LOG.md` committed.

## What this challenge is

You will apply a 20-item acceptance checklist to your team's `DAY-1-LOG.md` and produce a yes/no score with one-sentence evidence per item. The checklist is the operational definition of "the team ran a clean 24 hours."

The challenge is *self-graded*. The point is not to score 20/20; the point is to *honestly* score whatever the team did. A team that scores 14/20 with honest evidence is stronger than a team that scores 20/20 with fabricated evidence.

## Why this challenge matters

The dry-run produces a log. The log is the audit trail. The trail is only useful if it is *graded* — without a checklist, the team will look at the log and say "looks fine" and miss the three structural failures that surface as bigger conflicts at the real event.

The 20-item checklist is the *bench*. The dry-run is the *run*. The score is the *measurement*. Without the measurement, the bench is decoration.

## The 20-item acceptance checklist

The 20 items are grouped by phase: kickoff (5), scope and parallel (5), stand-ups and norms (5), close-out and artifacts (5).

### Kickoff (5 items)

```
1. The kickoff started at hour 0:00 ± 10 minutes.
   Evidence: timestamp in DAY-1-LOG.md hour-0 entry.

2. The kickoff finished at or before hour 1:00.
   Evidence: timestamp in the start-coding handoff log line.

3. The three roles (Builder, Demo, Comms) were assigned and named
   in the hour-0 log entry.
   Evidence: role names in the hour-0 entry.

4. The four comms norms (one channel, one doc, one stand-up cadence,
   one DM rule) were pinned in the team channel during segment 5.
   Evidence: screenshot or a "pins set" line in the hour-0 entry.

5. The "we start coding at" timestamp was named aloud and logged.
   Evidence: the timestamp in the hour-0 entry.
```

### Scope and parallel (5 items)

```
6. The formal scope pass happened at hour 2:00 ± 30 minutes.
   Evidence: timestamp in DAY-1-LOG.md hour-2 entry.

7. The committed MUST list has exactly 3 items.
   Evidence: count in SCOPING-WORKSHEET.md section 2.

8. Each MUST has a named owner and a done-row.
   Evidence: SCOPING-WORKSHEET.md section 2 rows.

9. The three tracks (build, design+demo, comms+log) have named
   owners in SCOPING-WORKSHEET.md section 5.
   Evidence: section 5 rows.

10. No track waited on another for more than 30 minutes without
    an escalation log entry.
    Evidence: zero or more "block escalation" entries in
    DAY-1-LOG.md; each escalation resolved in <30 min.
```

### Stand-ups and norms (5 items)

```
11. Stand-up 1 happened at hour 4:00 ± 30 minutes.
    Evidence: timestamp in DAY-1-LOG.md hour-4 entry.

12. Stand-up 2 happened at hour 12:00 ± 30 minutes.
    Evidence: timestamp in DAY-1-LOG.md hour-12 entry.

13. Stand-up 3 happened at hour 22:00 ± 30 minutes.
    Evidence: timestamp in DAY-1-LOG.md hour-22 entry.

14. Each stand-up note has all teammates' answers to the three
    questions (shipped, blocking, next 4h).
    Evidence: count of teammate answer blocks per stand-up entry.

15. At least one named conflict moment was logged, with the
    intervention sentence and the resolution.
    Evidence: zero or more "conflict" entries; each has the
    5-field template filled.
```

### Close-out and artifacts (5 items)

```
16. The hour-24 close-out happened at hour 24:00 ± 30 minutes.
    Evidence: timestamp in DAY-1-LOG.md hour-24 entry.

17. The close-out names which MUSTs satisfied their done-row and
    which did not (per-MUST yes/no).
    Evidence: the close-out entry's "MUSTs shipped" section.

18. The close-out names the day-2 plan as 3 bullets.
    Evidence: the close-out entry's "Day-2 plan" section.

19. The team-health one-word check captured a word per teammate.
    Evidence: the close-out entry's "Team-health words" section.

20. The recording link and the repo link are in the close-out
    log entry.
    Evidence: two URLs in the close-out entry.
```

Twenty items. Each is binary (yes / no). Each has named evidence — a log entry, a section, a count.

## Process

1. Open `DAY-1-LOG.md` from the dry-run.
2. For each of the 20 items, find the named evidence in the log.
3. If the evidence is present, mark "yes" and copy a one-line snippet from the log as evidence.
4. If the evidence is missing, mark "no" and write a one-line explanation of why ("Comms Lead was helping build; log catch-up at hour 24 had this gap").
5. Sum the yeses; the total is your team's score.

## The scorecard template

Append this scorecard to the end of `DAY-1-LOG.md`:

```markdown
## Hour 25:00 — Acceptance scorecard (Challenge 1)

| # | Item | Y/N | Evidence |
|---|------|-----|----------|
| 1 | Kickoff started ±10 min | Y | "Hour 0:00 — kickoff at UTC 2026-XX-XX..." |
| 2 | Kickoff finished by hour 1:00 | Y | "We start coding at hour 1:00..." |
| 3 | Three roles assigned in hour-0 entry | Y | "Pat (Builder Lead), Sam (Demo Lead), Jordan (Comms Lead)" |
| 4 | Four comms norms pinned | Y | "Pins set: agenda, stand-up cadence, DM rule, doc URL" |
| 5 | Start-coding timestamp named | Y | "Start-coding timestamp: 10:00 ET" |
| 6 | Scope pass at hour 2 ±30 min | Y | "Hour 2:30 — formal scope pass complete" |
| 7 | Exactly 3 MUSTs | Y | "MUST 1, MUST 2, MUST 3 in worksheet section 2" |
| 8 | Each MUST has owner + done-row | Y | "section 2 has owner col + done-row col" |
| 9 | Three tracks owned | Y | "section 5 names Pat, Sam, Jordan" |
| 10 | No 30-min block without escalation | N | "Hour 15-16 build block on deploy URL was 60 min; not logged" |
| 11 | Stand-up 1 ±30 min | Y | "Hour 4:00 — stand-up 1" |
| 12 | Stand-up 2 ±30 min | Y | "Hour 12:00 — stand-up 2" |
| 13 | Stand-up 3 ±30 min | N | "Stand-up 3 ran at hour 22:50 — 50 min late due to deploy fix" |
| 14 | All teammates' answers in each stand-up | Y | "4 answer blocks in each entry" |
| 15 | At least one conflict moment logged | Y | "Hour 16:00 — role-overlap intervention logged" |
| 16 | Close-out ±30 min | Y | "Hour 24:00 — close-out" |
| 17 | MUSTs shipped Y/N per MUST | Y | "MUST 1 Y, MUST 2 Y, MUST 3 PARTIAL" |
| 18 | Day-2 plan 3 bullets | Y | "3 bullets in close-out entry" |
| 19 | Team-health word per teammate | Y | "4 words logged" |
| 20 | Recording + repo links in close-out | Y | "YouTube + GitHub URLs" |

**Score:** 18/20.

**Notes:**
  - Item 10 missed: hour 15-16 deploy block was 60 min; team chose to
    work through instead of escalating. The escalation would have
    triggered a 5-min huddle and cut the block to 30 min.
  - Item 13 missed: stand-up 3 ran late because deploy URL was still
    being stabilized. The trade-off was acceptable but the timing slip
    should be flagged in the Week 8 retrospective.
```

The scorecard is honest. The 18/20 above is a *good* score — two structural learnings for Week 8. A 20/20 with no learnings is suspicious; the dry-run probably hid two problems.

## Calibration: what scores mean

```
20/20 — Suspicious. Re-read each "yes" with skeptical eye; usually 1-2
        are fabricated.
17-19/20 — Strong. The team ran a clean 24 hours; the missed items
        are honest gaps to address in Week 8.
13-16/20 — Acceptable. The team ran a real 24 hours; several structural
        gaps to address in Week 8.
9-12/20 — Concerning. The team's process broke down in one or more
        phases; the dry-run surfaced what it was supposed to surface.
        Treat this as the actual win — the gaps would have been
        invisible at the real event.
0-8/20 — Severe. Either the dry-run was abandoned partway through
        or the log was not maintained. Re-run the dry-run; the
        Week 8 retrospective will be hollow without it.
```

A 12/20 dry-run that surfaced eight structural failures *before* the real event is more valuable than a 18/20 dry-run that surfaced two. The score is not the win; the *learning* is the win.

## Acceptance checklist

- [ ] The scorecard table has 20 rows, one per item.
- [ ] Each row has Y or N (no "partial" or "kinda").
- [ ] Each row has a one-line evidence snippet from `DAY-1-LOG.md`.
- [ ] The "Notes" section names the structural learnings for any N rows.
- [ ] The scorecard is appended to `DAY-1-LOG.md` and committed.

## What to do with the deliverable

The scorecard goes into the Week 8 retrospective as the *primary input*. The Week 8 lecture re-reads the dry-run log against the same 20-item checklist; the team's pre-graded scorecard is the starting point.

If your team's score is below 13/20, the Week 8 lecture starts with a structured re-run plan — the second dry-run (Stretch Goal 1) becomes the focus. If the score is 17/20 or higher, Week 8 moves directly into day-2 (demo prep and recording) without a re-run.

The score is *not* a grade. The score is a *signal*. The signal is the input to the Week 8 plan.

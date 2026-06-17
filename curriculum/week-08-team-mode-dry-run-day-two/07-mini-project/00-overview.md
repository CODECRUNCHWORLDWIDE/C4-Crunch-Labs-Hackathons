# Mini-Project — The Hours-12-to-24 Continuation

> **Time:** 12 wall-clock hours of dry-run continuation (hours 12 through 24 of the Week-7 dry-run), of which ~4 are synchronous active work; plus a 30-minute retrospective at hour 24.
> **When in the week:** Saturday afternoon through Sunday afternoon (continuous with the Week-7 dry-run window).
> **Deliverable:** a committed `DAY-2-LOG.md` extending `DAY-1-LOG.md`, plus a `SUBMISSION.md` cover sheet, plus a 3-minute demo video URL, plus a single follow-up issue filed in the repo.
> **Prerequisite:** Week 7 mini-project complete (`DAY-1-LOG.md` committed); all three Week-8 lectures read; all three Week-8 exercises complete; quiz at 9/10 or better.

## What this mini-project is

You will continue the Week-7 dry-run from hour 12 to hour 24. The team, the prompt, the repo, the `TEAM-CONTRACT.md`, the `SCOPING-WORKSHEET.md`, and the `DAY-1-LOG.md` are all the same. The continuation runs the closing protocols from Lectures 1, 2, and 3 in their real-time sequence.

If your Week-7 dry-run ran the *full* 24-hour version, this mini-project is hours 12-24 of that same window. If your Week-7 dry-run ran the 4-hour compressed version (Week-7 mini-project's compressed option), the Week-8 continuation is hours 4-8 of an extended 8-hour compressed mini-hackathon. Both paths are acceptable; the artifacts are identical in shape, only the wall-clock scale differs.

## What this mini-project is not

This is *not* a separate event. It is the continuation of the Week-7 dry-run. The same team that ran hours 0-12 runs hours 12-24. If a teammate drops between Week 7 and Week 8, see Week 8 README's prerequisites — log the drop in `DAY-1-LOG.md` and continue with the remaining team.

## The continuation hours

```
┌────────────────────────────────────────────────────────────────────┐
│  THE HOURS-12-TO-24 CONTINUATION — DAY 2                            │
│                                                                    │
│  Hour 12:00 — 12:30   Hour-12 handoff stand-up (Lecture 1 §2)      │
│  Hour 12:30 — 14:00   Build sprint (MUSTs continue)                │
│  Hour 14:00 — 14:15   Pivot decision (if surfaced; Lecture 1 §6)   │
│  Hour 14:00 — 18:00   Midnight slump window + sleep window         │
│                       (Lecture 1 §4 protocols)                     │
│  Hour 14:00 — 18:00   Integration friction window                  │
│                       (Lecture 2 §2 merge protocol)                │
│  Hour 18:00 — 18:15   Demo cut conversation (Lecture 2 §4)         │
│  Hour 18:15 — 20:00   Polish + script lock                         │
│  Hour 20:00 — 21:30   Dress rehearsal (Lecture 3 §2)               │
│                       — two takes minimum                           │
│  Hour 21:30 — 22:00   Demo video publish                            │
│  Hour 22:00 — 23:00   Submission package (Lecture 3 §3)            │
│                       — SUBMISSION.md, README pass, link gather   │
│  Hour 23:00 — 24:00   Stop work; rest                              │
│  Hour 24:00 — 24:30   Hour-24 retrospective (Lecture 3 §5)         │
│  Hour 24:30 — 48:00   File the follow-up issue within 24 hours      │
└────────────────────────────────────────────────────────────────────┘
```

Twelve wall-clock hours of dry-run. Roughly 4 of those are synchronous active work (the hour-12 stand-up, the hour-18 cut, the hour-20 dress rehearsal, the hour-24 retro). The other 8 are async build, rest, or sleep window.

## The mapping for 4-hour compressed teams

If your Week-7 dry-run ran the 4-hour compressed mini-project, the Week-8 continuation extends to a total 8-hour mini-hackathon:

```
┌────────────────────────────────────────────────────────────────────┐
│  THE 8-HOUR COMPRESSED CONTINUATION — DAY 2 (HOURS 4-8)            │
│                                                                    │
│  Hour 4:00 — 4:15   Mid-event handoff stand-up                     │
│  Hour 4:15 — 5:30   Build sprint (MUSTs continue)                  │
│  Hour 5:30 — 5:40   Mid-event pivot check (if surfaced)            │
│  Hour 5:30 — 6:30   Integration window                             │
│  Hour 6:30 — 6:40   Demo cut conversation                          │
│  Hour 6:40 — 7:30   Dress rehearsal (one take minimum; two preferred)│
│  Hour 7:30 — 7:50   Submission package                              │
│  Hour 7:50 — 8:00   Retro (compressed to 10 minutes)               │
└────────────────────────────────────────────────────────────────────┘
```

Four-hour continuation. All five closing protocols happen; the *durations* shrink, not the *protocols*. The 4-hour version is harder, not easier — same coordination challenges in compressed time.

## The artifacts

By the end of the continuation, the repo contains:

```
.
├── DAY-1-LOG.md          ← from Week 7 (extends with hour-12 onward)
├── DAY-2-LOG.md          ← new in Week 8 (hours 12-24)
├── SUBMISSION.md         ← new in Week 8 (the cover sheet)
├── TEAM-CONTRACT.md      ← from Week 7 (may have one update from the retro)
├── SCOPING-WORKSHEET.md  ← from Week 7 (with cuts logged from hour 18)
├── README.md             ← from Week 7 (with the hour-22 README pass)
├── LICENSE               ← from the template repo (Week 2)
├── CODE_OF_CONDUCT.md    ← from the template repo (Week 2)
├── src/...               ← the build
└── ...
```

Plus, off-repo:
- The 3-minute demo video, published on a free host (YouTube unlisted, Loom).
- One GitHub issue filed in the repo within 24 hours of the retro.

## The `DAY-2-LOG.md` template

`DAY-2-LOG.md` extends `DAY-1-LOG.md`'s timestamp convention. Entries are in chronological order. Each entry has a heading with the hour and a UTC timestamp.

```markdown
# Day-2 Log — [Team name] — Hours 12 to 24

(Continuation of DAY-1-LOG.md. Same team; same repo; same prompt.)

## Hour 12:00 — Hour-12 handoff stand-up (UTC YYYY-MM-DDTHH:MM)

[Full template per Lecture 1 §2.6. The 3-question round, the MUST-status
table read aloud, the Builder Lead rotation (4-person teams), the team-
health midpoint check, the day-2 plan, the scribe.]

---

## Hour HH:MM — [event name] (UTC ...)

[Each named event during hours 12-24 gets its own heading and entry.
Entries can be:
  - Stand-up notes
  - Merge log entries (one per merge to main)
  - Pivot conversation log (even if "no pivot")
  - Demo cut log (at hour 18)
  - Dress rehearsal take notes
  - Submission package commit notes
  - Conflict log entries (with the intervention sentence and resolution)
  - Free-form log entries the team chooses to write (rare; usually
    the structured entries above are enough)]

---

## Hour 24:00 — Hour-24 retrospective (UTC ...)

[Full retro template per Lecture 3 §5.6. The team-health one-word check,
the KEPT round (4 items), the CHANGED round (4 items), the DROPPED round
(4 items), the follow-up issue title and scope, the scribe, the time
spent.]

---

*Day-2 log closes here. The follow-up issue is filed in the repo within
24 hours of the retro.*
```

## The `SUBMISSION.md` template

Use the full template from Lecture 3 §3.2. Commit it to the repo root with a link from the README.

## The minimum entries

The `DAY-2-LOG.md` must include, at minimum:

- 1 hour-12 stand-up entry.
- 1 pivot conversation entry (even if the decision is "no pivot" or "no pivot conversation surfaced; the team noted there was no need at hour 14").
- 1+ merge log entries (one per merge to main during hours 12-24).
- 1 demo cut entry (hour 18; even if the decision is "no cuts; all SHOULDs/COULDs shipped or were dropped earlier").
- 1+ dress rehearsal take notes (at minimum: take 1 + take 2 + the final decision).
- 1 submission package commit note.
- 1 stop-work declaration (hour 23).
- 1 hour-24 retro entry.

Total minimum entries: 9. Most teams' logs will have 12-20 entries (each conflict, each MUST-status change, each stand-up that surfaces something noteworthy gets an entry).

## The deliverable

By Sunday evening:

1. **`DAY-2-LOG.md`** committed to the repo. Minimum 9 entries; minimum 200 lines of markdown.
2. **`SUBMISSION.md`** committed to the repo. Full 6-section template. 400-600 words.
3. **3-minute demo video** published on a free host. URL pasted into `SUBMISSION.md` section 5.
4. **The repo's README** updated (the hour-22 README pass per Lecture 3 §3.3).
5. **One follow-up issue** filed in the repo, labelled `retro-followup`, with the title + 2-sentence scope + 3-item acceptance checklist. Filed within 24 hours of the hour-24 retro (i.e., by Monday end-of-day for a Sunday retro).

## The acceptance criteria

The mini-project is accepted if all five deliverables are committed/filed and at least 9 of the following 12 quality criteria are satisfied. The optional Challenge 1 lifts the bar from 9/12 to 12/12.

```
1. The hour-12 stand-up entry contains all six segments (or five on a 3-person team).
2. The MUST-status table read aloud at hour 12 has all 3 status values used correctly (DONE/IN PR/NOT STARTED).
3. Any pivot conversation logged completed within 15 minutes (the "time spent" line documents).
4. Every merge to main has a log entry with the §2.4 template.
5. Every merge to main has a commit message following the §2.3 template.
6. Every PR merged was <=200 lines (or the over-cap was logged with rationale).
7. The hour-18 demo cut entry (if cut occurred) applied the 3-line checklist.
8. The dress rehearsal had at least 2 takes; the take comparison sheet is in the log.
9. The demo video was recorded against the live deploy URL (not localhost).
10. SUBMISSION.md has all 6 sections and is 400-600 words.
11. The retro entry has 4 KEPT, 4 CHANGED, and 4 DROPPED items; team-health words are not "fine" or "good".
12. The follow-up issue is filed with a concrete title, a 2-sentence scope, and an acceptance checklist.
```

## What the dry-run measures

The dry-run does *not* measure whether the team won, or whether the demo is polished, or whether the build is impressive. It measures:

- **Whether the team ran the closing protocols at the named hours.** Hour-12 stand-up at hour 12 ± 30 min; demo cut at hour 18 ± 30 min; dress rehearsal at hour 20 ± 30 min; submission at hour 22 ± 30 min; retro at hour 24 ± 30 min.
- **Whether the team's log is honest.** A log that names the conflicts (rewriting fight, silent stalemate, attrition silence) scores higher than a log that pretends the team flowed.
- **Whether the team filed the follow-up issue.** A filed, labelled, concrete issue is the carry-out; absence of an issue is a failed dry-run regardless of how clean the rest looked.

## Facilitator notes (for the C4 cohort coordinator)

The cohort coordinator reads this section; learners can skip it.

### What to watch for during a team's day-2

The facilitator's job during day 2 is *light-touch observation*, not coaching. Three things to watch:

- **The hour-12 stand-up timestamp.** If a team is starting their hour-12 stand-up at hour 13:15, the dry-run has already slipped. Ask the Comms Lead, in DM, "you are running late on the hour-12 stand-up; what is the gating issue?" — surface the slip; do not intervene.
- **The hour-18 cut decision.** If a team is *not* having a cut conversation at hour 18, the team is either (a) genuinely on track with all MUSTs and SHOULDs shipping, or (b) avoiding the conversation. Ask the Builder Lead at hour 18:15, in DM, "is the team having a cut conversation, or are all SHOULDs shipping?" — the question surfaces the avoidance pattern.
- **The retro's KEPT-vs-CHANGED ratio.** A retro with 4 KEPT and 4 CHANGED and 4 DROPPED is honest. A retro with 4 KEPT and 1 CHANGED and 0 DROPPED is the team writing the retro they wish they had. The facilitator's review note can be one sentence: "the retro is light on DROPPED items; consider whether the dry-run actually had no drops."

### What not to do

- Do not enter the team's call uninvited during day 2. The team's dynamics are part of what the dry-run measures.
- Do not provide a sample answer for the cut decision. The team must own the cut.
- Do not file the follow-up issue for the team. The team files it; the facilitator may comment on the issue afterwards.

### Sample event-team Slack scripts

A cohort coordinator running a multi-team dry-run uses these scripted Slack messages to coordinate across teams. Each script is paste-and-edit; the bracketed fields are team-specific.

**Pre-dry-run notice (Friday morning):**

```
:wave: Team-mode dry-run starts tomorrow.

Per the Week-7 setup, the dry-run starts at [HH:MM UTC] on Saturday and
ends at the same time on Sunday. Week 8's continuation is hours 12-24
of the same window.

What to have ready by Friday end-of-day:
  - DAY-1-LOG.md from Week 7 committed.
  - The same repo as Week 7.
  - The same team (or a logged drop if someone left).
  - The 4-hour Saturday + 4-hour Sunday windows blocked on calendars.
  - The hour-12 stand-up agenda pinned in the team channel.

I am on-call Saturday 8am-10pm UTC and Sunday 8am-10pm UTC. I will not
enter your team calls; ping me in DM if you hit a blocker.

DROP-AND-RECOVER protocol: if a teammate drops mid-dry-run, log the
drop in DAY-1-LOG.md or DAY-2-LOG.md with a timestamp, and continue
with the remaining team. The continuation does not require a full team
restart.

Good luck.
```

**Hour-12 check-in (Sunday 12pm if the dry-run started Saturday 12am):**

```
:bell: hour-12 marker.

If your team has not held the hour-12 handoff stand-up by hour 12:30,
please ping me in DM with the gating issue. The handoff stand-up is
the discipline anchor for day 2; teams that skip it usually do not
ship the demo at hour 20.

The dry-run measurement (per Week-8 README) is about the *protocol
discipline*, not the build polish. The retro at hour 24 measures
whether you ran the protocols, not whether you won the prompt.
```

**Hour-18 check-in (Sunday 6pm):**

```
:bell: hour-18 marker.

If your team is having a demo cut conversation right now, you are on
schedule. If your team is not having one because everything shipped,
you are on schedule. If your team is avoiding a conversation that
needs to happen, the dry-run's retro at hour 24 will surface the
avoidance — better to face it now.

Reminder: the demo cut is bounded at 15 minutes by the cap. Use a
timer. The Comms Lead runs the cap.
```

**Hour-22 check-in (Sunday 10pm):**

```
:bell: hour-22 marker — submission window.

By hour 22:30, the SUBMISSION.md should be in the repo and the demo
video URL should be in your team channel. By hour 23:00, the stop-
work rule is in effect — no commits, no edits, no re-shoots.

Then rest. Then retro at hour 24.

I'll check the cohort's repos at hour 22:45 to confirm the submission
packages are committed. Ping me if you need a 30-minute extension; we
do not extend past hour 23:30 in the dry-run.
```

**Post-retro follow-up (Monday morning):**

```
:wave: Day-2 retros are committed. The follow-up issues are due in
the repo by Monday end-of-day.

I will read each retro this week and post one comment per retro in
the repo's issue tracker. The comment is feedback, not grading; the
dry-run is graded by the team's own measurement, not by me.

The Week 9 lectures pick up from here; Week 9 takes the recorded
demo and rehearses live judging. Bring the follow-up-issue habit
into Week 9 — Week 9's mini-project is a live pitch, and the same
follow-up-issue mechanism applies to that rehearsal too.

Good work this weekend.
```

### Sample conflict-resolution rubric for facilitator interventions

If a team escalates a conflict to the facilitator during day 2 (rare; the team's own Comms Lead is the first line of defense), use the following rubric to decide whether to intervene and how:

```
Step 1 — Did the team apply the 4-step intervention pattern themselves?
         (Surface without blame; offer paths; give the affected party
          choice; log resolution.)
         If yes → ask which step is not working. Do not impose; help
                  the team unblock that specific step.
         If no  → recommend the team's Comms Lead run the 4-step
                  pattern. Do not run it for them.

Step 2 — Is the conflict task/process or relationship?
         Task/process → the team owns it; facilitator stays out.
         Relationship → the facilitator may DM the affected teammate
                        privately to confirm safety; the MLH Code of
                        Conduct is the floor.

Step 3 — Is anyone's well-being at risk?
         If yes → leave the dry-run pattern; engage the team's
                  cohort coordinator and any campus mental-health
                  resource as appropriate.
         If no  → step 4.

Step 4 — Time-box the facilitator's involvement at 10 minutes.
         Longer involvement turns the dry-run into a guided exercise,
         not a rehearsal. The team must own the resolution.

Final note: the dry-run is a rehearsal. A team that experiences a real
relationship conflict in the dry-run is *better off* having it now,
under a facilitator's lens, than at a real event. The facilitator's
silence after step 4 is part of the rehearsal.
```

## Why this mini-project

Week 7 taught the team to start. This week the team learns to finish. The two are different muscles; the dry-run rehearses both in sequence so that, at a real event, the team's body knows the rhythm before the brain re-derives it.

A team that finishes the Week 8 mini-project with a clean log and a filed follow-up issue has the *infrastructure of a closing*. Week 9 builds on that infrastructure; Week 10 builds on Week 9's. The cumulative effect is a team that can ship a clean 24-hour event at a real hackathon — which is the point of the whole track.

> **C4 voice:** the dry-run was a rehearsal. The retro is the lesson. The follow-up issue is the discipline carried forward. Three artifacts; one team; twelve hours of practice. The real event uses the same protocols, at the same hours, with the same templates. The dry-run is the bench; the real event is the band; the discipline is the same in both rooms.

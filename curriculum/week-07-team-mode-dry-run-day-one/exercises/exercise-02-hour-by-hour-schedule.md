# Exercise 2 — Hour-by-Hour Schedule from a Written Prompt

> **Time:** ~45 minutes.
> **When in the week:** Friday morning.
> **Deliverable:** `EXERCISE-02-SCHEDULE.md` committed to your week-7 working folder.
> **Prerequisite:** Lecture 2 read; Exercise 1 complete.

## What this exercise is

You will take a fake event prompt and produce a *printable hour-by-hour schedule* for the team's first 24 hours. The schedule is the kind of document the real Comms Lead pins as message 5 in the team channel at hour 0:50 of the kickoff (Lecture 2 §5.3).

The exercise rehearses two muscles:

- **Reading a prompt and extracting a schedule.** Most prompts are 200-400 words; the schedule extracts the *scheduled events* (start, judging, submission) and slots the team's named events (kickoff, scope pass, stand-ups, close-out) around them.
- **Translating tracks into time.** Lecture 2's three-track parallelization is abstract; the schedule makes it concrete. The build track has named work blocks; the design+demo track has named milestones; the comms+log track has named log-entry timestamps.

## The fake event prompt

Use this prompt verbatim.

```
HACK-FOR-CIVICS 2026 — 24-hour theme hackathon

Event start: Saturday 09:00 ET (2026-XX-XX).
Event end: Sunday 09:00 ET (2026-XX-XX).
Judging window: Sunday 10:00-12:00 ET.
Final submission deadline: Sunday 09:00 ET (1 hour before judging).

Theme: "Local government transparency."

Teams of 2-4 ship a working web prototype that helps a specific local
constituency (residents of one named city, members of one named board,
attendees of one named public meeting) interact with a public-data
artifact (a meeting agenda, a budget line, a vote record, a permit
application).

Allowed: any free / open-source tool; any free hosting tier; any third-
party API with a free tier.

Submission requirements:
  - A public GitHub repo URL with README and license.
  - A live deploy URL.
  - A 3-minute demo video URL (YouTube unlisted or equivalent).
  - A 200-word "civic impact" paragraph in the README.

Judging: 40% demo, 30% civic impact, 20% technical execution,
10% repo hygiene.
```

The prompt is the input. Your schedule is the output.

## The team

Same fake team as Exercise 1 — Pat (frontend), Sam (design+copy), Jordan (backend+infra), Alex (generalist). Pat is Builder Lead; Sam is Demo Lead; Jordan is Comms Lead; Alex is Floating Builder.

## The schedule template

The schedule has six sections. Use the template; do not invent your own structure.

### Section 1 — Event-level timestamps

The fixed timestamps the prompt names.

```markdown
## 1. Event-level timestamps
- Event start: Saturday 09:00 ET
- Final submission deadline: Sunday 09:00 ET
- Judging window: Sunday 10:00-12:00 ET
- Event end: Sunday 09:00 ET (build window closes; judging follows)
```

Four bullets. Copy from the prompt.

### Section 2 — Team-level named events

The kickoff, scope pass, three stand-ups, recording, and close-out. Times in the team's local zone (ET for this exercise).

```markdown
## 2. Team-level named events (ET)
- Hour 0:00 — Saturday 09:00 — Kickoff (60 min)
- Hour 1:00 — Saturday 10:00 — First actions per role (60 min)
- Hour 2:00 — Saturday 11:00 — Formal scope pass (30 min)
- Hour 4:00 — Saturday 13:00 — Stand-up 1 (10 min)
- Hour 12:00 — Saturday 21:00 — Stand-up 2 (10 min) + role rotation (if 4-person)
- Hour 14:00 — Saturday 23:00 — Sleep window begins
- Hour 18:00 — Sunday 03:00 — Sleep window ends; build sprint 5 begins
- Hour 22:00 — Sunday 07:00 — Stand-up 3 (10 min)
- Hour 22:10 — Sunday 07:10 — Demo rehearsal (recording take 1)
- Hour 23:30 — Sunday 08:30 — Demo recording (take 2 → final)
- Hour 23:55 — Sunday 08:55 — Submission upload to GitHub + Devpost
- Hour 24:00 — Sunday 09:00 — Close-out (30 min)
```

Twelve rows. Each row is one named event. The hour-NN-NN column maps to the local-clock column.

### Section 3 — Build track work blocks

The build track's named sprints. One sprint per row.

```markdown
## 3. Build track work blocks (Pat + Alex; Sam in low-design hours)
- Hour 2:30 — 4:00  Build sprint 1 (1h30): MUST 1 scaffolding (signup + post).
                    Owner: Pat. Floating Builder: Alex on user-story drafting.
- Hour 4:10 — 8:00  Build sprint 2 (3h50): MUST 1 done; MUST 2 starts.
                    Owner: Pat (MUST 1), Alex (MUST 2 backend scaffolding).
- Hour 8:00 — 10:00 Async / break / meal (2h). Build continues async on PRs.
- Hour 10:00 — 12:00 Build sprint 3 (2h): MUST 2 progress; MUST 3 design doc.
                     Owner: Alex (MUST 2), Pat (MUST 3 design).
- Hour 12:10 — 14:00 Build sprint 4 (1h50): MUST 2 done; MUST 3 starts.
                     Owner: Alex + Pat. Sam joins for landing-page copy.
- Hour 14:00 — 18:00 Sleep window. No synchronous build; async PRs OK.
- Hour 18:00 — 22:00 Build sprint 5 (4h): MUST 3 done; deploy stabilized.
                     Owner: Pat (fresh after sleep) takes over Builder Lead
                     duties from hour 12 rotation.
- Hour 22:10 — 23:30 No build (rehearsal window).
- Hour 23:30 — 24:00 No build (recording window).
```

Nine rows. Each row names the duration, the work, and the owner.

### Section 4 — Design+demo track milestones

The Demo Lead's track. One milestone per row.

```markdown
## 4. Design+demo track milestones (Sam)
- Hour 1:30 — first hook draft posted in #channel.
- Hour 2:30 — design seed for the post-card landing page (Figma export).
- Hour 4:00 — script outline (5 beats: hook, problem, solution, demo clip, ask).
- Hour 8:00 — screen-capture rough of MUST 1 on the deploy URL.
- Hour 12:00 — full script draft (one page, ~415 words) committed.
- Hour 14:00 — landing-page copy draft committed.
- Hour 18:00 — script v2 with team feedback applied.
- Hour 22:10 — recording rehearsal (take 1).
- Hour 23:00 — three-note review of take 1; script tweaks.
- Hour 23:30 — recording take 2 (final).
- Hour 23:55 — recording uploaded to YouTube unlisted; URL in README.
```

Eleven rows. Each row is a deliverable at a timestamp.

### Section 5 — Comms+log track entries

The Comms Lead's track. One log entry per row.

```markdown
## 5. Comms+log track entries (Jordan)
- Hour 0:55 — DAY-1-LOG.md hour-0 entry (kickoff agenda + role assignments).
- Hour 2:30 — DAY-1-LOG.md hour-2 entry (formal scope pass).
- Hour 4:10 — DAY-1-LOG.md hour-4 stand-up note (4 teammates × 3 questions).
- Hour 4:30 — channel-cleanup pass; pin updates.
- Hour 8:00 — async checkpoint post in #channel.
- Hour 12:10 — DAY-1-LOG.md hour-12 stand-up note + role-rotation entry.
- Hour 14:00 — sleep-window-start announcement; channel quiet hours.
- Hour 18:00 — sleep-window-end announcement; resume channel pings.
- Hour 22:10 — DAY-1-LOG.md hour-22 stand-up note.
- Hour 23:55 — submission-uploaded entry with repo + video URLs.
- Hour 24:30 — DAY-1-LOG.md close-out entry (3 outputs).
```

Eleven rows.

### Section 6 — Conflict-watch checkpoints

A short list of the *expected* conflict-surface points. Not all of these will fire; the schedule lists them so the Comms Lead is watching.

```markdown
## 6. Conflict-watch checkpoints
- Hour 4 (stand-up 1): silent-disagreement check — short-answer teammates DMed by Comms Lead.
- Hour 6-8: scope-creep watch — any SHOULD PRs that should be parked.
- Hour 12 (stand-up 2): role-overlap check — any decisions made in DMs since hour 4 that need re-posting.
- Hour 16-18: merge-fight watch — any PRs older than 60 minutes without review.
- Hour 20-22: scope-creep watch — last-mile feature additions; cut to SHOULD.
- Hour 22 (stand-up 3): demo-readiness conflict — script vs deploy mismatches.
```

Six rows. Each row names the timestamp and the conflict to watch for.

## Process

1. Open a new file: `exercise-02-schedule.md`.
2. Paste the six-section template.
3. Read the prompt twice — once silently, once aloud.
4. Fill in each section using the prompt's timestamps and the team's profiles.
5. Pin a mental copy of the schedule: at any random hour (say "hour 14"), what is the team doing? If you cannot answer in under 5 seconds, the schedule is not yet readable.
6. Commit.

## Acceptance checklist

- [ ] Section 1 has the four event-level timestamps copied verbatim from the prompt.
- [ ] Section 2 has 12 named team-level events with hour-NN-NN and local-time columns matching.
- [ ] Section 3 has 9 build-track rows; each row has a duration, work description, and named owner.
- [ ] Section 4 has 11 design+demo milestones; each has a timestamp and a named deliverable.
- [ ] Section 5 has 11 comms+log entries; each has a timestamp and a named log action.
- [ ] Section 6 has 6 conflict-watch checkpoints; each has a timestamp and a named conflict.
- [ ] You can answer "what is the team doing at hour 14?" in under 5 seconds without re-reading the file.
- [ ] You can answer "what is the team doing at hour 22?" in under 5 seconds.
- [ ] You can answer "what is the team doing at hour 8?" in under 5 seconds.
- [ ] The schedule does not contain a single block longer than 4 hours without a named check-in.
- [ ] The sleep window is 4 hours and is named (not implied).
- [ ] The submission deadline (hour 23:55) is *before* the prompt's deadline (Sunday 09:00 ET).

## Common failure modes

- **The single-track schedule.** Section 3 (build) is detailed; sections 4 and 5 (design+demo, comms+log) are stubs. The schedule is a build-only document; the other two tracks have no time. The dry-run team will produce a beautiful build with no demo and no log. *Fix:* fill sections 4 and 5 to the same depth as section 3.
- **The optimistic schedule.** Every block is the *minimum* time the work could take. The schedule has no buffer; the first 30-minute over-run cascades through every later block. *Fix:* add a 30-minute buffer at hour 22 before rehearsal. The buffer is named — "hour 21:30-22:00: deploy stabilization, buffer." If unused, the team starts rehearsal early.
- **The missing sleep window.** The schedule lists 24 continuous hours of synchronous work. *Fix:* add the 4-hour sleep window between hour 14 and hour 18. The window is not a suggestion.
- **The unnamed handoff.** Hour 8:00-10:00 is "async / break" with no specifics. *Fix:* name what each teammate does in the window. "Pat: rest. Sam: lunch + landing-page copy draft. Jordan: log catch-up. Alex: continue MUST 2 backend async."
- **The end-of-event compression.** Hours 22-24 are 90 minutes of rehearsal, recording, and submission — with no buffer if the rehearsal surfaces a script bug. *Fix:* the rehearsal is hour 22:10-23:30 (80 minutes); the recording is hour 23:30-23:55 (25 minutes); the upload is hour 23:55-24:00 (5 minutes). The compression has *two* buffers — the rehearsal's last 30 minutes and the recording's last 5 minutes.

## What to do with the deliverable

The deliverable is the *Friday-morning rehearsal*. On Saturday at hour 0:50 of the real dry-run, the Comms Lead will produce a fresh schedule (mini-project), using this template, with real timestamps. The Friday version is the practice; the Saturday version is the artifact.

The schedule is *not* a contract — the real team will adjust the timestamps to their actual time zones and energy. The template is the contract; the timestamps are flexible. Practice the template until the timestamps come fast.

## Up next

Continue to [Exercise 3 — Conflict-intervention drill](./exercise-03-conflict-intervention-drill.md).

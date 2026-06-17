# Mini-Project — A 4-Hour Mock Hackathon at Home

> **Time:** 4 wall-clock hours of synchronous work, with a 2-4 person team.
> **When in the week:** Saturday or Sunday.
> **Deliverable:** a committed `DAY-1-LOG.md` in a public GitHub repo, with timestamped entries for the kickoff, the scope pass, the mid-event check, the close-out, and the demo recording.
> **Prerequisite:** all three lectures read, all three exercises complete, quiz at 9/10 or better.

## What this mini-project is

You will run a *compressed* dry-run — a 4-hour mock hackathon at home — with at least one other human. The full 24-hour dry-run is the gold standard; the 4-hour version is the *minimum viable rehearsal* the week's curriculum guarantees. Both are acceptable deliverables.

If you can run the 24-hour version with a team of 2-4 (this is the recommended path, named in the week's README), do that — the artifact is richer and the muscle is stronger. If you cannot — because of teammate availability, time zones, or the calendar — run the 4-hour version as a *strict compression* of the same artifacts.

The compression rule: every named event in the 24-hour schedule (kickoff, scope pass, stand-ups, close-out, recording) happens in the 4-hour version, at compressed timestamps. The artifact list is identical; the only thing that shrinks is the build window.

## Why the 4-hour compression works

Three reasons:

- **The muscles being built are coordination, not endurance.** The dry-run rehearses the kickoff (60 min in 24h; 30 min in 4h), the stand-up cadence (3 in 24h; 2 in 4h), and the close-out (30 min in 24h; 15 min in 4h). The muscles are the same; the duration of the build between events is the only variable.
- **A 4-hour event is a real hackathon format.** Hour-long and 4-hour mini-hackathons exist (FIU-hosted "build sprints," GitHub Universe's mini-events, club-level "midnight hacks"). The 4-hour artifact is portable to those real events.
- **The 4-hour version surfaces 80% of the same conflicts as the 24-hour version.** Scope creep happens at hour 1 of a 4-hour event, hour 8 of a 24-hour event. Role overlap happens at hour 2 of a 4-hour event, hour 16 of a 24-hour event. The fraction of the build at which the conflict surfaces is roughly constant; the wall-clock changes.

The 4-hour version is *not* easier than the 24-hour version. It is a different shape of difficulty — the same coordination challenges, compressed.

## The compressed schedule

```
┌────────────────────────────────────────────────────────────────┐
│  THE 4-HOUR MOCK HACKATHON — COMPRESSED SCHEDULE               │
│                                                                │
│  Hour 0:00 — 0:30  Kickoff (compressed: 30 min, 6 segments)    │
│  Hour 0:30 — 0:45  Formal scope pass (15 min)                  │
│  Hour 0:45 — 1:30  Build sprint 1 (MUST 1)                     │
│  Hour 1:30 — 1:40  Stand-up 1 (10 min)                         │
│  Hour 1:40 — 2:30  Build sprint 2 (MUST 1 done; MUST 2 starts) │
│  Hour 2:30 — 3:00  Async / break (30 min)                      │
│  Hour 3:00 — 3:10  Stand-up 2 (10 min)                         │
│  Hour 3:10 — 3:30  Build sprint 3 (MUST 2 done; demo prep)     │
│  Hour 3:30 — 3:50  Demo recording (3-min demo, 1-2 takes)      │
│  Hour 3:50 — 4:00  Close-out (10 min, 3 outputs)               │
└────────────────────────────────────────────────────────────────┘
```

Four hours. Two stand-ups (not three; the 4-hour version cuts the midpoint stand-up to a single mid-event check). One scope pass. One demo recording. One close-out. All named; all log-entry'd.

### Mapping to the 24-hour version

| 24-hour event | 4-hour compressed equivalent | Compression ratio |
|---------------|------------------------------|--------------------|
| Kickoff (60 min) | Kickoff (30 min) | 2x |
| Scope pass (30 min) | Scope pass (15 min) | 2x |
| Stand-up 1 (10 min at hour 4) | Stand-up 1 (10 min at hour 1:30) | identical |
| Stand-up 2 (10 min at hour 12) | Stand-up 2 (10 min at hour 3:00) | identical |
| Stand-up 3 (10 min at hour 22) | (absorbed into demo prep) | n/a |
| Build sprints (~18h) | Build sprints (~2.5h) | 7x |
| Recording (30 min) | Recording (20 min) | 1.5x |
| Close-out (30 min) | Close-out (10 min) | 3x |

The build window is the most-compressed. The named events shrink by 1.5x-3x; the build window shrinks by 7x. The compression is on the *work*, not the *coordination*.

## The fake prompt

Use this prompt verbatim. The prompt is short, deliberately scoped to a 2.5-hour build window.

```
MOCK-CRUNCH-7 — 4-hour mini-hackathon

Theme: "One-page tools."

In 4 hours, your team ships a single-page web tool that helps a
specific user group do a specific named task in under 30 seconds.

Examples (do NOT pick one of these; invent your own):
  - A page that lets a freshman convert their dorm address into a
    one-tap rideshare destination.
  - A page that lets a band attendee see the set time of their
    favorite act at a fake fictional 12-band festival.
  - A page that lets a tutor see which student needs them most
    right now from a fake queue.

Allowed: any free / open-source tool; any free hosting tier;
  any AI API with a free trial that does not require a credit
  card. localStorage is allowed; a JSON file in the repo as a
  fake database is allowed; a real database is overkill for
  4 hours.

Submission requirements:
  - A public GitHub repo URL with a README.
  - A live deploy URL (Vercel, Netlify, GitHub Pages, Render
    static — any free static host).
  - A 3-minute demo video URL (Loom, YouTube unlisted).
  - A committed DAY-1-LOG.md.
```

The prompt is intentionally narrow. The 2.5-hour build window will not support a multi-page tool or a real backend. The one-page-tool constraint is the *forcing function*.

## The team

Recruit 1 to 3 other humans for a 2-, 3-, or 4-person team.

### How to recruit (in order of preference)

1. **A C4 cohort-mate.** The cohort coordinator can pair you in the C4 channel; one message asking "anyone free for a 4-hour mini-hackathon on Saturday afternoon?" usually finds 1-2 takers.
2. **A classmate or club-mate.** A friend at gdgatfiu, swiftclubatfiu, ColorStack, CAHSI, Hack University, or Upsilon Phi Epsilon. The shared org context means they already know the C4 voice.
3. **A coding friend outside the cohort.** A friend who codes but is not in C4. Brief them on the 4-hour schedule before hour 0; expect a 5-minute onboarding overhead.
4. **A family member or roommate who codes.** A sibling, parent, or roommate who can spend 4 hours coding with you. The relationship is fine; the coordination muscles are the same.

If after 48 hours of trying you cannot recruit a teammate, the C4 fallback is the **paired-cohort dry-run** — the cohort coordinator pairs you with another cohort learner who is in the same fallback. The coordinator's pairing call goes out every Friday for the cohort.

### What to brief the team on (before hour 0)

Send a 3-paragraph brief to the team 24-48 hours before the dry-run:

- **Paragraph 1:** the prompt above (copy-paste).
- **Paragraph 2:** the 4-hour schedule (copy-paste from this README).
- **Paragraph 3:** the artifact list (kickoff log entry, scope pass, two stand-up notes, close-out, demo recording — committed to a shared public repo). Plus the link to Lectures 1, 2, and 3 of this week for context.

The brief is the *pre-read*. A team that arrives at hour 0 having read the brief runs a clean kickoff; a team that arrives without it spends 10 of the 30 kickoff minutes on context.

## The four artifacts you commit

1. **`DAY-1-LOG.md`** — the audit trail.
2. **`SCOPING-WORKSHEET.md`** — the team's MUST list (3 items in the 4-hour version; some teams cut to 2).
3. **`TEAM-CONTRACT.md`** — the team's working agreement (compressed; the Friday Exercise 1 draft is the starting point).
4. **A 3-minute demo recording** — a Loom URL or YouTube unlisted link in the repo README.

All four committed to one public GitHub repo. The repo is the deliverable for the week.

## The `DAY-1-LOG.md` template (4-hour version)

```markdown
# DAY-1-LOG.md — Team [name]

## Hour 0:00 — Kickoff (UTC YYYY-MM-DDTHH:MM)

**Team:** [name]
**Members:** [list with roles]
**Prompt:** Mock-Crunch-7 one-page tools.
**First-pass MUST list:**
  1. [verb]
  2. [verb]
  3. [verb]
**Comms norms set:** [one channel, one doc, two-stand-up cadence, DM rule]
**Start-coding timestamp:** [HH:MM]
**Next event:** Stand-up 1 at [HH:MM + 1:30].

## Hour 0:45 — Formal scope pass complete (UTC YYYY-MM-DDTHH:MM)

**MUST list (final, 3 items):**
  1. [verb] (Owner: [name])
  2. [verb] (Owner: [name])
  3. [verb] (Owner: [name])

**SHOULDs (cut from union list):** [...]
**Done-rows committed in SCOPING-WORKSHEET.md.**
**Next event:** Stand-up 1 at hour 1:30.

## Hour 1:30 — Stand-up 1 (UTC YYYY-MM-DDTHH:MM)

[teammate-by-teammate three-question answers]

**Cross-track:** [...]

## Hour 3:00 — Stand-up 2 (UTC YYYY-MM-DDTHH:MM)

[teammate-by-teammate three-question answers]

**Cross-track:** [...]
**Demo-readiness check:** [Y/N — MUST list status; deploy URL status]

[ANY CONFLICT MOMENTS GET LOGGED HERE AS THEY HAPPEN]

### Hour HH:MM — [Conflict type] (UTC ...)
**Trigger:** ...
**Affected:** ...
**Intervention (Comms Lead):** "..."
**Resolution:** ...
**Follow-up:** ...

## Hour 3:50 — Demo recorded (UTC YYYY-MM-DDTHH:MM)

**Take count:** [1, 2, or 3]
**Final take URL:** [Loom / YouTube unlisted URL]
**Script source:** [link to SCRIPT-DRAFT.md or in-line]

## Hour 4:00 — Close-out (UTC YYYY-MM-DDTHH:MM)

**MUSTs shipped:**
  - MUST 1 ([verb]): YES / NO. [evidence sentence]
  - MUST 2 ([verb]): YES / NO. [evidence sentence]
  - MUST 3 ([verb]): YES / NO. [evidence sentence]

**Day-2 plan (first 3 items, if this were a 24h event):**
  1. [...]
  2. [...]
  3. [...]

**Team-health words:**
  - [teammate 1]: [word]
  - [teammate 2]: [word]
  - [teammate 3]: [word]
  - [teammate 4]: [word, if 4-person]

**Recording link:** [URL]
**Repo link:** [URL]
**Dry-run complete.**
```

The template is the *spine*. The Comms Lead fills it in as the dry-run happens. By hour 4:10 the file is committed.

## Process

### Pre-dry-run (Thursday or Friday)

1. Recruit the team (1-3 other humans).
2. Pick a 4-hour window on Saturday or Sunday. Block it on calendars.
3. Send the 3-paragraph brief to the team 24 hours before hour 0.
4. Create the GitHub repo (private or public). Add all teammates as collaborators. Confirm everyone can push.
5. Pick the chat tool (Slack / Discord / a group chat). Pick the doc tool (Google Doc / repo `.md` files). Pick the video-call tool (Meet / Discord / Zoom). One of each.
6. Set up GitHub Projects or a Markdown checklist in the repo for the MUST list. Three columns: TODO / DOING / DONE.

### Hour 0 — Kickoff (30 minutes)

The compressed kickoff. Six segments, 5 minutes each.

```
[ 0:00 — 0:05 ] Introductions (2 sentences per teammate)
[ 0:05 — 0:10 ] Prompt reading (aloud, by Builder Lead-elect)
[ 0:10 — 0:15 ] Role assignment (fit grid filled live)
[ 0:15 — 0:20 ] Scope pass first-pass (3 MUSTs named)
[ 0:20 — 0:25 ] Comms norms pinned (4 pins in channel)
[ 0:25 — 0:30 ] "We start coding at" handoff + hour-0 log entry
```

The Comms Lead writes the hour-0 log entry live during segment 6.

### Hour 0:30 — Formal scope pass (15 minutes)

Compressed from the 30-minute version. Three segments, 5 minutes each.

```
[ 0:00 — 0:05 ] Union list (each teammate names their MUST 3 in chat)
[ 0:05 — 0:10 ] Intersection cut (Builder Lead facilitates)
[ 0:10 — 0:15 ] Owner-per-MUST + done-row + log entry
```

The Comms Lead writes the hour-0:45 log entry live.

### Hour 0:45 — 1:30 — Build sprint 1

Forty-five minutes of synchronous build work. The build track scaffolds MUST 1; the design+demo track drafts the hook; the comms+log track monitors the channel.

### Hour 1:30 — Stand-up 1 (10 minutes)

Three questions, 2 minutes per teammate, 10 minutes total. The Comms Lead writes the log entry live.

### Hour 1:40 — 2:30 — Build sprint 2

Fifty minutes. MUST 1 done; MUST 2 starts. Cross-track handoffs as needed.

### Hour 2:30 — 3:00 — Async / break

Thirty minutes. Teammates step away from the call. The build can continue async on PRs; the team is not required to be synchronous. The break is the *recovery* before the second sprint.

### Hour 3:00 — Stand-up 2 (10 minutes)

The midpoint check. Three questions plus the demo-readiness check ("MUST 2 done? Deploy URL stable? Script ready to record?"). The Comms Lead writes the log entry live.

### Hour 3:10 — 3:30 — Build sprint 3

Twenty minutes. MUST 2 must be done by 3:30 (or cut to SHOULD on the spot). The deploy URL stabilizes. The demo script is final.

### Hour 3:30 — 3:50 — Demo recording

Twenty minutes. The Demo Lead records the 3-minute demo on the live URL. Two takes typical; the second take is the artifact. The recording is uploaded to Loom or YouTube unlisted by 3:50.

### Hour 3:50 — 4:00 — Close-out (10 minutes)

The compressed close-out. Three outputs in 10 minutes.

```
[ 0:00 — 0:03 ] MUSTs shipped Y/N per MUST
[ 0:03 — 0:07 ] Day-2 plan (3 bullets)
[ 0:07 — 0:10 ] Team-health one-word check + final log entry
```

The Comms Lead writes the hour-4 close-out entry live and commits the final `DAY-1-LOG.md`.

## Acceptance criteria

The mini-project is *complete* if all of the following are true.

- [ ] The repo is public on GitHub.
- [ ] The repo has a README naming the team, the prompt, the live deploy URL, and the demo recording URL.
- [ ] The repo has `DAY-1-LOG.md` committed with the full template filled in.
- [ ] The repo has `SCOPING-WORKSHEET.md` committed with 3 MUSTs, owners, and done-rows.
- [ ] The repo has `TEAM-CONTRACT.md` committed with the 9 sections from Exercise 1.
- [ ] The live deploy URL is reachable from a phone browser.
- [ ] The 3-minute demo recording is uploaded to a public host (Loom, YouTube unlisted, Vimeo, or a direct `.mp4` in the repo).
- [ ] At least one teammate (not you) is a named contributor in the repo's commit history or in the `DAY-1-LOG.md` as a co-author.
- [ ] The log entries are timestamped in UTC + local time.
- [ ] The close-out log entry names the team-health word for every teammate.

If any box is unchecked, the mini-project is *incomplete* — fix the gap before continuing to Week 8. The most common gap is the missing teammate (the dry-run was solo or with a teammate who did not appear in the commit history). The fix is recruiting and re-running a 2-hour mini-dry-run with one other human to produce a co-authored log.

## Honesty rule

The log is honest. If MUST 3 was cut, the log says so. If a teammate missed the stand-up, the log says so. If a conflict was surfaced and resolved, the log captures the intervention sentence and the resolution. If a conflict was surfaced and *not* resolved, the log captures *that* — "intervention attempted; team chose to continue without resolution; revisit at close-out."

The Week 8 retrospective uses the log as primary input. A dishonest log produces a fictional retrospective; a fictional retrospective produces a fictional Week-8 plan. The honesty is the *value*, not the polish.

## Common failure modes

Five patterns the cohort tends to fall into during the 4-hour mock. Recognize them in your own run.

- **The skipped kickoff.** The team "just gets going" without the 30-minute kickoff. By hour 1 the team has no roles, no MUSTs, no comms norms. The log's hour-0 entry is fabricated at hour 4. *Fix:* the kickoff is non-optional. Even if all teammates have done dry-runs before, the 30 minutes is the team's *first 30 minutes of working together*. Run it.
- **The over-scoped MUST list.** The team agrees on 3 MUSTs that each take 90 minutes. The build window is 2.5 hours; the team finishes one MUST. *Fix:* the hour-2 (or hour-0:45 in the compressed version) scope pass *cuts* aggressively. Two MUSTs is a respectable 4-hour outcome; three is the stretch.
- **The silent build.** The team breaks into individual work after the kickoff and does not check in until hour 3. The stand-up at hour 1:30 happens, but the log entry shows everyone "in flow, no block" — the stand-up was a formality. *Fix:* the Comms Lead's enforcement of the cadence is the *value* of the role. The stand-up surfaces blocks even when teammates do not feel blocked.
- **The skipped close-out.** The team finishes the recording at hour 3:55 and disbands; the close-out is "we'll do it async later." *Fix:* the close-out is *synchronous and on the call*. Ten minutes; three outputs. The team-health word is *not* a Slack message; it is said aloud.
- **The solo recording.** The Demo Lead records the demo alone at hour 3:30 while the rest of the team is "on standby." The recording lands; the team did not see it. *Fix:* the Demo Lead records *with the team on the call* (muted). One take with team-on-call is stronger than three takes alone. The team sees what the recording shows; the Demo Lead gets the team's three-note feedback for take 2.

## What to do with the deliverable

The deliverable goes into the Week 8 retrospective. Week 8 starts by *reading the dry-run's `DAY-1-LOG.md` aloud* to the cohort coach (or in a self-review session if no coach is available). The reading is the *first input* of the next lecture. The dry-run's log is the bridge between Week 7 (day 1) and Week 8 (day 2).

The artifact is *also* portable. If you participate in a real 4-hour mini-hackathon at FIU, at HackUniversity, or at any local university event in the next 6 months, the same template runs. The dry-run is the rehearsal; the real event is the run; the artifact format is the *same*.

---

*The win is shipping. You have shipped one alone. You have shipped one with a team. The next 17 weeks of the cohort are about shipping again — more times, with more teams, at more events. The dry-run's log is your audit trail; the audit trail compounds across the course.*

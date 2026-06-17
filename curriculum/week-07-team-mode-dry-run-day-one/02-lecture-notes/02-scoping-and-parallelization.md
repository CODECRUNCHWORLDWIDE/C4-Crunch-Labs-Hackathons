# Lecture 2 — Scoping and Parallelization

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can re-run the Week-5 scoping worksheet as a *team* artifact at hour 2 of the dry-run, with every teammate having read the MUST list aloud and approved it. You can plan a three-track parallelization (build / design+demo / comms+log) with named track owners. You can defend the 30-minute block rule. You can read a printable hour-by-hour schedule for hours 0 through 24 and locate any named event on it in under 5 seconds. You can recognize the three most common scope failures during a 24-hour build — silent scope creep, lopsided MUST, and the unowned track — and the one-sentence fix for each.

If you only remember one sentence from this lecture, remember this:

> **A 24-hour team build is three parallel tracks, three MUST items, and three stand-ups. Anything that does not fit on one of the three tracks does not get worked on until hour 24; anything past three MUST items gets cut to SHOULD; any track that blocks another for more than 30 minutes triggers an escalation. The arithmetic is intentional and unforgiving.**

Lecture 1 taught you the kickoff — *who* runs the team and *how* the meeting that starts the team is timed. Lecture 2 teaches you the *work itself* — *what* the team builds, *how* the work is split across people in parallel, and *when* each named event happens on the wall-clock between hour 0 and hour 24. The kickoff is the commit point; the scoping and parallelization are the *plan of work* the kickoff commits to.

---

## 1. Why scoping for a team is a different skill from solo scoping

Week 5 taught you solo scoping. The MoSCoW worksheet, the prompt sentence, the demo-ability checklist, the three MUST items. The artifact is `SCOPING-WORKSHEET.md`. Solo scoping is *self-discipline*: you write what you would build and you cut what you cannot finish.

Team scoping is *negotiation*. Three or four people each have a *different* sense of what the build should be. The MUST list is the *intersection* of their intents, not the union. The hour-2 scope pass is the meeting that finds the intersection.

> **C4 voice:** solo scoping fails when the builder is too ambitious. Team scoping fails when the team is too polite. The polite team accepts the union of every member's "I really want to build X" — three teammates each wanting a different MUST 4 produces a worksheet with six MUSTs and a Sunday hour-22 panic. Politeness is not the value; the discipline is.

### 1.1 The intersection-not-union rule

```
┌────────────────────────────────────────────────────────────┐
│  THE INTERSECTION-NOT-UNION RULE                           │
│                                                            │
│  Solo MUST list  = what you would build.                   │
│  Union MUST list = sum of each teammate's "I want to       │
│                    build X" answers. Always too long.      │
│  Intersection    = the items every teammate would build    │
│  MUST list         if forced to pick three. Always right.  │
└────────────────────────────────────────────────────────────┘
```

The hour-2 scope pass is the conversion from union to intersection. The Builder Lead facilitates; the Comms Lead writes the worksheet; every teammate confirms each MUST aloud.

### 1.2 The four reasons solo and team scoping differ

Four short sentences, one per reason:

- **Different teammates have different skill profiles.** A MUST that depends on real-time WebSockets is reasonable if Pat has shipped a WebSocket app before; risky if nobody on the team has. Team scoping reads the MUST against the *team's* aggregate skills, not against any one teammate's.
- **Different teammates have different definitions of "done."** Pat's "done" is a deploy URL that handles the happy path. Sam's "done" includes a 404 page and a loading state. Jordan's "done" includes a CI pipeline. Team scoping defines "done" *per MUST*, in the worksheet's done-row, before the build starts.
- **Different teammates work at different paces.** A MUST that takes Pat 4 hours might take Alex 7 hours. Team scoping assigns each MUST to a teammate with the matching pace, and tracks the assignment in the worksheet's owner-row.
- **Different teammates have different stamina.** A 24-hour build has at least one sleep cycle per teammate. The MUST list cannot assume all teammates are working all hours; the scope must fit the *available* hours per teammate, not the nominal 24.

The hour-2 scope pass surfaces all four differences. Solo scoping does not.

---

## 2. The hour-2 scope pass

The hour-2 scope pass is a *30-minute meeting* run by the Builder Lead. It happens at hour 2:00 of the dry-run; the kickoff is at hour 0:00–1:00; the team has spent hour 1:00–2:00 on the four first-actions from segment 6 of the kickoff. Hour 2:00 is when the team re-convenes for the formal scope pass.

### 2.1 The four-segment scope-pass agenda

```
┌────────────────────────────────────────────────────────────┐
│  THE 30-MINUTE SCOPE PASS — 4 SEGMENTS                     │
│                                                            │
│  [ 0:00 — 0:05 ] First-pass MUST list re-read aloud        │
│  [ 0:05 — 0:15 ] Union list (every teammate's "I want X")  │
│  [ 0:15 — 0:25 ] Intersection: cut union to 3 MUSTs        │
│  [ 0:25 — 0:30 ] Owner-per-MUST + done-row + log entry     │
└────────────────────────────────────────────────────────────┘
```

Thirty minutes. Four segments. The output is the committed `SCOPING-WORKSHEET.md` with three MUSTs, three SHOULDs, three COULDs, an owner per MUST, a done-row per MUST, and a paragraph at the top explaining the cut.

### 2.2 Segment 1 — Re-read aloud (0:00 — 0:05)

The Builder Lead reads the first-pass MUST list from segment 4 of the kickoff. Three sentences. Five minutes is generous; the first three teammates raising hands "I would re-state this as..." is fine. The re-read is not a re-vote; it is a *refresh*.

### 2.3 Segment 2 — Union list (0:05 — 0:15)

Each teammate writes (in chat or in the shared doc) *their* MUST list — what they would build, if forced to pick three. Two minutes of writing per teammate; on a 4-person team, the segment finishes at 0:08 (writing in parallel). The team then has 7 minutes to *read* each list aloud.

The Comms Lead captures the union in the worksheet, with a name next to each item:

```
Union list (hour 2:08):
  - Pat:    1. signup + post  2. peer reply  3. real-time push notify
  - Sam:    1. signup + post  2. peer reply  3. design polish on the post card
  - Jordan: 1. signup + post  2. peer reply  3. moderation flag
  - Alex:   1. signup + post  2. peer reply  3. analytics dashboard
```

Four teammates; ten items; six unique items (signup, post, reply, push, polish, moderation, analytics). The union is twice as long as the MUST list. Segment 3 cuts it down.

### 2.4 Segment 3 — Intersection cut (0:15 — 0:25)

The Builder Lead facilitates the cut. Three rules:

- **Items every teammate listed go in.** "Signup + post" (4 of 4) and "peer reply" (4 of 4) are *in* — they are the kernel.
- **Items one or two teammates listed go to SHOULD or COULD.** "Real-time push" (1 of 4), "design polish" (1), "moderation" (1), "analytics" (1) are *out of MUST*. They are SHOULDs at best.
- **The third MUST is decided by the team in 5 minutes.** Two MUSTs are clear from the intersection; the third is *negotiated*. The negotiation rule: pick the item that *most enables the demo*. "Real-time push" enables the demo clip ("she gets the reply in real time on her phone"); the team picks it as MUST 3.

```
Final MUST list (hour 2:24):
  MUST 1: a freshman signs up and posts a question.        Owner: Pat.
  MUST 2: a peer sees the question and types a reply.      Owner: Sam.
  MUST 3: the freshman sees the reply in real time on her  Owner: Pat + Alex.
          phone.
```

Three MUSTs. Three owners (one MUST is shared between Pat and Alex because it spans frontend and backend). Each owner says "yes I own this" aloud; silence is not assent.

### 2.5 Segment 4 — Owner-per-MUST, done-row, log entry (0:25 — 0:30)

For each MUST, the team writes one *done-row*: a one-sentence definition of "this MUST is done." The done-row is the cell the build track checks against before merging.

```
MUST 1 done-row: "A new visitor to the deploy URL can create
  an account in <30s and post a question that appears in the
  feed within 5s of submission."

MUST 2 done-row: "A signed-in visitor sees the feed of open
  questions, taps reply on any question, types a reply in a
  text box, and submits — the reply appears under the
  question for the original poster within 5s."

MUST 3 done-row: "The original poster's browser tab on a
  separate device (phone) shows the new reply within 10s of
  submission without a manual refresh."
```

Three done-rows. The done-row is the *acceptance test* for the MUST. The Builder Lead does not merge a PR for MUST N unless the done-row for MUST N is satisfied on the deploy URL.

The Comms Lead's last action in segment 4 is to write the hour-2 log entry:

```markdown
## Hour 2:30 — Formal scope pass complete (UTC YYYY-MM-DDTHH:MM)

**MUST list (3 items, intersection of team union list):**
  1. Signup + post (Owner: Pat)
  2. Peer reply (Owner: Sam)
  3. Real-time push notify (Owner: Pat + Alex)

**SHOULDs (cut from union list):** design polish, moderation flag, analytics dashboard.
**COULDs:** see worksheet section 4.

**Done-rows committed in SCOPING-WORKSHEET.md.**
**Next event:** Stand-up 1 at hour 4:00. Build track begins immediately.
```

The scope pass is *closed* at hour 2:30. The team has 1 hour 30 minutes before stand-up 1; the build track is live.

---

## 3. The three-track parallelization model

A team of 3 or 4 working in parallel is *three tracks*, not four (or however many teammates). The tracks are functional, not per-person. A 4-person team has one teammate floating across tracks; a 3-person team has one teammate per track exactly.

### 3.1 The three tracks

```
┌────────────────────────────────────────────────────────────┐
│  THE THREE TRACKS                                          │
│                                                            │
│  BUILD TRACK                                               │
│    Owner: Builder Lead. (Floating Builder on 4-person.)    │
│    Inputs: MUST list, deploy URL, repo.                    │
│    Output: the deploy URL satisfies the done-rows by       │
│            hour 22.                                        │
│                                                            │
│  DESIGN + DEMO TRACK                                       │
│    Owner: Demo Lead.                                       │
│    Inputs: MUST list, hook draft, recording tool.          │
│    Output: a 3-minute demo script by hour 12 and a         │
│            recorded take by hour 24.                       │
│                                                            │
│  COMMS + LOG TRACK                                         │
│    Owner: Comms Lead.                                      │
│    Inputs: chat channel, log file, stand-up cadence.       │
│    Output: a committed DAY-1-LOG.md with an entry for      │
│            every named event.                              │
└────────────────────────────────────────────────────────────┘
```

Three tracks. One owner per track. The owner is the *decider* on the track, not the *only doer*. The Builder Lead decides what merges to main; other teammates push commits to feature branches that the Builder Lead reviews and merges.

### 3.2 Why three tracks and not five

Four short sentences, one per reason:

- **Three tracks fit one person's monitoring capacity.** The team has *one* shared call running in the background; the Comms Lead monitors three tracks across that call. Five tracks need a meta-coordinator, and the dry-run does not have one.
- **Three tracks map to three deliverables.** The deploy URL (build), the demo recording (demo), the log (log). Each track has one named artifact at hour 24; the artifact is the track's exit criterion.
- **Three tracks match the three roles.** One Builder Lead owns build; one Demo Lead owns design+demo; one Comms Lead owns comms+log. Roles and tracks are the same abstraction at different scopes.
- **Three tracks compress to a 30-second status check.** "Build: deploy URL up, MUST 1 done, MUST 2 in PR. Demo: script draft committed, hook approved. Log: hour-12 stand-up note committed." Three sentences; one per track. A team that cannot say its status in three sentences is over-parallelized.

### 3.3 The build track's sub-structure

The build track is the *broadest* of the three; it usually has 2 or 3 teammates on it (the Builder Lead, the Floating Builder if any, and a part-time contributor from the Demo Lead in low-design hours). The track has three sub-deliverables, one per MUST:

```
Build track sub-deliverables:
  MUST 1 deliverable: feature branch -> PR -> merge -> deploy. Owner: Pat.
  MUST 2 deliverable: feature branch -> PR -> merge -> deploy. Owner: Sam.
  MUST 3 deliverable: feature branch -> PR -> merge -> deploy. Owner: Pat + Alex.
```

The PR cadence is the *unit*. The build track does not "work on MUST 1 until done, then start MUST 2"; the build track has 2 or 3 PRs *in flight in parallel*. The Builder Lead merges them in MUST-order at hour 4, hour 12, and hour 20.

### 3.4 The design+demo track's sub-structure

The design+demo track has two sub-deliverables in parallel:

```
Design+demo track sub-deliverables:
  Hook draft: written by hour 2:30, pinned in #channel by hour 4.
  Script draft: written by hour 12, reviewed at stand-up 2.
  Recording take 1: by hour 22 (against the live deploy URL).
  Recording take 2: by hour 24 (after take-1 watch + 3 notes).
```

Four sub-deliverables; one teammate's full track. The Demo Lead does not write code in their primary hours; they write the script, run the recording rehearsals, and capture the demo at hour 24.

On low-design hours (hour 8 to hour 12, while the build is mid-MUST-1), the Demo Lead may pick up *one* build task — a UI polish PR, a copy-edit, a screen-recordable seed-data dataset. The picking-up is decided by the Builder Lead's call ("we need a hand on the post-card layout") and limited to *one* PR.

### 3.5 The comms+log track's sub-structure

The comms+log track is the *narrowest* of the three; the Comms Lead owns it alone in most teams. The track has four sub-deliverables:

```
Comms+log track sub-deliverables:
  Hour-0 log entry (kickoff): by hour 0:55.
  Hour-2 log entry (scope pass): by hour 2:30.
  Stand-up notes for hours 4, 12, 22: by 10 minutes after each stand-up.
  Hour-24 log entry (close-out): by hour 24:30.
```

Plus continuous duties: monitoring the channel, enforcing the DM-vs-channel rule, pinning new important messages, and capturing any *named conflict moment* as a one-paragraph log entry as it happens.

The Comms Lead is the most *async* of the three roles — their work is short bursts of writing across the 24 hours, not long stretches of focus. They are the team's *backstop* on tooling, channel hygiene, and the audit trail.

---

## 4. The 30-minute block rule

Three tracks running in parallel will *block each other*. The Build track needs a copy block from the Demo track; the Demo track needs a data seed from the Build track; the Comms track needs a stand-up time confirmed by the Build track. Blocks are *normal*. Long blocks are the failure.

### 4.1 The rule statement

```
┌────────────────────────────────────────────────────────────┐
│  THE 30-MINUTE BLOCK RULE                                  │
│                                                            │
│  No track waits on another for more than 30 minutes        │
│  between hour 4 and hour 22.                               │
│                                                            │
│  If a block exceeds 30 minutes, the blocked track          │
│  EITHER switches to its next-priority work item            │
│  OR escalates to the Builder Lead.                         │
│                                                            │
│  The escalation triggers a 5-minute "unblock huddle"       │
│  on the team call.                                         │
└────────────────────────────────────────────────────────────┘
```

Thirty minutes. The threshold is mechanical; the escalation is one-sentence.

### 4.2 Why 30 minutes and not 15 or 60

Four short sentences:

- **15 minutes is too tight to escalate every micro-block.** A teammate steps away to fill water and the block clock is at 5 minutes; escalating at 15 means a call every 30 minutes for the rest of the day. Burnout.
- **60 minutes is too loose to surface blockers.** A teammate blocked for 60 minutes has lost a quarter of a 4-hour work block; the surface comes at stand-up 2 (hour 12) when it should have come at hour 5.
- **30 minutes maps to one Pomodoro.** One focused work block is ~25-30 minutes. If a teammate finishes a Pomodoro and is still blocked at the start of the next one, that is the natural escalation moment.
- **30 minutes is the band of typical async response.** A DM sent to a teammate gets a reply in 5-30 minutes during the dry-run's active hours. If the DM has gone unanswered for 30 minutes, the answer is not coming async; switch to voice.

### 4.3 The "switch or escalate" protocol

When a track hits the 30-minute mark blocked:

1. **First option — switch to the next MUST item.** If the build track is blocked on MUST 1's design copy and MUST 2's backend is ready to scaffold, switch to MUST 2. The block on MUST 1 unblocks itself when the design copy arrives; the team does not lose 30 minutes.
2. **Second option — switch to a SHOULD or COULD.** If there is no next MUST to switch to (all three are blocked on the same dependency), the blocked teammate switches to a SHOULD item for at most 1 hour. SHOULDs are buffer work, not primary work; an hour on a SHOULD is acceptable, three hours is not.
3. **Third option — escalate to the Builder Lead.** A one-sentence message in #channel: "MUST 1 has been blocked on design copy for 30 minutes; switching to MUST 2 unsafe because of merge order. Escalating for a 5-minute huddle." The Builder Lead pings the team call; the huddle is *5 minutes*, not 30; the output is a decision (deliver the copy now, merge MUST 2 anyway, or cut MUST 1 to SHOULD).

The Comms Lead logs the escalation as a *named conflict moment* in `DAY-1-LOG.md`. The log entry is one paragraph; the resolution is one sentence.

### 4.4 The three most common block scenarios

Three predictable blocks during a 24-hour build:

- **The dependency block.** Build A is blocked on Build B because B's API contract has not been agreed. *Fix:* the Builder Lead writes the API contract as a 10-line note in the channel; both teammates work against the contract; the contract is the *interface*, not the implementation. Time to fix: 15 minutes.
- **The merge-conflict block.** Two PRs touch the same file; the second PR's rebase produces conflicts. *Fix:* the Builder Lead pairs with the second PR's owner on a 15-minute fix-conflicts session, voice on. The other teammates continue their tracks. Time to fix: 15 minutes.
- **The infrastructure block.** The deploy is down; the database is unreachable; the third-party API is rate-limiting. *Fix:* the Builder Lead names the block in #channel, sets a 30-minute fix-timer, and if the block is not resolved at the timer's end, the team falls back to the most-recent working deploy and cuts the affected MUST to SHOULD. Time to fix: up to 30 minutes.

The blocks are not *exceptional*; they are routine. The protocol is the discipline that prevents a routine block from eating 3 hours.

---

## 5. The hour-by-hour schedule

The dry-run's 24 hours are *named*. Each hour has either a *scheduled event* (kickoff, scope pass, stand-up, close-out) or a *track work block* (build, design+demo, comms+log). The Comms Lead pins the schedule in the channel.

### 5.1 The full schedule

```
┌──────────────────────────────────────────────────────────────────────┐
│  THE 24-HOUR SCHEDULE — DAY 1 OF THE DRY-RUN                         │
│                                                                      │
│  Hour 0:00 — 1:00  Kickoff (60 min, 6 segments)                      │
│  Hour 1:00 — 2:00  First actions per role                            │
│  Hour 2:00 — 2:30  Formal scope pass                                 │
│  Hour 2:30 — 4:00  Build sprint 1 (MUST 1 scaffolding)               │
│  Hour 4:00 — 4:10  Stand-up 1 (3-question check, 10 min cap)         │
│  Hour 4:10 — 8:00  Build sprint 2 (MUST 1 done, MUST 2 starts)       │
│  Hour 8:00 — 10:00 Async / break / individual meal                   │
│  Hour 10:00 — 12:00 Build sprint 3 (MUST 2 progress; demo script draft) │
│  Hour 12:00 — 12:10 Stand-up 2 (3-question check, role rotation if 4) │
│  Hour 12:10 — 14:00 Build sprint 4 (MUST 2 done; MUST 3 starts)      │
│  Hour 14:00 — 18:00 Async / sleep window                             │
│  Hour 18:00 — 22:00 Build sprint 5 (MUST 3 done; deploy stabilized)  │
│  Hour 22:00 — 22:10 Stand-up 3 (3-question check, demo readiness)    │
│  Hour 22:10 — 23:30 Demo rehearsal (recording take 1)                │
│  Hour 23:30 — 24:00 Demo recording (take 2 → final)                  │
│  Hour 24:00 — 24:30 Close-out (30 min retrospective)                 │
└──────────────────────────────────────────────────────────────────────┘
```

Twenty-four hours. Named segments. Six synchronous segments (kickoff, scope pass, three stand-ups, close-out) totaling about 2 hours; eighteen hours of build work; four hours of async/sleep window. The team can shift the async windows to match their time zones; the *named events* are the structural commitments.

### 5.2 The "sleep window" is not optional

A 24-hour build with no sleep window produces a worse outcome than a 24-hour build with a 4-hour sleep window. Three reasons:

- **The merge fight at hour 18.** Two exhausted teammates argue about a merge that, fresh, they would have solved in 5 minutes. The exhausted merge takes 60 minutes and produces a bug that costs another 30 minutes at hour 22.
- **The demo-clip line at hour 24.** A teammate recording the demo clip after 24 hours straight will deliver a tired narration that re-records badly. A teammate who slept 4 hours delivers a take 1 that lands in 2 takes instead of 4.
- **The Code of Conduct.** Sleep deprivation degrades behavior. A fresh team enforces the CoC on itself; an exhausted team picks at each other in #channel. The sleep window is a CoC mechanism, not just a productivity one.

The sleep window is *scheduled*. The team agrees on the window at the kickoff (segment 5 or 6), pins it in the channel, and the Comms Lead does not ping anyone in the window. The async build continues — PRs can be opened, the deploy can be rebuilding — but no synchronous decisions happen.

### 5.3 The pinned schedule message

The Comms Lead pins the schedule as a fifth pinned message in the team channel during segment 5 of the kickoff:

```
Pin 5: the 24-hour schedule
"Schedule: kickoff (0-1), scope pass (2-2:30), build sprints
 with stand-ups at 4 / 12 / 22, async window 8-10 and 14-18,
 demo rehearsal 22:10-23:30, recording 23:30-24, close-out
 24:00-24:30. Adjust times to team's local zone; named events
 are fixed."
```

Five pins total. The schedule pin is fifth because it depends on the timestamps decided in segment 6.

---

## 6. The three scope failure modes

Three predictable failures of the team scope, surfacing between hour 2 and hour 22.

### 6.1 Silent scope creep

> **Symptom:** at stand-up 2 (hour 12), MUST 2 is "almost done" but a SHOULD item ("design polish on the post card") has been merged.

The build track quietly absorbed a SHOULD because the teammate working on MUST 2 had 30 minutes free and "polished the card while waiting." The polish took 90 minutes instead of 30 and MUST 2 is now behind schedule.

The fix: the Builder Lead's standing rule — *no SHOULD or COULD merges to main before all MUSTs satisfy their done-rows*. SHOULDs go to a feature branch; the merge waits for hour 18. The Builder Lead enforces this at PR review. The Comms Lead surfaces silent scope creep at stand-up 2 with one question: "Are any SHOULDs merged that we agreed to defer?"

### 6.2 Lopsided MUST

> **Symptom:** MUST 3 is 4x the work of MUST 1 or MUST 2.

The team agreed on three MUSTs in the scope pass, but MUST 3 — "real-time push" — turns out to require WebSockets, a deployed server with a persistent connection, and a phone-side notification system that none of the teammates have shipped before. MUST 3 alone consumes hour 12 to hour 22.

The fix: the *done-row test* applied at stand-up 1. Each owner reads the done-row aloud and estimates the hours to completion. If any MUST estimates to more than 8 hours, the team *re-scopes* — MUST 3 might become "real-time poll-every-2-seconds refresh," which lowers the technical bar from WebSockets to a setInterval. The re-scope at hour 4 saves the demo at hour 24.

### 6.3 The unowned track

> **Symptom:** at stand-up 2, the comms+log track has no entries since hour 4.

The Comms Lead has been pulled into the build track to help with MUST 2. The log file has not been updated. The stand-up notes from hour 4 are not in the log. The channel has 40 messages with no decisions captured.

The fix: the Builder Lead's standing rule — *the Comms Lead's primary track is comms+log; they help build only at the Builder Lead's explicit ask*. The fix at stand-up 2 is to send the Comms Lead back to the log track for hour 12:10 to 14:00 and *catch up the log*. The catch-up is *required*; the team's audit trail is the artifact, and a half-written log is no log.

---

## 7. The hour-2 worksheet template

The hour-2 `SCOPING-WORKSHEET.md` extends the Week-5 template. Same six sections; team-mode amendments noted below.

```markdown
# SCOPING-WORKSHEET.md — Team [Crunch-7-A]

## 1. Prompt sentence
[user] can [verb] to [relieve / enable] [outcome].

## 2. MoSCoW worksheet (team-mode)
| Priority | Item | Owner | Done-row | Hours est. |
|----------|------|-------|----------|------------|
| MUST     | Signup + post | Pat | A new visitor signs up in <30s... | 4 |
| MUST     | Peer reply | Sam | A signed-in visitor replies to a question... | 4 |
| MUST     | Real-time push | Pat + Alex | Original poster sees reply within 10s without refresh... | 8 |
| SHOULD   | Design polish | Sam | Post card has consistent typography... | 3 |
| SHOULD   | Moderation flag | Jordan | Any user can flag a post... | 2 |
| SHOULD   | Empty-feed state | Alex | Feed shows seeded data when empty... | 1 |
| COULD    | Analytics dashboard | --- | Admin sees a count of posts/replies... | 4 |
| COULD    | Dark mode | --- | UI toggles light/dark... | 2 |
| COULD    | Push to native iOS | --- | Native iOS app pushes notifications... | 12 |

## 3. Demo-ability checklist (team-mode)
- [ ] The deploy URL is reachable from a phone browser.
- [ ] Seeded data is committed so the empty-feed state never appears on first load.
- [ ] MUST 1's done-row passes on the deploy URL by hour 8.
- [ ] MUST 2's done-row passes on the deploy URL by hour 14.
- [ ] MUST 3's done-row passes on the deploy URL by hour 22.

## 4. Risk register (team-mode)
- Risk: real-time push depends on WebSockets which nobody has shipped before.
  Mitigation: poll-every-2s fallback ready by hour 8 if WebSockets fail.
- Risk: Pat is in a different time zone; sleep window is 02:00-06:00 local.
  Mitigation: Sam covers async build during the window.
- Risk: deploy URL down at hour 22 = no recording surface.
  Mitigation: hour 20 freeze on infrastructure changes; only feature merges after.

## 5. Track ownership
- Build track: Pat (Builder Lead), Alex (Floating Builder).
- Design+demo track: Sam (Demo Lead).
- Comms+log track: Jordan (Comms Lead).

## 6. Acceptance criteria for "scope is good"
- Every MUST has an owner.
- Every MUST has a done-row.
- Every MUST's hour estimate fits inside the build window (sum <22 hours).
- Every teammate has read the MUST list aloud and confirmed it.
- The Comms Lead has committed this file before stand-up 1.
```

The worksheet is the *contract* for the next 22 hours. Every stand-up references it. Every merge satisfies a done-row. Every cut is a row in the SHOULD or COULD column with a name and a date.

---

## 8. How scoping threads the kickoff and the stand-ups

The scope pass at hour 2 is the *middle* of three artifacts. The kickoff at hour 0 set the team and the first-pass MUSTs; the scope pass at hour 2 formalizes the MUSTs and the tracks; the stand-ups at hours 4, 12, and 22 *check* the scope and the tracks. Three artifacts; three checkpoints.

### 8.1 Thread 1: the kickoff's MUST list becomes the scope pass's MUST list

The kickoff's first-pass MUST list (segment 4) is the *draft*. The scope pass's intersection-cut MUST list is the *committed* version. The first-pass list might be wrong; the intersection cut is the team's authoritative version. The Comms Lead's hour-2 log entry names both — the first-pass version and the committed version — so the team's audit trail captures the cut.

### 8.2 Thread 2: the scope pass's tracks become the stand-up's status questions

Each stand-up's three questions (what shipped, what is blocking, what is the next 4 hours) are answered *per track*. The build track reports on MUST progress; the design+demo track reports on script and recording state; the comms+log track reports on log entries. Three tracks; three reports; one stand-up.

### 8.3 Thread 3: the worksheet's done-rows become the stand-up's merge-gate

A PR for MUST N does not merge unless the done-row for MUST N is satisfied on the deploy URL. The Builder Lead checks the done-row at PR review. The stand-up does *not* re-check every done-row — that is the Builder Lead's continuous work — but the stand-up *does* re-check the done-row of any MUST that the Builder Lead has flagged as "shipped." A teammate's "MUST 1 shipped" is verified against the done-row in 60 seconds at the stand-up.

---

## 9. Scoping is half the artifact

The other half is the *parallel work itself*. Lecture 3 covers the team's communication norms during the parallel work — the channel rules, the DM rules, the stand-up cadence, and the four named conflicts that the parallel work surfaces. The scoping is the plan; the comms norms are the *enactment* of the plan under pressure.

The scope is what you would build. The track is who builds it. The schedule is when. The stand-up is the check. The log is the record. Five abstractions; one 24-hour window.

---

## 10. Recap

- Team scoping is *intersection-not-union*: the MUST list is the items every teammate would build, not the sum of each teammate's preferences. The hour-2 scope pass converts union to intersection in 30 minutes.
- The three-track parallelization model: build track (Builder Lead), design+demo track (Demo Lead), comms+log track (Comms Lead). Three tracks; three deciders; three deliverables.
- The 30-minute block rule: no track waits on another for more than 30 minutes between hour 4 and hour 22. The protocol is switch or escalate; the escalation is a 5-minute unblock huddle.
- The 24-hour schedule has six named synchronous events (kickoff, scope pass, three stand-ups, close-out) totaling ~2 hours, plus ~18 hours of build work and ~4 hours of async/sleep window.
- The sleep window is not optional. A team that skips sleep produces a worse hour-24 demo than a team with 4 hours of scheduled rest.
- Three scope failure modes: silent scope creep, lopsided MUST, unowned track. One fix per mode.
- The hour-2 `SCOPING-WORKSHEET.md` extends the Week-5 template with owners, done-rows, hour estimates, a risk register, and a track-ownership section.
- The kickoff, the scope pass, and the stand-ups are three checkpoints on the same plan. The artifact threads them; the Comms Lead's log records the threads.

Continue to [Lecture 3 — Comms Norms and Fixing Conflict](./03-comms-norms-and-fixing-conflict.md), where the team learns the communication norms that hold a 24-hour build under pressure, the three-question stand-up template, and the four day-1 conflicts that derail a clean dry-run — each with a one-sentence intervention.

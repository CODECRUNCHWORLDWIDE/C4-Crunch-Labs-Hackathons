# Lecture 3 — Dress Rehearsal, Submission, and Retro

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can run the hour-20 dress rehearsal as a two-take recording against the live deploy URL, with named roles during the recording (director, operator, audience proxy). You can package the hour-22 submission with the five required artifacts and a `SUBMISSION.md` cover sheet. You can run the hour-24 retrospective as a 30-minute meeting using the kept/changed/dropped template and file the follow-up issue within 24 hours.

If you only remember one sentence from this lecture, remember this:

> **The dress rehearsal makes the demo. The submission package puts the demo in front of judges. The retrospective turns the dry-run into a lesson. The team that finishes all three at the named hours has done a clean hackathon close; the team that skips any of them has a build but no event.**

Lectures 1 and 2 took the team from the hour-12 handoff through the integration window and the hour-18 demo cut. Lecture 3 picks up at hour 20 — the build is closing, the script is final, the team is tired and proud and uncertain in roughly equal measure — and runs through the last four hours: dress rehearsal (section 2), submission package (section 3), the stop-work rule (section 4), the retrospective (section 5), and the three remaining day-2 conflict patterns (section 6). Section 7 is the lecture's recap; section 8 connects to Week 9.

---

## 1. Why the closing four hours have their own skill

Hours 0-20 of the dry-run produced a build. Hours 20-24 produce *what the judges see*. The two are not the same artifact.

A judge at a real hackathon does not read the team's source code. The judge reads the project description on Devpost, watches the 3-minute demo video, clicks the live deploy URL for 60 seconds, and forms an opinion. Total judge attention per project: roughly 4-6 minutes. The team's 24 hours of build distill into 4-6 minutes of judge attention.

The closing four hours of the dry-run are where the distillation happens. Three skills, each named:

- **The dress rehearsal.** Hours 20-22 (roughly). The team's 3-minute demo is recorded, in front of a live deploy URL, with two takes minimum.
- **The submission package.** Hour 22. Five artifacts assembled: public repo URL, live deploy URL, demo video URL, `DAY-2-LOG.md` link, `SUBMISSION.md` cover sheet.
- **The retrospective.** Hour 24. Thirty minutes. Kept/changed/dropped. Follow-up issue filed.

The three skills are sequenced; the dress rehearsal cannot start before MUST 1-3 are merged, the submission package cannot close before the dress rehearsal produces a video, the retrospective cannot start before the submission is done. A team that runs them in order finishes at hour 24; a team that interleaves them stretches to hour 26 and misses the discipline.

### 1.1 What the closing four hours produce

Five outputs:

- **A 3-minute demo video.** Recorded against the live deploy URL. Two takes minimum. Published to a free host (YouTube unlisted, Loom free tier).
- **A `SUBMISSION.md` file in the repo.** Six sections. The cover sheet a judge would read first.
- **A clean README.** A pass through the repo's README to make it judge-readable (one-paragraph project description, what was built, what was cut, how to run locally, links to the demo).
- **A retrospective entry in `DAY-2-LOG.md`.** Thirty-minute meeting; three sections; one scribe; one team-health one-word check.
- **A follow-up issue filed in the repo.** One concrete change the team commits to for the next event. Filed within 24 hours.

All five together are the *closing package*. The retro names which of the five came easy and which came hard; the next dry-run inherits the lessons.

---

## 2. The dress rehearsal

The dress rehearsal is the team-mode version of the Week 6 solo recording. The structure is similar — a 3-minute script, a hook, three MUST beats, a close — but the team-mode version has three roles during the recording itself.

### 2.1 The three recording roles

```
┌────────────────────────────────────────────────────────────────────┐
│  THE DRESS REHEARSAL — RECORDING ROLES                              │
│                                                                    │
│  Director (Demo Lead)                                              │
│    — Calls "rolling." Calls "cut."                                 │
│    — Decides which take is the final.                              │
│    — Owns the script.                                              │
│                                                                    │
│  Operator (Builder Lead)                                           │
│    — Drives the screen during recording.                           │
│    — Clicks the live deploy URL features in script order.          │
│    — If a feature breaks mid-take, the operator decides whether   │
│      to keep rolling or call cut.                                  │
│                                                                    │
│  Audience proxy (Comms Lead)                                       │
│    — Watches the recording as if a judge.                          │
│    — Notes timestamps where the demo "loses" the audience.         │
│    — Vetoes the final take if the audience-proxy notes are bad.    │
└────────────────────────────────────────────────────────────────────┘
```

Three roles, distinct from the kickoff roles even though they map to the same people. The Demo Lead runs the script; the Builder Lead drives the build; the Comms Lead watches the recording with judge-empathy. The roles prevent the most common dress-rehearsal failure: the Builder Lead silently rewrites the script during the recording because they think a different click order is better.

### 2.2 The two-take minimum

The team records *at least two takes*. The first take is rough; it surfaces the click-order bugs, the script-pacing bugs, the audio-level bugs. The second take is the polish; it incorporates the first-take notes.

The audience proxy (Comms Lead) keeps a written take-comparison sheet:

```markdown
### Take 1 — recorded hour 20:15

- 0:00-0:10  Hook line 1 — Sam read slightly fast; otherwise clean.
- 0:10-0:25  Hook line 2 — clean.
- 0:25-0:45  MUST 1 demo — operator clicked the wrong nav link at 0:32;
             recovered in 4 seconds.
- 0:45-1:30  MUST 2 demo — clean; the seeded-data state worked.
- 1:30-2:15  MUST 3 demo — the polling fallback was visible but not
             named in the script; needs script addition.
- 2:15-2:50  Close — clean.
- 2:50-3:00  Buffer; Sam stuttered the URL.

Notes for take 2:
  - Pace hook line 1 slower (count 1-2 between sentences).
  - Operator: practice nav link order once before take.
  - Script: add "this is the 2-second polling fallback" to the MUST 3 beat.
  - Sam: read the URL slowly; consider showing it on screen.

### Take 2 — recorded hour 20:35

- 0:00-0:10  Hook line 1 — paced; clean.
- 0:10-0:25  Hook line 2 — clean.
- 0:25-0:45  MUST 1 demo — clean.
- 0:45-1:30  MUST 2 demo — clean.
- 1:30-2:15  MUST 3 demo — polling fallback named; clean.
- 2:15-2:50  Close — clean.
- 2:50-3:00  Buffer; URL on screen; clean.

Decision: Take 2 is the final.
```

Twenty-five lines. The take-comparison sheet is committed to the repo (the demo recording itself is on a video host; the sheet is in the repo so the team can study it).

### 2.3 The no-re-litigation rule

The dress rehearsal is *not* the place to re-debate the script, the hook, or which MUSTs to feature. The script was final at hour 18. The dress rehearsal records what the script says. If a teammate proposes a script change at hour 20, the Demo Lead has unilateral authority to say "no, the script is locked; we are recording it as written; we can file a follow-up issue if needed."

The rule prevents the common closing-stage failure: the team starts the dress rehearsal at hour 20, halfway through it someone says "wait, can we change the hook to mention X," and the rehearsal stalls for 40 minutes while the team re-litigates a decision that was made 2 hours ago. The 40 minutes pushes the recording into the submission window; the submission window pushes into the retro window; the retro is rushed; the dry-run closes badly.

> **C4 voice:** the script-lock at hour 18 is the discipline the dress rehearsal depends on. A team that does not lock the script at hour 18 is recording a draft, not a demo. The lock is the cost; the speed is the benefit.

### 2.4 Recording against the live deploy URL

The recording is *against the live deploy URL*, not localhost. The dress rehearsal at hour 20 verifies that:

- The deploy URL is responsive (load time <2 seconds).
- The MUST features work on the live URL (not just on the operator's localhost).
- The seeded data is present on the deploy (sometimes seeding scripts run only locally; the team checks).
- The browser console is clean of red errors (warnings are okay; errors are not).

If any of these fails, the team pauses the rehearsal and fixes the deploy. The pause cost is real (typically 15-45 minutes); the alternative — recording a localhost demo — is disallowed by Devpost and most MLH-affiliated event submission rules. The pause is non-negotiable.

### 2.5 The recording publish step

After the final take, the Demo Lead publishes the video. Three target hosts, in order of preference for the dry-run:

- **YouTube (unlisted).** Free, permanent link, supports timestamps in description. The default.
- **Loom (free tier).** Faster upload; 5-minute cap (well above the 3-minute demo); good if YouTube upload takes too long.
- **Direct host in the repo.** A `demo.mp4` committed to the repo. Discouraged because video files bloat the repo; allowed if the team has no other option.

The published URL goes in `SUBMISSION.md` and in `DAY-2-LOG.md`. The Comms Lead pins the URL in the team channel.

---

## 3. The submission package

The submission package is assembled at hour 22. Five artifacts, one cover sheet.

### 3.1 The five artifacts

```
1. Public GitHub repo URL.
   - Repo is public (not private).
   - README is judge-readable (see §3.3).
   - License file is present (MIT is the default for C4 builds).
   - CODE_OF_CONDUCT.md links to Contributor Covenant or MLH CoC.

2. Live deploy URL.
   - Responsive (load time <2 seconds).
   - HTTPS.
   - Browser console clean.

3. 3-minute demo video URL.
   - Published (YouTube unlisted, Loom, or other free host).
   - 3 minutes ± 10 seconds.
   - Recorded against the live deploy URL (per §2.4).

4. DAY-2-LOG.md link.
   - Committed to the repo.
   - Extends DAY-1-LOG.md with hours 12-24 entries.
   - Retro entry at the bottom (per §5).

5. SUBMISSION.md cover sheet.
   - Six sections (see §3.2).
   - One page (roughly 400-600 words).
   - Linked from the README.
```

Five artifacts. Each verifies the others. The submission cover sheet is what the judges read first; the README is what they read if they want more; the demo video is what they watch; the deploy URL is what they click; the log is what they read if they are curious about process.

### 3.2 The `SUBMISSION.md` cover sheet template

The cover sheet has six sections:

```markdown
# [Team name] — [Project name]

## 1. The prompt and our response

[2-3 sentences: which prompt the team responded to, and the one-sentence
project description.]

## 2. The team

| Name | Role | Solo contribution |
|------|------|-------------------|
| [name] | Builder Lead | [1-line summary] |
| [name] | Demo Lead | [1-line summary] |
| [name] | Comms Lead | [1-line summary] |
| [name] | Floating Builder | [1-line summary] |

## 3. What we shipped

The MUST list, with done-row status:

- MUST 1 — [name] — [DONE / IN PR / NOT STARTED]
- MUST 2 — [name] — [DONE / IN PR / NOT STARTED]
- MUST 3 — [name] — [DONE / IN PR / NOT STARTED]

[Optional: 1-2 sentences on what makes this build distinctive.]

## 4. What we cut

The SHOULD/COULD items, with cut status:

- SHOULD 1 — [name] — [SHIPPED / CUT at hour N]
- SHOULD 2 — [name] — [SHIPPED / CUT at hour N]
- COULD 1 — [name] — [SHIPPED / CUT at hour N]

[Optional: 1 sentence on the team's hour-18 cut conversation.]

## 5. Links

- **Live deploy:** [URL]
- **3-minute demo video:** [URL]
- **Source code:** [URL]
- **Day-1 log:** [URL to DAY-1-LOG.md]
- **Day-2 log:** [URL to DAY-2-LOG.md]

## 6. Demo video timestamps

For the judges' convenience:

- 0:00-0:25  Hook — [one-sentence summary]
- 0:25-0:45  MUST 1 — [one-sentence summary]
- 0:45-1:30  MUST 2 — [one-sentence summary]
- 1:30-2:15  MUST 3 — [one-sentence summary]
- 2:15-2:50  Close — [one-sentence summary]
- 2:50-3:00  Buffer

---

*Built during [event name] from [start time] to [end time].*
```

One page. Roughly 400-600 words. Judges read the cover sheet first; the cover sheet says what shipped, who shipped it, what was cut, where to find the artifacts, and what to look for in the video.

### 3.3 The README pass

The repo's README at hour 22 is *re-read with judge-empathy*. A good hour-22 README has:

- **A one-paragraph project description** at the top, above the fold.
- **A "what we built" section** with the MUST list and brief descriptions (sourced from `SUBMISSION.md` §3 but written in prose).
- **A "how to run locally" section** with 3-5 shell commands (`git clone`, `npm install`, `npm run dev`, deploy URL link).
- **A "links" section** with the deploy URL, demo video URL, and `SUBMISSION.md` link.
- **A footer** with the team names, the event name, and the date.

The README does not have to be beautiful. It has to be *legible to a judge who has 60 seconds*. The 60-second rule is the design constraint.

---

## 4. The stop-work rule

The submission is committed at hour 22. The team has 2 hours before the retro. The natural impulse during those 2 hours is to *keep polishing* — fix one more typo, re-shoot the demo, tweak the README copy.

C4's rule: *stop work at hour 23*. The submission is locked at hour 23; the team does not re-edit after.

### 4.1 Why the rule exists

Three reasons:

- **The team is exhausted.** Polish at hour 23 is more likely to introduce bugs than to remove them. The team's hour-23 cognitive state is worse than the team's hour-18 state; trusting the hour-23 self over the hour-22 self is a mistake.
- **The retro needs uncluttered hours 23-24.** A team that is still polishing at hour 23:55 cannot run a clean retro at hour 24. The retro is the lesson; cutting into the retro for last-minute polish trades a lesson for a typo fix.
- **The submission "freeze" rehearses a real-event submission cutoff.** Real events have hard submission deadlines; teams that miss the deadline are disqualified. The stop-work rule is the dry-run's equivalent.

### 4.2 What stop-work means concretely

- No new commits to main after hour 23.
- No edits to `SUBMISSION.md` after hour 23.
- No re-shoots of the demo after hour 23.
- No edits to the README after hour 23.

The team uses the hour-23-to-24 window for *rest*. Each teammate logs off, takes a 30-minute break, comes back for the retro at hour 24.

> **C4 voice:** the stop-work rule is harder than it sounds. The team's adrenaline at hour 23 wants to keep going. The discipline is to stop. The team that stops at hour 23 runs a retro that produces a lesson; the team that polishes through hour 23:55 produces nothing more than the polishing-team would have produced at hour 22:55.

---

## 5. The hour-24 retrospective

The retrospective is a 30-minute meeting at hour 24. It is the single most-important output of day 2. Without the retro, the dry-run is a build; with the retro, the dry-run is a *lesson*.

### 5.1 The 30-minute structure

```
┌────────────────────────────────────────────────────────────────────┐
│  THE HOUR-24 RETROSPECTIVE — 30 MINUTES                             │
│                                                                    │
│  [ 0:00 — 0:03 ]  Opening — the one-word team-health check         │
│  [ 0:03 — 0:13 ]  KEPT round (what worked; we keep doing this)     │
│  [ 0:13 — 0:23 ]  CHANGED round (what we changed mid-run; why)     │
│  [ 0:23 — 0:30 ]  DROPPED round (what we will not do next time)    │
│                                                                    │
│  Output 1: Retro entry in DAY-2-LOG.md (drafted during the meeting) │
│  Output 2: Follow-up issue filed in the repo within 24 hours       │
└────────────────────────────────────────────────────────────────────┘
```

Three sections after the opening. Each teammate contributes to each section. The scribe (Comms Lead) drafts the log entry during the meeting; the entry is committed before the meeting ends.

### 5.2 The one-word team-health check

Same rule as the hour-12 midpoint check (Lecture 1 §2.4). Each teammate says one word. "Fine" and "good" are rejected. Acceptable words at hour 24:

```
"relieved"        "proud"           "exhausted"
"frustrated"      "grateful"        "uncertain"
"satisfied"       "drained"         "energised"
```

The pattern across the four words is the retro's emotional baseline; the rest of the meeting reads against that baseline. A retro where three of four teammates say "drained" runs differently from a retro where three say "proud."

### 5.3 The KEPT round (10 minutes)

Each teammate names one thing that worked. The phrasing is *what worked, that we keep doing next time*. Examples from past cohort retros:

- "The hour-12 read-aloud MUST-status table — we caught the silent disagreement about MUST 2 at hour 12 instead of hour 18."
- "The pair-programming during the slump from hour 14-16 — we shipped MUST 2 cleanly because two pairs of eyes were on it."
- "The 30-minute branch-freeze rule — every merge had an actual review; nothing was rubber-stamped."
- "The stop-work rule at hour 23 — we ran a clean retro instead of polishing typos."

Four teammates × one item each = 4 KEPT items. The scribe writes each in the log.

### 5.4 The CHANGED round (10 minutes)

Each teammate names one thing the team *changed* during the run, and why. Examples:

- "We changed the demo script's hook line 2 at hour 18 because the seeded-data state told a different story than we expected — the change tightened the demo."
- "We changed the sleep window from a 4-hour-per-teammate block to a 4-hour staggered block at hour 14 because the all-nap-at-once mistake nearly happened — the change kept someone on call at all times."
- "We changed the MUST-3 implementation from real-time push to 2-second polling at hour 17 because the push integration was 90 minutes away from working — the change made the demo recordable at hour 20."

Four teammates × one item each = 4 CHANGED items. The scribe writes each in the log with the *why* attached.

### 5.5 The DROPPED round (7 minutes)

Each teammate names one thing they will *drop* for the next event. The phrasing is *what we did this time that we will not do next time*. Examples:

- "We started MUST 3 too late (hour 14 instead of hour 8). Next time, MUST 3 starts in parallel from hour 4."
- "Our PRs averaged 350 lines, twice the 200-line cap. Next time, we enforce the cap from hour 0."
- "Our hour-2 scope pass took 45 minutes instead of 30. Next time, the Comms Lead times the segments more strictly."
- "We argued about the framework choice for 20 minutes at hour 1. Next time, the kickoff names a default framework before any debate."

Four teammates × one item each = 4 DROPPED items. The scribe writes each. The DROPPED items become the follow-up issue's content.

### 5.6 The retro log entry template

```markdown
## Hour 24:00 — Hour-24 retrospective (UTC 2026-05-16T15:00)

**Duration:** 30 minutes (hour 24:00 to hour 24:30).
**Scribe:** Jordan.

**One-word team-health check:**
  - Pat: "relieved"
  - Sam: "proud"
  - Jordan: "exhausted"
  - Alex: "energised"

**KEPT (4 items):**
  - [Pat] The hour-12 read-aloud MUST-status table.
  - [Sam] The two-take dress rehearsal with audience-proxy notes.
  - [Jordan] The 30-minute branch-freeze before each merge.
  - [Alex] The stop-work rule at hour 23.

**CHANGED (4 items):**
  - [Pat] MUST-3 implementation: push → polling at hour 17 (build risk reason).
  - [Sam] Demo script hook line 2: rewritten at hour 18 (seeded-data discovery).
  - [Jordan] Sleep window: 4-hour block → 4-hour staggered at hour 14 (always-someone-on-call reason).
  - [Alex] Builder Lead rotation: skipped the planned hour-12 swap; we did a partial swap at hour 14 instead (Alex was not ready at hour 12).

**DROPPED (4 items, all become candidates for the follow-up issue):**
  - [Pat] MUST-3 starting late at hour 14; will start in parallel from hour 4 next time.
  - [Sam] PR sizes: averaged 350 lines, twice the 200-line cap; will enforce the cap from hour 0 next time.
  - [Jordan] Hour-2 scope pass: ran 45 minutes instead of 30; will time the segments more strictly next time.
  - [Alex] Framework debate at hour 1: 20 minutes spent; will name a default framework before debate in the kickoff agenda.

**Follow-up issue:**
Filed as issue #14 — "PR sizing: enforce 200-line cap from hour 0."
Scope: update bootstrap.sh to add a pre-push hook checking PR size; document
in TEAM-CONTRACT.md.

**Time spent:** 30 minutes (on the cap).
```

Forty lines. The retro log is the artifact; the follow-up issue is the *carry-out*.

### 5.7 The follow-up issue

One follow-up issue per retro. The issue is filed in the team's repo within 24 hours of the retro (so by the end of Monday for a Sunday retro). The issue:

- Has a clear title (e.g., "PR sizing: enforce 200-line cap from hour 0").
- Has a one-paragraph description connecting it to the retro's DROPPED list.
- Has a small, *concrete* scope (e.g., "update `bootstrap.sh`"; "add a paragraph to `TEAM-CONTRACT.md`"; "configure GitHub branch protection on main").
- Is labelled `retro-followup` so it is searchable.

One issue. Concrete. Filed within 24 hours. The single follow-up issue is the difference between a retro that taught the team something and a retro that produced four blog posts the team will not read again.

> **C4 voice:** the temptation at the retro is to file *every* DROPPED item as an issue. Resist. One concrete issue, filed and closed, builds a habit; four sprawling issues, half-filed and never closed, build resignation. Pick the most-impactful DROPPED item; file the issue; close it within a week. The next dry-run inherits the closure.

---

## 6. The three closing-stage conflict patterns

Lecture 2 covered four integration-stage conflict patterns (death-march, scope-creep, "I'll rewrite it," silent stalemate). Lecture 3 covers three more specific to the closing four hours.

### 6.1 The dress-rehearsal recording dispute

**Trigger:** Hour 20:30. The Demo Lead has called "take 2 is the final." The Builder Lead disagrees — they think take 1 was actually better and the team should re-record. The argument starts on the call.

**One-sentence intervention** (Comms Lead, addressed by name):
"Sam (Demo Lead) has unilateral authority on the take per §2.3; can we lock take 2 and file the disagreement as a follow-up issue, or is there something specific in take 1 that breaks the script if take 2 ships?"

**The intervention pattern:**
- Invoke the role's decision authority (no re-litigation).
- Offer the follow-up-issue mechanism (real outlet).
- Offer a tight, specific check (something in take 1 that *breaks the script*; not "I just like it better").
- Move on either way.

### 6.2 The over-polished-but-late submission

**Trigger:** Hour 22:40. The submission package is mostly done but the team is still tweaking the `SUBMISSION.md` and the README. The stop-work rule says lock at hour 23; the team is at hour 22:40 and not done.

**One-sentence intervention** (Builder Lead, in #channel):
"We have 20 minutes to the stop-work rule; let's lock SUBMISSION.md and README *now* and use the remaining 20 minutes for a single read-through of both, with no further edits unless we find a factual error."

**The intervention pattern:**
- Name the time constraint (stop-work rule).
- Convert "more editing" to "a single read-through" (bounded, productive).
- Allow factual-error fixes only (the discipline survives; typos do not block the lock).
- File polish items as follow-up issues if anyone wants to.

### 6.3 The attrition burnout

**Trigger:** Hour 23. A teammate has gone silent. They are still online but they have not posted in the channel for 90 minutes. They are physically present but not engaged.

**One-sentence intervention** (Comms Lead, in DM to the silent teammate):
"You have been quiet for a while; the retro starts at hour 24 and I want to make sure you have what you need to be in it — are you doing okay, or do you need 20 minutes to step away before the retro?"

**The intervention pattern:**
- Surface without judgment (no "where have you been").
- Offer the step-away path (real, bounded, not a confrontation).
- Connect to the retro (the retro needs them; this is not optional).
- Log the intervention in `DAY-2-LOG.md`, even if the resolution is "they showed up and were fine."

---

## 7. Recap

Three skills. Three sections. The closing four hours of day 2 in one discipline: *the team converts a build into what the judges see, then turns the dry-run into a lesson*.

- **Dress rehearsal.** Hour 20. Three recording roles (director, operator, audience proxy). Two takes minimum. Recording against the live URL. No re-litigation.
- **Submission package.** Hour 22. Five artifacts. `SUBMISSION.md` cover sheet (six sections). README judge-pass. Stop work at hour 23.
- **Retrospective.** Hour 24. Thirty minutes. KEPT, CHANGED, DROPPED. One scribe. One follow-up issue within 24 hours.
- **Three closing-stage conflicts.** Recording dispute, over-polish-but-late, attrition burnout. Each has a one-sentence intervention; same four-step structure as Lectures 1-2.

---

## 8. Connecting to Week 9

Week 9 takes the recorded demo (Week 8's hour-20 artifact) into a *live* pitch in front of judges. The recording is one shape of demo; the live pitch is another. The recording is the *director's cut*; the live pitch is the *live performance*. The two require different rehearsals.

Week 9 builds the live-pitch rehearsal. The team will:

- Cut the 3-minute recorded demo into a 60-second elevator version.
- Rehearse a judge-room pitch with a third teammate as the judge stand-in.
- Practice the Q&A pattern — short answers, no defensiveness, redirecting follow-up questions to the script.
- Run a panel-vs-table-judge drill (panels are 3-5 judges; tables are 1 judge at a time).

The transition from Week 8 to Week 9 is the transition from *demo* to *defense*. The demo is what the team showed; the defense is what the team says when a judge asks "how does this scale?" The two-week sequence covers both halves of judging.

> **C4 voice:** the dry-run is over at hour 24. The build is shipped; the demo is recorded; the submission is in. The team has *one artifact* the judges have seen, *one log* the future learners can read, and *one issue* filed for the next dry-run. The discipline of the close is the discipline of the next start.

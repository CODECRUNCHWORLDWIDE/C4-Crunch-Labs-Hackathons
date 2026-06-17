# Lecture 1 — Midnight Slump and the Pivot Protocol

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can run the hour-12 handoff stand-up as a structured midpoint check, not a status update. You can recognise the midnight-slump physiology and apply the four named coping protocols. You can execute the 15-minute pivot decision protocol from a written rubric and produce a single committed log entry that names both the decision and the alternative considered. You can defend why most "pivot conversations" should resolve as "no pivot, cut a MUST instead."

If you only remember one sentence from this lecture, remember this:

> **The hour-12 stand-up is a handoff, not a status check. The midnight slump is physiology, not character. The pivot conversation is 15 minutes, not 90. The team that knows the difference at hour 14 ships the demo at hour 24; the team that conflates them ships nothing and blames each other.**

Week 7 taught you the opening. Week 8 teaches you the *middle game* — the hours when the team is half-done, half-tired, and most exposed to the predictable failure modes. The opening was about discipline of agenda; the middle game is about discipline of *energy and judgment*. The two are different muscles. A team can ace the kickoff and still implode at hour 16 if they have not rehearsed what to do when the build is half-finished and the team is half-asleep.

This lecture has three parts. Part 1 (sections 2-3) covers the hour-12 handoff stand-up, including the Builder Lead rotation on 4-person teams. Part 2 (sections 4-5) covers the midnight slump physiology and the four named coping protocols. Part 3 (sections 6-7) covers the pivot decision protocol — when to use it, the 15-minute cap, the written rubric, and the log entry. Section 8 is the lecture's recap.

---

## 1. Why day 2 is a separate skill

Day 1 was about converting a group into a team. Day 2 is about *sustaining* the team through the part of the event where most teams fall apart.

The dry-run measurement is unambiguous: the failures named in MLH organizer post-mortems (publicly summarised on the MLH organizer guide and on conference talk recordings from past Devpost retrospectives) are heavily concentrated in hours 14-20 of a typical 24-hour event. The opening hours fail rarely in a structural way; the *closing* hours fail constantly. Three reasons:

- **The team's energy is lowest exactly when the integration friction is highest.** Hours 14-18 is where two or three teammates' branches first merge to main, where the first cross-track dependencies bind, where the demo lead first realises the build does not screen-record the way they imagined. The hardest technical and coordination problems are scheduled, accidentally but predictably, for the hours when the team is least equipped to solve them.
- **The decisions get bigger as the hours get later.** At hour 4, "should we use React or Vue" is a five-minute decision with a fast cost. At hour 16, "should we keep this feature" is a 90-minute argument with a sunk cost. The decisions look superficially similar; the consequences are not.
- **The conflict patterns shift from process to relationship.** Week 7's four conflicts (scope creep, silent disagreement, role overlap, the rewrite fight) were all *task or process* conflicts. Week 8's seven conflicts include three that are fatigue-driven and read as *relationship* conflicts — the snark, the silent withdrawal, the irritation. They are still process conflicts wearing a relationship costume; the lecture series teaches the unmasking.

> **C4 voice:** day 2 is not "day 1 again, more tired." It is a different game with different rules. Treating it as a continuation of day 1 is the single most common mistake the cohort makes; the protocols below are the corrective.

### 1.1 What day 2 produces

Five outputs by the time the team commits the day-2 log:

- **A handoff stand-up that resets the team's clock.** The hour-12 stand-up is the structural midpoint; the rotation and the MUST-status table re-anchor the team to *what they have actually shipped* versus what they planned at hour 2.
- **A pivot-decision log entry.** Even if the decision is "no pivot," the log entry exists. Future learners (and the team's own future selves) study the log to see *when* a pivot was almost taken; the entry's existence is the discipline.
- **A clean merge to main with every MUST integrated.** Hours 14-18 produce one merged-to-main commit per MUST. The branches die after the merge.
- **A recorded demo against the live deploy URL.** Hour 20 produces a 3-minute video. Two takes minimum. Live URL, not localhost.
- **A submission package and a retrospective.** Hour 22 packages; hour 24 retros. The retro produces one follow-up issue filed within 24 hours.

If day 2 does not produce all five, day 2 failed in some measurable way. The retro names which one and why.

---

## 2. The hour-12 handoff stand-up

The hour-12 stand-up is structurally different from the hour-4 and hour-8 stand-ups in Week 7. It is the *midpoint* — the team is half-done, the original Builder Lead has been on for 12 hours and is the most fatigued person in the room, and the MUST list is about to be measured against a clock that has half its hours left. The stand-up template is the same three-question template; the *added* segments are what make it a handoff.

### 2.1 The four added segments

```
┌────────────────────────────────────────────────────────────────────┐
│  THE HOUR-12 HANDOFF STAND-UP — 30 MINUTES                         │
│                                                                    │
│  [ 0:00 — 0:10 ]  Standard 3-question round (4 people × ~2 min)    │
│  [ 0:10 — 0:15 ]  MUST-status table read aloud                     │
│  [ 0:15 — 0:20 ]  Builder Lead rotation (4-person teams only)      │
│  [ 0:20 — 0:25 ]  Team-health midpoint check                       │
│  [ 0:25 — 0:30 ]  Day-2 plan (3 bullets)                           │
└────────────────────────────────────────────────────────────────────┘
```

Thirty minutes total. Three times longer than the standard 10-minute stand-up. The added time is paid back during hours 12-24 because the team's clock is reset honestly at hour 12.

### 2.2 The MUST-status table read aloud

The Comms Lead reads the team's `SCOPING-WORKSHEET.md` MUST section *aloud*, with the current status of each MUST in front of the team:

```markdown
MUST 1 — [name] — owner: [name] — status: DONE (merged to main at hour [N])
MUST 2 — [name] — owner: [name] — status: IN PR (PR #N, open since hour [N])
MUST 3 — [name] — owner: [name] — status: NOT STARTED (planned hour [N])
```

Read aloud is non-negotiable. Reading aloud forces every teammate to *hear* the actual state of the build, not the imagined state. The team that reads the MUST table aloud at hour 12 catches the silent disagreement (Week 7 Lecture 3 §7.2 conflict pattern) about whether MUST 2 is "in PR" or "actually merged" before the disagreement metastasises.

> **C4 voice:** a MUST that is "in PR but not reviewed" is *not done*. The MUST-status table has three values — DONE, IN PR, NOT STARTED — and "in PR" is not the same as "done." The team that conflates them at hour 12 reaches hour 22 with three "in PR" items and no merged demo.

### 2.3 The Builder Lead rotation (4-person teams)

On a 4-person team, the Builder Lead rotates at hour 12. The rotating-off lead takes a structured 2-hour rest; the rotating-on lead takes the role. The rotation is mechanical:

```
1. The rotating-off lead announces in the call:
   "I am rotating off Builder Lead as of hour 12. The merge state of main
    is at commit [SHA]. The next merge expected is the MUST 2 PR (#N)
    once review completes. I will be off the call until hour 14."

2. The rotating-on lead accepts:
   "I am accepting Builder Lead as of hour 12. I have read the MUST 2 PR
    and the open issues. I will hold off on merging anything new until
    MUST 2 lands. I will be on the call as Builder Lead until hour 22."

3. The Comms Lead logs both lines verbatim in DAY-2-LOG.md.
```

Three sentences. Two minutes per sentence. Five minutes total for the rotation segment. The rotation is *announced and accepted aloud*, not assumed; aloud is the difference between a clean handoff and a hour-14 confusion about who can approve the MUST 2 merge.

On a 3-person team, the rotation is skipped — the original Builder Lead stays on through hour 24, with a longer structured rest baked into the sleep window (Lecture 1 §4.3). Three-person teams compensate with sleep; 4-person teams compensate with rotation.

### 2.4 The team-health midpoint check

Five-minute round. Each teammate says one word describing their energy. Same rule as the Week 7 close-out: "fine" and "good" are rejected.

Acceptable words at hour 12:

```
"focused"          "tired-but-okay"    "behind"
"energised"        "slow"              "worried"
"frustrated"       "rested"            "stuck"
```

The Comms Lead writes each word in the log. The aggregation pattern matters more than any individual word: if three of four teammates say a fatigue-coded word ("tired-but-okay," "slow," "behind"), the team's day-2 plan needs an explicit sleep-window expansion. If three say a frustration-coded word ("frustrated," "stuck," "worried"), the team's day-2 plan needs to name the source.

### 2.5 The day-2 plan (3 bullets)

Last segment. The team commits to a 3-bullet day-2 plan:

```
1. By hour 16, MUST 2 is merged to main.
   Owner: [name] (current Builder Lead).
2. By hour 18, MUST 3 is in PR.
   Owner: [name].
3. By hour 20, the demo dress rehearsal happens with two takes.
   Owner: [name] (Demo Lead).
```

Three bullets. One owner per bullet. One named timestamp per bullet. The day-2 plan is the binding constraint for hours 12-24; the retrospective at hour 24 will measure the team against these three bullets specifically.

### 2.6 Sample log entry — full hour-12 handoff stand-up

```markdown
## Hour 12:00 — Hour-12 handoff stand-up (UTC 2026-05-16T03:00)

**3-question round:**

Pat (rotating off Builder Lead):
  - Shipped: MUST 1 merged at hour 9:30. MUST 2 in PR (#7) since hour 11.
  - Blocking: PR #7 needs review.
  - Next 4h: 2-hour rest; pick up MUST 3 frontend at hour 14.

Sam (Demo Lead):
  - Shipped: hook draft, script outline. Two storyboard sketches.
  - Blocking: needs MUST 1 seeded data for screen-capture rough.
  - Next 4h: get seeded data by hour 13; rough recording by hour 14; second take by hour 16.

Jordan (Comms Lead):
  - Shipped: hour-0/2/4/8 log entries; 5 pinned messages; one conflict log entry.
  - No block.
  - Next 4h: monitor channel; catch rotation announcement; prep hour-16 check template.

Alex (rotating on Builder Lead):
  - Shipped: empty-feed state, seeded data for MUST 1 (will publish in 30 min).
  - Blocking: need to accept Builder Lead role.
  - Next 4h: take over as Builder Lead; review PR #7 by hour 12:30; start MUST 3 frontend.

**MUST-status table:**
  - MUST 1 — Personalised feed — owner: Pat — DONE (commit a1b2c3d, hour 9:30).
  - MUST 2 — Saved-items view — owner: Pat — IN PR (#7, opened hour 11:00).
  - MUST 3 — Push notification — owner: Alex — NOT STARTED.

**Builder Lead rotation:**
  - Pat (rotating off) at hour 12:00: "Merge state of main at commit a1b2c3d.
    Next merge expected: PR #7 (MUST 2) once review completes. Off call until hour 14:00."
  - Alex (rotating on) at hour 12:00: "Accepting Builder Lead. Read PR #7
    and open issues. Will hold off on new merges until #7 lands.
    On call as Builder Lead until hour 22:00."

**Team-health midpoint:**
  - Pat: "tired-but-okay"
  - Sam: "focused"
  - Jordan: "energised"
  - Alex: "rested"

**Day-2 plan (3 bullets):**
  1. By hour 16: MUST 2 merged to main. Owner: Alex.
  2. By hour 18: MUST 3 in PR. Owner: Alex (with Pat support after hour 14).
  3. By hour 20: dress rehearsal with two takes. Owner: Sam.

**Scribe:** Jordan.
```

That log entry is the artifact of a clean handoff. Forty lines. Five minutes to draft after the stand-up. The team's day-2 trajectory is now in the file.

---

## 3. The hour-12 stand-up's failure modes

Three failures the lecture names so the team can avoid them:

### 3.1 The "everything is on track" stand-up

A stand-up where every teammate reports good news, the MUST-status table has three DONE rows, and the day-2 plan is "polish." If this is honest, the team is in great shape; if this is the team's wishful thinking, the team is in trouble.

The diagnostic: ask the Comms Lead to read back the MUST-status table. If a MUST is "in PR but not merged," it is not DONE. If a teammate's "shipped" line names a commit hash, it is real; if it names a feature in prose only, the commit hash may not exist yet.

> **C4 voice:** the "everything is on track" stand-up is the most dangerous one. The team's optimism overwrites the actual state; the actual state surfaces at hour 18 when MUST 2 turns out to have been "almost merged" for 6 hours. The cure is the read-aloud table.

### 3.2 The skipped rotation

A 4-person team where the hour-12 stand-up happens but the Builder Lead rotation does not. Pat stays on as Builder Lead through hours 12-24 because "I am still energised" or "Alex is busy with MUST 3 anyway."

The cost is concentrated at hour 18-22: Pat is now 22 hours into the build; merge decisions get sloppier; the recording window at hour 20 finds Pat exhausted in front of a camera. The rotation is structural; it is not optional based on how the rotating-off lead feels.

### 3.3 The skipped team-health check

The team-health round is the segment most often dropped under time pressure. "We are 25 minutes in and we have a day-2 plan; let's get back to work." That is wrong on two counts: first, the day-2 plan does not bind without a team-health context (a team where three of four teammates are stuck cannot ship a plan that ignores it); second, the team-health round is the *one place* the lecture series provides for surfacing fatigue, frustration, and stuckness before they become the day-2 conflicts.

The rule: the team-health round is the *last segment*, after the day-2 plan, so that the plan can be revised in light of it. If a teammate says "stuck" or "behind," the day-2 plan's bullet 1 or bullet 2 may need to be re-owned or re-scoped on the spot.

---

## 4. The midnight slump

The midnight slump is the period from roughly hour 14 to hour 18 of a 24-hour event (assuming an evening kickoff; the window shifts with the start time). Cognitive performance during this window drops measurably — the CDC's public-health pages on sleep deprivation, the NIH's StatPearls reference on the physiology, and the open MIT OCW materials on cognitive psychology all document the effect in different vocabularies. The slump is not a moral failing or a character issue; it is the *predictable cost of sustained attention without sleep*.

### 4.1 What the slump produces

Three observable effects, named in plain language:

- **Reading and writing slow down.** A teammate who could read a PR in 5 minutes at hour 4 takes 12 minutes at hour 16. The code is no harder; the reader is slower.
- **Working memory shrinks.** A teammate who could hold three open tabs and a chat conversation at hour 8 can hold one at hour 16. The "I'll just rewrite it" merge fight (Week 7 Lecture 3 §7.4) is more likely at hour 16 because the rewriting teammate cannot fit the original code into working memory long enough to merge it cleanly.
- **Decision quality drops.** A teammate at hour 16 makes the same decision they would have made at hour 4 *more slowly* and *with more emotional cost*. The decision content does not change; the deliberation cost does.

> **C4 voice:** the slump is not a problem to solve. It is a *condition to manage*. The four coping protocols below are not "ways to push through the slump"; they are *ways to make the slump less expensive*. The team that fights the slump loses to the team that plans around it.

### 4.2 The four coping protocols

C4 names four coping protocols, in order of how much they cost the team's wall-clock hours.

**Protocol 1 — Caffeine-and-water rule (zero cost).** One glass of water per hour, one caffeine source per 4-hour block. The water is the larger effect; the caffeine is the smaller effect. The pinned counter in the team channel (Comms Lead updates) tracks compliance.

```
Pinned message in #channel — updated each hour by Comms Lead:

  Hour 12 — Water: Pat 3, Sam 2, Jordan 4, Alex 1. Caffeine: 2 cups dispensed.
  Hour 13 — Water: Pat 4, Sam 3, Jordan 5, Alex 2. Caffeine: 0.
  Hour 14 — Water: Pat 4, Sam 4, Jordan 6, Alex 3. Caffeine: 4 cups dispensed.
```

Three lines per 4-hour block. Five seconds of typing per hour. The counter exists to *make hydration visible* to teammates who would otherwise forget; making it visible is the whole intervention.

**Protocol 2 — Two-person pair work (low cost).** Pair programming during the slump hours. Two teammates on one screen; one types, one watches. The watcher catches the typos, the off-by-one errors, the import bugs the typer's working memory cannot fit. The cost is one screen-share session; the gain is roughly 40% fewer bugs introduced during the slump hours (this is consistent with the general pair-programming research summarised on the Atlassian agile coach pages; the magnitude is approximate but the direction is robust).

**Protocol 3 — 90-minute focus block (medium cost).** A 90-minute pomodoro-style block: 90 minutes of synchronous work with no chat, no DMs, no PR reviews. Followed by a 15-minute break. The block protects the longest-attention task (usually MUST 2 integration) from the slump's working-memory shrinkage.

**Protocol 4 — 20-minute walk-or-sleep (high cost, highest reset).** A teammate who is *visibly* in the slump — re-reading the same line of code three times, typing and undoing, asking the same question twice — is sent on a 20-minute walk (outdoors if possible) or a 20-minute nap. The team writes the absence in the log; the teammate returns at a specific timestamp. The cost is 20 minutes of one teammate's wall-clock; the gain is the rest of the slump window with that teammate functional.

### 4.3 The structured sleep window

Adjacent to the slump but distinct from it: the *sleep window*. C4 recommends a 4-hour sleep window for at least one teammate at a time, on a 4-person team. On a 3-person team, two teammates sleep at the same time and the third stays on call.

Sample sleep window for a 4-person team with a Saturday 7pm kickoff:

```
Hour 14 (Sun 9am UTC, Sat 5am local) — Pat sleeps until hour 18.
Hour 18 (Sun 1pm UTC, Sat 9am local) — Pat wakes; Sam sleeps until hour 22.
Hour 16 (Sun 11am UTC, Sat 7am local) — Jordan naps for 2 hours; Alex stays on.
Hour 22 (Sun 5pm UTC, Sat 1pm local) — Sam wakes; full team on call for hour-22 submission and hour-24 retro.
```

Four-hour sleep window per teammate at staggered times. The team always has at least 2 teammates awake. The Builder Lead is on call continuously except during their sleep window.

> **C4 voice:** the team that does not plan the sleep window plans, by default, to have four exhausted teammates at hour 22. The plan is the difference between a clean hour-22 submission and a sloppy one.

---

## 5. The slump-window failure modes

Three patterns the lecture names so the team can recognise them:

### 5.1 The hero who refuses to sleep

A teammate (usually the original Builder Lead) refuses the sleep window. "I'll sleep when we ship." This is the *midnight death-march* pattern (Week 8 Lecture 2 §6.1). The team accepts the refusal at hour 14; at hour 20, the same teammate is the bottleneck on the recording because they cannot focus.

The intervention is mechanical, not emotional: the rotation protocol from §2.3 makes the sleep window *part of the rotating-off lead's role*. "You are off Builder Lead at hour 12; the rest window from hour 12-14 is part of the rotation, not optional." The hero's identity is preserved; the rest is enforced by the protocol.

### 5.2 The everyone-naps-at-once mistake

A 3-person team naps all three teammates from hour 14-18. The team is offline for 4 hours. At hour 18 they wake up and discover the deploy URL is down because the free-tier hosting expired during the sleep window. The recovery costs 90 minutes.

The fix is the staggered sleep window. At least one teammate is awake at all times during day 2. On a 3-person team, two teammates sleep at the same time and the third stays on call; the rotation is documented in the log.

### 5.3 The slump-denied

A team that refuses to acknowledge the slump exists. "We are fine." The four coping protocols are skipped. The team works through hours 14-18 at full pace. At hour 18, the merge of MUST 2 to main produces 4 conflicts the team did not have at hour 12. The conflicts read as "Pat wrote bad code"; the actual cause is "Pat wrote code at hour 16 in working-memory-shrunk conditions without the pair protocol."

The cure is the read-aloud team-health check at hour 12 (§2.4). The check names the slump *before* it happens; the team that names it can plan around it.

---

## 6. The pivot decision protocol

The pivot question is the most dramatic conversation a day-2 team can have. It is also, in most cases, the *wrong* question to be asking. The protocol's job is to *time-box* the conversation, *force the rubric*, and *produce a single log entry* that captures both the decision and the alternative.

### 6.1 What a pivot is, and is not

A pivot is a change of the *core direction* of the build. It is *not*:

- **A scope cut.** Cutting MUST 3 to SHOULD is not a pivot; it is a MoSCoW adjustment. Lecture 2 covers cuts.
- **A framework change.** Switching from Vue to React mid-event is not a pivot; it is a *catastrophic mistake*. Do not consider it.
- **A user change.** Changing the target user from "freshmen" to "transfer students" *is* a pivot, because the user defines the prompt response.
- **A prompt change.** Re-reading the prompt and noticing a sub-clause the team missed is *not* a pivot; it is a *prompt re-read* and the team adjusts the worksheet. If the team is genuinely responding to a different prompt now than they were at hour 0, that is a pivot.

> **C4 voice:** 90% of "should we pivot" conversations are actually "should we cut a MUST." The protocol's first job is to disambiguate; in most cases, the answer is "we are not pivoting; we are cutting MUST 3 to SHOULD." The conversation ends in 8 minutes, not 90.

### 6.2 When the question surfaces

Three triggers, named:

- **At hour 14, when MUST 1 is shipping but the team realises MUST 2 is more interesting than MUST 1.** This is the *seduction-of-the-alternative* pattern. The team is tempted to re-anchor on MUST 2 as the headline. The protocol's job is to check whether the headline change is actually a pivot or just a *demo-script rewrite* that does not require a build change.
- **At hour 16, when a teammate proposes a "better idea" they just thought of.** This is the *late-arriving inspiration* pattern. The protocol checks whether the new idea is a different *prompt response* (rare; probably a pivot) or a different *implementation* (common; not a pivot).
- **At hour 18, when the build's MUSTs are not screen-recordable as imagined.** This is the *demo-mismatch* pattern. The protocol checks whether the build needs to change (rare; possibly a pivot) or the demo script needs to change (common; not a pivot, just a script rewrite).

### 6.3 The 15-minute cap

The pivot conversation is *capped at 15 minutes*. The cap is the discipline; it is the difference between a conversation that produces a decision and a conversation that produces an argument.

```
┌────────────────────────────────────────────────────────────────────┐
│  THE 15-MINUTE PIVOT PROTOCOL                                       │
│                                                                    │
│  [ 0:00 — 0:02 ]  Naming what the proposed pivot is (2 min)        │
│  [ 0:02 — 0:07 ]  Rubric question 1: is it actually a pivot?       │
│  [ 0:07 — 0:12 ]  Rubric question 2: does it ship in remaining time? │
│  [ 0:12 — 0:14 ]  Decision (no pivot / pivot / cut a MUST instead) │
│  [ 0:14 — 0:15 ]  Log entry drafted (Comms Lead)                   │
└────────────────────────────────────────────────────────────────────┘
```

Fifteen minutes. The cap is enforced by the Comms Lead with a timer. At 15 minutes, the team has a decision *regardless of whether everyone is happy with it*. The Builder Lead breaks ties.

### 6.4 The 2-question rubric

Rubric question 1: **Is the proposed change a change of *user*, *pain*, or *verb* — or is it a change of *implementation*?**

If it is a change of implementation only (e.g., "we'll use a different chart library"), the conversation ends. It is not a pivot. The team adjusts in 5 minutes and goes back to work.

If it is a change of user, pain, or verb, the conversation continues. *Most* of the time the conversation still ends here; even a verb change is usually a script rewrite, not a build rewrite.

Rubric question 2: **If we pivot, does the new direction ship in the remaining hours, with the team's current skills, against the same prompt?**

The "same prompt" clause is the key. A pivot that no longer responds to the prompt is not a pivot; it is a *disqualification*. The new direction must still be a coherent response to the original event prompt.

If the answer to question 2 is "no," the decision is "no pivot, cut a MUST instead." Lecture 2 covers the cut.

If the answer to question 2 is "yes," the team is pivoting. Rare. The log entry names what was kept from the original build (sometimes a lot; sometimes the kept work is what makes the pivot feasible) and what was discarded.

### 6.5 Sample pivot log entry

```markdown
## Hour 14:30 — Pivot conversation: NOT PIVOTING (UTC 2026-05-16T05:30)

**Proposed pivot:**
Sam (Demo Lead) proposed shifting the target user from "FIU freshmen" to
"FIU transfer students" because the seeded data for the transfer-student
demo is more visually compelling.

**Rubric q1 — is it actually a pivot:**
Yes — user change is a pivot per Lecture 1 §6.1.

**Rubric q2 — does it ship in remaining time:**
No. Re-targeting requires re-seeding the dataset (2 hours), rewriting the
hook (45 minutes), and re-recording any rough takes already done. With
9.5 hours remaining and MUST 3 not started, the team does not have the
budget.

**Decision:**
NOT pivoting. Keeping freshmen as the target user. Adjusting the demo
script's hook line 2 to reference *both* freshmen and transfer students
as an aside, without changing the build's user model.

**Alternative considered (and rejected):**
Pivoting to transfer-student target — rejected on rubric q2.

**Owner of adjustment:** Sam (script-only change; no build change).
**Scribe:** Jordan.
**Time spent:** 12 minutes (3 min under the 15-minute cap).
```

That is the artifact. Twenty lines. Future learners and the team's own retro read this entry and see *exactly* what was considered, what was rejected, and why.

---

## 7. The pivot's failure modes

Three patterns the lecture names so the team can recognise them:

### 7.1 The 90-minute pivot debate

A team that opens the pivot conversation at hour 14 and is still in it at hour 15:30. The build has not moved for 90 minutes; the team has 8.5 hours left and now has both *less time* and *more frustration*.

The 15-minute cap exists to prevent this. The Comms Lead enforces it with a timer. If the team is at 15 minutes and has not converged on a decision, the Builder Lead breaks the tie unilaterally and the log entry says "Builder Lead tie-break, team disagreement noted." The frustration of an imposed decision is much smaller than the frustration of a 90-minute argument.

### 7.2 The silent stalemate

A pivot conversation where two teammates argue and two are silent. The argument concludes with "okay, let's not pivot then" but the silent teammates have not agreed; they have just waited it out.

The intervention is the same as the Week 7 silent-disagreement intervention (Week 7 Lecture 3 §7.2): the Comms Lead surfaces the silence. "Sam, Alex — you have not spoken. Do you have a vote?" The silent teammates' vote is captured in the log, even if it is "abstain." Silent stalemate is the worst outcome; abstention is acceptable.

### 7.3 The implementation-disguised-as-pivot

A teammate proposes a "pivot" that is actually a framework change or a chart-library swap. The team takes the bait and spends 15 minutes on it.

The cure is rubric question 1, applied strictly. "Is this a change of user, pain, or verb?" If no, the conversation ends in 5 minutes; the implementation question is rescheduled for the next stand-up and the build continues.

---

## 8. Recap

Three skills. Three sections. Eight pages of lecture notes that compress into a single discipline: *the team's middle game has its own protocols, and the protocols are not the opening's protocols*.

- **Hour-12 handoff stand-up.** Thirty minutes. Three-question round, MUST-status table, Builder Lead rotation (4-person teams), team-health midpoint, day-2 plan. Read aloud; logged; scribed.
- **Midnight slump.** Hours 14-18. Physiology, not character. Four coping protocols: caffeine-and-water, pair work, 90-minute focus, 20-minute walk-or-sleep. Plus the structured sleep window.
- **Pivot protocol.** Fifteen minutes. Two-question rubric. Most "pivot conversations" resolve as "no pivot, cut a MUST instead." Logged either way.

Read Lecture 2 next — the integration-friction window and the hour-18 demo cut. The middle game has more protocols; the lecture series finishes building the rehearsal of all of them.

> **C4 voice:** the kickoff was the steepest part of the curve. The middle is the longest. The closing is the most-watched. Day 2 is the longest part. The team that respects that asymmetry ships.

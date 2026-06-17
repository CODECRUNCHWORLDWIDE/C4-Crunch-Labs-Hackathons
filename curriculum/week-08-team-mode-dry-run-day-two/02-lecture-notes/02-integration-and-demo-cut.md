# Lecture 2 — Integration Friction and the Hour-18 Demo Cut

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can run the integration-friction window between hours 14 and 18 using a written merge protocol — branch-freeze rule, one-PR-at-a-time, 200-line cap, commit-message template. You can apply the hour-18 demo-cut rubric to convert an overrunning SHOULD or COULD into a clean cut, not a late-night marathon. You can recognise and resolve four day-2 conflict patterns at the integration stage — the surprise scope-creep at hour 16, the "I'll just rewrite it" merge fight, the silent stalemate, and the over-polish.

If you only remember one sentence from this lecture, remember this:

> **The integration window is where the team's individual work first becomes a team product. The merge protocol is the discipline; the demo cut is the discipline's escape valve; the team that runs both ships at hour 22, and the team that runs neither ships at hour 26 and misses the submission.**

Lecture 1 took the team from the hour-12 handoff stand-up through the midnight slump and the pivot protocol. Lecture 2 picks up at hour 14 — after the pivot conversation has resolved as "no pivot" — and runs through hours 14-18: the integration-friction window. The lecture has three parts: the merge protocol (sections 2-3), the hour-18 demo cut (sections 4-5), and the four integration-stage conflict patterns (section 6). Section 7 is the recap.

---

## 1. Why integration is its own skill

Hours 0-14 of the dry-run are the *individual-work* phase. Each teammate has their own branch, their own MUST, their own portion of the build. The work is parallel; the team is coordinated mostly through chat and stand-ups. The repo's main branch has the hour-0 commit and maybe MUST 1's merge; nothing more.

Hours 14-18 are when this changes. MUST 2 lands. MUST 3 starts. The first cross-MUST dependency surfaces — MUST 3's push notification depends on MUST 1's user model, which Sam wrote, which Pat needs to integrate into the notification scheduler, which Alex now owns after the rotation. The build becomes a *team build*; the repo's main branch now has work from three teammates; merge conflicts surface for the first time.

This shift is hard. Three reasons:

- **The team's coordination model changes.** Before integration, "we are all working on different things" is true. After integration, "we are all working on the same thing through different branches" is true. The chat patterns, the PR review patterns, the merge decisions are different.
- **The first real merge conflict reveals the team's PR sizing problem.** A team that wrote 800-line branches between hours 0 and 14 has 800-line PRs to merge between hours 14 and 18. An 800-line PR review at hour 16 is a 60-minute task that the slump-fatigued reviewer botches. The PR sizing should have been controlled from hour 0; if it was not, the integration window is when the team pays.
- **The technical debt accumulated in hours 0-14 becomes visible at hour 16.** The shortcuts ("we'll fix this when we integrate"; "we'll merge cleanly later") were free during the parallel-work phase; they are expensive now.

> **C4 voice:** the integration window is not a *new* phase of the build; it is the phase where the team's *earlier* discipline (or lack thereof) shows up. A team that wrote 100-line PRs from hour 0 has 100-line PRs to merge at hour 14. A team that wrote 600-line PRs has 600-line PRs to merge at hour 14. The protocol is the same; the cost is paid by the earlier behavior.

### 1.1 What integration produces

Three outputs by the time the window closes at hour 18:

- **One merged-to-main commit per MUST.** At hour 18, the main branch should have MUST 1, MUST 2, and MUST 3 (or MUST 3 in PR with review imminent). If a MUST is still on a branch and not merged at hour 18, the team is behind schedule.
- **A clean local-deploy-to-staging path.** The deploy URL (the same one the demo records against at hour 20) is in sync with main. A staging URL that lags main by 2 hours is a *separate* deploy URL the team needs to track; the C4 model treats the live deploy URL as auto-deployed on main merge.
- **A merge log entry for each merge.** The log entry is one paragraph: which MUST, which commit, which reviewer, what conflict was resolved (if any).

If the window does not produce all three, the window failed in a measurable way. The hour-18 demo cut is the escape valve when the window is failing.

---

## 2. The merge protocol

The merge protocol is the written set of rules the team agreed to in the kickoff (Week 7) and uses at hour 14-18. The rules are mechanical; the protocol's job is to make the merge decisions *not require a conversation*.

### 2.1 The four rules

```
1. Branches are named [must-N]-[short-description]. One branch per MUST.
2. PRs are <= 200 lines (excluding lockfiles and generated files).
3. One PR open at a time. The next PR opens after the previous merges.
4. The Builder Lead approves every merge. No self-approval.
```

Four rules. Each rule maps to a failure mode the protocol prevents.

- **Branch naming.** Prevents two teammates pushing to the same branch by accident.
- **200-line cap.** Prevents the 60-minute review fatigue at hour 16. A 200-line PR reviews in 10 minutes by a slumped teammate; an 800-line PR is unreviewable in the slump.
- **One PR at a time.** Prevents the merge-conflict cascade when two PRs touching the same file open simultaneously.
- **Builder Lead approves.** Prevents the silent self-merge that bypasses review. The Builder Lead is the *single point of accountability* for what is on main.

### 2.2 The 30-minute branch-freeze rule

Before a merge to main, the branch is *frozen* for 30 minutes: no new commits, no rebases, no force-pushes. The 30 minutes is the review window. The freeze is signalled in the team chat by the Builder Lead:

```
Pinned message in #channel — Builder Lead pins this when freezing a branch:

  BRANCH FREEZE: must-2-saved-items
  Frozen at hour [N]. Review window closes at hour [N+0.5].
  Reviewer: [name]. Expected merge at hour [N+0.5] if review passes.
```

Thirty minutes is short enough that the freeze does not block the team for long; it is long enough that the reviewer can read 200 lines, ask one or two clarifying questions, and approve.

### 2.3 The commit-message template

Each merge to main has a commit message in this template:

```
[must-N] [short verb-phrase summary of what shipped]

[1-2 sentence prose description of what was built and how.]

[Bullet list of any non-obvious decisions made:]
- decision 1
- decision 2

Co-authored-by: [other teammate, if pair worked on it]
Resolves: #[issue or PR number]
```

The template adapts the Conventional Commits format (free open spec) to the C4 voice. The `[must-N]` prefix makes the commit history readable by MUST number; the prose description gives the retro something to study; the co-authored-by line gives credit to the pair.

### 2.4 Sample merge log entry

```markdown
## Hour 15:45 — Merge: MUST 2 saved-items view (UTC 2026-05-16T06:45)

**MUST:** 2 (Saved-items view).
**PR:** #7 (opened hour 11:00, frozen hour 15:15, merged hour 15:45).
**Commit:** d4e5f6g
**Author:** Pat (originally; Alex rebased and rotated in at hour 12).
**Reviewer:** Alex (current Builder Lead).
**Conflict:** None. Branch was current with main as of hour 15:15 (Alex rebased).
**Lines:** 187 (under the 200-line cap).
**Deploy:** auto-deployed to live URL at hour 15:48. Verified live at hour 15:50.

**Commit message:**
[must-2] Saved-items view with localStorage persistence

Adds the /saved page. Reads from localStorage on mount; writes on every
"save" or "unsave" click. Empty state shows "no saved items yet" placeholder.

- Decision: localStorage chosen over server-side persistence because MUST 2
  does not require cross-device sync. Server-side persistence is a COULD
  (cut per hour-18 review).
- Decision: empty state placeholder is text-only to ship in the line budget;
  illustration is a SHOULD.

Co-authored-by: Pat <pat@example.com>
Resolves: #4
```

That is the artifact. Twenty-five lines. The retro can read this entry and see the full chain of what shipped, who shipped it, and what trade-offs were made.

---

## 3. Integration's failure modes

Three patterns the lecture names so the team can recognise them:

### 3.1 The 800-line PR

A PR opens at hour 14 with 800 lines of code. The reviewer (Builder Lead) tries to review it; the slump makes it unreviewable in <60 minutes. The reviewer either rubber-stamps it (review is not real) or asks for it to be split (the splitting takes 90 minutes during the slump).

The fix is upstream: PR sizing should have been controlled from hour 0. If the team is at hour 14 with an 800-line PR, the *immediate* fix is to split it into 4 logical commits and re-open as 4 PRs; the *longer-term* fix is the retro's "what we will change" follow-up issue.

### 3.2 The parallel-PR cascade

Two PRs open at the same time. They touch the same file. PR A merges; PR B now has a conflict. The PR-B author rebases; rebase produces new conflicts; the rebase takes 45 minutes during the slump.

The fix is the *one PR at a time* rule. If the team has two MUST PRs ready, the Builder Lead picks one, freezes the other branch (no new commits), merges the first, then unfreezes the second and rebases. Sequential, not parallel.

### 3.3 The silent self-merge

A teammate merges their own PR without the Builder Lead's review. The team only notices at hour 18 when the merge breaks the deploy.

The fix is repository settings: the team should configure GitHub branch protection on main to require at least one review from a non-author. This is set up at hour 0 in the team's `bootstrap.sh`. If it was not set up at hour 0, the team agrees verbally and the Comms Lead pins the agreement.

> **C4 voice:** the silent self-merge is the most common day-2 protocol violation in the cohort's history. The teammate who does it does not see it as a violation; they see it as "saving the team a step." The cost is the broken deploy at hour 18 and the recovery time. Branch protection prevents this mechanically.

---

## 4. The hour-18 demo cut

By hour 18, the team knows whether the MUST list is going to ship in the remaining 6 hours. If it is, the cut conversation is short; the team confirms the MUSTs and moves to dress-rehearsal prep. If it is not, the cut conversation is the *escape valve* that converts an overrunning SHOULD or COULD into a *cut* — not a late-night marathon.

### 4.1 What the demo cut is

The demo cut is a 15-minute conversation, structurally similar to the pivot protocol but with a different rubric. The cut decides:

- **Which SHOULD/COULD items are dropped from the demo entirely.** The build may have them partially; the demo does not show them.
- **Which MUSTs need a fallback.** A MUST that is "in PR but might not merge cleanly" needs a fallback (e.g., a polling-every-2s replacement for a real-time push, the fallback Alex's earlier exploratory work could supply).
- **Which features stay in the script.** The Week 6 script is the binding constraint; only features that ship are in the script.

### 4.2 The 3-line checklist

The cut applies a 3-line checklist to each SHOULD/COULD item:

```
1. Is the item screen-recordable in the 3-minute demo? [yes/no]
2. Does the item require >30 minutes to finish polishing? [yes/no]
3. If we cut it, does the script still tell a complete story? [yes/no]
```

The decision rule:

- If (1) is **no**, *cut*. A feature that does not screen-record cannot be in the demo regardless of whether it ships.
- If (1) is yes and (2) is **yes** and (3) is **yes**, *cut*. The feature is in scope but the polish budget is over and the script survives without it.
- If (1) is yes and (2) is no, *keep*. The feature is shippable in <30 minutes.
- If (1) is yes and (2) is yes and (3) is **no**, *escalate*. The script needs this feature; the team has to budget the >30 minutes or rewrite the script. Rewriting the script at hour 18 is expensive but allowed; cutting a feature that breaks the script is forbidden.

### 4.3 The cut log entry

```markdown
## Hour 18:00 — Demo cut: COULD-2 server-side sync (UTC 2026-05-16T09:00)

**Cut:**
COULD-2 — "Cross-device sync via Firestore." Dropped from the demo entirely.

**Trigger:**
At hour 17:45, Alex (Builder Lead) reported that the Firestore integration
required another 90 minutes to finish. The team applied the 3-line checklist.

**3-line checklist application:**
1. Screen-recordable in 3 min: yes (would have appeared as a "saved item
   syncs to phone" 8-second clip).
2. Requires >30 min to finish polishing: yes (90 min remaining).
3. Script survives without it: yes (the saved-items beat works with
   localStorage-only as shown in MUST 2; the cross-device line in the
   script was a "polish" mention, not a required beat).

**Decision:**
CUT.

**Replacement (if any):**
None. The localStorage saved-items view is sufficient for the demo.

**Owner of the cut:**
Alex agreed to stop work on the Firestore integration as of hour 18:00.
Alex pivoted to MUST 3 (push notification) for the remaining hours.

**Script adjustment:**
Sam (Demo Lead) updated the script line 6 from "your saves sync to your
phone" to "your saves persist between sessions." Five-second clip on the
sync animation removed.

**Scribe:** Jordan.
**Time spent:** 8 minutes.
```

That is the artifact. Twenty-five lines. Future learners and the team's retro can read this and see the entire reasoning chain.

### 4.4 The hour-18 cut is the only cut

A discipline rule: the team has *exactly one* formal cut conversation, at hour 18. If a SHOULD is overrunning at hour 16, the team notes it; the cut decision waits until hour 18. If a teammate proposes a cut at hour 20, the team rejects it — at hour 20 the recording is starting and a late cut wastes recording time.

The exception is *cutting from a MUST*. If at hour 20 the team discovers MUST 3 is not going to ship, the team is no longer in a cut conversation; the team is in a *fallback* conversation (see §5).

---

## 5. Fallbacks for MUSTs that do not ship

A MUST that does not ship at hour 20 is a crisis. The team's options:

### 5.1 Fallback option 1 — the polling stand-in

If a real-time MUST (e.g., push notification) is not ready, a *polling* version (e.g., every-2-seconds JS interval) is the fallback. The polling version is honest in the demo: "we have a 2-second polling fallback; the production target is real-time push, which is partially shipped."

### 5.2 Fallback option 2 — the seeded data demo

If a MUST that requires real user data is not generating data fast enough (e.g., a feed that needs 10 user-posted items but only 2 exist), the fallback is a *seeded dataset* — a hardcoded JSON file with 10 items, named as seed data in the demo script. Honest about the seeding; functional for the demo.

### 5.3 Fallback option 3 — the demo-mode toggle

If a MUST is functional but flaky, the team adds a *demo-mode toggle* — a query parameter or feature flag that enables the most-stable code path during recording. The toggle is mentioned in the demo (briefly): "the build supports both X and Y modes; the demo uses X mode."

### 5.4 The forbidden fallback — pretending it works

The one thing the team does *not* do is record a demo that pretends a feature works when it does not. The MLH and Devpost CoCs both treat fabricated demos as disqualifying; the C4 voice's discipline is stricter — the demo names what is shipped and what is fallback, every time. The seeded-data demo says "this is seeded data"; the polling fallback says "this is a 2-second polling fallback." Honesty is the floor.

> **C4 voice:** the judge who notices an unmentioned fabrication scores the team down; the judge who hears "this is a polling fallback to a real-time target" scores the team *up* because the team named the trade-off. The honesty is not just ethical; it is strategic.

---

## 6. The four day-2 conflict patterns at integration

Lecture 1 covered the midnight death-march and the pivot stalemate. Lecture 2 covers four more conflict patterns specific to the integration window. Each pattern has a name, a trigger, and a one-sentence intervention. The intervention pattern is the same as Week 7 Lecture 3 §7.5 — surface without blame, offer two or more paths, give the affected teammate the choice, log the resolution.

### 6.1 The midnight death-march

**Trigger:** Hour 15-16. A teammate (often the original Builder Lead) refuses the structured sleep window from §2.3 of Lecture 1. They are determined to work through; they assert they are fine; the team is uncomfortable confronting them.

**One-sentence intervention** (Comms Lead, in DM to the teammate):
"The rotation protocol is part of the role, not a comfort thing; can you take the 2-hour rest now and I'll have Alex hold the queue?"

**The intervention pattern:**
- Frame as a *role* requirement, not a *personal* requirement.
- Offer the alternative path (Alex holds the queue; team continues).
- Make the rest *2 hours*, not "rest as long as you want." Discrete and bounded.
- Log the intervention in `DAY-2-LOG.md` even if the teammate accepts immediately.

### 6.2 The hour-16 surprise scope creep

**Trigger:** Hour 16. A teammate proposes adding a feature that was not in the MUST/SHOULD/COULD list at hour 2. "I just realised we should add X." The proposed feature is genuinely cool; the team is tempted.

**One-sentence intervention** (Builder Lead, in #channel):
"That sounds great for a follow-up build; is it in the demo script, and if not, can we hold it until the hour-24 retro's 'changed' list?"

**The intervention pattern:**
- Acknowledge the proposal (no dismissal).
- Connect the proposal to the demo script (the binding constraint).
- Defer to the retro, which is a real outlet — features that surface at hour 16 often make excellent follow-up issues.
- Log the proposal in the retro's "considered" list.

### 6.3 The "I'll just rewrite it" merge fight

**Trigger:** Hour 17. A merge conflict surfaces. The reviewer (Builder Lead) reads the conflict and proposes rewriting the offending PR's approach. The author of the PR resists; they have spent 4 hours on the PR's current shape.

**One-sentence intervention** (Comms Lead, surfacing in #channel):
"The merge needs to happen in 30 minutes; can we ship Pat's PR as-is and file a follow-up issue for Alex's preferred refactor, or is there a non-refactor path that resolves the specific conflict?"

**The intervention pattern:**
- Name the time constraint (30-minute branch-freeze rule).
- Offer two paths (ship-and-refactor-later; or non-refactor resolution).
- Push the refactor to the follow-up-issue mechanism (real outlet; no work lost).
- Log the choice; if "ship as-is," the follow-up issue is filed immediately.

### 6.4 The silent stalemate during the cut

**Trigger:** Hour 18. The cut conversation reaches the 3-line checklist; two teammates argue; two are silent. The argument concludes with "okay, let's cut COULD 2" but the silent teammates have not voted.

**One-sentence intervention** (Comms Lead, addressed by name):
"Sam, Alex — you have not spoken; what is your vote on the COULD-2 cut, or do you want to abstain?"

**The intervention pattern:**
- Surface the silence by name.
- Offer the abstain option explicitly (silent stalemate is the worst outcome; abstention is acceptable).
- Capture the vote in the log.
- Continue with the cut decision regardless.

### 6.5 The intervention pattern's universal template

All four interventions share the structure:

```
Step 1 — Surface without blame.
         Name the situation; do not name the person as the problem.

Step 2 — Offer two or more paths.
         Never present a single "do this" command; always offer choice.

Step 3 — Give the affected teammate the choice.
         The teammate picks; the team supports the pick.

Step 4 — Log the resolution.
         The DAY-2-LOG.md entry names the conflict, the intervention,
         the choice, and the next step.
```

Four steps. The intervention's *voice* changes with the conflict; the *structure* does not.

> **C4 voice:** the interventions are not magic words. The structure is the magic. A team that surfaces-without-blame, offers-paths, gives-choice, and logs the resolution converts a day-2 conflict into a day-2 *protocol step*. The teams that win do not have fewer conflicts; they have more efficient resolutions.

---

## 7. Recap

Three skills. Three sections. The middle of day 2 in one discipline: *the team's individual work converges into a team product through a written merge protocol and an honest hour-18 cut*.

- **Merge protocol.** Branch names, 200-line PR cap, one-PR-at-a-time, Builder Lead approves. 30-minute branch-freeze. Commit-message template.
- **Hour-18 demo cut.** Fifteen minutes. Three-line checklist. Honest fallbacks if a MUST is shaky. The cut is logged.
- **Four conflict patterns.** Midnight death-march, surprise scope-creep, "I'll just rewrite it," silent stalemate. Each has a one-sentence intervention; all four share the same four-step structure.

Read Lecture 3 next — the dress rehearsal at hour 20, the submission package at hour 22, and the hour-24 retro. The dress rehearsal makes the demo. The submission package puts the demo in front of judges. The retro turns the dry-run into a lesson.

> **C4 voice:** the integration window is where the team learns whether they trust each other. The merge protocol is the visible discipline; the cut is the invisible one (cutting is harder than building). The team that runs both cleanly arrives at hour 20 with a build worth recording, and that is the entire point.

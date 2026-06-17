# Exercise Solutions — Week 8

One defensible solution per exercise. Multiple defensible solutions exist; the scoring criterion in each case is the *reasoning*, not the exact wording.

Read each solution *after* attempting the exercise. The solutions assume the lecture material was read.

---

## Exercise 1 — Pivot Decision Drill

### Scenario A — The seduction of the alternative (hour 14)

```markdown
## Scenario A — Sam proposes pivoting target user from FIU dorm walkers to Miami bus commuters

**Proposed pivot:**
Sam proposed changing the target user from FIU students walking from dorms
to morning classes to Miami bus commuters timing their trips. Sam argued
the seeded data for buses is more visually compelling.

**Rubric q1 — is it actually a pivot:**
Yes. Per Lecture 1 §6.1, a change of user is a pivot (user, pain, and verb
are the three pivot-class changes). FIU students → Miami bus commuters is
a user change.

**Rubric q2 — does it ship in remaining time:**
No. With ~10 hours remaining and MUST 2 only in PR (not merged), the team
does not have budget for re-seeding the dataset, re-targeting MUST 1's
form (dorm-and-classroom fields become origin-and-destination stops), and
re-recording any rough demo work that has been done. The user is genuinely
different; the build cannot accommodate the change.

**Decision:**
NOT PIVOTING.

**Alternative considered (and rejected):**
Pivoting to Miami bus commuters. Rejected on rubric q2 — the build budget
does not support a user change at hour 14.

**Owner of the next step:**
Sam (Demo Lead) confirms the FIU-student framing is locked. Demo script
will reference "students walking to morning classes" without introducing
bus-commuter language as a hedge.

**Time spent:** 11 minutes (under the 15-minute cap).
```

### Scenario B — The late-arriving inspiration (hour 16)

```markdown
## Scenario B — Alex proposes adding live GitHub API integration at hour 16

**Proposed pivot:**
Alex proposed replacing the static 5-card weekly-challenge deck with a
live feed of "good-first-issue" labelled GitHub issues, pulled from the
GitHub API.

**Rubric q1 — is it actually a pivot:**
No. The user (high-school CS club members), the pain (finding a starter
coding challenge), and the verb (pick a challenge in 30 seconds) are all
unchanged. The proposed change is an *implementation change* — the data
source for the deck. Per Lecture 1 §6.1, an implementation change is not
a pivot.

**Rubric q2 — does it ship in remaining time:**
Not relevant (the proposal is not a pivot, so rubric q2 does not apply).
Independently, with 8 hours remaining and all three MUSTs already merged,
*adding* live GitHub API integration is feasible but costly — the team is
in the slump window and the integration is non-trivial (rate limits, error
handling, the GitHub auth token).

**Decision:**
NOT PIVOTING. Implementation change. The team can consider the GitHub API
integration as a SHOULD-or-COULD *add*, evaluated against the demo cut
rubric at hour 18.

**Alternative considered (and rejected):**
Treating this as a pivot conversation. Rejected on rubric q1 — same user,
same pain, same verb; only the data source changes.

**Owner of the next step:**
Alex (Builder Lead) can pursue the GitHub API integration in parallel with
MUST polish, *but only* if the static deck remains the demo-recordable
path. The decision goes to the hour-18 demo-cut conversation.

**Time spent:** 7 minutes (well under the 15-minute cap).
```

### Scenario C — The demo mismatch (hour 18)

```markdown
## Scenario C — Push notification works but does not screen-record well

**Proposed pivot:**
Implicitly, Sam's question contains three options: (1) change the build to
mirror the push as an in-page banner; (2) change the script to remove the
push beat; (3) pivot to a different MUST 3.

**Rubric q1 — is it actually a pivot:**
Option 3 (pivot to a different MUST 3) would be a pivot if the new MUST 3
served a different pain or verb. Most likely, however, the team's MUST 3
is "real-time queue update for tutors," and any replacement MUST 3 would
serve the same pain (tutor visibility into queue updates). Options 1 and
2 are implementation/script changes, not pivots.

**Rubric q2 — does it ship in remaining time:**
At hour 18 with 6 hours remaining: option 1 (in-page banner mirror) is
shippable in <30 minutes (a small additional component listening on the
same event). Option 2 (remove the push beat) is free, with a script
rewrite cost of ~5 minutes. Option 3 (new MUST 3) is not shippable.

**Decision:**
NOT PIVOTING. Implementation change — *add* an in-page banner that mirrors
the push, so the recording shows both the OS-level push AND the in-page
banner. The script keeps the push beat; the banner makes it recordable.

**Alternative considered (and rejected):**
Pivoting to a different MUST 3. Rejected because (a) the existing push
implementation works for users (not just for the camera), and (b) a new
MUST 3 at hour 18 is not shippable.

**Owner of the next step:**
Alex (Builder Lead) adds the in-page banner. Estimated 25 minutes; falls
within the 30-minute threshold of the demo-cut rubric. Sam adjusts the
script to reference both the push and the banner.

**Time spent:** 14 minutes (right at the cap).
```

---

## Exercise 2 — Integration Friction Drill

### Part B — Prose answers

**Question 1.** PR #12 is 312 lines, over the 200-line cap. I (Builder Lead) request Alex split PR #12 into two PRs along the natural seam in the diff: a "push-infra" PR containing only `src/lib/push.ts` (198 lines, right at the cap), and a "push-integration" PR containing the `storage.ts` and `saved.tsx` modifications (114 lines). The split lets me review the new file (highest-risk surface area) separately from the integration deltas, and each split PR fits the cap. The "infra" PR opens first; the "integration" PR opens after the infra merges and rebases.

**Question 2.** PR #11 merges first. It is ready (review approved, rebased current, under the cap); blocking it on PR #12 violates the merge protocol's "ready PRs merge in arrival order" implicit rule. After PR #11 lands at the planned hour, I notify Alex in #channel: "PR #11 just merged; please rebase the split PR-12 branches against main before opening either as a PR." Alex rebases; conflicts on `storage.ts` resolve cleanly because PR #11's `storage.ts` is a *new* file with only Alex's additive modifications. The protocol for Alex is: rebase, push, open the infra PR, await my review.

**Question 3.** PR #11 merges before PR #13. PR #13 touches `saved.tsx` to add the empty-state illustration; PR #11 introduces `saved.tsx` as a new file. Sam's PR #13 was opened at hour 13:30 against an old main; it currently has *no* `saved.tsx` to modify (because PR #11 has not landed yet). After PR #11 merges, Sam rebases PR #13; the rebase will rewrite PR #13's `saved.tsx` modifications to apply against the just-merged version. The rebase strategy is `git fetch && git rebase origin/main`, resolving each conflict by *keeping PR #11's structure and integrating Sam's empty-state component placement*. Sam may need to revise the placement (e.g., the JSX hierarchy may have changed); the revision is a 10-minute task.

**Question 4.** Message in #channel from Alex (current Builder Lead):

> "Quick note: we have three PRs open right now and the merge protocol says one at a time. To get back on protocol, I'm freezing PRs #12 and #13 until PR #11 lands, then we'll re-sequence. No blame; just re-anchoring so the next two merges go cleanly. Expected: PR #11 merge in 30 min, then we'll figure out the order on #12 and #13 in a quick 5-min huddle at the merge."

### Part C — Merge log entry

```markdown
## Hour 16:00 — Merge: MUST 2 saved-items view (UTC 2026-05-16T07:00)

**MUST:** 2 (Saved-items view).
**PR:** #11 (opened hour 11:00, frozen hour 15:30, merged hour 16:00).
**Commit:** a7b8c9d
**Author:** Pat (rotated off Builder Lead at hour 12; the PR was opened
during their shift and reviewed during Alex's).
**Reviewer:** Alex (current Builder Lead).
**Conflict:** None at the merge. The src/lib/storage.ts file is new in
this PR; PR #12 (which also adds to it) has been deferred pending split
into smaller PRs.
**Lines:** 187 (under the 200-line cap).
**Deploy:** auto-deployed to live URL at hour 16:03. Verified live at
hour 16:06 by Sam (Demo Lead) screen-loading the /saved page.

**Commit message:**
[must-2] Saved-items view with localStorage persistence

Adds the /saved page. Reads from localStorage on mount; writes on every
"save" or "unsave" click. Empty state shows "no saved items yet" placeholder.

- Decision: localStorage chosen over server-side persistence because MUST 2
  does not require cross-device sync. Server-side persistence remains in
  COULD-2 pending the hour-18 demo cut.
- Decision: empty state placeholder is text-only to ship in the line budget;
  illustration is the SHOULD-1 PR (currently open as #13, awaiting rebase
  after this merge).

Co-authored-by: Pat <pat@example.com>
Resolves: #4
```

### Part D — `pr_sizer.py` script

The script in [pr_sizer.py](./pr_sizer.py) is the reference implementation. Running it against the sample JSON produces:

```
PR #11 (must-2-saved-items, Pat, 187 lines): OK
PR #12 (must-3-push-notify, Alex, 312 lines): OVER
PR #13 (should-1-empty-state-illustration, Sam, 64 lines): OK

Summary: 1 PR(s) over the 200-line cap.
```

Exit code 1 (one PR over). The script flags PR #12 as the over-cap PR — the same one the prose answer to Question 1 identified for splitting. The Builder Lead can wire the script into a pre-stand-up check or a CI hook with one extra line; the cohort's discipline of small, scriptable instrumentation continues.

---

## Exercise 3 — Retro from a Fake Log

### Retro entry

```markdown
## Hour 24:00 — Hour-24 retrospective (UTC 2026-05-16T15:00)

**Duration:** 30 minutes (hour 24:00 to hour 24:30).
**Scribe:** Jordan.

**One-word team-health check:**
  - Pat: "drained"
  - Sam: "proud"
  - Jordan: "relieved"
  - Alex: "satisfied"

**KEPT (4 items):**
  - [Jordan] The hour-12 read-aloud MUST-status table — we caught the
    "MUST 2 in PR" status honestly at hour 12 and re-anchored on it.
  - [Sam] The two-take dress rehearsal with audience-proxy notes — take
    1 surfaced the polling-fallback script gap; take 2 landed clean.
  - [Alex] The 15-minute pivot cap — Sam's transfer-student proposal at
    hour 14:30 resolved in 12 minutes (under cap) and we got back to the
    build.
  - [Pat] The Comms-Lead intervention at hour 23:25 — Jordan caught my
    silence and DMed me with a step-away offer; I came back energised.

**CHANGED (4 items):**
  - [Pat] MUST-3 implementation: original plan was a fully-featured push;
    the 410-line PR at hour 17 forced an "I'll just rewrite it" fight,
    which we resolved by landing as-is + follow-up issue #11.
  - [Sam] Demo script line 6: rewritten at hour 18 after the COULD-2
    Firestore cut; the script tightened with the cut.
  - [Alex] Branch-freeze duration: planned for 30 minutes; PR #7 actually
    sat in freeze for 30 minutes which was correct, but PR #9 got force-
    landed at hour 17:55 without a full freeze because of time pressure.
  - [Jordan] Stop-work declaration: Alex (not me) declared stop-work at
    hour 23; the protocol says Builder Lead or Comms Lead can declare,
    so this was protocol-valid, but I should have prepped the declaration
    in advance.

**DROPPED (4 items):**
  - [Sam] Demo script outline at hour 12 was only partial; will draft a
    full script outline by hour 8 next time so the dress rehearsal at
    hour 20 has a fully-locked script.
  - [Alex] PR #9 at 410 lines (more than 2x the cap) caused the "I'll
    just rewrite it" fight; will enforce the 200-line cap mechanically
    next time with a pre-push check (pr_sizer.py or a git hook).
  - [Pat] MUST 3 started at hour 14 (not hour 4 as ideal); will start
    MUST 3 in parallel from hour 4 next time, even if it's just scaffolding.
  - [Jordan] Stop-work prep: I did not have the stop-work declaration
    drafted in advance; will draft it at hour 22 next time as a Comms Lead
    deliverable.

**Follow-up issue:**
Filed as issue #14 — "PR sizing: enforce 200-line cap with a pre-push
check." Scope: add pr_sizer.py to a git pre-push hook in the template
repo's bootstrap.sh; document the override mechanism (a labelled-explicit
override for legitimate large refactors) in TEAM-CONTRACT.md.

**Time spent:** 30 minutes (on the cap).
```

### Follow-up issue body

```markdown
**Title:** PR sizing: enforce 200-line cap with a pre-push check
**Labels:** retro-followup
**Assignee:** Alex

**Description:**

During the dry-run, PR #9 (410 lines) triggered an "I'll just rewrite it"
merge fight at hour 17 (see DAY-2-LOG.md hour 17:30 entry). The 200-line
cap is in our TEAM-CONTRACT.md but is enforced only by eyeballing. A
mechanical pre-push check would have flagged PR #9 before the team paid
the integration-friction cost.

Scope:
- Add `pr_sizer.py` to `scripts/` in the team template repo.
- Add a `.git/hooks/pre-push` hook that runs the sizer against the
  current branch's diff vs. main.
- Document the override mechanism (`git push --no-verify` plus a labelled
  PR description explaining the override) in TEAM-CONTRACT.md §6.

**Acceptance criteria:**
- [ ] `pr_sizer.py` committed to `scripts/` of the template repo.
- [ ] `pre-push` hook example committed to `.git/hooks/pre-push.sample`
      and documented in the README.
- [ ] TEAM-CONTRACT.md §6 updated with the override mechanism (3-5 lines).
- [ ] One dry-run with the hook in place verifies the flow works.
```

---

*The solutions above are not the only defensible answers. Score yourself on the *reasoning* behind your choices, not the specific wording. A retro that is honest about the team's mistakes scores higher than a retro that is comfortable but invented.*

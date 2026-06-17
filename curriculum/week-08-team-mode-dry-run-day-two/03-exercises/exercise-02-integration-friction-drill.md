# Exercise 2 — Integration Friction Drill

> **Time:** ~1 hour.
> **When in the week:** Friday.
> **Deliverable:** `EXERCISE-02-MERGE-DRILL.md` + `pr_sizer.py` committed to your week-8 working folder.
> **Prerequisite:** Lecture 2 read.

## What this exercise is

You will run a *paper* merge-conflict resolution on a fake repo state — three PRs open, two of which conflict — and write the merge-log entries the Builder Lead would commit. You will also write and run a small Python script (`pr_sizer.py`) that flags PRs exceeding the 200-line cap. The script is part of the exercise; the merge resolution is the other part.

The exercise rehearses the merge protocol from Lecture 2 §2 under the specific conditions of the integration-friction window (hours 14-18). You are role-playing the Builder Lead.

## What this exercise is not

This is not a real merge against a real repo. The repo state is described in prose; the PRs are described as diff summaries; you write the resolution log entries without actually running `git merge`. The Python script is real, but its inputs are also fake (a sample JSON file with PR metadata).

## Part A — The fake repo state

```
Repository: dry-run-mock-7
Branch: main (commit: e1f2g3h, hour 14:00)

Three open PRs:

PR #11 — branch must-2-saved-items
  - Author: Pat
  - Opened: hour 11:00
  - Lines: 187
  - Touches: src/pages/saved.tsx (new file, 142 lines),
             src/lib/storage.ts (new file, 38 lines),
             src/pages/index.tsx (modified, +7 lines).
  - Status: review complete (Alex approved at hour 13:45);
             rebased against main at hour 13:50; ready to merge.

PR #12 — branch must-3-push-notify
  - Author: Alex
  - Opened: hour 14:00
  - Lines: 312 (over the 200-line cap)
  - Touches: src/lib/push.ts (new file, 198 lines),
             src/lib/storage.ts (modified, +28 lines),
             src/pages/saved.tsx (modified, +86 lines).
  - Status: opened just now; not yet reviewed.

PR #13 — branch should-1-empty-state-illustration
  - Author: Sam
  - Opened: hour 13:30
  - Lines: 64
  - Touches: src/components/EmptyState.tsx (new file, 48 lines),
             src/pages/saved.tsx (modified, +16 lines).
  - Status: opened; awaiting review.

Cross-PR observations:

- PRs #11 and #12 both modify src/lib/storage.ts.
- PRs #11 and #12 and #13 all modify src/pages/saved.tsx.
- The team's merge protocol (from TEAM-CONTRACT.md) says:
  1) One PR open at a time (but the team violated this by opening
     three; the drill resolves the violation).
  2) PRs <= 200 lines (PR #12 violates this).
  3) Builder Lead approves every merge (Alex is the current Builder
     Lead per the hour-12 rotation).
```

## Part B — The questions you answer (in prose)

For each question, write a 2-4 sentence answer in the deliverable file. Each answer is a *Builder Lead decision*; explain the decision, not just the action.

**Question 1.** PR #12 is 312 lines, over the 200-line cap. As Builder Lead, what do you do? List the specific commits or splits you would request, and the order.

**Question 2.** PRs #11 and #12 both modify `src/lib/storage.ts`. PR #11 is ready to merge; PR #12 is not. Which do you merge first, and what is the protocol for the second PR after the first lands?

**Question 3.** PRs #11 and #13 both modify `src/pages/saved.tsx`. The PR #13 modifications to `saved.tsx` likely conflict with PR #11's new content. What is the merge order, and what is the rebase strategy for PR #13?

**Question 4.** The team has been working under the merge protocol but the three-PR-open violation suggests the protocol has slipped. Write a 2-sentence message you (as Builder Lead) post in #channel to surface the protocol slip and re-anchor the team without blaming any individual.

## Part C — The merge log entries you write

After answering the questions in Part B, write the merge log entry for the *first* merge — the one that lands at the earliest timestamp under your resolution. Use the template from Lecture 2 §2.4.

```markdown
## Hour [N] — Merge: [MUST/SHOULD] [name] (UTC YYYY-MM-DDTHH:MM)

**MUST/SHOULD:** [N] ([name]).
**PR:** #[N] (opened hour [N], frozen hour [N], merged hour [N]).
**Commit:** [sha placeholder]
**Author:** [name]
**Reviewer:** [name]
**Conflict:** [None / 1-2 sentence description]
**Lines:** [N] (under/over the 200-line cap)
**Deploy:** [auto-deployed at hour [N]; verified live at hour [N]]

**Commit message:**
[Following the template from Lecture 2 §2.3]
```

## Part D — The `pr_sizer.py` script

Write a small Python script that reads a JSON file of PR metadata and prints a flag for each PR over the 200-line cap. The script is the *mechanical* version of the manual eyeballing you did in Part B.

Sample input file (`pr_metadata.json`) — commit this file as a starter:

```json
{
  "prs": [
    {"id": 11, "branch": "must-2-saved-items", "author": "Pat", "lines": 187},
    {"id": 12, "branch": "must-3-push-notify", "author": "Alex", "lines": 312},
    {"id": 13, "branch": "should-1-empty-state-illustration", "author": "Sam", "lines": 64}
  ],
  "cap": 200
}
```

The script (`pr_sizer.py`):

```python
"""pr_sizer.py — flag PRs over the team's line-count cap.

Usage:
    python3 pr_sizer.py pr_metadata.json

Output:
    One line per PR, OK or OVER.
"""
import json
import sys
from typing import TypedDict


class PRMetadata(TypedDict):
    id: int
    branch: str
    author: str
    lines: int


class InputFile(TypedDict):
    prs: list[PRMetadata]
    cap: int


def load_metadata(path: str) -> InputFile:
    with open(path, "r", encoding="utf-8") as handle:
        data: InputFile = json.load(handle)
    return data


def flag_pr(pr: PRMetadata, cap: int) -> str:
    status = "OVER" if pr["lines"] > cap else "OK"
    return f"PR #{pr['id']} ({pr['branch']}, {pr['author']}, {pr['lines']} lines): {status}"


def main(path: str) -> int:
    data = load_metadata(path)
    cap = data["cap"]
    for pr in data["prs"]:
        print(flag_pr(pr, cap))
    over_count = sum(1 for pr in data["prs"] if pr["lines"] > cap)
    print(f"\nSummary: {over_count} PR(s) over the {cap}-line cap.")
    return 0 if over_count == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pr_sizer.py pr_metadata.json")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
```

Run it:

```bash
python3 pr_sizer.py pr_metadata.json
```

Expected output:

```
PR #11 (must-2-saved-items, Pat, 187 lines): OK
PR #12 (must-3-push-notify, Alex, 312 lines): OVER
PR #13 (should-1-empty-state-illustration, Sam, 64 lines): OK

Summary: 1 PR(s) over the 200-line cap.
```

Commit both `pr_sizer.py` and `pr_metadata.json` to your week-8 working folder. Run `python3 -m py_compile pr_sizer.py` to verify the script compiles cleanly before committing.

## Acceptance checklist

- [ ] Part B has 4 prose answers, each 2-4 sentences.
- [ ] Part C has one merge log entry following the Lecture 2 §2.4 template.
- [ ] Part D has `pr_sizer.py` and `pr_metadata.json` committed.
- [ ] `python3 -m py_compile pr_sizer.py` exits with no errors.
- [ ] Running the script against the sample JSON produces the expected output.
- [ ] The deliverable file is under 600 lines (prose + commits).

## Why this exercise

The integration-friction window is mechanical; the mechanical work is also where the *most* day-2 conflicts surface. The exercise rehearses the mechanical work — the merge order decisions, the commit-message template, the PR sizing — under a fake constraint that lets you fail cheaply. By Saturday's real dry-run, the first merge of MUST 2 to main should feel familiar; the muscle is the rehearsal of this drill.

The Python script is a small token of "infrastructure as discipline" — a 30-line script that the Comms Lead can run once per stand-up to check PR sizes mechanically. The cohort builds these small scripts every week; the cumulative effect is a team that has cheap, reliable instrumentation around its own discipline.

## Notes on the solutions

The solutions in [SOLUTIONS.md](./SOLUTIONS.md) give one defensible answer per question. There may be multiple defensible answers; the scoring criterion is whether your reasoning *follows the merge protocol*. A merge order that violates the protocol (e.g., "merge PR #12 first even though it is over the cap") is wrong regardless of how cleverly the rationale is phrased. A merge order that follows the protocol (PR #11 first, PR #12 split, PR #13 rebased after) is correct even if your specific commit-message wording differs from the solution.

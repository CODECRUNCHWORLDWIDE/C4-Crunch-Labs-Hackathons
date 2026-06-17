# Challenge 1 — Submission Package Polish: Acceptance Criteria

> **Time:** ~1 hour.
> **When:** after the dry-run weekend (Sunday evening or Monday morning of Week 9).
> **Deliverable:** a fully polished submission package — repo README, `SUBMISSION.md`, demo-video metadata, GitHub topic tags, license, code of conduct — plus a 12-item acceptance scorecard appended to your `DAY-2-LOG.md`.
> **Prerequisite:** mini-project complete; `DAY-2-LOG.md` committed; retro entry in place.

## What this challenge is

You will treat the team's dry-run submission as if it were a *real* Devpost entry to a real hackathon, then apply a 12-item acceptance checklist. The checklist is the operational definition of "the submission package is judge-ready."

The challenge is *self-graded*. The point is not to score 12/12; the point is to *honestly* score whatever the team produced and identify the gaps. A team that scores 9/12 with honest evidence is stronger than a team that scores 12/12 with rationalised gaps.

## Why this challenge matters

The dry-run produced a submission. The submission is the *artifact a judge sees*. The challenge applies the lens of a judge with 4-6 minutes of attention; the gaps the lens surfaces are the items that, at a real event, would cost the team the win.

The acceptance scorecard is the *bench*. The submission polish is the *run*. The score is the *measurement*. Real events have submission deadlines that are unforgiving; the dry-run rehearses the discipline at low stakes so that the real event runs at low stress.

## The 12-item acceptance checklist

The 12 items are grouped by artifact: repo (4), README (3), submission cover (3), demo (2).

### Repo (4 items)

```
1. The repo is public.
   Evidence: GitHub repo URL accessible without login.

2. The repo has a LICENSE file.
   Evidence: a LICENSE file at the repo root, with the team's chosen
   license (MIT is the C4 default).

3. The repo has a CODE_OF_CONDUCT.md file.
   Evidence: a CODE_OF_CONDUCT.md at the repo root, linking to or
   embedding the Contributor Covenant or the MLH CoC.

4. The repo has at least 3 GitHub topic tags relevant to the build.
   Evidence: the topic tags appear under the repo's name on GitHub.
   Suggested: "hackathon", "react" (or your framework), plus one
   build-domain tag (e.g., "accessibility", "education", "data").
```

### README (3 items)

```
5. The README opens with a one-paragraph project description.
   Evidence: the first paragraph of README.md (above any subheading)
   names the user, the pain, and the verb the build performs.
   The paragraph fits in 4-6 sentences.

6. The README has a "how to run locally" section with 3-5 commands.
   Evidence: a code block with shell commands the judge could copy-paste
   to clone, install, and run the build locally.

7. The README has a "links" section near the top, listing the live
   deploy URL, the demo video URL, and the SUBMISSION.md file.
   Evidence: a "Links" section in the top half of README.md.
```

### Submission cover (3 items)

```
8. SUBMISSION.md exists and has all 6 sections from Lecture 3 §3.2.
   Evidence: the six section headings present in the file.

9. SUBMISSION.md is 400-600 words.
   Evidence: word count.

10. SUBMISSION.md's section 6 (demo video timestamps) has at least
    5 timestamp rows.
    Evidence: row count in section 6.
```

### Demo (2 items)

```
11. The 3-minute demo video is published on a free public host
    (YouTube unlisted, Loom free tier, or similar).
    Evidence: the URL works in an incognito browser window.

12. The demo video is between 2:50 and 3:10 (3 minutes ± 10 seconds).
    Evidence: video duration on the host's player.
```

## The deliverable

For each of the 12 items, score yes/no in your `DAY-2-LOG.md` and write *one sentence of evidence per item*. The scorecard is appended at the very end of `DAY-2-LOG.md`, below the retro entry.

```markdown
## Hour 25:00 — Submission polish scorecard

(Scored as part of Challenge 1; not part of the dry-run wall-clock.)

### Repo
1. [yes/no] [evidence]
2. [yes/no] [evidence]
3. [yes/no] [evidence]
4. [yes/no] [evidence]

### README
5. [yes/no] [evidence]
6. [yes/no] [evidence]
7. [yes/no] [evidence]

### Submission cover
8. [yes/no] [evidence]
9. [yes/no] [evidence]
10. [yes/no] [evidence]

### Demo
11. [yes/no] [evidence]
12. [yes/no] [evidence]

**Score:** [N]/12
**Gaps identified:** [bullet list of any "no" items]
**Polish actions taken:** [bullet list of any items you addressed during the polish pass]
```

## How to interpret the score

- **12/12:** the submission is judge-ready. Stop here. The team is done.
- **10-11/12:** strong. Fix the 1-2 gaps if they are quick (<30 minutes); document the unfixed ones in the retro's CHANGED list.
- **7-9/12:** acceptable. The gaps reveal which parts of the closing protocol slipped. List them in the retro's DROPPED list as candidates for the next dry-run's follow-up issue.
- **<7/12:** the submission is not judge-ready. This is informative; it means the team ran out of energy or discipline before hour 22. The fix is *not* to polish now (the dry-run is over); the fix is the *next* dry-run's discipline. Note the score in the retro and move on.

## Why no time bonus, no grade bump

The challenge does not offer a "polish bonus" or a "grade bump." Polish that takes more than 60 minutes is *not* a closing-discipline skill; it is a separate skill (the same skill a software-engineering polish pass at a job uses). The challenge's 60-minute time-box matches the closing-discipline budget; the team that polishes for 4 hours is solving a different problem.

> **C4 voice:** the challenge is a re-run of the closing discipline, not a new task. A submission that scores 8/12 in the dry-run and 11/12 in the next dry-run has *learned* something; a submission that scores 12/12 by polishing for 4 hours on Sunday night has only learned that 4 hours of polish is expensive.

## What to do with the deliverable

The scorecard goes in `DAY-2-LOG.md` as the last entry. It is the final artifact of the dry-run. The team can show it to the C4 facilitator, to a future learner reading the log, or to themselves at the start of the next dry-run.

The single most-useful thing a team can do with a 8/12 scorecard is to *file a second follow-up issue* (in addition to the retro's primary follow-up issue): the polish gap most worth closing for the next event. The second issue is optional; one issue is the discipline, two is the stretch.

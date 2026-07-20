# Exercise 1 — Self-Score the Team's Week 8 Submission

> **Time:** ~1 hour.
> **When in the week:** Tuesday.
> **Deliverable:** `EXERCISE-01-SELF-SCORE.md` committed to your `week-09/` working folder.
> **Prerequisite:** Lecture 1 read; Week 8 submission committed.

## What this exercise is

You will apply the five-dimension C4 rubric (Lecture 1 §2) to your team's *own* Week 8 submission. For each of the five dimensions, you will:

- Score the team's submission on the 1-5 scale (using the anchors from Lecture 1 §4.1).
- Write a one-line evidence cite for the score (Lecture 1 §4.3).
- Note which judging mindset (engineer or investor) is more likely to score the dimension favourably for *your specific* build.
- Optionally, run the score through the `rubric_score.py` helper to verify the weights.

The exercise is solo. The team's collective score can be averaged later; for this exercise, each teammate produces their own honest self-score. The variance between teammates is a useful signal in the mini-project.

## What this exercise is not

This is not a team activity. You are not gathering the team for a consensus discussion. The exercise is the *individual* honest self-score under the rubric. The team-level consensus score is in the mini-project.

The exercise is also not a *defence* of the team's choices. You are not arguing for high scores; you are *applying the rubric* as a judge would. The honest 3 of 5 with clear evidence is the goal, not the rationalised 4 of 5.

## What you will need

- Your team's Week 8 submission, accessible: the repo URL, the live deploy URL, the demo video URL, the `SUBMISSION.md` cover sheet, and the `DAY-2-LOG.md`.
- The five-dimension rubric from Lecture 1 §2.
- The 1-5 scale anchors from Lecture 1 §4.1.
- A 60-minute focus window (timer optional but recommended).
- (Optional) the `rubric_score.py` helper for the final weighted-total verification.

## The five dimensions to score

Score your submission on each of the five C4 dimensions:

```
1. Technical Complexity   (weight 25%)
2. Design and UX           (weight 20%)
3. Originality             (weight 20%)
4. Polish                  (weight 20%)
5. Presentation            (weight 15%)
```

The weights match the HackMIT-style sample from Lecture 1 §3.3. If you prefer a different weighting (MLH default is unweighted; NumFOCUS uses 25/20/20/15/10/10), use that and note the source.

## The deliverable

For each of the five dimensions, write:

```markdown
## Dimension N — [name]

**Score:** [1-5] / 5
**Evidence (one line):** [the one-line cite for the score, per Lecture 1 §4.3]
**Mindset tilt:** [engineer / investor / neutral] — [one-sentence reason]
**Weight applied (if any):** [percentage]
```

Then a closing **Weighted total** block:

```markdown
## Weighted total

[total score] / 5.0

Note: this score is the team's *self-score* — not the score a real judge
would give. It is the team's calibration baseline for the mock pitch
in the mini-project.
```

Then a closing **Honest gap** block:

```markdown
## Honest gap

The lowest-scored dimension is [name] at [score]. The reason it is low
is [honest reason, not rationalisation]. The single change the team
could make in the next 4 hours of polish work that would raise this
dimension by 1 point is [specific change].
```

## Acceptance checklist

- [ ] All five dimensions have a score, an evidence cite, a mindset tilt, and a weight.
- [ ] At least one dimension scores at 2 or below, OR there is an explicit acknowledgement in the Honest gap block that the team genuinely scored 3+ on every dimension (rare; usually indicates over-grading).
- [ ] The weighted total is computed correctly (within ±0.05 of what `rubric_score.py` produces, if used).
- [ ] The Honest gap block names a specific change, not a generic improvement.
- [ ] The committed file is under 200 lines.

## Why this exercise

The mock pitch in the mini-project rehearses *delivery*. The rubric self-score rehearses *the lens the judges will apply*. Without the self-score, the mock pitch is delivery practice without a target; with the self-score, the mock pitch is *targeted* delivery practice on the dimensions where the team is weakest.

Three of the five Q&A archetypes (the user question, the technical question, the challenge question — Lecture 3 §3) draw answers from the team's understanding of their own rubric weaknesses. The self-score is the source material for those answers.

## A note on what scores are "right"

There are no "right" scores. The exercise's hidden lesson: *honest* scoring is the skill, not high scoring. A team that scores themselves 16/25 honestly with clear evidence is better-prepared than a team that scores themselves 22/25 with rationalised evidence.

When scoring yourself against the solutions in [SOLUTIONS.md](./SOLUTIONS.md), the metric is *not* whether your scores match the sample — your build is different from the sample build. The metric is whether your evidence is concrete (specific, observable, defensible) versus abstract (generic, aspirational, unverifiable).

## Using `rubric_score.py`

To verify your weighted total, create a JSON file matching the sample shape in `rubric_input.json`, then run:

```
python3 rubric_score.py your_rubric.json
```

The script will print the per-dimension lines, the weight validation, and the weighted total. If the weights do not sum to 1.0 ± 0.01, the script exits with code 1; this is the most common gotcha when adapting from the sample.

The `rubric_score.py` helper does *not* judge your build. It checks the arithmetic. The arithmetic is the *floor*; the rubric judgment is the *muscle*.

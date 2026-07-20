# Week 9 — Exercises

Three exercises. Each is solo writing or solo scripting work that rehearses one of the judge-room skills. Together they build the muscle for the mock pitch and mock Q&A in the mini-project.

| Exercise | Skill rehearsed | Time | When |
|---------|------------------|------|------|
| [exercise-01-self-score.md](./exercise-01-self-score.md) | The five-dimension rubric; self-score against the team's own Week 8 submission. | ~1h | Tuesday |
| [exercise-02-qna-drill.md](./exercise-02-qna-drill.md) | The Q&A drill — five archetypes; five 30-second answers; one bridge sentence; one "I don't know." | ~1h | Friday |
| [exercise-03-cue-drill.md](./exercise-03-cue-drill.md) | Match four judge body-language cues to their named recovery moves; produce three written cue-and-recovery vignettes. | ~30 min | Friday |

Solutions for all three are in [SOLUTIONS.md](./SOLUTIONS.md). Do the exercises first; cover the solutions; check after.

Two small Python helpers live in this folder:

- [`pitch_timer.py`](./pitch_timer.py) — a CLI timer with the 30-90-45-15 beats baked in. Use with `--dry-run` for fast iteration; without the flag, it sleeps through the real beats.
- [`rubric_score.py`](./rubric_score.py) — a CLI scorer that adds the five dimensions with weights and prints the weighted total. Sample input in [`rubric_input.json`](./rubric_input.json).

Both helpers run on a stock Python 3.10+ install with no external packages.

## Submission

Each exercise's deliverable is a Markdown file committed to your `week-09/` working folder in the same repo as `DAY-1-LOG.md`, `DAY-2-LOG.md`, and the Week 8 `SUBMISSION.md`. The Comms Lead can collect all three under a single `WEEK-09-EXERCISES.md` if that is easier.

## Voice

The C4 voice on these exercises is sober, evidence-led, and time-boxed. The exercises are not creative writing; they are *judgment under constraint*. Aim for clarity over polish.

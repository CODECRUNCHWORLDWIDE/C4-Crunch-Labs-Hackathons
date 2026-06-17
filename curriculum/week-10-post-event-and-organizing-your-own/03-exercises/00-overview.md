# Week 10 — Exercises

Four exercises this week, two of which produce committed artifacts in the team repo and two of which produce individual deliverables. Plus two CLI helper scripts in Python that pair with the mini-project (budget estimation, run-of-show generation).

| File | What it covers | Output |
|------|----------------|--------|
| [exercise-01-recruiter-readme.md](./exercise-01-recruiter-readme.md) | Convert the team's submission into a recruiter-grade README using the seven-section template | `README-FOR-RECRUITERS.md` committed at repo root |
| [exercise-02-ninety-second-video.md](./exercise-02-ninety-second-video.md) | Record and upload the 90-second phone demo using the four-beat phone-demo arc | YouTube unlisted (or Loom public) URL committed in the recruiter-grade README |
| [exercise-03-sponsor-email.md](./exercise-03-sponsor-email.md) | Draft three sponsor cold-emails using the C4 seven-line template, with a tier menu and a non-cash menu | Three emails saved as markdown in `mini-project/sponsorship/` |
| [exercise-04-linkedin-and-resume.md](./exercise-04-linkedin-and-resume.md) | Write the LinkedIn post draft and the resume bullet for the team's hackathon project | LinkedIn post draft saved in `POST-EVENT-LOG.md`; resume bullet saved individually |
| [budget_estimator.py](./budget_estimator.py) | CLI helper for estimating a hackathon budget from attendee count and tier choices | Console output; numbers reused in the mini-project budget |
| [runofshow_builder.py](./runofshow_builder.py) | CLI helper for printing a minute-by-minute run-of-show for a one-day campus hackathon | Console output; structure reused in the mini-project run-of-show |
| [SOLUTIONS.md](./SOLUTIONS.md) | One defensible solution per exercise | Reference; committed at exercise close |

Order: Exercise 1 (Monday/Tuesday) → Exercise 2 (Tuesday/Wednesday) → Exercise 3 (Friday) → Exercise 4 (Friday). Run the two CLI helpers as part of the mini-project on Saturday/Sunday.

All four exercises tie into the deliverables for Week 10. None of them is busywork. Each one produces a single artifact the learner will *re-use*, *cite*, or *commit* — either in the team repo or in the capstone plan.

## How the exercises map to the deliverables

- **Exercise 1 — Recruiter-grade README.** Lives in the team repo as `README-FOR-RECRUITERS.md` at the repo root. Not re-used in the capstone (the capstone is an organising plan, not a project plan). Logged in `POST-EVENT-LOG.md` Day 2 of the carry-out window.
- **Exercise 2 — 90-second phone demo.** Lives in the team repo as a URL embedded in the recruiter-grade README. Not re-used in the capstone. Logged in `POST-EVENT-LOG.md` Day 3 of the carry-out window.
- **Exercise 3 — Sponsor cold-emails.** Does *not* live in the team repo — these emails belong to the capstone. Committed to `mini-project/sponsorship/email-0X-*.md`. Re-used as the *Sponsorship summary* section of the capstone's `PLAN.md`.
- **Exercise 4 — LinkedIn post + resume bullet.** Drafts live in `POST-EVENT-LOG.md` for team review; the published versions live on each member's individual LinkedIn and resume. Logged in `POST-EVENT-LOG.md` Days 4 and 5.

The two CLI helpers do not have a "lives in" mapping — they are *generators*. They output content that the capstone customises and commits:

- `budget_estimator.py` → output customised into `mini-project/budget/budget.md`.
- `runofshow_builder.py` → output customised into `mini-project/day-of/run-of-show.md`.

## Why this set of four

The C4 voice on Week 10 exercises is that the *individual* track and the *team* track of the carry-out are deliberately interleaved. Exercises 1 and 2 are *team* artifacts (one README, one video, shared by the team). Exercises 3 and 4 are *individual* artifacts on Friday (each learner drafts their own emails and their own LinkedIn post, with team review). Saturday and Sunday close on the capstone, which is *individual or pair* — the capstone is a plan for *the learner's* future hackathon, not a team consensus document.

The two-Python-helpers pattern is the C4 default for *generation* exercises that do not need fresh code each week. The same helpers can be re-run with different parameters by future cohorts; the *parameters* are the learning artifact, not the code.

## Running the Python helpers

Both helpers are zero-dependency (Python 3.9+ standard library only). To run:

```bash
# from the exercises/ folder
python3 budget_estimator.py --help
python3 runofshow_builder.py --help

# example invocations
python3 budget_estimator.py --attendees 80 --event-length one-day \
    --mlh-tier local --insurance university --swag-budget 8

python3 runofshow_builder.py --doors-open 09:00 --hacking-hours 7
```

Output is plain text to the terminal. Pipe to a file if you want to capture:

```bash
python3 budget_estimator.py --attendees 80 > budget-baseline.txt
```

Both helpers are intentionally small (under 300 lines each, type-hinted). They are *not* meant to be the final budget tool; they are meant to *anchor the conversation* about line items. Customise the constants at the top of each file if your event has named cost ranges that differ from the C4 defaults.

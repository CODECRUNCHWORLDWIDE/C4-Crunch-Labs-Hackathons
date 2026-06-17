# Capstone Master Guide — Run Your Own Hackathon

> Your C4 capstone is not another project you *build* — it is an event you can *run*. The deliverable is a complete, executable plan to organise and run a one-day campus hackathon, end to end: venue, sponsorship, budget, code of conduct, judging panel, a minute-by-minute run-of-show, and the seven-day post-event close-out. It is the proof that you've crossed from the attendee's side of the table to the organiser's.

This document is the **single source of truth** for the C4 capstone — its deliverable, milestones, rubric, and submission. The Week 10 curriculum folder breaks the same work into a day-by-day plan and gives you the lectures, templates, and tooling; come here when you want the whole picture on one page.

The capstone is a **plan, not a live event.** You do not have to actually run a hackathon to pass. You ship the plan — the 8-week organising timeline, the budget, the run-of-show, the sponsor cold-emails, the code-of-conduct adaptation, and the post-event template. Whether you then run the event live is a decision for after C4. (Roughly a fifth of C4 alumni do, within a year.)

This is a course about the *event format* itself. Weeks 1–9 taught you to scope, build, pitch, and survive a hackathon as a participant. The capstone turns that lens around: the hackathon ecosystem runs on a small number of people who know how to *run* events, and C4 ends with you being one of them.

---

## At a glance

| Aspect              | Detail                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| Deliverable         | An 8-week plan to organise a one-day campus hackathon, committed as a public repo                        |
| Format              | A Markdown plan document + budget + run-of-show + three sponsor cold-emails + code-of-conduct adaptation + post-event template |
| Required submission | Repo URL + a 90-second phone-demo video walking a reader through the plan                                |
| Audience            | Yourself, your prospective co-organisers, the campus student-org office, an MLH organiser-application reviewer, future sponsors |

All tools are free and open-source. You will not be asked to pay for anything to ship this capstone.

---

## Why this is the capstone

Three reasons:

1. **It proves the highest-leverage skill the course can give you.** Anyone can attend a hackathon. Far fewer can run one — secure a venue, close a sponsor, write a defensible budget, recruit a judging panel, and keep a hundred people fed and safe for a day. That is the skill recruiters, student-org boards, and MLH reviewers actually value.
2. **It is reusable, recruiter-grade, and real.** The plan document is what you bring to the campus career centre, to a student-org-leadership interview, to the MLH membership form, and to your first prospective co-organiser. It is not a throwaway exercise; it is an operating spec.
3. **It closes the loop.** You attended (Weeks 7–9). You carried out (Week 10, Lecture 1). Now you organise. The capstone is where you stop being the person who shows up and become the person who makes the event exist.

---

## What "done" looks like — required for the plan

Your capstone repo MUST contain a plan covering all six org-side tracks and the post-event close-out:

- **The four-question gating decision, answered honestly.** Do you have a venue? At least three co-organisers? At least eight weeks of lead time? Any sponsor leads? Failing one is fine; failing two or more is the honest *"not yet"* call — and writing the plan anyway, with the gaps named, is still a pass.
- **The six-track event scope.** Date, venue, capacity, theme, prize pool, judging format — each with its named gate and named failure mode.
- **A defensible budget.** Use the realistic student-event ranges ($1,500–$4,000 for a 50-person event; $5,000–$15,000 for a 150-person event). Name your biggest line items (food, swag, prizes, AV) and your cuttable ones. Use `budget_estimator.py` from the curriculum to sanity-check it.
- **An 8-week organising timeline.** Week-by-week, working backward from event day: MLH application, venue lock, sponsor outreach, judge recruitment, code of conduct, food order, run-of-show finalisation.
- **Three sponsor cold-emails**, drafted with the C4 seven-line structure, plus the named follow-up rhythm (day 0, 7, 14, drop) and a tier menu (Bronze/Silver/Gold/Title).
- **An MLH membership decision** — Local, Member, or Premier — with the reasoning (hardware lab, swag, judge intros, insurance) and the application timeline.
- **Insurance, food, and dietary coverage.** Your chosen insurance route (university-provided, MLH-provided, or third-party policy), a food budget at $8–12 per attendee per meal, and the dietary checklist (vegetarian, vegan, gluten-free, halal, kosher, nut allergies).
- **A code of conduct.** Adapt the MLH or Berlin Code of Conduct, with a named incident-response chain (report channel, on-call organiser, escalation, post-incident debrief).
- **A judging panel plan** using the 3-3-3 rule (three industry, three faculty/staff, three alumni/student judges), with the cold-email pattern, the confirm-and-brief timeline, and the rubric pre-share.
- **A minute-by-minute day-of run-of-show** for a one-day (8–10 hour) event, with staffing per segment. Use `runofshow_builder.py` from the curriculum as a starting scaffold.
- **A seven-day post-event template** — thank-you emails, photo gallery, attendee survey, social wrap-up, financial reconciliation, archive the chat.

Plus a **90-second walkthrough video** (landscape, single take, phone is fine) narrating the plan for a reader who has not read it — the same skill you rehearsed in the Week 10 carry-out.

---

## Learn in the open

Build this where people can see it. A private plan in a Google Doc helps no one and impresses no one.

- **Commit the plan to a public repo** with meaningful, frequent commits. Visible progress beats invisible perfection.
- **Pull in one co-organiser early.** The capstone is *organising*, which is a team sport. Even one conversation with a peer about co-running surfaces gaps you can't see alone.
- **Run a 30-minute teach-back** with two C4 peers before you call it done. Their questions are the audit your plan needs before a real advisor or sponsor sees it.
- **Pre-fill the public MLH Member-tier application** (without submitting). It surfaces every gap in 30 minutes and is itself a useful artifact.

---

## Milestones — the capstone weekend

The capstone is the mini-project of Week 10 and lands across the final weekend. Push commits each day.

| Day      | Milestone                                          | Output                                                              |
| -------- | -------------------------------------------------- | ------------------------------------------------------------------ |
| Saturday | Scope, budget, run-of-show, code of conduct        | Six-track scope + budget + minute-by-minute run-of-show + CoC adaptation, committed |
| Sunday   | Sponsor outreach, post-event template, finalise    | Three sponsor cold-emails + 8-week timeline + post-event template + 90-second video |

Follow the curriculum for the full hour-by-hour breakdown and the lectures that feed each piece:

- **[Week 10 — Post-Event and Organizing Your Own](../../curriculum/week-10-post-event-and-organizing-your-own/00-overview.md)** — the unit this capstone belongs to.
- **[Mini-project — the capstone brief](../../curriculum/week-10-post-event-and-organizing-your-own/07-mini-project/00-overview.md)** — the day-by-day capstone plan.
- **[Lecture 2 — Org-side: venue, sponsors, MLH, insurance, food](../../curriculum/week-10-post-event-and-organizing-your-own/02-lecture-notes/02-org-side-venue-sponsors-mlh.md)** — the gating decision, the six tracks, budgets, MLH tiers.
- **[Lecture 3 — Day-of: judging, run-of-show, code of conduct, prizes](../../curriculum/week-10-post-event-and-organizing-your-own/02-lecture-notes/03-day-of-run-of-show-judging-prizes.md)** — the 3-3-3 judging rule, prize structures, and the minute-by-minute run-of-show.
- **[Resources](../../curriculum/week-10-post-event-and-organizing-your-own/01-resources.md)** — the MLH organizer guide, the NumFOCUS event playbook, and code-of-conduct sources.

---

## Rubric (100 points)

| Category                       | Points | What we look for                                                                                  |
| ------------------------------ | ------ | ------------------------------------------------------------------------------------------------- |
| **Gating decision & scope**    | 15     | Four-question gate answered honestly; six tracks (date, venue, capacity, theme, prizes, judging) each scoped with a named gate |
| **Budget realism**             | 20     | Line items inside the named student-event ranges; biggest and cuttable items named; arithmetic checks out |
| **8-week organising timeline** | 15     | Backward-planned from event day; MLH, venue, sponsors, judges, food, CoC each placed in the right week |
| **Sponsor outreach**           | 15     | Three cold-emails using the seven-line structure; tier menu; follow-up rhythm; realistic conversion assumption |
| **Safety & inclusion**         | 15     | Code-of-conduct adaptation with a real incident-response chain; full dietary checklist; chosen insurance route with who-signs named |
| **Run-of-show**                | 10     | Minute-by-minute one-day schedule with staffing per segment; check-in, quiet-zone, and submissions-close all placed |
| **Post-event close-out**       | 5      | Seven-day template covering thank-yous, survey, photos, financial reconciliation, archive          |
| **Presentation**               | 5      | 90-second walkthrough video is clear, landscape, single take; repo reads cleanly to a stranger    |
| **Total**                      | **100**|                                                                                                   |

A passing capstone is **70+**. An excellent capstone is **90+** — the document you could hand to a campus student-org advisor or an MLH reviewer and have them take it seriously.

The honest *"not yet"* on the gating decision does not cost you points. A plan that names its own gaps clearly scores higher than one that papers over them.

---

## Submission

When you're done:

1. **Make the plan repo public** on GitHub.
2. **Pin it** to your GitHub profile (Profile → Customize your pins).
3. **Upload the 90-second video** somewhere streamable (unlisted YouTube or public Loom — never raw cloud storage).
4. **Link the video** at the top of the repo README.
5. **Share it** with at least one prospective co-organiser and, if you can, your campus student-org office. Their feedback is the first real test of the plan.

The Code Crunch community celebrates organiser capstones — a strong plan is how the *next* Code Crunch hackathon gets born.

---

## After the capstone

The track is ten weeks; the work is years. Your next branches:

- **Run the event.** If all four gating questions are "yes," the start date is the only decision left. Take two co-organisers and go.
- **Attend a regional or national.** HackMIT, TreeHacks, PennApps, BoilerMake, Hack the North, MHacks. You have the toolkit — apply.
- **Judge or mentor a cohort.** Seat-swap from attendee to judge sharpens your grader's eye and feeds back into your own future submissions.
- **Keep the hackathon repo open.** One issue a week, one PR a month — the weekend project becomes a year-round portfolio.

---

## Questions?

- **"I don't have a venue / co-organisers yet."** → Write the plan anyway and answer the four-question gate honestly. *"Not yet"* is a legitimate, passing outcome — the plan documents what you'd need to flip it to "yes."
- **"50 or 150 people?"** → Default to 50. A first event you can actually staff and feed beats a big one you can't.
- **"Cash prizes?"** → Avoid them for student events — cash creates tax and equity headaches. Prefer gift cards, hardware, conference tickets, or mentor sessions.
- **"My budget feels made up."** → Run it through `budget_estimator.py` in the curriculum and anchor every line to the named ranges. A defensible estimate beats a precise-looking guess.

Good luck. Build the plan you'd be proud to hand a sponsor — and then, when you're ready, build the event.

---

*C4 · Crunch Labs — Hackathons. Built in the open.*

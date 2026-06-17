# Week 10 Mini-Project — CAPSTONE — Organise a One-Day Campus Hackathon

## What you are building

The mini-project this week is the **capstone for the entire C4 track**. The deliverable is a complete, paperwork-ready plan to organise a one-day campus hackathon at your university, with a named week-by-week 8-week runway, a budget, a sponsor outreach package, a code-of-conduct adaptation, a judging panel plan, a minute-by-minute day-of run-of-show, and a seven-day post-event template. The capstone is the *proof-of-skill* artifact for the whole 10-week C4 sequence; it is the document the learner brings to the campus career centre, to the student-org-leadership interview, to the MLH organiser-application form, and to the next prospective co-organiser.

You do *not* need to actually run the event. The deliverable is the **plan document**, not a live event. Whether you then go and run the event is a decision for after C4.

## Time-box

Approximately **5–7 hours over Saturday and Sunday**. The capstone is the heaviest single deliverable of the track; it earns its budget. Smaller chunks across both days work better than a single 7-hour marathon.

## Pre-flight

- All exercises (1, 2, 3, 4) complete. Especially Exercise 3 — the three sponsor cold-emails feed directly into the capstone's sponsorship section.
- All homework problems complete. Problems 3, 4, 5, and 6 are re-used directly.
- Lectures 2 and 3 re-read. The named gates, tiers, structures, and run-of-show segments are the templates the capstone instantiates.
- The Python helpers from `exercises/` (`budget_estimator.py`, `runofshow_builder.py`) runnable locally. The capstone uses their output.

## Folder structure for the capstone

Inside `mini-project/`, create the following sub-structure as you work:

```text
mini-project/
├── README.md                          (this file — the spec)
├── PLAN.md                            (the capstone master plan)
├── week-by-week/
│   ├── week-08-pre.md                 (8 weeks out: kickoff)
│   ├── week-07-pre.md                 (7 weeks out: venue + insurance)
│   ├── week-06-pre.md                 (6 weeks out: sponsors + judges)
│   ├── week-05-pre.md                 (5 weeks out: application opens)
│   ├── week-04-pre.md                 (4 weeks out: confirmations)
│   ├── week-03-pre.md                 (3 weeks out: food + AV order)
│   ├── week-02-pre.md                 (2 weeks out: rehearsal + walkthroughs)
│   └── week-01-pre.md                 (1 week out: final brief)
├── sponsorship/
│   ├── email-01-large-tech.md         (from Exercise 3)
│   ├── email-02-regional.md           (from Exercise 3)
│   ├── email-03-foundation.md         (from Exercise 3)
│   ├── tier-menu.md                   (the formal tier menu)
│   ├── mou-template.md                (the one-page MOU)
│   └── deck-template.pdf              (optional — from Challenge 2)
├── code-of-conduct/
│   ├── CODE-OF-CONDUCT.md             (adapted from MLH or Berlin)
│   └── incident-response-chain.md     (named report-channel, on-call, escalation)
├── judging/
│   ├── judges-target-list.md          (3-3-3 rule — 9 named candidates)
│   ├── judge-invitation-email.md      (the cold email template)
│   ├── judge-briefing-script.md       (the 30-min brief-the-judges meeting)
│   └── rubric.md                      (the five-dimension rubric, adapted from Week 9)
├── budget/
│   ├── budget.md                      (the line-by-line budget)
│   └── budget-actuals-vs-plan.md      (the post-event reconciliation template)
├── venue/
│   ├── venue-contact.md               (named contact + signed-confirmation note)
│   ├── venue-walkthrough-checklist.md (1-week-out checklist)
│   └── venue-map.md                   (from Homework Problem 4)
├── day-of/
│   ├── run-of-show.md                 (minute-by-minute schedule)
│   ├── opening-ceremony-script.md     (from Homework Problem 6)
│   ├── closing-ceremony-script.md
│   ├── staffing-schedule.md           (organiser + volunteer assignments)
│   └── signage-list.md
└── post-event/
    ├── close-out-checklist.md         (seven-day template from Lecture 3 §6)
    ├── attendee-survey.md             (from Challenge 1 if completed; otherwise default)
    ├── sponsor-recap-template.md
    └── thank-you-templates/
        ├── sponsor.md
        ├── judge.md
        └── mentor.md
```

This is a *generous* structure — the named C4 default for a serious organising plan. Smaller events can collapse some files into fewer; larger events split them further. Your capstone should populate *at least*: `PLAN.md`, all eight `week-by-week/` files, the `sponsorship/` folder, the `code-of-conduct/` folder, the `judging/` folder, the `budget/budget.md` file, the `venue/venue-map.md` file, the full `day-of/` folder, and the `post-event/close-out-checklist.md` file.

## The 8-week pre-event plan (week-by-week)

Each `week-by-week/week-XX-pre.md` file follows the same structure: *goals*, *named gates*, *named artifacts produced*, *named risks*.

### Week 8 pre-event — Kickoff

- **Goals.** Finalise organising team (≥3 co-organisers); answer the four-question gate; confirm event date and primary venue contact.
- **Named gates.** Date held verbally by venue. MLH membership application submitted (if Member tier).
- **Artifacts.** Organising team roster with named roles. Four-question gate answers (Homework 3). MLH application screenshot.
- **Risks.** Co-organiser drop-out. The named *fix*: have one alternate on standby; over-recruit by one.

### Week 7 pre-event — Venue and insurance

- **Goals.** Venue contract signed. Insurance answer in writing.
- **Named gates.** Venue contract signed (or a written-and-dated hold from the venue contact). Insurance option decided (university / MLH / third-party). Insurance certificate requested.
- **Artifacts.** Signed venue contract or written hold. Insurance confirmation email.
- **Risks.** Venue cancellation. The named *fix*: have one backup venue on standby; do not pay deposit on either until both are confirmed.

### Week 6 pre-event — Sponsors and judges (first wave)

- **Goals.** First wave of sponsor outreach (30–50 cold emails). First wave of judge invitations (industry + faculty).
- **Named gates.** Sponsorship deck PDF finalised. Sponsor outreach tracker (a spreadsheet) populated with at least 30 prospects. First 9 judge invitations sent.
- **Artifacts.** Sponsor outreach tracker. Sent-emails log. Judge invitation tracker.
- **Risks.** Low sponsor reply rate. The named *expected conversion*: 3–8 percent cold; 15–25 percent warm. Plan volume accordingly.

### Week 5 pre-event — Application opens

- **Goals.** Open attendee applications. Marketing push on social media. Theme finalised.
- **Named gates.** Application form live (Devpost, Tally, Google Forms — verify on the platform). Capacity decided (with 20 percent buffer over seated target). Theme published on the event website.
- **Artifacts.** Application form URL. Marketing posts drafted (Twitter, LinkedIn, Instagram). Theme blurb.
- **Risks.** Under-application. The named *fix*: extend application window by 1 week; increase marketing reach via student-org cross-promotion.

### Week 4 pre-event — Confirmations

- **Goals.** Sponsors confirmed in writing (MOU signed). All 9 judges confirmed in writing. Insurance certificate received.
- **Named gates.** All confirmed sponsors have signed MOUs with deposits collected per the agreed payment timeline. All judges have written calendar holds.
- **Artifacts.** Signed sponsor MOUs in `sponsorship/`. Judge confirmation emails archived in `judging/`. Insurance certificate PDF in `venue/`.
- **Risks.** Sponsor backout. The named *fix*: the MOU's force-majeure clause and the deposit policy.

### Week 3 pre-event — Food and AV order

- **Goals.** Catering ordered. AV rental booked. Swag ordered.
- **Named gates.** Caterer contract signed with named *backup caterer* phone number on file. AV rental contract signed. Swag printer order confirmed with delivery date 1 week before event.
- **Artifacts.** Caterer contract. AV rental contract. Swag order confirmation.
- **Risks.** Caterer cancellation. The named *fix*: backup caterer phone number on the lead organiser's phone, day-of.

### Week 2 pre-event — Rehearsal and walkthroughs

- **Goals.** Brief-the-judges meeting (30 minutes). Venue walkthrough (the named *power audit*, *WiFi load test*, *AV check*). Rehearsal of opening ceremony.
- **Named gates.** Judges have read the rubric. Venue walkthrough checklist complete. Opening-ceremony script timed.
- **Artifacts.** Brief-the-judges meeting notes. Venue walkthrough checklist (`venue/venue-walkthrough-checklist.md`). Rehearsal timing notes.
- **Risks.** WiFi or AV failure surfaces at walkthrough. The named *fix*: contact campus IT immediately; plan for the failure with a hotspot or a portable speaker.

### Week 1 pre-event — Final brief

- **Goals.** Final sponsor reminders. Final judge reminders. Final attendee reminders (with logistics, parking, code-of-conduct link). Day-of run-of-show printed and distributed to all organisers.
- **Named gates.** All organisers know their day-of role. All volunteers briefed. Signage printed. Power strips delivered. Backup caterer phone number on the lead organiser's phone.
- **Artifacts.** Final reminder emails (sponsors, judges, attendees). Printed day-of run-of-show. Printed signage.
- **Risks.** Last-minute attendee no-shows. The named *expected rate*: 25–35 percent; planned for in capacity.

## The day-of run-of-show

Use `exercises/runofshow_builder.py` to generate the baseline, then customise. Save the customised version as `day-of/run-of-show.md`. The customised run-of-show:

- Names the doors-open time, the opening-ceremony start, the lunch time, the snacks time, the submissions-close time, the judging-window start and end, the closing-ceremony start, and the teardown end.
- Names the staffing per segment (which organiser is on mic, which volunteer is on check-in, which volunteer is on food).
- Names the *signage placement* — where the registration desk is, where the food line is, where the on-call organiser is, where the quiet zone is.
- Names the *backup phone numbers* — caterer backup, campus IT, faculty advisor, on-call organiser.

## The budget

Use `exercises/budget_estimator.py` to generate the baseline, then customise. Save the customised version as `budget/budget.md`. The customised budget:

- Names each line item with the actual quoted dollar amount (not the range).
- Names the *funding source* per line item (sponsor cash, university student-activities fee, organiser-fronted reimbursement, MLH-provided in-kind).
- Names the *delta versus the estimate*. If the actual quote is +20 percent over the estimate, name why.
- Names the *contingency line* — 10–15 percent of the total as a contingency reserve.

## The code of conduct

Adapt the MLH Code of Conduct (preferred) or the Berlin Code of Conduct. Save as `code-of-conduct/CODE-OF-CONDUCT.md` with attribution at the top. The named *incident response chain* lives in `code-of-conduct/incident-response-chain.md` and lists:

- The **report channel** (a named email and a named phone number).
- The **on-call organiser** rotation (named humans, named shift times).
- The **escalation path** (the faculty/staff advisor for serious incidents; the campus Title IX office for applicable cases).
- The **post-incident debrief** (within 48 hours of event close).

## The judging panel

The 3-3-3 rule. Save the target list as `judging/judges-target-list.md`:

- **Three industry judges** (named humans, named affiliations, named warm-intro path).
- **Three faculty/staff judges** (named humans, named departments, named scheduling constraint).
- **Three alumni or student judges** (named humans, named year of graduation, named connection to the event).

The judge invitation email (`judging/judge-invitation-email.md`) is the C4 cold-email template adapted for judges (Lecture 3 §2). The brief-the-judges script (`judging/judge-briefing-script.md`) is the 30-minute video call agenda. The rubric (`judging/rubric.md`) is the five-dimension Week 9 rubric, adapted with your event's theme weighting.

## The sponsorship package

The three cold emails from Exercise 3 live in `sponsorship/`. Add:

- A formal *tier menu* (`sponsorship/tier-menu.md`) with each tier's dollar range and named deliverables.
- A one-page MOU template (`sponsorship/mou-template.md`) including the named force-majeure clause and the named brand-protection clauses.
- (Optional, from Challenge 2) The 5–8 slide PDF deck.

## The post-event template

The named seven-day close-out from Lecture 3 §6. Save as `post-event/close-out-checklist.md`. Plus:

- The attendee survey (10 questions, from Challenge 1 if completed; otherwise the default in Lecture 3 §6).
- The sponsor recap deck template (`post-event/sponsor-recap-template.md`) for the within-14-days deliverable to sponsors.
- The thank-you templates in `post-event/thank-you-templates/` for sponsors, judges, and mentors.

## The master `PLAN.md`

The `PLAN.md` at the top of `mini-project/` is the *single-document overview* of the entire capstone. Structure:

1. **Event one-pager** — name, date, venue, attendee target, theme, format.
2. **Organising team** — named roles, named co-organisers, named faculty/staff advisor.
3. **Four-question gate** — the honest answers from Homework 3.
4. **MLH tier decision** — the choice and the rationale (Homework 5).
5. **Budget summary** — the total low/mid/high, with the named funding sources.
6. **Sponsorship summary** — the tier menu, the target prospect count, the expected conversion math.
7. **Judging panel summary** — the 9 names, the 3-3-3 split, the rubric overview.
8. **Code of conduct attribution** — which source, what changes were made, where the full document lives.
9. **Insurance summary** — the option, the coverage, the signer.
10. **Food and dietary plan** — meal cadence, per-attendee budget, dietary checklist confirmation.
11. **Day-of run-of-show overview** — the segment breakdown, the staffing.
12. **Post-event close-out overview** — the seven-day template, the named owners.
13. **Risks and mitigations** — top 5 risks, named *fix* per risk.

`PLAN.md` is 600–1,000 words and links to every sub-folder. It is the document a faculty advisor reads in 10 minutes and signs off on. It is the document MLH reviews as part of the membership application. It is the document a co-organiser onboards from.

## Acceptance criteria

- [ ] `PLAN.md` is committed, between 600 and 1,000 words, links to every sub-folder.
- [ ] All eight `week-by-week/week-XX-pre.md` files are committed, each with goals, gates, artifacts, and risks.
- [ ] The `sponsorship/` folder contains all three cold-emails (from Exercise 3), the tier menu, and the MOU template.
- [ ] The `code-of-conduct/` folder contains an adapted code of conduct with attribution and the incident-response chain.
- [ ] The `judging/` folder contains the 3-3-3 target list, the judge invitation template, the brief-the-judges script, and the rubric.
- [ ] The `budget/budget.md` file contains a line-by-line budget with named funding sources and a contingency line.
- [ ] The `venue/` folder contains the venue contact info and the walkthrough checklist.
- [ ] The `day-of/` folder contains the run-of-show, the opening-ceremony script (from Homework 6), the closing-ceremony script, the staffing schedule, and the signage list.
- [ ] The `post-event/` folder contains the seven-day close-out checklist, the attendee survey, the sponsor recap template, and the three thank-you templates.
- [ ] The capstone total file count is between 25 and 40 files.
- [ ] The capstone total word count across all files is between 4,000 and 8,000 words.

## Stretch acceptance criteria (optional)

- [ ] Challenge 2's sponsorship deck PDF is committed under `sponsorship/`.
- [ ] Challenge 1's attendee survey replaces the default in `post-event/attendee-survey.md`.
- [ ] The plan has been read by one human outside the C4 cohort — a faculty advisor, a student-activities staff member, or a peer organiser — and their feedback notes are in `PLAN.md` under a *reviewer feedback* section.
- [ ] The capstone has been pitched to one prospective co-organiser, and that co-organiser has agreed (in writing) to co-organise the event if it goes live.

## What this earns you

The capstone is the *artifact that proves you can run a hackathon, not just attend one*. It is the document that:

- Earns you a 20-minute meeting with the campus student-activities office.
- Earns you a return-conversation from an MLH program manager when you apply for Member-tier membership.
- Earns you a yes from the first sponsor you cold-email if the deck and the plan are both in the attachment.
- Earns you the *organising lead* line on your LinkedIn Experience section the moment the event goes live (and the *aspiring organiser, capstone plan attached* phrasing in the *Featured* section even before).

Without the capstone, you have completed 9 weeks of attendee skills. With the capstone, you have completed 10 weeks of attendee-and-organiser skills. The track ends here. The work begins now.

## Scoring guidance — what a strong capstone looks like

The acceptance criteria above are binary. The scoring guidance below is *qualitative* — what differentiates a passable capstone from a strong capstone from an exceptional one.

### Passable capstone

- Every acceptance-criterion checkbox is met.
- `PLAN.md` exists, hits the 600–1,000-word target, links to every sub-folder.
- All eight `week-by-week/*.md` files exist with goals, gates, artifacts, risks.
- The sponsorship, code-of-conduct, judging, budget, venue, day-of, and post-event folders are populated to floor.
- The capstone would survive a 15-minute read by a faculty advisor and earn a sign-off.

### Strong capstone

- All passable criteria, plus:
- The plan names *specific humans* — by name — for every named role (co-organisers, faculty advisor, sponsor leads, judge target list).
- The budget has *quoted dollar amounts* from at least three line items (caterer, AV rental, swag printer), not just C4-default ranges.
- The sponsor outreach plan names *specific candidate companies*, not just types of companies.
- The judging target list names *9 specific humans* across the 3-3-3 split.
- The venue map (from Homework 4) has a photo or sketch of the *actual room*, not a generic floor-plan.
- The plan has been read by *at least one outside human* (a faculty advisor, a student-org staff member, a peer organiser) and the feedback notes are in the plan.

### Exceptional capstone

- All strong criteria, plus:
- Challenge 1 (attendee survey) and Challenge 2 (sponsorship deck) are both committed.
- The plan has been pitched to *at least one prospective co-organiser*, who has agreed in writing to co-organise.
- The MLH application form has been *pre-filled* (not submitted) and the draft is in the plan as an appendix.
- At least one cold sponsor email has been *actually sent* to a real prospect (with the advisor's sign-off), and any reply is logged in the plan.
- The plan includes a *contingency narrative* — what changes if attendance triples, if the lead venue cancels, if the lead sponsor pulls out, if the faculty advisor changes.

The exceptional capstone is the *live-event-ready* capstone. The strong capstone is the *advisor-sign-off-ready* capstone. The passable capstone is the *C4-completion-ready* capstone. All three are valid endpoints; pick the level that matches your bandwidth and your intent to actually run the event.

## A note on the capstone's audience

The capstone has *four* named audiences. Different sections of the plan speak to different audiences; do not write all of `PLAN.md` for one of them.

1. **Yourself, six months from now.** When the runway begins, you re-read this plan. The plan must be *self-explanatory* — you do not remember every conversation that produced it.
2. **A faculty or staff advisor.** They read the plan to decide whether to back you. They scan for *risk*, *budget*, and *named accountability*. The four-question gate, the insurance section, and the code-of-conduct adaptation are what they look for first.
3. **A prospective co-organiser.** They read the plan to decide whether to join. They scan for *named roles*, *named division of labor*, *named co-organiser commitments* (hours per week, named decisions they own). The organising team section is what they look for first.
4. **A prospective sponsor.** They read the plan as it accompanies the cold email. They scan for *credibility* — venue locked, code of conduct adopted, judging panel under recruitment, past-event recap (or peer-event recap). The sponsorship deck (Challenge 2) is the front door; the plan is the proof.

A capstone that *only* addresses audience 1 reads as a personal notebook. A capstone that *only* addresses audience 2 reads as a risk-management memo. A capstone that *only* addresses audience 4 reads as a marketing brochure. The C4 voice is to write for all four; the section structure of `PLAN.md` is designed so each audience can navigate to *their* section in 30 seconds.

## A final stretch — the back-of-the-plan section

If you have time at the end of the capstone, add one final section to `PLAN.md`: a *back-of-the-plan reflection* (200–400 words) answering three questions:

1. *Of the four-question gate, which one is the weakest answer for my campus right now?* Be honest. Name what is weakest and why.
2. *Of the named org-side failure modes from Lecture 2 §8 and Lecture 3 §8, which two am I most likely to hit?* Be specific. Pre-commit to the named recovery move.
3. *If I had to pick one of the five alumni paths (A through E from the Week 10 README), which one am I on?* Path A (repeat organiser), Path B (regional attendee), Path C (open-source contributor), Path D (judge or mentor), Path E (curriculum contributor)? Honest answers fit one or two; aspirational answers fit all five.

The reflection is not graded; it is the *meaning paragraph* that turns the capstone from a checklist into a plan you actually believe in.

## Closing line

The win is shipping. The capstone is the *shipping artifact for the C4 track itself*. Commit it. Share it. Adapt it. Re-use it. The next organiser of the next event is reading your `PLAN.md` over your shoulder — make sure it is one they can run with.

End of C4 mini-project. End of C4 track.

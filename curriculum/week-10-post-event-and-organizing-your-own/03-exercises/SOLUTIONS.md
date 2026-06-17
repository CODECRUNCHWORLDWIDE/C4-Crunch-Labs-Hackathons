# Week 10 — Exercise Solutions

One defensible solution per exercise. Solutions are *examples*, not the only correct answers. The acceptance criteria in each exercise file are the binding rubric; this file shows what a strong submission looks like.

## Solution — Exercise 1: Recruiter-Grade README

A passing `README-FOR-RECRUITERS.md` for a hypothetical project *FundFlow* (campus emergency-tuition tool). Approximately 270 lines of markdown when committed.

```markdown
# FundFlow — Emergency Tuition-Assistance Decision Tool

Campus students filing for emergency tuition assistance wait an average
of 14 business days for a decision. Many drop classes during that wait;
some leave school entirely. FundFlow compresses the decision to under
48 hours by routing applications through an automated eligibility check,
pre-fetched financial-aid data, and a SMS-delivered confirmation flow.

> Built by Team FundFlow at HackFIU 2026, October 18-19, 2026.

## Demo

[![FundFlow — 90-second demo](./docs/screenshots/title-card.png)](https://youtu.be/aBcDeFgHiJk)

> **Watch the 90-second demo above.** Repo: [github.com/team-fundflow/fundflow](https://github.com/team-fundflow/fundflow) · Devpost: [hackfiu2026.devpost.com/projects/fundflow](https://hackfiu2026.devpost.com/projects/fundflow)

## Stack

- **Frontend:** Next.js 14 (App Router) with Tailwind for styling.
- **Backend:** FastAPI (Python 3.12) with async Postgres via asyncpg.
- **Database:** Postgres 15, hosted on Neon.
- **Deploy:** Vercel (frontend) + Railway (backend).
- **Third-party APIs:** Twilio (SMS), Plaid (financial-aid data lookup), Auth0 (university SSO).
- **Other notable choices:** A Postgres trigger fires the eligibility decision row into a Twilio SMS within 30 seconds of submission; the entire pipeline is one SQL statement plus one webhook.

## Run locally

\`\`\`bash
git clone https://github.com/team-fundflow/fundflow.git
cd fundflow
cp .env.example .env  # then fill in API keys
docker compose up     # builds frontend, backend, and Postgres
\`\`\`

Open `http://localhost:3000`. The eligibility-check flow uses the seeded demo dataset (50 rows in `seeds/eligibility.sql`).

## Screenshots

### Hero
![Hero screen](./docs/screenshots/01-hero.png)
*Application landing page: a single eligibility-check button above the fold.*

### Interaction
![Eligibility result](./docs/screenshots/02-eligibility.png)
*Decision returned in under 2 seconds with the named eligibility reason and the next-step link.*

### Evidence
![Deploy URL screenshot](./docs/screenshots/03-deploy.png)
*Live deployment at fundflow.vercel.app, serving demo traffic during the judging window.*

## Team

| Name | Role | GitHub | LinkedIn |
|------|------|--------|----------|
| Maria Lopez | Backend + deployment | [@mlopez](https://github.com/mlopez) | [linkedin.com/in/mlopez](https://www.linkedin.com/in/mlopez) |
| James Chen | Frontend + UX | [@jchen](https://github.com/jchen) | [linkedin.com/in/jchen](https://www.linkedin.com/in/jchen) |
| Priya Patel | API integrations + judging-day pitch | [@ppatel](https://github.com/ppatel) | [linkedin.com/in/ppatel](https://www.linkedin.com/in/ppatel) |
| Daniel Singh | Design + demo video | [@dsingh](https://github.com/dsingh) | [linkedin.com/in/dsingh](https://www.linkedin.com/in/dsingh) |

## License

MIT — see [LICENSE](./LICENSE).
```

What makes this a strong submission:

- Section 1 opens with the user pain in 3 sentences, names the user, and ends with the outcome.
- Section 2 puts the video link above the repo link.
- Section 3 names framework + database + deploy + third-party APIs; no version-number padding.
- Section 4 is 4 commands; the Docker compose collapses a multi-step setup.
- Section 5 has the named hero / interaction / evidence trio.
- Section 6 has named roles, not "full-stack" labels.
- Section 7 picks MIT explicitly.

## Solution — Exercise 2: 90-Second Phone Demo

The deliverable is the *video URL*, not text. A passing submission has:

- YouTube unlisted URL embedded in the recruiter-grade README Section 2.
- A frame export saved as `docs/screenshots/title-card.png`.
- The `POST-EVENT-LOG.md` Day 3 entry filled in with the URL and the duration (85–95 seconds).

A passing *script* for the same FundFlow project:

```text
Beat 1 — Problem (15 seconds)

"Hi, I'm Priya. Campus students filing for emergency tuition
assistance wait 14 days for a decision. Many drop classes during
that wait. We built FundFlow to decide in under 48 hours."

Beat 2 — Demo (50 seconds, voiceover over screen-record)

"This is the eligibility-check flow. The student authenticates with
their university SSO — that's an Auth0 layer. They confirm two
data points pulled from Plaid: their financial-aid status and
their last term GPA. The Postgres trigger fires the decision row
into a Twilio SMS. From application to text message: 41 seconds
on this demo run. The named decision reason — Tier 2 eligible —
appears in the SMS and as the next-step link in the app."

Beat 3 — Stack (15 seconds, back to camera)

"Stack is Next.js on Vercel, FastAPI on Railway, Postgres on Neon,
with Twilio for SMS and Plaid for the lookup. The named engineering
choice we're proud of is the Postgres-trigger-to-Twilio path —
no microservice, one SQL statement, one webhook."

Beat 4 — Ask (10 seconds, camera)

"Repo and 3-minute demo are linked below. We're open to internships
and full-time roles in civic tech. Thanks for watching."
```

Timed and rehearsed twice, this script lands at 88–92 seconds in delivery.

## Solution — Exercise 3: Three Sponsor Cold-Emails

Three sample emails for the FundFlow / HackFIU 2026 capstone.

### Email 1 — Microsoft (Gold tier, $3,000 ask)

```text
Subject: HackFIU 2026 sponsorship — Florida International University, Oct 18

Hi Sarah,

I'm Maria Lopez, co-organiser of HackFIU 2026, a one-day student
hackathon on October 18 at Florida International University.

We're hosting 80 undergraduate CS, IT, and design students for a 10-hour
build day, with a civic-tech theme. Doors open 9am; demos at 6pm.

We're inviting Microsoft to join as a Gold-tier sponsor at $3,000.
Gold includes logo placement on our website and T-shirt, a branded
recruiter table for the full event, a 5-minute opening-ceremony
speaking slot, and a Microsoft-named track prize ($500 in Azure credits).

The audience skews 60% CS, 25% IT, 15% design; 70% are second-or-third
year undergraduates. We see strong overlap with Microsoft's campus
recruiting funnel for the Miami metro — your March 2026 explorer
intern posting drew 84 applicants from FIU alone.

Full tier menu (deck attached, public link also at
hackfiu2026.com/sponsors).

Could we hold a 20-minute call next Tuesday or Wednesday afternoon
to walk you through the deck and confirm fit?

Best,
Maria Lopez
Co-Organiser, HackFIU 2026
maria.lopez@fiu.edu · linkedin.com/in/mlopez
```

### Email 2 — Citrix (Silver tier, $1,200 ask)

```text
Subject: HackFIU 2026 sponsorship — FIU, Oct 18 (local talent draw)

Hi Marcus,

I'm Maria Lopez, co-organiser of HackFIU 2026, a one-day civic-tech
hackathon on October 18 at Florida International University.

We're hosting 80 undergraduate CS, IT, and design students. As a
Fort-Lauderdale-headquartered employer, your hiring pipeline overlaps
directly with our attendee draw — 92% of our attendees are South
Florida residents.

We're inviting Citrix to join as a Silver-tier sponsor at $1,200,
which includes a branded table during the event (4–8 hours of
recruiter presence), swag distribution at registration, and logo
placement on the website and T-shirt.

The audience is 60% CS, 25% IT, 15% design; 70% second-or-third year
undergraduates; 92% South Florida.

Full tier menu in the linked deck: hackfiu2026.com/sponsors.

Could you confirm interest by October 1? Happy to hold a 10-minute
call if a yes/no is faster after a quick chat.

Best,
Maria Lopez
Co-Organiser, HackFIU 2026
maria.lopez@fiu.edu · linkedin.com/in/mlopez
```

### Email 3 — DigitalOcean Hatch (non-cash, credits + judge)

```text
Subject: HackFIU 2026 — DigitalOcean Hatch partnership ask

Hi Hatch Team,

I'm Maria Lopez, co-organiser of HackFIU 2026, a one-day civic-tech
hackathon on October 18 at Florida International University.

We're hosting 80 undergraduate CS, IT, and design students and would
love to partner with DigitalOcean Hatch on a non-cash basis: $50 in
DO credits for each of our 80 attendees ($4,000 total credit value),
plus one DO engineer as a judge for our 6:00–7:30pm judging window.

In return, we'll feature the Hatch logo on the website and T-shirt,
recite the credits offer at the opening ceremony, and send a recap
deck within 14 days post-event with attendee credit-redemption
counts.

The audience is 60% CS, 25% IT, 15% design; the civic-tech theme
aligns with several Hatch alumni projects in the public-good
category.

Could you confirm by September 20? Happy to share a deeper deck or
hold a 15-minute call.

Best,
Maria Lopez
Co-Organiser, HackFIU 2026
maria.lopez@fiu.edu · linkedin.com/in/mlopez
```

What makes these strong:

- Each email is tightly *one ask*, one tier, one specific dollar number or non-cash equivalent.
- Each email names a *specific personal angle* (recruiting funnel overlap, geographic match, programme alignment).
- Each email closes with a specific date or call-window.
- All three avoid filler adjectives.

## Solution — Exercise 4: LinkedIn Post + Resume Bullets

A passing LinkedIn feed post (260 words, in spec):

```text
Spent this weekend building FundFlow with three teammates at HackFIU 2026.

The problem: campus students filing for emergency tuition assistance
wait 14 days for a decision. We built a tool that decides in under
48 hours.

What worked: the scope cut on Friday night that dropped the second
feature was the move that made the demo possible. We focused on the
single eligibility-check flow.

What broke: the Plaid sandbox throttled us at hour 14. We swapped
to a static fixture-data layer for the demo, which was the right call
under time pressure but means the deploy is not production-ready yet.

What we'd change: we'd build the Auth0 SSO screen first, not last.
We sank 3 hours on Saturday morning into something the demo barely
needed.

Where it goes next: we're applying to TreeHacks in February with
this team. If you're going, hit one of us up — we'd grab a table
together.

Huge thanks to @James Chen, @Priya Patel, @Daniel Singh and the
HackFIU organising team. Special thanks to our mentor Alex Reyes
who unstuck us on the trigger pattern at hour 11.

Repo: github.com/team-fundflow/fundflow
90-second demo: youtu.be/aBcDeFgHiJk

#hackathon #civictech #studentdev #HackFIU2026
```

Resume bullets:

```text
PROJECTS

FundFlow — Emergency Tuition-Assistance Decision Tool
HackFIU 2026 · Team of 4 · 24-hour hackathon · October 2026

  - Built and deployed an emergency-tuition-assistance decision tool
    that reduces decision time from 14 days to under 48 hours.
  - Designed the Postgres-trigger-to-Twilio SMS pipeline that fires
    eligibility decisions in 41 seconds end to end on the demo dataset.
  - Integrated Auth0 SSO, Plaid financial-aid lookup, and Next.js on
    Vercel; shipped to a public demo URL by hour 22 of the event.
  - Placed 2nd of 18 teams in the Civic Tech track; 90-second demo
    video received 240 views in the first 7 days post-event.
```

Each bullet starts with a verb, names a measured outcome where available, sits at 16–22 words.

## Solution — Python helpers

Both helpers are runnable as-is. Sample invocations:

```bash
$ python3 budget_estimator.py --attendees 80 --event-length one-day \
    --mlh-tier local --insurance university --swag-budget 8
# Output: a budget table with line items and a low/mid/high total.

$ python3 runofshow_builder.py --doors-open 09:00 --hacking-hours 7
# Output: a minute-by-minute schedule with start, end, duration, staffing.
```

The capstone (mini-project) uses these outputs as inputs to the 8-week plan's budget and run-of-show sections. Do not edit the scripts to fit a specific event in this exercise; the *parameters* are the customisation point.

## Common feedback patterns from the C4 cohort

The submissions below are *representative* of what passes and what falls short, based on cohort grading patterns. Use the patterns to self-audit before committing.

### What passes the bar consistently

- Recruiter-grade READMEs that *open with the user pain*. Section 1 names the user in the first sentence. Section 1 does not contain the word *"hackathon"* until the byline at the end of the paragraph.
- 90-second phone demos that have a *human face on camera* for at least Beats 1, 3, and 4. The face is the trust signal; screen-record-only videos score lower in the cohort grading rubric.
- Sponsor cold emails that name a *specific candidate*, not "a relevant company." The personal angle in the email body is what differentiates a 3-percent reply rate from an 8-percent reply rate.
- LinkedIn posts that *credit teammates by handle*. Posts that read as solo work for team projects are flagged by reviewers.
- Resume bullets that *quantify the outcome*. Latency numbers, placement positions, view counts, conversion rates. Vague bullets ("led the engineering team") score lower than specific bullets ("integrated three APIs, shipped to public URL by hour 22").

### What falls short most often

- README Section 4 (run locally) with more than 6 commands. The 6-command floor is hard. If your project requires 10 commands to start, write a Dockerfile.
- Demo videos longer than 95 seconds. The cap is binding; cuts that come from over-the-cap rehearsal are noticeably tighter.
- Sponsor emails over 280 words. Sponsorship reps skim; emails over 280 words do not get skimmed past line 3.
- LinkedIn posts without the demo link or the repo link. The post is a dead-end without both.
- Resume bullets that pad ("Worked collaboratively in a team environment"). Strip every adjective; replace with a measured fact.

### A note on cross-team variance

Exercise 1 (the README) has high cohort variance. Strong submissions read as polished portfolio entries; weak submissions read as project READMEs with a few new section headers. The cohort grade gap on Exercise 1 is the widest of any Week 10 exercise.

Exercise 2 (the video) has *bimodal* outcomes — videos either land in the 85–95 second band with a clean four-beat arc, or they miss the cap entirely. The middle ground is rare; learners who write a tight script in Step 1 land cleanly, learners who skip Step 1 over-shoot.

Exercise 3 (the sponsor emails) has consistent variance — every learner gets roughly 7/10 of the structure right on the first attempt; the differentiator is the *named personal angle* in line 4 of each email. Learners who use generic angles ("we think this is a great fit") score lower than learners who use research-derived specifics ("your March 2026 intern posting drew 84 FIU applicants").

Exercise 4 (LinkedIn + resume) has the highest *self-correction* rate. Learners who do the cross-review step in Part D catch the *do not lie about prizes* failure mode 90 percent of the time before publishing. Learners who skip the cross-review publish inflated bullets that they later have to walk back.

## Re-grading guidance

If you submit and the reviewer flags one of the failure modes above, the recovery is fast:

- **README too long.** Cut the run-locally section first (Section 4). If still over 400 lines, cut the screenshots section captions.
- **Video over 95 seconds.** Re-record Beat 2 (the demo segment) with a tighter narration. The other beats are usually already within budget.
- **Sponsor email over 280 words.** Cut line 4 (the audience description) and line 5 (the deliverables) to one sentence each. The named *brevity move* is to merge them into one paragraph.
- **LinkedIn post solo-flavored.** Find every "I built" or "I designed" and replace with "we built" or "we designed." Reserve "I" for the *named individual contribution* clearly attributable to the speaker.
- **Resume bullet inflated.** Replace "Top 3 finalists" or "Award-winning project" with the literal closing-ceremony language — "Placed 2nd of 18 in the Civic Tech track" or "Named winner, Twilio API Track."

Most re-grading lands within one re-submission cycle. The C4 voice on this: the *first draft is not the final draft*; the reviewer feedback is the *first draft of the second draft*.

# Challenge 1 — Design the Post-Event Attendee Survey

## Goal

Design the post-event attendee survey for the capstone hackathon. The survey is the single highest-leverage piece of *learning* the organising team carries forward to next year; without it, the team is guessing. With it, the team has *data* — response rate, attendee NPS, food rating, judging fairness rating, venue rating, named-improvement requests, would-attend-again. The challenge is to design a survey that *will be answered*, not just a survey that *covers everything*.

## Time-box

60–90 minutes.

## Reading

- Lecture 3 §6 (the seven-day post-event close-out, Day 2 entry).
- NumFOCUS Event Playbook — post-event reporting section.
- MLH Organizer Guide — "After your event" section.

## Constraints

- **Length cap.** 10 questions, no more. Surveys longer than 10 questions see response rates collapse to under 15 percent. The named C4 floor for survey response rate is 30 percent.
- **Mix.** Two demographic questions (year, major), four Likert-scale questions (overall, food, judging, venue), two free-text questions (one positive, one growth), one would-attend-again, one open-anything.
- **Time-to-complete.** Survey should complete in 3–5 minutes. Test it yourself; if you cannot complete in 5 minutes, prune.
- **Anonymous by default.** Email collection is *optional* (a final question for those who want to be on next year's mailing list).

## Instructions

### Step 1 — Draft the 10 questions

A defensible structure:

1. *What year are you in?* (Multiple choice: 1st, 2nd, 3rd, 4th, 5th+, graduate.)
2. *What is your primary major or track?* (Multiple choice: CS, IT, Engineering, Design, Business, Other.)
3. *Overall, how would you rate the event?* (Likert 1–5.)
4. *How would you rate the food?* (Likert 1–5.)
5. *How would you rate the fairness of the judging?* (Likert 1–5.)
6. *How would you rate the venue (space, WiFi, AV, power)?* (Likert 1–5.)
7. *What was the single best thing about the event?* (Free text, 200-char cap.)
8. *What is the single biggest thing you'd want changed next year?* (Free text, 200-char cap.)
9. *Would you attend again next year?* (Yes / Probably / Maybe / Probably not / No.)
10. *Anything else you want the organising team to know? (Optional)* (Free text.)
    *Optional: Leave your email if you'd like to be on the next-year mailing list.*

### Step 2 — Pick a survey tool

Free tier acceptable: Google Forms, Typeform free tier, Tally. Open the tool; create the form; share the URL.

### Step 3 — Test the survey

Take the survey yourself. Time it (target: 3–5 minutes). Then ask one C4 peer to take it. Confirm the response time is under 5 minutes and the questions are unambiguous.

### Step 4 — Plan the distribution

- **Channel 1 — Email to all attendees.** Sent Day 2 of the close-out (Lecture 3 §6).
- **Channel 2 — Slack / Discord pin.** Pinned message in the event channel for the duration of the close-out week.
- **Channel 3 — A reminder email at Day 5** to non-responders (use the survey tool's *did not respond* filter, or a simple email-list cross-check).

Target response rate: 30 percent for a one-day event of 50–100 attendees; 25 percent for larger events. Below 25 percent, the survey is statistically thin; consider extending the response window by one week.

## Acceptance criteria

- [ ] 10 questions, exactly.
- [ ] Time-to-complete is under 5 minutes (verified by a peer test).
- [ ] Mix matches the constraint (2 demographic + 4 Likert + 2 free-text + 1 attend-again + 1 open).
- [ ] Survey tool URL is shareable without sign-in.
- [ ] Distribution plan written into the mini-project's post-event template.

## Submission

Commit the survey design (the 10 questions and the rationale) as `mini-project/post-event/attendee-survey.md`. Note the commit in the mini-project README.

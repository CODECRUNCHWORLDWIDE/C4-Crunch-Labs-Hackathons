# Exercise 4 — LinkedIn Post Draft and Resume Bullet

## Goal

Write a LinkedIn post draft and a resume bullet block for the team's hackathon project, using the placement and phrasing conventions from Lecture 1 §5. This exercise is *individual* — every team member completes it for their own LinkedIn profile and their own resume. The artifact lives in two places: a draft in the shared `POST-EVENT-LOG.md` (so the team can review for consistency) and the actual content on each person's LinkedIn and resume.

## Time-box

45–60 minutes total. The LinkedIn post takes 20–30 minutes; the resume bullet takes 15–25 minutes; the cross-review takes 5–10 minutes.

## Pre-flight

- The recruiter-grade README from Exercise 1 is committed.
- The 90-second video URL from Exercise 2 is live.
- Each team member has a LinkedIn account (or is setting one up today).
- Each team member has a current resume.

## Instructions

### Part A — The LinkedIn feed post (every team member)

The LinkedIn *feed post* is the 150–300-word version that goes on the LinkedIn feed. Different from the LinkedIn *long-form article* (1,200–1,500 words) which is optional and rare for first-time post-event writers.

Write the post following the C4 five-beat retro anatomy from Lecture 1 §4, *compressed*:

```
Beat 1 — What we built (1 sentence).
Beat 2 — What worked (1 sentence — name one thing).
Beat 3 — What broke (1 sentence — name one thing).
Beat 4 — What we'd change (1 sentence — name one thing).
Beat 5 — Where it's going next (1 sentence).
```

Plus:

- An opening hook (1 sentence) before Beat 1.
- A team thank-you (1 sentence) after Beat 5.
- The repo link and the 90-second video link in the post.
- The title-card screenshot as the post's image.
- Tag teammates (@mentions) where applicable.

Total length: 150–300 words. Target the lower end. LinkedIn feed posts that scroll past more than three taps lose audience.

Sample:

```
Spent this weekend building FundFlow with three teammates at HackFIU 2026.

The problem: campus students filing for emergency tuition assistance
wait 14 days for a decision. We built a tool that decides in 48 hours.

What worked: the scope cut on Friday night that dropped the second
feature was the move that made the demo possible.

What broke: the eligibility-lookup query timed out at scale; we capped
the demo dataset at 50 rows.

What we'd change next time: we'd build the auth screen first, not last.

Where it goes next: we're applying to TreeHacks in February with this
team. If you're going, hit one of us up — we'd grab a table together.

Huge thanks to @teammate1, @teammate2, @teammate3 and the HackFIU
organising team. Repo: github.com/team/fundflow. 90-second demo:
youtu.be/<id>.

#hackathon #civictech #studentdev #HackFIU2026
```

Save the draft in `POST-EVENT-LOG.md` under Day 4. After the team reviews, post it to LinkedIn.

### Part B — The resume bullet block (every team member)

The named *verb-first bullet pattern*. Project name on one line with the date and team count; two to four bullets below.

Format:

```
PROJECTS

FundFlow — Emergency Tuition-Assistance Decision Tool
HackFIU 2026 · Team of 4 · 24-hour hackathon · October 2026

  - Built and deployed an emergency-tuition-assistance decision tool
    that reduces decision time from 14 days to under 48 hours.
  - Designed the eligibility-lookup edge cache that held 1.2s p50 latency
    under a 50-row demo dataset.
  - Integrated Twilio SMS, Postgres, and Next.js on Vercel;
    shipped to a public demo URL by hour 22 of the event.
  - Placed 2nd of 18 teams in the Civic Tech track;
    demo video received 240 views in the first 7 days post-event.
```

Constraints:

- Each bullet starts with a verb (Built, Designed, Deployed, Integrated, Shipped, Won, Placed, Architected, Owned).
- Each bullet has *one measured outcome* where one is available.
- Each bullet is between 12 and 22 words.
- Two to four bullets total — no more, no less.
- The project name and date line is *one line*, dense, with the team count, the event, and the date.

### Part C — LinkedIn Featured and Projects sections (every team member)

After posting the feed post, also:

1. **Add the project to LinkedIn Featured.** Profile → Add profile section → Featured → Link. Paste the recruiter-grade README URL. Title: `<Project Name> — <Hackathon Name>, <Date>`. Description: 2 sentences (the problem and the outcome). Image: the title-card screenshot.

2. **Add the project to LinkedIn Projects.** Profile → Add profile section → Projects. Project name, URL (the README), associated organisation (if the hackathon was hosted by a recognised organisation), date range (one date), description. Associate teammates' LinkedIn handles.

3. **Pin the GitHub repo.** github.com/<your-handle> → Customize your pins → check the team repo. Pinned repos surface on the GitHub profile; recruiters who land on the GitHub profile see the repo immediately.

Confirmation: each team member updates `POST-EVENT-LOG.md` Day 5 with their name and three yes/no entries (Featured added, Projects added, Pin updated).

### Part D — Cross-review (the team)

After all members complete Parts A, B, C: the carry-out lead reads each member's draft post and resume bullets in `POST-EVENT-LOG.md`. Confirm:

- Phrasing across the team is *consistent* on the project facts (latency number, demo time, placement, prize). Inconsistent facts (one member's bullet says "Top 5 finalist" and another says "Placed 2nd") trigger the named *do not lie about prizes* rule from Lecture 1 §5.
- Each member credits the team appropriately. Solo-flavored ("I built FundFlow") for a team project is the named *team-credit failure mode*. Use "we" for team contributions and "I" only for the named individual contribution.
- All team members have the same demo URL, the same repo URL, the same title-card image.

## Acceptance criteria

- [ ] Each team member has drafted a LinkedIn feed post in `POST-EVENT-LOG.md` (150–300 words, five beats compressed, hook + thank-you, links and image referenced).
- [ ] Each team member has drafted resume bullets in `POST-EVENT-LOG.md` (verb-first, 2–4 bullets, 12–22 words each).
- [ ] Each team member has added the project to LinkedIn Featured.
- [ ] Each team member has added the project to LinkedIn Projects with teammates tagged.
- [ ] Each team member has pinned the team repo on their GitHub profile.
- [ ] The team carry-out lead has cross-reviewed all drafts for fact consistency.
- [ ] No member's draft violates the *do not lie about prizes* rule.

## Common pitfalls

- **Solo-flavored phrasing for a team project.** "I built..." for a 4-person team is misleading. Use "we built" for team contributions; reserve "I" for the *named individual* contributions (Section *Roles* in the README).
- **Adjective-heavy bullets.** "Amazing collaboration on a cutting-edge tool" is the *not-skim-able* mode. Strip every adjective; replace with a measured fact.
- **Inflated placement.** "Top 3 finalists" when the team placed 2nd in one of four tracks is the *do-not-lie* violation. Use the literal phrasing from the closing-ceremony slide.
- **No links.** A LinkedIn post without the repo URL and the video URL is a dead-end post. Both links go in the body, near the bottom, before the hashtags.
- **Too many hashtags.** Three to six is the LinkedIn sweet spot. More than ten reads as spam.

## Submission

Drafts in `POST-EVENT-LOG.md`. Confirmation entries in `POST-EVENT-LOG.md` Day 5. Each member's actual LinkedIn and resume update is *individual*, but the *draft and review* is *team*.

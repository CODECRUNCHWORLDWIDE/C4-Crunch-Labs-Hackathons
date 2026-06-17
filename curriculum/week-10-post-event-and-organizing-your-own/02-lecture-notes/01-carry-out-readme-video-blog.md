# Lecture 1 — Carry-Out, README, Video, Blog

## Why this lecture comes first

The single most under-attended hour of a 24-hour hackathon is the **first hour after the closing ceremony**. Energy is gone, the team is tired, the project is "done," and the team disperses. Two weeks later, three out of four members cannot remember the repo URL. One year later, the recruiter asks "what have you built?" and the team scrambles. The lecture below is the antidote: a named, dated, week-long carry-out plan that turns the *artifact* into a *portfolio entry*, the *demo* into a *recruiter-visible video*, and the *team weekend* into a *resume bullet*. Without this lecture, the previous nine weeks were rehearsal for a moment that vanishes. With it, the moment becomes the entry-point for everything next.

This lecture covers the named seven-day carry-out, the seven-section recruiter-grade README, the 90-second phone-demo arc, the post-event blog/tweet anatomy, and the LinkedIn-and-resume placement convention. It is a deliverable-heavy lecture; every section closes with an artifact the learner produces. The exercises this week run against these artifacts.

## 1. The seven-day carry-out window

The C4 vocabulary calls the seven days after the closing ceremony the **carry-out window**. The choice of word is editorial: hackathons are *takeaway* events; what you carry out of the room decides whether the weekend was a hobby or a portfolio entry.

**Day 0 — Closing day.** Before the team leaves the venue: take five group photos (two indoor with the demo on screen, two outdoor with the venue signage, one with the team holding the prize-or-certificate). Photos older than 24 hours from the event always feel staged.

**Day 1 — The Monday after.** Verify the repo is accessible to all team members. Verify the demo video uploaded successfully (open it in an incognito tab). Verify the Devpost submission (or equivalent) is visible. Send a *one-line group message* to the team thanking them and naming the next-step decision (who owns the carry-out, who is the point of contact for the README, who is uploading the phone-demo video).

**Day 2 — The README pass.** One team member (the named *carry-out lead*) writes the recruiter-grade README. The build README stays technical; the recruiter-grade README is a new file. Section 2 below specifies the structure. Time-box: 60–90 minutes.

**Day 3 — The 90-second phone demo.** One team member records the 90-second phone-demo video. Section 3 below specifies the arc. Upload to YouTube unlisted; paste the link into the recruiter-grade README; the team has now upgraded from "we have a demo video" to "we have *the* recruiter-grade demo video."

**Day 4 — The blog or tweet thread.** One team member drafts the post-event blog or tweet thread. Section 4 below specifies the anatomy. Length follows platform; voice is editorial; credit is explicit.

**Day 5 — LinkedIn and resume.** Each team member individually adds the project to their LinkedIn (Featured + Projects) and their resume (Projects section, verb-first bullets). Section 5 below specifies the placement and the phrasing. This step is *individual*, not collective — every team member's profile changes, not just the carry-out lead's.

**Day 6 — The retro PR.** Open one pull request against the team repo that adds: the recruiter-grade README, the link to the YouTube video, the link to the blog post, the link to the Devpost or equivalent, and a `POST-EVENT-LOG.md` file that the team will commit at week's end. Every team member reviews and approves the PR before merge.

**Day 7 — The thank-yous and the close-out.** Send a thank-you to: the event organisers (one paragraph, link to the team's post-event blog), the judges who scored your table (one paragraph each, with the *positive note from the judging* re-quoted back), the mentors who helped (named with one line per mentor), and the sponsor whose prize or API you used. The thank-you emails are not optional; they are the *follow-the-thread* mechanism that makes you visible the *next* time the same organiser runs an event.

The carry-out window is deliberately one week, not one day. A one-day carry-out leaves no time for the demo upload to render, the README to settle, the photos to be edited, the blog to be drafted, the LinkedIn placement to be considered. A one-week window gives each artifact its own afternoon. Carry-out is a *practice*, not a sprint.

## 2. The recruiter-grade README

The build README is for the next contributor: how to clone, how to install, how to run, the architecture diagram, the contribution guide. The build README is technical, dense, and assumes the reader is going to write code against the project.

The **recruiter-grade README** is for the recruiter: who built it, what it is, where the demo lives, what it took, what the team learned. The recruiter spends less than 60 seconds scanning. Every section above is structured to be skimmable in that window.

The named C4 seven-section template:

1. **Problem statement (one paragraph, three to five sentences).** Open with the user pain. Name the user. Name the moment. Do not start with the tech stack. Do not start with "for HackXYZ 2026 we built..." — the recruiter does not care which hackathon; the recruiter cares about the problem. Example opener that works: *"Campus students filing for emergency tuition assistance wait an average of 14 business days for a decision. Our project, FundFlow, compresses that to 48 hours."*
2. **Demo link (one block, video first, repo second).** A clickable thumbnail to the 90-second YouTube video, or a Loom embed, *above* the repo link. Recruiters watch before they read. The video is the close; the repo is the proof. Order them in that sequence.
3. **Tech stack (a list, one line per layer, no version numbers unless load-bearing).** Front-end framework, back-end framework, database, deploy target, named third-party APIs. Do not list every npm transitive dependency. Do not list "JavaScript" without naming the framework. The recruiter is scanning for *match with their open req*, not auditing your `package.json`.
4. **How to run locally (a code block, three to six commands).** Clone, install, env-var, run. Three to six commands, no more. If the project cannot start in six commands, fix the project or write a Dockerfile and link to the Docker docs in this section. The recruiter does not run it themselves, but the *brevity of the commands* signals *deployability*.
5. **Screenshots (three to five images).** Hero shot first (the screen the user sees first). Two interaction shots (the user using the app). One *evidence* shot (the database dashboard, the deploy URL response, the test suite green). Captioned with one line each. Hosted in the repo under `docs/screenshots/`, referenced with relative paths.
6. **Team and credits (a list, named role per member).** One line per team member. Name, role at the hackathon (front-end, back-end, design, pitch), GitHub handle, LinkedIn handle if public. The role *matters*; recruiters use it to map who-built-what. Do not list everyone as "full-stack" — name the actual division of labor.
7. **License (one line, conventional name).** MIT, Apache-2.0, or "All rights reserved" if the team is not ready to open-source. License decides whether the project can be forked by someone hiring the team; "all rights reserved" is the *default block* most teams unintentionally choose by silence. State it explicitly.

A recruiter-grade README is *between 200 and 400 lines of markdown*. Less than 200 reads as thin; more than 400 reads as a build README that wandered into recruiter territory. The named filename is `README-FOR-RECRUITERS.md`, committed at the repo root, linked from the build `README.md` under a header *"For recruiters: see [README-FOR-RECRUITERS.md](./README-FOR-RECRUITERS.md)."*

The seven-section template is the *floor*. Strong teams add: an *architecture diagram* (one image, hand-drawn or mermaid-rendered), a *what we'd do next* paragraph (the one-paragraph honest list of follow-ups), and a *roles-and-handles* table that doubles as the team's pin-able shareable list. None of those additions replace the seven sections; they extend them.

## 3. The 90-second phone demo

The Week 8 demo was a screen-recorded three-minute video. The recording mode rehearsed the judge-room pitch. The Week 9 mock pitch was the unrecorded judge-room rehearsal. The 90-second phone demo is the *third* mode: the *recruiter-facing*, *consumed-on-a-phone-while-on-the-train*, *attention-span-three-swipes* video. The medium decides the form.

**Why 90 seconds, not three.** The judge-room pitch is three minutes because the judge gives you three minutes. The recruiter gives you the seconds it takes to decide whether to keep watching. The named C4 attention-curve research (cited in `resources.md`) says social video drop-off is steepest between seconds 0–15 and seconds 60–90. The 90-second cap lands the *ask* before the second drop-off. Anything longer survives in *featured-list embeds* and dies in *autoplay scrolls*.

**Why phone-recorded, not screen-recorded.** Two reasons. One: the audience watches on a phone, in landscape, with phone-grade auto-exposure and phone-grade auto-focus. The recording medium matches the consumption medium. Two: phone-recorded video has *a person in it*. The screen-record demo from Week 8 had no human face. The 90-second video puts the speaker's face on camera for at least the first 5 and last 5 seconds. The face is the *trust signal* the screen-record version lacks.

The named four-beat phone-demo arc:

- **Beat 1 — Problem (15 seconds).** Speaker faces camera. One sentence on the user pain. One sentence on the moment. No tech, no team intro, no "for HackXYZ we built." Example: *"Campus students wait 14 days for emergency tuition decisions. We built a tool that decides in 48 hours."*
- **Beat 2 — Demo (50 seconds).** Cut to screen-recording (phone screen-share, or laptop-screen filmed by the phone, or pre-rendered demo video). Voiceover narrates two to three core flows. No live-coding. No menu-tour. No "and you can also..." — only the two to three flows that make the problem feel solved.
- **Beat 3 — Stack (15 seconds).** Cut back to speaker on camera. One sentence on the stack ("Next.js, Postgres, a Twilio SMS layer, deployed on Vercel"). One sentence on the engineering choice the team is proud of ("we cached the eligibility lookup at the edge to keep the 48-hour SLA"). Two sentences total.
- **Beat 4 — Ask (10 seconds).** Speaker faces camera. One sentence: where the repo is, what the team is open to ("we're open to internships and full-time offers; the repo and demo are linked below; thank you for watching").

**Production rules.** Landscape orientation only. Single cut between speaker-on-camera and screen-recording. Captioned title card on-screen for the first 5 seconds (project name, team initials, hackathon name, date). No background music unless the speaker is wearing headphones reviewing the take with a sound engineer (almost never). No b-roll. No animated transitions. The video is *information-dense, not cinematic*.

**Upload destination.** YouTube unlisted is the default. Public is fine if the team has agreed; private is wrong because the link cannot be shared in the README. Loom public is the fallback for teams without a YouTube account. *Never* upload only to Google Drive or Dropbox; cloud-storage links rotate access permissions, expire, and require sign-in. Permanent, unlisted, shareable — those three properties are the floor.

**The captioned title card.** Five seconds, top-left or top-center, white text on a translucent dark band. Project name. Team initials. Hackathon name and date. The card is the first thing a paused video shows; the card is what makes the screenshot useful in LinkedIn embeds.

## 4. The post-event blog or tweet thread anatomy

The post-event write-up is the artifact the team's *peers* see. Recruiters see the README; peers see the blog. Both audiences matter; both shape the team's reputation; both feed the *next* event's network. The named anatomy is the C4 *five-beat retro*.

The five named beats:

1. **What we built (one paragraph).** The same opener as the README problem statement, expanded one sentence further. Name the user pain, name the solution, name the demo link. Audience: the peer scrolling Twitter who has 8 seconds before the thumb moves.
2. **What worked (a list, three items, one sentence each).** The named *brag list* — not arrogant, not falsely modest, just *named*. The C4 voice on this: a team that cannot identify three things that worked is a team that under-credits its own work. Example items: *"the scope cut on Friday night that dropped the second feature was the move that made the demo possible"*; *"the Twilio sandbox swap to a paid trial at hour 14 unblocked the SMS layer"*; *"the README pass at hour 22 was what the judges actually scanned at the table."*
3. **What broke (a list, three items, one sentence each).** The named *honest list*. The named *honest list* is what makes the post-event write-up *useful* — to the team next year, to the cohort behind you, to the recruiter who values self-aware engineers. Example items: *"the eligibility-lookup query timed out at scale; we capped the demo dataset at 50 rows"*; *"the OAuth integration with the campus SSO never landed; we mocked the auth screen"*; *"team-member-name lost connection for three hours overnight; the recovery was rough and slowed the dawn build."*
4. **What we'd change (a list, three items, one sentence each).** The named *honest list* moves into the *what's next* mode. Scope, team, choice of stack, choice of hackathon track. Three items, no more. Example items: *"we'd build the auth screen first, not last"*; *"we'd take a 2-hour split-the-team sleep window, not the 1-hour we did"*; *"we'd cut the second feature on Friday night, not Saturday afternoon."*
5. **The next event we want to attend (one sentence).** Forward-looking. The named *cohort-pulling forward* sentence. Example: *"We're applying to TreeHacks in February; if you're going, hit one of us up and we'll grab a table together."* This sentence is what *pulls the network forward*; it is what makes the blog post recruit the next set of teammates.

**Length per platform.**

- **Twitter / X thread.** Five to seven tweets, one beat per tweet, the demo video in the first tweet, the repo link in the last tweet. Each tweet ≤ 280 characters; the thread reads as a single scroll.
- **Medium or Substack post.** 600–900 words. Five beats expanded to three or four sentences each. One screenshot per section.
- **LinkedIn long-form.** 1,200–1,500 words. Five beats fully expanded. Three screenshots inline. The team-and-credits section reused from the README. The *audience* is *recruiters who read LinkedIn long-form*, which is a different audience from the LinkedIn-feed *post* audience.
- **LinkedIn feed post.** 150–300 words. Beats compressed to one-line each. One image (the title-card screenshot from the 90-second video). The post is the *thumb-scrollable* version; the long-form is the deep-read version.

**Credit rule.** Every team member named at least once, with handle. Every mentor named at least once. The hackathon and organisers named at least once. The sponsors whose API or credits the project used named at least once. Crediting is *cheap and high-leverage*; it makes the named entities *resurface your post* in their own networks. The team gains reach mechanically by attributing reach to others.

## 5. LinkedIn and resume placement

The LinkedIn and resume placement steps are *individual* — every team member updates their own profile and resume. The team carry-out lead does not do this on behalf of the team. The artifact is *personal*.

**LinkedIn — Featured section.** The Featured section is the recruiter-facing surface at the top of the profile, below the headline. Add the project as a *link* with the title `"<Project Name> — <Hackathon Name>, <Date>"`, the description as a 2-sentence summary (problem + outcome), and the *image* as the 90-second video's captioned title-card screenshot. The Featured section displays as a clickable card with the image and title; recruiters click *into* the link. The link should be the recruiter-grade README, not the build README, not the bare GitHub-repo URL.

**LinkedIn — Projects section.** The Projects section is lower on the profile, but it is the *structured* version of the project entry. Project name, project URL (the README), associated organisation (if the hackathon was hosted by a recognised organisation, name it; otherwise leave blank), date range (one date, the event date), description (the README problem statement plus one sentence on the team's role). *Associate* the teammates' LinkedIn handles in the *associated with* field; this cross-links the profiles and surfaces the project on every teammate's profile by default.

**LinkedIn — Experience section.** Only if the hackathon was hosted by a recognised organisation *and* the learner had a named role (organiser, mentor, lead). For an attendee, the Experience section is the wrong section. For an organiser, the Experience section is the *right* section, with the title *"Organising Lead, [Event Name] [Year]"* and a 2-paragraph description that names the event, the audience, the budget, and the outcome.

**Resume — Projects section.** The named *verb-first bullet pattern*. Project name on one line, with the date and the named team-count *(Team of 4 · 24-hour hackathon · HackXYZ 2026)*. Two to four bullets below, each starting with a verb (Built, Designed, Deployed, Integrated, Shipped, Won, Placed). Each bullet ends with a *measured outcome* where one is available — a user count, a latency number, a placement, a prize, a count of demos shipped. Example bullets:

> *Built and deployed FundFlow, a 48-hour emergency-tuition-decision tool, in a 24-hour hackathon (Team of 4 · HackFIU 2026).*
> *— Designed the eligibility-lookup edge cache that maintained 1.2s p50 latency under a 50-row demo dataset.*
> *— Integrated Twilio SMS, Postgres, and Next.js on Vercel; shipped to a public demo URL by hour 22.*
> *— Placed 2nd of 18 teams in the Civic Tech track; demo received 240 views in the first 7 days.*

The resume Projects section is *fact-dense* and *verb-led*. Recruiters scan bullets, not paragraphs. Each bullet is between 12 and 22 words. Pad is not rewarded.

**The named *do not lie about prizes* rule.** If the team placed 2nd in the track, write "Placed 2nd in the Civic Tech track" — not "Top 3 finalists" (the implied claim is *top 3 overall*), not "Award-winning project" (vague enough to be misleading), not "Featured by [sponsor]" unless the sponsor literally published a feature post. The C4 voice on this is firm: hackathons are reputational; padding a single line is reputational debt that compounds.

## 6. The `POST-EVENT-LOG.md` file format

The deliverable for Week 10's individual track is a single committed file in the team repo: `POST-EVENT-LOG.md`. Format below; commit by end of Day 7 of the carry-out window.

```markdown
# Post-Event Log — <Project Name> — <Hackathon Name>, <Date>

## Day 0 — Closing day photos
- [ ] Five group photos taken? (link or note)
- [ ] Photos shared to team drive? (link)

## Day 1 — Verification
- [ ] Repo accessible to all team members? (yes/no)
- [ ] Demo video accessible incognito? (yes/no)
- [ ] Devpost submission visible? (yes/no/url)
- [ ] Team thank-you message sent? (yes/no)

## Day 2 — Recruiter-grade README
- [ ] `README-FOR-RECRUITERS.md` committed? (link)
- [ ] Build README linked to it? (yes/no)
- [ ] Carry-out lead name: <name>

## Day 3 — 90-second phone demo
- [ ] Video recorded? (yes/no)
- [ ] Uploaded to YouTube unlisted (or Loom public)? (link)
- [ ] Embedded in recruiter-grade README? (yes/no)

## Day 4 — Blog or tweet thread
- [ ] Platform: <Twitter / Medium / LinkedIn long-form / LinkedIn feed>
- [ ] Published? (link)
- [ ] Five beats covered? (yes/no)
- [ ] All teammates / mentors / sponsors credited? (yes/no)

## Day 5 — LinkedIn and resume (per team member)
- Member 1 (<name>): LinkedIn Featured (yes/no), Projects (yes/no), Resume (yes/no)
- Member 2 (<name>): ...
- Member 3 (<name>): ...
- Member 4 (<name>): ...

## Day 6 — Retro PR
- [ ] PR opened? (link)
- [ ] All members reviewed? (yes/no)
- [ ] Merged? (yes/no)

## Day 7 — Thank-yous
- [ ] Organisers thanked? (yes/no)
- [ ] Judges thanked? (yes/no/count)
- [ ] Mentors thanked? (yes/no/count)
- [ ] Sponsors thanked? (yes/no/count)

## Reflection (one paragraph, 4–8 sentences)
What did the carry-out week reveal about the team's project, the team's pitch,
and the team's next event? Name one thing each member is taking forward.
```

The format is a checklist *plus* a reflection paragraph. The checklist is the carry-out; the paragraph is the meaning. Both matter; only the checklist is mechanical; the paragraph is where the editorial work lives.

## 7. The C4 voice on carry-out

Carry-out is the cheapest, highest-leverage week of the entire hackathon experience. The build cost the team a weekend of sleep; the carry-out costs a few hours per day for a week. The build is the *prerequisite*; the carry-out is the *multiplier*. Teams that ship without carry-out have built; teams that ship and carry out have *built and been seen*. The difference compounds over years.

A line that re-surfaces in C4 alumni interviews: *"We won the track and then disappeared. The team next to us placed fourth and got two internships out of the demo. We rebuilt the repo a year later just to put it on a resume."*

Do not be that team. Carry out.

## 8. Named carry-out failure modes (and the recovery)

The C4 cohort retros surface the same handful of failure modes across years. Each one has a named recovery move; the recovery is cheap if you start within the seven-day window and expensive if you start later.

- **Failure mode A — the no-named-owner drift.** The team disperses after closing ceremony with a vague "let's write the README this week" and no one writes it. Recovery: assign the *carry-out lead* by name in the Day 1 group message. The role is one person, not the team. The role rotates next event; this event, it has a name.
- **Failure mode B — the screen-record-only video.** The team has the Week 8 three-minute screen-record and tries to reuse it for recruiter outreach. Reuse is fine as a backup; it is not the *primary* recruiter video. The 90-second phone demo is a different artifact, and it produces a measurably higher reply rate when used in the named LinkedIn-and-resume placement.
- **Failure mode C — the build-README-only repo.** The team never writes the recruiter-grade README and asks recruiters to read the build README. The build README assumes the reader is going to write code. The recruiter wants to *click, watch, scan, decide*. Without a recruiter-grade README, the repo is a closed door.
- **Failure mode D — the no-credit blog post.** The team writes a post-event blog without crediting teammates, mentors, sponsors. The post does not *resurface* in others' networks because no one is mentioned to surface it. The named credit rule (Lecture 1 §4) is the *cheap mechanism* for organic distribution.
- **Failure mode E — the inflated resume bullet.** The team places 2nd in one track of four and writes "Top 3 finalists, HackXYZ 2026" on each member's resume. The named *do not lie about prizes* rule (§5) protects long-term reputational capital. The recovery: rewrite the bullet with the literal closing-ceremony language. The audit happens during the cross-review step of Exercise 4.
- **Failure mode F — the LinkedIn Featured section staying empty.** The team adds the project to Projects but forgets Featured. Featured is the *recruiter-facing surface* at the top of the profile; Projects is below the fold. Both matter; Featured matters more for the first 30 seconds of a profile scan.
- **Failure mode G — the dead Google Drive link.** The team uploads the demo video to Google Drive only, and the link rotates access permissions after three months. By the time a recruiter clicks, the video is private. The named upload destination is YouTube unlisted or Loom public — both stable for years.

If your team hits any of A through G in the first 30 days post-event, run the recovery move within 14 days. The cost compounds; the recovery is still cheap if you move fast.

## 9. The named carry-out cadence after the first seven days

The seven-day carry-out is the *intensive* window. After that, the carry-out shifts into a *maintenance* cadence:

- **Days 8–30.** One social-media re-share post (a "one month later" reflection — what changed since the demo). One follow-up to any recruiter or sponsor who replied to the Day 1 thank-you. One LinkedIn update with any new outcome (a placement, a press mention, a follow-on internship).
- **Days 31–90.** Re-share the demo video on a relevant external thread (a sub-reddit, a discord, a peer event's discussion channel) when context fits. Do not spam. Update the README if the project has shipped any post-event changes. Re-pin the repo on GitHub if the pin has rotated.
- **Days 91–365.** Quarterly check on the project status. If the team is still building, the repo's commit graph tells the story; if the team has moved on, the recruiter-grade README is the *frozen artifact* that still works year-round. The video and README continue to earn reach long after the team has dispersed.

The named long-tail mechanic is that the recruiter-grade README and the 90-second video earn approximately *3–8 inbound recruiter messages per year per team member*, indefinitely. The build can grow stale; the artifacts compound. The named C4 voice on this: a recruiter-grade README produced in Week 10 of C4 will still be earning replies in the learner's senior year. That is the long-tail of the carry-out window.

Next lecture: **Lecture 2 — Org-Side: Venue, Sponsors, MLH, Insurance, Food.**

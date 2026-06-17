# Week 8 — Resources

Every resource on this page is **free** and **publicly accessible**. No paywalled books, no signups beyond a free tier. If a link breaks, please open an issue.

## Required reading and watching (work it into your week)

- **Major League Hacking (MLH) — "Hackathon Organizer Guide" (judging chapter).** Re-read the judging and submission chapters once. The same guide you read in Week 7 has a section on the closing ceremony and the judging window that maps directly onto the dry-run's hours 20-24. <https://organize.mlh.io/>
- **Devpost — "Hackathon participant guide" (submission and judging sub-sections).** Devpost's documentation on what counts as a started-during-the-event project, the 3-minute video cap, the public-repo requirement, and the judging window. The dry-run's hour-22 submission package rehearses these constraints. <https://help.devpost.com/hc/en-us/categories/360001712491>
- **Atlassian — "Sprint retrospective" and "Daily stand-up" guides.** The retrospective guide is the source template for the hour-24 retro. The stand-up guide informs the hour-12 handoff stand-up which is structurally a stand-up, not a retro. <https://www.atlassian.com/agile/scrum/retrospectives> and <https://www.atlassian.com/agile/scrum/standups>
- **NumFOCUS — "Project Sustainability and Event Playbook" (public chapters).** The NumFOCUS event playbook is a free, openly licensed document used by open-source community events. The closing-protocol chapter on retrospectives and the post-event follow-up issue pattern is the closest free reference to the C4 retro template. <https://numfocus.org/community/projects> (search "event handbook")
- **MLH — Code of Conduct.** Re-read once. Day-2 fatigue is where CoC violations most often surface; a tired team can mistake snark for banter and snark-at-fatigue for harassment. The MLH CoC is the floor. <https://mlh.io/code-of-conduct>

If you only have time for one, read the Devpost submission sub-section and the Atlassian retrospective guide back-to-back. Thirty minutes of reading; the submission package and the retro are half-written by the time you finish.

## On midnight-slump physiology and team behavior

| Piece | Why | Link |
|------|-----|------|
| **CDC — "Drowsy driving" public health pages** | A free reference on the cognitive-performance cost of sleep deprivation. Reading speed, working-memory, decision quality — all measurable, all worsened at hour 16+ of a hackathon. The reading frames *why* the C4 voice insists the midnight slump is real and not a moral failing. | <https://www.cdc.gov/sleep/about_sleep/drowsy_driving.html> |
| **NIH StatPearls — "Sleep deprivation"** | Open-access medical reference on the physiology. The relevant reading is the cognitive-performance section; the "judgment under fatigue" framing in Lecture 1 is borrowed from this kind of source. | <https://www.ncbi.nlm.nih.gov/books/NBK547676/> |
| **MIT OCW — "Cognitive psychology" open courseware** | Free course materials on attention, working memory, and decision-making under load. Useful background for the day-2 conflict patterns; the patterns are not personality issues, they are predictable cognitive responses. | <https://ocw.mit.edu/> |
| **Atlassian — "Forming, Storming, Norming, Performing"** | Re-read from Week 7. Day 2 is where most teams compress through "storming" into "performing." The dry-run is the rehearsal of the compression. | <https://www.atlassian.com/team-playbook/plays/team-formation> |

The midnight slump is not optional. Plan around it; do not pretend it does not exist.

## On the pivot decision

- **Devpost — public retrospectives by past hackathon winners.** Some winning teams write retrospectives describing the pivot decision they made (or did not make) mid-event. Search "Devpost retrospective pivot" or browse the comments on winning submissions; the honest retros name the hour at which the team almost pivoted. <https://devpost.com/hackathons?status=ended>
- **Y Combinator — "How to evaluate a pivot" essays (free archive).** Paul Graham and Jessica Livingston's free essays on the pivot pattern at a startup scale. The dry-run's pivot is 1/1000th the magnitude but the same shape — the question is "is the new direction more likely to ship?" not "is the new direction better in principle?" <https://www.paulgraham.com/articles.html>
- **GitHub Education Blog — student team retrospectives.** First-person posts from hackathon teams that pivoted (and ones that did not, and regretted it). The relevant reading is the *timing* of the decision — most successful pivots happen before hour 16; most unsuccessful "pivots" are actually scope cuts after hour 16. <https://github.blog/category/community/education/>

The pivot is rare. Most "pivot conversations" should resolve as "no pivot, cut a MUST instead." The reading sharpens the distinction.

## On integration friction and merge protocols

| Resource | Why | Link |
|----------|-----|------|
| **GitHub Docs — "About merge conflicts"** | The mechanical reference. Read once before hour 14. | <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts> |
| **GitHub Docs — "GitHub flow"** | The branching model the dry-run uses. Short branch lifespans, small PRs, fast merges. | <https://docs.github.com/en/get-started/quickstart/github-flow> |
| **Atlassian — "Pull request best practices"** | Free guide on PR sizing, descriptions, and review etiquette. The dry-run's 200-line PR cap and the commit-message template adapt this guide. | <https://www.atlassian.com/git/tutorials/making-a-pull-request> |
| **Conventional Commits** | The free open specification for commit messages. The C4 commit-message template is a relaxed version of this. | <https://www.conventionalcommits.org/> |

The merge protocol is mechanical. The conflict around the merge is human. The resources distinguish.

## On the hour-18 demo cut

- **C4 Week 5 — `SCOPING-WORKSHEET.md`.** The team re-applies the MoSCoW framing at hour 18, this time *deciding* what to cut, not what to plan. Re-read the Week-5 README's section on the SHOULD/COULD rows.
- **C4 Week 6 — Lecture 2 on the three-MUST script.** The demo script is the binding constraint at hour 18 — if a feature is not in the script, cutting it from the build is mechanical. Re-read the script-versus-build distinction.
- **Atlassian — "MoSCoW prioritization" guide.** A free overview of the MoSCoW method used in C4 since Week 5. The hour-18 cut is a MoSCoW conversation re-run under time pressure. <https://www.atlassian.com/agile/project-management/prioritization>

The cut is structural, not emotional. The framework prevents the cut from becoming an argument.

## On the dress rehearsal and recording

- **Devpost — "Tips for recording a demo video."** Re-read from Week 6. The dress rehearsal is the team-mode version of the Week-6 recording. <https://info.devpost.com/blog/hackathon-demo-videos>
- **OBS Studio — open-source screen-recording software.** Free, cross-platform, no signup. The default tool for hackathon demo recording. <https://obsproject.com/>
- **Loom — free tier (up to 25 videos at 5 minutes each, no credit card).** A faster alternative for the 3-minute team demo. Free tier is enough for the dry-run. <https://www.loom.com/>
- **YouTube — unlisted upload guide.** Free, public, link-based access. The recommended publish target for the dry-run's demo video. <https://support.google.com/youtube/answer/157177>

The recording tool does not matter. The discipline of two takes minimum, of the live deploy URL, and of the 3-minute cap matters.

## On submission packaging

- **Devpost — "Submission requirements" reference page.** A free, structured list of what most Devpost hackathons require: project description, built-with tags, GitHub link, demo video link, sometimes a Devpost-hosted gallery. The dry-run's `SUBMISSION.md` cover sheet rehearses this list. <https://help.devpost.com/hc/en-us/articles/360021841991>
- **MLH — "Submission deadlines" (organizer-side documentation).** A free reference on how MLH-affiliated events handle late submissions. The dry-run's hour-23 stop-work rule maps to the real-event's submission cutoff. <https://organize.mlh.io/>
- **GitHub — "Best practices for README files."** Free guide on what a README should contain. The hour-22 README pass adapts this for hackathon repos. <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>

The submission is *what the judges see*. The polish at hour 22 is not vanity; it is the difference between a judge scrolling past your project and a judge reading it.

## On the retrospective

- **Atlassian — "Sprint retrospective" guide.** The source template for the hour-24 retro. Three quadrants compressed into the C4 voice's three sections (kept, changed, dropped). <https://www.atlassian.com/agile/scrum/retrospectives>
- **Google re:Work — "Retrospective: discuss successes and challenges."** Google's open retrospective template. A cross-check on the Atlassian format. <https://rework.withgoogle.com/guides/teams-foster-psychological-safety/steps/>
- **NumFOCUS — Event Playbook retrospective chapter.** Open-source community event template for closing-protocol retros. The C4 retro's "one-word team-health check" inherits from this style. <https://numfocus.org/community/projects>
- **Devpost — public team retrospectives.** Search for terms like "Devpost retrospective lessons learned"; the long-form ones written by winning teams are the highest-signal study material. <https://devpost.com/hackathons?status=ended>

The retro is short. The honesty in the retro is the hard part. The resources help with structure; the team supplies the honesty.

## On day-2 conflict patterns

- **MIT Sloan — "Conflict management in teams" (open lecture slides on OCW).** Re-read from Week 7. Day-2 conflicts shift from task/process (Week 7) to *fatigue-induced relationship* conflicts; the OCW slides name the shift. <https://ocw.mit.edu/>
- **Atlassian Team Playbook — "Working agreements" play.** Re-read from Week 7. The hour-24 retro often updates the working agreements; the play is the template. <https://www.atlassian.com/team-playbook/plays/working-agreements>
- **Crucial Conversations — public summary articles.** Free summary articles cover the "high-stakes, opposing-opinion, strong-emotion" frame. Day-2 conflicts hit all three. Search: `crucial conversations summary opposing opinion`

The patterns are not new in Week 8; their *timing* and the *fatigue context* are new. The reading reframes Week 7's patterns for the day-2 conditions.

## Tools you will use this week (no paid installs)

- **A repo with multi-committer access.** Same one as Week 7. GitHub free public repo is the default.
- **A chat tool.** Same one as Week 7. Slack free / Discord / Microsoft Teams free. The pinned messages from Week 7 are still pinned.
- **A shared doc tool.** Same one as Week 7. The team's scoping worksheet and team contract live here.
- **A video call tool.** Same one as Week 7. Used for the hour-12 handoff stand-up, the hour-20 dress rehearsal, and the hour-24 retro.
- **A screen-recording tool.** OBS, Loom, QuickTime (on macOS), or any free screen recorder. Used for the dress rehearsal.
- **A video host.** YouTube unlisted, Loom, or any free host. Used to publish the team's 3-minute demo.
- **A timer.** Same as Week 7. Run it in-shot during the dress rehearsal so the 3-minute cap is mechanical.

No new tools this week. Day 2 is about using the tools the team already has, under fatigue, without breaking the protocols.

## On the dry-run logistics (day 2)

- **Sleep window planning.** If the team is co-located, plan the sleep window before hour 12. Most teams sleep hours 14-18 or hours 16-20; both work. The discipline is *naming* the sleep window in the log so async expectations are clear.
- **Caffeine-and-water tracking.** A simple counter in the team channel: pinned message updated by each teammate. Drinks fewer than three glasses of water per 4-hour block correlates with the midnight slump's worst hours.
- **Bandwidth check.** If teammates are remote, run a quick bandwidth check before the hour-20 dress rehearsal. Recording against the live deploy URL requires reliable upload bandwidth for the Demo Lead's screen-share.

Logistics is unglamorous. Logistics is the half of a hackathon closing that beginners skip and then spend hour 21 paying for. Front-load it.

## Examples of strong day-2 logs and retros (study samples)

The single best study material is *other teams' day-2 logs and retros*. Three sources, in order of usefulness:

| Source | What you find | How to search |
|--------|---------------|---------------|
| **The C4 cohort archive — past Week 8 dry-run logs** | Other cohort teams' committed `DAY-2-LOG.md` files with retros. Read three. The honest ones name the midnight slump moment; the dishonest ones do not. | Check the C4 archive folder in the repo |
| **Public GitHub repos with `hackathon` topic and committed retros** | A long tail of teams that committed retros during real events. Quality varies; the winners usually have retros. | <https://github.com/topics/hackathon> |
| **Devpost — past winning project repos with linked retros** | Some winning teams link their working repo and a `RETRO.md` from the Devpost submission. The repos with retros committed during the event window show real-time team-mode closing. | <https://devpost.com/hackathons?status=ended> |

The reading skill: read three retros this week, write one sentence per retro on what the team *changed* coming out of the event. Three sentences total. Homework Problem 3 is exactly this exercise.

## Glossary cheat sheet

| Term | Plain English |
|------|---------------|
| **Day 2** | Hours 12 to 24 of the 24-hour simulated hackathon. The closing half. |
| **Hour-12 handoff stand-up** | The midpoint stand-up. Same 3-question template as Week 7's stand-ups, plus an explicit Builder Lead rotation (on 4-person teams) and a MUST-status table with done-row yes/no. |
| **Midnight slump** | The hours-14-to-18 window where cognitive performance drops measurably. The C4 voice names it; the protocols cope with it; the team does not pretend it is not there. |
| **Pivot decision** | A 15-minute structured conversation, usually at hour 14, deciding whether to change the build direction. Most pivot conversations resolve as "no pivot, cut a MUST instead." |
| **Integration friction** | Hours 14 to 18, when two or three teammates' branches first merge to main. The build becomes a team build at this point; the first merge conflicts surface here. |
| **Merge protocol** | The written rules for how branches merge: 30-minute branch-freeze, one-PR-at-a-time, 200-line PR cap, commit-message template, required review. |
| **Demo cut** | The hour-18 conversation that converts an overrunning SHOULD or COULD into a cut, not a late-night marathon. 3-line checklist. |
| **Dress rehearsal** | The hour-20 recording rehearsal. Two takes minimum. Director (Demo Lead), operator (Builder Lead), audience proxy (Comms Lead). |
| **Submission package** | The hour-22 deliverable: public repo URL, live deploy URL, 3-minute demo video URL, `DAY-2-LOG.md` link, `SUBMISSION.md` cover sheet. |
| **`SUBMISSION.md`** | The cover sheet for the submission package. Six sections: project name, team, prompt response, MUST-list-shipped, links, demo-video timestamps. |
| **Stop-work rule** | The discipline of *stopping* at hour 23 even if the team feels there is more to polish. The submission is committed; the team does not re-edit after hour 23. |
| **Retrospective (retro)** | The 30-minute meeting at hour 24. Three sections: kept, changed, dropped. One scribe. One team-health one-word check. One follow-up issue filed in the repo. |
| **Follow-up issue** | A GitHub issue filed in the repo within 24 hours of the retro. One concrete change the team commits to for the next event. |
| **One-word team-health check** | A round where each teammate says one word describing how they feel. Same rule as Week 7: "fine" and "good" are rejected. |
| **The seven day-2 conflict patterns** | Midnight death-march, hour-16 scope creep, pivot stalemate, "I'll just rewrite it" merge fight, recording dispute, attrition burnout, late submission. Lecture 2 §6 and Lecture 3 §5 name each and give a one-sentence intervention. |
| **`DAY-2-LOG.md`** | The committed Markdown file that records hours 12-24. Extends `DAY-1-LOG.md`'s timestamp convention. Includes the retro at the bottom. |

---

*If a link 404s, please open an issue so a future learner has a working version.*

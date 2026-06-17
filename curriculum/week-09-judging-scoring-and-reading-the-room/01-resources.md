# Week 9 — Resources

Every resource on this page is **free** and **publicly accessible**. No paywalled books, no signups beyond a free tier. If a link breaks, please open an issue.

## Required reading and watching (work it into your week)

- **Major League Hacking (MLH) — "Hackathon Organizer Guide" (judging chapter).** Re-read the judging chapter, this time as a *contestant* preparing to be judged. The same chapter Weeks 7 and 8 referenced; the judging section names the rubric template most MLH-affiliated events adopt. <https://organize.mlh.io/>
- **Devpost — "Hackathon participant guide" (judging sub-sections).** Devpost's documentation on how submissions are judged, what judges typically see in the Devpost interface, and the timing of the judging window. The Week-9 mock pitch rehearses what happens *after* the Devpost submission lands. <https://help.devpost.com/hc/en-us/categories/360001712491>
- **NumFOCUS — "Project Sustainability and Event Playbook" (judging chapter).** The NumFOCUS event playbook is a free, openly licensed document used by open-source community events. The judging chapter is the closest free reference to a non-MLH rubric pattern; the five-dimension structure C4 uses borrows from this. <https://numfocus.org/community/projects>
- **GitHub Education — "Student Developer Pack" and "Campus Experts" judging resources.** The GitHub student developer pack ecosystem includes free judging resources from past Campus Expert events. The rubric patterns surfaced in these resources are the third comparator C4 uses (alongside MLH and NumFOCUS). <https://education.github.com/pack> and <https://githubcampus.expert/>
- **MLH — Code of Conduct.** The CoC is the floor for judge-team interactions, including the result-review-request channel discussion in Lecture 3 §4. <https://mlh.io/code-of-conduct>

If you only have time for one, read the MLH judging chapter and the NumFOCUS judging chapter back to back. Thirty minutes of reading; the rubric self-score is half-prepared by the time you finish.

## On the five rubric dimensions

| Piece | Why | Link |
|------|-----|------|
| **MLH organizer guide — sample judging rubric** | The canonical five-dimension rubric most MLH events publish: technical complexity, design and UX, originality, completion (which C4 maps to "polish"), and presentation. Open source under the MLH organizer-resources license. | <https://organize.mlh.io/> |
| **NumFOCUS event playbook — judging chapter** | The open-source community equivalent. Six dimensions in NumFOCUS (the C4 five plus "community fit"); the C4 voice rolls "community fit" into "originality" for simplicity at the cohort scale. | <https://numfocus.org/community/projects> |
| **HackMIT — public judging rubric (past years)** | A large public hackathon's published rubric. HackMIT publishes past rubrics; the weighting (often 25/20/20/20/15 across the five dimensions) is one of several public weight examples. | <https://hackmit.org/> (search past-event archives) |
| **TreeHacks — public judging guide for participants** | Stanford's annual hackathon publishes a guide for participants that explains how the team's submission is evaluated. Open access; the participant-side framing is rare and useful. | <https://www.treehacks.com/> |
| **PennApps — public participant FAQ on judging** | The University of Pennsylvania's hackathon publishes a participant FAQ that describes the table-walk format and the three-rotations-of-judges pattern. Useful as a non-MLH comparator. | <https://pennapps.com/> |

The five dimensions are not a law of physics. They are a community convention. Every event customises; the C4 voice insists on the *common floor* (technical complexity, design, originality, polish, presentation) and lets the event-specific overlay sit on top.

## On the two judging mindsets

- **First Round Capital — "How to Pitch" public guides.** First Round publishes free essays on the investor-mindset pitch. The "demo first, technical detail second" structure (Lecture 2 §1) is borrowed from this style. The investor-mindset judge thinks like a seed-stage investor, just for 4 minutes. <https://review.firstround.com/>
- **Y Combinator — "How to Pitch to Investors" essay (Paul Graham, free archive).** The classic essay on the investor mindset. The Q&A pattern in Lecture 3 §3 borrows the "answer the question you wish they had asked" *anti-pattern* (the C4 voice rejects this; it surfaces in real judging too). <https://www.paulgraham.com/articles.html>
- **Engineering blogs from past hackathon judges.** Public blog posts by engineers who judged hackathons (search "hackathon judging engineering blog"; the GitHub Engineering blog and many companies' engineering blogs occasionally publish post-event reflections). The engineer-mindset judge thinks about code quality, scalability, and engineering tradeoffs. <https://github.blog/category/engineering/>

The two mindsets are not exhaustive. Some judges are pure engineers; some are pure investors; most are some mix. The C4 voice teaches the *poles* so the team can read the room and adjust within the first 20 seconds.

## On the 3-minute pitch arc

| Resource | Why | Link |
|----------|-----|------|
| **Toastmasters International — public speaking guides** | A free worldwide community whose curriculum covers timed delivery. The 3-minute pitch is structurally a "speech" in Toastmasters terms. The body-language guidance in Lecture 3 §2 borrows from Toastmasters' public-domain training materials. | <https://www.toastmasters.org/resources> |
| **Devpost blog — "Tips for recording a demo video"** | Re-read from Week 6. The recording version is the floor; the live version is the load test. | <https://info.devpost.com/blog/hackathon-demo-videos> |
| **GitHub Education blog — student team pitch retros** | First-person post-hackathon reflections from student teams on the pitch they gave. The honest retros name the pitch's failure points; the C4 voice borrows the "demo first" pattern from a pattern-match across these retros. | <https://github.blog/category/community/education/> |
| **Public TED Talk archives on timed delivery** | The 18-minute TED format is not the same as the 3-minute pitch, but the *opening* discipline is the same: name the problem in the first 30 seconds or lose the room. Cherry-pick three TED openings; the cadence is instructive. | <https://www.ted.com/talks> |

The 3-minute arc is a convention. The 30-90-45-15 ratio is a C4 voice recommendation, not a law. Some events publish a 5-minute pitch slot; the same arc rescales (50s problem / 150s demo / 75s tech / 25s ask). The arc is structural, not durational.

## On the live-coding-in-the-demo trap

- **Public hackathon post-mortems on live-coding failures.** Search "hackathon demo went wrong" on Reddit (r/hackathons) and Devpost project comments. The pattern is consistent: the typo cascade, the API rate-limit at the wrong moment, the localhost-not-deployed surprise. The C4 voice's directive ("do not live-code in a 3-minute pitch") is empirical, not stylistic.
- **The "deploy-not-localhost" rule, named in Lecture 2 §4.3.** Tied to Week 8 Lecture 3's "live deploy URL only" rule. The recording-time discipline is the same as the live-pitch discipline.
- **A public Devpost gallery search for "lived-coded" projects.** Most don't win. The post-event comments occasionally surface the failure mode. Search Devpost galleries for keyword "live coding" in past entries.

The trap is reliable. Almost every cohort that includes a live-coder produces a public post-mortem about the typo or the rate-limit. Read three of these once; the lesson sticks.

## On the Q&A drill

| Resource | Why | Link |
|----------|-----|------|
| **MIT Sloan — "Crisis Communication and Q&A" public lecture slides (OCW)** | The bridge-sentence pattern (Lecture 3 §3.4) is borrowed from public crisis-communication training. The judge-room Q&A is not a crisis, but the *bridge mechanic* is the same. | <https://ocw.mit.edu/> |
| **First Round Capital — "How to Handle Q&A in a Pitch"** | Free essays on the investor-pitch Q&A. The "I don't know" sentence pattern (Lecture 3 §3.5) is named here. | <https://review.firstround.com/> |
| **Toastmasters — "Q&A handling" public guide** | A different framing of the same mechanic; useful as a cross-reference. | <https://www.toastmasters.org/resources> |
| **Public talks by ex-hackathon judges describing the questions they asked** | Search YouTube for "hackathon judging Q&A" — past judges have published 10-15 minute retro talks at meetups; the questions named are usually the same five-or-six. | <https://www.youtube.com/> |

The five most-asked questions in the team's specific build are predictable. The exercise of writing them down is the rehearsal. The drill is to make the answer surface in <2 seconds when the question hits.

## On reading the room

- **Public body-language research (open-access).** The four named cues (clipboard pickup, eye-contact loss, lean-back, side-glance) are borrowed from the human-behavior research surfaced in open-access papers and the public TED talk archive. The C4 voice's framing is *named patterns*, not deep nonverbal-communication theory.
- **MIT OCW — "Negotiation and Conflict Management" open courseware.** The lecture on reading the other side's body language has direct application to judge-room reading. <https://ocw.mit.edu/>
- **The Toastmasters guides referenced above.** Public-domain training on the speaker's side of the read — what to *do* when you see a cue, not just how to spot it.

The audience attention curve has a public reference shape — a U-curve, with attention high at the opening, dipping in the middle 50 seconds, and rising again near the close. The four cues are the inflection markers on that curve. The recovery moves are how to climb back up.

## On unfair judging

- **MLH organizer guide — "Handling judging disputes" chapter.** A free reference on the official channel for filing a *result review request* at MLH-affiliated events. The C4 voice on what is fair to push back on borrows from this chapter.
- **Public hackathon retros that name an unfair-judging moment.** Search Reddit r/hackathons for "unfair judging" — the honest retros are the highest signal; the comment threads underneath are often more useful than the original post.
- **NumFOCUS Code of Conduct — community judging principles.** A free reference on what *consistency in judging across teams* means. The C4 voice quotes this in Lecture 3 §4.

The unfair-judging conversation is hard. The resources do not pretend there is a clean answer. The C4 voice teaches the *channel* (the result-review-request, where it exists) and the *boundary* (do not burn the bridge with the judge or the event).

## On being a judge yourself

- **MLH organizer guide — "Recruiting and onboarding judges" chapter.** A free reference on what events expect from their judges. The first-time-judging sidebar in Lecture 3 §5 borrows from this chapter.
- **NumFOCUS event playbook — judging chapter.** Re-referenced for the judge-side framing.
- **GitHub Education — Campus Experts community resources on judging.** First-person posts from Campus Experts who judged events. The "do not coach" rule and the panel-versus-table-walk etiquette are named here. <https://githubcampus.expert/>

If you have not judged before, the sidebar is one read. Sometime in Weeks 10-12 the C4 cohort coordinator will invite some Week 9 grads to judge the Week 7 dry-runs for the next cohort. The invite is not a surprise; the sidebar is the prep.

## Public rubric samples — exact links

The mock pitch in the mini-project requires comparing against three public rubrics. Use any three of the below; the first three are the C4 default:

| Rubric source | Format | Link |
|---------------|--------|------|
| **MLH organizer guide — sample rubric** | 5 dimensions, 1-5 scale, unweighted | <https://organize.mlh.io/> |
| **NumFOCUS event playbook — judging chapter rubric** | 6 dimensions, 1-5 scale, weighted | <https://numfocus.org/community/projects> |
| **HackMIT — past-year judging rubric (search archives)** | 5 dimensions, 1-5 scale, weighted (25/20/20/20/15) | <https://hackmit.org/> |
| **TreeHacks participant guide rubric** | 4 dimensions, 1-10 scale, weighted | <https://www.treehacks.com/> |
| **PennApps participant FAQ rubric** | 5 dimensions, 1-5 scale, weighted | <https://pennapps.com/> |
| **DubHacks (University of Washington) — past-year rubric** | 5 dimensions, 1-5 scale | <https://dubhacks.co/> |
| **CalHacks (UC Berkeley) — public rubric** | 4 dimensions, 1-10 scale | <https://www.calhacks.io/> |
| **YHack (Yale) — past public rubric** | 5 dimensions, 1-5 scale | <https://www.yhack.org/> |

Eight public rubrics. Skim three. The variance teaches the *generalisation*: every event customises; the C4 five dimensions are the shared floor.

## Tools you will use this week (no paid installs)

- **A printed or screen-visible copy of three public rubrics.** Per the prerequisites above.
- **A 3-minute timer.** Phone timer, kitchen timer, watch. The timer is the binding constraint.
- **A video call tool with camera-off mode.** Used for the mock pitch in the mini-project. Zoom free, Google Meet, Discord, Teams free — any of them.
- **A screen-share that does *not* record by default.** The mock pitch should not be recorded; the recording-mode psychology defeats the rehearsal. If the platform records by default, turn recording off explicitly before starting.
- **A scratch document for the Q&A drill.** A Markdown file or a paper notebook for writing the five anticipated questions and the 30-second answers.
- **(Optional) `pitch_timer.py` and `rubric_score.py` from this week's `exercises/` folder.** Small Python CLI helpers; both run on a stock Python 3.10+ install with no external packages.

No new tools this week. Week 9 is about *delivery under live observation*; the tools are just the rehearsal scaffolding.

## On the mock-pitch logistics

- **Judge proxy selection.** A peer from another C4 cohort team is the best judge proxy. A friend who has not heard the build is the second-best. A teammate is the third-best (they already know the answers; the rehearsal teaches the *delivery*, not the *content*).
- **Camera-off mode.** The judge-room is unrecorded. Rehearse without a camera in the loop. If the judge proxy is on a video call, ask them to keep their camera on (their reactions are the data) and the team's camera off.
- **Timer in shot.** The 3-minute timer is in the team's field of view, ticking audibly if possible. The cap is structural, not advisory.
- **Two takes minimum.** Same rule as Week 8's dress rehearsal. Take 1 is the rough cut; take 2 is the lock. If take 1 went sideways at the 90-second mark, take 2 addresses the named failure.

Logistics is unglamorous. Logistics is the half of the rehearsal that beginners skip and then spend the actual judging slot regretting. Front-load it.

## Examples of strong judge-room performances (study samples)

The single best study material is *recorded pitches* from past hackathon finals where the team was in front of judges, not in front of a camera. Three sources, in order of usefulness:

| Source | What you find | How to search |
|--------|---------------|---------------|
| **YouTube channels of large hackathons** | TreeHacks, HackMIT, CalHacks, PennApps, HackTheNorth, MHacks — most publish final-round pitches from past years. The final-round pitches are *not* the same as the recorded demo videos; they are the live delivery in front of a panel. | Search YouTube for "[event name] finalists [year]" |
| **TED-Ed and Toastmasters open archives** | The pitch arc is shorter at hackathons but the delivery muscles are the same. Skim two 5-minute TED-Ed shorts; pattern-match the opening 30 seconds. | <https://www.ted.com/> and <https://www.toastmasters.org/> |
| **Public Q&A footage from past finals** | The same hackathon YouTube channels often include the Q&A after each pitch. The Q&A footage is the highest-signal — the unrehearsed answer is the muscle the team is rehearsing this week. | Same search; filter for "finals Q&A" |

The viewing skill: watch three final-round pitches this week, write one sentence per pitch on what the *first 20 seconds* did. Three sentences total. Homework Problem 3 is exactly this exercise.

## Glossary cheat sheet

| Term | Plain English |
|------|---------------|
| **Five-dimension rubric** | The C4 default rubric. Technical complexity, design and UX, originality, polish, presentation. 1-5 scale per dimension. |
| **Judge-as-engineer** | The judging mindset that prioritises technical depth, code quality, engineering tradeoffs, and scalability. Asks: "what did you build, how hard was the engineering, what would break under load." |
| **Judge-as-investor** | The judging mindset that prioritises user pain, market size, retention, and "would you keep building this." Asks: "who is this for, is there a market, would you keep building it." |
| **The 3-minute arc** | The C4 default pitch structure. Problem (30s) → demo first (90s) → tech briefly (45s) → ask (15s). The 30-90-45-15 ratio is the named C4 ratio. |
| **Demo first** | The discipline of showing the working build within the first 90 seconds of the pitch, before any deep technical explanation. The team that explains the tech before showing the demo loses the room. |
| **The live-coding trap** | The named failure mode of attempting to live-code in the demo. Typo cascade, API rate-limit, localhost-not-deployed. C4 voice directive: do not live-code in a 3-minute pitch. |
| **The Q&A drill** | The exercise of writing the five most-asked questions for the team's specific build, with a 30-second answer per question, rehearsed aloud once before the judging starts. |
| **The bridge sentence** | The sentence pattern for transitioning from a hard question back to the team's strongest answer. Format: "[acknowledge] — [bridge phrase] — [strongest answer]." |
| **The "I don't know" pattern** | The allowed honest answer when the team genuinely does not know. Format: "I do not know. The closest answer I can give is [closest]. If we had two more weeks we would investigate [direction]." |
| **The audience attention curve** | The U-curve of judge attention over a 3-minute pitch. Opening 30s high; middle 50s dip; closing 60s recovery. The named cues are the inflection markers. |
| **The four cues** | Clipboard pickup, eye-contact loss, lean-back, side-glance. The body-language signals from the judge that name the inflection point on the attention curve. |
| **The recovery moves** | One named move per cue. Re-anchor the demo (clipboard pickup); slow the cadence and look at the judge (eye-contact loss); pivot to the ask (lean-back); name the elephant (side-glance). |
| **The result review request** | The official channel (where it exists, mostly at MLH-affiliated events) for filing a post-event review request when the team believes the judging missed something material. |
| **The "do not coach" rule** | The judge-side rule. A judge does not coach the team mid-pitch, mid-Q&A, or mid-table-walk. Coaching is the cohort coordinator's job, not the judge's. |
| **Table-walk** | The judging format where judges rotate through team tables. ~4-minute slots, often 3 rotations of judges. |
| **Panel** | The judging format where the team presents to a single seated panel. ~5-7 minutes, one rotation. |
| **`JUDGE-ROOM-LOG.md`** | The committed Markdown file that records the rubric self-score, the mock pitch take notes, and the mock Q&A transcript. Sits in the same repo as `DAY-1-LOG.md` and `DAY-2-LOG.md`. |

---

*If a link 404s, please open an issue so a future learner has a working version.*

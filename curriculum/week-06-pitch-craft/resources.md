# Week 6 — Resources

Every resource on this page is **free** and **publicly accessible**. No paywalled books, no signups beyond the free tier. If a link breaks, please open an issue.

## Required reading and watching (work it into your week)

- **Y Combinator — "How to give a great demo."** A short blog post (and accompanying 8-minute talk) from the YC partners on what makes a demo land. Ignore the startup-pitch framing; the structural advice — hook with the user, demo on the live thing, end with the ask — is identical to the C4 voice. Search: `YC "how to give a great demo"`.
- **Devpost — "Tips for recording a demo video."** A short post on the mechanics of recording a hackathon demo. The most-useful section is the "common mistakes" list — it overlaps with the five pitch failure modes in Lecture 1 §6: <https://info.devpost.com/blog/hackathon-demo-videos>
- **One past Code Crunch event demo (your choice).** Pick any submission from `SPRING-2025/` of this repo that has a recorded demo. Watch it once at 1.0x. Watch it again at 1.5x. Note which beats land and which drift. The reading skill compounds — three demos this week is better than ten next month.
- **Re-read C4 Week 3 Lecture 1 §7.** The three-minute solo demo from Week 3 is the shape Week 6 sharpens. The lecture is short; the re-read is 10 minutes and frames the second-take comparison.

If you only have time for one, watch one past Code Crunch demo. The exposure to a real-team three-minute pitch is the single best input you can give your first take.

## On pitch structure (free, deeper)

| Piece | Why | Link |
|------|-----|------|
| **Y Combinator — "How to give a great demo"** | The closest thing to a canonical short essay on demo structure. 6 paragraphs. Read once. | Search: `YC how to give a great demo` |
| **Pitchwerk / 16:9 — short blog posts on demo openers** | A range of one-page essays on how the first 30 seconds work. Skip the consulting framing; keep the openers as study samples. | Search: `demo opener hook blog` |
| **Nancy Duarte — "The first 30 seconds" (free articles)** | Duarte's free archive includes short pieces on opener structure. Her longer books are paid; the free posts are enough. | <https://www.duarte.com/blog/> |
| **"How I record my hackathon demo" (dev.to, search query)** | Search dev.to for first-person posts from hackathon winners. The good ones name their take count and what changed between takes. | DuckDuckGo or Google: `dev.to hackathon demo recording` |

The YC piece is the single most-cited essay for demo structure outside the corporate-deck-coaching space. It is short, free, and most learners have not actually read it through to the end. Read it once, then come back to Lecture 1.

## On recording mechanics

- **Loom — free tier.** 25 videos per workspace, 5-minute cap per video on the free plan. A 3-minute demo fits easily. Public links work without sign-up walls for viewers: <https://www.loom.com/>
- **OBS Studio — free, open source.** The professional-grade option. Steeper learning curve; pays off for the dry-runs in Week 7 and the event in Week 10: <https://obsproject.com/>
- **QuickTime Player (macOS, free, pre-installed).** "File → New Screen Recording." Three clicks, no sign-up, exports as `.mov`. The cheapest recording on a Mac: <https://support.apple.com/guide/quicktime-player/>
- **Windows Game Bar (Win+G).** The pre-installed Windows screen recorder. Same simplicity as QuickTime; built into Windows 10 and 11.
- **Phone front camera + screen share.** Record your phone screen pointing at a laptop running the live URL. Crude but works; the audio is usually fine.
- **YouTube unlisted upload.** Free, ad-free for short videos, durable URL: <https://studio.youtube.com/>

C4's default recommendation is **Loom for the first three takes** (fast, frictionless) and **YouTube unlisted for the final submission** (durable, embeds well in READMEs). Use either; the tool is not the skill.

## On the demo-timing strip

- **C4 BRAND.md — the demo-timing strip.** Re-read the "demo timing" section of BRAND.md once. The five-beat strip is the standard every C4 pitch is graded against. The mono-font, strict-band style is intentional: three minutes is not a soft target.
- **The strip itself, for reference.** Copy this into your script file at the top of each take:

```
[ 0:00 — 0:30 ] hook         | who's hurting + the punch
[ 0:30 — 1:15 ] problem      | concrete, narrow, specific
[ 1:15 — 2:45 ] solution     | walkthrough + demo clip
[ 2:45 — 3:00 ] ask          | one ask, one number
```

The bands are tight. The hook is 30 seconds, not 45. The ask is 15 seconds, not 30. Every demo that drifts past 3:00 has lost the strip; every demo that finishes at 2:30 has under-used it. The discipline is the band, not the average.

## On watching yourself

- **The "cringe is the data" rule.** The discomfort of watching your own demo is the highest-signal feedback you will get this week. Sit through it. The notes you write between minute 0:30 and minute 1:30 of your first take are usually the three things that need to change in take 2.
- **Watch at 1.0x first, then 1.5x.** The 1.0x watch catches pacing; the 1.5x watch catches structural drift. Two passes; eight minutes total.
- **Mute the audio and watch the visuals alone.** Do this once on take 1. The visuals tell you whether the demo beat actually shows the MUST verb being performed, or whether you spent 90 seconds on the landing page. The audio-muted watch is the visual audit.
- **Mute the video and listen to the audio alone.** Then do the audio-only audit. The audio tells you whether the hook lands when nothing else is competing. The audio-only watch is the verbal audit.

The four watches (visual + audio + 1.0x + 1.5x) take about 12 minutes total per take. Budget them.

## Hosting and submission

- **YouTube unlisted.** The C4 default for the final submission. Durable URL, embeds in READMEs, no sign-up wall for viewers, indexed only via direct link.
- **Loom public.** Faster to upload; durable enough for a 10-week course. Free tier shows a small Loom branding. Acceptable.
- **Vimeo free.** Cleaner player than YouTube, lower bandwidth caps. Acceptable for a single 3-minute demo.
- **A direct `.mp4` in your repo.** GitHub's 100 MB file limit is the constraint. A 3-minute 720p screen recording is usually 30–80 MB. Works for repos with permissive size budgets.
- **Devpost video field.** If you are submitting the same demo to a real Devpost-hosted event later, Devpost accepts a YouTube/Vimeo URL in its video field. Same URL works for both.

Do not host on a service that requires the viewer to sign up. The judge has 90 seconds; the sign-up wall is the failure.

## Examples of strong pitches (study samples)

The single best study material is *other teams' recorded demos*. Three sources, in order of usefulness:

| Source | What you find | How to search |
|--------|---------------|---------------|
| **Major League Hacking (MLH) past events** | Submission pages with embedded demo videos. The "best overall" winners usually have strong openers. Watch three. | <https://mlh.io/seasons> → click into an event → submission gallery |
| **Devpost — public hackathon submissions with video** | Filter for "submitted" and look for the project's video field. Quality varies; the winners are usually fast to find. | <https://devpost.com/hackathons?status=ended> |
| **YouTube — search `hackathon demo 3 minutes`** | A long tail of recorded demos, both strong and weak. The weak ones teach as much as the strong ones — they show the five failure modes in real time. | <https://www.youtube.com/results?search_query=hackathon+demo+3+minutes> |

The watching skill: watch three demos this week, write one sentence per demo on what their hook did. Three sentences total. Homework Problem 3 is exactly this exercise.

## On the five pitch failure modes

Each failure mode below has a one-sentence test. Lecture 1 §6 elaborates.

- **The buried lede.** "The hook spends 30 seconds setting context before naming the user or the verb." Test: read the first sentence aloud. Does it name a user *and* a verb? If no, the lede is buried; re-write.
- **The feature tour.** "The solution beat clicks through every feature on every page." Test: count the clicks in the solution beat. If >5, the demo is a tour, not a demo; cut to the three MUST verbs.
- **The apology preface.** "Sorry the deploy is slow / sorry the design is rough / sorry I'm reading from notes." Test: are the first 10 seconds an apology? If yes, cut. The apology costs more than the imperfection it covers.
- **The silent demo.** "The pitcher clicks through the demo while the camera is on slides; the audience never sees the live URL move." Test: is the live URL visible during the demo beat? If no, the demo is theatre; re-record on the URL.
- **The missing ask.** "Thanks for watching." Test: does the last 15 seconds name a number, a channel, or a specific next step? If no, the ask is missing; re-write.

Read each test out loud once. You will recognize at least two of them from past school presentations. Naming them is half the cure.

## Tools you will use this week (no paid installs)

- **A recording tool.** Loom free / OBS / QuickTime / Windows Game Bar / phone camera — pick one. Do not buy anything.
- **A timer.** Phone timer, kitchen timer, browser timer. The 3-minute cap is the discipline. Run the timer in-shot if you want; many event judges do.
- **A quiet room.** Twenty minutes of quiet. Bedroom door closed, laptop fan low, dog walked. The audio is half the recording.
- **Your live URL from Week 3.** The deploy URL of your Week-3 solo prototype. If it is dead, re-deploy before Wednesday — or this week's mini-project has no subject.
- **Your `SCOPING-WORKSHEET.md` from Week 5.** The MUST list is the spine of the solution beat. Bring the worksheet open in a tab while writing the script.
- **A scratch text file or paper.** For drafting hooks, problem-paragraphs, and ask-lines. Do not write the first draft of these in your editor — three handwritten alternatives in 5 minutes beats one polished alternative in 20.

## Free tier limits worth knowing

- **Loom free** — 25 videos per workspace, 5-minute video cap. Fine for the four takes this week. The cap will become a concern in Week 10's event-day deliverable; plan to delete old takes.
- **YouTube unlisted** — no caps for short videos. Durable URL. The only thing to watch is that "unlisted" is not "private" — anyone with the URL can view. That is the intent; the cohort will share URLs.
- **Vimeo free** — 500 MB/week upload, 5 GB total. A 3-minute 720p video is usually well under 100 MB. Fine.
- **GitHub repo file size** — single file limit 100 MB; total recommended <1 GB per repo. A direct `.mp4` works for one demo; if you want multiple takes in the repo, host them elsewhere and commit only the link.

## Glossary cheat sheet

| Term | Plain English |
|------|---------------|
| **Demo-timing strip** | The five-beat, three-minute banded strip from BRAND.md: hook (0:30) → problem (0:45) → solution (1:30) → ask (0:15). The bench every pitch is graded against. |
| **Hook** | The first 30 seconds. Names the user, the pain, and the verb the demo will perform. The single most-rewritten beat in any pitch. |
| **Problem beat** | The 45 seconds after the hook. Narrows the pain to a concrete, specific moment. The audience nods or they do not — the test is mechanical. |
| **Solution beat** | The 90 seconds in the middle. Three clicks on the live URL, one MUST verb per click. The build, not the slide deck. |
| **Demo clip** | The single most-quotable 15 seconds of the recording. Lives inside the solution beat, not in addition to it. The line judges remember. |
| **Ask** | The last 15 seconds. One number, one channel, one specific next step. Not "thanks for watching." |
| **The live URL is the backdrop** | The C4 voice's strongest pitch-time claim. The solution beat is filmed against the live URL, not against slides. Slides are for follow-up. |
| **The first-sentence audit** | A 30-second test: read the first sentence of your hook aloud. If it does not contain a user and a verb, re-write. |
| **The last-sentence audit** | A 30-second test: read the last sentence of your ask aloud. If it does not contain a number and a channel, re-write. |
| **The two-take minimum** | You record once. You watch once. You record again. The second take is the artifact; the first take is the data. |
| **The cringe is the data** | The discomfort of watching your own demo is the highest-signal feedback this week. Sit through it. |
| **Buried lede** | A hook that spends 30 seconds setting context before naming the user or the verb. The first pitch failure mode; the fix is the first-sentence audit. |
| **Feature tour** | A solution beat that clicks through every feature instead of the three MUST verbs. The second pitch failure mode; the fix is the cut to three. |
| **Apology preface** | The opening sentence "sorry the deploy is slow." The third pitch failure mode; the fix is to cut the apology, ship what works. |
| **Silent demo** | The solution beat where the live URL is never visible. The fourth pitch failure mode; the fix is to re-record on the URL. |
| **Missing ask** | The closing sentence "thanks for watching." The fifth pitch failure mode; the fix is the last-sentence audit. |

---

*If a link 404s, please open an issue so a future learner has a working version.*

# Mini-Project — The 3-Minute Recorded Demo

> Record a three-minute demo of your Week-3 solo prototype, fit to the demo-timing strip from BRAND.md, host it publicly, and link it in your repo README. The recording is the artifact you keep; the script is the scaffold. The bar is not perfection; the bar is *strip-disciplined* — the hook names a user, the solution is on the live URL, the ask has a number. Two takes minimum; three to four is typical.

This is the only Week 6 deliverable that matters. The two lectures established the demo-timing strip and the recording rehearsal; the exercises drafted the hook and ran takes 1 and 2; the homework sharpened the corners; the optional challenge gave the muscle a 45-minute stress test on a partner's build. They all collapse into one artifact: a **3-minute recorded demo** of your Week-3 build, hosted publicly, linked in your repo README, with the take count stated honestly.

**Estimated time:** ~2 hours of focused recording on Saturday, plus ~0.5 hours of polish on Sunday before submission.

---

## What you will produce

A recorded video, hosted publicly (YouTube unlisted / Loom public / Vimeo free), of a 3-minute demo of your Week-3 solo prototype, walked through against the live URL. The recording is linked in three places:

1. The `## Demo` section of your `hackathon-template` repo's README (or your Week-3 build repo's README, if separate).
2. The `## Demo` section of your portfolio README, if you have one.
3. The Hackathon Operating Document from Week 1 (a one-line update to the "reusable artifacts" section).

The recording is the artifact. The script you wrote across the exercises is committed in `week-06-prep/`; the hosted recording link is in the repo README.

---

## Required structure of the recording

The recording must fit the BRAND.md demo-timing strip:

```
[ 0:00 — 0:30 ] hook         | who's hurting + the punch
[ 0:30 — 1:15 ] problem      | concrete, narrow, specific
[ 1:15 — 2:45 ] solution     | walkthrough + demo clip
[ 2:45 — 3:00 ] ask          | one ask, one number
```

The strip is the bench. Three minutes total. Drift up to 3:10 is acceptable; 3:15+ is over and needs re-cut. Under-runs to 2:50 are acceptable; 2:30 or less means the problem beat is too thin.

### Beat-by-beat requirements

- **Hook (0:00–0:30):** opens with the user and the pain in sentence 1; names the demo verb in sentence 2 or 3. No apology preface. No pitcher introduction in the first 8 seconds.
- **Problem beat (0:30–1:15):** narrows the pain to a specific user, time, and cost. Cites at least one number (a quantity, a duration, an outcome). Ends on the handoff sentence that cues the live URL.
- **Solution beat (1:15–2:45):** the live URL is visible the entire 90 seconds. Three clicks, one MUST verb per click, ~30 seconds per click. The third click ends with the demo clip — the most-quotable 15 seconds.
- **Ask (2:45–3:00):** names a number, a channel, and a specific next step. Not "thanks for watching." 15 seconds, two sentences.

### Recording requirements

- **Recorded on the live URL.** Not localhost. Not a screenshot. Not a pre-recorded localhost capture. The deploy URL the judges would open.
- **One take per submission.** No editing-together of multiple takes into a "best of." The submitted recording is one continuous take.
- **Public host.** YouTube unlisted, Loom public, or Vimeo free. No sign-up walls.
- **Take count noted.** The repo README states "Take N of N" honestly. The transparency rule is the C4 voice's discipline.

---

## The file tree

The mini-project is a hosted recording plus a 3-line block in the repo README. No directories. No video files committed to the repo. The simplicity is the artifact.

```
hackathon-template/   (or c4-week-06-prep-<yourhandle>/)
├── README.md                              (has ## Demo section)
├── TEAM-CONTRACT.md                       (from Week 4)
├── SCOPING-WORKSHEET.md                   (from Week 5)
├── week-06-prep/
│   ├── exercise-01-hooks.md
│   ├── exercise-02-record-v1.md           (has T1 hosted link)
│   ├── exercise-03-record-v2.md           (has T2 hosted link)
│   ├── final-take.md                      (this week's pick + link)
│   └── homework-*.md
└── ... (other Week 2 / 3 / 4 / 5 files)
```

The `final-take.md` file is one page; it contains the final recording URL, the take count, the script's word count, the four-beat measured timings, and a 3-sentence "what I would change for take N+1" note.

---

## The repo README block

The README's `## Demo` section is exactly three lines:

```markdown
## Demo

[Watch the 3-minute demo](https://youtube.com/watch?v=...) (Take 3 of 3)

This recording walks through the Week-3 solo prototype against the live URL at <deploy URL>. Recorded for C4 Week 6 — Pitch Craft.
```

Line 1: the heading. Line 2: the link, with take count in parens. Line 3: a one-sentence caption naming the live URL and the week context. Nothing else in the section.

If the take count is "Take 2 of 2" rather than "Take 3 of 3," that is also acceptable — the two-take minimum is the floor. The honesty is the rule.

---

## The final-take.md file

The mini-project's *committed file* (the recording is hosted externally) is `week-06-prep/final-take.md`. Required contents:

```markdown
# Final Take — Week 6 Mini-Project

## Pick

Hosted URL: <YouTube unlisted / Loom public / Vimeo free URL>
Take count: Take <N> of <N>
Recorded at: <YYYY-MM-DD HH:MM>
Final duration: <m:ss>     (target: 3:00; acceptable: 2:50-3:10)

## Strip audit

Beat lengths (measured from the final take):
  Hook:     <m:ss>   (target 0:30)
  Problem:  <m:ss>   (target 0:45)
  Solution: <m:ss>   (target 1:30)
  Ask:      <m:ss>   (target 0:15)
  Total:    <m:ss>   (target 3:00)

First-sentence audit (Lecture 1 §2.1):
  Sentence 1 names a user?   yes / no
  Sentence 1 names a pain?   yes / no
  Sentence 2 names the verb? yes / no

Last-sentence audit (Lecture 1 §5.2):
  Ask names a number?  yes / no
  Ask names a channel? yes / no

## Script

<paste your final ~415-word script here, with the four beat
 headers visible so a reader can scan-read it in 60 seconds>

## What I would change for take N+1

<3 sentences. Honest. Not "everything is perfect"; not "I gave up."
 The next-take note is a Week 7 input — your dry-run pitch carries
 the same correction.>
```

The file is one page. The hosted recording is the artifact; the file is the audit. Both are required.

---

## Rules

- **You will** record on the live URL of your Week-3 build. Not localhost. Not staging. Not a screenshot of the build.
- **You will** keep the recording to 3:00 ± 10 seconds. The strip is the bench.
- **You will** host the recording on a no-sign-up-wall service (YouTube unlisted, Loom public, Vimeo free).
- **You will** state the take count honestly. "Take 3 of 3" is the C4 default; "Take 2 of 2" is the minimum.
- **You will** link the recording from the repo README's `## Demo` section in exactly three lines.
- **You will** write the recording's script in your *own voice* — not by copy-pasting the lecture examples verbatim. The voice rule still holds: team-room, blameless, scope-discipline-first.
- **You will not** edit multiple takes together into a "best of." The submitted recording is one continuous take.
- **You will not** add slides between beats. The solution beat is filmed against the live URL; the hook and ask may have a single title card but not a deck.
- **You will not** open the recording with an apology. The apology preface is failure mode 3; cut it before take 1.
- **You will not** close the recording with "thanks for watching." The missing ask is failure mode 5; replace it with a number and a channel.

---

## Acceptance criteria

- [ ] A 3-minute recorded demo exists, hosted publicly, reachable in an incognito window without a sign-up wall.
- [ ] The recording's duration is between 2:50 and 3:10.
- [ ] The recording is one continuous take (no edits between beats).
- [ ] The hook (0:00–0:30) passes the first-sentence audit: sentence 1 names a user AND a pain.
- [ ] The problem beat (0:30–1:15) cites at least one number.
- [ ] The solution beat (1:15–2:45) shows the live URL on screen the entire 90 seconds.
- [ ] The solution beat has exactly 3 clicks (one MUST verb per click), not 4+.
- [ ] The ask (2:45–3:00) passes the last-sentence audit: contains a number AND a channel.
- [ ] The take count is stated honestly in the README (e.g., "Take 3 of 3").
- [ ] The repo README's `## Demo` section has the 3-line block (heading + link + caption).
- [ ] The recording link is also added to the Hackathon Operating Document (Week 1) and the portfolio README (if you have one).
- [ ] `week-06-prep/final-take.md` exists with the pick, strip audit, script, and take-N+1 note.
- [ ] Voice is team-room, blameless, scope-discipline-first. No "rockstar" / "ninja" / "10x" / "crush it." No emojis.

---

## Rubric

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Strip fit — all four beats within the timing bands | 25% | Hook 0:25-0:32, problem 0:40-0:50, solution 1:25-1:35, ask 0:13-0:17 |
| Live URL is the backdrop — solution beat shows the URL the entire 90 sec | 20% | No slides, no localhost, no screenshots; clicks visible, results visible |
| Hook lands the user and the pain in sentence 1 | 15% | First-sentence audit passes all three questions |
| Ask names a number and a channel | 15% | Last-sentence audit passes both questions; ask is not "thanks for watching" |
| Take count stated honestly in the README | 5% | "Take N of N" is in the demo section; no pretense of one-take perfection |
| Recording link in 3 required places (template README + portfolio README + Operating Document) | 10% | Three specific links exist; the recording is findable |
| Voice (blameless, team-room, no banned words) | 5% | Reads and sounds like a sticky note from a tired but proud team-room |
| Public, hosted, no sign-up wall | 5% | Incognito-tab test passes; viewer clicks play within 5 sec of arrival |

---

## What this prepares you for

- **Week 7 — Team-Mode Dry-Run, Day 1.** At hour 6 of the dry-run, the team pitches its 6-hour mock build using the same demo-timing strip. The take-1 / four-watches / three-notes / take-2 cycle is the same; the pitcher is now speaking for a team. The script transfers; the pronoun changes.
- **Week 8 — Team-Mode Dry-Run, Day 2.** A second dry-run with a different team and a different prompt. The recording skill is the same; the build is different. The reusability of the strip is what you verify here.
- **Week 9 — Event Recon.** The ask (the 15-second close) gets sharpened with event-specific data — sponsor APIs that align with your build's MUSTs, prize categories whose rubrics reward your demo's verb, judge profiles. The recon week tunes the ask.
- **Week 10 — The Real Event.** The recording you submit at hour 33 of the real event is built on the same strip you recorded this week. The capstone rubric's "Demo video lands the 3-minute structure" line (20% weight) grades on whether your event recording fits the bands you practiced this week. The muscle is the muscle; the build is what changes.

---

## Submission

When done:

1. Confirm the hosted recording is public, no sign-up wall, reachable in an incognito window.
2. Add the 3-line `## Demo` block to your `hackathon-template` repo's README (or your Week-3 build repo's README).
3. Add a line to your Hackathon Operating Document under the "reusable artifacts" section: "Week-3 demo recording: <hosted URL>."
4. Add the same line to your portfolio README if you have one.
5. Commit `week-06-prep/final-take.md` with the pick, strip audit, script, and take-N+1 note.
6. Watch the final recording one more time in an incognito window on a phone. If the play button does not work, fix the host; if the audio is unclear, re-export from your tool.
7. Post in the cohort channel: "Week 6 recording is up at [URL]. Take <N> of <N>. One thing I learned recording myself: <one sentence>." Watch one cohort-mate's recording that day and leave one specific comment on a *beat* they nailed, not a generic compliment.

You are now ready for [Week 7 — Team-Mode Dry-Run, Day 1](../../week-07-team-mode-dry-run-day-1/). In Week 7 you will run the *first 6-hour mock hackathon* with real teammates (or peer-simulated), and you will pitch *that* build at hour 6 using the same demo-timing strip you just recorded this week. The contract is the rhythm; the worksheet is the map; the pitch is the delivery. Together, they are the team-mode preparation for the dry-run.

---

*The win is shipping. You shipped one alone in Week 3. You wrote the contract that lets a team ship together in Week 4. You wrote the map that says which features ship in Week 5. Now you have the recording that says how the build is *seen* in the three minutes the audience gives you. The four artifacts together — contract, worksheet, script, recording — are what your team brings to the event.*

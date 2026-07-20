# Challenge 1 — Pitch Someone Else's Project

**Time estimate:** 30 minutes of paired drill + 15 minutes of written debrief. Total ~45 minutes.

> This is the Week 6 challenge in C4: a paired drill where you write a three-minute demo script and record one take for a *partner's* build, then they do the same for yours. The point is to feel the pitch muscle when the build's story is not yours — when you have to find the hook from a 5-minute walkthrough, when the user is not the one you have been thinking about all week, when the MUST verbs belong to someone else. Five minutes of pitching someone else's build produces more behavior change than 30 minutes of solo polish on your own.

---

## Problem statement

You and one partner (a cohort-mate, a non-C4 friend with a deployed build, or a sibling with a live URL that works) do a 45-minute paired session in two phases: the **script-write** (15 minutes per build, two builds total = 30 minutes) and the **one-take record** (one take per build, run in series). You finish with two recordings — your partner's build pitched by you, and your build pitched by them — and a 15-minute written debrief.

The cross-build constraint matters. The challenge teaches pitch muscle when the *content* of the build is unfamiliar. Working with a C4 partner on your own build re-rehearses what Exercises 1–3 already covered.

---

## Why someone else's project

Exercises 1–3 were on a build you know inside out. This challenge is the reps with a build whose story you must extract in 5 minutes.

> **C4 voice:** the script reads easy when you know the user, the pain, and the verb. It is harder when a real person hands you their build and says "pitch this in three minutes." The drill rehearses the *cold-start hook-finding* muscle that the team needs at hour 0 of a real event, when teammates are introducing their domains.

Your partner does *not* need to know the demo-timing strip. Your job, in fact, is to teach them the strip as you apply it to their build. The teaching is half the muscle.

The partner's build can be any of:

- A cohort-mate's Week-3 solo prototype.
- A non-C4 friend's class project that is deployed.
- A sibling's side-project with a live URL.
- A club initiative's tool ("our team built X for the showcase, here is the link").
- A community-organization tool with a working demo.

The build needs a live URL. The challenge is unworkable without one — the solution beat is filmed against the URL, not against a README.

---

## Acceptance criteria

- [ ] You and your partner each spend 15 minutes writing the strip for the other's build.
- [ ] You each record one 3-minute take pitching the other's build.
- [ ] Both takes are hosted publicly (YouTube unlisted / Loom public / Vimeo free).
- [ ] You commit your take (of *their* build) to your repo as `week-06-prep/challenge-01-partner-pitch.md` with the link, plus a one-paragraph "what was hard about pitching someone else's build" note. (With the partner's permission; redact the build name if needed.)
- [ ] You write a 15-minute debrief at `week-06-prep/challenge-01-debrief.md` covering one moment your strip worked and one moment it broke.
- [ ] You leave the partner with the link to your recording — the artifact is theirs to keep.

---

## How to run the 45 minutes

```
┌────────────────────────────────────────────────────────────┐
│  THE 45-MINUTE CROSS-BUILD PITCH DRILL                     │
│                                                            │
│  Pre-drill (5 min, async): both partners share their live  │
│   URL and a one-sentence prompt. Each opens the other's    │
│   URL once before the call.                                │
│                                                            │
│  Min  0 — 5   Setup. 60-sec strip explanation. Both        │
│               confirm live URLs work.                       │
│  Min  5 —20   Script swap (15 min). You write the strip    │
│               for partner's build; they write the strip    │
│               for yours. Side-by-side, same Zoom/voice.    │
│  Min 20 —25   Record A. Partner records the strip you      │
│               wrote for them, on their URL.                │
│  Min 25 —30   Record B. You record the strip they wrote    │
│               for you, on your URL.                         │
│  Min 30 —35   Swap recordings. Watch the other's take      │
│               of your build for 3 minutes.                  │
│  Min 35 —45   Debrief. 10 minutes of voice debrief — one   │
│               note per partner per take.                    │
│                                                            │
│  Tools: voice or video call. Shared screen for the URL.    │
└────────────────────────────────────────────────────────────┘
```

The "script swap" rule is the key. You write *their* strip; they write *yours*. The cross-write is the muscle — finding the hook in a build that is not yours is the skill the drill teaches.

### The 60-second strip explainer

Memorize this script for minute 0:

> "The three-minute demo strip from BRAND.md: 30 seconds of hook, 45 seconds of problem, 90 seconds of solution on the live URL, 15 seconds of ask. The hook names a user and a pain in sentence 1, and the demo verb in sentence 2. The ask names a number and a channel. The solution is three clicks on the live URL, one MUST verb per click. We will each write the other's strip in 15 minutes, then record once. Ready?"

That is 60 seconds. Do not over-explain. Apply the strip; the explanation deepens as you write.

### Writing someone else's strip in 15 minutes

Three concrete moves for the script-swap:

1. **Open the live URL first.** Click around for 2 minutes. Identify the three MUST verbs (signup, post, reply — or whatever the build does). The solution beat is those three verbs in order.
2. **Ask the partner one question for the hook.** "Who is hurting?" That gives you the user. The pain follows.
3. **Write the ask last.** The build's owner will know the right ask better than you — ask them: "if a judge watches this and likes it, what's the one thing you want them to do?" That is the ask.

The 15-minute write produces a draft strip — 5–6 lines for the hook, 3–4 sentences for the problem, 3 click-bullets for the solution, 1–2 sentences for the ask. Total ~400 words. The partner reviews it before recording.

### Recording the other's strip

You record on *their* URL. Three calibrations:

- **You are the pitcher, not the builder.** The first-person pronoun is "they" or "the team," not "I" or "we." "The team at <build name> shipped X."
- **Use their prompt's verbs.** If their prompt says "post a question," you say "post a question" — not "submit an inquiry." Vocabulary fidelity is the partner's reward for the cross-pitch.
- **One take. No restarts.** Same rule as Exercise 2. The fluffs are the data.

---

## The midpoint check (minute 20)

At minute 20 (script swap done; recording about to start), pause for 30 seconds and check:

- Does the strip you wrote name a user in the hook's first sentence? If no, force a re-write before recording.
- Does the strip you wrote have exactly 3 clicks in the solution beat? If 4+, cut to 3 before recording.
- Does the strip you wrote close with a number and a channel? If no, force-add before recording.

The 30-second check is the difference between a 30-minute drill where you record a strip that fails the audit and a 30-minute drill that ships.

---

## Pitfalls (forewarned)

The drill fails for predictable reasons. Plan around them.

### 1. The partner's build is broken

Their live URL 502s during the recording, or the MUST verb fails on the deploy. You cannot record a working demo of a broken build. Three options, in order:

1. **Pause the drill. The partner spends 10 minutes re-deploying.** Then resume.
2. **Pivot to a static demo for that build.** Record against the README screenshots, narrating "the live URL is currently down; here is the build via screenshots." This is a *honest* take, not a polished one. Acceptable.
3. **Reverse the drill direction.** Skip the broken-URL build; both partners record the *one working URL* with two different strips. The cross-build muscle still gets reps; one direction is fine.

### 2. You become the build's owner

You start telling the partner what their build *should* do. Stop. You are the pitch expert; the build is theirs. If the build is rough, the strip is honest about the roughness — you do not redesign the build mid-pitch.

### 3. The strip drifts past 3:00 on recording

The partner's build is unfamiliar; your narration of the solution beat takes 2 minutes instead of 90 seconds because you are explaining what you are clicking. The fix is to cut the explanation, not to extend the strip. "She clicks. The reply appears." Eight words is enough.

### 4. The 15-minute script cap is ignored

The script-write goes 25 minutes, then 35, then the partner's recording slot is missed. The cap is the discipline. At minute 20, stop the script-write — even if it feels incomplete. The recording is the artifact; the script is the scaffold.

### 5. The debrief is skipped

"We did the drill, we have the recordings, we're done." No. The debrief is where the *learning* is captured. The drill is the data; the debrief is the lesson.

---

## The written debrief

After the drill, write `week-06-prep/challenge-01-debrief.md` with three sections:

```markdown
# Cross-Build Pitch Drill — Debrief

Partner: <handle or pseudonym, with permission>
Date: <YYYY-MM-DD>
Partner's build (one sentence, redacted if needed): <text>
My recording of their build: <hosted URL>
Their recording of my build: <hosted URL>

## One moment my strip worked
- During <beat — hook / problem / solution / ask> on the partner's
  build, I <what happened — found the user fast / cut to 3 clicks
  / named a number in the ask>. The recording landed: <one specific
  observation from watching the take>.

## One moment my strip broke
- During <beat> on the partner's build, I <what happened — buried
  the lede / clicked beyond 3 / closed with "thanks for watching">.
  Behavior change for next event: <one sentence with a when and
  a what>.

## What pitching someone else's build taught me
- <One sentence on what the cross-pitch surfaced that the solo
  pitch did not. Usually one of: the hook is harder when you do
  not pre-know the user / the ask is easier when you do not have
  a personal stake / the solution beat tightens fast when you do
  not over-explain.>
```

Total: 200–300 words. Commit the file. Push.

---

## Rubric (for self-grading)

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| The 15-min script-swap happened against a real clock | 20% | A timer ran; both scripts finished at 15 min, even if rough |
| Each partner recorded one take of the other's build | 25% | Two hosted recordings exist, both reachable in incognito |
| The strips passed the first-sentence and last-sentence audits | 20% | Hook names user + verb; ask names number + channel |
| The solution beats are 3 clicks, not 5+ | 15% | The cross-pitch did not become a feature tour |
| Written debrief committed | 15% | The three-section file, 200–300 words, in the prep repo |
| Voice was team-room and blameless throughout | 5% | Even on a rough take, the debrief stayed strip-disciplined |

---

## Stretch (only if you both finish under 35 minutes)

- **Run the second take on each build.** Each partner watches the take of their build, writes one note, partner re-records. Two takes per build, four total. The compound is the Week 7 dry-run preview.
- **Trade roles for the strip-write.** You wrote the strip for their build; now they edit your strip for their build (or vice versa). The dual-author strip is closer to the team-mode dynamic of Week 7 than the solo-author strip is.
- **Watch both takes side-by-side.** Open both recordings in two windows. Press play simultaneously. Compare hooks. The visual side-by-side surfaces the strip's structural differences that single-watching misses.

---

## Submission

When done:

1. Commit `week-06-prep/challenge-01-partner-pitch.md` (your take of their build, hosted link) and `week-06-prep/challenge-01-debrief.md` to your repo. With permission. Redact if needed.
2. Send the recording link to your partner. They keep the artifact.
3. Post in the cohort channel: "Did the cross-build pitch drill with [a cohort-mate or non-C4 partner]. One thing I learned about pitching someone else's build: <one sentence>." Read one cohort-mate's debrief and leave one specific comment on a *moment they named*, not a generic compliment.

You are now meaningfully readier for [Week 7 — Team-Mode Dry-Run, Day 1](../../week-07-team-mode-dry-run-day-1/), where the cross-build muscle becomes the cross-teammate muscle — pitching a build that *the team* shipped, not the one you alone shipped. The reps you just ran are the reason that team pitch will not feel theoretical.

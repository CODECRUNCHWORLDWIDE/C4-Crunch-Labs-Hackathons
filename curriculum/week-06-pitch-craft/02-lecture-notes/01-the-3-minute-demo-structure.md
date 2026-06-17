# Lecture 1 — The 3-Minute Demo Structure

> **Duration:** ~1 hour of reading.
> **Outcome:** You can write a five-beat three-minute demo script for any MUST-clean build in under 60 minutes. You can defend each beat's length cap — 30s hook / 45s problem / 90s solution / 15s ask — as a *bench*, not a soft target. You can name the five most common pitch failure modes and the one-sentence fix for each. You can run the first-sentence audit on any hook and the last-sentence audit on any ask in 30 seconds each.

If you only remember one sentence from this lecture, remember this:

> **The three-minute demo is not a presentation; it is a banded strip. Five beats, four boundaries, one live URL. The hook names the user; the problem narrows the pain; the solution clicks the three MUST verbs on the live URL; the ask names one number. Everything between those beats is decoration, and decoration loses the demo.**

Week 5 taught you the scoping worksheet — *what* the team ships. Week 6 teaches you the demo script — *how* the team's three MUST items are walked through, on the live URL, in three minutes, in front of an audience whose patience is 90 seconds and whose attention budget for the hook is 30 seconds. The worksheet is the map; the script is the delivery. A team with the map and no script ships and then watches a worse build win the demo session. The asymmetry is the cost of skipping the recording rehearsal.

---

## 1. Why three minutes, and not five

The first reaction beginners have to "your demo is three minutes" is: *that is not enough.* I have so much to show. The build has six features. The judges should see the design system, the API choices, the database schema, the deployment pipeline.

That reaction is wrong on every count. Here is the steel-man:

> **C4 voice:** the judges at hour 33 have watched 40 demos this hour. The two they remember at scoring time are the two with a clear hook and a clear ask. Length does not buy memory; structure does. Three minutes is the bench because three minutes is what the audience can hold without drifting. Anything past 3:00 is borrowing attention you have not earned.

### 1.1 What the three-minute cap actually does

Three short sentences, one per outcome:

- **Three minutes forces the cut.** A four-minute demo always becomes a three-minute demo at the event — by the timer, by the judges' patience, or by a cut-off bell. Practice the cut at hour 0 of the week, not at hour 33 of the event.
- **Three minutes maps to the MUST list.** Three MUST items, 30 seconds of click + narration each, equals 90 seconds of solution beat. The arithmetic is on purpose: the worksheet's MUST cap (3 items) is the script's solution-beat cap (3 clicks).
- **Three minutes is the judge's attention span.** Every hackathon judging rubric in the C4 archive shows attention dropping sharply after 2:45. The 15-second ask exists because that is the last sliver of attention available.

If the three-minute cap does not force any of these three, the cap is decoration. If it forces all three, it is the highest-ROI constraint a pitch follows.

### 1.2 The demo-timing strip — five beats, four boundaries

C4 uses the BRAND.md demo-timing strip as the canonical structure. Re-read BRAND.md once if you have not; this lecture extends it:

```
┌────────────────────────────────────────────────────────────┐
│  THE DEMO-TIMING STRIP — 3-MINUTE EVENT DEMO               │
│                                                            │
│  [ 0:00 — 0:30 ] hook         | who's hurting + the punch  │
│  [ 0:30 — 1:15 ] problem      | concrete, narrow, specific │
│  [ 1:15 — 2:45 ] solution     | walkthrough + demo clip    │
│  [ 2:45 — 3:00 ] ask          | one ask, one number        │
└────────────────────────────────────────────────────────────┘
```

The bands are tight. The hook is 30 seconds, not 45. The ask is 15 seconds, not 30. Every demo that drifts past 3:00 has lost the strip; every demo that finishes at 2:30 has under-used it. The discipline is the band, not the average.

### 1.3 The audience's attention budget at each beat

A hidden curve runs underneath the strip: the audience's attention. It starts at 100% in the first second, drops to about 60% by the end of the hook if the hook is generic, climbs back to 80% if the problem beat is concrete, peaks at 90% on the first successful click of the solution beat, and falls off a cliff after 2:45 if the ask is missing.

> **C4 voice:** the strip is not "three minutes split into four beats." It is "four boundaries where the audience's attention either compounds or collapses." Plan the boundary, not the beat.

Three implications:

- **The 0:30 boundary is where most demos lose the room.** A generic hook ("Hi everyone, my name is X, I'm here to talk about Y") burns 30 seconds before the audience knows what user is hurting. By 0:30 they have decided to half-listen.
- **The 1:15 boundary is where the demo *starts*.** The first 75 seconds set up the problem; the next 90 are the build. If the live URL is not on screen by 1:15, the demo has not begun.
- **The 2:45 boundary is the last chance to give the audience a reason to do something.** Most pitches close with "thanks for watching." That is not an ask; that is a wave goodbye.

---

## 2. The hook — 0:00 to 0:30

The hook is the single most-rewritten beat in any C4 pitch. It is also the beat where most learners make the first failure-mode mistake. The hook has one job: name a user, name a pain, and promise the verb the demo will perform. Thirty seconds. Three sentences, sometimes four.

### 2.1 The first-sentence rule

```
┌────────────────────────────────────────────────────────────┐
│  THE FIRST-SENTENCE RULE                                   │
│                                                            │
│  Sentence 1 names a user AND a pain.                       │
│  Sentence 2 names the verb the demo will perform.          │
│                                                            │
│  If sentence 1 does not name a user, the lede is buried.   │
│  If sentence 2 does not name a verb, the hook is decoration│
└────────────────────────────────────────────────────────────┘
```

Three examples, in order of strength:

- **Weak:** "Hi, my name is Pat. I'm a sophomore at State U. Today I'm presenting Quickhelp."
  - *Diagnosis:* no user, no pain, no verb. Thirty seconds spent introducing the pitcher, not the build. Buried lede.
- **Medium:** "Freshmen at our university often need help with class scheduling. Our tool helps with that."
  - *Diagnosis:* user is named, pain is named, verb is vague ("helps with that"). Audience does not know what the demo will *show*.
- **Strong:** "A freshman picks up her phone at 11pm, has a math-homework question, and there is no one online to ask. Quickhelp gets her a peer reply in under three minutes — let me show you."
  - *Diagnosis:* user (freshman), pain (11pm math question, no one online), verb (gets her a peer reply). The audience knows what the next 2:30 will show.

The strong hook is 27 seconds spoken. It fits the strip. The weak hook is 22 seconds spoken and has burned all of them.

### 2.2 The hook's three-line scaffold

```
Line 1 (8-12 sec): the user, in a scene. "A freshman picks up her
                   phone at 11pm with a math-homework question..."
Line 2 (8-12 sec): the pain, made concrete. "...and there is no one
                   online to ask. The TA office hours ended at 6."
Line 3 (6-10 sec): the verb the demo will perform. "Quickhelp gets
                   her a peer reply in under three minutes — let
                   me show you."
```

Three lines, 22 to 34 seconds spoken. Stay inside the 30-second cap by trimming the third line; the third line is the most-cuttable. Lines 1 and 2 are the lede; line 3 is the *transition* into the problem beat.

### 2.3 The "no apology preface" rule

The hook does *not* open with:

- "Sorry the deploy is slow today."
- "Sorry for the rough design."
- "Sorry I'm reading from notes."
- "Sorry, give me a sec to load the page."

These are the apology preface (failure mode 3). They cost more than the imperfection they cover. The audience does not know the deploy is slow until you tell them; the rough design is invisible until you flag it; reading from notes is fine if the words are good.

> **C4 voice:** the hook opens with the user, never with the pitcher. The apology preface is a pitcher-centered opener. Cut it. Open with the user; the polish or lack of polish is the audience's call, not yours.

### 2.4 The hook's tone calibration

The C4 voice rules from BRAND.md apply to the hook with the most force:

- **No "rockstar," "ninja," "10x," "crush it."** Even at the hackathon. The hook is the moment those words are most tempting; resist them most.
- **No "we built X." "We solved Y."** Past-tense bragging compresses the audience's evaluation; let the build speak. "Quickhelp gets her..." is present-tense and lets the demo earn its claim.
- **Credit teammates by name (with permission) at the *end* of the hook, not the start.** "...let me show you. Team: Pat, Sam, Jordan, and me on design." Five seconds, post-verb. Names do not pre-empt the lede.

---

## 3. The problem beat — 0:30 to 1:15

The problem beat narrows the pain. The hook named the user and the pain in scenes; the problem beat makes the pain *concrete, narrow, specific*. Forty-five seconds. Two paragraphs, sometimes three.

### 3.1 What the problem beat actually does

Three short sentences, one per outcome:

- **The problem beat surfaces the cost of the pain.** Not the abstract "students struggle with X" — the concrete "the average freshman has 4 unanswered late-night questions per week, and 60% of them give up before getting an answer." The number is the cost.
- **The problem beat narrows the user.** The hook named "a freshman"; the problem beat names "the freshman who lives in a single dorm, takes intro CS, and does not have an upperclassman roommate." Specificity is the discipline; the audience aligns to the specific user, then transfers the empathy to broader users themselves.
- **The problem beat *previews* the demo.** The last sentence of the problem beat is the line that hands off to the solution beat: "this is the moment Quickhelp is built for." That handoff is the cue for the live URL to appear on screen.

### 3.2 The problem beat's structure

```
┌────────────────────────────────────────────────────────────┐
│  THE PROBLEM BEAT — 0:30 to 1:15 (45 seconds)              │
│                                                            │
│  Paragraph 1 (~20 sec): the pain, narrowed.                │
│    Who specifically. When specifically. Why it matters     │
│    specifically.                                           │
│                                                            │
│  Paragraph 2 (~20 sec): the cost.                          │
│    A number, an outcome, a missed opportunity. The most-   │
│    quotable line of the beat lives here.                   │
│                                                            │
│  Handoff sentence (~5 sec): "this is the moment X is built │
│    for." The live URL appears on screen at this sentence.  │
└────────────────────────────────────────────────────────────┘
```

The handoff sentence is the boundary between the problem beat and the solution beat. The audience's attention is at its highest right before the first click; spend the 5 seconds on the handoff, not on apology or transition fluff.

### 3.3 The "nod test"

A working problem beat passes the nod test: a stranger watching the recording at 1.5x nods at the cost. If they do not nod, the cost is not concrete enough.

> **C4 voice:** the audience does not need the pain to be theirs. They need the pain to be *real*. Real means a named user, a named time, a named cost. Three nameds; one nod.

Three things that *kill* the nod:

- **Generic pain.** "Students struggle." Test: which student? When? What does the struggle cost? If you cannot answer in one sentence each, the pain is generic.
- **Hypothetical cost.** "This could save them hours." Test: name one hour. Name the activity. Name the alternative they currently use. Hypotheticals are aspirational; named alternatives are concrete.
- **Solution-flavored problem.** "Students do not have a peer-help platform." Test: this is a missing-feature statement, not a pain. Re-state the pain in terms of *what the user experiences*, not what the market lacks.

---

## 4. The solution beat — 1:15 to 2:45

The solution beat is 90 seconds. Three clicks. Three MUST verbs. The live URL on screen the entire time. The demo *is* the build. Not the slide deck; not the architecture diagram; not the GitHub readme. The build, performing the MUST verbs, on the deploy URL the audience could open on their phone right now.

### 4.1 The 3-click structure

```
┌────────────────────────────────────────────────────────────┐
│  THE SOLUTION BEAT — 1:15 to 2:45 (90 seconds)             │
│                                                            │
│  Click 1 (1:15 — 1:45)  30 sec  MUST verb 1.               │
│    Narrate: "She opens the URL, signs up in 30 seconds,    │
│    posts her math question — see, here, [click]."          │
│                                                            │
│  Click 2 (1:45 — 2:15)  30 sec  MUST verb 2.               │
│    Narrate: "A peer on the platform sees her question      │
│    on the feed, taps reply, types an answer — [click]."    │
│                                                            │
│  Click 3 (2:15 — 2:45)  30 sec  MUST verb 3 + demo clip.   │
│    Narrate: "She gets the reply in real time, on her       │
│    phone, three minutes after posting — [click, pause for  │
│    the visible result]."                                   │
└────────────────────────────────────────────────────────────┘
```

Three clicks. Thirty seconds each. The 30-second click includes the narration *and* the visible click *and* the pause for the result to appear on screen. Practice the 30-second click; the first take usually runs to 50 seconds on the first click and rushes the third.

### 4.2 The demo-clip line

The third click — the last 15 seconds of the solution beat — is the *demo clip*. This is the single most-quotable 15 seconds of the recording. It is the line judges write down. It is the moment the camera should be on the result, not on the pitcher.

Three demo-clip examples:

- **Quickhelp:** "She gets the reply in 47 seconds. Forty-seven seconds. The TA office hours don't reopen until tomorrow at 9, but her peer just answered."
- **A weather widget:** "It shows the rain icon turning to a sun icon as the storm passes. Live, on the deploy URL, no refresh needed."
- **A meme generator:** "She picks the image, types the caption, hits export, and — there. Three seconds. Ready to share."

The demo clip is the line that survives the demo. Plan it. Write it. Read it aloud before recording. Most pitches that "land" land here.

### 4.3 The "live URL is the backdrop" rule

> **C4 voice:** the solution beat is filmed against the live URL, not against slides. Slides are for follow-up; the demo is the build. If the live URL is not visible during the 90 seconds of the solution beat, the demo failed the bench test from Week 5.

Three things this rule excludes:

- **A slide deck with screenshots of the build.** Screenshots are not clicks. A demo that runs on screenshots is a presentation about a build, not a demo of a build.
- **A pre-recorded screen capture of localhost.** localhost is not the bench. A pre-recorded localhost demo is a localhost demo with extra editing; same failure mode as Week 5.
- **A screenshare of the IDE.** Code is not a demo. Judges have seen the README; the demo's job is to show the build *running*, on the URL they will open.

The exception: a 5-second cut to a code snippet during the solution beat, to flag a specific technical choice ("here's where we call the LLM API"). Five seconds total, max. Not 30. Not "let me walk you through the architecture."

### 4.4 Pacing the three clicks

The first click is usually too slow; the third is usually too fast. Three calibration moves:

- **Set a phone timer in-shot.** Many event judges do this; recording with the timer visible builds the muscle to feel the 30-second cap.
- **Practice the third click first.** The demo-clip line is the most important; rehearse it five times before the first take. The first click can be improvised on take 2.
- **Cut narration on the third click.** The third click is the result; the visible result speaks for itself. The narration in the third click is one short sentence, then silence for the result to land.

---

## 5. The ask — 2:45 to 3:00

The ask is 15 seconds. One number, one channel, one specific next step. Not "thanks for watching." The ask is the difference between a pitch the audience nods at and a pitch the audience does something about.

### 5.1 The ask's three-part structure

```
┌────────────────────────────────────────────────────────────┐
│  THE ASK — 2:45 to 3:00 (15 seconds)                       │
│                                                            │
│  Number  : a specific quantity. "100 freshmen this week,"  │
│            "$200 in API credits," "10 minutes of feedback."│
│  Channel : where the audience finds you. A URL, a handle,  │
│            a QR code on the screen, a sponsor booth #.     │
│  Next step: one specific action. "Sign up at this URL,"    │
│            "DM us on Devpost," "Stop by booth 12 today."   │
└────────────────────────────────────────────────────────────┘
```

Three asks, in order of strength:

- **Weak:** "Thanks for watching. We hope you liked it."
  - *Diagnosis:* no number, no channel, no next step. The audience has no action.
- **Medium:** "Check us out on GitHub."
  - *Diagnosis:* channel is named, number and next step are not. The audience does not know what to do once they arrive.
- **Strong:** "We're piloting Quickhelp with 100 freshmen at State U this week — sign up at quickhelp.app/pilot or stop by sponsor booth 12 today. Feedback channel is on the landing page."
  - *Diagnosis:* number (100 freshmen), channel (quickhelp.app/pilot + booth 12), next step (sign up or stop by). Audience has options.

### 5.2 The "not thanks for watching" rule

> **C4 voice:** "thanks for watching" is the demo equivalent of a verbal-only MoSCoW. It is a closer that pretends to be an ask. Replace it with one number, one channel, one specific next step. Even a small ask is more valuable than a polite closer.

The fix is mechanical: the last sentence of the script is the ask. Write it before the hook. Read it aloud. If it does not contain a number and a channel, re-write it. The last-sentence audit is the closer's equivalent of the first-sentence audit on the hook.

### 5.3 Calibrating the ask to the event

The ask differs by event type:

- **Hackathon, judging round.** Ask = a feedback channel and a quantity of expected users. "We're looking for 50 feedback comments by Monday; channel is on the URL."
- **Hackathon, sponsor booth.** Ask = a specific sponsor API or credit. "We're hoping for $200 in [Sponsor] credits to keep the deploy live for the pilot."
- **Internal team demo.** Ask = a follow-up. "Pat and Sam are running a working session at 4pm tomorrow; sign up in #quickhelp on Slack."
- **Recorded portfolio demo.** Ask = a contact channel. "GitHub is in the link below; the team is open to internships starting June."

The ask is the only beat that changes between events. The hook, problem, and solution stay the same; the ask is event-specific. Calibrate it.

---

## 6. The five pitch failure modes

Five predictable failure modes for the three-minute demo. Recognize them in your own first take, not in the retro after the event.

### 6.1 The buried lede

> **Symptom:** the first 30 seconds do not name a user and a pain.

The hook spends time on the pitcher's introduction, the team name, the sponsor thanks, the "today I'm presenting." By 0:30 the audience does not know who is hurting. The hook is decoration; the demo never recovers.

The fix: the first-sentence audit (§2.1). Read the first sentence aloud. Does it name a user and a pain? If not, re-write. The re-write is usually a deletion of the pitcher's name and a promotion of the scene to sentence 1.

### 6.2 The feature tour

> **Symptom:** the solution beat clicks through more than three features.

The build has six features; the pitcher wants to show all of them. The solution beat becomes a clickfest: signup, profile, post, reply, search, leaderboard, settings, dark-mode toggle. Forty seconds in, the audience has lost the verb. The demo is a tour, not a demo.

The fix: cut to the three MUST verbs from your Week-5 scoping worksheet. The MUSTs are the demo verbs; the SHOULDs and COULDs do not appear in the solution beat. They can appear in the demo *clip* (one 5-second peek) or in the ask ("there's also a leaderboard — link in the README").

### 6.3 The apology preface

> **Symptom:** the first 10 seconds are an apology.

"Sorry the deploy is slow." "Sorry the design is rough." "Sorry I'm reading from notes." Each apology costs more than the imperfection it covers, because each apology pre-empts the audience's own judgment. The audience does not know the deploy is slow until you tell them; the rough design is invisible until you flag it.

The fix: cut the apology. Open with the user. The audience will note the imperfections themselves; your job is to outweigh them with the hook.

### 6.4 The silent demo

> **Symptom:** the live URL is never visible during the solution beat.

The pitcher narrates the solution beat while the camera is on slides, on the pitcher's face, or on a static screenshot. The audience never sees the live URL move. The demo is theatre; the build might or might not work.

The fix: re-record on the URL. The solution beat's 90 seconds are filmed against the deploy URL. The camera follows the click. If the build is broken at recording time, fix the build, then re-record. Theatre demos lose to working demos every time.

### 6.5 The missing ask

> **Symptom:** the last 15 seconds are "thanks for watching."

The pitcher closes with a generic farewell. The audience has no number, no channel, no next step. The pitch ends; the audience claps; nobody acts.

The fix: the last-sentence audit (§5.2). Read the last sentence aloud. Does it contain a number and a channel? If not, re-write. The re-write usually takes 2 minutes and lifts the pitch's outcome more than any other 2-minute fix.

---

## 7. The script — what to write, what to improvise

The full three-minute script fits on one printed page. About 450 to 500 words. Three sections, written in this order:

### 7.1 Write the ask first

The ask is 15 seconds. Two sentences. It is the easiest beat to write because it is the most constrained — and writing it first means the rest of the script aims at it.

Three minutes of writing. The ask sentence is the destination; the hook, problem, and solution work backwards from it.

### 7.2 Write the hook second

The hook is 30 seconds. Three lines (§2.2). Five to ten minutes of drafting. Read each line aloud as you write it.

The hook is the most-rewritten beat in the script. Most learners draft three alternatives; one is the keeper. The first-sentence audit (§2.1) grades each draft in 30 seconds.

### 7.3 Write the problem beat third

The problem beat is 45 seconds. Two paragraphs and a handoff sentence (§3.2). Ten minutes of drafting. The handoff sentence at the end is the cue to the solution beat; write it tight.

### 7.4 Outline the solution beat, do not script it

The solution beat is 90 seconds. Three clicks. The narration on each click is one or two sentences — short enough to improvise from a bullet list, not from a paragraph.

```
Click 1: signup. "She opens the URL, signs up in 30 sec, posts her question."
Click 2: reply. "A peer sees the question on the feed, taps reply, types."
Click 3: result. "She gets the reply in real time, on her phone."
```

The narration is the bullet; the click is the verb. Writing the solution beat as a script tends to make the recording stiff; outline it and let the take breathe.

### 7.5 The full script length

```
┌────────────────────────────────────────────────────────────┐
│  THE FULL DEMO SCRIPT — STRUCTURE                          │
│                                                            │
│  Hook       (3 lines, ~70 words)        30 sec spoken      │
│  Problem    (2 paragraphs + handoff, ~105 words) 45 sec    │
│  Solution   (3 bullet clicks, ~200 spoken words) 90 sec    │
│  Ask        (2 sentences, ~40 words)    15 sec             │
│                                                            │
│  Total: ~415 words. One page printed.                      │
└────────────────────────────────────────────────────────────┘
```

The full script is one page. The recording is three minutes. If your script is two pages, you will over-run; cut. If your script is half a page, you will under-run; expand the problem beat.

---

## 8. How the script threads the worksheet and the contract

Week 5's worksheet has five sections; Week 4's contract has eight. Week 6's script has four beats. The three artifacts share three threads:

### 8.1 Thread 1: the MUST list is the solution beat

The worksheet's MUST column (3 items) is the solution beat's three clicks. The arithmetic is intentional:

- Worksheet's MUST item 1 = solution beat's click 1 (30 sec).
- Worksheet's MUST item 2 = solution beat's click 2 (30 sec).
- Worksheet's MUST item 3 = solution beat's click 3 (30 sec + demo clip).

If the worksheet's MUST list is not 3 items, the solution beat does not fit the 90-second band. Re-cut MUST to 3.

### 8.2 Thread 2: the prompt sentence is the hook's lede

The worksheet's prompt sentence ("X can Y to relieve Z") is the structural lede of the hook. The hook's first sentence is the prompt sentence, rendered as a scene:

- Worksheet prompt: "A freshman can post a late-night question to get a peer reply within 5 minutes."
- Hook lede: "A freshman picks up her phone at 11pm with a math-homework question..."

Same user (freshman), same verb (post + reply), same time (late-night). The prompt sentence is the kernel; the hook is the scene rendering. If the hook and the prompt sentence disagree on the user, something is wrong.

### 8.3 Thread 3: the demo-ability checklist runs the recording

The worksheet's demo-ability checklist (five questions) runs against the recording the way it runs against the build. If the recording is on localhost (Q1 failed), or the recording does not show the MUST verb (Q3 failed), or the recording shows empty seeded-data screens (Q5 failed), the recording is not yet demo-able.

The fix is identical: re-record on the live URL, on the deploy, with seeded data visible. The demo-ability test is the bench for both the build and the recording.

---

## 9. The script is half the artifact

The other half is the recording. Lecture 2 covers the mechanics: how to record on the live URL, how to watch the first take without flinching, how to write the three notes that drive the second take, and how to commit the final recording with a public link in the repo README.

The script is the half you can write at your desk. The recording is the half you can only learn by watching yourself. Most learners write a beautiful script and skip the recording rehearsal; their first hackathon demo runs to 4:30 because they have not yet *felt* the three-minute clock. The recording rehearsal is non-negotiable.

---

## 10. Recap

- The demo-timing strip from BRAND.md is the canonical structure: 30s hook / 45s problem / 90s solution / 15s ask. Three minutes total. The bands are tight; the discipline is the band.
- The hook names a user and a pain in sentence 1, and the demo verb in sentence 2. The first-sentence audit grades any hook in 30 seconds.
- The problem beat narrows the pain to a specific user, time, and cost. The nod test grades any problem beat: a stranger watching at 1.5x nods at the cost, or they do not.
- The solution beat is three clicks on the live URL, one MUST verb per click, 30 seconds each. The third click ends with the demo clip — the single most-quotable 15 seconds of the recording.
- The ask is 15 seconds: one number, one channel, one specific next step. The last-sentence audit grades any ask. "Thanks for watching" is not an ask.
- Five pitch failure modes: buried lede, feature tour, apology preface, silent demo, missing ask. One test per mode; one fix per mode.
- The script is one page (~415 words). The order to write it: ask first, hook second, problem third, solution as a bullet outline. The solution beat is improvised from bullets, not read from a paragraph.
- The script threads the Week-5 worksheet: MUST list is the solution beat; prompt sentence is the hook's lede; demo-ability checklist runs the recording.

Continue to [Lecture 2 — Recording, Watching, and Cringing](./02-recording-watching-and-cringing.md), where the team learns to record on the live URL, watch the first take honestly, write the three notes that drive the second take, and commit the final recording with a public link.

# Lecture 2 — The 3-Minute Arc and the Live-Coding Trap

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can deliver a 3-minute judge-room pitch using the 30-90-45-15 arc — problem, demo first, tech briefly, ask — without notes, without live-coding, and without exceeding 3:15 even with stumbles. You can name the four canonical pitch-failure modes (notes-fixation, no-demo-first, the live-coding cascade, the long-ask) and the named recovery from each. You can lock the pitch script under fatigue.

If you only remember one sentence from this lecture, remember this:

> **Demo first. Then tech. Never live-code. The 3-minute pitch that wins is the one where the judge sees the build working before they hear the team explain it.**

Lecture 1 named the rubric and the two judging mindsets. Lecture 2 names the *vehicle* — the 3-minute structure that carries the rubric-relevant evidence into the judge's scoring. The structure is the *what*; this lecture covers the *how*.

This lecture has three parts. Part 1 (sections 2-3) covers the 30-90-45-15 arc and the "demo first" rule. Part 2 (section 4) covers the live-coding trap and the named failure modes. Part 3 (sections 5-6) covers script-locking, the four canonical failure modes, and the named recovery from each. Section 7 is the recap.

---

## 1. Why the 3-minute slot is its own skill

Most C4 learners reach Week 9 with a 3-minute *recorded* demo from Week 6 and a 3-minute *team-recorded* demo from Week 8. The recordings are *almost* the same as the live pitch — same script, same length, same beats. They are not the same skill. Three reasons:

- **The recording is forgiving.** Stumble at 1:20, hit pause, rewind, re-record from 1:15. The judge-room is the opposite — stumble at 1:20, the timer keeps running, the next 90 seconds are now compressed.
- **The recording has one audience: the camera.** The camera does not give cues. The judge gives cues constantly — clipboard pickup, eye-contact loss, lean-back, side-glance (Lecture 3 §2). The team that pitches *to a camera* and the team that pitches *to a judge* are reading different signals.
- **The recording is solo or team-paced.** The live pitch is *judge-paced* — the judge may interrupt at 0:45 with a clarification question, may speed-up at 2:30 with a "wrap up" signal, may sit back at 1:50 if the demo isn't landing. The team must hold the script while also reading the room.

The three differences compound. A team that has rehearsed only the recording rehearses 30% of the live skill. The other 70% is the live delivery muscle.

> **C4 voice:** the live pitch is the load test. The recording is the bench. The team that thinks "we already did this in Week 6 and Week 8" arrives at the load test unprepared. The mock-pitch rehearsals this week are the rehearsal of the *live* mode, not the recording mode.

### 1.1 What the 3-minute slot actually contains

Three minutes is 180 seconds. The judge's job during those 180 seconds:

```
0:00 — 0:30  Form initial impression. Note the problem framing.
              First rubric data point: "is this a real problem?"
0:30 — 2:00  Watch the demo. Read for the build's quality.
              Rubric data points: design, polish, originality.
2:00 — 2:45  Listen to the tech. Read for engineering credibility.
              Rubric data points: technical complexity.
2:45 — 3:00  Note the ask. Read for follow-through intent.
              Rubric data point: presentation (closing discipline).
```

The judge is scoring four rubric dimensions across the four beats. The fifth dimension (presentation) is scored across all four beats by the *quality of delivery*. The team's job is to give the judge a clean read on each dimension within the time-window allotted to that dimension.

The team that *inverts* this — tech first, demo second — gives the judge a low data point on technical complexity (no demo to anchor it) and a low data point on design (no demo to anchor it) and a low data point on polish (no demo to anchor it). Demo-first is not a stylistic preference; it is the *mechanical* way to give the judge clean rubric data points.

---

## 2. The 30-90-45-15 arc

The C4 default arc:

```
┌────────────────────────────────────────────────────────────────────┐
│  THE 3-MINUTE PITCH ARC — 30-90-45-15                              │
│                                                                    │
│  [ 0:00 — 0:30 ]   PROBLEM       (30 seconds)                       │
│  [ 0:30 — 2:00 ]   DEMO          (90 seconds)                       │
│  [ 2:00 — 2:45 ]   TECH          (45 seconds)                       │
│  [ 2:45 — 3:00 ]   ASK           (15 seconds)                       │
└────────────────────────────────────────────────────────────────────┘
```

Four beats. The durations are *targets*, not laws — the team can shift ±5 seconds per beat without breaking the arc. Shifting more than 5 seconds re-balances the rubric data points; do not shift more than 5 seconds without thinking through which dimension you are downgrading.

### 2.1 Beat 1 — Problem (30 seconds)

The opening 30 seconds. The judge forms the initial impression. The team's job: name the user, the pain, and the verb in the first 20 seconds; spend the remaining 10 seconds on the prompt-fit (why does this prompt produce this user/pain/verb).

Template (the C4 default; the team will personalise):

```
"Hi, we are [team name]. We built [build name] for [specific user] who
need to [verb] [specific pain] in [specific context]. The prompt asked
us to [prompt summary]; we read that as a problem about [user's
experience]. We are going to show you the working build."
```

Eight sentences. Twenty seconds of speech at a normal pace. Ten seconds remaining for the transition into the demo.

Anti-patterns:
- **Starting with the team's bio.** "We are four CS students from FIU." The judge does not care; the judge cares about the user.
- **Starting with the tech stack.** "We built this with React and Supabase." The judge does not score the stack at 0:00; the judge scores the user-pain framing.
- **Starting with a story longer than 30 seconds.** The story is the problem framing, not a separate beat. Compress it.

> **C4 voice on the problem beat:** the first 20 seconds of the pitch is the *single highest-leverage 20 seconds* of the team's day. The team's user-pain-verb framing from Week 5's scoping worksheet *is* this beat. Do not improvise it; use the framing you already wrote.

### 2.2 Beat 2 — Demo (90 seconds)

The 90 seconds where the judge sees the build working. The team's job: walk the judge through the *most demonstrable* user flow, in 90 seconds, against the live deploy URL.

Structure:

```
0:30 — 0:45   Open the live URL. Pause for 2 seconds while the page loads
              and the judge sees the landing screen.

0:45 — 1:15   Walk through the primary user flow. Three actions, max.
              Each action: 8-10 seconds. Narrate what the user is seeing
              and what just happened.

1:15 — 1:45   Show one secondary feature that demonstrates the originality
              dimension. 30 seconds.

1:45 — 2:00   Return to the landing screen or to a "summary" view. The
              judge needs a clean visual to anchor the next beat.
```

Anti-patterns:
- **Localhost demos.** Same rule as Week 8: the dress rehearsal records against the live URL; the judge-room pitch also runs against the live URL. A localhost demo signals "we did not deploy" which signals incomplete polish.
- **Demoing every feature.** The 90 seconds is for the *most-impressive* flow, not all flows. The judge does not need to see every screen.
- **Talking over the demo.** The narration is in service of the demo; the demo is not in service of the narration. If the team is talking and the judge is not watching the screen, the team is talking too much.

> **C4 voice on the demo beat:** demo first is structural. The judge cannot score design, polish, or originality without seeing the build. Withholding the demo for 60 seconds while you explain "first let me give you context" downgrades three rubric dimensions for free. Do not do this.

### 2.3 Beat 3 — Tech (45 seconds)

The 45 seconds for the engineering credibility. The team's job: name one specific technical decision and the alternative rejected.

Template:

```
"Under the hood, the build is [framework] on [platform]. The most
interesting engineering decision was [decision]. We considered
[alternative] but chose [decision] because [reasoning]. The hardest
part was [hardest problem]; we solved it by [solution]."
```

Four sentences. ~40 seconds at a normal pace. Five seconds for the transition into the ask.

Anti-patterns:
- **Naming every framework and library.** "We used React and TypeScript and Supabase and Vercel and Tailwind and Radix UI and..." The list is not the same as the *decision*. Name one decision.
- **Saying "we used [framework] because it is the best framework."** This is not engineering judgment; it is brand recitation. Engineering judgment names the *trade-off*.
- **Skipping this beat entirely.** Teams sometimes spend the demo beat on tech and the tech beat on more demo. The judge-as-engineer's rubric data point lives in this beat; skipping it costs technical-complexity points.

> **C4 voice on the tech beat:** name one decision, not the whole stack. The decision-with-trade-off reads as engineering judgment; the stack-list reads as a resume.

### 2.4 Beat 4 — Ask (15 seconds)

The closing 15 seconds. The team's job: state the one ask and stop talking.

Template:

```
"We are [team name]. The build is at [URL]. We would love to [one
specific next step we will take regardless of the judging outcome].
Thank you."
```

Three sentences. ~12 seconds at a normal pace. Three seconds of silence at the end (intentional; the silence cues the judges that the pitch is over).

The ask is not "please give us a high score." The ask is the team's *commitment* — what the team will do next regardless of the outcome. The investor-judge scores follow-through intent on this beat; the engineer-judge scores presentation discipline.

Anti-patterns:
- **No ask.** The pitch ends with "...and that's our project." This costs presentation points and follow-through points.
- **Multiple asks.** "We would love to talk to you about partnerships, and also we are looking for a CTO, and also we want feedback." Pick one.
- **An ask that depends on the judging outcome.** "If we win, we will spend the prize money on..." The judge does not yet know if you are winning; the ask should not be contingent.

### 2.5 The total

Thirty plus ninety plus forty-five plus fifteen equals one hundred eighty. Three minutes flat.

The team that hits 2:55 and stops scores higher on presentation than the team that hits 3:05. The team that hits 3:30 has overshot meaningfully and loses points.

The team that hits 2:30 has under-used the slot; usually this means the team rushed and is missing rubric data points (no tech beat, or a 5-second ask). Practice the slot until the pitch fills the 3:00.

---

## 3. Why "demo first"

The 30-90-45-15 arc puts the demo at beat 2 (0:30-2:00) before the tech at beat 3 (2:00-2:45). The alternative arcs (tech first, problem-tech-demo-ask) are common in non-hackathon contexts (academic talks, investor pitches with slides). At a hackathon, demo first is the C4 default. Three reasons:

### 3.1 The judge needs the demo to anchor the other dimensions

Without seeing the demo, the judge cannot score:
- *Design and UX* (no UI to read)
- *Polish* (no finished product to assess)
- *Originality* (no specific build to compare against alternatives)

Three of the five dimensions are unscoreable until the judge has seen the build. Putting the demo at beat 2 gives the judge those three data points by 2:00; putting the demo at beat 3 leaves only 75 seconds for the judge to score three dimensions.

### 3.2 The judge's attention is highest in minutes 1-2

The audience attention curve (Lecture 3 §2.1) shows attention peaks in the opening 30 seconds, dips in the middle, and recovers slightly near the close. The demo lands during the *high-attention* window when it is at beat 2; the demo lands during the *attention recovery* window when it is at beat 4.

A judge who saw the demo at high attention forms a clearer rubric data point than a judge who saw the demo while their attention was already returning to the day's accumulated fatigue.

### 3.3 Demo-first is the *trust* move

The team that shows the working build before explaining why it should work signals confidence. The team that explains for 90 seconds and then shows the build signals "we are nervous; let us prepare you for the demo." The first signal scores higher on presentation across both mindsets.

> **C4 voice on demo-first:** the demo is the team's strongest evidence. Lead with strength. The team that puts the demo at beat 2 is making the judge's job easy; the team that holds the demo to beat 4 is making the judge work for it.

### 3.4 When to *not* demo first

Three narrow exceptions:

- **Hardware builds where the device needs to physically materialise.** A hardware demo may need a 15-second setup where the team turns the device on or hands the prototype to the judge. The setup happens during the problem beat; the demo still starts at 0:30 but with the device in hand.
- **Ethically-sensitive builds where the problem context is non-obvious.** A build for trauma survivors, for example, requires problem framing before the demo to set the appropriate stakes. The problem beat extends to 0:45 in this narrow case; demo at 0:45-2:00.
- **Builds whose user experience is invisible (background processes, security tools).** The team may need to *narrate the invisible work* during what would have been the demo beat. In this case, the "demo" is a screen-share of logs or a system diagram; the structure stays the same but the visual content differs.

The exceptions are narrow. Default to demo-first; deviate only with deliberation.

---

## 4. The live-coding-in-the-demo trap

The single most reliable failure mode in a 3-minute hackathon pitch is the team attempting to *live-code* a feature during the demo beat. This section names the failure modes and the C4 voice's directive.

### 4.1 What "live coding" means here

For the purposes of this lecture, "live coding" means any of:

- Typing code into an editor during the pitch (any amount).
- Running a shell command whose output the team cannot guarantee in advance.
- Executing a build step (`npm run build`, `python setup.py`, etc.) during the pitch.
- Invoking an API endpoint with data entered by hand during the pitch.

What *is* allowed (and is not live coding):
- Clicking buttons in the deployed UI.
- Entering form data into the deployed UI (data the team has tested in advance).
- Showing a pre-built code snippet from a slide or a static file (read-only).
- Switching browser tabs to the team's GitHub repo.

The distinction: pre-tested deterministic action is allowed; on-the-fly action whose outcome the team cannot guarantee is the trap.

### 4.2 The four named failure modes

```
1. The typo cascade.
   The team types a command, fat-fingers a character, gets an error,
   tries to fix it, breaks something else. Total wall-clock cost:
   30-90 seconds. Demo beat: half-consumed by the typo recovery.

2. The API rate-limit moment.
   The team invokes a third-party API live. The API returns a 429
   (rate limit) or a slow response. The team waits, the judge waits,
   the timer keeps running. Total cost: 20-60 seconds.

3. The localhost-not-deployed surprise.
   The team's local environment behaves differently from the deploy.
   A path that worked at home does not work on the demo machine
   (because the demo machine does not have the local env vars or
   the local Python venv or the local node_modules). Total cost:
   anywhere from 30 seconds to the entire demo beat.

4. The network-failed-at-the-wrong-moment.
   The team relies on the conference WiFi (or the judge's hotspot)
   for an API call that does not work over the conference's
   throttled connection. Total cost: 30+ seconds.
```

All four failure modes are *recoverable in principle* — the team can apologise, recover, and continue. In *practice*, the team's recovery consumes the rubric-relevant time the team would have used to score on design, polish, and originality. The mode in which the failure happens (in front of the judge, not in a recording) compounds the cost.

### 4.3 The C4 voice's directive

```
┌────────────────────────────────────────────────────────────────────┐
│  THE C4 LIVE-CODING DIRECTIVE                                       │
│                                                                    │
│   Do not live-code in a 3-minute hackathon pitch.                  │
│                                                                    │
│   The 90 seconds of demo time is for pre-tested deterministic      │
│   action against the live deploy URL. Anything that can fail in   │
│   a way the team cannot rehearse against is out of scope for the  │
│   90 seconds. Use pre-built data, pre-built code snippets, and    │
│   pre-tested user flows.                                           │
│                                                                    │
│   If a feature requires live execution to be impressive, the      │
│   feature is not ready for a 3-minute pitch. Cut it from the      │
│   demo and mention it in the tech beat or the Q&A.                │
└────────────────────────────────────────────────────────────────────┘
```

The directive is empirical. The C4 voice arrived at it after pattern-matching across public hackathon post-mortems (search Reddit r/hackathons for "demo went wrong"; the failure mode is consistent). The directive is not "live coding is impressive but risky"; it is "live coding is *not* impressive and is reliably risky."

### 4.4 The exception: "live" features that are pre-recorded

Some builds have a "live" feel — real-time data, streaming events, push notifications — that the team wants to convey. The C4 voice's framing:

- **The team can *show* the live feel** by demoing the deployed feature working in real-time against the live URL (the data is real but the *user input* is pre-tested by the team).
- **The team can *narrate* the live feel** by describing what is happening under the hood while the deployed feature runs.
- **The team should *not* enter new live input during the pitch.** New input has a non-zero probability of failure; the failure consumes the slot.

A team that wants to demo a "live push notification" should set up a second device or second window that triggers the notification at a pre-tested moment, on a pre-tested input. The demo is *deterministic* but *looks live*. The judge cannot tell the difference; the failure-mode probability drops to near-zero.

---

## 5. Script-locking under fatigue

By the time the team reaches the judging window, they have been awake 18-30 hours (real event) or 6-12 hours (post-dry-run). Fatigue is the operating condition. The script must be lockable *under* fatigue, not in spite of it.

### 5.1 The lock-script protocol

```
┌────────────────────────────────────────────────────────────────────┐
│  THE SCRIPT-LOCK PROTOCOL — 15 MINUTES                              │
│                                                                    │
│  [ 0:00 — 0:05 ]   Read the script aloud once, looking at notes    │
│  [ 0:05 — 0:08 ]   Read the script aloud once, looking at the      │
│                    screen (the live deploy URL)                     │
│  [ 0:08 — 0:11 ]   Read the script aloud once, looking at a        │
│                    teammate (eye contact)                            │
│  [ 0:11 — 0:14 ]   Set a 3-minute timer. Read the script aloud     │
│                    once, against the timer, no notes                │
│  [ 0:14 — 0:15 ]   Lock decision: keep, tweak, or rewrite           │
└────────────────────────────────────────────────────────────────────┘
```

Fifteen minutes. Four reads. One decision.

The fourth read is the team's *commitment*: if the no-notes read landed at 3:00 ± 10 seconds, lock the script. If it landed at 3:00 ± 30 seconds, tweak one beat and re-read once. If it landed outside ± 30 seconds, the script is too long or too short — rewrite the most-stretched or most-rushed beat and re-run the protocol.

### 5.2 What "lock" means

Locked means:

- **No further edits to the script before the pitch slot.** Edit-mode at the last minute is the most reliable way to forget a beat.
- **The team has read the script aloud at least four times.** The muscle memory is in the voice, not on the page.
- **The team has practiced the script once against the live timer.** The timing intuition is calibrated.
- **The team has a hardcopy or a phone-screen of the script for emergency reference, but does not plan to read from it.**

The locked script is the team's *parachute*. The team plans to deliver from memory and rapport with the judge; the parachute is there in case the memory or the rapport flickers.

### 5.3 Why fatigue makes script-locking harder

Three measurable effects of 18+ hours of awake-time (referenced in the open-access sleep-deprivation literature, e.g., the NIH StatPearls page from Week 8's resources):

- **Working-memory capacity drops by ~20%.** The team's ability to hold the script's beats in active memory degrades. Solution: lock the script earlier, re-read more times.
- **Word-retrieval speed drops by ~15%.** The team will pause more, search for words more, default to filler ("um", "like") more. Solution: rehearse the *exact* phrasing, not just the gist; the muscle memory is the failsafe.
- **Tendency to over-explain rises.** Tired brains over-explain to compensate for self-doubt about clarity. Solution: trust the locked script; do not add improvised explanations during the pitch.

The script-lock protocol is fatigue-resistant by design. The four reads build the muscle memory; the timer practice builds the timing intuition; the lock decision prevents last-minute edits.

---

## 6. The four canonical failure modes and named recoveries

This section names the four failure modes the team can hit *during* the pitch and the recovery move for each. The recovery moves are not "the failure is fine"; they are "the failure is contained, and the team continues."

### 6.1 Failure mode 1 — Notes-fixation

```
Symptom: the team's eyes are on the script (printed or screen), not
on the judge. The pitch is read, not delivered.

Cost: presentation points drop by 1-2 of 5. The judge writes "read
from notes" on the rubric.

Recovery: at the next beat transition (the next time the script
hits a paragraph break), look up at the judge for the duration of
that beat. The team rehearses *recovery* in the mock pitch, not the
elimination of the symptom.
```

The team that has rehearsed the script with the four-read protocol (Lecture 2 §5.1) hits this failure less often. The team that has not rehearsed hits it constantly.

### 6.2 Failure mode 2 — No-demo-first

```
Symptom: the team's problem beat extends to 0:45 or 0:60. The demo
beat starts late. The judge has not seen the build by 1:00.

Cost: design, polish, and originality data points are compressed
into <60 seconds. Three rubric dimensions lose 1-2 points.

Recovery: the moment the team realises they are at 0:40 still
talking about the problem, transition immediately ("...and here is
the build"). Do not finish the sentence; cut the problem beat short.
The judge cares more about the demo than the rest of the problem
framing.
```

The team that has rehearsed against a timer (Lecture 2 §5.1, read 4) catches this early. The team that hasn't rehearsed against a timer runs over the problem beat without noticing.

### 6.3 Failure mode 3 — The live-coding cascade

```
Symptom: the team attempted live coding (despite Lecture 2 §4's
directive). The first command failed. The team is now trying to
recover.

Cost: 30-90 seconds of the demo beat are consumed. The judge writes
"demo did not work" on the rubric.

Recovery: stop attempting the recovery. Apologise once ("the live
command isn't running; here is the static screenshot of the result
we tested at hour 18"). Show the pre-tested screenshot. Continue
the demo from the next beat.

The recovery is the *interruption* of the cascade, not the
completion of the live command. Continuing to attempt the live
command for 60+ seconds while the judge watches is worse than the
apology-plus-screenshot.
```

This failure is *prevented* by the directive in §4.3 — do not live-code. The recovery is for the team that has already violated the directive; the prevention is to not violate it in the first place.

### 6.4 Failure mode 4 — The long-ask

```
Symptom: the team's closing beat extends to 25-30 seconds. The pitch
total hits 3:15 or 3:20. The judge has cued "wrap up" but the team
keeps talking.

Cost: presentation points drop. The judge's last impression is "this
team does not respect the time."

Recovery: once the team realises they have exceeded 3:00, end the
sentence at the next natural break and stop. Do not continue to the
end of the planned ask. The recovery is the *stop*, not the
completion.
```

The team that practices the 15-second ask against the timer hits this less often. The team that practices the pitch without the ask under timer hits this constantly.

### 6.5 The fifth failure mode — the unprepared Q&A

Not strictly a pitch-beat failure, but it consumes the team's post-pitch slot:

```
Symptom: the team finishes the pitch at 3:00, the judge asks a
question, and the team's first response is "umm" or "good question,
let me think about that."

Cost: presentation and follow-through points drop on the Q&A
moment. The judge writes "didn't anticipate the question."

Recovery: this is Lecture 3's terrain. The Q&A drill (Lecture 3 §3)
is the prevention. The recovery move within the Q&A is the bridge
sentence pattern (Lecture 3 §3.4).
```

The pitch is half the judging slot; the Q&A is the other half. Both need rehearsal.

---

## 7. Recap and exit criteria

This lecture covered three things: the 30-90-45-15 arc and why demo-first matters; the live-coding trap and the C4 voice's directive against live coding in a 3-minute pitch; the script-lock protocol and the four canonical pitch-failure modes.

### 7.1 Recap

- The 3-minute slot is its own skill, distinct from the recorded demo.
- The 30-90-45-15 arc gives the judge clean rubric data points across four dimensions in four beats.
- Demo first because the judge cannot score design/polish/originality without seeing the build.
- Live coding is reliably risky and reliably under-rewards; the C4 voice directs against it.
- Pre-tested deterministic action against the live deploy URL is the allowed alternative.
- The script-lock protocol uses four reads in 15 minutes to lock the script under fatigue.
- The four pitch failure modes (notes-fixation, no-demo-first, live-coding cascade, long-ask) each have a named recovery move.

### 7.2 What "I read this lecture" means

After reading this lecture, the team should be able to:

- Recite the 30-90-45-15 beat distribution from memory.
- Name the three rubric dimensions that require the demo to score (design, polish, originality).
- Recite the four named live-coding failure modes.
- Run the script-lock protocol on the team's actual Week 8 demo script.
- Name the four canonical failure modes and the recovery move for each.

The lecture's deliverable is the team's preparation for Exercise 1 (alongside Lecture 1's rubric work) and the mini-project (the mock pitch itself).

### 7.3 Exit criteria

- [ ] You can recite the 30-90-45-15 distribution.
- [ ] You can name the three rubric dimensions that demo-first protects.
- [ ] You can name the four live-coding failure modes.
- [ ] You can run the four-read script-lock protocol against a script.
- [ ] You can name the four pitch failure modes and the recovery move for each.

When all five are checked, continue to Lecture 3 (Q&A, reading the room, unfair judging, and the be-a-judge sidebar).

---

*Demo first. Then tech. Never live-code. Three minutes. Lock the script. Recover from the failure modes you can name; prevent the ones you cannot.*

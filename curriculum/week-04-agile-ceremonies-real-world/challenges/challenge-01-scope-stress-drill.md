# Challenge 1 — Scope Stress Drill

**Time estimate:** 30 minutes of paired drill + 15 minutes of written debrief. Total ~45 minutes.

> This is the Week 4 challenge in C4: a paired drill where one teammate plays the *scope-pusher* and the other runs the three-sentence "no" script under a clock. The point is to *feel* the muscle of refusal, not just to write it. Five minutes of out-loud drill produces more behavior change than 30 minutes of silent reading.

---

## Problem statement

You and one other C4 learner do a 30-minute drill in two roles: the **Defender** runs the "no" script; the **Pusher** plays an excited teammate proposing mid-event scope additions. Each role lasts 12 minutes, with a 6-minute debrief in between. You both finish having said "no" out loud six times and having heard "no" out loud six times.

You may run this drill over a voice call (Discord, Meet, FaceTime, phone) or in person. No screen-share is needed. No code is written. The whole drill is conversational.

---

## Why a drill, not a written exercise

Exercise 3 was the writing. This challenge is the reps. The difference matters:

> **C4 voice:** the "no" script reads easy in a markdown file. It is hard at hour 12 when a teammate is excited about a feature and looking at you. The drill rehearses the *looking-at-you* part.

The Pusher's job is to be plausibly excited about each scope-creep request — not a caricature, not a hostile teammate, but a real-sounding voice the Defender has to refuse. The Defender's job is to run the three-sentence script (acknowledge, refuse with a reason, offer a cheaper alternative) without freezing, without skipping the acknowledge, without forgetting the offer.

Each role gets twelve minutes — long enough to do six rounds of the script, short enough to keep the energy up. By minute six you will be tired of saying no. That is the point — hour 24 of a real event is *more* tiring than this.

---

## Acceptance criteria

- [ ] You and your partner each play both roles (Defender for 12 min, Pusher for 12 min, in some order).
- [ ] Each of you runs the three-sentence "no" script at least six times during your Defender block.
- [ ] Each of you commits a written debrief at `week-04-prep/challenge-01-debrief.md` (in your own repo).
- [ ] The debrief names one specific moment your script broke (a skipped sentence, a slipped phrasing, a freeze) and one specific moment it worked.
- [ ] Your partner's debrief is linked from yours, and yours is linked from theirs.

---

## How to run the 30 minutes

```
┌────────────────────────────────────────────────────────────┐
│  THE 30-MINUTE SCOPE STRESS DRILL                          │
│                                                            │
│  Pre-drill (5 min, async): both partners pick the same     │
│   fake team setup from Exercise 3 (A, B, or C). Both       │
│   agree on the WON'T list.                                 │
│                                                            │
│  Min  0 — 1   Setup the call. Agree who is Defender first. │
│  Min  1 —13   Defender 1 / Pusher 1 block.                 │
│                  - Pusher reads a triggering line (15 sec) │
│                  - Defender runs the script (45 sec)       │
│                  - Pusher gives 5 sec of feedback          │
│                  - Loop. Six rounds in 12 minutes.         │
│  Min 13 —19   Switch and debrief (6 min):                  │
│                  - 90 sec each: name one moment that broke │
│                  - 90 sec each: name one moment that worked│
│  Min 19 —31   Defender 2 / Pusher 2 block. Same format.   │
│                                                            │
│  Tools: voice or video call. No screen-share, no code.     │
└────────────────────────────────────────────────────────────┘
```

### The Pusher's six trigger lines

The Pusher picks six lines to read, two per scope-creep shape. Lecture 2 §3.1 gave you the three shapes. Here are example trigger lines per shape — use these or write your own:

```
HOUR 2 SHAPE — "while we're in there"
- "While I'm adding the signup form, let me add password reset — it's quick."
- "Since we're already touching the matching code, what about adding a 'skip' button?"

HOUR 12 SHAPE — "we have time for one more"
- "We shipped MUST early — what if we add a leaderboard? Judges will love it."
- "I have an extra hour — let me add a quick analytics dashboard for us."

HOUR 24 SHAPE — "we have to add X or the demo dies"
- "Wait — the demo needs auth, otherwise nobody will believe it's real."
- "We have to add a loading spinner or the page looks broken to a judge."
```

The Pusher reads each line *with the energy of a teammate who genuinely believes it*. Not as a script. Try to sell it.

### The Defender's response

For each trigger line, run the three-sentence script from Lecture 2 §3.2:

1. ACKNOWLEDGE — "That's a good catch / I had the same impulse."
2. REFUSE WITH A REASON — "We agreed in the contract that <X> is in WON'T because <reason>."
3. OFFER A CHEAPER ALTERNATIVE — "What if we <cheaper version> instead?"

Hard 45-second cap. The Pusher uses the timer. If you blow the cap, the round counts as a freeze — note it in the debrief.

### The Pusher's 5-second feedback

After each round, the Pusher gives one sentence of feedback. Examples:

- "You skipped the acknowledge — straight to refuse. Try again next round."
- "The alternative was vague — what specifically would we ship?"
- "Good — that one landed clean. Move on."
- "You said 'I don't think' — the script wants 'we agreed.' Re-phrase next time."

Five seconds. Hard cap. Move to the next round.

---

## The midpoint switch (minute 13–19)

The 6-minute switch is the *most valuable* part of the drill. The format:

```
Min 13:00 — 14:30  Defender 1 names one specific moment the script
                   broke (a skipped sentence, a slip, a freeze).
Min 14:30 — 16:00  Pusher 1 names one specific moment Defender 1's
                   script worked, with the exact phrasing they used.
Min 16:00 — 17:30  Defender 1 names one behavior change they will
                   try in the Pusher-2 block.
Min 17:30 — 19:00  Roles switch. Setup for block 2.
```

The "what worked" round is intentionally placed *between* the failure note and the next block. You will be tempted to skip it ("it's fine, let's just go"). Do not. Hearing a specific phrase that landed is what calibrates the next attempt.

---

## Pitfalls (forewarned)

The drill fails for predictable reasons. Plan around them.

### 1. The Pusher gets too gentle

The Pusher's job is to be plausibly pushy. If both trigger lines come out apologetic ("um, what if we maybe added…"), the Defender never gets stressed and the drill does nothing. Pushers: read each line with conviction.

### 2. The Defender treats it as a script reading

The Defender's job is to respond, not to recite. If you read sentence 1, 2, 3 mechanically off Lecture 2 §3.2, you are not building muscle — you are reading a script that, at hour 24, you will not have in front of you. Respond from memory; the words are imperfect, the *structure* is what we are practicing.

### 3. The 45-second cap is ignored

If you blow the cap, the round is a freeze. Note it. Do not "make up for it" by being faster on the next round. The cap is the discipline; respect it.

### 4. The drill turns into a discussion

If the drill turns into "but what if the leaderboard really is a good idea?" — pause. The drill is about *refusal mechanics*, not about whether any specific request is correct. Discuss the leaderboard at a different time. During the drill, the Defender refuses; that is the only correct response.

### 5. Skipping the debrief

The debrief is where the learning lives. A drill without a debrief is a 30-minute conversation that produced nothing. Commit the debrief file even if it is short. The act of writing one specific moment surfaces the muscle.

---

## The written debrief

After the drill, write `week-04-prep/challenge-01-debrief.md` with three sections:

```markdown
# Scope Stress Drill — Debrief

Partner: <handle, repo link>
Date: <YYYY-MM-DD>
Fake team setup: <A / B / C>

## One moment my script broke
- Round <N>, on the trigger "<one phrase of the request>": I <what
  happened — skipped acknowledge / froze / refused without a reason>.
  Behavior change for next event: <one sentence with a when and a what>.

## One moment my script worked
- Round <N>, on the trigger "<one phrase of the request>": I said
  "<the exact phrase that landed>." My partner noted: "<their feedback>".

## One behavior the drill added to my list
- <One sentence, when + what — this is the bridge to the mini-project
  contract. It often updates the team's "no" script section.>
```

Total: 150–250 words. Commit the file. Push.

---

## Rubric (for self-grading)

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Both partners played both roles | 25% | 12 min Defender + 12 min Pusher each, no skipping |
| Each Defender ran the script at least 6 times | 20% | Six rounds per block, hard 45-second cap |
| The 6-minute midpoint debrief happened | 20% | Both partners named one break + one win + one behavior |
| Written debrief committed | 15% | The three-section file, 150–250 words, in the prep repo |
| Pushers were plausibly excited, not caricatures | 10% | Trigger lines were read with energy, not in apology voice |
| Voice was blameless and team-room throughout | 10% | Even on a fumbled round, the debrief stayed scope-disciplined |

---

## Stretch (only if you both finish under 25 minutes)

- **Add a "hour 32 panic" shape.** Invent a fourth scope-creep shape: "we have to ship X in the last 4 hours or we will look unprofessional." Run two more rounds on that shape. Note in the debrief whether your script needs a fourth variant.
- **Record one round.** With permission, audio-record one Defender round and listen to it once afterward. The *pace* of your "no" is something only the recording surfaces.
- **Trade your contract drafts.** If you have both started the mini-project, swap drafts. Read one section of each other's contract aloud. Note one phrasing you want to steal.

---

## Submission

When done:

1. Both partners commit `week-04-prep/challenge-01-debrief.md` to their own repos.
2. In each repo's debrief, link the partner's debrief URL.
3. Post in the cohort channel: "Did the scope-stress drill with [@partner]. One behavior I'm adding to the contract: <one sentence>."
4. Read your partner's debrief and leave one specific comment on a *moment they named*, not a generic compliment.

You are now meaningfully readier for [Week 5 — Scoping Discipline](../../week-05/), where the "no" script is one of the inputs to the pre-event scoping worksheet. The reps you just ran are the reason that worksheet will not feel theoretical.

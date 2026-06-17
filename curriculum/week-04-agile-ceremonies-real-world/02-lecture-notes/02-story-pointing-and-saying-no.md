# Lecture 2 — Story Pointing and Saying No

> **Duration:** ~1 hour of reading.
> **Outcome:** You can run a planning-poker round on a 10-item backlog in 10 minutes using the 1-2-3-5 scale. You can defend story points as a relative-size measure, not a time estimate. You can name the three predictable shapes of hackathon scope creep — hour-2, hour-12, hour-24 — and write the three-sentence "no" script that meets each of them without breaking the room.

If you only remember one sentence from this lecture, remember this:

> **Pointing is relative size; the "no" is a concrete sentence. Treat points as hours and you produce missed commitments. Refuse scope without a script and you produce a wounded teammate. Both kill the team faster than any single technical failure.**

Lecture 1 taught you the three ceremonies and their failure modes. Lecture 2 teaches you two specific skills that thread through every ceremony: how to *size* the work the team commits to, and how to *refuse* the work the team should not commit to. Pointing happens in the opening 15 minutes; the "no" happens at hour 2, hour 12, hour 24. The skills are the second half of the team-mode rhythm.

---

## 1. Why story points at all in a hackathon

The first reaction beginners have to "point a story in a 36-hour event" is: *why?* We do not need formal Agile. We just code. The points are corporate theatre.

That reaction is wrong. Here is the steel-man:

> **C4 voice:** points are not a planning tool on a 36-hour clock. They are a *disagreement-surfacing* tool. The value is not the number; the value is the 30-second argument that produces the number. The argument is what aligns the team on what "done" means.

### 1.1 What pointing actually does

Three short sentences:

- **Pointing surfaces hidden disagreement about size.** Teammate A points "auth" at 1; teammate B points it at 5. The 4-point gap is a disagreement about what "done" means for auth. Surface it in 30 seconds.
- **Pointing produces a shared mental model.** After three pointing rounds, the team has a calibrated sense of what "1 point" means in this team's vocabulary. That calibration is the artifact.
- **Pointing forces a cut conversation early.** A backlog where every item is "5 points" forces the team to ask "what do we cut to fit 36 hours?" at hour zero, not at hour 24.

If pointing does not do these three things, it is theatre. If it does, it is one of the highest-ROI 10-minute investments the team makes all event.

### 1.2 The 1-2-3-5 scale

C4's default scale is **1-2-3-5**, plus the question mark.

```
┌────────────────────────────────────────────────────────────┐
│  THE 1-2-3-5 SCALE — WHAT EACH NUMBER MEANS                │
│                                                            │
│  1   │ Trivial. One person, one short session. (~30 min-2h)│
│  2   │ Small. One person, a focused session. (~2-4h)       │
│  3   │ Medium. One person, half a working day. (~4-6h)     │
│  5   │ Large. One person, a full working day. (~6-10h)     │
│  ?   │ Unknown. Needs a spike, a sub-card, or a cut.       │
│                                                            │
│  No 8. No 13. No 21. If a card feels like 8, point it as   │
│  "?" and split it into two cards before re-pointing.       │
└────────────────────────────────────────────────────────────┘
```

The hours in parentheses are *not* time commitments. They are calibration anchors so the team's first round has a shared starting point. After three rounds, the hours fall away and the relative sizes do the work.

> **Why no Fibonacci above 5:** in a 36-hour event, anything bigger than 5 is "this card is too big for one person; split it." Letting the team point 8 or 13 invites the false-precision argument ("is it 8 or 13?") that adds nothing. Cut the scale; force the split.

### 1.3 Points are relative, not absolute

A 3-point card on team A might be a 1-point card on team B. That is fine. Points only have to be calibrated *within the team*, for *this event*. They do not transfer across teams. They do not transfer across events.

What this means in practice:

- Do not say "this is 3 hours of work" when you mean "this is 3 points."
- Do not commit "we will ship 20 points in 36 hours" as a velocity target — there is no velocity history in hackathons.
- Do say "this card is the same size as the auth card we pointed, which we agreed was 3."

The phrase that produces this is **"relative to what?"** When a teammate points a card, the calibrating question is "relative to what other card you have pointed?" That question forces the comparison; the comparison forces the calibration.

---

## 2. Running a planning-poker round in 10 minutes

Planning poker is the format. Done right, you point 10 items in 10 minutes. Done wrong, you spend an hour on one item.

### 2.1 The format

```
┌────────────────────────────────────────────────────────────┐
│  PLANNING POKER — 10 ITEMS IN 10 MINUTES                   │
│                                                            │
│  Setup (1 min):                                            │
│    - Facilitator reads the 10 items aloud, one phrase each │
│    - Each teammate has a 1-2-3-5-? card or sticky note    │
│                                                            │
│  Per item (~50 sec):                                       │
│    1. Facilitator reads item (5 sec)                       │
│    2. Teammates think silently (15 sec)                    │
│    3. Reveal cards simultaneously (5 sec)                  │
│    4. If unanimous: record + move on (5 sec)               │
│    5. If split: highest and lowest argue 20 sec each       │
│       → re-vote once → if still split, point as "?"       │
│       → record + move on                                   │
│                                                            │
│  Total: ~10 min for 10 items.                              │
└────────────────────────────────────────────────────────────┘
```

Two notes on the format:

- **Reveal simultaneously, not sequentially.** Sequential reveals anchor everyone on the first number. Simultaneous reveals surface real disagreement. Cards face-down until "show."
- **The 20-second argument cap is the discipline.** If the highest-pointer cannot explain in 20 seconds why the card is larger, the disagreement is not productive. Force "?", split the card, move on.

### 2.2 Points-as-promises — the fourth failure mode

Lecture 1 §5.4 named this failure mode and deferred it to here. The full version:

> **Points-as-promises** is when a teammate treats a 3-point estimate as "3 hours" and is surprised when the card takes 5. The points failed because they were read as a time commitment, not a size estimate. The cure is to use the word "points" not "hours" in every reference.

```
┌────────────────────────────────────────────────────────────┐
│  POINTS-AS-PROMISES — LANGUAGE TEST                        │
│                                                            │
│  BAD:                                                      │
│  "I'll have the auth done in 3 hours — it's 3 points."     │
│  "We have 20 points left, we have 8 hours, we're fine."    │
│  "You said this was 2 points and it took all day."         │
│                                                            │
│  GOOD:                                                     │
│  "Auth is 3 points — same size as the search card we      │
│   shipped yesterday. I'll start now and call out if it    │
│   grows."                                                  │
│  "We have 20 points and ~8 hours. The remaining points     │
│   are mostly 5s, so we're tight. Cut?"                     │
│  "Auth grew from 3 to 5. Same as we did with search.       │
│   Note for next event: auth on a new framework is always   │
│   5+ for this team."                                       │
└────────────────────────────────────────────────────────────┘
```

The good column references *other cards* and uses points language. The bad column slides into hours and produces missed commitments. The first time a teammate says "you said 3 hours" when you said "3 points," correct the language immediately. It is the smallest possible course-correction and it pays compounding interest.

### 2.3 What to do with a "?" card

A "?" card means the team could not agree on size. Three options, in order of preference:

1. **Split the card.** "Auth" → "login form" + "session storage" + "logout". Re-point each piece. Usually this resolves the disagreement.
2. **Spike it.** Assign one teammate 30 minutes to investigate, then re-point at the next stand-up. Useful for cards that are unknown because of a technical question, not a scope question.
3. **Cut it.** If splitting and spiking both feel like overkill, the card is probably not worth doing for this event. Move it to SHOULD or WON'T.

A backlog with 3+ "?" cards after a pointing round is a backlog the team has not yet scoped. Re-read your MoSCoW from Week 3 and cut before re-pointing.

---

## 3. Saying no without breaking the room

The "no" is the single most under-practiced skill on a hackathon team. Every team will face at least three scope-creep requests during a 36-hour event. Each one is a small fork — say yes and the room stays warm and the build runs late; say no and the build ships but a teammate may feel rejected. The script in this section is how you say no *and* keep the room.

### 3.1 The three predictable scope-creep shapes

Scope creep is not random. It follows three predictable shapes across the 36-hour clock:

```
┌────────────────────────────────────────────────────────────┐
│  THE THREE PREDICTABLE SCOPE-CREEP SHAPES                  │
│                                                            │
│  HOUR 2 — "while we're in there"                           │
│    Teammate: "while I'm adding the login form, let me      │
│    add password reset — it's quick."                       │
│    Trigger: in-flow optimism. Card-in-hand bias.           │
│                                                            │
│  HOUR 12 — "we have time for one more"                     │
│    Teammate: "we shipped MUST early — what if we add a     │
│    leaderboard? Judges will love it."                      │
│    Trigger: midpoint confidence. Plus-one ambition.        │
│                                                            │
│  HOUR 24 — "we have to add X or the demo dies"             │
│    Teammate: "wait, the demo needs auth, otherwise nobody  │
│    will believe it's real."                                │
│    Trigger: late-stage demo anxiety. Reality-check spiral. │
└────────────────────────────────────────────────────────────┘
```

Each shape needs a different "no." All three use the same three-sentence script.

### 3.2 The three-sentence "no" script

```
┌────────────────────────────────────────────────────────────┐
│  THE C4 "NO" SCRIPT (THREE SENTENCES)                      │
│                                                            │
│  1. ACKNOWLEDGE: "That's a good catch / a real concern."   │
│  2. REFUSE WITH A REASON: "We agreed in the contract that  │
│     <feature> is in WON'T because <one-sentence reason>."  │
│  3. OFFER A CHEAPER ALTERNATIVE: "What if we <cheaper      │
│     version> instead? It hits the same job in <smaller     │
│     points>."                                              │
└────────────────────────────────────────────────────────────┘
```

The script is three sentences for three reasons:

- **Acknowledge** says "I heard you." It keeps the teammate in the room.
- **Refuse with a reason** says "the team already decided this together." It cites the contract, not your personal preference. You are not the gatekeeper; the contract is.
- **Offer a cheaper alternative** says "I am not just blocking — I am steering us back." This is the sentence that turns a "no" into a "yes, *to a smaller thing*."

### 3.3 The three "no" scripts, one per shape

The script in §3.2 is the template. Here are three filled-in versions, one per scope-creep shape:

**Hour 2 — "while we're in there":**

> "Good catch — password reset is a real need. We put it in WON'T at hour 0 because auth-related cards always grow to 5+ points and we have one MUST left. What if we ship login-only and add a paragraph in the README that says 'password reset is in the roadmap'? That hits the credibility without the build time."

**Hour 12 — "we have time for one more":**

> "I love that we're ahead — that's real. We agreed leaderboard is in WON'T because it adds a new database table and we already have one. What if we add a static 'top three demos' section to the landing page, hard-coded from our test data? It looks like a leaderboard without being one."

**Hour 24 — "we have to add X or the demo dies":**

> "I hear the demo anxiety — it's a real concern. We put auth in WON'T at hour 0 because the build-time would push MUST past hour 30. What if we add a 'demo user' button on the live URL that auto-fills the form? It hits the 'is this real?' question without the auth build."

Three sentences. Three filled-in versions. The structure transfers; the specifics change.

### 3.4 What the script is NOT

The script is not:

- **A way to win the argument.** The script is a way to *exit* the argument with a smaller, agreed-on next step. If the teammate disagrees with the smaller version, that is a 90-second sidebar after stand-up, not a 30-minute meeting now.
- **A way to be polite while still saying no.** Politeness is a side effect. The script's job is to keep the team aligned on the contract.
- **A way to avoid the cut.** The script *makes* the cut by routing the request to a smaller version. The cheaper alternative is the cut.
- **A way to make a teammate feel bad for asking.** If your "no" reads like a rejection of the teammate's ideas in general, you wrote the wrong "no." The script names the *contract*, not the teammate's judgment.

### 3.5 The "yes" variant — when scope creep is right

Sometimes a scope-creep request is *correct*. The team got pessimistic at hour 0, MUST is shipping early, and the request is a real improvement. The "no" script then becomes a "yes, on these conditions":

> "Good catch — I think you're right. Let me propose: we point it, we cut something else of equal points from MUST, and we re-confirm at the next stand-up. If anyone disagrees, we drop it."

This is the *negotiated yes*. It pulls scope through the same pointing-and-cutting process as the original backlog. It is not "yes, sure, let's add it" — that is the failure mode. A scope addition without an equal-points cut is the path to hour-32 panic.

---

## 4. The pointing-no thread across all three ceremonies

The pointing and the "no" thread through every ceremony in Lecture 1:

- **Stand-up:** the team-cut question (Q4 in §2.1) is the moment for the "no" script. A teammate proposes adding X; the timekeeper or any teammate runs the script.
- **Internal demo (12h, 24h):** the cut-or-keep call (§3.3) is a re-application of the "no" script to the team's own MUST. "We're cutting feature Y because it does not appear in the stranger's path."
- **Retro:** the three-behaviors line includes — for most teammates — at least one behavior about pointing or about saying no. "At hour 2 of the next event, I will run the three-sentence 'no' script the first time I hear 'while we're in there.'"

The pointing-no skill is not a separate Lecture 2 topic that sits alongside Lecture 1's ceremonies. It is the *muscle inside* the ceremonies. Lecture 1 told you the shapes; Lecture 2 puts the muscle in them.

---

## 5. Common pointing-and-no failure modes

Four to recognize, in addition to the four ceremony failure modes from Lecture 1.

### 5.1 The unanimous-3 backlog

> **Symptom:** every card in the backlog points at 3. No 1s, no 5s, no "?" cards.

This means the team has not been honest about sizes. Either the small cards are over-pointed (because nobody wants to look lazy by pointing a 1), or the big cards are under-pointed (because nobody wants to be the pessimist). Run the pointing round again with a one-rule constraint: "this round, every teammate has to point at least one card a 1 and at least one card a 5."

### 5.2 The "I'll figure it out" point

> **Symptom:** a teammate points a card at 1 with the phrase "I'll figure it out."

A 1-point card with an unknown solution is not a 1-point card. It is a "?" card pretending to be a 1. Re-point at "?", spike it for 30 minutes, then re-point with data.

### 5.3 The silent "no"

> **Symptom:** a teammate disagrees with a scope addition but says nothing in the stand-up. They start building the new feature anyway. Or they refuse to and the team finds out at hour 20.

The silent "no" is the worst failure mode. The fix is the contract: the contract specifies that any scope addition runs through the stand-up's Q4 cut question, period. A silent "no" is a contract violation, not a personality issue.

### 5.4 The escalating yes

> **Symptom:** the team says yes to scope addition #1 at hour 2. The team says yes to #2 at hour 12. The team says yes to #3 at hour 24. At hour 30, half of MUST is not shipped.

Each individual yes seemed reasonable. The accumulated cost was fatal. The fix is the "yes, *with an equal-points cut*" rule from §3.5. Any added scope produces an equal-points cut from the same backlog. No exceptions.

---

## 6. The script-in-the-contract

The team contract (this week's mini-project) includes a section for the team's three-sentence "no" script *and* a section for the team's pointing scale (defaults to 1-2-3-5 unless someone has a strong reason). The reason both live in the contract is that both are easier to follow when they are written down before hour 0 than when they are improvised at hour 2.

A team contract without the "no" script will not produce a "no" at hour 2. A team contract without the pointing scale will produce a different scale every event. Both sections are the discipline.

```
┌────────────────────────────────────────────────────────────┐
│  THE PRE-FILLED "NO" SCRIPT IN THE CONTRACT                │
│                                                            │
│  When a teammate proposes adding scope mid-event:          │
│                                                            │
│  1. "That's a good catch / a real concern."                │
│  2. "We agreed in the contract that <feature> is in WON'T  │
│     because <reason>."                                     │
│  3. "What if we <cheaper alternative> instead?"            │
│                                                            │
│  If the teammate insists: the request goes to the next     │
│  stand-up's Q4 cut question, with an equal-points cut      │
│  from MUST as a precondition.                              │
└────────────────────────────────────────────────────────────┘
```

This block is what you commit. The fill-ins (`<feature>`, `<reason>`, `<cheaper alternative>`) are event-specific; the structure transfers.

---

## 7. Practicing the "no" before you need it

The "no" script reads easy in a lecture. It is hard at hour 12 when a teammate is excited about a leaderboard. The cure is rehearsal: Exercise 3 this week is the dry-run. Run it.

The single best rehearsal is to practice the "no" *out loud* with another person — a roommate, a sibling, a club-mate — in a 5-minute drill:

1. Hand them the three scope-creep shapes from §3.1.
2. They pick one at random and read the "while we're in there" line aloud.
3. You respond with the three-sentence script.
4. Repeat with the next shape.
5. Switch roles.

Five minutes of this drill is worth more than 30 minutes of reading. The vocal cords catch the awkwardness that the eyes skip; the awkwardness is the muscle you are building.

### 7.1 What to expect the first time

Your first three "no" attempts will probably:

- Skip sentence 1 (acknowledge) because you are eager to get to the refuse.
- Phrase sentence 2 as a personal preference ("I don't think we should…") rather than a contract reference ("we agreed in the contract that…").
- Forget sentence 3 entirely (offer alternative), so the conversation ends on a refusal with nowhere to go.

That is fine. The drill names the misses; the next event runs the script cleaner. Re-read Week 3 Lecture 2 §2 — the blameless retro voice — if you are tempted to self-blame the misses.

---

## 8. Pointing and saying no, transferred to the contract

The contract section that holds this lecture is two boxes:

```
┌────────────────────────────────────────────────────────────┐
│  CONTRACT SECTION — STORY POINTING                         │
│                                                            │
│  Scale: 1-2-3-5-?                                          │
│  Round time: 10 min for 10 items, 50 sec/item              │
│  Cards: simultaneous reveal, no anchoring                  │
│  Disagreement: highest and lowest argue 20 sec each,       │
│    re-vote once, then "?" if still split                   │
│  No 8, no 13. Cards bigger than 5 must split.              │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  CONTRACT SECTION — SAYING NO                              │
│                                                            │
│  When a teammate proposes mid-event scope addition:        │
│  1. ACKNOWLEDGE the concern.                               │
│  2. REFUSE with reference to the contract's WON'T list.    │
│  3. OFFER a cheaper alternative that hits the same job.    │
│                                                            │
│  Scope additions require an equal-points cut from MUST.    │
│  Disagreement on a "no" goes to the next stand-up's Q4.    │
└────────────────────────────────────────────────────────────┘
```

Both boxes go directly into the mini-project template. The template's sections 6 and 7 (from Lecture 1 §9.1) are these two boxes, filled in with your team's defaults.

---

## 9. The bridge to Week 5

Week 5 sharpens scoping discipline into a *36-hour scoping worksheet* — the artifact that turns the contract you wrote this week into a cut-list you can hold under the real clock. What carries forward:

- The 1-2-3-5 pointing scale.
- The three-sentence "no" script.
- The "scope additions require equal-points cuts" rule.
- The WON'T list as the most-important MoSCoW column.

What Week 5 adds:

- A pre-written cut-list — what gets cut at hour 2, hour 12, hour 24 — before the event starts.
- A "demo-ability test" that runs the stranger demo on a pre-event walk-through.
- A scoping rubric that audits your contract against the real event's prompt.

The two weeks together — Week 4's contract and Week 5's worksheet — are the team-mode preparation for the Week 7 dry-run and the Week 10 real event. Lecture 1 was the rhythm; this lecture was the muscle. Next week is the *map*.

---

## 10. Recap

- Story points are relative size, not time. The 1-2-3-5 scale plus "?" is the C4 default. No 8, no 13. Bigger than 5 means split the card.
- Planning poker: 10 items, 10 minutes, simultaneous reveal, 20-second argument cap on splits.
- Points-as-promises is the fourth ceremony failure mode. The fix is language discipline — "points" not "hours."
- Three predictable scope-creep shapes: hour 2 ("while we're in there"), hour 12 ("we have time for one more"), hour 24 ("we have to add X or the demo dies").
- The three-sentence "no" script: acknowledge, refuse with a reason, offer a cheaper alternative.
- The "yes, *with an equal-points cut*" rule is the only acceptable scope-addition pattern.
- Four pointing-and-no failure modes: unanimous-3 backlog, "I'll figure it out" point, silent "no", escalating yes.
- Practice the "no" out loud before the event. Five minutes of drill beats 30 minutes of reading. Exercise 3 is the rehearsal.
- The contract holds both — the pointing scale section and the "no" script section. Pre-fill before hour 0; refine at the retro.

Return to [Lecture 1 — Stand-up, Demo, Retro, Compressed](./01-stand-up-demo-retro-compressed.md) once more on Sunday before the quiz. The ceremonies and the muscles inside them are a single skill; the lecture split is for your reading, not for the team-room.

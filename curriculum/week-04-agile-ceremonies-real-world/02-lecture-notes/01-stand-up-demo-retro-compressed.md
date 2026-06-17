# Lecture 1 — Stand-up, Demo, Retro, Compressed

> **Duration:** ~1 hour of reading.
> **Outcome:** You can defend the three Agile ceremonies — stand-up, demo, retro — as compression targets for a 36-hour event. You can run a 60-second team stand-up with a rotating timekeeper, schedule the 12h and 24h internal demos, and run a 30-minute team retro at hour 36. You can name the four most common ceremony failure modes and the test that detects each one.

If you only remember one sentence from this lecture, remember this:

> **A ceremony that does not produce a decision is a meeting. Stand-up produces a cut. Demo produces a cut. Retro produces three behaviors per teammate. If a ceremony ends with applause and no decision, it failed — repeat it tomorrow with a shorter clock.**

Week 3 taught you the solo loop: scope, build, demo, retro, alone, on a clock. Week 4 keeps the loop and adds three to five humans. The job is to compress the same Agile ceremonies that take an hour each in a three-week corporate sprint into shapes that fit *inside* a 36-hour event. The point is not "do Agile properly." The point is to extract the smallest dose of each ceremony that still produces the decision that ceremony exists for.

---

## 1. Why ceremonies at all on a 36-hour clock

The first reaction beginners have to "do Agile ceremonies in a hackathon" is: *why?* We have 36 hours. We need every minute for code. Stand-ups are corporate theatre. Demos are for the end. Retros are after the event.

That reaction is wrong on all three counts. Here is the steel-man:

> **C4 voice:** ceremonies are not overhead on a 36-hour clock. They are the *cheapest* coordination tool you own. Skip the stand-up and you pay for the skipped coordination with a half-day of duplicated work at hour 18. The math is brutal.

### 1.1 What each ceremony is actually *for*

Three short sentences, one per ceremony:

- **Stand-up exists to surface blockers and decide cuts.** Not to report progress. Progress is on the board; read the board. Stand-up asks "what is in the way?" and "what do we cut to still ship?"
- **Demo exists to test what a stranger would see.** Internal demos at hour 12 and 24 are not for applause. They are for catching the gap between "what we built" and "what a stranger could click and understand."
- **Retro exists to produce three behavior changes per teammate, for the next event.** Not to process feelings. The artifact is the list; the list is the point.

If a ceremony does not produce its decision, the ceremony failed. Failing a ceremony in week one of a real job means tomorrow's stand-up runs shorter and tighter. Failing a ceremony in a 36-hour hackathon means you lost coordination value for an hour and now you cannot get it back. Run the ceremonies tight.

### 1.2 The compression rule

| Ceremony | Corporate length | Hackathon length | What you cut to get there |
|----------|------------------|------------------|---------------------------|
| Stand-up | 15 min × 4 people = ~3 min/person | 60 sec/person, 5 min total for 5 people | Status reporting; "yesterday I…" filler; manager updates |
| Demo (internal) | 60 min sprint review | 15 min at hour 12, 15 min at hour 24 | The presentation slides; the Q&A; the stakeholder theatre |
| Demo (judge) | 5–10 min judge demo | 3 min strict, per Week 3 strip | Anything that does not fit the four-band strip |
| Retro | 60 min sprint retrospective | 30 min at hour 36 | Open-ended feelings; "what could we do better?"; the manager-led discussion |

The compression is not "do less Agile." It is "extract the decision from each ceremony in a smaller dose." A 60-second stand-up still surfaces a blocker. A 15-minute internal demo still produces a cut decision. A 30-minute retro still produces three behaviors per teammate. The doses are smaller; the decisions are the same.

---

## 2. The 60-second stand-up

The team stand-up is the ceremony you will run most. On a 36-hour event, you run it five or six times: hour 0 (opening), hour 6, hour 12, hour 18, hour 24, hour 30. The hour-36 mark is the retro, not the stand-up. Set a recurring alarm.

### 2.1 The four questions

```
┌────────────────────────────────────────────────────────────┐
│  THE 60-SECOND TEAM STAND-UP — FOUR QUESTIONS              │
│                                                            │
│  1. What did I ship in the last 6 hours? (10 sec)          │
│  2. What is the next 6 hours of work? (15 sec)             │
│  3. What is in my way? (10 sec)                            │
│  4. What do we cut to still ship? (25 sec, team answers)   │
│                                                            │
│  60 seconds per teammate for Q1-Q3.                        │
│  Q4 is a team question, asked once at the end.             │
│  Total for a team of 5: ~3.5 minutes. Hard cap: 5 minutes. │
└────────────────────────────────────────────────────────────┘
```

The four questions are not the same as the Week 3 solo stand-up's four questions. The team version adds "what is in my way?" — which is the whole point of stand-up — and replaces "what is still not on the live URL?" with the team-scale cut question.

### 2.2 The rotating timekeeper

Stand-up needs a timekeeper. The timekeeper is *not* the team lead. The timekeeper rotates each stand-up. The timekeeper has two jobs:

1. **Cut people off at the 60-second dot.** Not 75 seconds. Not "one more sentence." The dot.
2. **Read the four questions aloud at the start.** Same script every stand-up. Boring on purpose.

The rotation matters because the timekeeper role concentrates social cost — being the person who cuts a teammate off mid-sentence. Rotating spreads that cost evenly and prevents one person from becoming "the stand-up boss."

> **C4 voice:** the timekeeper is not a manager. The timekeeper is the alarm clock with a name on it. Treat the role like dishes — rotate it, do it well for ten minutes, hand it off.

### 2.3 The written board update

Every stand-up produces one artifact: a written board update. Three lines per teammate, in a shared note. Concretely:

```
STAND-UP — Hour 12, <DATE>
Timekeeper: <name>

<Teammate 1>:
  - Shipped: <one phrase>
  - Next: <one phrase>
  - Blocker: <one phrase or "none">

<Teammate 2>:
  - Shipped: ...
  - Next: ...
  - Blocker: ...

Team cut decision: <one sentence> OR "no cut this hour"
```

The written artifact is what survives the ceremony. A stand-up without a written board update is a meeting that produced nothing. The note lives in a shared Notion, a `STANDUPS.md` in the repo, a pinned Discord message — anywhere all teammates can see it. The location is your team contract's job to specify; the existence is non-negotiable.

### 2.4 What stand-up is NOT for

- It is not a status report to the team lead. The board has the status.
- It is not a problem-solving session. If a blocker needs a 20-minute discussion, the discussion happens *after* stand-up with the two or three teammates who need to be there. Not during.
- It is not a re-planning session. Re-planning happens at the 12h or 24h demo, on its own clock.
- It is not the place to demo work. Demoing during stand-up means the stand-up ran 15 minutes. Cut it.

If a stand-up exceeds 5 minutes for a team of five, the next stand-up's timekeeper has one job: cut everyone harder.

---

## 3. The internal mid-event demo

The internal demo is the ceremony beginner teams skip first. It is also the ceremony that catches the most expensive failures — the scope creep that has eaten ten hours, the deploy that has been broken since hour 8, the MUST feature nobody can actually click yet.

### 3.1 The 12h and 24h checkpoints

```
┌────────────────────────────────────────────────────────────┐
│  THE TWO INTERNAL DEMOS — 36-HOUR EVENT                    │
│                                                            │
│  Hour 12 — "Are we on the live URL?"                       │
│    - Click through the MUST feature on the deployed URL.   │
│    - If you cannot, the MUST feature does not exist yet.   │
│    - Decision: keep MUST as-is, or cut and replace.        │
│    - 15 minutes. Hard cap.                                 │
│                                                            │
│  Hour 24 — "Would a stranger understand this?"             │
│    - Pick one teammate to play "stranger."                 │
│    - They click the live URL with no context.              │
│    - If they cannot perform the MUST verb, the build fails │
│      the demo-or-die test. Cut features, polish path.      │
│    - 15 minutes. Hard cap.                                 │
└────────────────────────────────────────────────────────────┘
```

Two demos, 30 minutes total out of 36 hours. The ROI is among the highest in the entire event.

### 3.2 The "stranger" test

At hour 24, the demo's whole job is to surface the gap between "what we built" and "what a stranger sees." The cleanest way is to designate one teammate as the *stranger* for the demo. That teammate:

- Has not touched the live URL in the last 4 hours.
- Opens the URL with no setup, no instructions, no warmups.
- Tries to perform the MUST verb the team built toward.
- Narrates aloud what they see and what they expect.

The other teammates listen silently. They do not coach. They do not correct typos. They do not say "oh, you have to click the other button." The whole point is the silence; the whole value is the friction the stranger surfaces.

### 3.3 The cut-or-keep call

Every internal demo ends with one named decision: **cut or keep.** Concretely:

- **Cut**: name one feature from MUST that becomes SHOULD or WON'T in the remaining hours.
- **Keep**: name the one remaining hour where, if MUST is not on the live URL, you cut anyway.

A demo that ends without a cut-or-keep call failed. Re-do it at the next hour mark with a 10-minute cap. The decision is the artifact, not the demo.

### 3.4 The demo-as-showcase failure mode

Teams new to internal demos often turn them into showcases — "look what I built, isn't it cool?" That is not the job. The job is to find what to cut. If your hour-24 demo ends with applause and no cut decision, the demo failed.

> **C4 voice:** the internal demo is the meeting where you say "the thing we built is not yet the thing a stranger would understand, and here is what we cut to fix that." Applause is later. At hour 24, applause is the enemy.

---

## 4. The 30-minute team retro

The hour-36 retro is the ceremony beginner teams either skip or run for two hours. Both are wrong. Thirty minutes, tight, with a structured agenda, produces a list of three behaviors per teammate. That list is the entire point.

### 4.1 The agenda

```
┌────────────────────────────────────────────────────────────┐
│  THE 30-MINUTE TEAM RETRO — AGENDA                         │
│                                                            │
│  Min 0–2    │ Facilitator restates the goal: 3 behaviors   │
│             │ per teammate, written down, by hour 36:30.   │
│  Min 2–10   │ Silent writing. Each teammate fills KEEP /   │
│             │ START / STOP on a shared doc. No talking.    │
│  Min 10–20  │ Round-robin. Each teammate reads their bullets│
│             │ aloud. 2 min/teammate, hard cap.             │
│  Min 20–28  │ Each teammate names 3 behaviors they will    │
│             │ change at the next event. 60 sec/teammate.   │
│  Min 28–30  │ Facilitator commits the doc to the repo.     │
└────────────────────────────────────────────────────────────┘
```

The silent-writing block (min 2–10) is the most under-used technique in team retros. Talking-first retros are dominated by the loudest voice in the room. Writing-first retros surface every voice. Use the silent block. Set a timer. Honor it.

### 4.2 The facilitator role

The retro needs a facilitator. The facilitator is *not* the team lead and is *not* the retro's note-taker. The facilitator has three jobs:

1. Restate the goal at minute 0.
2. Enforce the timer at every transition.
3. Commit the doc to the repo at minute 28.

That is the entire role. The facilitator participates in the silent writing and round-robin like everyone else. Rotating the facilitator across events (week 4 → week 8 → week 10) builds a team that can run a retro without any single person being the "retro person."

### 4.3 The three-behaviors line, at team scale

Each teammate produces their own three-behaviors list. Same shape as the Week 3 solo retro: *when* + *what*, evidence-anchored. The team does not merge them into a single team list. The reason is mechanical: behaviors are personal habits, and a team-merged list dilutes them into committee-speak.

A retro for a team of four produces twelve behaviors total. That is fine. The next event, each teammate carries their own three. The team is the union of personal habits, not a single shared one.

### 4.4 The blame retro failure mode

The retro fails when a teammate's sentence is phrased "X broke Y." Even if X did break Y. Especially then. Re-read Week 3 Lecture 2 §2 — blameless voice, applied to systems, not selves.

At team scale, blame is more tempting because there is a name to point at. The facilitator's silent fourth job is to re-phrase any blame sentence on the fly: "the sprint board did not catch the rate limit" instead of "Pat broke the rate limit." Practice the translation; you will need it.

```
┌────────────────────────────────────────────────────────────┐
│  TEAM-SCALE BLAMELESS TRANSLATION                          │
│                                                            │
│  "Pat broke the deploy at hour 20."                        │
│   → "Our hourly stand-up did not check the deploy URL      │
│      after each merge; the failure went unseen for 4 hours."│
│                                                            │
│  "Sam took too long on the auth flow."                     │
│   → "Auth was sized at 5 points; nobody flagged that as    │
│      'too big for the remaining time' at the 12h demo."    │
│                                                            │
│  "The team did not listen when I said cut."                │
│   → "The 12h demo ended without a named cut decision; the  │
│      cut request did not enter the board update."          │
└────────────────────────────────────────────────────────────┘
```

The right column reads slower. It also produces a fix. The left column reads faster and produces a wound. Hackathon retros must produce fixes, not wounds.

---

## 5. The four ceremony failure modes

Four predictable failure modes, one per ceremony plus one that cuts across. Recognize them in your own team as they happen, not in the retro after.

### 5.1 The silent stand-up

> **Test:** did at least one teammate ask another teammate a question during stand-up?

If no, the stand-up was a round of status reports. Status reports go on the board. The whole point of stand-up is the *exchange* — "you mentioned a blocker on auth; I have a working pattern from Week 2, ping me after this." If nobody asks anybody anything for a full stand-up, the next one's timekeeper opens with: "before we start: blockers from the last six hours — who needs help with what?"

### 5.2 The demo-as-showcase

> **Test:** did the demo end with a named cut-or-keep decision?

If no, the demo was a showcase. Showcases feel good. They produce nothing. The internal demo's whole value is the cut decision the team makes after watching a teammate fail to perform the MUST verb. If you finish the demo and everyone says "great job!", you did not run a demo; you ran a celebration. Re-run it in 90 minutes with the stranger test.

### 5.3 The blame retro

> **Test:** were any sentences in the retro phrased "Pat broke Y"?

Even one such sentence flunks the retro. The facilitator translates on the fly. If the facilitator missed it, the next ceremony's facilitator opens with: "before we start: every sentence about a teammate names a system, not a person. Practice round."

### 5.4 Points-as-promises (the fourth, cross-ceremony, failure)

> **Test:** did anyone treat a point estimate as a time commitment?

This one is covered in Lecture 2 §2.2 — story-pointing under time pressure. The short version: a "3-point" task is *relative size 3*, not "3 hours." Teams new to pointing slide constantly into treating points as hours. The slide kills the points' value and produces missed estimates that read as missed commitments. We will solve this in Lecture 2; flag it as a failure mode you will see your team hit.

---

## 6. Sequencing the ceremonies inside a 36-hour event

Knowing the ceremonies is half the battle. Sequencing them inside a 36-hour event is the other half. Here is the C4 default schedule:

```
┌────────────────────────────────────────────────────────────┐
│  THE 36-HOUR CEREMONY CLOCK                                │
│                                                            │
│  Hour  0:00  │ Opening stand-up + planning poker (15 min)  │
│  Hour  6:00  │ Stand-up #2 (5 min)                         │
│  Hour 12:00  │ Stand-up + internal demo (20 min)           │
│  Hour 18:00  │ Stand-up #4 (5 min)                         │
│  Hour 24:00  │ Stand-up + internal demo (20 min)           │
│  Hour 30:00  │ Stand-up #6 (5 min)                         │
│  Hour 33:00  │ Judge-demo dress rehearsal (15 min)         │
│  Hour 36:00  │ Submit, then 30-min team retro              │
│                                                            │
│  Total ceremony time: ~90 min out of 2160 min (~4%).       │
└────────────────────────────────────────────────────────────┘
```

Ninety minutes of ceremony across a 36-hour event is the C4 default. If your team's first contract specifies more, cut it. If it specifies less, you are skipping the 24h demo, which is the most expensive cut you can make.

### 6.1 The opening stand-up + pointing round

Hour zero deserves a longer ceremony than later stand-ups. You will:

- Run a 5-minute stand-up — introductions if needed, one sentence each on background, the team's one-sentence prompt.
- Run a 10-minute planning-poker round on the top 6–10 backlog items. Lecture 2 covers the mechanics.
- Commit the team contract to the repo (drafted in this week's mini-project).

Total: 15 minutes. The opening hour is the most over-thought hour in any hackathon; the team-mode opening is no different. Re-read Week 3 Lecture 1 §4 on the opening-hour ritual; everything there applies, with the team-contract commit added.

### 6.2 What to do when a ceremony slips

Ceremonies slip. The 12h demo runs 25 minutes instead of 15. The retro at hour 36 ends at hour 37. That is fine *once*. Twice is a pattern. Three times means the timekeeper or facilitator needs a re-orientation — re-read this lecture's §2.2 (timekeeper) or §4.2 (facilitator) and try again.

Do not "make up for" a slip by cutting the next ceremony. The next ceremony's job is the next decision; cutting it costs you that decision. If the 12h demo ran long, the 18h stand-up still runs the full 5 minutes.

### 6.3 What if a teammate refuses ceremonies?

This happens, especially on a team of strangers. One teammate decides ceremonies are "corporate" and skips them. The right response is a 30-second sidebar:

> "We agreed to the contract at hour 0. The stand-up is 60 seconds of your time. If it stays useless after three rounds, we cut it in the retro. Until then, we run it. Yes?"

Most refusals fold at that sentence. The refusal is usually less about the ceremony and more about the discomfort of being interrupted at 60 seconds. The contract you commit this week is the artifact that holds the team to its own decision.

---

## 7. Reading a stand-up update

Reading other teammates' stand-up updates well is a skill in itself. The skill is not "read everything carefully." The skill is "scan for blockers, ignore status filler."

### 7.1 What to look for

- **Any blocker.** This is the line that earns the rest of the update. "Blocker: deploy URL has been 502 for 90 min" is the line that triggers a sidebar.
- **Any cut decision in the team line.** "Team cut: dropping the second seeded example." Read it; carry it forward; do not bring the cut item back at hour 24.
- **Any pattern across two consecutive updates.** "Same blocker reported by two teammates in two consecutive stand-ups" means the team has a structural issue, not a single-task issue.

### 7.2 What to ignore

- **The "shipped" line, unless it is "shipped: nothing."** "Shipped: nothing" is a blocker in disguise. Otherwise, the board has the actual list of shipped items; the stand-up's phrase is a summary, not a record.
- **The "next" line, unless it contradicts MUST.** If a teammate's "next: building the leaderboard" appears and leaderboard is in WON'T, that is a sidebar. Otherwise the next line is informational.

### 7.3 The 90-second post-stand-up sidebar

After every stand-up, the timekeeper looks at the updates and asks: "any sidebars?" A sidebar is a 90-second pull-aside between 2–3 teammates to resolve a blocker or align on a sudden cut. The remaining teammates go back to building.

Sidebars are the *result* of stand-up. If no sidebars happen across three consecutive stand-ups, the stand-ups are not surfacing the right things. Re-read the four questions; ask Q3 ("what is in my way?") with more force.

---

## 8. The ceremony muscle, transferred from Week 3

You ran a one-person version of each ceremony last week:

- The hourly self stand-up (Week 3 Lecture 1 §5) is the prototype of the team stand-up.
- The three-minute solo demo (Week 3 Lecture 1 §7) is the prototype of the judge demo, with the internal demo as a new ceremony layered on top.
- The structured solo retro (Week 3 Lecture 2 §3) is the prototype of the team retro, with the silent-writing block as the team-scale upgrade.

What transfers cleanly:

- The four-question structure of stand-up (shipped, next, blocker, cut).
- The keep / start / stop columns of retro.
- The blameless voice — though it is harder at team scale, the rule is the same.
- The "what does a stranger see" test for demos.

What needs new muscle:

- **Cutting a teammate off at 60 seconds.** Doing it to yourself is awkward; doing it to a teammate is harder. The rotating timekeeper role is the cure.
- **Asking another teammate's blocker out loud.** The silent stand-up failure mode is the manifestation of nobody being willing to do this.
- **Translating blame into systems on the fly during retro.** The facilitator's invisible fourth job.
- **Demoing for a stranger.** The hour-24 demo's whole format is new — designating a stranger teammate and watching them silently is a skill that does not exist in the solo loop.

This is why Week 4 exists between Week 3 and Week 7. The solo loop is the foundation; the team loop adds three new muscles on top. Lecture 2 will cover the fourth: story-pointing and saying no.

---

## 9. The team contract is the artifact

Every habit in this lecture — the four-question stand-up, the rotating timekeeper, the 12h/24h internal demos, the 30-minute retro, the silent-writing block, the facilitator rotation — needs to be *agreed* by the team before hour 0. The artifact that holds the agreement is the **team contract**, this week's mini-project.

The contract is not optional. A team that does not commit a contract is a team that re-negotiates the ceremonies at every ceremony. That is overhead you cannot afford on a 36-hour clock.

### 9.1 What goes in the contract

Eight sections, all one-page:

1. The team's one-sentence prompt or focus.
2. The stand-up format and schedule.
3. The cut decision protocol (who can call a cut, when).
4. The internal demo schedule and the stranger-test protocol.
5. The retro time and the facilitator rotation.
6. The story-pointing scale (Lecture 2 sets this; default 1-2-3-5).
7. The "saying no" script (Lecture 2 sets this).
8. The conflict-de-escalation step (one paragraph).

The mini-project this week is to draft the template. Each event you bring it to, you fill in 1, 5, and 8 with the team's specifics; sections 2, 3, 4, 6, 7 are pre-filled from your defaults.

---

## 10. Recap

- Three ceremonies, three compressed shapes: 60-second team stand-up, 15-minute internal demo at hours 12 and 24, 30-minute team retro at hour 36.
- Each ceremony exists to produce a *decision*. No decision means the ceremony failed; repeat tomorrow with a shorter clock.
- Rotating timekeeper for stand-up. Rotating facilitator for retro. The roles are alarm clocks with names, not management positions.
- The four failure modes: silent stand-up, demo-as-showcase, blame retro, points-as-promises. One test per mode; learn the tests.
- Sequencing inside 36 hours: ~90 minutes of ceremony total. Anything more is overhead; anything less skips the 24h demo, which is the most expensive cut.
- What transfers from Week 3's solo loop is real (the four-question stand-up, the keep/start/stop, the blameless voice). What does not (cutting teammates off, the stranger-test demo, the silent-writing retro block) needs new muscle.
- The team contract is the artifact. This week's mini-project is the template. Without it, the ceremonies are re-negotiated every ceremony — an overhead a 36-hour event cannot afford.

Continue to [Lecture 2 — Story Pointing and Saying No](./02-story-pointing-and-saying-no.md), where the team learns the 1-2-3-5 pointing scale, runs a planning-poker round in 10 minutes, and writes the three-sentence script that cuts scope without breaking the room.

# Lecture 1 — MoSCoW and the Cut-List

> **Duration:** ~1 hour of reading.
> **Outcome:** You can run a MoSCoW scoping pass on a 36-hour hackathon prompt in under 20 minutes and produce a four-column board that the team will hold to. You can defend the WON'T column as the most-important column, not the least. You can write a *pre-event cut-list* — the named cuts that fire at hour 2, hour 12, and hour 24 — before the event starts, instead of improvising under fatigue. You can name the four most common MoSCoW failure modes and the test that catches each one.

If you only remember one sentence from this lecture, remember this:

> **MoSCoW is not a planning grid; it is a cut-list with names attached. The MUST list says what ships; the WON'T list says what does not, in writing, so that at hour 12 a teammate's excited "what if we add X" lands on a pre-written "no" instead of a fresh argument.**

Week 4 taught you the team contract — *how* the team runs. Week 5 teaches you the scoping worksheet — *what* the team ships. The contract is the rhythm; the worksheet is the map. A team with a contract and no scoping worksheet still drifts; a team with a scoping worksheet and no contract still bickers. You need both, and Week 5's job is to make the worksheet sharp enough to survive contact with a real event prompt.

---

## 1. Why MoSCoW at all on a 36-hour clock

The first reaction beginners have to "do MoSCoW in a hackathon" is: *why?* We have 36 hours. We know what we want to build. MoSCoW is a corporate four-column grid. We will scope as we go.

That reaction is wrong on every count. Here is the steel-man:

> **C4 voice:** MoSCoW is not a planning grid on a 36-hour clock. It is a *pre-written argument*. The arguments you have about scope at hour 12 are arguments you could have had — calmly, slowly, with coffee — at hour 0. MoSCoW is the writing-down of those arguments before fatigue corrupts them.

### 1.1 What MoSCoW actually does

Three short sentences, one per outcome:

- **MoSCoW surfaces hidden disagreement about importance.** Teammate A puts auth in MUST; teammate B puts it in COULD. The two-column gap is a disagreement about what "the build" actually is. Surface it in the first 20 minutes, not in the last 4 hours.
- **MoSCoW produces a shared mental model of the demo.** After the scoping pass, every teammate can name the three things on the MUST list. That alignment is the artifact, not the four-column grid.
- **MoSCoW pre-authorizes the cut conversation.** When a teammate proposes a scope addition, the worksheet says "yes, but cut something from MUST of equal points first." The cut is not a fresh argument; it is a pre-agreed protocol.

If MoSCoW does not do these three things, it is decoration. If it does, it is one of the highest-ROI 20-minute investments the team makes all event.

### 1.2 The four columns, what each one means

C4 uses the standard MoSCoW columns with hackathon-specific length caps. Re-read the BRAND.md scoping chart pattern; this lecture extends it.

```
┌────────────────────────────────────────────────────────────┐
│  THE FOUR COLUMNS — 36h HACKATHON                          │
│                                                            │
│  MUST    | Ships or the demo dies. 3 items max.            │
│          | Each one must be clickable on the live URL at   │
│          | hour 33. No exceptions.                         │
│                                                            │
│  SHOULD  | Ships if MUST is clean by hour 24. 2-3 items.   │
│          | If MUST slips, SHOULD becomes WON'T at hour 12. │
│                                                            │
│  COULD   | Ships if MUST and SHOULD are clean by hour 30.  │
│          | 1-2 items. Almost never ships. Plan for that.   │
│                                                            │
│  WON'T   | Does not ship this event. 4-6 items, written.   │
│          | The most-important column. Refusal lives here.  │
└────────────────────────────────────────────────────────────┘
```

The item-count caps are not soft suggestions. A MUST list with 5 items is a MUST list that has not been cut yet. A WON'T list with 0 items is a WON'T list that the team has not been honest about.

### 1.3 The WON'T list is the most-important column

This is the C4 voice's strongest scoping claim, and it is unfamiliar to most beginners. Three reasons it is true:

- **WON'T is the column that holds the refusal.** When a teammate proposes adding X at hour 12, the worksheet's WON'T list either contains X — in which case the refusal is one sentence ("X is in WON'T, we agreed at hour 0") — or does not, in which case the refusal is a 20-minute argument the team did not budget.
- **WON'T is the column that protects MUST.** A short MUST list is the only kind that ships. A short MUST list requires a long WON'T list, because every item not-in-MUST must be named somewhere. WON'T is where those items live in writing.
- **WON'T is the column that the next event inherits.** "We tried real-time chat last event and put it in WON'T because it ate 8 hours; same call this event." That history compounds. No other column compounds.

> **C4 voice:** the MUST list says what ships. The WON'T list says what does not, *in writing*, *before fatigue corrupts the conversation*. The asymmetry is the discipline.

### 1.4 Compression: 20 minutes for the whole pass

A corporate MoSCoW workshop runs 90–120 minutes. The hackathon version runs 20 minutes. The compression is real and it works because the team is small (3–5 people), the timebox is fixed (36 hours), and most candidate items get cut, not argued.

```
┌────────────────────────────────────────────────────────────┐
│  THE 20-MINUTE MoSCoW PASS — HOUR 0                        │
│                                                            │
│  Min  0 — 3   Brainstorm: every teammate writes 6 candidate│
│               items on stickies. ~30 stickies total.       │
│  Min  3 — 8   Cluster: group obvious duplicates.           │
│               Aim for ~15 unique items.                    │
│  Min  8 —15   Sort: each teammate places stickies in MUST /│
│               SHOULD / COULD / WON'T. 1 min/item.          │
│  Min 15 —18   Cut: MUST > 3 items? Force cut to 3.         │
│               WON'T < 4 items? Add the cuts.               │
│  Min 18 —20   Commit: photograph or transcribe to worksheet│
└────────────────────────────────────────────────────────────┘
```

If your first pass runs 35 minutes, fine. The second pass at the next event will run 22. The third will run 18. The pace is built by reps, not by reading.

---

## 2. The cut-list — pre-written cuts at hour 2, 12, 24

The four-column board is half of the worksheet. The other half is the *cut-list*: a pre-written list of which items get cut at which hour, *before the event*. This is the single most under-practiced scoping artifact, and the one Week 5 spends the most time on.

### 2.1 Why pre-write cuts at all

> **C4 voice:** improvising a cut at hour 24 produces a wound. Pre-writing the cut at hour 0 produces a decision. The difference is whether your tired hour-24 self has to argue or just has to read.

Cuts that fire at hour 2, hour 12, or hour 24 are predictable in shape — Week 4 Lecture 2 §3.1 named the three scope-creep shapes. The cuts that meet those shapes are equally predictable, and you can write them before the event. The cut-list is the document that holds them.

### 2.2 The three predictable cut moments

```
┌────────────────────────────────────────────────────────────┐
│  THE THREE PRE-WRITTEN CUT MOMENTS                         │
│                                                            │
│  HOUR  2 — "while we're in there" cut                      │
│    Trigger: a teammate proposes a "quick add" on a MUST    │
│      card they are already working on.                     │
│    Pre-written cut: the proposed add goes to SHOULD if     │
│      it is small (≤2 points) and SHOULD is not full; else  │
│      to WON'T with a one-line reason.                      │
│                                                            │
│  HOUR 12 — "we have time for one more" cut                 │
│    Trigger: MUST appears clean; the team is tempted to add │
│      a SHOULD item to MUST, or a COULD to SHOULD.          │
│    Pre-written cut: only promote a card up one column if   │
│      the current column is *clickable on the live URL*.    │
│      Not "almost done." Clickable. If not, no promotion.   │
│                                                            │
│  HOUR 24 — "we have to add X or the demo dies" cut         │
│    Trigger: late-stage demo anxiety; a teammate names a    │
│      feature that "feels missing."                         │
│    Pre-written cut: at hour 24, the only allowed scope     │
│      changes are *cuts down*, never additions. Any feature │
│      that "feels missing" gets a README paragraph or a     │
│      static fake — not a build. The build window is closed.│
└────────────────────────────────────────────────────────────┘
```

Three moments, three pre-written cuts. The cut-list lives inside the worksheet, one paragraph per moment. The mini-project at the end of this week is the template that holds them.

### 2.3 The "named cut" rule

Each pre-written cut has a *name*: the specific item that gets cut, not just the protocol. Concretely:

- **Hour 2 cut**: name the *first* SHOULD-list item that would be downgraded if a new add appears. "If anyone proposes a quick add at hour 2, the seeded-examples count drops from three to two."
- **Hour 12 cut**: name the *first* MUST-list item that would be cut if the live URL is not clickable yet. "If MUST is not on the live URL by hour 12, we cut item 3 (multi-user) to single-user."
- **Hour 24 cut**: name the *first* feature that becomes a README paragraph instead of a build. "If we are panicking at hour 24, the leaderboard becomes a static image in the README — not a feature."

The named cut is the discipline. A cut-list without names is a *vague intention*. A cut-list with names is a *decision in advance*.

### 2.4 The cut-list lives next to the worksheet

The cut-list is not a separate file. It is the bottom half of the same scoping worksheet. The four-column MoSCoW board is the top half; the three pre-written cuts are the bottom half. Both together fit on one page. The mini-project at the end of this week is exactly this one-page document.

```
┌────────────────────────────────────────────────────────────┐
│  THE ONE-PAGE SCOPING WORKSHEET — STRUCTURE                │
│                                                            │
│  Top half: MoSCoW board (4 columns, 12–16 items total)    │
│  Middle:   the prompt sentence (one line)                  │
│  Bottom:   the cut-list (3 paragraphs, one per moment)     │
└────────────────────────────────────────────────────────────┘
```

The structure is fixed; the fill-ins are event-specific. You bring the template; the event gives you the prompt; the team fills in the four columns and the three cuts in the first 30 minutes.

---

## 3. How MoSCoW threads the team contract

Week 4's team contract has eight sections; Week 5's worksheet has two halves. The two artifacts share three threads:

### 3.1 Thread 1: the WON'T list is the contract's refusal list

The team contract (Week 4 mini-project) section 7 is the three-sentence "no" script. The middle sentence — "we agreed in the contract that X is in WON'T because Y" — *references the WON'T list*. Without the worksheet's WON'T list, the contract's "no" script has nowhere to point.

> **C4 voice:** the contract holds the *script* for saying no. The worksheet holds the *list* that the script references. Either alone is incomplete; together, they are the full refusal machine.

### 3.2 Thread 2: the cut-list runs through the stand-up's Q4

The team contract's stand-up format (section 2) has four questions; Q4 is "what do we cut to still ship?" The cut-list is what answers Q4 *in advance*. At every stand-up, the team re-reads the cut-list's pre-written cuts and asks: did any of these fire? If yes, run the cut. If no, move on.

A stand-up Q4 without a cut-list is a fresh argument every six hours. A stand-up Q4 with a cut-list is a pre-agreed protocol that runs in 30 seconds.

### 3.3 Thread 3: the demo-ability test runs against MUST

The team contract's internal demo (section 4) tests whether the MUST features are clickable on the live URL at hour 12 and hour 24. The MUST column is *defined* by the worksheet. Without the worksheet, the demo has nothing to test against; without the demo, the worksheet's MUST is not validated.

Lecture 2 covers the demo-ability test in detail. For now, note that MUST and "demo-able" are the *same definition* in C4 voice: a MUST item is one that the team commits to having clickable on the live URL by hour 33. If it is not clickable by hour 33, it was not a MUST. It was a wish.

---

## 4. The four MoSCoW failure modes

Four predictable failure modes for MoSCoW in hackathon practice. Recognize them as they happen, not in the retro after.

### 4.1 The MUST-of-five

> **Symptom:** the MUST list has 5+ items at the end of the scoping pass.

The team has not yet cut. A MUST list with 5+ items always becomes a MUST list with 3 items by hour 24 — but by then the cut has cost real build hours. Cut to 3 at the scoping pass, not at hour 24. The discipline is the cap, not the apology after.

The fix: at the end of the scoping pass, the facilitator counts MUST. If MUST > 3, the facilitator picks the largest MUST item and asks the team: "is this a MUST or a SHOULD?" Repeat until MUST = 3.

### 4.2 The empty WON'T

> **Symptom:** the WON'T column has 0–1 items.

The team has not been honest about what they are *not* building. An empty WON'T column means the team has not yet faced the refusal — every teammate's pet feature is somewhere in MUST or SHOULD. The first scope-creep request at hour 2 will find the team unprepared.

The fix: each teammate names *one feature they personally want to build* that they agree to move to WON'T. That is the test. If no one can name one, the WON'T list is fiction.

### 4.3 The aspirational COULD

> **Symptom:** the COULD column has 4+ items, each one ambitious.

The COULD column is a graveyard for features the team does not want to put in WON'T but knows will never ship. A COULD list with 4+ items is a WON'T list with poor labeling. Move them to WON'T; be honest about it.

The fix: at the end of the pass, the facilitator asks: "of the COULD items, which one would actually ship if MUST and SHOULD were both clean by hour 30?" Whichever one the team names stays in COULD; the rest move to WON'T.

### 4.4 The verbal-only MoSCoW

> **Symptom:** the team talked through MoSCoW but did not write it down.

A MoSCoW pass that lives only in conversation is a MoSCoW pass that does not exist by hour 6. Memory fades; tired teammates re-negotiate. The worksheet is the artifact that holds the decisions when memory fails.

The fix: at minute 18 of the scoping pass, the facilitator's only job is to transcribe the stickies into the worksheet. No drift. No edits at minute 22. Photograph the wall if needed; transcribe within the same hour.

---

## 5. Calibration: what counts as a MUST, SHOULD, COULD, WON'T

The four columns sound clear in the lecture. They are blurry in practice. This section is the calibration.

### 5.1 MUST — the demo-or-die definition

A MUST item is an item that, if missing from the live URL at hour 33, makes the demo *meaningfully worse*. Not "a feature we like." Not "a feature we promised." A feature whose absence the audience would notice in 60 seconds of clicking.

Three tests:

- **The stranger test.** If a stranger opens the live URL with no setup, can they perform the MUST verb? If no, the MUST is not yet a MUST.
- **The demo-script test.** Write the three-minute demo script (Week 6 will deepen this). Does the script reference the MUST item? If not, the MUST is not a MUST.
- **The headline test.** If you had to write one sentence about the build, would the MUST item appear? If not, the MUST is not a MUST.

A MUST item that fails all three tests is not a MUST. Move it to SHOULD or WON'T.

### 5.2 SHOULD — the "clean by hour 24" definition

A SHOULD item ships *if MUST is clean by hour 24*. The conditional matters: SHOULD is contingent. If at hour 12 the team has not yet shipped MUST, the SHOULD items are already de-facto WON'T. Acknowledge that early; cut them officially at hour 12.

Two tests:

- **The conditional test.** Can the team say "we will ship X if MUST is clean by hour 24"? If the team says "we will ship X period," X is a MUST in disguise. Move it up.
- **The cut-down test.** If at hour 12 MUST is not clean, will the team actually cut this SHOULD? If not — if the SHOULD is sacred — it is a MUST in disguise. Move it up. Then cut a real MUST.

### 5.3 COULD — the "almost never ships" definition

COULD items almost never ship in a 36-hour event. That is fine; the column exists to acknowledge "we considered it, we did not cut it, but realistically it will not be in the demo." Most COULD items at hour 36 are still in COULD.

One test:

- **The hour-30 test.** At hour 30, if MUST and SHOULD are both on the live URL, would the team actually start building this COULD? Or would the team polish what is there? In 80% of events, the answer is polish. Plan for that.

### 5.4 WON'T — the named-refusal definition

A WON'T item is an item the team explicitly *refuses* to build this event. Not "we did not get to it." *Refused.* Each WON'T item has a one-sentence reason. The reason matters because the next time someone proposes adding it mid-event, the team's "no" cites the reason, not the column.

Two tests:

- **The reason test.** Does each WON'T item have a one-sentence reason next to it? If not, the WON'T is incomplete. Add reasons.
- **The teammate test.** When read aloud, do all teammates agree with the WON'T list? If one teammate disagrees, the WON'T is not yet a refusal; it is a unilateral edit. Re-discuss.

---

## 6. Sequencing the worksheet inside the event opening

Knowing MoSCoW is half the battle. Sequencing the scoping pass inside the event opening is the other half. Here is the C4 default opening:

```
┌────────────────────────────────────────────────────────────┐
│  THE FIRST HOUR — TEAM-MODE OPENING                        │
│                                                            │
│  Hour 0:00 — 0:05  Team introductions, prompt read aloud   │
│  Hour 0:05 — 0:10  One-sentence prompt agreed by team      │
│  Hour 0:10 — 0:30  MoSCoW pass (20 min, §1.4 above)        │
│  Hour 0:30 — 0:35  Cut-list pre-write (§2.2)               │
│  Hour 0:35 — 0:45  Planning poker on MUST + SHOULD         │
│  Hour 0:45 — 0:50  Roles agreed; first cards assigned      │
│  Hour 0:50 — 1:00  Worksheet committed to repo; build starts│
└────────────────────────────────────────────────────────────┘
```

One hour of ceremony at hour 0. Most beginner teams open with 0 minutes of ceremony and reach hour 4 with no shared model. The one-hour invest produces 30+ hours of saved confusion. The math is brutal.

### 6.1 The "prompt sentence" line

The single-most-important line in the entire worksheet is the prompt sentence:

```
PROMPT: <one user> can <one verb> to relieve <one pain>.
```

The same shape as the Week 1 Hackathon Operating Document's prompt, and the Week 3 solo prompt. The team-mode version is agreed by the team at hour 0:05 and written at the top of the worksheet. Every MoSCoW item is then graded against the prompt: "does this serve the prompt sentence? If not, why is it in MUST?"

A worksheet without a prompt sentence is a worksheet where MUST is whatever the loudest teammate insisted on. The prompt sentence is the third party that holds the line, the same way the contract was in Week 4.

### 6.2 What to do when the team disagrees on the prompt

Disagreement on the prompt sentence at hour 0:05 is a *good* signal — it surfaces the misalignment early. Three options, in order of preference:

1. **Vote.** Each teammate writes their preferred prompt sentence in 60 seconds. Read aloud. Vote. Majority rules. 5 minutes total.
2. **Combine.** If two prompts are close, combine into one sentence. Test the combination against the "is this one user, one verb, one pain?" structure. If yes, use it. If the combination is two-headed, return to vote.
3. **Cut.** If the prompts disagree on the *user*, cut to the user the team has the most empathy for. If they disagree on the *verb*, cut to the verb that is most demo-able.

The disagreement is the value; the resolution is the discipline.

### 6.3 What to do when a teammate joins late

A teammate who arrives at hour 2 missed the scoping pass. The team does *not* re-run MoSCoW for them. Instead:

1. The late teammate reads the worksheet for 3 minutes.
2. They name one item they would propose moving — to MUST, SHOULD, or WON'T.
3. The team votes on the proposed move.
4. If the vote passes, the move happens. If not, the worksheet stands.

3 minutes of read + 5 minutes of vote = 8 minutes. The build resumes at hour 2:08. The worksheet is not re-negotiated; it is amended by motion.

---

## 7. The scoping muscle, transferred from Week 4

You ran a team contract in Week 4. The scoping worksheet builds on it. Three threads carry over; two are new.

What transfers cleanly:

- **The blameless voice from §4.4 (Lecture 1 Week 4) — "the sprint board did not catch the rate limit," not "Pat broke it."** Same voice in the worksheet's WON'T-reasons: "WON'T: real-time chat — adds a new socket layer we do not yet have a pattern for." Not "Pat does not know sockets."
- **The "yes-with-cut" rule from Lecture 2 Week 4 §3.5.** The cut-list at hour 2, 12, 24 is the operationalization of "yes-with-cut" pre-written by hour.
- **The 1-2-3-5 pointing scale from Lecture 2 Week 4 §1.2.** The MUST + SHOULD lists get pointed at hour 0:35–0:45 using the same scale. The total points on MUST is the team's budget; SHOULD is the wishlist.

What needs new muscle:

- **Cutting on the spot at hour 0:18 to get MUST to 3.** Most teams write 5 MUSTs and stop. The 3-item cap is the discipline. Forcing the cut at hour 0:18 is harder than it sounds; the exercises this week rehearse it.
- **Writing the cut-list before the event.** A pre-written cut at hour 2 is conceptually strange — "how can I write the cut before I know what the team adds?" — until you realize the *shape* of the add is predictable (Week 4 Lecture 2 §3.1) and the *shape* of the cut is predictable too.

This is why Week 5 sits between Week 4 and Week 6. The contract is the rhythm; the worksheet is the map; the pitch (Week 6) is the delivery. The three together are the team-mode preparation for Week 7's dry-run.

---

## 8. Reading other teams' MoSCoW boards

A late skill: reading a *different team's* scoping worksheet is one of the most under-used hackathon study habits. Most public hackathon submissions have a project README that contains an implicit MoSCoW (the "what we built" and "what we didn't") even if it does not call it that. Reading three of those across the week sharpens your eye.

### 8.1 What to look for

- **A clear MUST in the README.** "What this does, in one sentence." If the README cannot say it, the team did not have a MUST.
- **A short SHOULD section, usually labeled "features."** Three or four bullets. If the section has 15 bullets, the team had no SHOULD/COULD discipline.
- **A WON'T list — usually labeled "future work" or "not in scope."** This is the rarest section. The teams that have it are the teams that scoped.
- **A "lessons learned" or "what we would cut differently" section.** This is the gold. Read it.

### 8.2 What to ignore

- **The tech-stack list.** Almost always irrelevant to scoping. A team that shipped on the wrong stack still shipped; a team that did not ship on the right stack did not.
- **The "thank you sponsors" line.** Brand decoration. Skip.
- **The screenshots, unless they show a clickable demo.** A polished screenshot does not mean the demo worked; a screenshot of the deploy URL with a real timestamp does.

Homework Problem 5 this week asks you to read three real hackathon project READMEs and produce a 200-word "MoSCoW reverse-engineering" note. The skill builds fast with reps.

---

## 9. The worksheet is the artifact

Every habit in this lecture — the 20-minute MoSCoW pass, the 3-item MUST cap, the long WON'T list, the three pre-written cuts, the prompt sentence at the top — needs to be *captured* in the artifact you bring to the event. That artifact is this week's mini-project: the **36-hour scoping worksheet template**.

The worksheet is not optional. A team without a scoping worksheet is a team that re-negotiates scope at every stand-up. That is overhead you cannot afford on a 36-hour clock — same logic as the contract in Week 4, applied to scope instead of process.

### 9.1 What goes in the worksheet

Five sections, one page:

1. The team's prompt sentence (one line, filled at hour 0).
2. The MoSCoW board (4 columns, 12–16 items total).
3. The points budget (total MUST points, total SHOULD points).
4. The cut-list (3 paragraphs, one per pre-written cut moment).
5. The demo-ability checklist (Lecture 2 covers this; 3–5 bullets).

The mini-project this week is to draft the template. Each event you bring it to, you fill in 1, 2, 3 with the event-specifics; sections 4 and 5 are pre-filled with your defaults from this week.

---

## 10. Recap

- MoSCoW is the C4 signature scoping artifact: MUST / SHOULD / COULD / WON'T, with item-count caps (3 / 2–3 / 1–2 / 4–6) for a 36-hour event.
- The WON'T list is the most-important column. It is the column that holds the refusal and protects the MUST.
- The 20-minute pass at hour 0 is the C4 default. Brainstorm, cluster, sort, cut, commit. Five named steps; 20 minutes.
- The cut-list is the second half of the worksheet: three pre-written cuts, one per predictable moment (hour 2, hour 12, hour 24). Each cut has a *name*, not a vague intention.
- The worksheet threads the team contract: WON'T feeds the "no" script, the cut-list feeds the stand-up's Q4, the MUST feeds the internal demo.
- Four MoSCoW failure modes: MUST-of-five, empty WON'T, aspirational COULD, verbal-only MoSCoW. One test per mode; learn the tests.
- The five worksheet sections (prompt, MoSCoW board, points budget, cut-list, demo-ability checklist) fit on one page. The mini-project this week is the template.
- The bridge to Lecture 2 is the demo-ability test — the bench against which every MUST is validated, on the live URL, at hour 12 and hour 24.

Continue to [Lecture 2 — The Demo-Ability Test](./02-the-demo-ability-test.md), where the team learns to grade every MUST item against the live URL — *not* the IDE, *not* the staging branch — and to run the pre-event walk-through that catches the demo-killing gaps before the event starts.

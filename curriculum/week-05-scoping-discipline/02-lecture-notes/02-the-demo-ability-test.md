# Lecture 2 — The Demo-Ability Test

> **Duration:** ~1 hour of reading.
> **Outcome:** You can grade any MUST item against a *live URL* in 60 seconds and produce a pass/fail with one named gap. You can run a pre-event walk-through against your `hackathon-template` repo that catches the demo-killing gaps before the event starts. You can defend the "live URL is the bench" rule against the four most common shortcuts — localhost, the staging branch, the screenshot, the screenshare. You can name the four demo-ability failure modes and the test that catches each one.

If you only remember one sentence from this lecture, remember this:

> **A MUST item is not "done" when the code compiles. It is done when a stranger can click the live URL at hour 33 and perform the MUST verb. Everything between compile and clickable is a gap; the demo-ability test surfaces those gaps before they kill the demo.**

Lecture 1 taught you MoSCoW — what *goes* on the MUST list. Lecture 2 teaches you the bench against which every MUST is validated: the live URL. The bench is harsh on purpose. A feature that works on your laptop and does not work on the deploy URL is not yet a feature; it is a promise to a feature.

---

## 1. Why the live URL is the only bench

The first reaction beginners have to "the live URL is the bench" is: *why?* The code works. I ran it. The unit tests pass. The staging branch is green. Why does the live URL get to be the judge?

That reaction is wrong on every count. Here is the steel-man:

> **C4 voice:** the judges at hour 33 do not have your laptop. They do not have your staging branch. They have a URL in a browser tab. If the URL does not work, the feature does not exist. The harshness is the point.

### 1.1 What the live URL actually tests

Three short sentences:

- **The live URL tests the deploy pipeline.** A feature that works on localhost and does not work on the deploy URL has a *deploy* bug, not a feature bug. That bug is invisible to localhost testing. The live URL exposes it.
- **The live URL tests the seeded data.** A feature that requires a logged-in user to demo, on a deploy without a seeded test user, is not demo-able. The live URL exposes the missing seed.
- **The live URL tests the third-party dependencies.** A feature that calls an LLM API with a localhost-only key is not demo-able. The live URL exposes the missing prod key.

Three classes of bug; one bench that catches all three. There is no other bench that catches all three. localhost catches the first two and misses the third. The staging branch catches the third and misses the first two. The live URL is the only bench that catches all three.

### 1.2 The four common shortcuts (and why each fails)

Beginners try to substitute four cheaper benches for the live URL. Each shortcut fails for a specific reason:

```
┌────────────────────────────────────────────────────────────┐
│  THE FOUR SHORTCUTS THAT FAIL                              │
│                                                            │
│  SHORTCUT 1 — "It works on localhost."                     │
│    Fails because: deploy bugs are invisible to localhost.  │
│    The MUST item is not validated until it works on the    │
│    deploy URL. localhost is the build environment, not the │
│    bench.                                                  │
│                                                            │
│  SHORTCUT 2 — "It works on the staging branch URL."        │
│    Fails because: staging is often missing prod data,      │
│    prod API keys, or the production CDN config. The demo  │
│    runs on the URL you submit, which is prod.              │
│                                                            │
│  SHORTCUT 3 — "Here is a screenshot of it working."        │
│    Fails because: screenshots are not a click. The judge   │
│    cannot click a screenshot. A demo that requires a       │
│    screenshot to be believed has already failed.           │
│                                                            │
│  SHORTCUT 4 — "I will screenshare from my laptop during    │
│  the demo."                                                │
│    Fails because: most modern hackathons judge async, on   │
│    submitted URLs, not on a live screenshare. Even at      │
│    judge-live events, the judges open the URL after; the   │
│    URL is the bench.                                       │
└────────────────────────────────────────────────────────────┘
```

The discipline is to refuse all four shortcuts during the internal demo. If a teammate says "it works on localhost," the internal demo's facilitator says: "show me on the live URL." If the live URL fails, the feature is not yet done. The internal demo is not the place to grade *intent*; it is the place to grade *clickability*.

### 1.3 The "stranger clicks the URL" definition

A MUST item is *demo-able* when a stranger can:

1. Open the live URL in a browser.
2. Read no documentation, no README, no instructions.
3. Perform the MUST verb in 60 seconds.
4. Close the tab and have understood what the build does.

That is the entire definition. If any of the four steps fails, the MUST is not yet demo-able. The Week 4 internal demo at hour 24 (Lecture 1 §3.2) operationalizes this by designating a teammate as the stranger.

---

## 2. The pre-event walk-through

The demo-ability test runs at hour 12 and hour 24 of the event. But there is an earlier, often-skipped pass: the *pre-event walk-through* on your `hackathon-template` repo, run during Week 5, before any real event. This walk-through catches deploy and seed bugs *before* you arrive at the event with them.

### 2.1 What the walk-through is

```
┌────────────────────────────────────────────────────────────┐
│  THE PRE-EVENT WALK-THROUGH — 30 MINUTES                   │
│                                                            │
│  Min  0 — 5   Clone `hackathon-template` to a fresh dir    │
│               and run `bootstrap.sh`.                      │
│  Min  5 —10   Confirm the deploy URL is live and serves    │
│               the template's default landing page.         │
│  Min 10 —20   Click through the template's seeded demo —   │
│               every interactive element. Note each click.  │
│  Min 20 —25   Pretend you are a stranger. Open the URL in  │
│               an incognito window. Click through again,    │
│               narrating aloud.                             │
│  Min 25 —30   Write the walk-through note: 3 gaps found,   │
│               1 sentence each.                             │
└────────────────────────────────────────────────────────────┘
```

The walk-through is run *this week*, on your `hackathon-template` from Week 2. The point is to *exercise* the template on the live URL — not on localhost, not on a staging branch — and find the gaps before the next event. Exercise 1 this week is exactly this walk-through.

### 2.2 What "gaps" look like

A gap is any of:

- **A seeded record that does not appear on the deploy.** "The example post that was supposed to render on the landing page is empty in prod." Common cause: seed script not run on deploy.
- **An interactive button that 404s.** "The 'submit' button on the demo page returns 404." Common cause: backend route not deployed.
- **A form that succeeds in dev and fails on prod.** "The form succeeds on localhost; on the deploy, it shows a CORS error." Common cause: environment variable for the prod backend URL not set.
- **A page that takes 8+ seconds to load.** "The landing page first-paint is 9 seconds on cold cache." Common cause: server cold-start on the free tier.

Each gap is a one-sentence note. Three gaps is normal; six gaps means your `hackathon-template` from Week 2 has rot and should be rebuilt; zero gaps means you did not actually click through — re-run the walk-through.

### 2.3 The "fresh eyes" pass at minute 20

The incognito-window pass is the secret of the walk-through. After 10 minutes of clicking, your eyes are tuned to the template; you see the demo the way the team that built it sees it. The incognito window gives you fresh eyes — no cached login, no remembered click path, no shortcut.

Most demo-killing gaps are caught in the 5-minute incognito pass, not the 10-minute logged-in pass. Schedule the time.

---

## 3. The demo-ability checklist

The walk-through produces a generic note ("3 gaps found"). The *worksheet* this week's mini-project ships needs a more structured artifact: a per-MUST-item checklist that runs in 60 seconds. This is the demo-ability checklist.

### 3.1 The five-question test

For each MUST item, run these five questions:

```
┌────────────────────────────────────────────────────────────┐
│  THE FIVE-QUESTION DEMO-ABILITY TEST — PER MUST ITEM       │
│                                                            │
│  1. Is the live URL reachable right now? (yes/no)          │
│  2. Can a stranger open it with no setup? (yes/no)         │
│  3. Can the stranger perform the MUST verb in 60 sec?      │
│     (yes/no)                                               │
│  4. Does the MUST verb produce the expected result on the  │
│     live URL — not localhost? (yes/no)                     │
│  5. Is the seeded data visible on the live URL? (yes/no)   │
│                                                            │
│  Five yeses = demo-able.                                   │
│  Any no = not demo-able. Name the gap.                     │
└────────────────────────────────────────────────────────────┘
```

The five questions run in 60 seconds. A team of four can grade three MUST items in 4 minutes flat. This is the cadence of the internal demos at hour 12 and hour 24 — fast, structured, no rationalization.

### 3.2 The "any no" rule

Any "no" in the five questions means the MUST is not yet demo-able. The team does *not* discuss the no. The team *names the gap* (one sentence) and moves on. The discussion of the gap happens after the demo, in a sidebar, with the two or three teammates who own the gap.

> **C4 voice:** the demo-ability test is not a debate. It is a checklist. Each "no" is a gap, written down, owned by a teammate, with a one-sentence fix. The debate about whether the gap matters is a *retro* topic. During the demo, the gap is just a fact.

### 3.3 The "five-yes ceiling" rule

A MUST item with five yeses is demo-able. That is the ceiling. The team does not polish a five-yes MUST further; the team moves to the next MUST item. Polish is a SHOULD or COULD activity, not a MUST one.

Beginners over-polish demo-able MUSTs and under-build not-yet-demo-able SHOULDs. The five-yes ceiling is the discipline that prevents this. Once a MUST passes the test, *move on*.

---

## 4. The cut-or-keep call at hour 12 and 24

The internal demos at hour 12 and hour 24 (Week 4 Lecture 1 §3) run the demo-ability test and produce a *cut-or-keep* call. Lecture 1 of Week 4 named the call; this section operationalizes it against the demo-ability checklist.

### 4.1 The hour-12 decision tree

At hour 12, the team runs the demo-ability test on every MUST item. The decision tree:

```
┌────────────────────────────────────────────────────────────┐
│  HOUR-12 DECISION TREE                                     │
│                                                            │
│  All MUST items pass 5/5? → keep MUST as-is.               │
│    SHOULD items become eligible for upgrade to MUST if     │
│    the team agrees (rare; usually stay in SHOULD).         │
│                                                            │
│  At least one MUST fails 5/5? → cut decision required.     │
│    Options, in order of preference:                        │
│    1. Cut the failing MUST item to SHOULD or WON'T.        │
│    2. Pivot the failing MUST to a simpler version (e.g.    │
│       "single-user" instead of "multi-user").              │
│    3. Re-deploy with a fix in the next 4 hours, with a     │
│       hard re-test at hour 16.                             │
│                                                            │
│  Default: cut, do not extend. Extension is a trap.         │
└────────────────────────────────────────────────────────────┘
```

The default-cut bias is the C4 voice's strongest demo-time claim. Beginners default to extension ("we can fix this in 2 hours"). Veterans default to cutting ("we already lost the buffer; cut, ship the rest, re-add later if we have time"). The default-cut bias is the safer call 80% of the time.

### 4.2 The hour-24 decision tree

At hour 24, the same demo-ability test runs, but the decision tree is harsher because the build window is closing:

```
┌────────────────────────────────────────────────────────────┐
│  HOUR-24 DECISION TREE                                     │
│                                                            │
│  All MUST items pass 5/5? → freeze MUST. Move to polish.   │
│    No more MUST work. Move SHOULD items to live URL or cut.│
│                                                            │
│  At least one MUST fails 5/5? → cut, full stop.            │
│    No more "fix it in 2 hours." At hour 24, a failing      │
│    MUST is cut to SHOULD or WON'T; the build runway is     │
│    for polish and demo-script-fitting, not for new MUSTs.  │
│                                                            │
│  Any SHOULD that is not on the live URL at hour 24:        │
│    → cut to WON'T. No exceptions.                          │
└────────────────────────────────────────────────────────────┘
```

The asymmetry is intentional. At hour 12, fixing a MUST is sometimes the right call. At hour 24, fixing is almost never the right call — the remaining 12 hours are for *polish* of what already ships, not for *building* what does not.

### 4.3 The cut is a re-write, not a delete

When a MUST item is cut at hour 12 or 24, the team does not *delete* it from the worksheet. The team *re-writes* the worksheet:

- The cut MUST item moves to SHOULD or WON'T.
- The reason for the cut is added in one sentence ("cut at hour 12 because deploy URL was 502 for 90 min").
- The worksheet is re-committed to the repo with the cut visible.

The cut is *visible history*. The next event the team reviews the worksheet, the cuts are part of the data. "We cut multi-user at hour 12 last event because deploy was broken; this event, let's seed a deploy-health check at hour 6."

---

## 5. Demo-ability failure modes

Four predictable demo-ability failure modes. Recognize them in your own team as they happen, not in the retro after.

### 5.1 The localhost demo

> **Test:** is the demo running on localhost, or on the deploy URL?

If localhost, the demo failed. localhost is not a bench. Restart the demo on the deploy URL. If the deploy URL fails, that *is* the demo result — and the MUST is not demo-able, cut it.

Most beginner teams do their internal demos on localhost because it is faster. That speed is the failure: every minute spent demoing on localhost is a minute the deploy URL bugs go uncaught. Demo on the URL the judges will use; everything else is theatre.

### 5.2 The seeded-data ghost

> **Test:** does the seeded test data appear on the deploy URL?

The "seeded-data ghost" is when the team's demo data exists on localhost but is missing on the deploy. Most common cause: the seed script ran during local dev but was never run as part of the deploy pipeline. The demo at hour 24 shows an empty page; the team panics.

The fix is preventive: the `bootstrap.sh` from Week 2 should seed prod data as part of the first deploy. If it does not, the Week 2 template has rot; fix it this week before the next event.

### 5.3 The polishing trap

> **Test:** is the team polishing a demo-able MUST, or building a not-yet-demo-able SHOULD?

The polishing trap is the third predictable failure: the team finishes a MUST at hour 16, then spends 6 hours polishing the MUST instead of building the SHOULD. At hour 22 the SHOULD is empty and the MUST is over-polished. The demo is *thin*: one MUST, beautifully styled, no SHOULDs visible.

The fix is the five-yes ceiling rule (§3.3). Once a MUST passes 5/5, *move on*. Polish at hour 28+, when MUST and SHOULD are both demo-able.

### 5.4 The "we'll fix it before the demo" delusion

> **Test:** is the failing MUST being cut, or being "fixed in the next 2 hours"?

The "we'll fix it" delusion is the fourth predictable failure: the team's hour-24 demo finds a failing MUST, the team commits to fixing it in 2 hours, the fix takes 8 hours, the demo at hour 33 is broken. The default-cut bias from §4.1 is the cure; the courage to apply it is the muscle.

A common script: "we have 12 hours left; this is a 2-hour fix; we can absolutely ship it." A common reality: "the 2-hour fix uncovered a 6-hour bug; we now have 4 hours to also polish, write the demo script, and rehearse; we have already lost." The delusion is the misjudged-time-cost; the cure is the cut.

---

## 6. The demo-ability checklist threads the worksheet

The demo-ability checklist (§3.1) is the fifth section of this week's mini-project worksheet. It threads the rest of the worksheet:

### 6.1 Thread 1: the checklist is the MUST-validation method

The MUST column in MoSCoW is the *intent*: what the team commits to building. The demo-ability checklist is the *validation*: how the team knows the MUST is done. Without the checklist, MUST is aspirational; with it, MUST is testable.

### 6.2 Thread 2: the checklist runs at every internal demo

Week 4 Lecture 1 §3 named the two internal demos (hour 12, hour 24). This lecture gives those demos a structured test: the five-question checklist, run on every MUST item, in under 60 seconds each. The internal demo without a checklist is a showcase; the internal demo with a checklist is a validation.

### 6.3 Thread 3: the checklist informs the cut-list

The cut-list (Lecture 1 §2) names *which* MUST gets cut at hour 12. The demo-ability checklist names *why* it gets cut: the specific question that failed. "Cut multi-user at hour 12 because question 3 failed — stranger could not perform the MUST verb in 60 sec."

The "why" matters because it shapes the next event's cut-list. "We cut multi-user last event because the auth flow was 5+ points; this event, multi-user is in WON'T from hour 0."

---

## 7. The demo-script rehearsal (a Week 5 preview of Week 6)

Week 6 is pitch craft — the three-minute demo. Week 5's worksheet feeds Week 6 by making sure every MUST is *demo-able* before the pitch is rehearsed. Two threads carry forward:

### 7.1 Thread 1: the MUST list is the demo script

A clean MUST list of three items is *also* the spine of a clean three-minute demo. Each MUST verb is one beat of the demo:

```
0:00 — 0:30  Hook: who is hurting, the prompt sentence.
0:30 — 1:15  Problem: the pain the prompt names.
1:15 — 2:00  MUST 1 on the live URL: click + show.
2:00 — 2:30  MUST 2 on the live URL: click + show.
2:30 — 2:45  MUST 3 on the live URL: click + show.
2:45 — 3:00  Ask: one number, one ask.
```

A demo that opens at hour 33 without a clean MUST list cannot fit this strip. Week 6's pitch lecture will sharpen the strip; Week 5's worksheet makes sure there is something to put in it.

### 7.2 Thread 2: the live URL is the demo's backdrop

The pitch (Week 6) is rehearsed *on the live URL*. Not on localhost. Not on a screenshare-of-localhost. On the live URL. Week 5's demo-ability test is the gate that makes Week 6's pitch rehearsal possible.

If the live URL is broken at hour 31, the pitch at hour 33 is impossible — the slides do not save you. The discipline of validating MUST against the URL is the discipline of *making the pitch possible*.

---

## 8. The demo-ability muscle, transferred from Week 4 and Week 3

What transfers cleanly from Week 4:

- **The internal demo schedule (hour 12, hour 24).** Same schedule; this lecture adds the structured checklist.
- **The stranger-test definition.** Same definition; this lecture adds the five-question test that operationalizes it.
- **The cut-or-keep call.** Same call; this lecture adds the decision tree.

What transfers cleanly from Week 3:

- **The three-minute solo demo (Week 3 Lecture 1 §7).** Same shape; the team version uses the same three-minute strip but with a clean MUST list as the spine.
- **The "deploy URL or it does not exist" rule (Week 3 Lecture 1 §3).** Same rule; this lecture extends it to every MUST item, not just the deploy itself.

What needs new muscle:

- **The 60-second per-MUST grading.** Doing it on three MUST items in 4 minutes flat, with no rationalization, is harder than it sounds. Exercise 2 this week (the scope-stress game) builds this muscle.
- **The default-cut bias at hour 12 and 24.** The instinct is to extend; the discipline is to cut. Exercise 3 (cut-list rehearsal) builds this muscle.
- **The pre-event walk-through.** A 30-minute walk-through on the `hackathon-template` repo this week catches gaps that would otherwise surface at hour 12 of the next event. The mini-project codifies the checklist.

---

## 9. The worksheet is the artifact (echo)

Same claim as Lecture 1 §9, applied to the demo-ability half of the worksheet. The five-question test belongs in the worksheet, on the same page as the MoSCoW board and the cut-list. The whole worksheet is one page; the mini-project this week ships it.

### 9.1 What the worksheet looks like, after both lectures

```
┌────────────────────────────────────────────────────────────┐
│  THE 36-HOUR SCOPING WORKSHEET — FULL STRUCTURE            │
│                                                            │
│  Header:   event name, date, team handles                  │
│  Section 1: prompt sentence (one line)                     │
│  Section 2: MoSCoW board (4 columns, 12-16 items)          │
│  Section 3: points budget (MUST total, SHOULD total)       │
│  Section 4: cut-list (3 paragraphs, hour 2/12/24)          │
│  Section 5: demo-ability checklist (5 questions per MUST)  │
│                                                            │
│  One page. 50-70 lines including whitespace.               │
└────────────────────────────────────────────────────────────┘
```

The mini-project specifies the template; the event specifies the fill-ins. The structure is reusable; the content is event-specific.

---

## 10. Recap

- The live URL is the only bench. Localhost, staging, screenshots, and screenshares all fail for specific reasons.
- The five-question demo-ability test grades any MUST item in 60 seconds: URL reachable / no setup needed / stranger performs verb in 60s / verb produces expected result on prod / seeded data visible.
- Five yeses = demo-able. Any no = not demo-able; name the gap, do not debate it.
- The pre-event walk-through (30 min, this week) catches deploy and seed gaps in your `hackathon-template` *before* the event starts.
- Hour-12 decision tree: default-cut bias. Hour-24 decision tree: cut, full stop — the build window is closed.
- A cut is a re-write of the worksheet, not a delete. The visible history is the next event's data.
- Four demo-ability failure modes: localhost demo, seeded-data ghost, polishing trap, "we'll fix it" delusion. Tests for all four; learn them.
- The checklist is section 5 of the scoping worksheet. The full worksheet is one page, five sections, opinionated defaults pre-filled.
- The bridge to Week 6 is the demo script — Week 5's clean MUST list is the spine of Week 6's three-minute strip.

Return to [Lecture 1 — MoSCoW and the Cut-List](./01-moscow-and-the-cut-list.md) once more on Sunday before the quiz. The MoSCoW pass and the demo-ability test are one skill; the lecture split is for your reading, not for the team-room. The worksheet is one page on purpose.

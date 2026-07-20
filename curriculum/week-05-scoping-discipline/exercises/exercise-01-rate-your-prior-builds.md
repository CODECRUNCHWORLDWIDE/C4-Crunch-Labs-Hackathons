# Exercise 1 — Rate Your Prior Builds

**Goal:** Grade your Week 3 solo build (and any past hackathon or class project you can recall) against the five-question demo-ability test from Lecture 2 §3.1. By the end of the exercise, you have a written audit of what was actually demo-able versus what felt demo-able-from-the-inside.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

Lecture 2 §1 said it: the live URL is the only bench. Most learners have a Week 3 build that *felt* clean from the inside — they could click through it on localhost, they knew the seeded paths, they were the one teammate who knew which button worked. The defense is a *cold-open* grading pass: open the live URL with no setup, run the five questions, write down what fails. Tuesday-you can judge a build honestly; hour-33-you cannot judge your own.

The exercise is harshest on builds that *feel* polished. Be honest. The audit is the muscle.

---

## What to produce

A file at `week-05-prep/exercise-01-prior-builds.md` (in your `hackathon-template` repo or a new `c4-week-05-prep-<yourhandle>` repo) with:

- A list of 1–3 prior builds you will grade. The Week 3 solo build is required. Past class projects, past hackathon work, or any project with a live URL are valid additions.
- The five-question demo-ability test, run on each build's MUST verb. One pass/fail per question.
- A one-paragraph audit per build: what passed, what failed, what the gap was.
- A reflection paragraph: which of the four demo-ability failure modes (Lecture 2 §5) showed up most across the builds you graded.

---

## Step-by-step

### 1. List the builds you will grade

At the top of `exercise-01-prior-builds.md`, list 1–3 builds. The Week 3 solo build is required; the others are optional but recommended if you have them.

```
BUILDS UNDER AUDIT

1. Week 3 solo prototype
   - Live URL: <paste your deploy URL>
   - MUST verb (from your Week 3 prompt): <the verb you committed to>

2. <Optional: a past hackathon or class project>
   - Live URL: <URL or "not deployed">
   - MUST verb: <the verb the project committed to>

3. <Optional: another past build>
   - ...
```

If your Week 3 build is no longer deployed (free tier sleep, expired domain, deleted repo), note that — and treat the audit as a "what would have failed at hour 33" thought experiment. The honest version of "I cannot test this any more" is *itself* a finding: production builds rot. Plan for it.

### 2. Run the five-question demo-ability test on each build

For each build, open the live URL in an *incognito window* on a device you do not normally use it on (phone, second laptop, a sibling's machine). Run the five questions from Lecture 2 §3.1:

```
DEMO-ABILITY TEST — Build <N>

Q1. Is the live URL reachable right now?         (yes / no)
Q2. Can a stranger open it with no setup?         (yes / no)
Q3. Can the stranger perform the MUST verb
    in 60 seconds?                                (yes / no)
Q4. Does the MUST verb produce the expected
    result on the live URL — not localhost?       (yes / no)
Q5. Is the seeded data visible on the live URL?   (yes / no)

Five yeses = demo-able.
Any no = name the gap in one sentence.
```

The incognito-window step is the secret. Logged-in browsers cache state; logged-out incognito sessions show what a judge sees. Use it.

### 3. Write the one-paragraph audit per build

Below the test results, write a 3–5 sentence audit per build. Cover:

- Which questions passed and which failed.
- The single most surprising finding (the one you would not have predicted from the inside).
- If a question failed: what the gap was, and which of Lecture 2 §5's four failure modes it falls under (localhost demo / seeded-data ghost / polishing trap / "we'll fix it" delusion).
- If all five passed: what the build's *next* gap would be — the one a judge would find on a longer session.

Most Week 3 builds fail Q5 (seeded data) more than the learner expects. The seed script that worked locally often did not run on prod. That is a finding, not a failure of the build.

### 4. Write the reflection paragraph

Below the per-build audits, write a 4–6 sentence reflection answering:

- Which failure mode showed up most across the builds you graded?
- What single behavior would have prevented it? (e.g., "running the seed script as part of the deploy pipeline," or "testing on the deploy URL in an incognito window before declaring the build done")
- How does that behavior translate to a *team* setting? (i.e., which section of next Saturday's scoping worksheet captures it?)

This last bullet is the bridge to the mini-project. The audit is the muscle; the worksheet is where the muscle is captured for the next event.

### 5. Commit

```
git add week-05-prep/exercise-01-prior-builds.md
git commit -m "week 5 exercise 1: demo-ability audit on prior builds"
git push
```

---

## Acceptance criteria

- [ ] `week-05-prep/exercise-01-prior-builds.md` exists in a committed repo.
- [ ] At least one build (your Week 3 solo prototype) is graded.
- [ ] The five-question test is run on each build with pass/fail per question.
- [ ] Each build has a 3–5 sentence audit paragraph.
- [ ] The reflection paragraph names which of the four failure modes (Lecture 2 §5) was most common.
- [ ] The reflection bridges to a specific worksheet section (Lecture 2 §9.1 or Lecture 1 §9.1).
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Run the test in incognito, not your default browser.** Your default browser is logged in, cached, and biased. The judge will be in incognito or a fresh session. Match the judge.
- **Test on a phone or a second device.** The single most-common "passes on my laptop, fails for a stranger" failure is a desktop-only design that breaks on mobile. Half of judges open URLs on a phone first; design for that.
- **Be honest about Q5 (seeded data).** A landing page with placeholder Lorem Ipsum is a failed Q5. A demo with no clickable example data is a failed Q5. Name the gap; do not rationalize.
- **A "no" is not a defeat.** Every "no" is a future event's lesson. The audit is *most valuable* when it surfaces gaps you did not know existed.

---

## What to do if your live URL is dead

If your Week 3 build's live URL is no longer reachable:

1. **Note the cause.** Free-tier sleep, expired domain, deleted Vercel project, broken DB connection. Each is a different finding.
2. **Re-deploy if you can.** Twenty minutes of effort gets the URL back; that is also a finding ("ship rot is real; the demo at hour 33 is only as durable as the deploy pipeline").
3. **If you cannot re-deploy**, run the audit on the *most recent* live build you have. A current build with a current URL is more useful than a hypothetical audit on a dead one.
4. **Add to the reflection paragraph:** what would need to change in your `hackathon-template` to make ship-rot less likely? (Hint: a `health-check.md` or a scheduled ping. Not in scope for this week, but worth noting.)

---

## What is next

Move on to [Exercise 2 — Scope stress game](./exercise-02-scope-stress-game.md), where you run a 20-minute MoSCoW pass on a fake event prompt and force MUST to 3 items.

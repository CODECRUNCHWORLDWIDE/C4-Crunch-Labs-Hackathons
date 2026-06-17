# Lecture 1 — The Six-Hour Solo Build

> **Duration:** ~1 hour of reading.
> **Outcome:** You can defend the six-hour solo build as a rehearsal (not a performance), pick a one-sentence prompt, scope a build into MoSCoW where MUST has one feature, run the hourly cut reflex, apply the hour-five freeze, and ship a live URL by hour six or honestly report why you did not.

If you only remember one sentence from this lecture, remember this:

> **The win is shipping. Not innovating, not impressing, not feature-completing. Shipping a small, live, demoable thing on a clock you did not move.** This week you do it alone. Every following week you do it with a team. The rhythm is the same.

Week 1 told you what hackathons reward: clarity, demo-ability, polish. Week 2 stood up the toolkit so the first six hours of an event are not yak-shaving. Week 3 puts the toolkit and the doctrine in your hands at the same time, on a six-hour clock, with no team to hide behind. The point is to feel the rhythm.

---

## 1. The solo build is a rehearsal, not a performance

A common Week 3 failure mode is to treat the six-hour build like a small hackathon: "I will impress somebody with what I ship." Stop. There is no judge. There is no prize. There is no audience that matters more than future-you reading the retro.

> **C4 voice:** the solo build is the dress rehearsal. The retro is the performance review. Most of the learning is in the retro, not the build.

### 1.1 What the rehearsal is rehearsing

Three things, in order of importance:

1. **The cut reflex.** "What do I cut to still ship?" — said out loud, hourly, even when nothing needs cutting yet. The muscle is built by repetition, not by emergency.
2. **The demo-path discipline.** Knowing — before you write the first line of feature code — which two clicks the judge will perform. Building toward those two clicks. Cutting anything that does not appear in them.
3. **The clock-respecting habit.** When the kitchen timer dings at hour 5:00, you freeze new code, full stop. Not "one more commit." Not "let me finish this function." Freeze.

You will fail at all three the first time. That is what the retro is for.

### 1.2 What the rehearsal is *not*

- It is not a chance to learn a new framework. Re-read Week 2 §4 if you are tempted. You ship in your boring stack.
- It is not a chance to build a product. Six hours is a sketch.
- It is not a chance to skip the demo recording. The recording is the only artifact that survives the day; without it you cannot retro honestly.
- It is not a portfolio piece. The *next* event's submission is the portfolio piece. This week's submission is the receipt that you did the work.

---

## 2. Picking a real prompt

The prompt is the *first* place beginners over-scope. You hear "build anything" and the brain serves up "a Twitter clone with AI replies." Six hours later, nothing is deployed.

### 2.1 The one-sentence rule

Your prompt must fit in one sentence with one user, one pain, and one verb. Concretely:

```
┌────────────────────────────────────────────────────────────┐
│  THE ONE-SENTENCE PROMPT TEST                              │
│                                                            │
│  <one user> can <one verb> to relieve <one pain>.          │
│                                                            │
│  GOOD:                                                     │
│  - A commuter can save the next three bus times so they    │
│    do not refresh the transit app every minute.            │
│  - A reader can paste a long article and get one sentence  │
│    back so they can decide whether to read it.             │
│  - A study-group host can post one prompt and see who      │
│    has not replied yet.                                    │
│                                                            │
│  BAD:                                                      │
│  - "A social platform for X." (no verb, no pain)           │
│  - "A tool with multiple features for managing X." (vague) │
│  - "An AI-powered marketplace." (three over-scope words)   │
└────────────────────────────────────────────────────────────┘
```

If you cannot say it in one sentence on Tuesday, your build is already over scope.

### 2.2 What "real" means

"Real" means: the pain exists for at least one human you can name. You. A roommate. A teammate from a class. A specific friend who texts you about the same annoyance. Not "people in general." Not "the world." One human.

The single most useful question to ask is: **whose afternoon does this small tool fix?** If the answer is "nobody specific," pick a different prompt. The exercise is not to invent a product; it is to scope a build to a real, named pain so you can demo against it later.

### 2.3 Examples that have shipped at past Code Crunch events

- *A vegetarian student* can paste a recipe and get a meat-free swap suggestion.
- *A photo-club organizer* can RSVP-tally a single weekly meetup by emoji.
- *A late-night coder* can have their playlist auto-mute when their commit volume spikes (joke build; it shipped; it was funny).
- *A campus parking-lot user* can mark a spot as "leaving in five" and others can see it.

Each one is one user, one pain, one verb. Each one shipped in six hours. None of them are "novel." All of them demoed.

---

## 3. Scoping the solo build into MoSCoW

You saw MoSCoW in Week 1. On a *team* hackathon, MUST has two or three items. On a *six-hour solo build*, **MUST has one item.** One. Not "one feature plus auth."

### 3.1 The six-hour MoSCoW shape

```
┌────────────────────────────────────────────────────────────┐
│  SCOPE — 6h solo build                                     │
│                                                            │
│  MUST    ✓ ONE demo-able feature, end to end               │
│  MUST    ✓ Live deploy URL the demo can hit                │
│                                                            │
│  SHOULD  ▢ A second small interaction on top of MUST       │
│  SHOULD  ▢ A landing page with one paragraph of copy       │
│                                                            │
│  COULD   ▢ Light/dark toggle                               │
│  COULD   ▢ A second example seeded in the database         │
│                                                            │
│  WON'T   ✗ Auth, login, accounts                           │
│  WON'T   ✗ Multi-user / real-time                          │
│  WON'T   ✗ Database migrations (use seed data only)        │
│  WON'T   ✗ Mobile responsiveness beyond "it does not break"│
└────────────────────────────────────────────────────────────┘
```

Notice **WON'T** carries the real weight. The first time you write a solo MoSCoW you will leave WON'T half-empty; that is the bug. Filling WON'T is the work. Each line you write under WON'T is a future emergency you have already cut.

### 3.2 The "if I demo this, can I demo it?" test

Read your MUST line aloud. Now describe, in two sentences, the screen the judge will see when you click. If you cannot describe the screen, the MUST line is still too vague. Rewrite it.

> **Example.** MUST line: "User can paste an article and get a summary." Demo description: "Judge sees a textarea, pastes a Wikipedia paragraph, clicks Summarize, waits two seconds, sees one sentence appear in a card below." That is concrete. That is demo-able. That MUST line is good.

---

## 4. The opening-hour ritual

Hour zero is the most over-thought hour in any hackathon, solo or team. C4 prescribes a ritual: identical every time, fast, and ending with a live URL.

```
┌────────────────────────────────────────────────────────────┐
│  THE OPENING-HOUR RITUAL (≤ 60 minutes)                    │
│                                                            │
│  Min 0–5    │ Re-read the one-sentence prompt out loud.    │
│             │ Re-read the MUST line. Confirm both.         │
│  Min 5–35   │ Run ./bootstrap.sh week-03-solo-<your-slug>. │
│             │ Push to GitHub. Trigger Vercel + Railway.    │
│             │ Visit both URLs. Confirm 200 OK.             │
│  Min 35–55  │ Wire the simplest possible MUST screen.      │
│             │ One route, one component, one fake response. │
│  Min 55–60  │ Re-deploy. Confirm the MUST screen is        │
│             │ visible on the live URL, not just localhost. │
└────────────────────────────────────────────────────────────┘
```

If your hour-one ends with localhost-only progress, **you broke the "blank page live at hour 2" rule that Week 2 prevented**. Stop, fix the deploy, then continue. New code on a broken deploy is debt.

### 4.1 Why deploy first, feature later

Two mechanical reasons:

- **Deploy errors cluster early.** A wrong env var, a missing build script, a CORS rule that drops requests — these break first, when changes are small and recoverable. At hour five they break under a stack of half-finished features and you cannot bisect them.
- **The deploy URL is the demo's only artifact.** If hour six arrives and the URL is dead, nothing else you built matters for the demo. The deploy is *the* feature.

### 4.2 What a "live URL" must do at hour one

- Return 200 from the root.
- Show a page that says, in plain text, "Hello — \<your prompt sentence\>."
- Have your name or handle visible.

That is the entire spec for hour one. You will be tempted to make hour one look impressive. Resist. Hour one is the receipt.

---

## 5. The hourly cut reflex

Every sixty minutes, on the hour, you stop typing for sixty seconds and answer four questions out loud. (Yes, out loud. Even alone. It surfaces what your eyes have stopped seeing.)

```
┌────────────────────────────────────────────────────────────┐
│  THE 60-SECOND SELF STAND-UP (every hour, on the hour)     │
│                                                            │
│  1. What did I ship in the last 60 minutes?                │
│  2. What is the next 60 minutes of work?                   │
│  3. What in my MUST list is still not on the live URL?     │
│  4. What do I cut to still ship?                           │
│                                                            │
│  Write your answers in a scratch file. One line each.      │
│  Move on.                                                  │
└────────────────────────────────────────────────────────────┘
```

The fourth question is the muscle. Some hours the answer is "nothing yet." Most hours, by hour three or four, the answer is something real — a SHOULD that has crept into MUST, a COULD that ate forty minutes, a deploy bug you have been avoiding.

### 5.1 The "still not on the live URL" trap

Beginners commonly run hours two through four on localhost, planning to "deploy at the end." Deploying at the end is the failure mode. The MUST feature must be on the live URL at the end of *every* hour, not just hour six.

If hour three ends and the MUST is on localhost only, that is a cut. You either fix the deploy in the next 15 minutes or you cut whatever last localhost change broke it and re-deploy the previous-working version. The graveyard of half-deployed builds is real and you do not have to join it.

### 5.2 Out-loud is the format

Whisper if you are in a library. Mutter if you are in a cafe. The point is the *vocal cords*, not the volume. Subvocalizing in your head reads as agreement; out-loud reading catches over-confidence. You will hear yourself say "I will deploy that at hour five" and notice immediately that it is not a plan.

---

## 6. The hour-five freeze

```
┌────────────────────────────────────────────────────────────┐
│  HOUR 5:00 — FREEZE                                        │
│                                                            │
│  No new code paths.                                        │
│  No new components.                                        │
│  No new routes.                                            │
│  No "one more refactor."                                   │
│                                                            │
│  The last hour is for:                                     │
│   - One pass of the demo path, clicked end to end.         │
│   - One pass of the README ("How to run / what it does").  │
│   - The 3-minute demo recording (one or two takes).        │
│   - The retro draft (started in your scratch file).        │
│                                                            │
│  If something broke at 4:55, you ROLL BACK to the last     │
│  green commit. You do not "just fix it real quick."        │
└────────────────────────────────────────────────────────────┘
```

This is the rule most learners break the first time. They will be writing code at 5:45, the deploy will be broken at 5:55, and the retro will start with "I should have frozen at 5:00." Write that retro early; do not earn it.

### 6.1 Why a full hour of freeze

A full hour sounds excessive. It is not. Inside the freeze you will:

- Click your demo path three times to find the crash you did not see while building.
- Re-read your README and discover one wrong copy-paste command.
- Re-record the demo because the first take had your phone ringtone in the audio.
- Push one more deploy because you found a typo in the title tag.
- Write the keep / start / stop columns of the retro while the build is still fresh.

Sixty minutes evaporates. Plan for it.

### 6.2 The rollback rule

If at 5:55 you have a half-finished change and a broken deploy, you **roll back to the last green commit and ship that**. The half-finished change does not exist for demo purposes. This is one of the most important muscles in C4 and it is the one that feels the worst the first time. Roll back. Ship green. Note the change in the retro. Move on.

---

## 7. Demo or die, applied alone

You will demo your build to nobody live this week, but you will *record* a three-minute demo on Saturday or Sunday. The recording is the artifact.

### 7.1 The three-minute strip, recapped from C4 branding

```
[ 0:00 — 0:30 ] hook         | who's hurting + the punch
[ 0:30 — 1:15 ] problem      | concrete, narrow, specific
[ 1:15 — 2:45 ] solution     | walkthrough + demo clip
[ 2:45 — 3:00 ] ask          | one ask, one number
```

You will write the script in Exercise 3 (Friday) and record on Saturday at hour 5:30–5:45.

### 7.2 The two demo-recording mistakes to pre-empt

1. **Live coding on camera.** Do not. Click through the deployed URL. If your demo includes typing, type one short input — not a function body.
2. **No live URL on screen.** The judge wants to see the URL bar. The URL bar is part of the demo. If you cut to a slide for the demo, you have failed the demo-or-die doctrine. Show the live URL. Click. Wait. Show the result.

### 7.3 The "ask" on a solo demo

A team demo's "ask" is for users, capital, beta testers. On a solo Week 3 demo, the ask is **for the retro reader**: "If you've built something like this, tell me one cut I should have made earlier." That ask points the retro reader at the artifact you actually want feedback on — the retro, not the build.

---

## 8. Common solo-build failure modes (forewarned)

Recognize these in your own build *as they happen*, not at hour seven in the retro.

1. **Scope creep at hour two.** "It would be cool if it also did X." Cut X out loud and write the cut in your scratch file.
2. **Polish before deploy.** Choosing a font for thirty minutes before the first deploy has gone green. Deploy first. Font later.
3. **Localhost lock-in.** Every change is "working great on localhost" through hour four. Then deploy breaks at hour 4:45 and you are dead. Deploy hourly, not at the end.
4. **No timer.** You "feel" the hours. You are wrong. Set a real timer. The kitchen-timer rule is not metaphorical.
5. **No recording.** You "will record after the deploy is perfect." The deploy is never perfect. Record at hour 5:30. Re-record at 5:45 if you have time.
6. **No retro.** You ship the URL and close the laptop. The build's value is the retro; without it you ran a six-hour sprint and learned almost nothing.
7. **A retro that praises yourself.** "It went great." That is not a retro; that is a performance review you wrote for an audience of one. Lecture 2 will teach you the blameless self-retro voice.
8. **Treating the build as a product launch.** Posting it to social media, asking for users, hoping it goes viral. It will not. The build is a rehearsal. Treat it like one.

You will see at least two of these eight in your own build. That is fine. Naming them is half of the cure.

---

## 9. Sequencing: what you do this week, in order

Lecture 1 told you the doctrine and the clock. The rest of the week is the application:

1. **Monday — Lecture 1.** You are here.
2. **Tuesday — Exercise 1.** Pick a real prompt. One sentence. One user. One pain.
3. **Wednesday — Exercise 2.** Pre-build the MoSCoW chart and pre-write the hourly clock on paper. Reading your own MoSCoW before the build is the second-most useful artifact of the week.
4. **Thursday — Lecture 2.** Read the post-build retro doctrine. You need this *before* Saturday because the retro starts during the build, not after.
5. **Friday — Exercise 3.** Draft the three-minute demo script. You will not have time to write a script on Saturday at hour 5:45.
6. **Saturday — Mini-Project.** The six-hour solo build, continuous, timer on, clock the lecture. Save the last 30 minutes for the recording and retro draft.
7. **Sunday — Quiz + retro polish.** Take the quiz. Polish the retro. Push everything. Post a one-line update in the cohort channel.

By Sunday night, your solo prototype is live, your demo is recorded, and your retro is committed.

---

## 10. Recap

- The solo build is a rehearsal, not a performance. The retro is where the learning lives.
- The prompt fits in one sentence with one user, one pain, one verb. If it does not, it is over scope.
- MoSCoW for a six-hour build: MUST has one feature. WON'T has more than you think.
- The opening hour is a ritual ending with a live deploy URL — not a clever feature.
- The hourly cut reflex is a 60-second out-loud self stand-up. The fourth question is the muscle.
- Hour-five freeze is non-negotiable. The last hour is for the demo path, the recording, and the retro draft.
- Demo or die applies alone: live URL on screen, no live coding, an "ask" pointing at the retro.
- Eight common failure modes — name them in your own build as they happen.

Continue to [Lecture 2 — The Post-Build Retro](./02-the-post-build-retro.md), where the artifact becomes structured: how to write a blameless retro on yourself, the keep / start / stop columns, and the three-behaviors-to-change line that this week's grade really turns on.

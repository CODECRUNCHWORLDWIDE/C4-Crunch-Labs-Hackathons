# Challenge 1 — Pair Prototype

**Time estimate:** the six-hour solo build itself, plus about 30 minutes of pairing logistics across the week.

> This is the canonical Week 3 challenge in C4: run the same six-hour build as the mini-project, but paired with another C4 learner — on parallel prompts, not the same prompt — with a 60-second sync at every hourly stand-up. The point is to *see your scoping habits from the outside* one week before the team-mode dry-runs of Week 4.

---

## Problem statement

You and one other C4 learner each run a six-hour solo build on Saturday. You each have your own prompt (from Exercise 1), your own MoSCoW (from Exercise 2), your own repo, your own deploy, and your own retro. You do not share a codebase. You do not pair-program. You build separately.

What you share is the **clock and the 60-second sync.** You start at the same minute. You break for a 60-second voice call at every hourly stand-up. You both ship at hour 6:00. You read each other's retros on Sunday.

This is *not* team programming. It is *parallel* solo building with a shared rhythm. The challenge is the first time you experience the team-mode rhythm of Week 4 without the team-mode coordination cost.

---

## Why parallel, not paired

Paired programming on a six-hour clock is a real skill — and it is not the skill Week 3 is teaching. Week 3 is teaching the solo build. Week 4 will teach the team build. The pair-prototype challenge is the *bridge*: solo focus with team-style accountability.

> **C4 voice:** the pair prototype is a duet, not a band. Two soloists on adjacent stages, listening for each other's drift.

The single most useful thing about the pair format is that **your partner will notice scope creep in your work before you do.** At hour three, you will say into the voice call, "I'm adding a small profile section," and your partner will say, "is that on your MoSCoW?" That question is the value of the challenge.

---

## Acceptance criteria

- [ ] You and your partner each ship a public live deploy URL by hour 6:00.
- [ ] You each have a recorded three-minute demo committed.
- [ ] You each have a `retro/RETRO.md` committed, in the template format from Lecture 2 §7.
- [ ] In addition, each of you has a `retro/PAIR-RETRO.md` section that names:
  - one specific moment your partner's scope question helped you cut,
  - one specific moment you noticed your partner over-scoping, and what you said,
  - one behavior the pair format added to your three-behavior list.
- [ ] Your partner's repo URL is linked in your README, and your URL is linked in theirs.

---

## How to run the 6 hours, paired

```
┌────────────────────────────────────────────────────────────┐
│  THE PAIR-PROTOTYPE RHYTHM                                 │
│                                                            │
│  Pre-Saturday: both partners complete Exercises 1, 2, 3    │
│                independently. Trade prompts on Friday.     │
│                                                            │
│  Hour 0  start :00         60-sec sync :55 (call)          │
│  Hour 1  build :00–:55    60-sec sync :55                  │
│  Hour 2  build :00–:55    60-sec sync :55                  │
│  Hour 3  build :00–:55    60-sec sync :55 (midpoint cut?)  │
│  Hour 4  build :00–:55    60-sec sync :55                  │
│  Hour 5  FREEZE :00       60-sec sync :30 (record check)   │
│  Hour 6  ship  :00        60-sec sync :05 (URL trade)      │
│                                                            │
│  Tools: any voice/video call. Discord, Meet, FaceTime,     │
│  phone call. No screen-share. No code-share.               │
└────────────────────────────────────────────────────────────┘
```

### The 60-second sync format

Each partner takes 30 seconds. Same four questions as the solo hourly stand-up (Lecture 1 §5), but spoken to a witness:

```
1. What did I ship in the last 60 minutes?
2. What is the next 60 minutes of work?
3. What in my MUST list is still not on the live URL?
4. What do I cut to still ship?
```

Your partner listens silently for 25 seconds, then has 5 seconds for one sentence of feedback — usually "are you sure that's a MUST?" or "deploy still green?" That is the entire protocol. Hard 60-second cap. Re-start the timer.

---

## The midpoint cut sync (hour 3:55)

The hour-3:55 sync is special: it is the **midpoint cut review.** Re-read the C4 12-hour rule, scaled to six hours:

> At hour three, your remaining scope must fit in three hours plus a 30% buffer (≈ 3h 54min), or you cut.

Your partner's job at hour 3:55 is to listen for whether you are still on a feasible six-hour trajectory, and to ask the cut question explicitly: "name one thing you are cutting in the next hour." If you cannot name anything, your partner repeats the question. They cannot accept "nothing" if the four-question stand-up suggested you are behind.

This is the *only* sync where a partner is allowed to push past the 5-second feedback window. The midpoint cut is worth 30 seconds of friction.

---

## Logistics that go wrong (forewarned)

The challenge fails for predictable reasons. Plan around them.

### 1. Different time zones

If your partner is in another time zone, agree on a *single shared start minute* and do not negotiate hour boundaries. "We both start at 09:00 our local time" does not work — the clock drifts immediately. Pick one timezone for the build and both use it.

### 2. Voice call fatigue

Twelve 60-second calls feels lighter than expected. You may forget one. That is fine — but if you skip two in a row, the format is no longer the pair format. Re-start at the next hour. Note the slip in your `PAIR-RETRO.md`.

### 3. Asymmetric stacks

Your partner uses Next.js full-stack; you use the C4 default. Fine. You are not pairing on code. The sync questions are stack-agnostic. Do *not* spend the 60-second sync explaining your stack-specific bug; that is what your scratch file is for.

### 4. Over-helping

The single biggest pair-prototype failure mode is one partner abandoning their build to help the other. **Do not.** Your job is to listen for 25 seconds, ask one sentence in 5 seconds, and go back to your build. The pair format is parallel solo, not switched roles.

If your partner is genuinely stuck and asks for help during a sync, the right response is: "tell me at the next sync if it is still blocking and we will trade one URL for a 5-minute walk-through after we both ship." Do not abandon your build during your build.

### 5. No screen-share

Tempting. Forbidden. The challenge tests whether you can scope under remote accountability, not whether you can debug under pair-screen-share. If you find yourself wanting to screen-share, the answer is "no, and write that urge in your retro."

---

## Pair-retro additions

In your `retro/PAIR-RETRO.md`, add these three sections beyond the solo retro:

```markdown
## Pair-prototype additions

### The cut my partner helped me make
- Hour <N>, my partner asked "<the question>." I had been about to
  add <feature>. I cut it. Cost saved: ~<minutes>. Result: MUST
  shipped on time.

### A moment I noticed my partner over-scoping
- At hour <N>, my partner said "<paraphrase>." I asked "<your
  question>." They <kept it / cut it>. Lesson for me: <one sentence>.

### One behavior the pair format added to my list
- (This becomes behavior 4 if your solo retro already has 3, or
  it replaces one of the solo 3 if the pair-specific behavior is
  more important.)
```

The third bullet is the bridge to Week 4. It is the first time you will name a behavior that *only* exists in a team-style environment.

---

## Rubric (for self-grading)

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Both partners shipped on time | 25% | Both URLs live at hour 6:00, both demo recordings exist |
| The 60-second sync format was honored | 20% | At least 5 of 6 hourly syncs happened, hard-capped at 60 sec |
| Midpoint cut sync produced a real cut | 15% | At least one partner cut a feature at hour 3:55 in response to the question |
| `PAIR-RETRO.md` exists for both partners | 15% | Both files committed, both reference specific moments |
| Pair format did not collapse into screen-share | 15% | No partner abandoned their build to help the other |
| Voice was blameless and team-room throughout | 10% | Even on a stuck partner, the sync stayed scope-disciplined |

---

## Stretch (only if you both finish under 5:30)

- **Read each other's demo recording before you record your own re-take.** A 5-minute swap at 5:35. One specific note on the partner's hook.
- **Each name one specific Week 4 team-mode behavior you suspect the pair format taught you.** Write it as a Week 4 pre-game note.
- **Try Mob Demo:** record a 2-minute back-to-back combined demo where you each take 60 seconds. Useful Week 4 prep; the time-share discipline transfers.

---

## Submission

When done:

1. Both partners push their solo build repos with the `PAIR-RETRO.md` committed.
2. In each repo's README, link to the partner's repo.
3. Post in the cohort channel: "Paired with [@partner] on the Week 3 build. Both shipped at hour 6:00. Live URLs: [yours], [theirs]."
4. Read your partner's retro and `PAIR-RETRO.md` on Sunday. Leave one specific comment on a *file*, not a generic compliment.

You are now meaningfully readier for [Week 4 — Agile ceremonies, real-world version](../../week-04/), where the pair format becomes a team-of-three-to-five rhythm, with proper stand-ups, demos, and retros under shared scope.

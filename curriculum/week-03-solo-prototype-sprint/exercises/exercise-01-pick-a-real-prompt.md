# Exercise 1 — Pick a Real Prompt

**Goal:** Write the one-sentence prompt your six-hour solo build answers. One user, one pain, one verb. By the end of the exercise, the sentence is in a committed file, you have run it past the four sanity checks below, and you can demo-describe the screen the judge will see in two sentences.

**Estimated time:** 45 minutes.

---

## Why this exercise exists

The prompt is the first place every solo build fails. Lecture 1 §2 said it: "build anything" plus an excited brain produces "a Twitter clone with AI replies," and the build is over before Saturday morning. The defense is a *written* prompt sentence, signed and committed on Tuesday, so Saturday-you cannot edit it under the influence of caffeine and ambition.

---

## What to produce

A file at `week-03-prep/prompt.md` (in your `hackathon-template` repo, or a new `c4-week-03-prep-<yourhandle>` repo if you prefer) with:

- The one-sentence prompt, in the shape from Lecture 1 §2.1.
- The named human whose afternoon this fixes (yourself counts).
- The two-sentence demo-screen description from Lecture 1 §3.2.
- The four sanity-check answers below.

---

## Step-by-step

### 1. Brainstorm three prompts, fast

Set a five-minute timer. Write three candidate prompts in the shape:

```
A <user> can <verb> to relieve <pain>.
```

Do not edit while brainstorming. Three lines. Stop the timer.

### 2. Cut two

Read the three out loud. Cross out the two you do not believe. "Do not believe" means: you cannot name a specific human who has the pain, or you cannot picture the screen, or the verb is not a single concrete action.

You are left with one sentence.

### 3. Apply the four sanity checks

Write the answers to each in `prompt.md`, one or two lines per question. Be honest; the exercise is not graded on the answers being yes.

```
┌────────────────────────────────────────────────────────────┐
│  THE FOUR SANITY CHECKS                                    │
│                                                            │
│  1. WHO HURTS?                                             │
│     Name one specific human (you, a roommate, a friend     │
│     who has texted you about this annoyance). Not "users." │
│     Not "people." One human, named or initialed.           │
│                                                            │
│  2. ONE VERB?                                              │
│     The sentence has one concrete verb (save, paste, mark, │
│     tally, swap). Not two ("save and share"). Not vague    │
│     ("manage," "organize," "handle").                      │
│                                                            │
│  3. ONE SCREEN?                                            │
│     You can describe in two sentences the screen the demo  │
│     judge sees when they perform the verb. If you cannot,  │
│     the prompt is too vague — rewrite.                     │
│                                                            │
│  4. IS THIS BUILDABLE IN 6 HOURS ON THE C4 STACK,          │
│     WITHOUT AUTH, WITHOUT REAL-TIME, WITHOUT MIGRATIONS?   │
│     If no — cut features until yes, or pick a new prompt.  │
└────────────────────────────────────────────────────────────┘
```

### 4. Write the demo-screen description

Two sentences. The first sentence describes what the judge sees when the page loads. The second sentence describes what changes after the verb is performed. Example:

> The judge sees a textarea with the placeholder "paste a recipe here" and a button labeled "Find a swap." After they paste a recipe and click the button, a card appears below with one suggested vegetarian substitution for the most prominent meat ingredient.

That is your North Star for the build. Tape it to your monitor on Saturday morning.

### 5. Commit

```
git add week-03-prep/prompt.md
git commit -m "week 3 prep: pick a real prompt"
git push
```

---

## Acceptance criteria

- [ ] `week-03-prep/prompt.md` exists in a committed repo.
- [ ] It contains a one-sentence prompt in the `<user> can <verb> to relieve <pain>` shape.
- [ ] A specific human is named (initials are fine; "the user" is not).
- [ ] The four sanity-check answers are written, one or two lines each.
- [ ] The two-sentence demo-screen description is present.
- [ ] No banned voice ("rockstar," "ninja," "10x," "crush it").

---

## Hints

- **Pick a pain you can demo, not a pain you can monetize.** This is not a startup. The prompt that wins Week 3 is the one with the clearest demo path, not the one with the biggest market.
- **The pain can be silly.** "I forget which playlist I muted at 2 AM" is a real pain. So is "I cannot find the campus parking spot anyone is leaving." Boring and specific beats novel and vague every time.
- **If you cannot name a human, you are still over scope.** Re-read Lecture 1 §2.2.
- **If your verb is "manage" or "organize," it is not a verb.** Swap for a concrete action.

---

## What to do if you cannot pick

You have three options:

1. **Steal one of the four examples from Lecture 1 §2.3.** They are public; use one as-is for Week 3. You can pick your own for the next solo build.
2. **Ask a friend.** Text someone: "what is the smallest annoyance in your day I could build a one-page tool for in six hours?" The first answer is usually good enough.
3. **Use yourself.** Your last week of frustration probably contained three candidate prompts. Pick the one with the clearest screen.

What you may *not* do is skip the exercise and "decide on Saturday morning." That is the failure mode the exercise prevents.

---

## What is next

Move on to [Exercise 2 — The six-hour clock](./exercise-02-the-six-hour-clock.md), where you turn the prompt into a MoSCoW chart and a written hourly clock for Saturday's build.

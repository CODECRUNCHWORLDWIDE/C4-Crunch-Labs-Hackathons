# Exercise 3 — The "Saying No" Script

**Goal:** Write your three-sentence "no" script for each of the three predictable scope-creep shapes from Lecture 2 §3.1. Read each one aloud. Commit. By the end of the exercise, you have a rehearsed script for the three moments you will face at the next event.

**Estimated time:** 60 minutes (15 min reading + 30 min writing + 15 min drilling and commit).

---

## Why this exercise exists

Lecture 2 §3 said it: the "no" is the single most under-practiced skill on a hackathon team. Most learners face their first scope-creep request at hour 2 of a real event, freeze, and say yes. The defense is a *written and rehearsed* script before the event. Tuesday-you can write a clean refusal; hour-2-you cannot.

Reading the script is not enough. The vocal cords catch the awkwardness that the eyes skip. Five minutes of out-loud drill beats 30 minutes of silent reading. Run the drill.

---

## What to produce

A file at `week-04-prep/exercise-03-saying-no.md` with:

- The three filled-in "no" scripts, one per scope-creep shape (hour 2, hour 12, hour 24).
- A one-paragraph reflection on which script was hardest to write and why.
- A note on whether you read each script aloud, and what was awkward.

---

## Step-by-step

### 1. Re-read the three scope-creep shapes

From Lecture 2 §3.1:

```
HOUR 2  — "while we're in there" (in-flow optimism)
HOUR 12 — "we have time for one more" (midpoint confidence)
HOUR 24 — "we have to add X or the demo dies" (late-stage anxiety)
```

Skim the example scripts in Lecture 2 §3.3. Do not copy them; use them as scaffolding.

### 2. Pick a fake team setup

Use the same fake event as Exercise 1, or pick from these three:

```
A. A team of 4 building a study-buddy matcher.
   MUST: signup + match + send request. WON'T: notifications, calendar, theme.
B. A team of 3 building a campus event finder.
   MUST: list view + add event. WON'T: auth, search, map view.
C. A team of 5 building an AI recipe-swap tool.
   MUST: paste recipe + get swap. WON'T: auth, save history, share.
```

Pick one and note it at the top of `exercise-03-saying-no.md`. The "no" scripts reference the contract's WON'T list, so you need to know what is in it.

### 3. Write the three filled-in scripts

For each scope-creep shape, write the *exact teammate's request line* (the one that triggers the "no") and your three-sentence response. Use this format:

```
HOUR 2 SCRIPT

Teammate's request: "<one sentence the teammate would say>"

Your response:
1. ACKNOWLEDGE: "<your sentence>"
2. REFUSE WITH A REASON: "<your sentence — reference the WON'T list>"
3. OFFER A CHEAPER ALTERNATIVE: "<your sentence — name a smaller version>"
```

Repeat for hour 12 and hour 24. Each script is a triggering request + three response sentences. Total: six paragraphs of script (three triggers, three three-line responses).

### 4. Read each script aloud against a partner or against yourself

If you have a partner: hand them the three triggering requests. They read one at random. You respond with the three-sentence script *from memory* (not reading). They give you 5 seconds of feedback. Switch roles.

If you do not have a partner: read each script aloud yourself, twice. Once normally, once at "hour 24 stress" pace — slightly faster, slightly tireder. The point is to hear how the script sounds *under fatigue*.

Note in the file what was awkward. Common awkwardness: skipping the "acknowledge" sentence, refusing without citing the contract, forgetting the cheaper alternative entirely.

### 5. Reflect on the hardest shape

Below the three scripts, write a one-paragraph reflection (3–5 sentences) on:

- Which shape was hardest to write the "no" for, and why.
- Which sentence (acknowledge / refuse / offer) was hardest to phrase.
- One real-life moment where you should have used this script but did not (group project, work, family — anywhere).

This last bullet is the muscle. The "no" script is not just a hackathon skill; it transfers. Naming the past moment is half of the cure.

### 6. Commit

```
git add week-04-prep/exercise-03-saying-no.md
git commit -m "week 4 exercise 3: three-sentence 'no' scripts"
git push
```

---

## Acceptance criteria

- [ ] `week-04-prep/exercise-03-saying-no.md` exists in a committed repo.
- [ ] The fake team setup is noted at the top with the WON'T list visible.
- [ ] Three filled-in scripts (hour 2, 12, 24), each with a triggering request and three numbered response sentences.
- [ ] Each "refuse" sentence references the contract's WON'T list, not personal preference.
- [ ] Each "offer" sentence names a *cheaper alternative* — a smaller version, not a flat refusal.
- [ ] A note on whether each script was read aloud, and one specific awkwardness.
- [ ] The reflection paragraph names a real past moment where the script would have helped.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Cite the contract, not yourself.** "We agreed in the contract that…" is the right opener. "I don't think we should…" is the wrong one. The contract is the third party that holds the line; you are the messenger.
- **The cheaper alternative is the cut.** If you cannot name a smaller version, you do not understand the request well enough to refuse it. Re-read the teammate's request and find the *job* they are trying to do; offer a smaller way to do that job.
- **The acknowledge sentence is the warmest.** Beginners skip it because they want to get to the refusal. The skip is what makes the "no" feel cold. Do not skip it.
- **Practice reading at hour-24 pace.** A script that lands clean at minute one of a calm Tuesday will *not* land clean at hour 24 of a real event when you are tired. Read it aloud at half-fatigue. Adjust the phrasing if it sounds harsh.

---

## What to do if your "no" feels too harsh

You have three options:

1. **Lengthen the acknowledge sentence.** Two sentences of acknowledgment is fine: "That's a good catch. I had the same impulse at hour 11 myself." Then the refuse.
2. **Soften the refuse with a we, not an I.** "We agreed in the contract" reads warmer than "I don't think." The contract is shared; the refusal is shared.
3. **End the alternative with a question.** "What if we ship the static version instead — would that work for you?" The question invites them back in.

If all three feel forced, the issue is not the script — the issue is rehearsal. Run the drill twice more.

---

## What is next

Saturday: draft the [mini-project — team contract template](../mini-project/README.md). The three exercises feed into the contract: the stand-up format becomes contract section 2, the pointing scale becomes section 6, the "no" script becomes section 7. The contract is the artifact that holds all three.

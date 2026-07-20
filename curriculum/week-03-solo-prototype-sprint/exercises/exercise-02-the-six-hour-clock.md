# Exercise 2 — The Six-Hour Clock

**Goal:** Turn the prompt from Exercise 1 into a written MoSCoW chart and a written hourly clock for Saturday's build. By the end of the exercise, you have a single-page plan you can tape to your monitor and follow without rethinking on Saturday morning.

**Estimated time:** 60 minutes.

---

## Why this exercise exists

Lecture 1 §3 said: on a six-hour solo build, MUST has one item. That is the easy line to read and the hard line to write. Writing it on Wednesday — with a calm brain, away from the keyboard — is the only reliable way to enforce it on Saturday. The brain that has been building for four hours cannot scope; the brain on Wednesday afternoon can.

The hourly clock is the second half: a written, hour-by-hour intent for the build. You will not follow it exactly. The point is to have it to deviate from, on purpose, with awareness.

---

## What to produce

A file at `week-03-prep/clock.md` containing:

1. The MoSCoW chart for the build, in the shape from Lecture 1 §3.1.
2. The hourly clock, hour 0 through hour 6, in the shape below.
3. A list of the WON'T items you will say out loud during the opening-hour ritual.

---

## Step-by-step

### 1. Draft the MoSCoW chart

Copy this block into `clock.md` and fill it in. Use the Sprint Coral monospace shape from the C4 branding.

```
SCOPE — 6h solo build, <DATE>

PROMPT: <your one-sentence prompt from Exercise 1>

MUST    ✓ <one demo-able feature, end to end>
MUST    ✓ Live deploy URL the demo can hit

SHOULD  ▢ <a second small interaction>
SHOULD  ▢ <a landing line of copy>

COULD   ▢ <a polish item>
COULD   ▢ <a second polish item>

WON'T   ✗ Auth, login, accounts
WON'T   ✗ Multi-user / real-time
WON'T   ✗ Database migrations
WON'T   ✗ <one specific feature you are tempted by; name it>
WON'T   ✗ <a second feature you are tempted by>
```

The two named WON'T lines at the bottom are the work. They are the features your Saturday brain will try to smuggle into MUST. Naming them on Wednesday is what stops Saturday from smuggling.

### 2. Draft the hourly clock

Copy this block and fill it in. Each hour is one to three lines. Do not over-plan; the point is intent, not a script.

```
THE SIX-HOUR CLOCK

HOUR 0 (opening ritual)
  - Re-read prompt + MUST out loud
  - bootstrap.sh, deploy frontend + backend, confirm 200 OK
  - "Hello — <prompt sentence>" live on the URL by min 55

HOUR 1
  - Wire MUST screen, simplest possible version
  - Hardcoded data, no real backend logic yet
  - Re-deploy. MUST screen visible on live URL.

HOUR 2
  - Replace hardcoded data with one real backend route
  - 60-sec stand-up at the top of the hour
  - Cut check: anything sneaking out of WON'T?

HOUR 3
  - Polish the MUST screen to demo-quality
  - 60-sec stand-up. Curl deploy URL. Confirm 200.
  - If MUST is not on live URL: roll back to last green commit.

HOUR 4
  - Optional: pick ONE SHOULD if MUST is fully demo-able
  - 60-sec stand-up
  - Begin README "How to run" section

HOUR 5 (freeze begins at 5:00)
  - No new code. Click demo path end-to-end three times.
  - Catch crashes. Roll back if needed.
  - 5:30 — record demo (take 1)
  - 5:45 — record demo (take 2 if needed)

HOUR 6 (ships at 6:00)
  - Final deploy push
  - Draft retro keep/start/stop in scratch file
  - Commit retro draft + push everything
  - Phone the result into the cohort channel
```

### 3. Write the WON'T out-loud script

In `clock.md`, add a section titled **"WON'T list (read aloud at hour 0:00)"** with your WON'T items as a short script:

```
"For the next six hours, I will not build:
 - auth, login, or accounts
 - multi-user features or real-time
 - database migrations beyond a seed file
 - <your tempted feature 1>
 - <your tempted feature 2>
If I catch myself building any of these, I roll back."
```

Yes, read this aloud on Saturday. Lecture 1 §5.2 — out-loud is the format. The vocal cords catch what the brain skips.

### 4. Tape it to your monitor

Print `clock.md` if you can, or open it in a separate window pinned next to your editor. The point is that it is *visible* during the build without you having to switch tabs.

### 5. Commit

```
git add week-03-prep/clock.md
git commit -m "week 3 prep: scope + 6-hour clock"
git push
```

---

## Acceptance criteria

- [ ] `week-03-prep/clock.md` exists in a committed repo.
- [ ] The MoSCoW chart has exactly **one** MUST feature line (plus the "live deploy URL" MUST line).
- [ ] WON'T has at least **five** items, with at least **two** named-specific items beyond the generic three.
- [ ] The hourly clock covers hour 0 through hour 6 with one to three lines each.
- [ ] The "WON'T list (read aloud at hour 0:00)" section exists.
- [ ] No banned voice. No emojis.

---

## Hints

- **The MUST line is the same as the prompt's verb.** "Save the next three bus times" — MUST is "user can save a bus time and see it persist on reload." One verb, one screen.
- **If you have two MUST items, one of them is a SHOULD.** Move it. The second MUST will eat hour 5 every single time.
- **Two named WON'T items is the minimum.** Your brain has at least two features it wants to smuggle in. Name them. The naming is the discipline.
- **Do not plan inside hour 5.** Hour 5 is the freeze. Planning inside the freeze means you are still building inside the freeze; that breaks Lecture 1 §6.

---

## What to do if your MUST does not fit in 6 hours

You have three options:

1. **Make the MUST simpler.** "Summarize an article" → "Summarize the first paragraph of an article using a hardcoded `Lorem ipsum` example." Demo-able, six-hour-able.
2. **Mock the hard part.** A "real" AI call is hard to get right under deadline; a fake response that demos the experience is fine. Lecture 1 §2.3 — the playlist auto-mute joke build was mocked end to end and shipped.
3. **Pick a different prompt.** Go back to Exercise 1. Better to redo the prompt than to ship a half-deployed build.

---

## What is next

Move on to [Exercise 3 — The three-minute demo](./exercise-03-the-three-minute-demo.md), where you draft the demo script before you write the code.

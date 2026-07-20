# Exercise 3 — Record v2 (Improved)

**Goal:** Re-read Thursday's three notes aloud, re-record once against the live URL, watch take 2, and compare the two takes against the demo-timing strip. By the end of the exercise, you have a take-2 recording that fits closer to 3:00 than take 1 did, a side-by-side timing comparison, and a written note on which beat improved most.

**Estimated time:** 60 minutes (5 min note re-read + 5 min recording + 10 min watching + 20 min comparison + 20 min reflection and commit).

---

## Why this exercise exists

Lecture 2 §5 said it: the second take is the artifact; the first take is the data. Most learners try to make take 1 the artifact and abandon the recording when it does not work; the defense is a *planned* second take, run after a structured watch of the first. Take 2 with three pre-read notes lands 80% of the time on the first try. Take 2 without notes is just take 1 repeated.

The compare is the second muscle. A take-2 recording that you do not compare to take 1 is a recording you cannot grade. The contrast is the lesson.

---

## What to produce

A file at `week-06-prep/exercise-03-record-v2.md` with:

- A pre-record re-read of Exercise 2's three notes.
- The hosted link to your take-2 recording.
- The four watches re-run on take 2.
- A side-by-side comparison of takes 1 and 2 against the demo-timing strip.
- A one-paragraph reflection on which beat improved most, and which still needs work.
- A pick: which take you will submit as the final (Saturday's mini-project default is the *better* of the two, with optional take 3).

---

## Step-by-step

### 1. Re-read the three notes aloud

Open Exercise 2's `exercise-02-record-v1.md`. Find the three notes section. Read each note aloud — not silently. The verbal re-read commits the notes to working memory in a way silent reading does not.

```
NOTES RE-READ — Friday, take 2 prep

Note 1 (worst beat): <re-read aloud, then check off>      ✓
Note 2 (filler/trailing): <re-read aloud, then check off>  ✓
Note 3 (structural/timing): <re-read aloud, then check off>✓
```

The three check-marks are the prep. Do not record take 2 without them.

### 2. Re-run the four pre-recording checks

Same four checks from Exercise 2 §1. They do not regress fast, but they regress. Run them again:

```
PRE-RECORDING CHECKS — take 2

CHECK 1 — Live URL reachable.    PASS / FAIL
CHECK 2 — Script ready.           PASS / FAIL
CHECK 3 — Recording tool tested.  PASS / FAIL
CHECK 4 — Room quiet.             PASS / FAIL
```

If a check failed since Thursday — common: the free-tier deploy slept and the URL is now 502 on cold start — fix it before recording. Five minutes; do not skip.

### 3. Record take 2. One take. No restarts.

Same setup as take 1. Same one-take rule. The only differences:

- You re-read the three notes 5 minutes ago.
- You know the script better.
- You catch filler words mid-take (awareness from watching take 1 catches ~50% of them on take 2).

Press record. Run the full 3 minutes. Stop. Export. Host.

```
TAKE-2 HOSTED LINK

URL: <paste host URL>
Host: <YouTube unlisted / Loom public / Vimeo free / other>
Recorded at: <YYYY-MM-DD HH:MM>
Take duration: <minutes:seconds>     (target: 3:00; take-2 typical: 2:55-3:10)
```

### 4. Run the four watches on take 2

Same four watches from Exercise 2 §5. Same order. Twelve minutes total. Log them in the file:

```
WATCH 1 — 1.0x, audio on, video on (3 minutes)

Beat lengths:
  Hook:     <m:ss>   (target 0:30)
  Problem:  <m:ss>   (target 0:45)
  Solution: <m:ss>   (target 1:30)
  Ask:      <m:ss>   (target 0:15)
  Total:    <m:ss>   (target 3:00)

Filler count: <number>

Worst-performing beat: <hook / problem / solution / ask>


WATCH 2 — 1.5x

Structural drift noted:
  - <observation>
  - <observation>


WATCH 3 — 1.0x video-only

Visual audit:
  - Live URL visible on solution beat? yes / no
  - 3 clicks crisp? yes / no
  - Stagnant screens (5+ sec)? yes / no


WATCH 4 — 1.0x audio-only

Audio audit:
  - Hook lands in first 8 sec? yes / no
  - Ask names number AND channel? yes / no
  - Trailing sentences? yes / no
  - Most common filler word: <word>
```

### 5. The side-by-side comparison

Build the take-1 vs take-2 comparison table from Lecture 2 §5.3:

```
TAKE 1 vs TAKE 2 — COMPARISON

                       Take 1     Take 2     Target
Hook length            <m:ss>     <m:ss>     0:30
Problem length         <m:ss>     <m:ss>     0:45
Solution length        <m:ss>     <m:ss>     1:30
Ask length             <m:ss>     <m:ss>     0:15
Total length           <m:ss>     <m:ss>     3:00

Worst beat (named):    <beat>     <beat>     --
Filler count:          <number>   <number>   <5

Note 1 fix applied?    --         yes / no   --
Note 2 fix applied?    --         yes / no   --
Note 3 fix applied?    --         yes / no   --
```

The table is the audit. If take 2 is closer to target on every line, take 2 is the artifact and Exercise 3 is done. If take 2 regressed on a line, that line is the focus of take 3 (Saturday's mini-project session).

### 6. The reflection paragraph

Write 5–8 sentences answering:

- Which beat improved most between take 1 and take 2? Cite the timing change in seconds.
- Which beat still needs work? Cite the timing gap from the target.
- Which of the three notes was easiest to apply? Which was hardest? Why?
- If you were to record take 3, what would be the *one* note (not three) that you would give yourself?
- Which of the five pitch failure modes (Lecture 1 §6) does take 2 still show traces of?

The reflection is short. Do not over-write it. The point is one specific note, not an essay.

### 7. The pick — which take is the final

If take 2 is clearly better (the comparison table shows improvement on most lines), take 2 is the final. Log:

```
FINAL PICK FOR THIS WEEK

Picked take: 2
Reason: <one sentence; e.g., "Take 2 hit 3:05 vs 3:42 on take 1,
  hook now names the user in sentence 1, ask now contains a number">
```

If take 2 is *worse* (rare but possible — most often when the pitcher over-corrected and made the take stiff), record take 3 on Saturday. The mini-project session is designed to absorb take 3 if needed.

If you are unsure, record take 3 on Saturday and decide between takes 2 and 3 then.

### 8. Commit

```
git add week-06-prep/exercise-03-record-v2.md
git commit -m "week 6 exercise 3: take 2 recorded; compared to take 1; final pick logged"
git push
```

---

## Acceptance criteria

- [ ] `week-06-prep/exercise-03-record-v2.md` exists in a committed repo.
- [ ] The three notes from Exercise 2 are re-read and checked off.
- [ ] All four pre-recording checks re-run with PASS / FAIL.
- [ ] The take-2 hosted link is present and reachable.
- [ ] All four watches are logged on take 2.
- [ ] The take-1 vs take-2 comparison table is filled in with real numbers.
- [ ] The reflection paragraph is 5–8 sentences and names which beat improved most.
- [ ] The final pick is logged with a one-sentence reason.
- [ ] Voice is team-room, blameless. No banned voice. No emojis.

---

## Hints

- **Re-read the notes ALOUD, not silently.** The verbal re-read is the activation. Silent re-reading does not work; the take that follows will not carry the corrections without the verbal commit.
- **Pause for 1 second between sentences in take 2.** The pause kills two failure modes at once: filler words ("um" fills the gap that the pause displaces) and trailing sentences (the pause forces a clean stop instead of a fade).
- **Look at the camera, not the script, in the hook.** The script is on a second monitor or printed; the camera is the user-facing eye. The hook is talking to a person, not narrating from a page.
- **Hit the ask with the same energy as the hook.** Most take-2s improve the hook but coast the ask. The ask is the highest-leverage 15 seconds; give it the same attention.
- **Compare with the file open, not from memory.** Take 1 and take 2 are 24 hours apart; your memory of take 1 is already compressing. The video timeline is the bench, not your recollection.

---

## What to do if take 2 is over 3:30

Three options:

1. **Re-cut the longest beat.** Identify the beat with the largest over-run (vs target). Cut one paragraph or one click. Re-record take 3 on Saturday.
2. **Re-pace, do not re-cut.** If the script is tight but the delivery is slow, the fix is pacing. Read the script in 2:50 against a timer (not while recording). If you can read it in 2:50, take 3 should hit 3:00.
3. **Accept the over-run for now, target take 3.** Take 2 with a 3:20 length is still the artifact this week if take 1 was 3:50. The improvement curve is real even if the target is not hit yet.

The C4 default: most learners hit 3:00 on take 3 or take 4. The two-take minimum is the floor. The Saturday mini-project session is where take 3 lands.

---

## What to do if you cringed less on take 2

The cringe decreases with each take. That is the muscle building. Watch for the *trap* version of this:

- **Less cringe on T2 ≠ T2 is good.** A less-cringey watch can mean you got numb to your own voice, not that the take improved. The comparison table is the bench; if T2's numbers are worse than T1's, the take regressed even if it felt better.
- **Less cringe on T2 = T2 is better when the table confirms it.** If the timing is closer to target, the worst beat improved, and the filler count dropped, the lower cringe is real. Accept the artifact; move on to the mini-project session on Saturday.

The cringe is the data; the table is the verdict.

---

## What is next

Saturday: the [mini-project — 3-minute recorded demo](../mini-project/README.md). The three exercises feed into the mini-project: Exercise 1's hook becomes the opener; Exercise 2's take 1 becomes the baseline; Exercise 3's take 2 becomes the candidate. The mini-project session is where you record take 3 (typical) and commit the final recording to your repo's README.

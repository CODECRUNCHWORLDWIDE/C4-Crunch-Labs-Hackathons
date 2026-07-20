# Week 6 Homework

Six practice problems that revisit the week's topics. The full set should take about **2 hours** in total. Work in your `week-06-prep` folder (or the build repo, where the prompt says) so each problem produces at least one commit you can point to later.

Each problem includes:

- A short **problem statement**.
- **Acceptance criteria** so you know when you are done.
- A **hint** if you get stuck.
- An **estimated time**.

The homework is meant to be done *around* the exercises and the mini-project. Most problems pair naturally with a specific lecture section; the order below mirrors the order you encountered the material.

---

## Problem 1 — Rewrite a bad hook

**Problem statement.** Take this deliberately bad hook for a 3-minute hackathon demo: *"Hi everyone, my name is Pat and I'm a sophomore at State University. Today I'm here to present a project that my team and I worked on for the past 36 hours. We call it Quickhelp, and we think it's going to revolutionize how learners get help with their homework. Let me tell you a little bit about it."* Rewrite it as a C4-compliant 30-second hook — three lines, scene + pain + verb handoff — that passes the first-sentence audit.

**Acceptance criteria.**

- File at `week-06-prep/homework-01.md`.
- The original bad hook is at the top.
- The rewritten 3-line hook follows Lecture 1 §2.2's scaffold.
- The first-sentence audit (Lecture 1 §2.1) is run on the rewrite with pass/fail per question.
- The rewrite is spoken-timed (target 25–28 seconds).
- A 1–2 sentence note on what was wrong with the original (buried lede, no user named in sentence 1, no verb in sentence 2).
- Voice is team-room; no banned voice.
- Committed.

**Hint.** The bad hook is bad on four axes: opens with the pitcher, no user named in sentence 1, no pain named in sentence 1, vague verb in line 3 ("revolutionize"). Fix each in turn. The fix is what produces a C4 hook.

**Estimated time.** 15 minutes.

---

## Problem 2 — The "pitch failure mode" diagnosis drill

**Problem statement.** Below are five demo scenarios. For each, name which of the five pitch failure modes (Lecture 1 §6) is happening, and write the one-sentence fix.

1. The pitcher opens with "Sorry the deploy is a little slow today, give me a sec to load."
2. The solution beat clicks through signup, profile, posting, replying, searching, leaderboard, and settings — seven clicks in 90 seconds.
3. The first 30 seconds is the pitcher introducing themselves, the team, and the sponsor before any user or verb is named.
4. The 90 seconds of the solution beat is a voiceover over a static slide showing one screenshot of the build.
5. The last 15 seconds is "thanks for watching, we hope you enjoyed it."

**Acceptance criteria.**

- File at `week-06-prep/homework-02.md`.
- Each scenario is reproduced.
- Each scenario is diagnosed with the named failure mode.
- Each scenario has a one-sentence fix.
- No banned voice.
- Committed.

**Hint.** The fixes are mostly *behavioral*: re-read the five pitch failure modes in Lecture 1 §6 and the test for each. The fix is rarely "be better"; it is almost always "cut the apology / cut to three / re-record on the URL / write a real ask."

**Estimated time.** 15 minutes.

---

## Problem 3 — Watch three public hackathon demos and audit them

**Problem statement.** Find three pieces of recorded hackathon demos — not the C4 lectures, not generic tutorial videos. Sources, in order of preference: (a) Devpost submissions from past major events (MLH, TreeHacks, HackMIT) with embedded videos, (b) YouTube search "hackathon demo 3 minutes," (c) C4's `SPRING-2025/` archive in this repo if it has recorded demos. For each, write a 50-word audit of the strip — does the hook name a user in 8 seconds, does the solution beat show the live URL, does the ask name a number and a channel?

**Acceptance criteria.**

- File at `week-06-prep/homework-03.md`.
- 150–250 words total across the three demos.
- Three video URLs are linked.
- For each: a yes/no on hook (8-second user), solution (live URL visible), ask (number + channel).
- One sentence per demo on which beat was the *strongest* and which was the *weakest*.
- A closing sentence: which one of the three demos you would steal a pattern from for your own recording, and which pattern.
- No banned voice.
- Committed.

**Hint.** The most useful watches are 3-minute demos by working teams, not consulting-firm marketing videos. Look for the hook's first 8 seconds especially — most pitches reveal their fate there.

**Estimated time.** 25 minutes.

---

## Problem 4 — Run the four watches on your own Exercise 2 take 1

**Problem statement.** Run the four watches from Lecture 2 §4.1 on your Exercise 2 take-1 recording. The four watches are: 1.0x audio+video, 1.5x audio+video, 1.0x video-only, 1.0x audio-only. For each, write 2–3 sentences on what you noticed. The point is to *practice the four-watch protocol* — not to invent new findings.

**Acceptance criteria.**

- File at `week-06-prep/homework-04.md`.
- The four watches are run, in order, with 2–3 sentences each.
- The watches are on *your own* Exercise 2 take 1, not a partner's take.
- One observation per watch is *specific* (a timestamp, a beat name, a filler word).
- A closing 2-sentence note: which watch surfaced the most new information.
- Committed.

**Hint.** The video-only and audio-only watches usually surface the most-new information, because they decouple two channels you normally process together. If your "most new" note is one of those two, you ran the watches honestly.

**Estimated time.** 25 minutes.

---

## Problem 5 — Write three different asks for the same build

**Problem statement.** Take your Week-3 build. Write three different versions of the 15-second ask, calibrated to three different audiences:

- **Ask A — Judging round.** The audience is hackathon judges; the ask is a feedback channel and a quantity of expected users.
- **Ask B — Sponsor booth.** The audience is a sponsor representative; the ask is a specific sponsor API or credit.
- **Ask C — Portfolio review.** The audience is a recruiter or internship coordinator; the ask is a contact channel.

Each ask is 2 sentences, ~40 words, ~15 seconds spoken. Each ask passes the last-sentence audit (a number AND a channel).

**Acceptance criteria.**

- File at `week-06-prep/homework-05.md`.
- Three asks drafted, each clearly labeled A / B / C.
- Each ask is 2 sentences with a number and a channel.
- The last-sentence audit is run on each with pass/fail.
- One sentence per ask on *who* the audience is and what the number captures.
- Voice is team-room; no banned voice.
- Committed.

**Hint.** The number in Ask A is usually a feedback quantity ("50 feedback comments"). The number in Ask B is usually a credit amount ("$200 in API credits"). The number in Ask C is usually a timeline ("internships starting June"). Calibrate.

**Estimated time.** 20 minutes.

---

## Problem 6 — The take-3 plan

**Problem statement.** Before Saturday's mini-project session, pre-write the three notes that you will apply to your take 3. Use Exercise 3's take-1-vs-take-2 comparison table as the source. Pick the three highest-leverage corrections — typically one timing fix, one filler-word fix, and one structural fix (an ask re-write, a hook re-write, or a solution-beat cut). The point is to arrive at Saturday with three pre-written notes, so the mini-project session is *recording* and *committing*, not *deciding*.

**Acceptance criteria.**

- File at `week-06-prep/homework-06.md`.
- The take-1 vs take-2 comparison table is re-pasted (or linked) at the top.
- Three pre-written notes for take 3, each labeled with which beat or behavior they target.
- Each note is a specific, named change (not "be better at the hook," but "cut line 2 of the hook from 12 words to 7").
- A 2-sentence note on which beat is closest to demo-able already (and therefore needs no note).
- Committed by Friday night.

**Hint.** The easiest notes to pre-write are timing fixes (cite a number from the comparison table) and ask re-writes (the last-sentence audit is mechanical). Structural fixes are the highest-leverage but the hardest to pre-write — leave them for the recording session if needed.

**Estimated time.** 20 minutes.

---

## Time budget recap

| Problem | Estimated time |
|--------:|---------------:|
| 1 | 15 min |
| 2 | 15 min |
| 3 | 25 min |
| 4 | 25 min |
| 5 | 20 min |
| 6 | 20 min |
| **Total** | **~2 hours** |

If your time is strict, drop Problems 3 and 5. Keep 1, 2, 4, and 6 — those are the muscles the recording itself relies on. Problem 4 (the four-watch practice) is the single most valuable problem of the week; do not skip it.

When you have finished, push your repo and finalize the [mini-project](./mini-project/README.md) — the 3-minute recorded demo of your Week-3 solo prototype.

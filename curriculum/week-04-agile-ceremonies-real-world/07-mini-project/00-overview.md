# Mini-Project — The One-Page Team Contract Template

> Draft a one-page team contract template — the artifact you bring to the next event and hand to a team of strangers in the first hour. Eight sections, one page, opinionated defaults, blank lines for event-specifics. The artifact you commit this week is reusable across every event from Week 10 onward.

This is the only Week 4 deliverable that matters. The two lectures established the ceremonies and the muscles inside them; the exercises rehearsed each muscle; the homework sharpened the corners; the optional challenge gave the muscles a 30-minute stress test. They all collapse into one artifact: a **one-page team contract template** that holds your team's defaults for ceremonies, pointing, refusing, and disagreeing.

**Estimated time:** ~2 hours of focused drafting on Saturday, plus ~0.5 hours of polish on Sunday before submission.

---

## What you will produce

A single markdown file at `TEAM-CONTRACT.md` in your `hackathon-template` repo (or in a new `c4-week-04-prep-<yourhandle>` repo). It is linked from your Hackathon Operating Document (Week 1 mini-project), from your `hackathon-template` README, and from any portfolio README you have.

The template is intentionally one printed page. If your draft runs to two pages, cut it. The constraint is the discipline — a team of strangers will not read a three-page contract at hour 0.

---

## Required sections

Every section below must appear, in the order shown, with the exact heading shown. Each section's length cap is given in lines. Total page target: **~50 lines including headings and blank lines**.

### 1. The team's prompt (3 lines)

A single sentence, filled in at hour 0 of each event:

```
PROMPT: <one user> can <one verb> to relieve <one pain>.
```

Same shape as the Week 3 solo prompt, but agreed by the team at hour 0. Leave the angle-brackets in the template — the team fills them in at the event.

### 2. The stand-up format (8 lines)

The 60-second, four-question format from Lecture 1 §2.1, plus the schedule and the rotating-timekeeper rule:

```
Format: 60 sec/teammate, four questions.
  1. Shipped (10s) | 2. Next (15s) | 3. Blocker (10s)
  4. Team cut (25s, asked once at end by timekeeper)
Schedule: hour 0, 6, 12, 18, 24, 30.
Timekeeper: rotates each stand-up. Cuts at the 60-sec dot.
Board update: written to STANDUPS.md after every stand-up.
```

Pre-fill all five lines. The event-specific blank is the schedule's absolute times (start time + 6h, +12h, etc.); the team fills that in at hour 0.

### 3. The cut decision protocol (5 lines)

Who can call a cut, when:

```
Any teammate can propose a cut at any stand-up or sidebar.
Cuts are voted on at the next stand-up's Q4 line.
Majority rules. Ties go to MUST staying shorter, not longer.
A cut requires naming what becomes WON'T (or SHOULD) and why.
The cut is logged in STANDUPS.md with the date and hour.
```

This section is the hardest to draft on Saturday because the lectures only sketched it. Use the defaults above; refine them after the next event.

### 4. The internal demo schedule (6 lines)

The 12h and 24h mid-event demos, plus the stranger-test protocol from Lecture 1 §3:

```
Internal demo 1: hour 12. 15 min cap. Click MUST on live URL.
  Decision: keep MUST as-is, or cut and replace.
Internal demo 2: hour 24. 15 min cap. Stranger test.
  One teammate plays "stranger" — clicks the URL with no setup.
  Other teammates listen silently. No coaching.
  Decision: name one feature cut from MUST.
```

Pre-fill all six lines.

### 5. The retro time and facilitator rotation (5 lines)

The 30-minute retro at hour 36, plus the rotating-facilitator rule:

```
Retro: hour 36 (after submission). 30 min cap.
Facilitator: rotates across events. Names: <list here>.
Format: 2 min restate | 8 min silent write | 10 min round-robin |
  8 min three-behaviors | 2 min commit to RETRO.md.
Output: 3 behaviors per teammate, written, committed.
```

Leave the facilitator names blank; the team fills them in.

### 6. The story-pointing scale (5 lines)

The 1-2-3-5-? scale from Lecture 2 §1.2 and the planning-poker format from §2:

```
Scale: 1, 2, 3, 5, ?
Round: 10 items in 10 min, ~50 sec/item.
Reveal: simultaneous. No anchoring.
Disagreement: highest and lowest argue 20 sec each. Re-vote once.
  Still split → "?" → split the card or spike it.
No 8, no 13. Cards bigger than 5 must split.
```

Pre-fill all six lines. The team can override the scale only by majority vote at hour 0.

### 7. The "saying no" script (8 lines)

The three-sentence script from Lecture 2 §3.2 plus the "yes-with-cut" rule from §3.5:

```
When a teammate proposes mid-event scope addition:
  1. ACKNOWLEDGE: "That's a good catch / a real concern."
  2. REFUSE WITH A REASON: "We agreed in the contract that <X>
     is in WON'T because <reason>."
  3. OFFER A CHEAPER ALTERNATIVE: "What if we <smaller> instead?"

Scope additions require an equal-points cut from MUST.
Disagreement on a "no" goes to the next stand-up's Q4.
```

Pre-fill all eight lines.

### 8. The conflict de-escalation step (6 lines)

One paragraph (3–6 lines) on what the team does when a disagreement does not resolve in the stand-up's Q4:

```
If a disagreement persists past two stand-ups, the team pauses
for a 5-minute structured sidebar (not during stand-up). Each
teammate names their position in one sentence + their best
counter-argument to their own position in one sentence. The
team votes. Ties go to the option that ships sooner.
If still unresolved: cut the feature in question.
```

Pre-fill all six lines. This is the section most likely to evolve event-to-event.

---

## The file tree

The mini-project is a single markdown file. No directories. No screenshots. No deploy. The simplicity is the artifact.

```
hackathon-template/   (or c4-week-04-prep-<yourhandle>/)
├── README.md
├── ... (other Week 2 / Week 3 files)
└── TEAM-CONTRACT.md  (this week's deliverable)
```

If you keep the file in a new prep repo, the file tree is identical except the parent directory name.

---

## The header block

The contract opens with a 4-line header block — metadata only, filled in at hour 0 of each event:

```markdown
# Team Contract — <Event Name>, <Date>

Team: <handle1>, <handle2>, <handle3>, <handle4>
Repo: <event repo URL>
Drafted at: hour 0:00. Reviewed at: hour 18, hour 36.
```

The "Reviewed at" line is the discipline. At hour 18 and hour 36, the team re-reads the contract. Most reviews find nothing to change; some find one line worth rewriting. The act of re-reading is the value.

---

## Rules

- **You will** keep the contract to one page (~50 lines including headings and whitespace). One page printed at 10pt is the constraint.
- **You will** pre-fill sections 2, 3, 4, 5, 6, 7, 8 with the C4 defaults from the lectures. Sections 1 and the header are blank in the template.
- **You will** write the contract in your *own voice* — not by copy-pasting the lecture examples verbatim. The voice rule still holds: team-room, blameless, scope-discipline-first.
- **You will** commit the file as `TEAM-CONTRACT.md` exactly (case matters in some git workflows).
- **You will not** add a section 9. The eight sections are the C4 default for a reason. If you want a section 9, propose it at the next retro and let the team decide.
- **You will not** use the contract to assign roles to teammates. The contract is about *how* the team works, not *who* does what. Role assignment happens in the opening stand-up.
- **You will not** make the contract pre-fill the angle-bracket blanks in section 1 (the prompt). The prompt is event-specific and is the team's first decision at hour 0.

---

## Acceptance criteria

- [ ] `TEAM-CONTRACT.md` exists in a committed public repo.
- [ ] The header block is present with the four metadata lines (with angle-bracket placeholders for the event-specific fields).
- [ ] All eight sections appear with the exact headings and in the order shown above.
- [ ] Section length caps are respected (total ~50 lines).
- [ ] Sections 2, 3, 4, 5, 6, 7, 8 are pre-filled with C4 defaults adapted to your voice.
- [ ] Section 1 (the prompt) leaves the angle brackets visible — to be filled at hour 0.
- [ ] The file fits on one printed page at 10pt (test: print preview shows one page).
- [ ] Linked from the README of your `hackathon-template` (one line: "Team contract template: `./TEAM-CONTRACT.md`").
- [ ] Linked from your Hackathon Operating Document (Week 1 mini-project).
- [ ] Voice is team-room, blameless, scope-discipline-first. No "rockstar" / "ninja" / "10x" / "crush it." No emojis.

---

## Rubric

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| All eight sections present, in order, with correct headings | 25% | Section 1 through 8, header on top, no extra sections |
| Sections 2–8 pre-filled with the C4 defaults adapted to your voice | 20% | Reads like *your* team's contract, not a verbatim lecture copy |
| One-page constraint honored | 15% | Print preview shows one page at 10pt; word count under ~500 |
| Section 1 left blank (angle brackets visible) for event-specific fill-in | 10% | The team's first decision at hour 0 is theirs, not yours |
| Voice (blameless, team-room, no banned words) | 15% | Reads like a sticky note from a tired but proud team-room |
| Linked from the right places (template README + Operating Document) | 10% | Two specific links exist; the contract is findable |
| Public, committed, license noted | 5% | Public repo, MIT or your default LICENSE |

---

## What this prepares you for

- **Week 5 — Scoping Discipline.** The contract's sections 6 (pointing scale) and 7 ("no" script) are inputs to the 36-hour scoping worksheet. The worksheet pre-writes the cuts; the contract pre-writes the refusals.
- **Week 6 — Pitch Craft.** The internal demo schedule (section 4) is what produces a clean judge demo at hour 33. Teams that skipped section 4 produce judge demos that surprise them.
- **Week 7 — Team-Mode Dry-Run, Day 1.** The contract is what you commit at hour 0 of the 6-hour mock event. The dry-run is the first time you watch the contract hold (or break) under real teammate pressure.
- **Week 8 — Team-Mode Dry-Run, Day 2.** A second dry-run with a *different* team. The contract is the same; the team's fill-ins (header, section 1, facilitator names) are different. The reusability of the template is what you verify here.
- **Week 10 — The Real Event.** The contract you commit at hour 0 of the real event is the same template you committed this week, with three lines filled in. The capstone rubric's "Team contract was used during the event" line (10% weight) grades on whether the contract was *actually consulted* during the event, not just committed.

---

## Submission

When done:

1. Commit `TEAM-CONTRACT.md` to your `hackathon-template` repo (or your Week 4 prep repo). Public.
2. Add one line to your `hackathon-template` README's "What is in here" section: "Team contract template: `./TEAM-CONTRACT.md`."
3. Add a link to the contract in your Hackathon Operating Document (Week 1 mini-project), under the section that lists your reusable artifacts.
4. Print it once. Read it aloud once. Note any line that does not survive being read aloud — re-write that line. Re-commit.
5. Post in the cohort channel: "Week 4 team contract is up at [URL]. One section I pre-filled in my own voice: <quote 1–2 lines>." Read one cohort-mate's contract that day and leave one specific comment on a *section*, not a generic compliment.

You are now ready for [Week 5 — Scoping Discipline](../../week-05/). In Week 5 you will turn the contract you just drafted into a *36-hour scoping worksheet* — the cut-list you bring to the event in addition to the contract. The contract holds the team; the worksheet holds the scope. Together, they are the team-mode preparation for the Week 7 dry-run.

---

*The win is shipping. You shipped one alone in Week 3. Now you have written the words that let a team ship together.*

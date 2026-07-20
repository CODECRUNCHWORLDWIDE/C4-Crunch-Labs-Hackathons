# Mini-Project — The 36-Hour Scoping Worksheet Template

> Draft a one-page 36-hour scoping worksheet template — the artifact you bring to the next event and fill in with the team in the first hour. Five sections, one page, opinionated defaults, blank lines for event-specifics. The artifact you commit this week is reusable across every event from Week 10 onward.

This is the only Week 5 deliverable that matters. The two lectures established MoSCoW under hackathon compression and the demo-ability bench; the exercises rehearsed the muscle on a fake prompt; the homework sharpened the corners; the optional challenge gave the muscles a 30-minute stress test on a real partner's idea. They all collapse into one artifact: a **one-page 36-hour scoping worksheet template** that holds your team's defaults for MoSCoW, cuts, and demo-ability validation.

**Estimated time:** ~2 hours of focused drafting on Saturday, plus ~0.5 hours of polish on Sunday before submission.

---

## What you will produce

A single markdown file at `SCOPING-WORKSHEET.md` in your `hackathon-template` repo (or in a new `c4-week-05-prep-<yourhandle>` repo). It is linked from your Hackathon Operating Document (Week 1 mini-project), from your `TEAM-CONTRACT.md` (Week 4 mini-project), from your `hackathon-template` README, and from any portfolio README you have.

The template is intentionally one printed page. If your draft runs to two pages, cut it. The constraint is the discipline — a team of strangers will not fill in a three-page worksheet in the first hour of an event.

---

## Required sections

Every section below must appear, in the order shown, with the exact heading shown. Each section's length cap is given in lines. Total page target: **~60 lines including headings and blank lines**.

### 1. The prompt sentence (3 lines)

A single sentence, filled in at hour 0:05 of each event by the team:

```
PROMPT: <one user> can <one verb> to relieve <one pain>.
```

Same shape as the Week 3 solo prompt and the Week 4 contract section 1. The worksheet version is *the bench against which every MoSCoW item is graded*. Every MUST candidate runs through the question: "does this serve the prompt sentence?" If not, it is not a MUST.

Leave the angle-brackets in the template. The team fills them in at the event.

### 2. The MoSCoW board (16 lines)

The four-column board, with the C4 default item-count caps. The board pattern matches BRAND.md's scoping chart:

```
SCOPE — 36-hour event

MUST (3 items max — ships or the demo dies):
  ✓ <item — verb the stranger performs in 60s on live URL>
  ✓ <item>
  ✓ <item>

SHOULD (2-3 items — ships if MUST is clean by hour 24):
  ▢ <item>
  ▢ <item>

COULD (1-2 items — almost never ships; plan for that):
  ▢ <item>

WON'T (4-6 items — does not ship; reason required):
  ✗ <item> — <one-sentence reason>
  ✗ <item> — <one-sentence reason>
  ✗ <item> — <one-sentence reason>
  ✗ <item> — <one-sentence reason>
```

Leave all item-lines blank in the template (the angle-brackets are the placeholder). The team fills them in during the 20-minute scoping pass at hour 0:10–0:30.

Pre-fill the column-headers, the caps, and the WON'T-row reason format. The structure is yours; the content is event-specific.

### 3. The points budget (4 lines)

The total points across MUST and SHOULD, using the 1-2-3-5 scale from Week 4 Lecture 2 §1.2:

```
MUST points total:   <sum>  (target: ≤9; cap: 12)
SHOULD points total: <sum>  (target: ≤6)
Total ship-target:   <sum>  (MUST + SHOULD; target: ≤15)
Re-budget at:        hour 12, hour 24 (cut down if behind)
```

Pre-fill the labels and targets. The team fills the sums after the planning-poker round at hour 0:35–0:45.

The targets (9, 6, 15) are C4 defaults for a team of 4 at 36 hours. Smaller teams use smaller targets; rougher prompts use lower MUST caps. Adjust at retro, not mid-event.

### 4. The cut-list (12 lines)

Three pre-written cut paragraphs, one each for hour 2, hour 12, hour 24, with named items from the board:

```
HOUR-2 CUT — "while we're in there"
  If anyone proposes a quick add (~1-2 points), it replaces
  <SHOULD item to be named at hour 0:30>. >2 points or off-verb
  → WON'T with reason.

HOUR-12 CUT — "we have time for one more"
  If MUST is not fully clickable on the live URL at hour 12,
  cut <MUST item most likely to fail> to SHOULD or WON'T. No
  promotion of SHOULD to MUST unless MUST is 5/5 demo-able.

HOUR-24 CUT — "we have to add X or the demo dies"
  At hour 24, the build window is closed. Any new feature
  request becomes a README paragraph or a static fake. Named
  default: <feature most likely to be requested → README line>.
```

Pre-fill the paragraphs' *structure*. The angle-bracket fills (the named MUST and named feature) are filled at hour 0:30 once the MoSCoW board is finalized.

### 5. The demo-ability checklist (12 lines)

The five-question test from Lecture 2 §3.1, run on every MUST item at hour 12 and hour 24:

```
DEMO-ABILITY TEST (run on each MUST item at hour 12 and 24)

Per MUST item, in 60 seconds:
  1. Live URL reachable?               (yes / no)
  2. Stranger opens with no setup?     (yes / no)
  3. Stranger performs MUST verb < 60s?(yes / no)
  4. Verb produces expected result on
     LIVE URL — not localhost?         (yes / no)
  5. Seeded data visible on live URL?  (yes / no)

Five yeses = demo-able. Any "no" = name the gap, do not debate.
Default-cut bias: at hour 24, failing MUST → SHOULD or WON'T.
```

Pre-fill all twelve lines. No event-specific blanks; the checklist is identical across events.

---

## The file tree

The mini-project is a single markdown file. No directories. No screenshots. No deploy. The simplicity is the artifact.

```
hackathon-template/   (or c4-week-05-prep-<yourhandle>/)
├── README.md
├── TEAM-CONTRACT.md      (from Week 4)
├── SCOPING-WORKSHEET.md  (this week's deliverable)
└── ... (other Week 2 / 3 / 4 files)
```

If you keep the file in a new prep repo, the file tree is identical except the parent directory name.

---

## The header block

The worksheet opens with a 5-line header block — metadata only, filled in at hour 0 of each event:

```markdown
# 36-Hour Scoping Worksheet — <Event Name>, <Date>

Team: <handle1>, <handle2>, <handle3>, <handle4>
Repo: <event repo URL>
Live URL: <deploy URL — confirmed at hour 0:30>
Scoped at: hour 0:10–0:30. Re-checked at: hour 12, hour 24.
```

The "Re-checked at" line is the discipline. At hour 12 and hour 24, the team re-reads the worksheet — specifically the cut-list and the demo-ability checklist — and runs the test. The act of re-reading is the value.

---

## Rules

- **You will** keep the worksheet to one page (~60 lines including headings and whitespace). One page printed at 10pt is the constraint.
- **You will** pre-fill the structure of all five sections (headers, caps, scripts, checklists). The *content* of sections 1, 2, 3, 4 is event-specific and stays blank until hour 0.
- **You will** write the worksheet in your *own voice* — not by copy-pasting the lecture examples verbatim. The voice rule still holds: team-room, blameless, scope-discipline-first.
- **You will** commit the file as `SCOPING-WORKSHEET.md` exactly (case matters in some git workflows).
- **You will not** add a section 6. The five sections are the C4 default for a reason. If you want a section 6, propose it at the next retro and let the team decide.
- **You will not** pre-fill section 2's MoSCoW board with example items. The board is event-specific. Leaving it blank is the discipline.
- **You will not** treat the worksheet as a replacement for the Week 4 team contract. The contract holds *how* the team works; the worksheet holds *what* the team ships. Both are required.

---

## Acceptance criteria

- [ ] `SCOPING-WORKSHEET.md` exists in a committed public repo.
- [ ] The header block is present with the five metadata lines (with angle-bracket placeholders for the event-specific fields).
- [ ] All five sections appear with the exact headings and in the order shown above.
- [ ] Section length caps are respected (total ~60 lines).
- [ ] Section 1 (prompt) leaves the angle brackets visible — to be filled at hour 0.
- [ ] Section 2 (MoSCoW board) has the column headers, caps, and structure pre-filled; item lines are blank placeholders.
- [ ] Section 3 (points budget) has the labels and targets pre-filled; sum lines are blank.
- [ ] Section 4 (cut-list) has the three paragraphs' structure pre-filled; named-item fills are placeholders.
- [ ] Section 5 (demo-ability checklist) is fully pre-filled — no event-specific blanks.
- [ ] The file fits on one printed page at 10pt (test: print preview shows one page).
- [ ] Linked from the README of your `hackathon-template` (one line: "36-hour scoping worksheet: `./SCOPING-WORKSHEET.md`").
- [ ] Linked from your `TEAM-CONTRACT.md` (one line in the contract: "Scope is held in `./SCOPING-WORKSHEET.md`.").
- [ ] Linked from your Hackathon Operating Document (Week 1 mini-project).
- [ ] Voice is team-room, blameless, scope-discipline-first. No "rockstar" / "ninja" / "10x" / "crush it." No emojis.

---

## Rubric

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| All five sections present, in order, with correct headings | 25% | Section 1 through 5, header on top, no extra sections |
| Sections pre-filled with C4 defaults adapted to your voice | 20% | Reads like *your* team's worksheet, not a verbatim lecture copy |
| One-page constraint honored | 15% | Print preview shows one page at 10pt; word count under ~600 |
| Section 1 left blank (angle brackets visible); section 5 fully pre-filled | 10% | The asymmetry is right: event-specific bits are placeholders, defaults are filled |
| Voice (blameless, team-room, no banned words) | 15% | Reads like a sticky note from a tired but proud team-room |
| Linked from the right places (template README + contract + Operating Document) | 10% | Three specific links exist; the worksheet is findable |
| Public, committed, license noted | 5% | Public repo, MIT or your default LICENSE |

---

## What this prepares you for

- **Week 6 — Pitch Craft.** The MUST list in your scoping worksheet is the spine of your three-minute demo. Week 6's demo script *is* the MUST list, rephrased for an audience. If your worksheet's MUST is clean, your pitch is half-written.
- **Week 7 — Team-Mode Dry-Run, Day 1.** The worksheet is what you commit at hour 0 of the 6-hour mock event. The dry-run is the first time you watch the worksheet hold (or break) under real teammate pressure. Pair with the Week 4 contract; the two together are the team-mode preparation.
- **Week 8 — Team-Mode Dry-Run, Day 2.** A second dry-run with a *different* team. The worksheet template is the same; section 1's prompt and section 2's items are different. The reusability of the template is what you verify here.
- **Week 9 — Event Recon.** The cut-list (section 4) gets sharpened with event-specific data — sponsor APIs that historically have rate limits, prizes whose rubrics push toward specific MUSTs, judge profiles. The recon week tunes the defaults.
- **Week 10 — The Real Event.** The worksheet you commit at hour 0 of the real event is the same template you committed this week, with sections 1–4 filled in during the first hour. The capstone rubric's "Scoping log shows deliberate cuts" line (15% weight) grades on whether the worksheet was *actually consulted* during the event — specifically, whether the cut-list paragraphs fired and produced named cuts.

---

## Submission

When done:

1. Commit `SCOPING-WORKSHEET.md` to your `hackathon-template` repo (or your Week 5 prep repo). Public.
2. Add one line to your `hackathon-template` README's "What is in here" section: "36-hour scoping worksheet: `./SCOPING-WORKSHEET.md`."
3. Add a link to the worksheet in your `TEAM-CONTRACT.md` (one line, near section 1 or section 3): "Scope is held in `./SCOPING-WORKSHEET.md`."
4. Add a link to the worksheet in your Hackathon Operating Document (Week 1 mini-project), under the section that lists your reusable artifacts.
5. Print it once. Read it aloud once with your contract open beside it. Note any line where the worksheet and the contract contradict each other — re-write the contradicting line. Re-commit.
6. Post in the cohort channel: "Week 5 scoping worksheet is up at [URL]. One section I pre-filled in my own voice: <quote 2–3 lines>." Read one cohort-mate's worksheet that day and leave one specific comment on a *section*, not a generic compliment.

You are now ready for [Week 6 — Pitch Craft](../../week-06/). In Week 6 you will turn the clean MUST list of your scoping worksheet into a *three-minute demo script* — the artifact that fits inside the demo strip from BRAND.md. The contract holds the team; the worksheet holds the scope; the pitch holds the audience. Together, they are the team-mode preparation for Week 7's dry-run.

---

*The win is shipping. You shipped one alone in Week 3. You wrote the contract that lets a team ship together in Week 4. Now you have the map that says which features ship — and which features your team agreed, in writing, before the event, would not.*

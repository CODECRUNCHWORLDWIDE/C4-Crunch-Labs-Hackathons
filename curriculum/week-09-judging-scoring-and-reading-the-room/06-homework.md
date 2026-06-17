# Week 9 — Homework

Six practice problems. The homework rehearses the lectures with new fake scenarios. Each problem has a deliverable; commit them all to a single file `WEEK-09-HOMEWORK.md` in your `week-09/` working folder.

The homework is *cumulative-style* — the problems compound. Problem 1 is the easiest; Problem 6 integrates several lectures. Aim for 5/6 problems complete by Sunday morning of Week 9.

| Problem | Skill | Time estimate |
|--------|-------|---------------|
| 1 | Rubric anchor recall | 15 min |
| 2 | Mindset cue classification | 20 min |
| 3 | Three pitch-opening retros | 30 min |
| 4 | Pitch-failure-mode diagnosis | 25 min |
| 5 | Bridge sentence drill | 20 min |
| 6 | Cross-skill scenario — the panel with mixed mindsets | 40 min |
| **Total** | | **~2.5h** |

---

## Problem 1 — Rubric anchor recall

For each of the five C4 rubric dimensions, write the 1-5 anchor description in your own words. Use the anchors from Lecture 1 §4.1 as the source; your wording will differ slightly from the lecture.

**Deliverable:**

```markdown
### Problem 1 — Rubric anchors

## Technical Complexity
1 — [description]
2 — [description]
3 — [description]
4 — [description]
5 — [description]

## Design and UX
[same; 5 anchors]

## Originality
[same]

## Polish
[same]

## Presentation
[same]
```

The exercise is *anchor fluency*. By Saturday's mock pitch, the team should be able to score a teammate's pitch on the spot without re-opening the lecture.

---

## Problem 2 — Mindset cue classification

For each of the following six cues observed in the first 30 seconds of a judging slot, classify the judge's mindset as **engineer**, **investor**, or **neutral/mixed**. Provide a one-sentence justification per cue.

```
Cue A: The judge picks up the clipboard as soon as the team mentions
        their tech stack at 0:08.
Cue B: The judge asks "who is the user, specifically?" before the
        demo starts.
Cue C: The judge looks at the screen, not the team, for the first
        45 seconds.
Cue D: The judge takes a phone call mid-pitch.
Cue E: The judge writes during the team's mention of "we surveyed 8
        FIU students."
Cue F: The judge nods slightly at the team's mention of "we used
        Postgres because of the JSON column type for the saved-trips
        feature."
```

**Deliverable:**

```markdown
### Problem 2 — Cue classification

| Cue | Mindset | Justification (1 sentence) |
|-----|---------|----------------------------|
| A | [engineer/investor/neutral] | [why] |
| B | ... | ... |
| C | ... | ... |
| D | ... | ... |
| E | ... | ... |
| F | ... | ... |
```

The exercise is *cue-reading fluency*. Most "mixed panels" have judges leaning one way; recognising which way within 30 seconds lets the team adjust the pitch's emphasis.

---

## Problem 3 — Three pitch-opening retros

Find three publicly-recorded hackathon final-round pitches on YouTube. Sources:

- TreeHacks, HackMIT, CalHacks, PennApps, HackTheNorth, MHacks finalist videos
- The Devpost gallery's "winner" project pages (some include the finals video)
- The cohort archive (if accessible)

If none of the above are available, use:
- The Week 6 solo demo videos from your own cohort (with permission).
- The Week 8 dry-run demo videos from your team and two peer teams.
- The three sample retros from Lecture 2 (if your archive has them).

For each pitch, watch the *first 30 seconds only*. Write one sentence per pitch on what the opening 30 seconds *did*:
- Did the pitch name the user/pain/verb?
- Did the pitch open with team bio?
- Did the pitch open with the tech stack?
- Did the pitch open with a story or a question?

**Deliverable:**

```markdown
### Problem 3 — Three pitch-opening retros

Pitch 1: [URL or source]
  Opening 30 seconds: [one sentence on what the opening did]

Pitch 2: [URL or source]
  Opening 30 seconds: [one sentence]

Pitch 3: [URL or source]
  Opening 30 seconds: [one sentence]

Pattern across the three: [one sentence on the shared pattern or
                          the divergence]
```

The exercise is *opening-recognition*. Watching three openings sharpens the eye for what the C4 30-second problem beat looks like in the wild.

---

## Problem 4 — Pitch-failure-mode diagnosis

```
Fake pitch transcript (excerpted middle 60 seconds):

  ...so, um, like, the way the build works is we have a frontend and
  a backend and we used React and Node and Express and PostgreSQL
  and Tailwind and Radix UI and we deployed on Vercel and...

  [Team Member 2 starts typing in a terminal]
  
  Member 2: hold on, let me run the seed script...
  Member 1: actually let me explain the user flow first...
  Member 2: ...npm run seed... wait, the seed is erroring...
  Member 1: ...so the user, who is a college student...
  Member 2: ...it says "ENOENT: no such file or directory"...
  
  [Judge's eye contact has been on the screen for 12 seconds with
   no demo visible]

  Member 1: ...you know, let me just show the screenshot of how it
  looks...

  [Member 1 shares a screenshot taken at hour 18]
```

Diagnose the pitch failure modes present in the excerpt. Reference Lecture 2 §6.

**Deliverable:**

```markdown
### Problem 4 — Pitch-failure-mode diagnosis

Failure mode 1: [name from Lecture 2 §6.X]
  Evidence in transcript: [specific quote or moment]
  Recovery move that should have been deployed: [from Lecture 2 §6.X]

Failure mode 2: [same fields]

Failure mode 3: [same fields]

Failure mode 4 (if present): [same fields]

The single highest-cost moment in the transcript: [identify the
moment that lost the most rubric points and name which dimension
took the hit]
```

The exercise is *post-mortem fluency*. Reading other teams' failure modes is the cheapest way to internalise the failure modes; by the time the team's own pitch surfaces one in the mock, the diagnosis is fast.

---

## Problem 5 — Bridge sentence drill

For each of the following hard questions, write a bridge sentence using the pattern from Lecture 3 §3.8. Each bridge sentence is 25-30 seconds (the format is `[acknowledge] — [bridge phrase] — [pivot]`).

```
Question A: "How does your build handle accessibility for blind users?"
            (Assume the team did not specifically build accessibility but
             did pay attention to alt-text and colour contrast.)

Question B: "What's your customer acquisition cost going to be?"
            (Assume the team has not modelled CAC at all, but did talk
             to 8 potential users informally.)

Question C: "How would this perform under 10 million concurrent users?"
            (Assume the team's stack is a stock React/Postgres/Vercel
             setup that would not naively scale to 10M but the team has
             thought about a CDN and a queue for the saved-trips writes.)

Question D: "Why didn't you use Rust instead of Node?"
            (Assume the team chose Node because the team knew it and the
             slot was a 24-hour event, not for any deep reason.)
```

**Deliverable:**

```markdown
### Problem 5 — Bridge sentence drill

Question A bridge:
"[Acknowledge] — [bridge phrase from Lecture 3 §3.8] — [pivot to
 the team's actual related answer]."

Question B bridge:
[same format]

Question C bridge:
[same format]

Question D bridge:
[same format]
```

The exercise is *bridge fluency*. The bridge muscle is the *most-reused* Q&A pattern; rehearsing four bridges this week is the floor.

---

## Problem 6 — Cross-skill scenario — the panel with mixed mindsets

A scenario integrating Lectures 1, 2, and 3:

```
Time: 3 PM on the judging Sunday.
Format: panel judging.
Panel: 4 judges.
  Judge 1: a senior software engineer at a Fortune-500 cloud company.
  Judge 2: a partner at a seed-stage venture firm.
  Judge 3: a university CS professor.
  Judge 4: a product manager from the event's title sponsor.

The team is MorningWalk (the fake build from SOLUTIONS.md). The
team's pitch ran clean: 30-90-45-15 arc respected; demo against the
live URL; tech beat named the API-key trade-off.

In the Q&A:
  Judge 2 (investor) asks: "Have you talked to any FIU students who
                            said they would pay for this?"
  
  Judge 1 (engineer) asks: "What does the request path look like
                            when the Google Maps API quota is
                            exhausted?"
  
  Judge 4 (PM) asks: "How does this fit into the broader 'campus
                       life' product space?"
  
  Judge 3 (professor) does not ask a question; she takes notes
  during the team's responses.
```

**Deliverable:**

Write three artifacts:

(a) The team's 30-second answer to Judge 2's investor question.

(b) The team's 30-second answer to Judge 1's engineer question. Note: the team has *not* prepared this specific edge case (quota exhaustion). Use the bridge sentence pattern from Lecture 3 §3.8.

(c) The team's 30-second answer to Judge 4's PM question. Note: the team has *not* thought about the broader product space. Use the "I don't know" pattern from Lecture 3 §3.9 if appropriate.

After the three answers, write a one-paragraph reflection: *which of the three answers do you expect Judge 3 (the professor, who is taking notes silently) to find most credible, and why?*

```markdown
### Problem 6 — Mixed-mindset panel Q&A

(a) Judge 2 (investor) — answer:
[30 seconds; the user-research-and-payment honest answer]

(b) Judge 1 (engineer) — bridge answer:
[acknowledge the quota-exhaustion specific] — [bridge phrase] — 
[pivot to the team's actual related thinking: the proxy alternative
they considered, or the caching layer on the v0.2 issue list]

(c) Judge 4 (PM) — "I don't know" answer (or bridge):
[choose I-don't-know or bridge; justify the choice in the answer's
structure]

Reflection on Judge 3 (the silent professor):
[one paragraph; which answer is most credible to her and why]
```

The exercise is *mixed-panel integration*. Problem 6 touches the rubric (the answer to each judge is anchored to the dimension that judge scores), the bridge pattern, the "I don't know" pattern, and the *reading-the-room* skill of noticing a silent judge whose notes are scoring evidence.

---

## Rubric

Each problem is graded on three axes: completeness (deliverable filled), accuracy (matches the lecture taxonomy), and concision (no padding).

| Score | Meaning |
|------|---------|
| 6/6  | Strong. Every problem is concise, accurate, complete. Move to Week 10. |
| 5/6  | Strong. One problem is partial. Identify which one; the muscle for that problem is the weakest. |
| 4/6  | Acceptable. Two problems are partial. Re-read the relevant lectures; iterate. |
| <4/6 | The homework is not warming the muscles. Re-read all three lectures; redo from problem 1. |

## Acceptance checklist

- [ ] All six problems have a deliverable section in `WEEK-09-HOMEWORK.md`.
- [ ] Problem 1's five-dimension anchor table is filled with 5 anchors × 5 dimensions = 25 anchor descriptions.
- [ ] Problem 2's classification table has 6 rows.
- [ ] Problem 3's three retros each have a one-sentence opening note plus a pattern note.
- [ ] Problem 4 names at least three failure modes from Lecture 2 §6 and the recovery move per mode.
- [ ] Problem 5's four bridge sentences each use one of the four named bridge phrases.
- [ ] Problem 6's three Q&A answers each follow the structure (direct/evidence/close or acknowledge/bridge/pivot or I-don't-know) and the reflection paragraph is present.
- [ ] The full file is committed to your `week-09/` working folder.

## What to do with the deliverable

The homework is *practice for the mock pitch and mock Q&A*. The fluency built here — recalling the rubric anchors in 5 seconds, classifying a judge's mindset in 30 seconds, deploying a bridge in <3 seconds — is the difference between a Saturday mock pitch that feels practiced and one that feels like a first take.

Most cohort learners under-do Week 9's homework because the Week 7-8 dry-run weekend was heavy. The mock pitch surfaces the under-doing on Saturday afternoon when the team's bridge sentences come out garbled and the Q&A archetypes feel unfamiliar. Do the six problems; come into the weekend with the muscles warm.

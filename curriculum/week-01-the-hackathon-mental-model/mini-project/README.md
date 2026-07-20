# Mini-Project — Your Hackathon Operating Document

> Build a single, durable document that captures who you are at a hackathon: your strengths, your default role, your stack, your sleep pattern, your ceremonies, your dealbreakers, your post-event ritual. You will reference this document at every hackathon you attend, from your first event in Week 10 to events years from now.

This is the only Week 1 deliverable that is meant to outlive the week. The personal brief from Exercise 1, the team contract from Exercise 3, the project ratings from Exercise 2 — they all collapse into the **Hackathon Operating Document** (HOD). One file. One source of truth.

**Estimated time:** ~2.5 hours (split across Thursday, Saturday, Sunday in the suggested schedule).

---

## What you will produce

A single Markdown file, `HACKATHON-OPERATING-DOC.md`, committed to your Week 1 repo *and* copied into your personal portfolio repo (you will keep updating it from there).

The file is one printed page if printed at a sensible font, roughly 600–900 words. It is *not* an essay. It is a document of decisions, with short paragraphs and bulleted lists.

---

## Required sections

Every section below must appear, in this order, with the heading text shown.

### 1. Who I am at a hackathon

A pulled-forward version of Exercise 1's personal brief. Two-to-three short paragraphs covering:

- What you are genuinely good at (specific, not generic).
- What you avoid if you can.
- One sentence on how you behave under sleep deprivation.

### 2. My default role

One paragraph. Pick one of the four canonical roles (PM/scope-keeper, full-stack builder, designer, pitch lead) and explain the reasoning in two sentences. Then list up to two roles you can cover in a pinch.

### 3. My stack defaults

A small table of your defaults at hackathon hour zero, so you do not have to re-debate them on the day:

| Layer | My default | Acceptable substitute | I will not use |
|-------|------------|-----------------------|----------------|
| Frontend | ... | ... | ... |
| Backend | ... | ... | ... |
| DB | ... | ... | ... |
| Deploy | ... | ... | ... |
| Auth | ... | ... | ... |

The "I will not use" column is essential. You are picking battles you will *not* fight at hour 18.

### 4. My ceremonies

The minimum ceremonies you commit to running or asking the team to run. Copy this list from the team contract template, but tailor it:

- Hour 0 — kickoff (MoSCoW chart, repo, blank deploy).
- Hour 12 — 12-hour stand-up.
- Hour 24 — mid-event retro.
- Hour 33 — final-3-hour freeze.
- Hour T-1:00 — submission.

If you commit to running more (a quick stand-up every six hours, a daily retro for week-long events) list them here.

### 5. My MoSCoW posture

Two or three sentences on how you handle the MoSCoW chart in practice. Sample shapes:

- "I draw it on the wall in hour zero. I do not start writing code until every teammate has read it aloud."
- "I am the PM by default. I expect to be the one calling cuts at hour 12, and I expect teammates to push back if my cuts are wrong."
- "I am a builder by default. I commit to *trusting* the PM's cut, even when it is mine that gets cut."

### 6. My demo and pitch defaults

Two paragraphs. The first: when do I start writing the pitch? (Default: hour 18.) The second: how do I record? (Tool, fallback if the first fails, who else needs to review.)

### 7. My sleep plan

One paragraph. The honest version. "I push through with two 30-minute naps." "I require a real two-hour sleep at hour 20." "I cannot pull all-nighters and I plan tasks around that fact."

This is the most often skipped section. Do not skip it. Sleep blow-ups cause more team failures than scope creep.

### 8. My dealbreakers

A bulleted list of three to five hard nos. The shape that works:

- "I will not commit secrets to a repo."
- "I will not skip the deploy in hour one."
- "I will not work with someone who is rude to teammates."
- "I will not be the pitch lead unless absolutely no one else can be."

Dealbreakers are how you stay yourself under fatigue. Write them when fresh; honor them when tired.

### 9. My post-event ritual

A short, repeatable list of what you do in the 72 hours after every event:

1. Push the final repo public (if it is not already).
2. Write the post-mortem within 24 hours.
3. Update this HOD with anything I learned.
4. Credit teammates by name (with permission).
5. Watch the demo recording one more time, with kind eyes.

### 10. Version log

A small table at the bottom:

| Date | What changed | Trigger event |
|------|--------------|---------------|
| (today) | First draft | C4 Week 1 |
| ... | ... | ... |

Every time you attend an event, you update at least one section of this document, and log it here. This is how the HOD stays alive instead of becoming a fossil.

---

## Rules

- **You may** copy text from your Exercise 1 personal brief and your Exercise 3 team contract. They were always going to feed in here.
- **You may** keep this document in your personal portfolio repo rather than a course-specific one — but you must commit a copy under Week 1 for grading.
- **You may** evolve the format over time. The headings above are the starter; later events may add a section (e.g., "How I handle remote teammates") or remove one.
- **You will not** make this a marketing document. No "I am a 10x engineer." Plain language only.

---

## Acceptance criteria

- [ ] File exists at `mini-project/HACKATHON-OPERATING-DOC.md` in your Week 1 repo.
- [ ] All ten sections present, in the order listed, with the exact heading text.
- [ ] Section 3 (stack table) is filled in for every row, including the "I will not use" column.
- [ ] Section 7 (sleep plan) is filled in honestly, not skipped.
- [ ] Section 8 (dealbreakers) has at least three items.
- [ ] Total length 600–900 words.
- [ ] No use of "rockstar," "ninja," "10x," or "crush it."
- [ ] Voice is team-room, blameless, scope-discipline-first.
- [ ] A copy is also committed in your personal portfolio repo (if you have one).
- [ ] Committed.

---

## Rubric

| Criterion | Weight | What "great" looks like |
|-----------|-------:|-------------------------|
| Specificity | 25% | Every section names actual choices, not platitudes |
| Honesty | 20% | Sleep plan, dealbreakers, and "what I avoid" feel true |
| Defaults are pre-decided | 20% | A teammate could read Section 3 and understand your stack opinion in 30 seconds |
| Ceremonies match doctrine | 15% | The 12-hour stand-up, mid-event retro, and final freeze are all listed |
| Voice | 10% | Reads like the C4 brand — team-room, no fluff |
| Version log present | 10% | Section 10 exists with the first entry filled in |

---

## What this prepares you for

- **Weeks 2 and 3** — you will set up the stack from Section 3, and run a solo prototype that obeys your Section 5 MoSCoW posture.
- **Weeks 4–6** — you will run Agile ceremonies and a pitch from your Section 4 and Section 6 defaults.
- **Weeks 7–9** — your mock-hackathon teams will look at your HOD when you join. You will look at theirs.
- **Week 10** — the real event. You will print this document, fold it into your laptop bag, and reference Section 7 when you decide whether to nap at hour 20.

The HOD is the longest-lived artifact in the entire C4 course. The repo from Week 10 will be public for years; the HOD will be edited for years. Treat it accordingly.

---

## Submission

When done:

1. Push your Week 1 repo to GitHub with a public URL.
2. Copy the HOD to your portfolio repo (or create a portfolio repo if you do not have one).
3. In the Code Crunch club channel (or wherever the cohort gathers), post: "Week 1 HOD is up at [URL]." Read one other person's HOD that day and leave one specific comment.

You are now ready for [Week 2 — Rapid-Prototyping Toolkit Setup](../../week-02-rapid-prototyping-toolkit-setup/). In Week 2 you will turn your Section 3 stack table into a one-command project scaffold.

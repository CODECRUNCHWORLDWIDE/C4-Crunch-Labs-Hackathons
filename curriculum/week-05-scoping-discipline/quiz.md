# Week 5 — Quiz

Ten multiple-choice questions. Take it with your lecture notes closed. Aim for 9/10 before moving to Week 6. Answer key at the bottom — do not peek.

---

**Q1.** In the C4 MoSCoW for a 36-hour event, the **MUST** column has a hard item-count cap of:

- A) 5 items.
- B) 3 items.
- C) 7 items.
- D) No cap; MUST holds whatever the team commits to.

---

**Q2.** Which MoSCoW column does Lecture 1 §1.3 name as the **most-important** column?

- A) MUST — it is what ships.
- B) SHOULD — it is the most-debated.
- C) COULD — it is the team's stretch goal.
- D) WON'T — it holds the refusal and protects the MUST.

---

**Q3.** The 20-minute MoSCoW pass at hour 0 follows five named steps. Which is the *last* step?

- A) Brainstorm candidate items on stickies.
- B) Cluster duplicates.
- C) Commit the four-column board to the worksheet (or photograph the wall).
- D) Force the MUST cap to 3.

---

**Q4.** A teammate at hour 12 says, "It works on my laptop." Lecture 2 §1.2 says this is:

- A) Acceptable — localhost validation is sufficient for internal demos.
- B) Shortcut 1; the live URL is the only bench. Restart the demo on the deploy URL.
- C) The right answer if the deploy URL is slow.
- D) Acceptable if a screenshare backs it up.

---

**Q5.** The five-question demo-ability test grades a MUST item in 60 seconds. Which is **not** one of the five questions?

- A) Is the live URL reachable right now?
- B) Can a stranger perform the MUST verb in 60 seconds?
- C) Is the codebase under 10,000 lines?
- D) Is the seeded data visible on the live URL?

---

**Q6.** A pre-written cut-list paragraph for hour 24 says, "If we are panicking at hour 24, the leaderboard becomes a static image in the README — not a feature." This is an example of:

- A) A vague intention; needs to be more abstract.
- B) The named-cut rule — a specific item with a specific cut, written before the event.
- C) The wrong cut; hour 24 cuts should always be feature deletions, not README paragraphs.
- D) A failure of scoping discipline.

---

**Q7.** Lecture 2 §5.3 names the **polishing trap**. The test for the polishing trap is:

- A) Is the team polishing a demo-able MUST while a SHOULD goes unbuilt?
- B) Is the team over-testing the deploy URL?
- C) Is the team committing too many small commits?
- D) Is the team taking too many stand-up breaks?

---

**Q8.** The hour-12 decision tree (Lecture 2 §4.1) has a default bias when a MUST is failing 5/5. The default is:

- A) Extend — commit to fixing the MUST in the next 4 hours.
- B) Polish — pretty the MUST so the failure is less visible.
- C) Cut — move the failing MUST to SHOULD or WON'T, ship the rest.
- D) Pivot the whole project to a different prompt.

---

**Q9.** The pre-event walk-through (Lecture 2 §2) is run:

- A) At hour 24 of the real event.
- B) On the `hackathon-template` repo *this week*, before any real event, to catch deploy and seed gaps.
- C) Only once per quarter.
- D) On the judges' laptops at hour 33.

---

**Q10.** Which is the **most accurate** statement about the 36-hour scoping worksheet (this week's mini-project)?

- A) It replaces the team contract from Week 4.
- B) It is filled in at hour 12 of the event, once teammates have built enough to know what to cut.
- C) It is a one-page, five-section artifact (prompt, MoSCoW board, points budget, cut-list, demo-ability checklist) — pre-filled before the event with C4 defaults, filled in event-specific sections at hour 0.
- D) It is identical to a corporate Agile backlog.

---

## Answer key

<details>
<summary>Click to reveal answers</summary>

1. **B** — MUST is capped at 3 items in a 36-hour event. A MUST list with 5+ items is a MUST list that has not been cut yet. (Lecture 1 §1.2)
2. **D** — WON'T is the most-important column. It holds the refusal, protects the MUST, and compounds across events. (Lecture 1 §1.3)
3. **C** — Commit is the fifth step (brainstorm → cluster → sort → cut → commit). The verbal-only MoSCoW failure mode is the failure to commit. (Lecture 1 §1.4 and §4.4)
4. **B** — Shortcut 1: "It works on localhost." The live URL is the only bench. Restart the demo on the deploy URL. (Lecture 2 §1.2)
5. **C** — Codebase line count is not a demo-ability question. The five are: URL reachable / no setup / stranger verb / prod result / seeded data visible. (Lecture 2 §3.1)
6. **B** — The named-cut rule. A pre-written cut with a specific item and a specific destination ("static image in the README") is the gold pattern. (Lecture 1 §2.3 and Exercise 3)
7. **A** — Polishing trap test: is the team polishing a demo-able MUST while a SHOULD goes unbuilt? The five-yes ceiling is the cure. (Lecture 2 §3.3 and §5.3)
8. **C** — Default-cut bias at hour 12. Extension is a trap; cut, ship the rest, re-add later only if there is real headroom. (Lecture 2 §4.1)
9. **B** — On the `hackathon-template` repo *this week*, before any real event. The walk-through catches gaps before they kill the next event's demo. (Lecture 2 §2.1)
10. **C** — One-page, five sections, pre-filled before the event with C4 defaults; event-specific sections filled at hour 0. The worksheet is the artifact that holds the scope. (Lecture 1 §9.1, Lecture 2 §9.1, and the mini-project README)

</details>

---

If you scored under 7, re-read the lecture sections referenced in the answers. If you scored 9 or 10, you are ready for the [homework](./homework.md).

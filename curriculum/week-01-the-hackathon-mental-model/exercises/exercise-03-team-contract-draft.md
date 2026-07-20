# Exercise 3 — Team Contract Draft

**Goal:** Adapt the C4 team-contract template into a real contract you will bring to your next event. By Friday you should have a contract you would actually sign with a team of strangers.

**Estimated time:** 45 minutes.

---

## Why this exercise exists

Most hackathon teams form in the first hour of the event. They never write down how they will work together. Then at hour 18 someone is frustrated, at hour 24 someone disappears for sleep without telling anyone, and at hour 33 there is no agreement on who delivers the pitch.

A 10-minute conversation in hour one, anchored by a one-page contract, prevents most of this. The contract is not legal. It is a *shared promise*, in writing, so nobody has to invent norms at hour 30 when they are exhausted.

---

## What to produce

Create a file `exercises/exercise-03-team-contract-draft.md` in your Week 1 repo using the template below. Fill in every section. Where the template says **[FILL IN]**, replace it with your actual choice.

```markdown
# Team Contract — <event name or "[event TBD]">

## 1. Roles
- **PM / scope-keeper:** [FILL IN: name, or "to be picked hour 0"]
- **Builder(s):** [FILL IN]
- **Designer:** [FILL IN]
- **Pitch lead:** [FILL IN]

A role can be shared, but every role must have a *primary* person responsible for it.

## 2. Stack
- **Frontend:** [FILL IN]
- **Backend:** [FILL IN]
- **DB:** [FILL IN]
- **Deploy target:** [FILL IN] — live with a blank page by **hour 2**.

## 3. The MoSCoW chart
- We draw it at hour zero. It lives on a shared Excalidraw or whiteboard.
- MUSTs cap at **three**.
- We re-read it at every stand-up.
- The PM has the gavel on cuts.

## 4. Ceremonies
- **Hour 0:** Kickoff (60 min). Draw the MoSCoW chart, set up the repo, deploy a blank page.
- **Hour 6:** Quick stand-up (10 min). Status check.
- **Hour 12:** 12-hour stand-up (15 min). Apply the 12-hour rule. Cut.
- **Hour 18:** Quick stand-up (10 min). Re-check MoSCoW.
- **Hour 24:** Mid-event retro (30 min). Blameless. Re-plan.
- **Hour 30:** Quick stand-up (10 min). Confirm freeze plan.
- **Hour 33:** Final freeze. Build stops. Rehearsal and recording only.

## 5. Communication
- **Primary channel:** [FILL IN: Discord / Slack / WhatsApp group]
- **Decisions:** discussed verbally, then a one-line summary is posted in the channel by the PM.
- **Silent disagreement is not allowed.** If you think something is wrong, you say so.

## 6. Sleep
- Each teammate names their own sleep plan in hour 0: nap-at-hour-20, push-through, etc.
- Whoever naps tells the team when they will be back. No silent disappearances.
- The PM does not police sleep, but the PM does adjust scope if someone is unavailable.

## 7. The deploy URL
- A deploy URL is live by **hour 2**. Even if it is a blank page.
- All feature work targets the deploy URL, not localhost-only.
- The deploy URL is in the Devpost submission and in the team channel pinned message.

## 8. Demo and pitch
- Pitch lead starts writing the script at **hour 18**.
- The demo recording is captured by **hour T-1:30** (90 minutes before deadline).
- We rehearse the pitch live **three times** before recording.

## 9. Submission
- We use Devpost (or the event's submission platform).
- We submit by **hour T-1:00** (one hour before deadline). The last hour is for fixing the broken thing the submission form revealed.

## 10. Conflict
- We use blameless language. "The sprint board missed the rate limit," not "Pat broke the rate limit."
- A teammate can call a **two-minute timeout** at any point. No questions, no debate. We reconvene.
- If we cannot resolve a conflict in two timeouts, we defer to the PM.

## 11. After the event
- We will write a blameless team post-mortem within **72 hours**.
- We will credit each teammate by name (with permission) in the post-mortem and any public write-up.
- The repo will be public.

## 12. Sign-off
- [ ] [name] — agreed
- [ ] [name] — agreed
- [ ] [name] — agreed
- [ ] [name] — agreed

(Each teammate physically ticks the box at hour 0.)
```

---

## How to actually adapt this

This is the *template*. Your contract should:

1. **Be shorter where you have an opinion.** If you know your stack is React + FastAPI + Supabase + Vercel, write that, not a menu.
2. **Be longer where you have a concern.** If you have a teammate who is famous for vanishing at hour 22, add a clause: "if anyone is unreachable for more than 90 minutes the team can re-plan their assigned tasks without them."
3. **Be readable in three minutes.** A team that cannot read the contract in the kickoff hour will ignore it. One page max.
4. **Use the C4 voice.** Blameless, scope-discipline-first, no "rockstar." If you find yourself writing "we will crush this hackathon," delete that line.

---

## Acceptance criteria

- [ ] File exists at `exercises/exercise-03-team-contract-draft.md`.
- [ ] Every **[FILL IN]** has been replaced with a real choice, or a documented "to be decided at hour 0."
- [ ] The contract fits on one printed page (under 600 words).
- [ ] Section 4 (Ceremonies) lists at least the hour-0, hour-12, hour-24, and final-freeze ceremonies.
- [ ] Section 11 (After the event) commits to a post-mortem within 72 hours.
- [ ] The contract uses blameless language (no "fault," "blame," "rockstar," "ninja").
- [ ] Committed.

---

## Hints

- **Pick the event before you fill in the contract.** Even if you do not know your teammates yet, the event format (24h vs 36h vs 48h) changes the ceremonies section.
- **If you have a team already, bring this to a shared call.** Edit it together. The act of editing it together *is* the team-formation conversation.
- **If you do not have a team yet, leave names blank** — `[FILL IN]` — and the contract is ready to print and circulate at the event.

---

## What's next

This contract is the second-most-referenced artifact in your event prep (after the Hackathon Operating Document, the Week 1 mini-project). Keep it in your portfolio repo; you will reuse it for years.

If you have time, move on to the optional [Challenge 1 — 12-hour solo build](../challenges/challenge-01-12-hour-solo-build.md). Otherwise, head to the [mini-project](../mini-project/README.md).

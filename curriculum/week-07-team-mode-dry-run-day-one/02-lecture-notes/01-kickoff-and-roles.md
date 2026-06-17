# Lecture 1 — Kickoff and Roles

> **Duration:** ~1.5 hours of reading.
> **Outcome:** You can run a 60-minute hackathon kickoff meeting from a written agenda. You can assign the three core hackathon roles — Builder Lead, Demo Lead, Comms Lead — to a 3- or 4-person team in under 10 minutes using a fit-grid. You can defend why the kickoff is six 10-minute segments, not one open 60-minute discussion. You can recognize the three most common kickoff failures — the introduction loop, the unclaimed role, the un-named channel — and the one-sentence fix for each.

If you only remember one sentence from this lecture, remember this:

> **The kickoff is six 10-minute segments, three named roles, one written agenda, and one timestamp that says "we start coding now." Everything else is decoration. A team that runs the kickoff in 60 minutes ships at hour 24; a team that runs it in 90 minutes ships at hour 32 and blames the prompt.**

Week 6 taught you the script — *how* the team's three MUST items are walked through. Week 7 teaches you the kickoff — *who* runs the team, *how* the meeting that starts the team is timed, and *which* role catches the four day-1 conflicts before they spread to hour 12. The script is the delivery; the kickoff is the *opening*. A team with a beautiful script and a chaotic kickoff loses hour 4 to a side-channel argument about who should have done what; a team with a tight kickoff has hour 4 free to ship.

---

## 1. Why the kickoff is a separate skill

The first reaction beginners have to "your kickoff is a 60-minute structured meeting" is: *that is overhead.* I want to start coding. We have 24 hours and you want to spend the first one in a meeting.

That reaction is wrong on every count. Here is the steel-man:

> **C4 voice:** the kickoff is not a meeting *about* the build; the kickoff is the *commit point* of the build. A team that has not picked a prompt, picked a role, picked a channel, and read the MUST list aloud has not yet started the build. They have started typing. Typing without a kickoff is faster than not typing, but slower than typing after a kickoff. The kickoff is the steepest part of the curve.

### 1.1 What the kickoff actually does

Five short sentences, one per outcome:

- **The kickoff converts a group into a team.** A group is N people who showed up. A team is N people with N-1 named handoffs between them. The kickoff names the handoffs.
- **The kickoff converts a prompt into a worksheet.** The prompt is "build something with AI in 24 hours." The worksheet is "freshmen can post a late-night question to get a peer reply within 5 minutes." The kickoff is the conversion.
- **The kickoff converts an empty repo into a shared workspace.** The repo at hour 0 has one README. By the end of the kickoff, the repo has a `TEAM-CONTRACT.md`, a `SCOPING-WORKSHEET.md`, a pinned `DAY-1-LOG.md`, and three named committers.
- **The kickoff converts a chat channel into a comms norm.** Before the kickoff, the team has a chat. After the kickoff, the team has a *pinned message* in the chat that says "decisions in #channel, banter in DMs, stand-ups at hours 4 / 12 / 22."
- **The kickoff converts an undefined success criterion into a named demo verb.** The hook from Week 6 is half-written by the end of the kickoff. The team knows the user, the pain, and the verb. The script is a writeable artifact by hour 2; without the kickoff, it is not.

If the kickoff does not produce any of these five outputs, the kickoff failed. If it produces all five, the team is 60 minutes in and 23 hours of build is ahead with the highest-ROI hour of the entire event in the bank.

### 1.2 The six 10-minute segments

C4 uses a six-segment kickoff. Each segment has a named output. The clock is the discipline.

```
┌────────────────────────────────────────────────────────────┐
│  THE 60-MINUTE KICKOFF — 6 SEGMENTS                        │
│                                                            │
│  [ 0:00 — 0:10 ] Introductions and intent                  │
│  [ 0:10 — 0:20 ] Prompt reading and reflection             │
│  [ 0:20 — 0:30 ] Role assignment (Builder, Demo, Comms)    │
│  [ 0:30 — 0:40 ] Scope pass one (worksheet draft)          │
│  [ 0:40 — 0:50 ] Comms-channel setup and pinning           │
│  [ 0:50 — 1:00 ] "We start coding at" handoff              │
└────────────────────────────────────────────────────────────┘
```

Six segments. Ten minutes each. The clock runs whether or not the segment finishes. If a segment over-runs, the time comes out of the *next* segment, not from outside the 60-minute window. The 60-minute cap is the bench; segments are the bands.

### 1.3 The audience's energy budget during the kickoff

A hidden curve runs underneath the six segments: the team's energy. It starts at 100% in the first minute, drops to about 70% by the end of the introductions if introductions ran long, climbs back to 90% during prompt reading if the prompt is interesting, dips to 60% during role assignment if the roles are contested, recovers to 80% during the scope pass if the worksheet template is open on screen, and finishes at 95% on the "we start coding" handoff if the timestamp is named.

> **C4 voice:** the kickoff is not "60 minutes split into six segments." It is "six energy boundaries where the team's commitment compounds or evaporates." Plan the boundary, not the segment.

Three implications:

- **The 0:10 boundary is where most kickoffs lose the room.** Introductions over-run. Pat tells a 4-minute story about a previous hackathon. By 0:14 the team has decided this kickoff is going to run long. The first segment is the most-cuttable; cap it hard.
- **The 0:30 boundary is where the team is decided.** Role assignment is done or it is not. If it is not done at 0:30, the rest of the kickoff happens with three people who think they are the Builder Lead.
- **The 0:50 boundary is the last chance to set the comms norm.** Most kickoffs close with "okay, let's get coding." That is not a handoff; that is an exit. The handoff names the channel pin, the next stand-up timestamp, and the hour-4 check.

---

## 2. Segment 1 — Introductions and intent (0:00 — 0:10)

Introductions are the segment beginners get most wrong. They treat it as a get-to-know-you ice-breaker. It is not. It is the *intent surface* — what each teammate is here to do, in two sentences.

### 2.1 The two-sentence introduction

Each teammate says two sentences:

```
Sentence 1: who I am and what I bring.
            "I'm Pat. I'm strongest at front-end React; I've shipped
             one Week-3 prototype with a deploy URL."
Sentence 2: what I want to get out of the dry-run.
            "I want to practice a 24-hour timeline with handoffs;
             I'm okay being Builder or Demo, less okay on Comms."
```

Two sentences. Ninety seconds per teammate. A four-person team finishes introductions in 6 minutes; a three-person team finishes in 4.5. Keep the remainder for the team-name decision (one minute) and the prompt-reading handoff (one minute).

### 2.2 The "no war stories" rule

Three things the intro does *not* contain:

- **A previous-hackathon war story.** "At HackMIT last year we built a..." cut. Save it for the post-dry-run debrief. The war story is decoration; the intent is the data.
- **A list of every framework you know.** "I work in React, Vue, Svelte, Next, Remix, Astro, Solid, and I'm learning Qwik." cut. Name the *one* tool you are strongest at and the *one* tool you are willing to learn this week.
- **A modesty disclaimer.** "I'm not very good at..." cut. The team-fit grid (§4) will surface skill gaps with less self-deprecation; the intro is intent, not capability inventory.

> **C4 voice:** the intro is *intent*, not *resume*. The resume is the GitHub profile, the LinkedIn, the past project. The intent is what this teammate *wants from the next 24 hours*. The intent is what a Builder Lead needs to decide who gets which MUST.

### 2.3 The team-name decision

The last minute of segment 1 is the team-name decision. It is *deliberately fast* — a team that spends 20 minutes on a name has 20 minutes less to build. Three rules:

- **Default to a placeholder.** "Team Crunch-7-A" is a placeholder. It works. The real name can come at hour 12 if the team has the energy.
- **First suggestion that nobody hates wins.** Not "first suggestion everyone loves" — that bar is too high. Nobody-hates is the threshold.
- **The name does not need to be clever.** Clever is fine; not-clever is also fine. The judges remember the demo, not the name.

The name goes in the repo README, in the channel name, and at the top of `DAY-1-LOG.md`. It is the team's stable identifier for the next 24 hours.

---

## 3. Segment 2 — Prompt reading and reflection (0:10 — 0:20)

The prompt reading is the segment beginners most often *skip*. They read the prompt silently, in their own browser tab, while the meeting drifts. That is not the prompt reading. The prompt reading is a *team event*.

### 3.1 The shared-screen rule

One teammate shares their screen. The prompt is open in a browser, in a doc, or in a Markdown file. Every teammate is looking at the same words. The Builder Lead-elect reads the prompt *aloud* to the team. Three minutes; the prompt is rarely longer than 400 words.

> **C4 voice:** silent reading is half-reading. The team that hears the prompt aloud has a 10x higher chance of agreeing on what it says than the team that read it in parallel. Three minutes of reading aloud saves an hour of re-arguing at hour 4.

### 3.2 The two-minute reflection round

After the read, two minutes of silent reflection. Each teammate writes (in the team chat, in DMs to themselves, or on paper) one sentence: "the user I think the prompt is for is..." Two minutes; no discussion yet.

Then a 5-minute round-robin: each teammate reads their sentence aloud. The Builder Lead-elect captures the common threads in a paragraph at the top of the (still-empty) `SCOPING-WORKSHEET.md`. If the threads disagree on the user, the disagreement is *named* — "Pat thinks freshmen, Sam thinks juniors, we will pick one in the scope pass."

### 3.3 The "do not solution yet" rule

The most common failure of segment 2 is jumping to the solution. "Oh, we could use the OpenAI API to..." cut. Solutions come in the scope pass (segment 4). Segment 2 is *prompt comprehension*, not architecture.

The Comms Lead-elect's first job is to enforce this rule. Their one-sentence intervention: "Park that for the scope pass at 0:30." Park = write it in the chat as a one-line note; the chat is the parking lot. The team revisits the lot in segment 4.

---

## 4. Segment 3 — Role assignment (0:20 — 0:30)

Ten minutes. Three roles. Up to four people. The role assignment is the segment that *cannot be skipped* — every other segment can be 10% sloppy and recover; a role-less team is a chaotic team for the next 23 hours.

### 4.1 The three core roles

C4 compresses the larger hackathon-team taxonomy into three named roles. Each role has one job, one decider authority, and one deliverable.

```
┌────────────────────────────────────────────────────────────┐
│  THE THREE CORE ROLES                                      │
│                                                            │
│  BUILDER LEAD                                              │
│   - Decides what merges to main and when                   │
│   - Owns the build track                                   │
│   - Deliverable: a working deploy URL by hour 4            │
│                                                            │
│  DEMO LEAD                                                 │
│   - Decides what goes in the 3-minute team demo recording  │
│   - Owns the design+demo track                             │
│   - Deliverable: a draft script by hour 12,                │
│     a recorded take by hour 24                             │
│                                                            │
│  COMMS LEAD                                                │
│   - Decides what gets posted in channel vs DMs             │
│   - Owns the comms+log track                               │
│   - Deliverable: a committed DAY-1-LOG.md with entries     │
│     for every named event                                  │
└────────────────────────────────────────────────────────────┘
```

Three roles; three deciders. Note the verb in each role is *decides*, not *does*. The Builder Lead does not write all the code; they decide what code gets merged. The Demo Lead does not narrate the demo alone; they decide what the demo shows. The Comms Lead does not write every message; they decide what gets pinned and what gets logged.

### 4.2 The role-fit grid

A team of 3 or 4 assigns roles using a one-sheet grid. The grid has one row per teammate, one column per role, and one cell per match. Each cell holds a number 0 to 3: 0 = "I would actively prefer not to," 1 = "I can do this if needed," 2 = "I am willing and decent at this," 3 = "I am strongest at this."

```
            | Builder Lead | Demo Lead | Comms Lead |
            |--------------|-----------|------------|
   Pat      |      3       |     1     |     2      |
   Sam      |      2       |     3     |     1      |
   Jordan   |      1       |     2     |     3      |
   Alex     |      2       |     1     |     2      |
```

The grid takes 3 minutes to fill (each teammate writes their own row). The Builder Lead-elect (or any rotating facilitator) reads each column aloud and assigns the role to the highest-number cell. If two cells tie at 3, the teammate with the lower max on other rows takes the role.

In the example above:
- Builder Lead: Pat (3).
- Demo Lead: Sam (3).
- Comms Lead: Jordan (3).
- Alex (the 4th teammate) is the *floating builder* — they pick up MUST items from the build track without owning the merge decision.

### 4.3 The 4-person team and the hour-12 rotation

On a 4-person team, the Builder Lead role *rotates at hour 12*. The original Builder Lead hands the merge decision to the floating builder (or any teammate with a 2+ on the Builder column of the grid). The rotation prevents two failure modes:

- **The exhausted Builder Lead at hour 18.** Decisions about merges, scope cuts, and stand-up direction degrade after 12 hours of focus. The rotation is a forced break.
- **The over-centralized Builder Lead.** The teammate who runs the build from hour 0 to hour 24 alone is making 100% of the merge decisions; the other 3 teammates are passengers. The rotation distributes the decision load.

On a 3-person team, the Builder Lead does not rotate (no spare teammate to hand to). Instead, the Builder Lead takes a *2-hour break* at hour 12 — no merges, no decisions, sleep or eat or walk. The Demo Lead and Comms Lead hold the build track in caretaker mode for those 2 hours.

### 4.4 The three kickoff failure modes (role-side)

Three predictable failures of the role-assignment segment:

- **The unclaimed Comms Lead.** Everyone wants Builder; nobody wants Comms. The team agrees to "share Comms" and 24 hours later there is no log. *Fix:* the role-fit grid forces a column-3; even if nobody scored 3 on Comms, the highest score takes it.
- **The double-Builder.** Two teammates both score 3 on Builder. The team agrees to "co-lead the build." Twenty-four hours later there are two merge philosophies and a 4-hour merge fight. *Fix:* one Builder; the tie-breaker is the teammate with the lower max elsewhere. The other Builder-3 becomes the floating builder.
- **The silent disagreement.** A teammate scores their row low across all three roles (1/1/1). They are signaling "I do not want to be here" and the team interprets it as modesty. *Fix:* the Comms Lead-elect asks one question: "Pat, your row is low — is this the right week for this dry-run for you?" The answer is honest; the team adjusts (smaller team, postponed dry-run, or Pat as a floating builder with no role decisions).

The role-assignment segment is the segment that surfaces team-formation problems *before* the build starts. Spending 10 minutes here saves the 4-hour conflict at hour 16.

---

## 5. Segment 4 — Scope pass one (0:30 — 0:40)

Ten minutes; the worksheet draft. The worksheet is *not* fully written in segment 4 — segment 4 is the *first pass*. Lecture 2 covers the team scope pass in depth; segment 4 is the kickoff's hand-off to the scope pass.

### 5.1 The three-MUST list (kickoff version)

In segment 4, the team writes a *first-pass* MUST list: three lines, one verb each. The MUSTs at this point are *candidates*, not committed; the team revisits them at hour 2 of the dry-run with the full worksheet template open.

```
First-pass MUST list (kickoff segment 4):

MUST 1: a freshman can post a question (signup + post).
MUST 2: a peer can see the question and reply.
MUST 3: the freshman sees the reply in real time on her phone.
```

Three verbs. One sentence each. The team reads the three aloud — the Comms Lead-elect goes first, then each teammate confirms ("yes that is the build" or "I would re-state MUST 2 as..."). The agreement at the read-aloud is the kickoff's exit criterion for segment 4.

### 5.2 The "no SHOULDs in the kickoff" rule

Segment 4 does *not* write the SHOULD column or the COULD column. The kickoff's job is the MUST list — the *spine* of the build. SHOULDs and COULDs are scope-pass content (Lecture 2 §2). A kickoff that writes all three columns runs to 90 minutes; a kickoff that writes just the MUSTs holds the 60-minute cap.

### 5.3 The handoff to the formal scope pass

The last line of segment 4 is a written sentence in the (now half-written) `SCOPING-WORKSHEET.md`:

> "First-pass MUST list approved by team at hour 0:40. Formal scope pass to run at hour 2:00 of the dry-run. Builder Lead facilitates."

That sentence is the handoff. Segment 4 closes; segment 5 begins.

---

## 6. Segment 5 — Comms-channel setup and pinning (0:40 — 0:50)

Ten minutes; the comms norm. The Comms Lead-elect runs this segment. The output is *one channel*, *one shared doc*, *one stand-up cadence*, and *one DM rule*, with the four items pinned as the channel's first four pinned messages.

### 6.1 The four pinned messages

```
┌────────────────────────────────────────────────────────────┐
│  THE FOUR PINNED MESSAGES                                  │
│                                                            │
│  Pin 1: the kickoff agenda                                 │
│    "60-minute kickoff: intro / prompt / roles / scope /    │
│     comms / handoff. We are in segment 5 of 6."            │
│                                                            │
│  Pin 2: the stand-up cadence and template                  │
│    "Stand-ups at hour 4, hour 12, hour 22. Three           │
│     questions: shipped / blocking / next 4h. 10 min cap."  │
│                                                            │
│  Pin 3: the DM vs channel rule                             │
│    "Decisions in #channel. Banter, async-OK, and           │
│     time-sensitive blockers in DMs. If you DM a decision,  │
│     re-post it to the channel."                            │
│                                                            │
│  Pin 4: the shared doc URL                                 │
│    "Shared doc: [URL]. Worksheet, log, and stand-up notes  │
│     live here. Read-write for all team members."          │
└────────────────────────────────────────────────────────────┘
```

Four pins. The Comms Lead does the pinning live, on the call, while the team watches. The pinning takes 4 minutes; the remaining 6 minutes of segment 5 are spent reading each pin aloud and confirming the team agrees with each one.

### 6.2 The "one tool per role" rule

The team uses *one* chat tool, *one* shared doc tool, *one* repo. Not two of any. The temptation to "use Slack for chat and Discord for voice and Google Docs for notes and Notion for tasks and GitHub for code" is the comms-tool sprawl that costs the team 1 hour over the 24-hour window in tool-switching alone.

The C4 default tool set:
- Chat: Slack free *or* Discord. Pick one at hour 0.
- Voice: Google Meet free *or* Discord voice. The team agrees on which call URL is "the team call."
- Doc: Google Docs *or* HackMD *or* GitHub wiki. Pick one.
- Repo: GitHub. Default for the cohort.

Five categories; one tool per category; five total tools. Not ten.

### 6.3 The "first DM that should have been a channel post" pattern

The most common day-1 comms failure is the side-channel decision: two teammates DM each other, decide something, and never tell the third. The fix is mechanical and lives in pin 3: *if you DM a decision, re-post it to the channel*.

The Comms Lead's role across the next 23 hours is to enforce this rule once per shift. The intervention sentence: "Was that a decision? Mind dropping it in #channel?" Six words. Repeatable.

---

## 7. Segment 6 — "We start coding at" handoff (0:50 — 1:00)

The final ten minutes. The kickoff *closes*. The output is one timestamp, one named first-action per role, and one calendared next event.

### 7.1 The named timestamp

The Builder Lead says, aloud: "We start coding at [HH:MM] today. Stand-up 1 is at [HH:MM + 4 hours]. Stand-up 2 is at [HH:MM + 12 hours]. Stand-up 3 is at [HH:MM + 22 hours]. Close-out is at [HH:MM + 24 hours]."

Five timestamps. The Comms Lead writes them into pin 2 and into the calendar. The first one — "we start coding at" — is the kickoff's exit timestamp; the kickoff is officially over at that timestamp.

### 7.2 The first action per role

Each role's first action is named aloud, in one sentence:

```
Builder Lead, first action:
  "I am scaffolding the repo with the W2 template and pushing
   the first commit by hour 1:30."

Demo Lead, first action:
  "I am drafting the hook sentence from the prompt and posting
   the first draft in #channel by hour 2:00."

Comms Lead, first action:
  "I am opening DAY-1-LOG.md and writing the hour-0 entry —
   the kickoff agenda timestamps and the role assignments —
   by hour 1:15."

Floating Builder (4-person team), first action:
  "I am writing one MUST-list user story per MUST item and
   posting them in #channel by hour 2:00."
```

Four first-actions; four sentences; four deadlines inside the next 2 hours. The first-actions are the *receipts* of the kickoff — the team can prove the kickoff happened because four commits / posts / log entries land inside the first 2 hours, each with a named owner.

### 7.3 The kickoff-end log entry

The last thing the Comms Lead does in segment 6 is *write the hour-0 entry in `DAY-1-LOG.md`*. Live, on the call, while the team watches. The entry looks like this:

```markdown
## Hour 0:00 — Kickoff (UTC YYYY-MM-DDTHH:MM)

**Team:** Crunch-7-A
**Members:** Pat (Builder Lead), Sam (Demo Lead), Jordan (Comms Lead), Alex (Floating Builder)
**Prompt:** [paste the prompt text]
**First-pass MUST list:**
  1. A freshman can post a question.
  2. A peer can see the question and reply.
  3. The freshman sees the reply in real time on her phone.
**Comms norms set:** one channel, one shared doc, stand-up cadence (hours 4 / 12 / 22 / 24), DM-vs-channel rule.
**Start-coding timestamp:** [HH:MM]
**Next event:** Stand-up 1 at [HH:MM + 4 hours].
```

That entry is the artifact. The Comms Lead commits it to the repo before segment 6 ends; the first commit to `DAY-1-LOG.md` is the kickoff's last act.

---

## 8. The three kickoff failure modes (meeting-side)

Five predictable failures of the kickoff meeting (we covered three role-side failures in §4.4; here are three meeting-side ones).

### 8.1 The introduction loop

> **Symptom:** segment 1 runs 18 minutes; segment 2 starts at 0:18.

The intros over-ran. Pat told a war story; Sam went 4 minutes on their React-vs-Vue preferences; Jordan apologized for not knowing the prompt yet. By 0:18 the team has 42 minutes left for 5 segments; one segment is going to get cut.

The fix: a visible 90-second per-teammate timer during segment 1. The Comms Lead-elect runs the timer; when it hits zero, the next teammate goes. The intro is the most-cuttable segment; cap it hard.

### 8.2 The unclaimed channel

> **Symptom:** segment 5 ends without pin 3 (the DM rule) being agreed.

The team agreed on a chat tool and a doc but not on the DM-vs-channel rule. The Comms Lead-elect read pin 3 aloud and Pat said "we can figure that out as we go." Twenty-four hours later, two teammates have DM'd four decisions to each other and the third teammate finds out at the close-out.

The fix: read pin 3 aloud *twice*. The first read is the proposal; the second read is the agreement. The agreement is "yes" or "I would re-state it as..." — silence is not agreement. The Comms Lead pushes for the explicit "yes" before moving on.

### 8.3 The vague handoff

> **Symptom:** segment 6 ends with "okay, let's get started" instead of a named timestamp.

The Builder Lead said "let's get started" instead of "we start coding at 14:00." The team trickles out of the call over the next 10 minutes; Pat starts coding at 14:05, Sam at 14:18, Jordan does not start at all because they are waiting for the formal start. The kickoff did not close; it dissolved.

The fix: the named timestamp (§7.1). Five timestamps, said aloud, written in pin 2, written in the calendar. The kickoff *ends* at the start-coding timestamp; teammates leave the call when that timestamp arrives.

---

## 9. The kickoff and the rest of the dry-run

The kickoff is hour 0:00 to 1:00. The rest of the dry-run is hour 1:00 to 24:00 — 23 hours. The kickoff is 4% of the wall-clock and roughly 30% of the variance in outcome. A clean kickoff produces a 90% chance of a clean hour-24 close-out; a sloppy kickoff produces a 30% chance.

The kickoff's outputs survive the dry-run:

- The `TEAM-CONTRACT.md` (drafted in segment 4-ish, formalized at hour 2): the team's working agreement.
- The `SCOPING-WORKSHEET.md` (first-pass in segment 4, formalized at hour 2): the team's MUST list.
- The four pinned messages: the comms norms.
- The `DAY-1-LOG.md` (first entry at hour 0:55): the team's audit trail.
- The four named first-actions: the team's hour-1 commits.

Five artifacts; one hour. The kickoff's ROI is the ratio.

---

## 10. Recap

- The kickoff is six 10-minute segments: introductions, prompt reading, role assignment, scope pass one, comms-channel setup, "we start coding at" handoff. The cap is 60 minutes; the discipline is the band.
- The three core roles are Builder Lead (decides merges), Demo Lead (decides demo content), Comms Lead (decides channel posts and runs the log). One per team; rotation rule at hour 12 on 4-person teams.
- The role-fit grid is the 3-minute tool for role assignment. Each teammate scores each role 0-3; the highest-scoring teammate takes the role; ties break to the teammate with the lower max elsewhere.
- The four pinned messages (kickoff agenda, stand-up cadence, DM-vs-channel rule, shared doc URL) are the comms norm. The Comms Lead pins them live during segment 5 and reads each aloud.
- The "we start coding at" handoff names five timestamps (start, stand-up 1, stand-up 2, stand-up 3, close-out) and four first-actions (one per role). The kickoff ends when the first timestamp arrives.
- Three role-side failure modes: unclaimed Comms Lead, double-Builder, silent disagreement. Three meeting-side failures: introduction loop, unclaimed channel, vague handoff. One fix per mode.
- The kickoff's artifacts — `TEAM-CONTRACT.md`, `SCOPING-WORKSHEET.md`, four pinned messages, `DAY-1-LOG.md` hour-0 entry, four first-actions — survive the dry-run. The kickoff is the *commit point* of the build.
- The kickoff is 4% of the dry-run's wall-clock and ~30% of the variance in outcome. Sixty minutes is the highest-ROI hour of the entire event.

Continue to [Lecture 2 — Scoping and Parallelization](./02-scoping-and-parallelization.md), where the team learns the formal hour-2 scope pass (re-running the Week-5 worksheet as a team), the three-track parallelization model (build / design+demo / comms+log), the 30-minute block rule, and the hour-by-hour schedule for hours 0 through 24.

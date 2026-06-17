# Exercise 1 — Team Charter for a Fake Event

> **Time:** ~1 hour.
> **When in the week:** Tuesday.
> **Deliverable:** `EXERCISE-01-TEAM-CHARTER.md` committed to your week-7 working folder.
> **Prerequisite:** Lecture 1 read.

## What this exercise is

You will draft a complete `TEAM-CONTRACT.md` for a *fake hackathon team* responding to a *fake event prompt*. The team is imaginary; you are the only person doing the writing. The output is the kind of document the real Comms Lead would commit at hour 1:30 of a real dry-run after a 60-minute kickoff.

This exercise is solo writing for *team-mode preparation*. The muscle being built is "I can produce a team charter in 45 minutes" — so that in the real dry-run on Saturday, the charter is not the bottleneck.

## What this exercise is not

This is not a team activity. You are not recruiting four imaginary friends and role-playing the kickoff meeting with them. The kickoff role-play is the actual dry-run (mini-project). Exercise 1 is *the writing only*.

## The fake event prompt

Use this prompt verbatim. Do not invent your own; one of the muscles being built is responding to a prompt that you did not write.

```
SPRING SHIPLAB 2026 — 24-hour micro-hackathon

Theme: "Local accessibility"

You and your team have 24 hours to ship a working web prototype that
solves a small, named accessibility problem for a real (or realistic)
local group. The prompt is intentionally narrow: the problem must be
specific (one named user group, one named pain), the solution must be
shippable in 24 hours (one named verb, three MUST features), and the
demo must be a 3-minute video against a live deploy URL.

Allowed: any free / open-source tool; any free hosting tier; any third-
party API with a free tier; any framework. Disallowed: a build started
before the event start time; a demo recorded against localhost.

Judging: 50% demo, 30% accessibility-impact narrative, 20% repo
hygiene (README, license, code of conduct).

Submission: a public GitHub repo URL and a 3-minute demo video URL.
```

The prompt is the input. Your charter is the output.

## The fake team

You are inventing the team. Four people; reasonable skill profiles. Use these names and one-sentence skill profiles to keep yourself from over-tweaking:

- **Pat** — strongest at frontend React; has shipped two solo Week-3-style prototypes.
- **Sam** — strongest at design (Figma) and copy; has shipped one solo Week-3 prototype.
- **Jordan** — strongest at backend (Node / Express) and infrastructure (Vercel / Render); has shipped one solo Week-3 prototype and one small team project.
- **Alex** — generalist; can do frontend, backend, or design; has shipped one solo Week-3 prototype.

Four teammates. Use these profiles; do not invent new ones (a muscle being built is "I can write a charter for a team I did not pick").

## The charter template

Your `EXERCISE-01-TEAM-CHARTER.md` has nine sections in this order. Each section is one paragraph or one short list. The full document fits on one printed page (about 600-800 words).

### Section 1 — Team name and members (5 minutes)

Pick a team name in 60 seconds. Use a placeholder ("Shiplab-A") if needed.

```markdown
## 1. Team name and members
**Team:** [name]
**Members:**
  - Pat — [role] — [skill summary]
  - Sam — [role] — [skill summary]
  - Jordan — [role] — [skill summary]
  - Alex — [role] — [skill summary]
```

Fill in the roles using the role-fit grid from Lecture 1 §4.2. Score the grid in your head; assign the roles; write the result.

### Section 2 — Working agreement (10 minutes)

A one-paragraph working agreement. The team's commitment to each other across the 24 hours.

```markdown
## 2. Working agreement
We agree to:
  - Show up to all three stand-ups (hours 4, 12, 22) on the team call.
  - Post decisions in #channel within 30 minutes of making them.
  - Cap the kickoff at 60 minutes and stand-ups at 10 minutes.
  - Sleep at least 4 hours between hour 14 and hour 18.
  - Treat the MLH Code of Conduct as the floor of team behavior.
We agree NOT to:
  - Make scope decisions in DMs without posting to channel.
  - Merge SHOULDs to main before all MUSTs satisfy done-rows.
  - Skip a stand-up for "I'm in the middle of something."
```

Two short lists. Five "we agree to" items; three "we agree NOT to" items. Write them in the voice the team would *say* them, not in the voice a lawyer would draft them.

### Section 3 — Roles and decision authority (5 minutes)

A short table mapping the four teammates to the three core roles and the floating-builder slot.

```markdown
## 3. Roles and decision authority
| Role | Owner | Decision authority |
|------|-------|-------------------|
| Builder Lead | [name] | What merges to main and when. |
| Demo Lead | [name] | What goes in the 3-minute demo recording. |
| Comms Lead | [name] | What gets pinned in #channel and what gets logged. |
| Floating Builder | [name] | None alone; supports the Builder Lead on MUST work. |
```

Four rows. The names come from your section 1 role assignment.

### Section 4 — Communication norms (5 minutes)

The four norms from Lecture 3 §1.2, restated in your team's voice.

```markdown
## 4. Communication norms
- **One channel:** #shiplab-a. All team comms here.
- **One shared doc:** [link to Google Doc / HackMD / repo wiki].
- **One stand-up cadence:** hours 4, 12, 22, 10-min cap, three questions.
- **One DM rule:** decisions in #channel; banter in DMs; if you DM a
  decision, re-post within 30 minutes.
```

Four bullets. Each is a one-line norm.

### Section 5 — Schedule and time-zone agreement (10 minutes)

The hour-by-hour schedule from Lecture 2 §5, plus the team's time-zone reconciliation.

```markdown
## 5. Schedule and time-zone agreement
**Event start:** 2026-XX-XX 09:00 local team time.
**Time zones:** Pat and Sam in ET; Jordan in PT; Alex in CT.
**Synchronous hours:** 09:00-14:00 ET on day 1; 09:00-14:00 ET on day 2.
**Sleep window:** ~23:00-03:00 ET (cohort-default).
**Stand-up times (local team time):**
  - Stand-up 1: 13:00 day 1 (hour 4)
  - Stand-up 2: 21:00 day 1 (hour 12)
  - Stand-up 3: 07:00 day 2 (hour 22)
  - Close-out: 09:00 day 2 (hour 24)
```

Five fields. Pick local times that match the cohort norm (US-Eastern-leaning); the cohort coordinator publishes the canonical times each event.

### Section 6 — Tools and accounts (5 minutes)

The team's tool list. One tool per category, one link per item.

```markdown
## 6. Tools and accounts
- Chat: Slack (workspace: [URL]) or Discord (server: [URL]).
- Voice: Google Meet ([URL]).
- Doc: Google Docs ([URL]) or HackMD ([URL]).
- Repo: GitHub ([URL]).
- Kanban: GitHub Projects ([URL]).
- Deploy host: Vercel or Render (decided at hour 1).
- Recording: Loom free or YouTube unlisted (decided at hour 22).
```

Seven categories; one tool each. The team's *one* of each.

### Section 7 — Conflict and escalation (5 minutes)

A short paragraph naming the four day-1 conflicts (Lecture 3 §7) and the team's agreement on how they get surfaced.

```markdown
## 7. Conflict and escalation
We expect four kinds of day-1 friction: scope creep, silent
disagreement, role overlap, and merge-fight. Each gets surfaced
the same way: name the observation in #channel without blame,
offer two paths, let the affected teammate choose, log the
resolution in DAY-1-LOG.md. The Comms Lead is the default
surfacer; any teammate can also surface. The Builder Lead
is the final decider on merge conflicts; the Demo Lead is
the final decider on demo content; the Comms Lead is the
final decider on what gets logged.
```

One paragraph. Three sentences minimum.

### Section 8 — Code of Conduct (3 minutes)

A short paragraph linking to the MLH CoC (or Contributor Covenant) and naming the team's behavioral floor.

```markdown
## 8. Code of Conduct
We follow the MLH Code of Conduct (https://mlh.io/code-of-conduct)
as the floor of our behavior. Harassment, discrimination, and
disrespect are not tolerated regardless of timing. Tired-team
behavior at hour 18 is held to the same standard as fresh-team
behavior at hour 1.
```

Two sentences. Plus the link.

### Section 9 — Signatures (2 minutes)

A simple sign-off block. Each teammate types their name (or initials) in the document.

```markdown
## 9. Signatures
By committing this file, each of us acknowledges we have read,
understood, and agreed to the working agreement above.

  - Pat: ____
  - Sam: ____
  - Jordan: ____
  - Alex: ____
```

For the exercise, you sign all four lines as the writer of the document.

## Process

1. Open a new file: `exercise-01-team-charter.md` in your week-7 working folder.
2. Paste the nine-section template.
3. Fill in each section using the fake event prompt and the fake team.
4. Read the document aloud once.
5. Edit any sentence that sounds like a lawyer wrote it (you are writing in the team's voice).
6. Commit.

## Acceptance checklist

Grade your own work. The document is *acceptable* if every box is checked. The document is *strong* if every box is checked and the language reads like a team would say it aloud.

- [ ] The team name is one word or a short phrase, picked in under 60 seconds.
- [ ] Each teammate has a role from the role-fit grid (Builder, Demo, Comms, Floating).
- [ ] The working agreement has 5 "we agree to" items and 3 "we agree NOT to" items.
- [ ] The roles table has four rows with decision authority named in one sentence each.
- [ ] The four communication norms are written in one-line form.
- [ ] The schedule names 4 stand-up timestamps in the team's local time.
- [ ] The tools section names one tool per category, no duplicates.
- [ ] The conflict section names all four day-1 conflicts (scope creep, silent disagreement, role overlap, merge fight).
- [ ] The Code of Conduct section links to the MLH CoC.
- [ ] The signatures section has four named lines.
- [ ] The full document fits on one printed page (~600-800 words).
- [ ] Reading the document aloud takes 3-4 minutes.

If any box is unchecked, fix that section before continuing. The acceptance bar is mechanical, not aesthetic.

## Common failure modes

Five patterns the cohort tends to fall into. Recognize them in your own draft.

- **The "rockstar" voice.** The working agreement reads like a startup manifesto ("we crush it / we never stop / we ship every day"). Cut. The C4 voice is sober. Replace with declarative one-liners.
- **The lawyer voice.** The working agreement reads like a contract ("the parties hereby agree..."). Cut. The team is four people, not a law firm. Replace with the way the team would say it on the call.
- **The two-page sprawl.** The document grows to 1500+ words because each section has 4 paragraphs. Cut. The charter fits on one printed page. The discipline is the brevity.
- **The role over-specification.** The Builder Lead's row in the roles table lists 12 specific tasks ("merges PRs, reviews code, fixes deploy bugs, runs CI, ..."). Cut. The role's *decision authority* is one sentence; the work the role does is downstream of the authority.
- **The missing time-zone reconciliation.** The schedule section names timestamps in one time zone with no acknowledgment that one teammate is in a different zone. Add the time-zone field; name the reconciliation.

## What to do with the deliverable

The deliverable is the *practice draft*. You will write a *fresh* charter at the real dry-run on Saturday (mini-project), using the same template, with real teammates. The Tuesday draft is the warm-up; the Saturday draft is the artifact.

Some teammates copy the Tuesday draft into the Saturday draft as a starting point. That is fine *only if* the Saturday version is re-discussed line-by-line with the real team — the charter is the team's agreement, not the writer's preference. Re-discussion is the rule; copy-paste is the antipattern.

## Up next

Continue to [Exercise 2 — Hour-by-hour schedule from a written prompt](./exercise-02-hour-by-hour-schedule.md).

# Week 5 — Resources

Every resource on this page is **free** and **publicly accessible**. No paywalled books, no signups beyond the free tier. If a link breaks, please open an issue.

## Required reading (work it into your week)

- **DSDM Consortium — The official MoSCoW prioritization page.** Read the "How to use MoSCoW" section; ignore the consulting framing: <https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html>
- **Atlassian — Prioritization frameworks (MoSCoW summary).** A two-minute corporate primer; the framing is what we adapt for hackathon compression: <https://www.atlassian.com/agile/product-management/prioritization>
- **Will Larson — "Pre-mortems are the best tool you are not using."** A blog post on writing the failure scenario before the project starts. The cut-list at hour 2 / 12 / 24 is a pre-mortem applied to scope: <https://lethain.com/pre-mortems/>
- **Re-read C4 Week 4 Lecture 2 §3.** The three scope-creep shapes (hour 2, 12, 24) are this week's three cut-list moments. The connection is direct.

If you only have time for one, read the Larson piece. The pre-mortem framing is the single best thing you can borrow from outside the hackathon space, and it makes the cut-list paragraph in Lecture 1 §2 click immediately.

## On MoSCoW (free, deeper)

| Piece | Why | Link |
|------|-----|------|
| **DSDM Agile Project Framework, MoSCoW chapter** | The primary source. 4 pages, free, the closest thing to a canonical definition. Read once. | <https://www.agilebusiness.org/dsdm-project-framework/moscow-prioritisation.html> |
| **ProductPlan — MoSCoW method overview** | A short visual primer; the four-column diagram is the most-cited one online. Skip the certification ads. | <https://www.productplan.com/glossary/moscow-prioritization/> |
| **Romano Roth — "Why I use MoSCoW for backlog grooming"** | A developer's blog post (not a consulting page). Closer to the C4 voice; useful for the hackathon adaptation. | Search "Romano Roth MoSCoW prioritisation"; multiple mirrors exist. |
| **"The dangerous comfort of MUST" (search query)** | A pattern: search for blog posts critiquing MoSCoW for over-using MUST. The critique is exactly the C4 voice's "MUST-of-five failure mode." | DuckDuckGo or Google: `MoSCoW must overused blog` |

The DSDM piece is the most-cited document for MoSCoW. It is 4 pages, written for free, and most people who quote it have not read it. Read it once, then come back to the lecture.

## On scoping under time pressure

- **Reforge / Lenny's Newsletter, free posts on scoping.** Search "scoping prototype timebox blog." Pick three free posts; ignore paywalled excerpts. The common thread — "cut to the demo verb" — is the C4 voice's MUST-or-die.
- **The "pre-mortem" technique (Gary Klein).** A 90-second technique: before the project starts, the team writes "we failed because…" The cut-list at hour 2/12/24 is a structural pre-mortem.
- **C4 Week 1 Lecture 2 §"Demo or die".** Re-read once. The discipline of cutting scope to fit a demo is the same discipline of saying no to a teammate's suggestion. The voice is the same; this week extends the muscle.

## Planning and worksheet templates

- **A printable 4-column MoSCoW grid.** Print one page with four boxed columns labeled MUST / SHOULD / COULD / WON'T. That is the entire toolkit for the hour-0 pass.
- **Index cards or sticky notes.** A pack of 100 sticky notes is the most cost-effective MoSCoW deck on Earth. For in-person hackathons, this beats every browser tool.
- **The C4 mini-project template.** The one you commit this week. It is intentionally one page and intentionally opinionated. Outgrow it after Week 8.

C4's default is sticky notes for in-person events and a shared Google Doc / Notion page for remote. The tool is not the skill; the skill is the cut the tool forces.

## Real hackathon project READMEs (for reverse-engineering)

The single best study material for scoping discipline is *other teams' public submissions*. Three sources, in order of usefulness:

| Source | What you find | How to search |
|--------|---------------|---------------|
| **Major League Hacking (MLH) past events** | Submitted projects with submission pages, devpost links, and READMEs. The good ones have a "what we built / what we did not" section. | <https://mlh.io/seasons> and click into past events |
| **Devpost — public hackathon submissions** | The largest searchable database of hackathon submissions. Filter for "submitted" + the rubric of past events. | <https://devpost.com/hackathons?status=ended> |
| **GitHub topic: `hackathon`** | Public repos with a hackathon README. Quality varies; the good ones are gold. | <https://github.com/topics/hackathon> |

The reading skill: open three READMEs, *not* the live demos. The README is where the team's MoSCoW lives (implicitly or explicitly). Look for "what this does" (the MUST), "features" (the SHOULD), "future work" (the de-facto WON'T). Homework Problem 5 this week is exactly this exercise.

## On the demo-ability bench

- **Vercel docs — Deploy previews and environment variables.** Re-read once. The "seeded-data ghost" failure mode is almost always a Vercel env-var or preview-deploy gap: <https://vercel.com/docs/deployments>
- **Railway docs — Environment variables and seeding.** Same logic for Railway: <https://docs.railway.app/develop/variables>
- **Supabase docs — Seeding and migrations.** If you used Supabase in Week 2, re-skim the seeding section. Most prod-empty-page bugs originate here: <https://supabase.com/docs/guides/database/seeding>
- **OWASP "deploy checklist" (free).** A more security-flavored checklist; useful for the demo-ability checklist's "is it reachable" and "is HTTPS green" questions: <https://owasp.org/www-project-application-security-verification-standard/>

The "deploy URL is the bench" rule is mechanical: every URL you submit needs a green padlock, a sub-3-second load, and a clickable MUST. The OWASP checklist is the upper bound; the C4 five-question test is the lower bound.

## On reading public hackathon submissions

- **"What good hackathon READMEs look like" (search query).** Search the cohort channel and GitHub for examples. The C4 default reference: any project README from a past Code Crunch event. The archive lives in `SPRING-2025/` of this repo.
- **"How to write a hackathon README" (HelloAI, Mintlify, dev.to).** Three free posts on the structure; ignore the templates that pad with screenshots, focus on the structure that explicitly names MUST and WON'T.
- **C4 BRAND.md scoping chart.** Re-read once. The four-column chart in the brand guide is the visual standard for every C4 worksheet you ship. Your mini-project's MoSCoW section should match it in shape.

## On the four MoSCoW failure modes

Each failure mode below has a one-sentence test. Lecture 1 §4 elaborates.

- **MUST-of-five.** "We have 5 MUSTs and we will ship them all." Test: did the team force MUST to 3 at the end of the scoping pass? If no, the pass failed.
- **Empty WON'T.** "Everything is in MUST or SHOULD; we did not say no to anything yet." Test: does WON'T have 4+ items, each with a one-sentence reason? If no, the WON'T is fiction.
- **Aspirational COULD.** "We have 5 COULDs and they are all exciting." Test: at hour 30 with MUST and SHOULD done, would the team actually start *one* of these? If no, move them to WON'T.
- **Verbal-only MoSCoW.** "We talked it through; we know what to build." Test: is the four-column board *committed to the repo* by hour 1? If no, MoSCoW has not happened yet.

Read each test out loud once. You will recognize at least two of them from past group projects. Naming them is half the cure.

## On the four demo-ability failure modes

Same shape. Lecture 2 §5 elaborates.

- **The localhost demo.** "It works on my laptop." Test: is the demo running on the deploy URL the judges will use? If no, the demo failed.
- **The seeded-data ghost.** "The seed data is there in dev." Test: does the seeded record appear on the deploy URL? If no, the seed bug is real.
- **The polishing trap.** "I am polishing the MUST." Test: are MUST and SHOULD both clickable on the live URL? If MUST is and SHOULD is not, *stop polishing MUST*.
- **The "we'll fix it" delusion.** "We can fix this in 2 hours before the demo." Test: at hour 24, is the failing item being cut, or being "fixed"? Default-cut is the safer call 80% of the time.

## Tools you will use this week (no new installs beyond Week 2)

- **Your `hackathon-template` repo from Week 2.** The pre-event walk-through (Lecture 2 §2) exercises this repo. Bring it.
- **Your `TEAM-CONTRACT.md` from Week 4.** The cut-list (Lecture 1 §2) extends the contract's "no" script. Bring it.
- **A timer.** Phone timer, kitchen timer, `sleep 1200 && say "scope pass over"` in your terminal — any of these. The 20-minute MoSCoW pass needs a clock.
- **Sticky notes (or a shared doc with four columns).** For Exercise 2. Buy a pack of 100 stickies; they last six months.
- **A scratch text file or paper.** For drafting cut-list paragraphs, demo-ability gaps, and worksheet drafts. Do not write these for the first time in your editor.

## Free tier limits worth knowing (Week 2 recap, still true)

- **Vercel free** — unlimited deploys, generous bandwidth, the only free-tier wall most C4 learners ever hit is the 100GB/mo bandwidth cap. Not a Week 5 concern.
- **Railway free** — a small monthly credit; enough for one always-on hackathon project but not three. Plan accordingly.
- **Supabase free** — 500MB DB, 1GB storage, 50,000 monthly active users. The MAU cap is the only one a hackathon team ever hits, and only if your demo goes viral.
- **GitHub Pages** — free, no caps for static demos. If your build is fully static (no backend), this is the cheapest demo URL on Earth.

## Glossary cheat sheet

| Term | Plain English |
|------|---------------|
| **MoSCoW** | The four-column scoping framework: MUST / SHOULD / COULD / WON'T. The "o"s are spacers, not abbreviations. |
| **MUST** | Ships or the demo dies. Max 3 items in a 36-hour event. Each item is clickable on the live URL at hour 33. |
| **SHOULD** | Ships if MUST is clean by hour 24. Conditional. 2–3 items. |
| **COULD** | Ships if MUST and SHOULD are clean by hour 30. Almost never ships. 1–2 items. Plan for that. |
| **WON'T** | Does not ship this event. *In writing*. 4–6 items, each with a one-sentence reason. The most-important column. |
| **Cut-list** | A pre-written list of *named* cuts that fire at hour 2, hour 12, hour 24. Lives at the bottom of the scoping worksheet. |
| **Demo-ability test** | The five-question test that grades a MUST item against the live URL in 60 seconds. Five yeses = demo-able. Any no = name the gap. |
| **The live URL is the bench** | The C4 voice's strongest demo-time claim. Localhost / staging / screenshot / screenshare all fail the bench test. Only the URL the judges will open counts. |
| **Pre-event walk-through** | A 30-minute structured exercise on your `hackathon-template` *this week*, before any real event, to catch deploy and seed gaps. |
| **Default-cut bias** | At hour 12 and 24, when a MUST is failing, the C4 default is to cut, not to extend. Extension produces hour-33 panic. |
| **The 36-hour scoping worksheet** | The one-page, five-section artifact: prompt, MoSCoW board, points budget, cut-list, demo-ability checklist. This week's mini-project. |
| **Pre-mortem** | A failure-scenario written before the project starts. The cut-list is a structural pre-mortem applied to scope. |
| **Seeded-data ghost** | The failure where seed data exists on localhost and is missing on the deploy URL. Most common cause: seed script not in the deploy pipeline. |
| **Polishing trap** | The failure where the team polishes a demo-able MUST while a SHOULD goes unbuilt. The five-yes ceiling is the cure. |

---

*If a link 404s, please open an issue so a future learner has a working version.*

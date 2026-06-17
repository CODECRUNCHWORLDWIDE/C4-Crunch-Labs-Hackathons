# Exercise Solutions — Week 9

One defensible solution per exercise. Each solution assumes a fake build for illustration; your own build is different, so your honest score and your honest answers will differ. The scoring criterion in each case is the *reasoning and the structure*, not the exact wording.

Read each solution *after* attempting the exercise.

The fake build referenced throughout these solutions is `MorningWalk` — a single-page web tool for FIU CS students that takes the user's dorm and class building and returns a "leave by" timestamp using a hardcoded Google Maps API call. Three MUSTs (form, walk-time estimate, leave-by timestamp); two SHOULDs (saved trips in localStorage, dark-mode toggle); committed in the Week 8 dry-run with a live deploy URL and a 3-minute demo video.

---

## Exercise 1 — Self-Score the Team's Week 8 Submission

A defensible self-score for `MorningWalk`:

```markdown
## Dimension 1 — Technical Complexity

**Score:** 2 / 5
**Evidence (one line):** Single-page React app with a hardcoded Google Maps
API call; no backend; no auth; no persistence beyond localStorage.
**Mindset tilt:** engineer — engineers will score this strictly because the
build's technical surface is small. The honest answer to "what was hard"
is "handling the API key in a client-only deploy without leaking it."
**Weight applied:** 25%

## Dimension 2 — Design and UX

**Score:** 3 / 5
**Evidence (one line):** One-screen form with three inputs and one output;
no design system; readable typography; mobile-responsive; one accessibility
fix (alt-text on the leave-by icon).
**Mindset tilt:** neutral — both mindsets score design directly.
**Weight applied:** 20%

## Dimension 3 — Originality

**Score:** 3 / 5
**Evidence (one line):** Narrow target (FIU CS students walking to 8am
classes) but the underlying mechanic (route + walk time) is a
well-trodden problem; the narrowness is the only originality lever.
**Mindset tilt:** investor — investors score originality on the
narrow-target framing, which is the build's strongest claim.
**Weight applied:** 20%

## Dimension 4 — Polish

**Score:** 3 / 5
**Evidence (one line):** Live deploy URL works; README has the C4 standard
sections; SUBMISSION.md present with six sections; one obvious rough edge
(the "leave by" timestamp is in 24-hour format with no AM/PM toggle).
**Mindset tilt:** neutral — polish is evidence-driven for both mindsets.
**Weight applied:** 20%

## Dimension 5 — Presentation

**Score:** 3 / 5
**Evidence (one line):** Week 8 dress rehearsal recording is 2:54, under
the cap; problem beat at 0:28; demo opens at 0:30; tech beat at 2:00;
ask at 2:48. The 30-90-45-15 arc is respected but the demo narration
runs slightly fast in the middle 30 seconds.
**Mindset tilt:** neutral.
**Weight applied:** 15%

## Weighted total

Computed: (2 * 0.25) + (3 * 0.20) + (3 * 0.20) + (3 * 0.20) + (3 * 0.15)
        = 0.50 + 0.60 + 0.60 + 0.60 + 0.45
        = 2.75 / 5.00

Note: this score is the team's *self-score* — not the score a real judge
would give. It is the team's calibration baseline for the mock pitch
in the mini-project.

## Honest gap

The lowest-scored dimension is Technical Complexity at 2. The reason it is
low is that the build is a thin client over a single hardcoded API call;
there is no engineering decision that a senior engineer would call
non-trivial. The single change the team could make in the next 4 hours
of polish work that would raise this dimension by 1 point is *adding a
saved-trips persistence layer using a free hosted KV (Upstash free tier
or Cloudflare KV)* and naming the "where to store state" trade-off in
the tech beat — the engineering decision becomes visible and scoreable.
```

Scoring notes:

- The honest 2-of-5 on Technical Complexity is the right move for `MorningWalk`. A team that scored this 4 of 5 is grading on effort, not artifact.
- The 3-of-5 on Design, Originality, Polish, and Presentation reflects the *expected baseline* anchor from Lecture 1 §4.1 — the team did the work but did not push the dimension.
- The Honest Gap names a *specific* 4-hour change (the KV persistence) that converts a 2 into a 3 on Technical Complexity. The named change is the bridge between "low score" and "actionable."

Weighted total of 2.75 / 5.00 corresponds to roughly 13.75 / 25 if the team was using an unweighted MLH-style total. Below the median; honest. The mock pitch will rehearse delivery; the gap analysis will rehearse the team's awareness of where the rubric will land.

---

## Exercise 2 — The Q&A Drill

Five sample Q&A answers for `MorningWalk`, plus a bridge sentence and an "I don't know."

```markdown
## Q1 — The user question

**Specific question for our build:**
"Who is this for, exactly? Why did you choose FIU CS students?"

**30-second answer (written):**

The user is a junior or senior CS student at FIU who lives in the on-campus
dorms (West Tower or Lakeview) and has at least one 8am class on the
classroom-block side of campus.

We chose this user because three of us are this user — we know the walk
takes between 8 and 14 minutes depending on the building, and we have
all been late to class for the same reason at least twice.

Before the build, we surveyed 8 FIU CS students; 6 of them said they
guess the walk time and pad it by 5 minutes. The number is the specific
data point we built against.

**Timing check (aloud):**
- Time spent on the aloud read: 27 seconds.
- Notes on what to tighten: the "junior or senior" hedge can drop; "CS
  students" is enough.

**Mindset tilt:** investor — investors score originality on the narrow-target framing.

## Q2 — The closest-competitor question

**Specific question for our build:**
"What is the closest existing tool that does this? Why hasn't Google
Maps just added this feature?"

**30-second answer (written):**

The closest existing tool is Google Maps' walking directions, which we
actually use under the hood. Google Maps gives you the walk time but
doesn't give you the "leave by" timestamp for a specific class time;
the user has to do the math themselves.

We differ in two ways: we pre-set the user's class times once (so the
math is automated for repeat trips), and we narrow the route options
to the specific dorm-to-class-building paths that FIU students actually
use, which Google sometimes routes off-campus through the gate.

Google probably won't build this because the addressable market is
"college students at residential campuses with morning classes" — a
fraction of a fraction of Google Maps' users.

**Timing check (aloud):**
- Time spent: 31 seconds (one second over; tightenable).
- Notes: the "two ways" framing is strong; the second one can be a
  half-sentence shorter.

**Mindset tilt:** investor — investors score the market-and-competitor reasoning here.

## Q3 — The technical question

**Specific question for our build:**
"How does the build handle the Google Maps API key? Is the key exposed
in the client?"

**30-second answer (written):**

We made the trade-off to deploy the API key with a domain restriction
on the Google Cloud console side rather than proxying through a backend.
The key is visible in the page source, but the restriction makes it
useless from any other origin.

The alternative was a serverless proxy on Cloudflare Workers or
Vercel; we rejected it because the latency added by the proxy was 200-
400ms in our prototype, which mattered for the "leave-by under 5 seconds"
UX target.

If we 10x'd the user count, the domain-restricted key would still work
but the free Google Maps quota would run out; the next step is the
proxy with caching, which solves both the quota and the cost.

**Timing check (aloud):**
- Time spent: 33 seconds (overshoot; the third paragraph is the cuttable one).
- Notes: tighten the "next step" paragraph to one sentence.

**Mindset tilt:** engineer — engineers score technical credibility on this
specific decision-and-trade-off.

## Q4 — The follow-through question

**Specific question for our build:**
"Would you keep building this after the hackathon? What's your plan
for next week?"

**30-second answer (written):**

Yes, two of us are committed to continuing for the next 4 weeks. The
specific deliverable in the first week is the saved-trips persistence
layer using a free hosted KV; the user can save their dorm and their
class schedule once and not re-enter the form each morning.

We will keep the live deploy URL, file two more issues from our user
survey (the "afternoon-class" path and the "Lakeview gate route"
ambiguity), and ship a v0.2 by end of next week.

If 20 FIU students actually use this in the first month, we will keep
going. If 0-5 use it, we will write a post-mortem and move on.

**Timing check (aloud):**
- Time spent: 29 seconds.
- Notes: the explicit "20 vs 0-5" measurement is the strong sentence
  — keep it.

**Mindset tilt:** investor — investors score follow-through intent on the
specific commitment and the measurable threshold.

## Q5 — The challenge question

**Specific question for our build:**
"Why should this win over the other team that built a similar tool for
a more general audience?"

**30-second answer (written):**

The strongest version of the challenge is that a more general tool
serves more users and has a bigger market.

Our response is that a narrower tool *works better* for the user it
serves — our build knows the FIU campus paths Google sometimes mis-
routes, knows the class start times without requiring user input, and
knows the FIU dorm names without ambiguity.

We agree the addressable user count is smaller. The reason we made the
narrow choice was the prompt asked for "a specific user group," and a
narrow tool with one happy user beats a general tool with zero.

**Timing check (aloud):**
- Time spent: 28 seconds.
- Notes: the "narrow tool with one happy user beats a general tool with
  zero" is the line that lands; keep it.

**Mindset tilt:** investor — challenge questions almost always come from
investor-mindset judges.

## Bridge sentence — fake hard question

**Fake hard question:**
"Did you consider GDPR compliance for the user's saved trip data?"

**Bridge sentence (full 25-30 seconds):**

"We did not build for GDPR specifically — the related question we did
spend time on was *data minimisation* in the saved-trips feature, which
we have not yet shipped. The plan for the saved-trips layer is to store
only the dorm name and the class building, never the user's identity or
location history. The privacy story is mostly a *what we don't store*
story; GDPR compliance would extend that with the deletion-request
endpoint, which is on the v0.2 issue list."

**Timing check (aloud):**
- Time spent: 27 seconds.
- Notes: the bridge phrase "the related question we did spend time on"
  carried the answer; without it, the response would have been a dodge.

## "I don't know" — fake genuinely-out-of-scope question

**Fake question:**
"What is the average walking speed of a CS student at FIU compared to
the national average for college students?"

**"I don't know" answer (full 15 seconds):**

"I don't know. The closest answer I can give is that we used Google
Maps' default pedestrian-speed estimate, which is 5 km/h. If we had two
more weeks, we would survey 30 FIU students with a phone GPS and
calibrate the model with the actual measured speed.

**Timing check (aloud):**
- Time spent: 16 seconds.
- Notes: stating the Google Maps default (5 km/h) made the "I don't
  know" feel honest rather than evasive — the specificity of the
  *closest* answer matters.
```

Scoring notes:

- The five answers each hit the three-beat structure (direct / evidence / close) from Lecture 3 §3.7.
- Two of the five answers overshot the 30-second cap (Q2 at 31s, Q3 at 33s); the *tightening* note is the muscle, not the failure.
- The bridge sentence used "the related question we did spend time on" — one of the four phrases from Lecture 3 §3.8.
- The "I don't know" stated the *closest* answer (the 5 km/h default), which is what makes the pattern read as honest rather than evasive.

---

## Exercise 3 — The Cue Drill

### Part 1 — the cue/recovery matrix for `MorningWalk`

```markdown
## Cue 1 — Clipboard pickup

**Cue (one sentence in your own words):**
The judge picks up the rubric clipboard and starts writing — they are
actively scoring this beat.

**Named recovery move:**
Re-anchor on rubric-relevant detail in the next sentence.

**Where in our pitch this cue is most likely to appear:**
0:25 (end of problem beat) — when we name the specific user "FIU CS
students walking to 8am classes."

**Recovery move applied to our pitch:**
The next sentence I would deliver is "and the originality lever for
this build is the narrow target — no existing tool we found scores the
'FIU dorm to classroom-block route' specifically." The sentence puts
the originality data point directly in front of the judge while they
are writing, so the rubric score lands on the dimension I named.

## Cue 2 — Eye-contact loss

**Cue (one sentence in your own words):**
The judge looks away from me or from the screen — phone, water bottle,
or the next team's table.

**Named recovery move:**
Pause for one beat, return eye contact, deliver the next sentence at
80% normal speed.

**Where in our pitch this cue is most likely to appear:**
1:10 (middle of demo beat) — when I am narrating the "leave by"
calculation step and the screen has not changed for ~5 seconds.

**Recovery move applied to our pitch:**
I would pause for one second, look up directly at the judge, and slow
the next sentence: "and *this* number — 7:42 — is the leave-by
timestamp." The pause and the slowed cadence pulls the judge's
attention back to the screen.

## Cue 3 — Lean-back

**Cue (one sentence in your own words):**
The judge leans backward, crosses their arms, or moves their hand
away from the rubric — they are mentally closing the slot.

**Named recovery move:**
Pivot to the ask early; abbreviate the tech beat.

**Where in our pitch this cue is most likely to appear:**
2:25 (mid tech beat) — when the engineering-decision narration is
running and the judge does not need more depth.

**Recovery move applied to our pitch:**
I would skip the second half of the tech beat (the proxy alternative)
and move directly to the ask: "...and that's the trade-off. We are
MorningWalk; the build is at morningwalk.vercel.app; we would love to
see 20 FIU students using this in the first month. Thank you." The
ask still lands at ~2:45, the pitch wraps under the cap, and the
judge's lean-back was respected.

## Cue 4 — Side-glance

**Cue (one sentence in your own words):**
The judge looks at another judge, at their notes from a previous team,
or at the room facilitator — they have a question brewing.

**Named recovery move:**
Name the elephant in the next sentence.

**Where in our pitch this cue is most likely to appear:**
2:05 (early tech beat) — right after I name the API key trade-off, a
co-judge might consult the engineer-judge on whether the trade-off is
acceptable.

**Recovery move applied to our pitch:**
The next sentence I would deliver is "I notice this trade-off might be
worth a question — to be specific, the key is restricted by domain on
Google Cloud, which makes it useless from any other origin. We can go
deeper in Q&A." The sentence pre-empts the question and routes the
deeper conversation to the Q&A.
```

### Part 2 — three composite vignettes

Three vignettes from three combinations (A, D, F):

```markdown
## Vignette 1 — Combination A — Clipboard pickup at 0:25

I am at the end of the problem beat, naming "FIU CS students walking
from the West Tower dorm to morning CS classes." The judge picks up
their clipboard and starts writing — they are scoring originality on
the user-pain framing. My next planned sentence was "and the
challenge is timing the walk so you're not late." I drop it and
substitute the rubric-relevant version: "and the originality lever
here is the narrow target — no existing tool we found scores the
'FIU dorm to classroom-block route' specifically." The cue redirected
the next 7 seconds; the rubric score landed where I aimed it.

## Vignette 2 — Combination D — Eye-contact loss at 2:20

I am two-thirds through the tech beat, describing the proxy
alternative we rejected. The judge's eyes drift to their phone — they
have stopped tracking the technical depth. I pause for one beat,
look up directly at the judge, and slow my next sentence: "...so
the trade-off was *latency over engineering elegance*. Two hundred
milliseconds matters when the user is checking their phone five
seconds before they need to leave." The slowed cadence and the
concrete fact (200ms) pulls the judge's eyes back. The pitch
continues at 2:30 with the judge re-engaged.

## Vignette 3 — Combination F — Lean-back during Q&A on a follow-up question

The Q&A is at the second-question mark. The judge asked about the
domain-restricted key (Q3 archetype); I answered in ~25 seconds. The
judge asked a follow-up: "but what if the user is on the campus VPN
and the domain restriction breaks?" I started a second technical
explanation — my answer is running 35 seconds and the judge leans
back, hand off the rubric. I see the lean-back, stop mid-sentence,
and end with: "the short answer is the campus VPN would route through
fiu.edu, which is on the allow-list. We tested it." The single-sentence
close beats the rambling continuation; the judge's lean-back ended; I
move to the next question.
```

Scoring notes:

- Each Part-1 block names a specific second-mark and a specific recovery sentence the team would deliver. The vignettes are not generic.
- Each Part-2 vignette is 90-110 words, within the 60-100 word guidance with a small overrun on Vignette 1.
- The three vignettes cover three different beats (problem, tech, Q&A) — the variance teaches the *generalisation* (the same recovery family, applied across the arc).
- The Q&A vignette (F) demonstrates the recovery-during-rambling pattern, which is the most common cue-driven recovery in real Q&A.

---

*The exercises are the bench. The mini-project is the run. Read the solutions once you have done the exercises; the comparison sharpens the next iteration.*

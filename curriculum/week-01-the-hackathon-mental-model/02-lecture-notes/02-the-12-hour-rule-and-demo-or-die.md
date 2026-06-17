# Lecture 2 — The 12-Hour Rule and the Demo-or-Die Doctrine

> **Duration:** ~1 hour of reading.
> **Outcome:** You can apply the 12-hour feasibility check, the demo-or-die filter, and the MoSCoW chart to any hackathon prompt. You can run a 12-hour stand-up, a 24-hour mid-event retro, and a final-3-hour freeze.

If you only remember two sentences from this lecture, remember these:

> **The 12-hour rule:** at the 12-hour mark of a 36-hour event, the remaining scope must fit in the remaining time *plus a 30% buffer*, or you cut. No exceptions, no "we will work faster."
>
> **The demo-or-die doctrine:** if a feature does not appear in the three-minute demo, it does not exist in the judges' eyes. Cut features that cannot make the demo. Build features that can.

Lecture 1 told you what hackathons reward. Lecture 2 is the operating discipline that lets you actually deliver on that reward when the clock is running.

---

## 1. Why scope discipline is the dominant skill

A 36-hour hackathon is a hostile schedule. You will lose hours you did not plan to lose — to setup, to a deploy that fails at 4 AM, to a teammate falling asleep at the keyboard, to a sponsor's API that throws 500s for thirty minutes. **The team that wins is rarely the one that built the most.** It is the team that *finished* the most.

There is a single skill that separates teams that finish from teams that do not: **the cut reflex**. The ability, hourly, to look at the remaining work and ask "what comes out?" — and to do it without ceremony.

The cut reflex is uncomfortable. It feels like giving up. It is not. It is acknowledging that the project you imagined in hour one is not the project you can ship in hour 36, and the project that ships *is* the project. The project on the whiteboard is fiction.

> **C4 voice:** the WON'T list is the most important list. Scoping *out* is the dominant skill. Scoping in is the easy part.

---

## 2. The MoSCoW chart

C4 leans on the **MoSCoW** prioritization technique because it survives the chaos of a 36-hour clock. The acronym:

- **M**ust — if any one of these does not ship, the project fails.
- **S**hould — if any one of these does not ship, the project is weaker but it still works.
- **C**ould — nice-to-haves; if there is time and energy.
- **W**on't — explicitly out of scope for *this* event.

The chart, as the C4 brand book renders it, is your team's operating document for the entire 36 hours:

```
┌────────────────────────────────────────────────────────────┐
│  SCOPE — 36h hackathon                                     │
│                                                            │
│  MUST    ✓ Login + profile                                 │
│  MUST    ✓ Submit a single user-generated entry            │
│  MUST    ✓ Public demo URL                                 │
│                                                            │
│  SHOULD  ▢ Search across entries                           │
│  SHOULD  ▢ Three-section landing page                      │
│                                                            │
│  COULD   ▢ Image upload                                    │
│  COULD   ▢ Light/dark theme                                │
│                                                            │
│  WON'T   ✗ Multi-tenancy                                   │
│  WON'T   ✗ Real-time chat                                  │
│  WON'T   ✗ Mobile app                                      │
└────────────────────────────────────────────────────────────┘
```

### 2.1 Rules of the chart

1. **The chart is drawn at hour zero.** Not hour six. Not "once we figure out the idea." Hour zero. If you do not know enough to fill it out, you do not know enough to start building.
2. **The MUSTs cap at three.** Three. Not five, not "well, technically four." Three. If you cannot describe your project with three musts, your project is two projects.
3. **The WON'Ts are written down and named.** "We will not build authentication. We will not build a mobile app. We will not build admin tooling." Write these out loud. Out loud means typed on the team Slack or written on the whiteboard. A WON'T that is implied is a WON'T that comes back at hour 28.
4. **The chart is revisited at every stand-up.** Hour 12. Hour 18. Hour 24. Hour 30. Hour 33. Items move from SHOULD to COULD to WON'T as the clock runs. Items rarely move *up*; assume they only move down.
5. **A demo URL is always a MUST.** Always. We will return to this in section 5.

### 2.2 Where teams go wrong with MoSCoW

- They write SHOULDs as MUSTs. Then they cannot cut anything because everything is "must."
- They forget the WON'T column entirely. Without it, every conversation is "could we add..."
- They fill the chart and then ignore it. The chart is not an art piece; it lives on the wall and gets updated.

---

## 3. The 12-hour rule, formally

The **12-hour rule** is a feasibility check you run at the midpoint of any 36-hour event (scale proportionally for 24h or 48h):

```
┌────────────────────────────────────────────────────────────┐
│  THE 12-HOUR RULE                                          │
│                                                            │
│  At hour 12 of a 36-hour event:                            │
│    REMAINING_WORK ≤ REMAINING_TIME × 0.7                   │
│                                                            │
│  Equivalently: leave a 30% buffer for                      │
│    - the demo recording                                    │
│    - the pitch rehearsal                                   │
│    - the final-3-hour freeze                               │
│    - the inevitable surprise (a deploy that breaks, an     │
│      API that rate-limits, a teammate who needs sleep)     │
│                                                            │
│  If the inequality fails, you CUT. Not "work faster."      │
└────────────────────────────────────────────────────────────┘
```

### 3.1 Why hour 12, not hour 18

At hour 18 (the midpoint) it is too late to cut cleanly. The team has invested in the original scope; cuts at hour 18 feel like a wake. At hour 12, the build is one-third complete and cuts feel like *strategy*. You buy six hours of execution time by cutting at hour 12 instead of hour 18.

### 3.2 Why a 30% buffer, not 10%

A 10% buffer assumes everything goes right. Nothing goes right at hour 30. The buffer is for the things you cannot list in advance:

- The deploy provider hits a 502 for ten minutes.
- A teammate falls asleep mid-merge.
- The sponsor's OAuth flow is broken on their staging environment.
- The hackathon Wi-Fi dies for thirty minutes.
- The demo recording renders out of sync.

In real events these happen *every event*. Teams that pretend they will not are surprised every event. The 30% buffer makes the surprises survivable.

### 3.3 The 12-hour stand-up

The 12-hour rule is enforced in a single ceremony: the **12-hour stand-up**. It runs about fifteen minutes:

1. **Each person, two minutes:** what did I ship since the start? What is blocked? What am I about to do?
2. **PM, three minutes:** read the MoSCoW chart out loud. Which items are *done*? Which are *in flight*? Which are *not started*?
3. **PM, two minutes:** apply the 12-hour rule. Is the remaining MUST + SHOULD list ≤ 70% of the remaining time? If not, cut.
4. **Whole team, three minutes:** agree on the cuts. Move items down. Re-draw the chart on the wall.

That is it. Fifteen minutes, no slides, no debate-club. The PM has the gavel.

---

## 4. The demo-or-die doctrine

```
┌────────────────────────────────────────────────────────────┐
│  THE DEMO-OR-DIE DOCTRINE                                  │
│                                                            │
│  If it does not appear in the 3-minute demo,               │
│  it does not exist in the judges' eyes.                    │
│                                                            │
│  Therefore: do not build features that cannot demo.        │
│             do not skip features that must.                │
└────────────────────────────────────────────────────────────┘
```

This is the harshest filter in C4 and it saves the most projects. The demo is approximately 180 seconds. Most demos cover three to five user actions visually. If a feature cannot be shown on screen in under thirty seconds, it does not belong in the demo, and therefore it does not belong in the build during a hackathon.

### 4.1 What "appears in the demo" actually means

- A user clicks something visible. The screen changes.
- A piece of data is shown that proves the system works.
- A second action is visible from the result of the first.

That is the unit. "Our backend handles 10,000 requests per second" does not appear in the demo. "The graph loads instantly when I click the button" does. The first is real engineering; the second is what the judge sees.

### 4.2 What this means at hour zero

When you draw the MoSCoW chart in hour zero, **annotate every MUST with the 30-second demo moment it produces**:

```
MUST  ✓ Login + profile         → "Watch me sign in, my name shows here"
MUST  ✓ Submit an entry         → "I type, I click submit, it appears"
MUST  ✓ Public demo URL         → "Anyone can click this link right now"
```

If a MUST does not produce a demo moment, it is not a MUST. Demote it.

### 4.3 The "show, don't tell" rule

In the demo itself, you will be tempted to *describe* features instead of showing them. Resist. The demo timing strip (from the C4 brand book) forces you to show:

```
[ 0:00 — 0:30 ] hook         | who's hurting + the punch
[ 0:30 — 1:15 ] problem      | concrete, narrow, specific
[ 1:15 — 2:45 ] solution     | walkthrough + demo clip
[ 2:45 — 3:00 ] ask          | one ask, one number
```

The middle 90 seconds are pure walkthrough: clicks, screen changes, results. The judge sees the product. We go deep on this in Week 6.

---

## 5. Why the demo URL is always a MUST

You will read this rule for the rest of the course and you will see why teams that ignore it lose:

> **The project must be reachable from a public URL at the time of judging.**

A localhost demo is not a demo. A "we did not have time to deploy" project is not a project. The deploy is part of the build, and on every event-day judging rubric, "publicly reachable" is the single biggest score multiplier you have.

This is why Week 2 (toolkit setup) puts so much weight on **the deploy target being live before you write feature code**. The pattern in C4 is:

1. Hour 1: deploy a *blank* page to your Vercel / Railway / Fly URL.
2. Hour 2: confirm the URL loads on someone else's phone.
3. Hour 3+: build features on top of the live URL, not on top of localhost.

Teams that follow this never have to scramble to deploy at hour 35. Teams that do not, do.

---

## 6. The 24-hour mid-event retro

At hour 24, you run a longer ceremony — about thirty minutes — that combines retro and re-planning. Three questions:

1. **What is working?** Name three things. Not "the team is great." Specific: "the API contract we drew in hour two has not changed once." "Pat's CSS pattern made the new screens take twenty minutes each."
2. **What is broken?** Name two things. Specific: "the deploy is taking nine minutes per push and that is killing our iteration speed." "We have two MUSTs still not started."
3. **What do we cut and what do we promote?** Apply the 12-hour rule again. Items move down the chart.

A retro at hour 24 is *not* a complaint session. It is a re-plan. The blameless-post-mortem voice applies: "the sprint board did not catch the API rate limit," not "Pat broke the rate limit."

> **C4 voice:** post-mortems are blameless, both at hour 24 and after the event. Always.

---

## 7. The final-3-hour freeze

In the last three hours, **the build is frozen**. No new features. No new dependencies. No new database tables. Bug fixes only, and only if they are visible in the demo path.

```
┌────────────────────────────────────────────────────────────┐
│  FINAL-3-HOUR FREEZE                                       │
│                                                            │
│  H-3:00  All MUSTs done. Build is frozen.                  │
│  H-3:00 → H-2:00  Demo rehearsal. Three full run-throughs. │
│  H-2:00 → H-1:30  Demo recording. Two takes minimum.       │
│  H-1:30 → H-1:00  Pitch rehearsal. Three run-throughs.     │
│  H-1:00 → H-0:30  Submission: Devpost form, repo polish,   │
│                   README rewrite, screenshot, demo link.   │
│  H-0:30 → H-0:00  Sleep / coffee / a moment of being human │
└────────────────────────────────────────────────────────────┘
```

If you cannot freeze the build at hour 33, it is because you did not cut at hour 12. The freeze is the consequence of the cut. Teams that do not cut do not get to freeze, and they ship a half-rehearsed pitch.

---

## 8. Worked example — the cut in practice

Imagine a team picks a hackathon prompt: *"build a tool that helps a small group of users coordinate something."* They draft the MoSCoW chart:

```
MUST   ✓ Login + profile
MUST   ✓ Create a group
MUST   ✓ Post a message to the group
MUST   ✓ Send email reminders
MUST   ✓ Public demo URL
SHOULD ▢ Search across messages
SHOULD ▢ Three-section landing page
COULD  ▢ Image upload
COULD  ▢ Light/dark theme
WON'T  ✗ Real-time chat
WON'T  ✗ Mobile app
```

At hour 12 the PM runs the rule. Status:

- Login + profile: **done**.
- Create a group: **done**.
- Post a message: **in flight, 80% complete**.
- Email reminders: **not started — requires SendGrid signup, the team has not done it**.
- Demo URL: **live with a placeholder page, not the real app**.

Remaining time: 24 hours. With a 30% buffer, executable work is 16.8 hours. The team has four items in flight: finish message-posting, do email reminders, wire the deploy to the real app, and at minimum two SHOULDs.

The PM cuts:

- **Email reminders** drops from MUST to WON'T. It was a MUST that did not produce a demo moment, and it required a new sponsor signup. Killing it returns four hours.
- **Search across messages** drops from SHOULD to WON'T. There is no demo time for it.
- **Image upload** stays in COULD but the PM verbally writes it off ("we are not going to do this").

New chart at hour 12:

```
MUST   ✓ Login + profile          [done]
MUST   ✓ Create a group           [done]
MUST   ✓ Post a message           [in flight]
MUST   ✓ Public demo URL          [in flight]
SHOULD ▢ Three-section landing    [not started]
WON'T  ✗ Email reminders          [cut at h-12]
WON'T  ✗ Search                   [cut at h-12]
WON'T  ✗ Image upload             [will not start]
WON'T  ✗ Real-time chat           [original]
WON'T  ✗ Mobile app               [original]
```

The team now ships. The demo is: "I sign in, I create a group, I post a message, you can see it on the live URL right now."

That demo wins. The five-MUST version did not get built.

---

## 9. Recap

- The cut reflex is the dominant skill. Scoping *out* matters more than scoping *in*.
- MoSCoW (Must, Should, Could, Won't) is the team's operating document, drawn at hour zero and updated hourly.
- The 12-hour rule: at hour 12, remaining scope ≤ remaining time × 0.7, or you cut.
- The 12-hour stand-up enforces the rule in fifteen minutes.
- The demo-or-die doctrine: if it does not appear in the demo, it does not exist. Every MUST must produce a 30-second demo moment.
- The demo URL is always a MUST. Always.
- The 24-hour mid-event retro is a blameless re-plan.
- The final-3-hour freeze: no new features, only rehearsal, recording, and submission.

You now have the discipline. The rest of the course gives you the toolkit (Week 2), the practice (Weeks 3–8), and the event itself (Week 10). Continue to [Exercise 1 — the personal brief](../03-exercises/exercise-01-personal-brief.md).

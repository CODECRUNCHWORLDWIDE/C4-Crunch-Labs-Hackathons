# Exercise 2 — Record the 90-Second Phone Demo

## Goal

Record and upload a 90-second phone demo of the team's hackathon project using the four-beat phone-demo arc from Lecture 1 §3. Upload to YouTube unlisted (or Loom public as a fallback). Paste the URL into the recruiter-grade README. The phone demo is the *recruiter-facing*, *consumed-on-a-phone* video — the third recording mode (after Week 8's screen-record and Week 9's mock pitch).

## Time-box

60–90 minutes including upload and link verification.

## Pre-flight

- A phone with a working camera and microphone.
- Landscape mode confirmed (the phone is in landscape orientation, not portrait — this is non-negotiable).
- A quiet space with even lighting (window-light at the speaker's face is the cheapest acceptable lighting).
- The project's demo URL is live and tested incognito.
- A second person to hold the phone (preferred) or a phone tripod / stack of books.
- A YouTube account (or a Loom account).

## Instructions

### Step 1 — Write the script (15 minutes)

Use the four-beat arc. Write the script as four labeled paragraphs in a text file.

```
Beat 1 — Problem (15 seconds, ~40 words spoken at moderate pace).

Beat 2 — Demo (50 seconds, voiceover narrating 2–3 user flows).

Beat 3 — Stack (15 seconds, ~40 words).

Beat 4 — Ask (10 seconds, ~25 words).
```

Rehearse the script aloud once. Time it with a stopwatch. If the total is over 95 seconds, prune. If under 80, you have skipped a beat; expand the demo narration.

### Step 2 — Prepare the title card (5 minutes)

Open Canva, Figma, or any image editor. Create a 1920×1080 image (landscape, 16:9) with:

- Project name (large, top-center or top-left).
- Team initials or team name (subtitle).
- Hackathon name and date (smaller, below).
- Optional: project tagline (one line).

Save as `title-card.png`. The first 5 seconds of the video display this card; the speaker can be visible behind or beside the card or layered over it.

### Step 3 — Record Beat 1 (Problem, 15 seconds)

Speaker on camera. Landscape. Title card visible top-left or top-center on screen (overlay via the phone's photo-overlay app, or via a printed sheet held next to the speaker, or via post-production).

Speaker faces camera and delivers Beat 1 in one take. Record 3 takes; pick the best.

### Step 4 — Record Beat 2 (Demo, 50 seconds)

Two options:

- **Option A — Phone screen-share.** Use the phone's built-in screen recorder. Open the demo URL on the phone, narrate over the screen recording. Best for mobile-friendly projects.
- **Option B — Laptop screen filmed by phone.** Sit the phone on a tripod or book-stack pointing at the laptop screen. Demo on the laptop, narrate aloud, phone records both the screen and the voice. Best for desktop-first projects.

Record 2 takes; pick the cleaner one. Aim for the demo narration to cover *two to three* user flows in 50 seconds — not a full feature tour.

### Step 5 — Record Beat 3 (Stack) and Beat 4 (Ask)

Speaker back on camera. Landscape. Deliver Beats 3 and 4 in one continuous take (25 seconds total). Record 3 takes; pick the best.

### Step 6 — Stitch (15 minutes)

Use a free editor: iMovie (Mac), CapCut (cross-platform), DaVinci Resolve (cross-platform, more advanced). Stitch in this order:

1. Title-card hold for 0–5 seconds (with Beat 1 audio starting at 0:00).
2. Beat 1 (speaker on camera) for 5–15 seconds.
3. Beat 2 (screen recording with voiceover) for 15–65 seconds.
4. Beat 3 (speaker on camera) for 65–80 seconds.
5. Beat 4 (speaker on camera) for 80–90 seconds.

No background music. No animated transitions (hard cut between segments is fine). No b-roll. Captioned title card stays in the top-left or top-center corner for the first 5 seconds and re-appears for the last 3 seconds (with the repo URL displayed).

### Step 7 — Upload (10 minutes)

**YouTube (preferred).** Sign in. Upload. Set visibility to *Unlisted*. Title: `<Project Name> — 90-second demo` (no all-caps; no clickbait). Description: paste the recruiter-grade README problem statement plus the repo URL. Save the watch URL.

**Loom (fallback).** Sign in. Upload. Set visibility to *Public*. Use the same title and description. Save the watch URL.

### Step 8 — Embed in the README

Update `README-FOR-RECRUITERS.md` Section 2 (Demo) with the watch URL. Update the title-card screenshot path to point at `./docs/screenshots/title-card.png` (export a frame from the video; PNG; commit alongside the other screenshots).

### Step 9 — Verify

Open the YouTube/Loom URL in an *incognito tab* on a phone. Confirm:

- The video plays without sign-in.
- The title card is readable on a phone screen (not too small).
- The audio is intelligible at 50% phone volume.
- The video is exactly between 85 and 95 seconds long.

## Acceptance criteria

- [ ] Video is between 85 and 95 seconds long.
- [ ] Recorded in landscape orientation.
- [ ] Title card displays in the first 5 seconds (project name, team, hackathon, date).
- [ ] Speaker is on camera for Beats 1, 3, and 4.
- [ ] Demo narration covers 2–3 user flows in Beat 2.
- [ ] No background music, no b-roll, no animated transitions.
- [ ] Uploaded to YouTube unlisted or Loom public.
- [ ] URL plays in an incognito tab without sign-in.
- [ ] URL embedded in `README-FOR-RECRUITERS.md` Section 2.
- [ ] Title-card frame saved as `./docs/screenshots/title-card.png`.

## Common pitfalls

- **Portrait orientation.** Phone is held vertically. The video crops badly in every embed. Re-record in landscape.
- **Live-coding in the demo.** Beat 2 is *pre-recorded screen* narrated *over* — not a live typing session. The typo-cascade failure mode from Week 9 §3 applies here too.
- **No human face in the video.** Screen-record-only videos read as anonymous. Beats 1, 3, 4 require a face on camera.
- **Background music drowning the voice.** Either skip the music or set it at 5–10% of the voice volume. The C4 default is no music.
- **Uploaded to Google Drive only.** Drive links rotate access and require sign-in. Not acceptable; re-upload to YouTube unlisted.
- **Over-90-second cut.** The 90-second cap is the binding constraint. Prune ruthlessly.

## Submission

The URL is the deliverable. Commit it into `README-FOR-RECRUITERS.md` and note the URL in `POST-EVENT-LOG.md` Day 3.

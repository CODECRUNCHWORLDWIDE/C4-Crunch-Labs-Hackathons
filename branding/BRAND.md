# C4 · Crunch Labs Hackathons — Brand Guide

> **Voice:** team-room, late-night, scope-discipline-first. The voice of a team lead who has shipped at a hackathon and learned what *not* to do at the next one.
> **Feel:** sprint-board, sticky-note, energy without exclamation marks.

Extends the family brand. C4-specific overrides only.

---

## Identity

- **Full name:** Crunch Labs — Hackathons
- **Program code:** C4
- **Full title in copy:** *C4 · Crunch Labs Hackathons*
- **Tagline (short):** Ship at the hackathon. Then ship better at the next one.
- **Tagline (long):** A free, open-source ten-week prep cycle for hackathons — Agile mechanics, full-stack rapid prototyping, scoping discipline, pitch craft — plus a permanent archive of past Code Crunch events.
- **Canonical URL:** `codecrunchglobal.vercel.app/course-c4-hackathons`
- **License:** GPL-3.0

---

## Where C4 diverges from the family palette

Inherits Ink/Parchment/Gold. Adds **Sprint Coral** — the color of a fresh sticky note on a sprint board:

| Role | Name | Hex | Use |
|------|------|-----|-----|
| Accent | Sprint Coral | `#F97316` | The C4 mark, "must-ship" scope tags, sprint indicators |
| Accent deep | Sprint Coral deep | `#9A3412` | Hover, eyebrows |
| Accent soft | Sprint Coral soft | `#FED7AA` | Subtle background of "in progress" cards |

```css
:root {
  --sprint-coral:       #F97316;
  --sprint-coral-deep:  #9A3412;
  --sprint-coral-soft:  #FED7AA;
}
```

> **Why Coral over a flatter orange:** the brand needs a color that reads as *team energy without burning out the reader.* Sprint Coral is warm enough to feel alive at 2 AM in a hacker room without screaming.

### Typography

EB Garamond display, Lora body, JetBrains Mono for any commit hash, slack handle, sprint number, or deploy URL.

---

## Recurring page elements

### The scoping chart (MoSCoW)

C4's signature deliverable on every event-prep brief:

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

The **WON'T** list is the most important line. C4 voice teaches that scoping out is the dominant skill.

### The "demo timing" strip

Every pitch lecture renders the three-minute demo as a banded strip:

```
[ 0:00 — 0:30 ] hook         | who's hurting + the punch
[ 0:30 — 1:15 ] problem      | concrete, narrow, specific
[ 1:15 — 2:45 ] solution     | walkthrough + demo clip
[ 2:45 — 3:00 ] ask          | one ask, one number
```

Mono. Strict. Three minutes is three minutes.

---

## Voice rules

- **The win is shipping, not innovating.** Most hackathon judging weights "did it work in 36 hours" higher than "is it conceptually novel."
- **Credit teammates by name (with permission).** Always.
- **Cite sponsors only when germane.** Sponsor APIs that were genuinely useful, yes. "Powered by SponsorCorp" decoration, no.
- **No "rockstar" / "ninja" / "10x."** Even at a hackathon. Especially at a hackathon.
- **Post-mortems are blameless.** "The sprint board didn't catch the API rate limit" — not "Pat broke the rate limit."

---

## Course page conventions

The course page for C4 uses a stylized sprint-board hero — three Sprint Coral cards in a row labeled "Today / In Review / Done." The 10-week prep cycle is rendered as a countdown to "Event Day." The archive section appears in chronological reverse, each event as a small editorial-style card.

---

*GPL-3.0. Fork freely.*

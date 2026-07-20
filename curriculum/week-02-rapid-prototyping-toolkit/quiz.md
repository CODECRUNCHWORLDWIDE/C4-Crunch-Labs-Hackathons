# Week 2 — Quiz

Ten multiple-choice questions. Take it with your lecture notes closed. Aim for 9/10 before moving to Week 3. Answer key at the bottom — do not peek.

---

**Q1.** The "boring stack doctrine" in C4 says:

- A) Use the oldest framework available so that nothing is novel.
- B) Pick the technology your team has already shipped with; never the one you read about last week.
- C) Pick the stack with the most GitHub stars.
- D) Pick whichever sponsor's stack is best advertised at the event.

---

**Q2.** The C4 default stack is:

- A) Next.js + tRPC + Prisma + NextAuth + Vercel.
- B) React (Vite) + Tailwind + shadcn/ui + react-query + FastAPI + SQLite/Supabase + Vercel + Railway.
- C) Django + HTMX + Postgres + Fly.io.
- D) SvelteKit + Drizzle + Cloudflare Workers.

---

**Q3.** The **30-minute scaffold-to-first-route rule** says:

- A) The team should sleep for 30 minutes every hour.
- B) From `git clone` of your `hackathon-template` to a live deploy URL returning a real HTTP response, total elapsed time should be ≤ 30 minutes.
- C) The first feature must ship in 30 minutes.
- D) The pitch lead must finish the script 30 minutes before the deadline.

---

**Q4.** A teammate at hour 2 suggests, "let's swap our backend to [unfamiliar framework] — it'd be perfect for this." According to Lecture 1, the C4-voice response is:

- A) "Sure, the team that learns the most wins."
- B) "Cool — let's bookmark it for the post-mortem. For this event, we ship in the boring stack and we use the time we saved on rehearsal."
- C) "Veto. Stop suggesting things."
- D) "Only if you can prove it is faster in the next 15 minutes."

---

**Q5.** Why is `.env.example` committed but `.env` is *not*?

- A) `.env` files are too large to fit in a Git repo.
- B) `.env.example` names every env var your code reads, with placeholders; `.env` contains real secrets and stays local.
- C) GitHub only allows `.example` files in public repos.
- D) The two files are functionally identical; you can commit either.

---

**Q6.** Which of the following is **not** something `bootstrap.sh` is allowed to do, according to Lecture 2?

- A) Rename project strings in `README.md`, `package.json`, `pyproject.toml`.
- B) Reset Git history with `rm -rf .git && git init`.
- C) Install dependencies via `pnpm install` and `pip install`.
- D) Phone home to an analytics endpoint.

---

**Q7.** The template's README has a line "Last measured spin-up: 22 minutes." What is the purpose of this line?

- A) Marketing — to show off in the GitHub README.
- B) An honest scoreboard against the 30-minute rule, useful for catching template rot over time.
- C) A legal requirement for open-source projects.
- D) Vercel uses it to estimate build time.

---

**Q8.** When you switch the React app's API host from `localhost:8000` to the deployed Railway URL, you do it by:

- A) Hard-coding the URL in `App.tsx`.
- B) Reading from `VITE_API_URL` and setting it in Vercel's environment variables.
- C) Pushing the change to GitHub Actions secrets.
- D) Editing the `vercel.json` file in production.

---

**Q9.** In the **default Code Crunch stack**, the recommended order for choosing a database is:

- A) Supabase free first, fall back to SQLite if Supabase is down.
- B) SQLite for the first 12 hours; Supabase Postgres free only if you need to scale demo data.
- C) Always Postgres on Railway from hour zero.
- D) MongoDB Atlas free tier.

---

**Q10.** Which is the **most accurate** statement about the version log at the bottom of your `hackathon-template` README?

- A) It is a marketing artifact, listing every cool feature added.
- B) Each row is a real-world friction the template hit at a past event, with a one-sentence fix that future-events benefit from.
- C) It must follow semantic versioning rules.
- D) It is optional and most teams skip it.

---

## Answer key

<details>
<summary>Click to reveal answers</summary>

1. **B** — The team that has already shipped wins. The "exciting" stack is the one your teammate proposes at hour 2 after reading a blog post. (Lecture 1, §1)
2. **B** — React + Vite + Tailwind + shadcn/ui + react-query + FastAPI + SQLite/Supabase + Vercel + Railway. (Lecture 1, §2)
3. **B** — From `git clone` to a live deploy URL returning a real HTTP response: ≤ 30 minutes total elapsed. (Lecture 1, §5)
4. **B** — Validate the curiosity, defer it, re-anchor on the win. Three sentences. (Lecture 1, §4)
5. **B** — `.env.example` is exhaustive and committed; `.env` is local and never committed. The crime is committing `.env`. (Lecture 1, §7; Lecture 2, §4.2)
6. **D** — Phone home. Hostile-network paranoia applies to hackathon Wi-Fi. The bootstrap script must be transparent and local-only. (Lecture 2, §5.2)
7. **B** — Honest scoreboard. If the number drifts up over time, the template has rotted. (Lecture 2, §3 + §7)
8. **B** — Env var (`VITE_API_URL`) read from Vercel's environment variables. `VITE_*` is the Vite convention; the value bakes at build time. (Lecture 1, §7; Exercise 3, §5)
9. **B** — SQLite first, Supabase only if you need to scale demo data. SQLite is a file; nothing to configure. (Lecture 1, §2.1)
10. **B** — Real-world friction with a one-sentence fix per row. The point is that the next event reads it and benefits. (Lecture 2, §6.2)

</details>

---

If you scored under 7, re-read the lecture sections referenced in the answers. If you scored 9 or 10, you are ready for the [homework](./homework.md).

"""pitch_timer.py — a small CLI timer for the 3-minute pitch arc.

Companion script for Exercise 2 of Week 9 (C4 Crunch Labs Hackathons).
Counts down the four beats (30s / 90s / 45s / 15s) of the 30-90-45-15
arc and prints a single line per beat boundary. No external packages
required; runs on a stock Python 3.10+ install.

Usage:
    python3 pitch_timer.py              # uses the default beats
    python3 pitch_timer.py --dry-run    # prints the beats without sleeping

The script is intended for rehearsal, not for use in the actual
judging room. Use a phone timer in the judging room; the script is
the bench, not the run.
"""
from __future__ import annotations

import argparse
import sys
import time
from typing import NamedTuple


class Beat(NamedTuple):
    """A single beat of the pitch arc."""

    name: str
    duration_seconds: int
    cue: str


# The C4 default arc — 30/90/45/15 seconds across four beats.
DEFAULT_BEATS: list[Beat] = [
    Beat(name="PROBLEM", duration_seconds=30, cue="name the user, pain, verb"),
    Beat(name="DEMO", duration_seconds=90, cue="show the build against the live URL"),
    Beat(name="TECH", duration_seconds=45, cue="one decision, one trade-off"),
    Beat(name="ASK", duration_seconds=15, cue="one ask, then stop talking"),
]


def total_seconds(beats: list[Beat]) -> int:
    """Return the total duration of the arc in seconds."""
    return sum(beat.duration_seconds for beat in beats)


def format_seconds(seconds: int) -> str:
    """Format a seconds count as M:SS."""
    minutes, secs = divmod(seconds, 60)
    return f"{minutes}:{secs:02d}"


def run_timer(beats: list[Beat], dry_run: bool = False) -> int:
    """Run the timer over the provided beats.

    If dry_run is True, the function prints the beat schedule without
    sleeping. Useful for testing the beats and for fast iteration.

    Returns 0 on success.
    """
    cumulative_seconds = 0
    total = total_seconds(beats)
    print(f"Pitch arc total: {format_seconds(total)} ({total} seconds)")
    print(f"Beats: {len(beats)}")
    print("-" * 60)
    for index, beat in enumerate(beats, start=1):
        start_mark = format_seconds(cumulative_seconds)
        end_mark = format_seconds(cumulative_seconds + beat.duration_seconds)
        print(
            f"[{start_mark} - {end_mark}] Beat {index}/{len(beats)}: "
            f"{beat.name} ({beat.duration_seconds}s) — cue: {beat.cue}"
        )
        if not dry_run:
            time.sleep(beat.duration_seconds)
        cumulative_seconds += beat.duration_seconds
    print("-" * 60)
    print(f"Pitch complete at {format_seconds(cumulative_seconds)}.")
    print("Stop talking; let the silence land for ~3 seconds.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Time the 30-90-45-15 pitch arc."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the beat schedule without sleeping.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    """Entry point."""
    args = parse_args(argv)
    return run_timer(DEFAULT_BEATS, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

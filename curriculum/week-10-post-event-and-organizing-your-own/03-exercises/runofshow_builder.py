"""C4 Week 10 — Run-of-Show Builder for a One-Day Campus Hackathon.

A small CLI that prints a minute-by-minute run-of-show for a one-day campus
hackathon, parameterised by doors-open time and the duration of the hacking
window. Output is a table of segments with start, end, duration, and named
staffing.

Usage:
    python3 runofshow_builder.py
    python3 runofshow_builder.py --doors-open 09:00 --hacking-hours 8

The segment template follows Lecture 3 section 5. Adjust the constants
below to fit your specific event; verify the schedule with your venue
contact at the venue walkthrough (1 week out).
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Segment:
    """A single segment of the day-of run-of-show."""

    name: str
    duration_minutes: int
    staffing: str


# Named C4 default segments for a one-day campus hackathon.
# These come from Lecture 3 section 5. Durations are minutes.
DEFAULT_PRE_HACKING_SEGMENTS: list[Segment] = [
    Segment(
        name="Organisers arrive, venue setup",
        duration_minutes=60,
        staffing="All organisers",
    ),
    Segment(
        name="Sponsor table setup, judge tech check",
        duration_minutes=30,
        staffing="Logistics + outreach leads",
    ),
    Segment(
        name="Doors open, attendee check-in, breakfast",
        duration_minutes=30,
        staffing="2 check-in volunteers + breakfast volunteer",
    ),
    Segment(
        name="Opening ceremony (welcome + CoC + theme + judging + sponsors)",
        duration_minutes=45,
        staffing="Lead organiser on mic",
    ),
    Segment(
        name="Team formation (for attendees without a team)",
        duration_minutes=30,
        staffing="Programming lead facilitates",
    ),
]

DEFAULT_POST_HACKING_SEGMENTS: list[Segment] = [
    Segment(
        name="Submissions close",
        duration_minutes=0,
        staffing="Lead organiser closes the submission form",
    ),
    Segment(
        name="Demo prep + judging room setup",
        duration_minutes=30,
        staffing="Logistics lead",
    ),
    Segment(
        name="Judging window (table-walk format)",
        duration_minutes=90,
        staffing="Judges + lead organiser timekeeps",
    ),
    Segment(
        name="Judges deliberate + closing-ceremony setup",
        duration_minutes=30,
        staffing="Judges in private room",
    ),
    Segment(
        name="Closing ceremony (winners + thank-yous + photo)",
        duration_minutes=45,
        staffing="Lead organiser on mic",
    ),
    Segment(
        name="Attendee farewell + venue teardown",
        duration_minutes=45,
        staffing="All organisers + volunteers",
    ),
    Segment(
        name="Organisers' debrief over food",
        duration_minutes=60,
        staffing="All organisers",
    ),
]


def parse_time(timestr: str) -> datetime:
    """Parse a HH:MM string to a datetime on a placeholder date."""
    return datetime.strptime(timestr, "%H:%M")


def fmt_time(dt: datetime) -> str:
    """Format a datetime to HH:MM."""
    return dt.strftime("%H:%M")


def build_hacking_block_segments(hacking_hours: float) -> list[Segment]:
    """Split the hacking window into block 1, lunch, block 2, snacks, block 3.

    Allocates roughly: 30 percent to block 1, 45 percent to block 2 (which is
    split by snacks), 25 percent to block 3. Lunch is a fixed 60 minutes.
    """
    total_minutes = int(hacking_hours * 60)
    lunch_minutes = 60
    snack_minutes = 30
    block_minutes = total_minutes - lunch_minutes - snack_minutes
    if block_minutes <= 60:
        # Tiny hacking window — collapse to single block.
        return [
            Segment(
                name="Hacking block (single block)",
                duration_minutes=block_minutes + snack_minutes,
                staffing="All organisers floor-walk",
            ),
            Segment(
                name="Lunch",
                duration_minutes=lunch_minutes,
                staffing="Food volunteer",
            ),
        ]
    block_one = int(block_minutes * 0.28)
    block_three = int(block_minutes * 0.24)
    block_two = block_minutes - block_one - block_three
    return [
        Segment(
            name="Hacking block 1",
            duration_minutes=block_one,
            staffing="All organisers floor-walk",
        ),
        Segment(
            name="Lunch",
            duration_minutes=lunch_minutes,
            staffing="Food volunteer",
        ),
        Segment(
            name="Hacking block 2",
            duration_minutes=block_two,
            staffing="All organisers floor-walk",
        ),
        Segment(
            name="Afternoon snacks (concurrent with end of block 2)",
            duration_minutes=snack_minutes,
            staffing="Food volunteer",
        ),
        Segment(
            name="Hacking block 3 (sprint to submission)",
            duration_minutes=block_three,
            staffing="All organisers floor-walk",
        ),
    ]


def build_run_of_show(
    doors_open: str,
    hacking_hours: float,
) -> list[tuple[Segment, datetime, datetime]]:
    """Build the full run-of-show with start and end times for each segment."""
    # Setup time is before doors open.
    setup_minutes = sum(
        seg.duration_minutes for seg in DEFAULT_PRE_HACKING_SEGMENTS[:2]
    )
    cursor = parse_time(doors_open) - timedelta(minutes=setup_minutes)

    schedule: list[tuple[Segment, datetime, datetime]] = []
    all_segments = (
        DEFAULT_PRE_HACKING_SEGMENTS
        + build_hacking_block_segments(hacking_hours=hacking_hours)
        + DEFAULT_POST_HACKING_SEGMENTS
    )
    for segment in all_segments:
        start = cursor
        end = cursor + timedelta(minutes=segment.duration_minutes)
        schedule.append((segment, start, end))
        cursor = end
    return schedule


def print_run_of_show(
    schedule: list[tuple[Segment, datetime, datetime]],
) -> None:
    """Print the run-of-show as a table."""
    print()
    header = (
        f"{'Segment':<60} {'Start':>6} {'End':>6} "
        f"{'Mins':>5}  {'Staffing'}"
    )
    print(header)
    print("-" * (len(header) + 8))
    for segment, start, end in schedule:
        print(
            f"{segment.name:<60} "
            f"{fmt_time(start):>6} "
            f"{fmt_time(end):>6} "
            f"{segment.duration_minutes:>5}  "
            f"{segment.staffing}"
        )
    print()


def parse_args() -> argparse.Namespace:
    """Parse the CLI arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "C4 Week 10 run-of-show builder for a one-day campus hackathon."
        ),
    )
    parser.add_argument(
        "--doors-open",
        type=str,
        default="09:00",
        help="Doors-open time in HH:MM 24-hour format (default: 09:00).",
    )
    parser.add_argument(
        "--hacking-hours",
        type=float,
        default=7.0,
        help=(
            "Length of the hacking window in hours, including lunch and "
            "snacks (default: 7.0)."
        ),
    )
    return parser.parse_args()


def main() -> None:
    """CLI entry point."""
    args = parse_args()
    schedule = build_run_of_show(
        doors_open=args.doors_open,
        hacking_hours=args.hacking_hours,
    )
    print()
    print(
        f"Run-of-show — doors open {args.doors_open}, "
        f"{args.hacking_hours} hours of hacking."
    )
    print_run_of_show(schedule=schedule)


if __name__ == "__main__":
    main()

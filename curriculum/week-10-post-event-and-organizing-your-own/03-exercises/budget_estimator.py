"""C4 Week 10 — Budget Estimator for a Student-Run Hackathon.

A small CLI that estimates a hackathon budget from attendee count, event
length, and tier choices. Outputs a per-line-item breakdown and a total.

Usage:
    python3 budget_estimator.py
    python3 budget_estimator.py --attendees 80 --event-length one-day \\
        --mlh-tier local --swag-budget 5

The numbers are based on the named C4 ranges from Lecture 2 (food per
attendee per meal, swag per attendee, prize-pool ranges) in 2026 US dollars.
Recalibrate the constants below every two years against local pricing.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


# Named C4 constants — 2026 US dollars.
FOOD_PER_ATTENDEE_PER_MEAL_LOW: float = 8.0
FOOD_PER_ATTENDEE_PER_MEAL_HIGH: float = 12.0

MEALS_ONE_DAY: int = 2   # breakfast + lunch, snacks bundled
MEALS_TWENTY_FOUR_HOUR: int = 4  # breakfast, lunch, dinner, late-night

SWAG_PER_ATTENDEE_LOW: float = 5.0
SWAG_PER_ATTENDEE_HIGH: float = 15.0

PRIZE_POOL_SMALL_LOW: float = 500.0
PRIZE_POOL_SMALL_HIGH: float = 2000.0
PRIZE_POOL_MEDIUM_LOW: float = 2000.0
PRIZE_POOL_MEDIUM_HIGH: float = 5000.0

AV_RENTAL_FLAT: float = 300.0
SIGNAGE_FLAT: float = 150.0
INSURANCE_THIRD_PARTY_FLOOR: float = 200.0
INSURANCE_THIRD_PARTY_CEILING: float = 800.0

MLH_TIER_COSTS: dict[str, tuple[float, float]] = {
    "local": (0.0, 0.0),
    "member": (500.0, 1500.0),
    "premier": (2500.0, 5000.0),
    "none": (0.0, 0.0),
}


@dataclass
class BudgetLine:
    """A single line item in the budget."""

    name: str
    low: float
    high: float

    @property
    def midpoint(self) -> float:
        return (self.low + self.high) / 2.0


def estimate_food(attendees: int, event_length: str) -> BudgetLine:
    """Estimate the food line for the event."""
    if event_length == "one-day":
        meals = MEALS_ONE_DAY
    elif event_length == "twenty-four-hour":
        meals = MEALS_TWENTY_FOUR_HOUR
    else:
        raise ValueError(f"unknown event_length: {event_length!r}")

    low = attendees * meals * FOOD_PER_ATTENDEE_PER_MEAL_LOW
    high = attendees * meals * FOOD_PER_ATTENDEE_PER_MEAL_HIGH
    return BudgetLine(name="Food", low=low, high=high)


def estimate_swag(attendees: int, swag_per_attendee: float) -> BudgetLine:
    """Estimate the swag line for the event."""
    if swag_per_attendee < SWAG_PER_ATTENDEE_LOW:
        low = high = attendees * swag_per_attendee
    else:
        low = attendees * SWAG_PER_ATTENDEE_LOW
        high = attendees * max(swag_per_attendee, SWAG_PER_ATTENDEE_HIGH)
    return BudgetLine(name="Swag", low=low, high=high)


def estimate_prize_pool(attendees: int) -> BudgetLine:
    """Estimate the prize-pool line for the event based on attendee count."""
    if attendees < 60:
        return BudgetLine(
            name="Prize pool",
            low=PRIZE_POOL_SMALL_LOW,
            high=PRIZE_POOL_SMALL_HIGH,
        )
    return BudgetLine(
        name="Prize pool",
        low=PRIZE_POOL_MEDIUM_LOW,
        high=PRIZE_POOL_MEDIUM_HIGH,
    )


def estimate_mlh(tier: str) -> BudgetLine:
    """Estimate the MLH membership line for the event."""
    if tier not in MLH_TIER_COSTS:
        raise ValueError(f"unknown MLH tier: {tier!r}")
    low, high = MLH_TIER_COSTS[tier]
    return BudgetLine(name=f"MLH membership ({tier})", low=low, high=high)


def estimate_insurance(option: str) -> BudgetLine:
    """Estimate the insurance line for the event."""
    if option == "university":
        return BudgetLine(name="Insurance (university-provided)", low=0.0, high=0.0)
    if option == "mlh":
        return BudgetLine(name="Insurance (MLH-provided)", low=0.0, high=0.0)
    if option == "third-party":
        return BudgetLine(
            name="Insurance (third-party policy)",
            low=INSURANCE_THIRD_PARTY_FLOOR,
            high=INSURANCE_THIRD_PARTY_CEILING,
        )
    raise ValueError(f"unknown insurance option: {option!r}")


def estimate_av_and_signage() -> list[BudgetLine]:
    """Estimate AV rental and signage flat lines."""
    return [
        BudgetLine(name="AV rental", low=AV_RENTAL_FLAT, high=AV_RENTAL_FLAT),
        BudgetLine(name="Signage and printing", low=SIGNAGE_FLAT, high=SIGNAGE_FLAT),
    ]


def build_budget(
    attendees: int,
    event_length: str,
    mlh_tier: str,
    insurance: str,
    swag_per_attendee: float,
) -> list[BudgetLine]:
    """Build the full list of budget lines."""
    lines: list[BudgetLine] = []
    lines.append(estimate_food(attendees=attendees, event_length=event_length))
    lines.append(estimate_swag(attendees=attendees, swag_per_attendee=swag_per_attendee))
    lines.append(estimate_prize_pool(attendees=attendees))
    lines.append(estimate_mlh(tier=mlh_tier))
    lines.append(estimate_insurance(option=insurance))
    lines.extend(estimate_av_and_signage())
    return lines


def print_budget(lines: list[BudgetLine]) -> None:
    """Print the budget table to stdout."""
    print()
    print(f"{'Line item':<40} {'Low ($)':>12} {'High ($)':>12} {'Mid ($)':>12}")
    print("-" * 80)
    total_low = 0.0
    total_high = 0.0
    for line in lines:
        print(
            f"{line.name:<40} "
            f"{line.low:>12,.0f} "
            f"{line.high:>12,.0f} "
            f"{line.midpoint:>12,.0f}"
        )
        total_low += line.low
        total_high += line.high
    print("-" * 80)
    total_mid = (total_low + total_high) / 2.0
    print(
        f"{'TOTAL':<40} "
        f"{total_low:>12,.0f} "
        f"{total_high:>12,.0f} "
        f"{total_mid:>12,.0f}"
    )
    print()
    print("Reminder: numbers are 2026 USD ranges; recalibrate every 2 years.")
    print("Sponsorship offsets this total; see Exercise 3 + the sponsorship deck.")
    print()


def parse_args() -> argparse.Namespace:
    """Parse the CLI arguments."""
    parser = argparse.ArgumentParser(
        description="C4 Week 10 budget estimator for a student-run hackathon.",
    )
    parser.add_argument(
        "--attendees",
        type=int,
        default=80,
        help="Total expected attendees (default: 80).",
    )
    parser.add_argument(
        "--event-length",
        type=str,
        choices=["one-day", "twenty-four-hour"],
        default="one-day",
        help="Event duration (default: one-day).",
    )
    parser.add_argument(
        "--mlh-tier",
        type=str,
        choices=["none", "local", "member", "premier"],
        default="local",
        help="MLH membership tier (default: local).",
    )
    parser.add_argument(
        "--insurance",
        type=str,
        choices=["university", "mlh", "third-party"],
        default="university",
        help="Insurance option (default: university).",
    )
    parser.add_argument(
        "--swag-budget",
        type=float,
        default=8.0,
        help="Swag spend per attendee in USD (default: 8.0).",
    )
    return parser.parse_args()


def main() -> None:
    """CLI entry point."""
    args = parse_args()
    lines = build_budget(
        attendees=args.attendees,
        event_length=args.event_length,
        mlh_tier=args.mlh_tier,
        insurance=args.insurance,
        swag_per_attendee=args.swag_budget,
    )
    print()
    print(
        f"Budget estimate — {args.attendees} attendees, "
        f"{args.event_length} event, MLH {args.mlh_tier}, "
        f"insurance via {args.insurance}."
    )
    print_budget(lines=lines)


if __name__ == "__main__":
    main()

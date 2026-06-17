"""rubric_score.py — compute a weighted rubric score from a JSON input.

Companion script for Exercise 1 of Week 9 (C4 Crunch Labs Hackathons).
Reads a JSON file describing the five C4 rubric dimensions and prints
a one-line summary per dimension plus a weighted total.

Usage:
    python3 rubric_score.py rubric_input.json

Exit code 0 if every dimension has a score in the 1-5 range; exit
code 1 if any dimension's score is out of range. The JSON shape:

    {
      "dimensions": [
        {"name": "Technical Complexity", "score": 3, "weight": 0.25,
         "evidence": "one-line cite"},
        ...
      ]
    }

Weights are floats summing to 1.0. The script validates the sum to
within ±0.01 tolerance. No external packages required; runs on a
stock Python 3.10+ install.
"""
from __future__ import annotations

import json
import sys
from typing import TypedDict


class Dimension(TypedDict):
    """One dimension entry in the rubric input file."""

    name: str
    score: int
    weight: float
    evidence: str


class RubricInput(TypedDict):
    """The full rubric input file."""

    dimensions: list[Dimension]


WEIGHT_TOLERANCE: float = 0.01
SCORE_MIN: int = 1
SCORE_MAX: int = 5


def load_rubric(path: str) -> RubricInput:
    """Load the rubric input JSON from `path`."""
    with open(path, "r", encoding="utf-8") as handle:
        data: RubricInput = json.load(handle)
    return data


def validate_scores(dimensions: list[Dimension]) -> list[str]:
    """Return a list of validation error strings (empty if all OK)."""
    errors: list[str] = []
    for dimension in dimensions:
        score = dimension["score"]
        if score < SCORE_MIN or score > SCORE_MAX:
            errors.append(
                f"Dimension '{dimension['name']}' has score {score}, "
                f"outside the {SCORE_MIN}-{SCORE_MAX} range."
            )
    return errors


def validate_weights(dimensions: list[Dimension]) -> list[str]:
    """Return a list of weight-validation errors (empty if OK)."""
    errors: list[str] = []
    total_weight = sum(dimension["weight"] for dimension in dimensions)
    if abs(total_weight - 1.0) > WEIGHT_TOLERANCE:
        errors.append(
            f"Dimension weights sum to {total_weight:.3f}, "
            f"expected 1.000 ± {WEIGHT_TOLERANCE:.3f}."
        )
    return errors


def weighted_total(dimensions: list[Dimension]) -> float:
    """Compute the weighted total of all dimension scores."""
    return sum(d["score"] * d["weight"] for d in dimensions)


def format_dimension_line(dimension: Dimension) -> str:
    """Format a single dimension as a one-line summary."""
    return (
        f"  {dimension['name']:<24} "
        f"score: {dimension['score']}/{SCORE_MAX} "
        f"weight: {dimension['weight']:.2f} "
        f"evidence: {dimension['evidence']}"
    )


def main(path: str) -> int:
    """Run the scorer on the file at `path`. Return exit code."""
    data = load_rubric(path)
    dimensions = data["dimensions"]
    print(f"Loaded {len(dimensions)} dimension(s) from {path}")
    print("-" * 60)
    for dimension in dimensions:
        print(format_dimension_line(dimension))
    print("-" * 60)
    score_errors = validate_scores(dimensions)
    weight_errors = validate_weights(dimensions)
    if score_errors or weight_errors:
        print("Validation errors:")
        for err in score_errors + weight_errors:
            print(f"  - {err}")
        return 1
    total = weighted_total(dimensions)
    print(f"Weighted total: {total:.2f} (out of {SCORE_MAX}.00)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 rubric_score.py rubric_input.json")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))

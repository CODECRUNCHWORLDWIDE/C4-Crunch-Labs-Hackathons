"""pr_sizer.py — flag PRs over the team's line-count cap.

Companion script for Exercise 2 of Week 8 (C4 Crunch Labs Hackathons).
Reads a JSON file describing open PRs and prints one line per PR
flagged OK or OVER against a team-defined line cap (default 200).

Usage:
    python3 pr_sizer.py pr_metadata.json

Exit code 0 if every PR is at or under the cap; exit code 1 if any
PR is over the cap. The exit code lets a team add this script to a
pre-stand-up check or a CI hook with minimum plumbing.
"""
import json
import sys
from typing import TypedDict


class PRMetadata(TypedDict):
    id: int
    branch: str
    author: str
    lines: int


class InputFile(TypedDict):
    prs: list[PRMetadata]
    cap: int


def load_metadata(path: str) -> InputFile:
    """Load the JSON file describing open PRs and the cap."""
    with open(path, "r", encoding="utf-8") as handle:
        data: InputFile = json.load(handle)
    return data


def flag_pr(pr: PRMetadata, cap: int) -> str:
    """Return a one-line flag string for the given PR."""
    status = "OVER" if pr["lines"] > cap else "OK"
    return (
        f"PR #{pr['id']} ({pr['branch']}, {pr['author']}, "
        f"{pr['lines']} lines): {status}"
    )


def count_over(prs: list[PRMetadata], cap: int) -> int:
    """Count how many PRs are over the cap."""
    return sum(1 for pr in prs if pr["lines"] > cap)


def main(path: str) -> int:
    """Run the sizer on the file at `path`. Return exit code."""
    data = load_metadata(path)
    cap = data["cap"]
    for pr in data["prs"]:
        print(flag_pr(pr, cap))
    over_count = count_over(data["prs"], cap)
    print(f"\nSummary: {over_count} PR(s) over the {cap}-line cap.")
    return 0 if over_count == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pr_sizer.py pr_metadata.json")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))

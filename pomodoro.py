#!/usr/bin/env python3
"""Simple command-line Pomodoro timer."""

import time
import argparse


def run_timer(minutes: float, label: str) -> None:
    """Run a countdown timer for ``minutes`` and print updates.

    Args:
        minutes: Duration of timer in minutes.
        label: Description of the timer phase.
    """
    total_seconds = int(minutes * 60)
    print(f"\nStarting {label} for {minutes} minutes")
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        print(f"{label}: {mins:02d}:{secs:02d}", end="\r", flush=True)
        time.sleep(1)
        total_seconds -= 1
    print(f"{label} complete!\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple Pomodoro timer")
    parser.add_argument("--work", type=float, default=25,
                        help="work session length in minutes (default: 25)")
    parser.add_argument("--short-break", type=float, default=5,
                        dest="short_break",
                        help="short break length in minutes (default: 5)")
    parser.add_argument("--long-break", type=float, default=15,
                        dest="long_break",
                        help="long break length in minutes (default: 15)")
    parser.add_argument("--cycles", type=int, default=4,
                        help="number of work sessions before a long break (default: 4)")
    args = parser.parse_args()

    for cycle in range(1, args.cycles + 1):
        run_timer(args.work, f"Work session {cycle}")
        if cycle < args.cycles:
            run_timer(args.short_break, "Short break")
        else:
            run_timer(args.long_break, "Long break")


if __name__ == "__main__":
    main()

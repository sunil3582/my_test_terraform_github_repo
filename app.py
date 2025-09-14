from __future__ import annotations

import argparse
import os
import sys

__version__ = "0.1.0"


def add_numbers(left: int, right: int) -> int:
    """Return the sum of two integers.

    This tiny function gives us something deterministic to validate in CI.
    """
    return left + right

def subtract_numbers(left: int, right: int) -> int:
    """Return the difference of two integers.

    This tiny function gives us something deterministic to validate in CI.
    """
    return left - right

def is_even(value: int) -> bool:
    """Return True if the provided integer is even, otherwise False."""
    return value % 2 == 0


def run_smoke_checks() -> None:
    """Run simple, deterministic checks that should pass in CI.

    Raises AssertionError if any check fails.
    """
    assert add_numbers(2, 3) == 5, "add_numbers failed"
    assert is_even(4) is True, "is_even failed for even number"
    assert is_even(5) is False, "is_even failed for odd number"
    assert subtract_numbers(2, 3) == -1, "subtract_numbers failed"

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simple app for CI/CD pipelines smoke checks."
    )
    parser.add_argument(
        "--run-checks",
        action="store_true",
        help="Run built-in smoke checks and exit.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print extra diagnostics.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.verbose:
        ci_env = os.getenv("CI", "")
        github_actions = os.getenv("GITHUB_ACTIONS", "")
        print(f"version={__version__}")
        print(f"ci_detected={bool(ci_env or github_actions)}")

    if args.run_checks:
        try:
            run_smoke_checks()
            print("SMOKE_TESTS_PASSED")
            return 0
        except AssertionError as exc:
            print(f"SMOKE_TESTS_FAILED: {exc}", file=sys.stderr)
            return 1

    print("APP_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



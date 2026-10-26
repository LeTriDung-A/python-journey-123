"""Exercise 02: add one argparse option to a small CLI."""

import argparse


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description="Print a requested turn number.")
    result.add_argument(
        "--turn",
        type=int,
        required=True,
        help="turn number as an integer",
    )
    return result


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    args = parser().parse_args()
    print(args)


if __name__ == "__main__":
    main()

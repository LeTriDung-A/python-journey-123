"""Exercise 01: imports, modules and main guard."""

import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.core import choose_action  # noqa: E402


def main() -> None:
    """Run a few examples using the imported function."""
    print(choose_action(1, 4))
    print(choose_action(4, 4))
    print(choose_action(3, 1))


if __name__ == "__main__":
    main()

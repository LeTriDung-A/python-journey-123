"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Run a few examples using the imported function."""
    print(choose_action(1, 4))
    print(choose_action(4, 4))
    print(choose_action(3, 1))


if __name__ == "__main__":
    main()

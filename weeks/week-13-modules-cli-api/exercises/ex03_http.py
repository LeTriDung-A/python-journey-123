"""Exercise 03: inspect an offline HTTP fixture."""

import sys
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
if str(WEEK_ROOT) not in sys.path:
    sys.path.insert(0, str(WEEK_ROOT))

from bot_course.http_foundation import parse_json_response  # noqa: E402

fixture = b'{"lesson": 13}'


def main() -> None:
    """Inspect successful and unsuccessful offline response fixtures."""
    data = parse_json_response(200, fixture)
    assert data["lesson"] == 13
    print(data)

    try:
        parse_json_response(500, b'{"error": "server error"}')
    except ValueError as error:
        print(f"Expected error: {error}")
    else:
        raise AssertionError("non-2xx response should raise ValueError")


if __name__ == "__main__":
    main()

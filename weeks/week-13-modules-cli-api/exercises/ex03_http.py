"""Exercise 03: inspect an offline HTTP fixture."""

from bot_course.http_foundation import parse_json_response

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

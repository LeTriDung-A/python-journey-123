"""Giao dien dong lenh cho bai tap Week 13."""

import argparse
import json

from week13_api import get_json
from week13_utils import is_even, make_greeting


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Bai tap Python Week 13")
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="In loi chao")
    greet_parser.add_argument("name", help="Ten can chao")

    even_parser = subparsers.add_parser("even", help="Kiem tra so chan")
    even_parser.add_argument("number", type=int, help="So nguyen can kiem tra")

    get_parser = subparsers.add_parser("get", help="Goi HTTP GET va in JSON")
    get_parser.add_argument("url", help="URL API cong khai")
    get_parser.add_argument("--timeout", type=int, default=5, help="Timeout tinh bang giay")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "greet":
            print(make_greeting(args.name))
        elif args.command == "even":
            print("So chan" if is_even(args.number) else "So le")
        elif args.command == "get":
            data = get_json(args.url, timeout=args.timeout)
            print(json.dumps(data, ensure_ascii=False, indent=2))
    except (ValueError, RuntimeError) as error:
        parser.error(str(error))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

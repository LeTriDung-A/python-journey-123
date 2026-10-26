# Week 13 - Modules, Packages, CLI va API/HTTP

## Chay chuong trinh

Yeu cau Python 3.10+.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

python -m pip install -e .
python -m week13_app --help
python -m week13_app greet Dung
python -m week13_app get https://api.github.com
```

## Noi dung

- `utils.py`: ham xu ly chuoi va so.
- `api_client.py`: HTTP GET, timeout, status code va JSON.
- `cli.py`: giao dien dong lenh bang argparse.
- `__main__.py`: cho phep chay package bang `python -m week13_app`.
- `pyproject.toml`: khai bao project va dependency.

API demo dung endpoint cong khai, khong can API key. Can ket noi Internet de chay lenh `get`.

"""Goi HTTP GET va doc JSON tu API."""

import requests


def get_json(url: str, timeout: int = 5):
    """Lay JSON tu URL; bao loi neu HTTP hoac mang gap su co."""
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL phai bat dau bang http:// hoac https://")

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.Timeout as error:
        raise RuntimeError("Yeu cau het thoi gian cho.") from error
    except requests.RequestException as error:
        raise RuntimeError(f"Khong the goi API: {error}") from error

    try:
        return response.json()
    except requests.JSONDecodeError as error:
        raise ValueError("API khong tra ve JSON hop le.") from error

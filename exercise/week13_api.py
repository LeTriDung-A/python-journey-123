"""Goi HTTP GET va doc JSON bang thu vien chuan cua Python."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def get_json(url: str, timeout: int = 5):
    """Lay JSON tu URL; bao loi neu HTTP, mang hoac JSON gap su co."""
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL phai bat dau bang http:// hoac https://")
    if timeout <= 0:
        raise ValueError("Timeout phai lon hon 0.")

    request = Request(url, headers={"User-Agent": "Python-Journey-Week13"})
    try:
        with urlopen(request, timeout=timeout) as response:
            status = response.status
            body = response.read().decode("utf-8")
    except HTTPError as error:
        raise RuntimeError(f"API tra ve HTTP {error.code}.") from error
    except URLError as error:
        raise RuntimeError(f"Khong the ket noi API: {error.reason}") from error
    except TimeoutError as error:
        raise RuntimeError("Yeu cau het thoi gian cho.") from error

    if not 200 <= status < 300:
        raise RuntimeError(f"Yeu cau that bai, HTTP {status}.")

    try:
        return json.loads(body)
    except json.JSONDecodeError as error:
        raise ValueError("API khong tra ve JSON hop le.") from error

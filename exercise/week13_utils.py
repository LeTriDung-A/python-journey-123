"""Cac ham tien ich cho bai tap Week 13."""


def make_greeting(name: str) -> str:
    """Tao loi chao tu ten nguoi dung."""
    name = name.strip()
    if not name:
        raise ValueError("Ten khong duoc de trong.")
    return f"Xin chao, {name}!"


def is_even(number: int) -> bool:
    """Tra ve True neu number la so chan."""
    return number % 2 == 0

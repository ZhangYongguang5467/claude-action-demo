"""工具函数模块"""


def add(a: int, b: int) -> int:
    """两数相加"""
    return a + b


def subtract(a: int, b: int) -> int:
    """两数相减"""
    return a - b


def multiply(a: int, b: int) -> int:
    """两数相乘"""
    return a * b


def divide(a: float, b: float) -> float:
    """两数相除"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

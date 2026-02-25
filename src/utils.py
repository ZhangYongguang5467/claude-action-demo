"""工具函数模块"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """两数相加"""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """两数相减"""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """两数相乘"""
    return a * b


def divide(a: Number, b: Number) -> float:
    """两数相除，除数为零时抛出 ValueError"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

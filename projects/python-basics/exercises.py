# projects/python-basics/exercises.py
"""Small helper functions for Phase-1: Python basics."""

from typing import List


def formatted_sentence(age: int, size: float, name: str) -> str:
    """Return a formatted sentence using f-strings."""
    return f"my age is {age}, my size is {size} and my name is {name}"


def sum_and_average(nums: List[int]) -> tuple[int, float]:
    """Return (sum, average) for a list of numbers.
    Raises ValueError on empty list.
    """
    if not nums:
        raise ValueError("nums must not be empty")
    total = sum(nums)
    avg = total / len(nums)
    return total, avg


def odd_numbers(nums: List[int]) -> List[int]:
    """Return a list containing only odd numbers from nums."""
    return [n for n in nums if n % 2 != 0]


def mean(values: List[float]) -> float:
    """Return arithmetic mean of values."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def save_names(names: List[str], path: str) -> None:
    """Save list of names (one per line) to path."""
    with open(path, "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")


def load_names(path: str) -> List[str]:
    """Load names from file and return as list (stripped)."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

"""Utility functions for pyask."""

import re


__all__ = ("always_true", "process", "items", "ns_between")


def always_true(*args, **kwargs):
    """Always returns True, no matter the arguments."""
    return True


def process(func, valid, s):
    """Processes s with func then validates it with valid."""
    x = func(s)
    if valid(x):
        return x
    raise ValueError(f"{s} is not valid.")


def items(s, func=str):
    """Returns items processed by func in a comma or space delimited string."""
    return [func(x) for x in re.split(r"\s*,\s*|\s+", s)]


def ns_between(l, r, ns):
    """Checks if all ns are between l and r (inclusive)."""
    return all(l <= n <= r for n in ns)

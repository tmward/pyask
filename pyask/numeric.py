"""Functions to ask questions with numeric answers on the terminal."""

from functools import partial

from .ask import ask
from .utils import always_true, process


__all__ = (
    "integer",
    "decimal",
    "number",
    "number_between",
    "number_greater_than",
    "number_greater_than_or_eq",
    "number_less_than",
    "number_less_than_or_eq",
    "number_eq_to",
    "positive_number",
    "negative_number",
    "positive_integer",
    "negative_integer",
    "natural_number",
    "seconds",
)


def to_number(s):
    """Takes str s and returns int (preferentially) or float."""
    if s.find(".") > -1:
        return float(s)
    return int(s)


def integer(question, aid="enter an integer", **kwargs):
    """Asks user for an integer."""
    p_func = partial(process, int, always_true)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def decimal(question, aid="enter a decimal", **kwargs):
    """Asks user for a decimal."""
    p_func = partial(process, float, always_true)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number(question, aid="enter a number", **kwargs):
    """Asks user for any number."""
    p_func = partial(process, to_number, always_true)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number_between(l, r, question, aid="", only_int=False, **kwargs):
    """Asks user for a number between l and r, inclusive."""
    value_type, parser = ("integer", int) if only_int else ("number", to_number)
    if aid == "":
        aid = f"enter {value_type} between {l} and {r}, inclusive"
    p_func = partial(process, parser, lambda n: l <= n <= r)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number_greater_than(l, question, aid="", only_int=False, **kwargs):
    """Asks user for number greater than l."""
    value_type, parser = ("integer", int) if only_int else ("number", to_number)
    if aid == "":
        aid = f"enter {value_type} greater than {l}"
    p_func = partial(process, parser, lambda n: l < n)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number_greater_than_or_eq(l, question, aid="", only_int=False, **kwargs):
    """Asks user for number greater than or equal to l."""
    value_type, parser = ("integer", int) if only_int else ("number", to_number)
    if aid == "":
        aid = f"enter {value_type} >= {l}"
    p_func = partial(process, parser, lambda n: l <= n)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number_less_than(r, question, aid="", only_int=False, **kwargs):
    """Asks user for number less than r."""
    value_type, parser = ("integer", int) if only_int else ("number", to_number)
    if aid == "":
        aid = f"enter {value_type} less than {r}"
    p_func = partial(process, parser, lambda n: n < r)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number_less_than_or_eq(r, question, aid="", only_int=False, **kwargs):
    """Asks user for number less than or equal to r."""
    value_type, parser = ("integer", int) if only_int else ("number", to_number)
    if aid == "":
        aid = f"enter {value_type} <= {r}"
    p_func = partial(process, parser, lambda n: n <= r)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def number_eq_to(n, question, aid="enter the correct number", **kwargs):
    """Asks user for number equal to n."""
    p_func = partial(process, to_number, lambda x: n == x)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


positive_number = partial(number_greater_than, 0)
negative_number = partial(number_less_than, 0)
positive_integer = partial(number_greater_than, 0, only_int=True)
negative_integer = partial(number_less_than, 0, only_int=True)
natural_number = partial(number_greater_than_or_eq, 0, only_int=True)


def to_seconds(s):
    """Takes str s in HH:MM:SS, MM:SS, or SS format and returns total seconds (integer)."""
    ssmmhh = [int(n) for n in reversed(s.split(":"))]
    # only [SS]; we allow user to give us any positive number of seconds
    if len(ssmmhh) == 1 and ssmmhh[0] >= 0:
        return ssmmhh[0]
    # [SS, MM]
    elif len(ssmmhh) == 2 and ssmmhh[0] in range(60) and ssmmhh[1] in range(60):
        return ssmmhh[0] + ssmmhh[1] * 60
    # [SS, MM, HH]
    elif (
        len(ssmmhh) == 3
        and ssmmhh[0] in range(60)
        and ssmmhh[1] in range(60)
        and ssmmhh[2] >= 0
    ):
        return ssmmhh[0] + ssmmhh[1] * 60 + ssmmhh[2] * 3600
    raise ValueError(f"{s} is not a valid time.")


def seconds(question, aid="enter time in HH:MM:SS, MM:SS, or SS format", **kwargs):
    """Asks user for time."""
    p_func = partial(process, to_seconds, always_true)
    return ask(question, aid=aid, process_func=p_func, **kwargs)

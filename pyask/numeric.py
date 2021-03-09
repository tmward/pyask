from .ask import ask, process, always_true
from functools import partial


def to_number(s):
    """Takes str s and returns int (preferentially) or float."""
    if s.find(".") > -1:
        return float(s)
    return int(s)

def between(l, r):
    """Returns pred function to test if a numeric is between l and r (inclusive)."""
    return lambda n: l <= n <= r


def integer(question, default="", aide="enter an integer"):
    p_func = partial(process, int, always_true)
    return ask(question, default=default, aide=aide, process_func=p_func)


def decimal(question, default="", aide="enter a decimal"):
    p_func = partial(process, float, always_true)
    return ask(question, default=default, aide=aide, process_func=p_func)


def number(question, default="", aide="enter a number"):
    p_func = partial(process, to_number, always_true)
    return ask(question, default=default, aide=aide, process_func=p_func)


def positive_integer(question, default="", aide="enter a positive integer"):
    p_func = partial(process, int, lambda i: 0 < i)
    return ask(question, default=default, aide=aide, process_func=p_func)


def natural_number(question, default="", aide="enter a natural number"):
    p_func = partial(process, int, lambda i: 0 <= i)
    return ask(question, default=default, aide=aide, process_func=p_func)


def positive_number(question, default="", aide="enter a positive number"):
    p_func = partial(process, to_number, lambda n: 0 < n)
    return ask(question, default=default, aide=aide, process_func=p_func)


def negative_number(question, default="", aide="enter a negative number"):
    p_func = partial(process, to_number, lambda n: n < 0)
    return ask(question, default=default, aide=aide, process_func=p_func)


def negative_integer(question, default="", aide="enter a negative integer"):
    p_func = partial(process, int, lambda i: i < 0)
    return ask(question, default=default, aide=aide, process_func=p_func)


def integer_between(question, l, r, default="", aide=""):
    if aide == "":
        aide = f"enter integer between {l} and {r} (inclusive)"
    p_func = partial(process, int, between(l, r))
    return ask(question, default=default, aide=aide, process_func=p_func)


def number_between(question, l, r, default="", aide=""):
    if aide == "":
        aide = f"enter number between {l} and {r} (inclusive)"
    p_func = partial(process, to_number, between(l, r))
    return ask(question, default=default, aide=aide, process_func=p_func)

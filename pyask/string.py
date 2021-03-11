"""Functions to ask questions with string answers on the terminal."""

from functools import partial
from operator import contains, eq

from .ask import ask, process, always_true

__all__ = ("string", "char", "yes_no")


def string(question, default="", aide="", allow_empty=False):
    """Asks user for a string response."""
    value_type, valid_f = (
        ("any string", always_true)
        if allow_empty
        else ("a non-empty string", lambda s: s != "")
    )
    if aide == "":
        aide = f"enter {value_type}"
    p_func = partial(process, str, valid_f)
    return ask(question, default=default, aide=aide, process_func=p_func)


def char(question, default="", aide="enter a single character", allow_empty=False):
    comparison = partial(contains, (0, 1)) if allow_empty else partial(eq, 1)
    p_func = partial(process, str, lambda s: comparison(len(s)))
    return ask(question, default=default, aide=aide, process_func=p_func)


def yes_no_to_bool(s):
    return {"yes": True, "y": True, "no": False, "n": False}[s.casefold()]


def yes_no(question, default="", aide="yes or no"):
    p_func = partial(process, yes_no_to_bool, always_true)
    return ask(question, default=default, aide=aide, process_func=p_func)

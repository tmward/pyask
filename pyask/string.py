"""Functions to ask questions with string answers on the terminal."""

from functools import partial
import re
from operator import contains, eq

from .ask import ask
from .utils import always_true, process

__all__ = ("string", "char", "yes_no", "string_regex")


def string(question, aide="", allow_empty=False, **kwargs):
    """Asks user for a string response."""
    value_type, valid_f = (
        ("any string", always_true)
        if allow_empty
        else ("a non-empty string", lambda s: s != "")
    )
    if aide == "":
        aide = f"enter {value_type}"
    p_func = partial(process, str, valid_f)
    return ask(question, aide=aide, process_func=p_func, **kwargs)


def char(question, aide="enter a single character", allow_empty=False, **kwargs):
    """Asks user for a single character response."""
    comparison = partial(contains, (0, 1)) if allow_empty else partial(eq, 1)
    p_func = partial(process, str, lambda s: comparison(len(s)))
    return ask(question, aide=aide, process_func=p_func, **kwargs)


def yes_no_to_bool(s):
    """Converts yes or y to True. false or f to False.  Case-insensitive."""
    return {"yes": True, "y": True, "no": False, "n": False}[s.casefold()]


def yes_no(question, aide="yes or no", **kwargs):
    """Asks user a yes or no question."""
    p_func = partial(process, yes_no_to_bool, always_true)
    return ask(question, aide=aide, process_func=p_func, **kwargs)

def string_regex(regex, question, case_insensitive=False, **kwargs):
    """Asks user for a string response that must completely match the regex."""
    flags = re.IGNORECASE if case_insensitive else 0
    p_func = partial(process, str, re.compile(regex, flags).fullmatch)
    return ask(question, process_func=p_func, **kwargs)

"""Functions to ask questions with string answers on the terminal."""

from functools import partial
import re

from .ask import ask
from .utils import always_true, process

__all__ = ("string", "char", "yes_no", "string_regex")


def string(question, aid="any string", **kwargs):
    """Asks user for a string response."""
    p_func = partial(process, str, lambda s: s != "")
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def char(question, aid="single character", **kwargs):
    """Asks user for a single character response."""
    p_func = partial(process, str, lambda s: len(s) == 1)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def yes_no_to_bool(s):
    """Converts yes or y to True. false or f to False.  Case-insensitive."""
    return {"yes": True, "y": True, "no": False, "n": False}[s.casefold()]


def yes_no(question, aid="yes or no", **kwargs):
    """Asks user a yes or no question."""
    p_func = partial(process, yes_no_to_bool, always_true)
    return ask(question, aid=aid, process_func=p_func, allow_empty=False, **kwargs)


def string_regex(regex, question, case_insensitive=False, **kwargs):
    """Asks user for a string response that must completely match the regex."""
    flags = re.IGNORECASE if case_insensitive else 0
    p_func = partial(process, str, re.compile(regex, flags).fullmatch)
    return ask(question, process_func=p_func, **kwargs)

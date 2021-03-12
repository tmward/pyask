"""Functions to prompt user to select from lists of options."""

from functools import partial

from .numeric import number_between
from .utils import items, process, ns_between

__all__ = ("which", "which_items")


def which(xs, question, aide="pick a number", **kwargs):
    """Ask user to select an item from a sequence and returns that item."""
    return xs[
        number_between(
            0, len(xs) - 1, question, aide=aide, only_int=True, choices=xs, **kwargs
        )
    ]


def which_items(xs, question, aide="", allow_repeats=True, empty_ok=False, **kwargs):
    """Ask user to select multiple items from a list."""
    if aide == "":
        aide = "pick the number(s) of item(s) you want"
    parsef = partial(items, func=int)
    validf = lambda ns: ns_between(0, len(xs) - 1, ns) and len(ns) == len(set(ns))
    if empty_ok:
        parsef = lambda s: items(s, func=int) if len(s) > 0 else []
        aide += ", ok to give no choice"
    if allow_repeats:
        validf = lambda ns: ns_between(0, len(xs) - 1, ns)
        aide += ", repeats ok"
    p_func = partial(process, parsef, validf)
    return [
        xs[i]
        for i in ask(question, aide=aide, process_func=p_func, choices=xs, **kwargs)
    ]

"""Functions to prompt user to select from lists of options."""

from functools import partial

from .ask import ask
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


def which_items(
    xs, question, aide="space/comma separated number(s)", allow_repeats=True, **kwargs
):
    """Ask user to select multiple items from a list."""
    if allow_repeats:
        validf = lambda ns: ns_between(0, len(xs) - 1, ns)
        aide += ", repeats ok"
    else:
        validf = lambda ns: ns_between(0, len(xs) - 1, ns) and len(ns) == len(set(ns))
    p_func = partial(process, partial(items, func=int), validf)
    return [
        xs[i]
        for i in ask(question, aide=aide, process_func=p_func, choices=xs, **kwargs)
    ]

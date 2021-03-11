"""Functions to prompt user to select from lists of options."""

from .numeric import number_between

__all__ = ("which",)

def which(xs, question, aide="pick a number", **kwargs):
    return xs[
        number_between(
            0, len(xs) - 1, question, aide=aide, only_int=True, choices=xs, **kwargs
        )
    ]

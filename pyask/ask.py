"""Provides generic functions to ask questions on the terminal."""

from functools import partial

from .utils import always_true, process

__all__ = ("ask",)


def print_choices(choices):
    """Pretty prints choices on terminal with option numbers."""
    sig_figs = len(str(len(choices) - 1))
    print("Available choices are:")
    for i, choice in enumerate(choices):
        print(f"({i:>{sig_figs}}) {choice}")


def prompt(question, aid="", default=""):
    """Constructs question prompt."""
    if aid:
        return f"{question.rstrip('?')}? ({aid}) [{default}] "
    return f"{question.rstrip('?')}? [{default}] "


whatever = partial(process, str, always_true)


def ask(question, aid="", default="", allow_empty=False, process_func=whatever, choices=None):
    """Returns user answer to question once they enter a valid response."""
    if choices is not None:
        print_choices(choices)
    if allow_empty and "empty response ok" not in aid:
        aid += "empty response ok" if aid == "" else ", empty response ok"
    response = input(prompt(question, aid, default)).strip()
    if response == "":
        if allow_empty:
            return None
        response = default
    try:
        return process_func(response)
    except (KeyError, ValueError):
        print("Invalid respose.")
        return ask(question, aid, default, allow_empty, process_func, choices)

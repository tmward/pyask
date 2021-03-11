"""Provides generic functions to ask questions on the terminal."""

from functools import partial

__all__ = ("ask",)


def print_choices(choices):
    """Pretty prints choices on terminal with option numbers."""
    sig_figs = len(str(len(choices) - 1))
    print("Available choices are:")
    for i, choice in enumerate(choices):
        print(f"({i:>{sig_figs}}) {choice}")


def prompt(question, default="", aide=""):
    """Constructs question prompt."""
    if aide:
        return f"{question.rstrip('?')}? ({aide}) [{default}] "
    return f"{question.rstrip('?')}? [{default}] "


def process(func, valid, s):
    """Processes s with func then validates it with valid."""
    x = func(s)
    if valid(x):
        return x
    raise ValueError(f"{s} is not valid.")


def always_true(*args, **kwargs):
    """Always returns True, no matter the arguments."""
    return True


whatever = partial(process, str, always_true)


def ask(question, default="", aide="", process_func=whatever, choices=None):
    """Returns user answer to question once they enter a valid response."""
    if choices is not None:
        print_choices(choices)
    response = input(prompt(question, default, aide)).strip()
    if response == "":
        response = default
    try:
        return process_func(response)
    except (KeyError, ValueError):
        print("Invalid respose.")
        return ask(question, default, aide, process_func, choices)

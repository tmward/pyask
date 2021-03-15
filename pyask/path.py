"""Functions to ask user questions about files/directories."""

from functools import partial
from os.path import abspath, exists, isdir, isfile, normpath

from .ask import ask
from .utils import always_true, process


def filename(question, aid="filename", absolute=False, must_exist=False, **kwargs):
    """Asks user for filename, returns path."""
    parser = abspath if absolute else normpath
    validf = lambda p: exists(p) and isfile(p) if must_exist else always_true
    p_func = partial(process, parser, validf)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def dirname(question, aid="directory name", absolute=False, must_exist=False, **kwargs):
    """Asks user for directory name, returns path."""
    parser = abspath if absolute else normpath
    validf = lambda p: exists(p) and isdir(p) if must_exist else always_true
    p_func = partial(process, parser, validf)
    return ask(question, aid=aid, process_func=p_func, **kwargs)


def pathname(question, aid="pathname", absolute=False, must_exist=False, **kwargs):
    """Asks user for pathname, returns path."""
    parser = abspath if absolute else normpath
    validf = lambda p: exists(p) if must_exist else always_true
    p_func = partial(process, parser, validf)
    return ask(question, aid=aid, process_func=p_func, **kwargs)

# `pyask`

A python library for terminal programs to ask users questions
and validate their responses.
It is pure Python (3.6+)
and requires no dependencies beyond the standard library.

# Installation

`pyask` is available on the Python Package Index (PyPI) and
can be installed with `pip`:

```
$ pip install pyask
```

# Use

## `ask()`

`pyask`'s main functionality stems from the function `ask()`:

```
ask(question, aid="", default="", allow_empty=False, process_func=whatever, choices=None)
```

`ask()` takes the following arguments:

1. `question`: a question in the form of a string.
    Including a question mark is optional, so `"What is your favorite color?" and
    "What is your favorite color" are equivalent.
2. `aid`: Optional and defaults to an empty string.
    Provides user with aid to answer the question. So setting
    `aid="primary color"` to the above question will ask the user
    `What is your favorite color? (primary color)`.
3. `default`: Optional and defaults to an empty string. Whatever you
   provide will be the assumed answer from the user if they simply hit
   `Enter` at the prompt rather than providing an answer.
   Providing a default response will prevent the user from entering a blank response.
4. `allow_empty`: Optional and defaults to `False`.
    Setting it to `True` will prevent the user from entering a blank response
    (remember, if you provide a `default` then the user will not be able to enter a blank response`.
5. `process_func`: Defaults to `whatever`,
    a function that keeps the user's answer and returns it as is.
    It is easy to build an appropriate `process_func` using `pyask.utils.process()`.
    See documentation below for full explanation, but in brief,
    a `process_func` will first process the user input into a certain form
    (be it a number, list of characters, etc) then
    validate that it meets the needed requirements (e.g., is positive for example).
6. `choices`: Optional and defaults to `None`.
    Will provide the user with a list of choices to select from the sequence provided.
    Options are numbered with the index (0-based) of the sequence.

`ask()` then returns the user's answer. If the user's answer is not a valid one,
it will inform the user it is not valid then redo the prompt.
This can continue indefinitely until the user provides a valid response.

## `process()`

```
process(func, valid, s)
```

Takes `func` and `valid` functions with a string, `s`,
and returns `s` processed by `func` if `valid(func(s))` is `True`.
Otherwise, it raises a `ValueError`. Both `func` and `valid` are functions.
Best used with `partial` from Python's standard library `functools`, like:

```
partial(process, int, lambda x: x > 0)
```

Which would create a function that takes a string,
casts it as an integer, then returns it if it's positive.

## Convenience functions
Having to build a `process_func` for `ask()` would be cumbersome.
I created various convenience functions which take the exact same arguments
as `ask()` but can ask users common questions.
Examples are below.

### `pyask.numeric`

Contains convenience functions for asking the user number questions.
These include:

```
decimal(question, aid='enter a decimal', **kwargs)
```

Asks user for a decimal (aka float). Example would be calling:

```
>>> pyask.decimal("How tall are you", aid="in cm", default=5)
How tall are you? (in cm) [5]
5.0

>>> pyask.decimal("How tall are you", aid="in cm", default=5)
How tall are you? (in cm) [5] 7.8
7.8
```

```
integer(question, aid='enter an integer', **kwargs)
```

Asks user for an integer (a float/decimal response is illegal and not accepted).

```
number(question, aid='enter a number', **kwargs)
```

Asks user for any number, and returns an integer if an integer was given
or a float if a float was given.

```
number_between(l, r, question, aid='', only_int=False, **kwargs)
```
Asks user for a number between l and r, inclusive.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

```
number_eq_to(n, question, aid='enter the correct number', **kwargs)
```
Asks user for number equal to n.

```
number_greater_than(l, question, aid='', only_int=False, **kwargs)
```

Asks user for number greater than l.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

```
number_greater_than_or_eq(l, question, aid='', only_int=False, **kwargs)
```

Asks user for number greater than or equal to l.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

```
number_less_than(r, question, aid='', only_int=False, **kwargs)
```

Asks user for number less than r.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

```
number_less_than_or_eq(r, question, aid='', only_int=False, **kwargs)
```

Asks user for number less than or equal to r.

```
seconds(question, aid='enter time in HH:MM:SS, MM:SS, or SS format', **kwargs)
```

Asks user for time. Time can be in HH:MM:SS, MM:SS, or SS format.
SS format takes any number of positive seconds.
MM:SS and HH:MM:SS must have MM and SS between 0 and 59 (inclusive).
HH can be any positive number or zero.

# Contributions/suggestions

Contributions and suggestions are welcome.
Feel free to raise an [issue](https://github.com/tmward/pyask/issues)
for a feature request or
to submit a [pull request](https://github.com/tmward/pyask/pulls)
if you have implemented features you would like to see in `pyask`.

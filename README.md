# Table of Contents

* [Table of Contents](#table-of-contents)
* [pyask](#pyask)
* [Brief Overview](#brief-overview)
* [Installation](#installation)
* [Use](#use)
  * [ask()](#ask)
  * [process()](#process)
* [Convenience functions](#convenience-functions)
* [Number convenience functions in pyask\.numeric](#number-convenience-functions-in-pyasknumeric)
  * [decimal()](#decimal)
  * [integer()](#integer)
  * [number()](#number)
  * [number\_between()](#number_between)
  * [number\_eq\_to()](#number_eq_to)
  * [number\_greater\_than()](#number_greater_than)
  * [number\_greater\_than\_or\_eq()](#number_greater_than_or_eq)
  * [number\_less\_than()](#number_less_than)
  * [number\_less\_than\_or\_eq()](#number_less_than_or_eq)
  * [seconds()](#seconds)
* [Filepath convenience functions in pyask\.path](#filepath-convenience-functions-in-pyaskpath)
  * [dirname()](#dirname)
  * [filename()](#filename)
  * [pathname()](#pathname)
* [Selection convenience functions in pyask\.selection](#selection-convenience-functions-in-pyaskselection)
  * [which()](#which)
  * [which\_items()](#which_items)
* [String convenience functions in pyask\.string](#string-convenience-functions-in-pyaskstring)
  * [any\_string()](#any_string)
  * [char()](#char)
  * [string\_regex()](#string_regex)
  * [yes\_no()](#yes_no)

# `pyask`

A python library for terminal programs to ask users questions
and validate their responses.
It is pure Python (3.6+)
and requires no dependencies beyond the standard library.

# Brief Overview

Do you wish you could easily ask a user a question
and keep on asking it until they give a valid response?
Now you can! Here's an example of asking the user for a
time duration in seconds:

```
>>> answer = pyask.seconds("How long is the game?")
How long is the game? (enter time in HH:MM:SS, MM:SS, or SS format) [] -10
Invalid respose.
How long is the game? (enter time in HH:MM:SS, MM:SS, or SS format) [] 10:61
Invalid respose.
How long is the game? (enter time in HH:MM:SS, MM:SS, or SS format) [] 10:59
>>> answer
659
>>> type(answer)
<class 'int'>
>
```

Note that it checked to make sure the answer was a valid timestamp
and continued to ask the user until they gave a valid response.
It then returned an integer so you can immediately put their response to use in your program.

Here's another example, this time asking a user to select the filenames for videos to concatenate together.
Note that videos are not named nicely, so sorting them alphabetically and putting them together would scramble the video!
Also note that there are non-video files you would not want to put together in the directory:

```
>>> pyask.which_items(os.listdir(), "What videos, in order, should be stitched together?")
Available choices are:
(0) video1.mp4
(1) video3.mp4
(2) usb.txt
(3) video2.mp4
(4) video_4.mp4
What videos, in order, should be stitched together? (space/comma separated number(s), repeats ok) [] 0 3 1 4
['video1.mp4', 'video2.mp4', 'video3.mp4', 'video_4.mp4']
```

It returns a nice list in the order the user specified.
They can also use commas and any variable number of spaces to separate items.

The package can ask many types of questions about numbers,
strings, selecting multiple items, and filenames.
Please see below for more information.

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
    `aid="primary color"` to the above question will ask the user\
    `What is your favorite color? (primary color)`.
3. `default`: Optional and defaults to an empty string. Whatever you
   provide will be the assumed answer from the user if they simply hit
   `Enter` at the prompt rather than providing an answer.
   Providing a default response will prevent the user from entering a blank response.
   Providing a default of "blue" to the above question would prompt:\
   `What is your favorite color? (primary color) [blue]`
4. `allow_empty`: Optional and defaults to `False`.
    Setting it to `True` will prevent the user from entering a blank response
    (remember, if you provide a `default` then the user will not be able to enter a blank response).
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

Empty responses return `None`.

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

# Convenience functions
Having to build a `process_func` for `ask()` would be cumbersome.
I created various convenience functions which ask users common questions.
All these convenience functions take the same arguments as `ask()`,
but some may require additional arguments (see below).
All the convenience functions are available at the top level of the package
(as in, can be called with `pyask.decimal` rather than `pyask.numeric.decimal`.

# Number convenience functions in `pyask.numeric`

## `decimal()`

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

## `integer()`

```
integer(question, aid='enter an integer', **kwargs)
```

Asks user for an integer (a float/decimal response is illegal and not accepted).

## `number()`

```
number(question, aid='enter a number', **kwargs)
```

Asks user for any number, and returns an integer if an integer was given
or a float if a float was given.

## `number_between()`

```
number_between(l, r, question, aid='', only_int=False, **kwargs)
```
Asks user for a number between l and r, inclusive.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

## `number_eq_to()`

```
number_eq_to(n, question, aid='enter the correct number', **kwargs)
```
Asks user for number equal to n.

## `number_greater_than()`

```
number_greater_than(l, question, aid='', only_int=False, **kwargs)
```

Asks user for number greater than l.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

## `number_greater_than_or_eq()`

```
number_greater_than_or_eq(l, question, aid='', only_int=False, **kwargs)
```

Asks user for number greater than or equal to l.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

## `number_less_than()`

```
number_less_than(r, question, aid='', only_int=False, **kwargs)
```

Asks user for number less than r.
`only_int` allows you to accept only an integer response
if `True` or accept decimals/floats if `False` (default).

## `number_less_than_or_eq()`

```
number_less_than_or_eq(r, question, aid='', only_int=False, **kwargs)
```

Asks user for number less than or equal to r.

## `seconds()`

```
seconds(question, aid='enter time in HH:MM:SS, MM:SS, or SS format', **kwargs)
```

Asks user for time. Time can be in HH:MM:SS, MM:SS, or SS format.
SS format takes any number of positive seconds.
MM:SS and HH:MM:SS must have MM and SS between 0 and 59 (inclusive).
HH can be any positive number or zero.
It returns the time (seconds).

# Filepath convenience functions in `pyask.path`

## `dirname()`

```
dirname(question, aid='directory name', absolute=False, must_exist=False, **kwargs)
```

Asks user for directory name, returns path.
`absolute` when `True` will return an absolute path rather than a relative one.
`must_exist` when `True` will only let the user enter in the path of an existing directory.

## `filename()`

```
filename(question, aid='filename', absolute=False, must_exist=False, **kwargs)
```

Asks user for filename, returns path.
`absolute` when `True` will return an absolute path rather than a relative one.
`must_exist` when `True` will only let the user enter in the path of an existing file.

## `pathname()`

```
pathname(question, aid='pathname', absolute=False, must_exist=False, **kwargs)
```

Asks user for pathname (either file or directory), returns path.
`absolute` when `True` will return an absolute path rather than a relative one.
`must_exist` when `True` will only let the user enter in the path of an existing file or directory.

# Selection convenience functions in `pyask.selection`

Contains functions that prompt a user to select from a list of questions.

## `which()`

```
which(xs, question, aid='pick a number', **kwargs)
```

Ask user to select an item from the sequence `xs` and returns that item.

Example, with a default answer of 2 and the user hitting `Enter` to use the default answer:

```
>>> pyask.which(['a', 'b', 'c'], "Which letter?", default="2")
Available choices are:
(0) a
(1) b
(2) c
Which letter? (pick a number) [2]
'c'
```

## `which_items()`

```
which_items(xs, question, aid='space/comma separated number(s)', allow_repeats=True, **kwargs)
```

Ask user to select multiple items from the sequence `xs`,
by specifying a comma or space delimited response.
If `allow_repeats` is `True`, they can specify the same item multiple times.

Example:

```
>>> pyask.which_items(os.listdir(), "What videos, in order, should be stitched together?")
Available choices are:
(0) video1.mp4
(1) video3.mp4
(2) usb.txt
(3) video2.mp4
(4) video_4.mp4
What videos, in order, should be stitched together? (space/comma separated number(s), repeats ok) [] 0, 3, 1, 4
['video1.mp4', 'video2.mp4', 'video3.mp4', 'video_4.mp4']
```

# String convenience functions in `pyask.string`

Contains functions that prompt a user to select from a list of questions.

## `any_string()`

```
any_string(question, aid='any string', **kwargs)
```

Asks user for a string response.

## `char()`

```
char(question, aid='single character', **kwargs)
```

Asks user for a single character response.

## `string_regex()`

```
string_regex(regex, question, case_insensitive=False, **kwargs)
```

Asks user for a string response that must completely match the regex.
The regex must be in standard
[Python regex](https://docs.python.org/3/library/re.html?highlight=re#module-re).
This allows you to easily ask any possible variant of a question
and validate it with any regex you can think of.
The example below checks for a string that ends in "mp4", "avi", or "mov" and is case-insensitive:

```
>>> pyask.string_regex(r"(?i).+mp4|avi|mov$", "What is a valid video filename")
What is a valid video filename? [] myvideo.docx
Invalid respose.
What is a valid video filename? [] myvideo.MP4
'myvideo.MP4'
>>> pyask.string_regex(r"(?i).+mp4|avi|mov$", "What is a valid video filename")
What is a valid video filename? [] myvideo.mp4
'myvideo.mp4'
```

## `yes_no()`

```
yes_no(question, aid='yes or no', **kwargs)
```

Asks user a yes or no question.
Accepts "yes", "y", "no", or "n" in any case (so "YES" or "YeS" works).
Returns a boolean. Nice to use in control-flow logic. 

Example:

```
>>> if pyask.yes_no("Are you hungry"):
...     print("Here's a snack.")
... else:
...     print("You don't need a snack.")
...
Are you hungry? (yes or no) [] yes
Here's a snack.
>>>
```

 Contributions/suggestions

Contributions and suggestions are welcome.
Feel free to raise an [issue](https://github.com/tmward/pyask/issues)
for a feature request or
to submit a [pull request](https://github.com/tmward/pyask/pulls)
if you have implemented features you would like to see in `pyask`.

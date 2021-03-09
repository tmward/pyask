def print_choices(choices):
    sig_figs = len(str(len(choices)))
    print("Available choices are:")
    for i, choice in enumerate(choices, 1):
        print(f"({i:>{sig_figs}}) {choice}")


def prompt(question, default="", aide=""):
    if aide:
        return f"{question.rstrip('?')}? ({aide}) [{default}] "
    return f"{question.rstrip('?')}? [{default}] "


def not_empty_str(string):
    if string:
        return string
    raise ValueError("String is empty!")


def ask(question, default="", aide="", process_func=not_empty_str, choices=None):
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

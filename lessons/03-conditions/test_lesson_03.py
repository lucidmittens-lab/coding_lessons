# Tests for Lesson 3. You do not need to understand this file yet.
# Run it from the top folder of the repository:
#     python3 lessons/03-conditions/test_lesson_03.py

import contextlib
import io
import re
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent


def run_code(code, filename, answers=None):
    """Run some code, answering its input() questions from `answers`.

    `answers` maps a word in the question to the reply, for example
    {"Amount": "75"}. Returns (its variables, what it printed).
    """
    answers = answers or {}

    def fake_input(prompt=""):
        for word, reply in answers.items():
            if word.lower() in prompt.lower():
                return reply
        raise AssertionError(
            f"Your code asked {prompt!r}, but the tests expected one of: "
            + ", ".join(repr(word) for word in answers)
        )

    variables = {"__name__": "__main__", "input": fake_input}
    printed = io.StringIO()
    with contextlib.redirect_stdout(printed):
        exec(compile(code, filename, "exec"), variables)
    return variables, printed.getvalue().strip().splitlines()


def run_exercise(**starting_values):
    """Run lesson_03.py with some starting lines swapped, e.g. number=-4."""
    path = HERE / "lesson_03.py"
    code = path.read_text()
    for name, value in starting_values.items():
        pattern = rf"^{name}\s*=.*$"
        assert re.search(pattern, code, re.MULTILINE), (
            f"Could not find the line '{name} = ...' in lesson_03.py. Please put it back."
        )
        code = re.sub(pattern, f"{name} = {value!r}", code, count=1, flags=re.MULTILINE)
    return run_code(code, str(path))


def test_part_1_sizing_a_number():
    for number, size in [(7, "small"), (-4, "negative"), (0, "zero"), (10, "large"), (250, "large"), (1, "small")]:
        variables, lines = run_exercise(number=number)
        assert "size" in variables, "There is no variable called size in lesson_03.py"
        assert variables["size"] == size, (
            f"With number = {number}, expected size to be {size!r}, but it is {variables['size']!r}"
        )
        wanted = f"{number} is {size}"
        assert wanted in lines, (
            f"With number = {number}, expected a printed line saying: {wanted}\n"
            f"Printed lines were: {lines}"
        )


def test_part_2_at_the_door():
    cases = [
        # age, has_ticket, day, can_enter, is_weekend
        (25, True, "Saturday", True, True),
        (18, True, "Sunday", True, True),
        (17, True, "Monday", False, False),
        (40, False, "Friday", False, False),
        (12, False, "Sunday", False, True),
    ]
    for age, has_ticket, day, can_enter, is_weekend in cases:
        setup = f"With age = {age}, has_ticket = {has_ticket} and day = {day!r}"
        variables, lines = run_exercise(age=age, has_ticket=has_ticket, day=day)
        for name, expected in [("can_enter", can_enter), ("is_weekend", is_weekend)]:
            assert name in variables, f"There is no variable called {name} in lesson_03.py"
            assert variables[name] == expected, (
                f"{setup},\nexpected {name} to be {expected}, but it is {variables[name]!r}"
            )
        wanted = "Welcome in!" if can_enter else "Sorry, no entry."
        unwanted = "Sorry, no entry." if can_enter else "Welcome in!"
        assert wanted in lines and unwanted not in lines, (
            f"{setup},\nexpected the line {wanted!r} and not {unwanted!r}.\n"
            f"Printed lines were: {lines}"
        )


def test_capstone_spending_limit():
    path = REPO / "pocket_ledger" / "main.py"
    code = path.read_text()
    variables, _ = run_code(code, str(path), {"Amount": "1", "Description": "tea"})
    assert "limit" in variables, "There is no variable called limit in pocket_ledger/main.py"
    limit = variables["limit"]
    assert type(limit) in (int, float), f"Expected limit to be a number, but it is {limit!r}"

    for amount, warn in [(limit + 25, True), (limit, False), (limit - 1, False)]:
        typed = f"With limit = {limit}, when the test typed {str(amount)!r} for Amount and 'dinner' for Description"
        _, lines = run_code(code, str(path), {"Amount": str(amount), "Description": "dinner"})
        warning = f"Warning: dinner is over your limit of {limit:.2f}"
        if warn:
            assert warning in lines, (
                f"{typed},\nexpected a printed line saying: {warning}\nPrinted lines were: {lines}"
            )
        else:
            warnings = [line for line in lines if line.startswith("Warning")]
            assert not warnings, (
                f"{typed},\nexpected no warning, because {amount} is not over the limit.\n"
                f"Printed lines were: {lines}"
            )


if __name__ == "__main__":
    failed = 0
    for test in (test_part_1_sizing_a_number, test_part_2_at_the_door, test_capstone_spending_limit):
        try:
            test()
            print(f"PASS  {test.__name__}")
        except AssertionError as problem:
            failed += 1
            print(f"FAIL  {test.__name__}\n      {problem}")
        except Exception as problem:
            failed += 1
            print(f"FAIL  {test.__name__}\n      The code crashed: {type(problem).__name__}: {problem}")
    print("All tests passed" if not failed else f"{failed} test(s) failed")

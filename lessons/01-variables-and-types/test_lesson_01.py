# Tests for Lesson 1. You do not need to understand this file yet.
# Run it from the top folder of the repository:
#     python3 lessons/01-variables-and-types/test_lesson_01.py

import contextlib
import io
import re
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent


def run_code(code, filename):
    """Run some code, returning (its variables, what it printed)."""
    # Later lessons make Pocket Ledger ask questions, so the tests answer
    # them instead of waiting for you: "1" three times, then "done".
    answers = ["1"] * 3

    def fake_input(prompt=""):
        return answers.pop(0) if answers else "done"

    variables = {"__name__": "__main__", "input": fake_input}
    printed = io.StringIO()
    with contextlib.redirect_stdout(printed):
        exec(compile(code, filename, "exec"), variables)
    return variables, printed.getvalue().strip().splitlines()


def run_exercise(celsius=None):
    path = HERE / "lesson_01.py"
    code = path.read_text()
    if celsius is not None:
        assert re.search(r"^celsius\s*=", code, re.MULTILINE), (
            "Could not find the line 'celsius = 25' in lesson_01.py. Please put it back."
        )
        code = re.sub(r"^celsius\s*=.*$", f"celsius = {celsius}", code, flags=re.MULTILINE)
    return run_code(code, str(path))


def check_type(variables, name, expected):
    assert name in variables, f"There is no variable called {name} in lesson_01.py"
    actual = type(variables[name])
    assert actual is expected, (
        f"Expected {name} to be a {expected.__name__}, "
        f"but it is a {actual.__name__}: {variables[name]!r}"
    )


def test_part_1_types():
    variables, _ = run_exercise()
    check_type(variables, "year", int)
    check_type(variables, "height_m", float)
    check_type(variables, "first_name", str)
    check_type(variables, "likes_coffee", bool)


def check_line(line, celsius, unit, expected):
    start = f"{celsius} C is "
    shape = f"{celsius} C is <number> {unit}"
    assert line.startswith(start) and line.endswith(f" {unit}"), (
        f"Expected a line shaped like: {shape}\nGot: {line!r}"
    )
    number = line[len(start):-len(unit) - 1]
    try:
        value = float(number)
    except ValueError:
        raise AssertionError(f"Expected a number in this line, got {number!r}: {line!r}")
    assert abs(value - expected) < 0.001, (
        f"With celsius = {celsius}, expected {expected} {unit}, got {number} {unit}"
    )


def test_part_2_temperature():
    for celsius, fahrenheit, kelvin in [(25, 77.0, 298.15), (100, 212.0, 373.15), (0, 32.0, 273.15)]:
        variables, lines = run_exercise(celsius)
        for name, expected in [("fahrenheit", fahrenheit), ("kelvin", kelvin)]:
            assert name in variables, f"There is no variable called {name} in lesson_01.py"
            assert abs(variables[name] - expected) < 0.001, (
                f"With celsius = {celsius}, expected {name} to be {expected}, "
                f"but it is {variables[name]}"
            )
        assert len(lines) >= 2, (
            f"Expected two printed lines, but lesson_01.py printed {len(lines)}"
        )
        check_line(lines[-2], celsius, "F", fahrenheit)
        check_line(lines[-1], celsius, "K", kelvin)


def test_capstone_total():
    path = REPO / "pocket_ledger" / "main.py"
    variables, lines = run_code(path.read_text(), str(path))
    for name in ("expense_1", "expense_2", "expense_3", "total"):
        assert name in variables, f"There is no variable called {name} in pocket_ledger/main.py"
    expected = variables["expense_1"] + variables["expense_2"] + variables["expense_3"]
    assert abs(variables["total"] - expected) < 0.001, (
        f"Expected total to be the three expenses added up ({expected}), "
        f"but it is {variables['total']}"
    )
    assert lines and lines[0] == "Pocket Ledger", (
        "Expected the first printed line to still be: Pocket Ledger"
    )
    wanted = f"Total spent: {variables['total']}"
    assert wanted in lines, (
        f"Expected a printed line saying: {wanted}\nPrinted lines were: {lines}"
    )


if __name__ == "__main__":
    failed = 0
    for test in (test_part_1_types, test_part_2_temperature, test_capstone_total):
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

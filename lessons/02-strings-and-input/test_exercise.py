# Tests for Lesson 2. You do not need to understand this file yet.
# Run it from the top folder of the repository:
#     python3 lessons/02-strings-and-input/test_exercise.py

import contextlib
import io
import re
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent


def run_code(code, filename, answers):
    """Run some code, answering its input() questions from `answers`.

    `answers` maps a word in the question to the reply, for example
    {"Bill": "40"}. Returns (its variables, what it printed).
    """

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


EXERCISE_ANSWERS = {"Bill": "40", "Tip": "15"}


def run_exercise(raw_name=None, answers=EXERCISE_ANSWERS):
    path = HERE / "exercise.py"
    code = path.read_text()
    if raw_name is not None:
        assert re.search(r"^raw_name\s*=", code, re.MULTILINE), (
            "Could not find the line 'raw_name = ...' in exercise.py. Please put it back."
        )
        code = re.sub(r"^raw_name\s*=.*$", f"raw_name = {raw_name!r}", code, flags=re.MULTILINE)
    return run_code(code, str(path), answers)


def check_variable(variables, name, expected, where="exercise.py"):
    assert name in variables, f"There is no variable called {name} in {where}"
    assert variables[name] == expected, (
        f"Expected {name} to be {expected!r}, but it is {variables[name]!r}"
    )


def test_part_1_tidying_text():
    for raw_name, clean in [("   tOM sMITH   ", "Tom Smith"), ("  ada LOVELACE ", "Ada Lovelace")]:
        variables, lines = run_exercise(raw_name)
        check_variable(variables, "clean_name", clean)
        check_variable(variables, "shout", clean.upper())
        check_variable(variables, "name_length", len(clean))
        check_variable(variables, "greeting", f"Hello, {clean}!")
        assert f"Hello, {clean}!" in lines, (
            f"Expected a printed line saying: Hello, {clean}!\nPrinted lines were: {lines}"
        )


def test_part_2_tip_calculator():
    for bill, percent, tip, total in [("40", "15", "6.00", "46.00"), ("12.50", "20", "2.50", "15.00")]:
        _, lines = run_exercise(answers={"Bill": bill, "Tip": percent})
        for wanted in (f"Tip: {tip}", f"Total: {total}"):
            assert wanted in lines, (
                f"With a bill of {bill} and a {percent}% tip, expected a printed line saying: {wanted}\n"
                f"Printed lines were: {lines}"
            )


def test_capstone_add_expense():
    path = REPO / "pocket_ledger" / "main.py"
    for typed_amount, typed_description, amount, description in [
        ("4.5", "coffee", 4.5, "coffee"),
        ("12", "  lunch with Sam  ", 12.0, "lunch with Sam"),
    ]:
        answers = {"Amount": typed_amount, "Description": typed_description}
        variables, lines = run_code(path.read_text(), str(path), answers)
        assert "amount" in variables, "There is no variable called amount in pocket_ledger/main.py"
        assert type(variables["amount"]) in (int, float), (
            f"Expected amount to be a number, but it is a {type(variables['amount']).__name__}: "
            f"{variables['amount']!r}. Remember input() always gives back a string."
        )
        assert variables["amount"] == amount, (
            f"When {typed_amount!r} was typed, expected amount to be {amount}, "
            f"but it is {variables['amount']!r}"
        )
        check_variable(variables, "description", description, "pocket_ledger/main.py")
        wanted = f"Added {description}: {amount:.2f}"
        assert wanted in lines, (
            f"Expected a printed line saying: {wanted}\nPrinted lines were: {lines}"
        )


if __name__ == "__main__":
    failed = 0
    for test in (test_part_1_tidying_text, test_part_2_tip_calculator, test_capstone_add_expense):
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

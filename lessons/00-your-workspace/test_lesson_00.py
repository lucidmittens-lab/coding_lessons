# Tests for Lesson 0. You do not need to understand this file yet.
# Run it from the top folder of the repository:
#     python lessons/00-your-workspace/test_lesson_00.py

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent


# Later lessons make Pocket Ledger ask questions, so the tests type
# some answers in for it instead of waiting for you.
ANSWERS = "1\n" * 3 + "done\n" * 50


def run(path):
    result = subprocess.run(
        [sys.executable, str(path)], capture_output=True, text=True, input=ANSWERS
    )
    return result.stdout.strip(), result.stderr.strip()


def test_exercise_prints_hello_world():
    output, errors = run(HERE / "lesson_00.py")
    assert not errors, f"lesson_00.py crashed with this error:\n{errors}"
    assert output == "Hello, world!", (
        f"Expected lesson_00.py to print: Hello, world!\n"
        f"It printed: {output!r}"
    )


def test_capstone_prints_pocket_ledger():
    main = REPO / "pocket_ledger" / "main.py"
    assert main.exists(), "pocket_ledger/main.py does not exist yet"
    output, errors = run(main)
    assert not errors, f"pocket_ledger/main.py crashed with this error:\n{errors}"
    # Later lessons add more lines, so only the first line is checked here.
    first_line = output.splitlines()[0] if output else ""
    assert first_line == "Pocket Ledger", (
        f"Expected pocket_ledger/main.py to print: Pocket Ledger\n"
        f"It printed: {output!r}"
    )


if __name__ == "__main__":
    failed = 0
    for test in (test_exercise_prints_hello_world, test_capstone_prints_pocket_ledger):
        try:
            test()
            print(f"PASS  {test.__name__}")
        except AssertionError as problem:
            failed += 1
            print(f"FAIL  {test.__name__}\n      {problem}")
    print("All tests passed" if not failed else f"{failed} test(s) failed")

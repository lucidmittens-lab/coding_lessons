# Notes for Claude

This repository is Tom's Python course. Tom is a near beginner and writes the code himself.

- Never fill in exercise files (`lesson_NN.py`) or capstone steps for Tom. Write lessons, tests and hints; review his work and explain.
- Lessons live in `lessons/NN-name/` with `README.md`, `lesson_NN.py` (the exercise) and `test_lesson_NN.py`; names are unique so editor tabs and pytest can tell them apart. Tests must run with plain `python lessons/NN-name/test_lesson_NN.py` until Lesson 12 introduces pytest, and should also work under pytest.
- Only use concepts already taught. Check `docs/lesson-plan.md` for the order.
- Test failure messages are written for a beginner: say what was expected and what happened.
- Every earlier lesson's tests must keep passing as the capstone grows: capstone tests check only what their own lesson added.
- Exercise file comments spell out every target value, so Tom never has to switch to the README to find what's asked.
- When a test fails, its message says what the test typed in or changed, so sample inputs never look like they came from nowhere.

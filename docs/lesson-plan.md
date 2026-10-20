# Coding Lessons: Lesson Plan

A path from near-beginner to writing production-quality Python, in seven modules. Every lesson has the same three parts:

1. **Concept**: one idea, explained briefly with a small example.
2. **Exercise**: a short, self-contained task that proves you understand it. Each comes with tests you make pass.
3. **Capstone step**: apply the same idea to the one project you grow across the whole course.

## The capstone: Pocket Ledger

A personal expense tracker. You start with a script that adds up a few numbers and finish with an installable, tested, packaged app that has a command line, a database, and a small web API.

Why this project: it is small enough to understand completely, but it naturally needs every topic in the course.

| Area | Where it shows up in Pocket Ledger |
|---|---|
| 1. Fundamentals | Store expenses, total them, read and write files, handle bad input |
| 2. Practical skills | Git history, tests, a virtual environment, logging, debugging real bugs |
| 3. Data structures & algorithms | Group by category, find duplicates, sort and search transactions, undo history |
| 4. Design principles | Split into modules, an `Expense` class, a storage interface |
| 5. Functional style | Pure functions for reports, generators that stream big CSV files |
| 6. Patterns & architecture | Adapters for different bank CSV formats, strategies for categorising, a factory for exporters, dependency injection for storage |
| 7. Production quality | SQLite database, a web API, config files, packaging, security, CI |

## How a lesson works

- Each lesson lives in the repository as `lessons/NN-name/` with a short `README.md` (the concept), an `exercise.py` to fill in, and `test_exercise.py` that tells you when you are done.
- The capstone lives in `pocket_ledger/` and grows by one step per lesson. Each capstone step is one commit (later, one pull request).
- From lesson 7 onward, you open a pull request for each capstone step and I review it, the way a teammate would.

### When you get stuck

Getting stuck is what ended the last course, so here is the rule: **if you have been stuck for 20 minutes, post in the thread.** Paste what you tried and the error. Being stuck is information about the lesson, not about you. I will either unblock you or split the lesson into smaller steps.

## Repository layout (once the repo exists)

```
coding-lessons/
├── lessons/
│   ├── 01-variables-and-types/
│   │   ├── README.md
│   │   ├── exercise.py
│   │   └── test_exercise.py
│   └── ...
├── pocket_ledger/        # the capstone, grows each lesson
├── tests/                # capstone tests
└── README.md
```

---

## Module 0: Setup (1 lesson)

### 0. Your workspace
- **Concept**: what Python is, how to run a file, what an editor and a terminal are for.
- **Exercise**: install Python 3 and VS Code, run `print("hello")` from a file and from the terminal.
- **Capstone step**: create `pocket_ledger/main.py` that prints "Pocket Ledger". Commit it (I will walk you through your first commit).

## Module 1: Python fundamentals (8 lessons)

### 1. Variables and types
- **Concept**: `int`, `float`, `str`, `bool`; assigning names to values; `type()`.
- **Exercise**: convert temperatures and format the result as text.
- **Capstone step**: store three expenses as variables and print their total.

### 2. Strings and input
- **Concept**: string methods, f-strings, `input()`, converting text to numbers.
- **Exercise**: a tip calculator that asks for a bill amount.
- **Capstone step**: ask the user for an expense amount and description, then print it back nicely.

### 3. Conditions
- **Concept**: `if` / `elif` / `else`, comparisons, `and` / `or` / `not`.
- **Exercise**: classify a number as negative, zero, small or large.
- **Capstone step**: warn when a single expense is over a set limit.

### 4. Loops
- **Concept**: `while` and `for`, `range()`, `break` and `continue`.
- **Exercise**: FizzBuzz, then sum the digits of a number.
- **Capstone step**: keep asking for expenses until the user types `done`, then print the total.

### 5. Lists and dictionaries (first look)
- **Concept**: storing many values; a dictionary as a labelled record.
- **Exercise**: track scores for a few players and print the winner.
- **Capstone step**: store each expense as a dict (`amount`, `category`, `description`) in a list.

### 6. Functions
- **Concept**: `def`, parameters, return values, why functions beat copy-paste.
- **Exercise**: write `is_even`, `average`, and `longest_word`.
- **Capstone step**: move the code into functions: `add_expense()`, `total()`, `print_summary()`.

### 7. Exceptions
- **Concept**: what tracebacks mean, `try` / `except`, raising your own errors.
- **Exercise**: a `safe_divide` and a number parser that rejects bad input politely.
- **Capstone step**: stop the program from crashing when someone types "ten" as an amount.

### 8. Files, modules and the standard library
- **Concept**: reading and writing files, the `csv` and `json` modules, `import`, splitting code across files.
- **Exercise**: count word frequency in a text file using `collections.Counter`.
- **Capstone step**: save expenses to `expenses.csv` and load them on startup, so data survives between runs. Move the file code into its own module, `storage.py`.

## Module 2: Practical programming skills (6 lessons)

### 9. Git properly
- **Concept**: commits, branches, diffs, pushing to GitHub, pull requests.
- **Exercise**: a practice repo: make a branch, change a file, open and merge a pull request.
- **Capstone step**: from now on, every capstone step is a branch and a pull request.

### 10. Reading errors and debugging
- **Concept**: reading a traceback bottom-up, `print` debugging, the VS Code debugger, breakpoints.
- **Exercise**: fix three deliberately broken programs.
- **Capstone step**: I plant a bug in Pocket Ledger; you find it with the debugger.

### 11. Testing with pytest
- **Concept**: what a test is, `assert`, writing tests before fixing a bug.
- **Exercise**: write tests for the Module 1 exercise functions.
- **Capstone step**: add `tests/` with tests for `total()` and the CSV loading.

### 12. Virtual environments and dependencies
- **Concept**: why projects need their own environment, `venv`, `pip`, `requirements.txt` then `pyproject.toml`.
- **Exercise**: create a venv, install a package, freeze its version.
- **Capstone step**: give Pocket Ledger a venv and install `pytest` and `rich` (for nicer tables) as declared dependencies.

### 13. Logging
- **Concept**: the `logging` module, levels, why not to leave `print` everywhere.
- **Exercise**: add logging to a small script and change the level from the command line.
- **Capstone step**: log file loads, saves and errors to `pocket_ledger.log`.

### 14. Reading documentation
- **Concept**: how to read the Python docs and a library's docs, finding examples, reading a function signature.
- **Exercise**: use only the docs to solve a small task with `datetime`.
- **Capstone step**: add a date to each expense and a "this month" summary using `datetime`.

## Module 3: Data structures and algorithms (6 lessons)

### 15. Lists, dictionaries and sets in depth
- **Concept**: what each is good at, membership tests, comprehensions.
- **Exercise**: find the common and unique items between two shopping lists.
- **Capstone step**: totals by category with a dictionary; list of categories used with a set.

### 16. Big-O: how fast is this?
- **Concept**: counting steps, O(1), O(n), O(n²), why a set lookup beats a list lookup.
- **Exercise**: time a list search against a set search on a million items.
- **Capstone step**: detect duplicate expenses on import, first the slow way, then the fast way, and measure both.

### 17. Searching
- **Concept**: linear search, binary search on sorted data.
- **Exercise**: implement binary search yourself, then compare with `bisect`.
- **Capstone step**: find all expenses between two dates quickly once they are sorted.

### 18. Sorting
- **Concept**: how a simple sort works (insertion sort), then `sorted()` with `key=`.
- **Exercise**: write insertion sort; sort people by age then by name.
- **Capstone step**: sort the expense list by date, amount or category from a menu option.

### 19. Stacks and queues
- **Concept**: last-in-first-out and first-in-first-out, `list` and `collections.deque`.
- **Exercise**: check whether brackets in a string are balanced.
- **Capstone step**: an "undo last change" command backed by a stack.

### 20. Choosing a data structure
- **Concept**: `namedtuple`, `dataclass`, when to use which structure.
- **Exercise**: pick and justify structures for three short scenarios.
- **Capstone step**: replace the expense dicts with a `@dataclass Expense`.

## Module 4: Software design principles (5 lessons)

### 21. Modules and separation of concerns
- **Concept**: one job per module; keeping input/output apart from logic.
- **Exercise**: untangle a 60-line script into three modules.
- **Capstone step**: split Pocket Ledger into `models.py`, `storage.py`, `reports.py` and `cli.py`.

### 22. Classes and objects
- **Concept**: `class`, `__init__`, methods, `self`, instances.
- **Exercise**: a `BankAccount` class with deposit, withdraw and a balance.
- **Capstone step**: a `Ledger` class that holds expenses and offers `add`, `remove`, `total`.

### 23. Encapsulation
- **Concept**: hiding internals, properties, validation inside the class.
- **Exercise**: make `BankAccount` refuse negative balances.
- **Capstone step**: `Expense` refuses negative amounts and unknown categories at creation.

### 24. Interfaces and abstract classes
- **Concept**: agreeing on what methods something has, `abc.ABC`, `typing.Protocol`.
- **Exercise**: a `Shape` interface with `Circle` and `Square`.
- **Capstone step**: a `Storage` interface; `CsvStorage` implements it.

### 25. Inheritance, carefully
- **Concept**: subclasses, `super()`, when inheritance helps and when it hurts.
- **Exercise**: an `Animal` hierarchy, then spot where it goes wrong.
- **Capstone step**: add `JsonStorage` and see what the two storages share.

## Module 5: Functional programming concepts (5 lessons)

### 26. Pure functions and side effects
- **Concept**: same input, same output, nothing else changed; why pure functions are easy to test.
- **Exercise**: rewrite three impure functions as pure ones.
- **Capstone step**: make every function in `reports.py` pure: take expenses in, return results out.

### 27. Immutability
- **Concept**: tuples, frozen dataclasses, why shared mutable state causes bugs.
- **Exercise**: find the bug caused by a mutable default argument.
- **Capstone step**: make `Expense` frozen; adding and editing return new objects.

### 28. Functions as values and composition
- **Concept**: passing functions around, `lambda`, `map`, `filter`, small functions combined.
- **Exercise**: build a text pipeline from small functions.
- **Capstone step**: composable filters: "food, over 20, this month".

### 29. Iterators and generators
- **Concept**: `iter`, `next`, `yield`, processing data one item at a time.
- **Exercise**: a generator that yields the Fibonacci numbers; one that reads a huge file line by line.
- **Capstone step**: stream CSV imports with a generator so a file with 100,000 rows uses little memory.

### 30. Avoiding shared state
- **Concept**: globals, why they hurt, passing what you need instead.
- **Exercise**: remove globals from a small program without changing its behaviour (tests prove it).
- **Capstone step**: remove any remaining global variables from Pocket Ledger.

## Module 6: Design patterns and architecture (6 lessons)

### 31. Composition over inheritance
- **Concept**: "has a" versus "is a"; building behaviour from parts.
- **Exercise**: rebuild the Animal hierarchy from lesson 25 with composition.
- **Capstone step**: replace the storage inheritance from lesson 25 with composition.

### 32. Strategy
- **Concept**: swap an algorithm without changing the code that uses it.
- **Exercise**: interchangeable discount rules for a shop.
- **Capstone step**: categorisation strategies: by keyword rules, or by "same as last time for this shop".

### 33. Adapter
- **Concept**: make an awkward interface fit the one your code expects.
- **Exercise**: adapt a third-party temperature sensor class.
- **Capstone step**: import CSVs from two different (made-up) banks, each with its own column layout, through adapters.

### 34. Factory
- **Concept**: one place that decides which object to create.
- **Exercise**: a shape factory driven by a string.
- **Capstone step**: an exporter factory for CSV, JSON and Markdown reports.

### 35. Dependency injection
- **Concept**: hand an object what it needs instead of letting it create it; why this makes testing easy.
- **Exercise**: test a function that sends email by injecting a fake sender.
- **Capstone step**: `Ledger` receives its `Storage`; tests use an in-memory fake.

### 36. Organising a larger application
- **Concept**: layers (interface, application logic, storage), package structure, where things belong.
- **Exercise**: sort a list of files into the right layer.
- **Capstone step**: restructure into a proper package under `src/pocket_ledger/` with a command-line entry point.

## Module 7: Production-quality software (7 lessons)

### 37. A real test suite
- **Concept**: fixtures, parametrised tests, coverage, testing edge cases.
- **Exercise**: reach full coverage on a small module.
- **Capstone step**: raise Pocket Ledger coverage and add GitHub Actions so tests run on every pull request.

### 38. Databases with SQLite
- **Concept**: tables, SQL basics, the `sqlite3` module, transactions.
- **Exercise**: create a table, insert, query, update.
- **Capstone step**: `SqliteStorage` implements the `Storage` interface. Nothing else in the app changes, which proves the design from Modules 4 and 6 works.

### 39. Configuration
- **Concept**: config files, environment variables, keeping settings out of code.
- **Exercise**: read settings from a TOML file with defaults.
- **Capstone step**: choose storage type, database path and spending limits from a config file.

### 40. Building an API
- **Concept**: HTTP basics, JSON APIs, FastAPI, testing an API.
- **Exercise**: a two-endpoint "hello" API with tests.
- **Capstone step**: a web API for Pocket Ledger: list, add and summarise expenses.

### 41. Security basics
- **Concept**: never trust input, SQL injection and parameterised queries, secrets out of git, dependency scanning.
- **Exercise**: break, then fix, a deliberately vulnerable query.
- **Capstone step**: audit Pocket Ledger: parameterised queries, input validation on the API, an API key read from the environment.

### 42. Packaging
- **Concept**: `pyproject.toml`, building a wheel, versioning, installing your own package.
- **Exercise**: package a tiny utility and install it in a fresh venv.
- **Capstone step**: make Pocket Ledger installable with `pip install .` and runnable as `ledger` from anywhere.

### 43. Maintainability
- **Concept**: type hints, a formatter and linter (`ruff`), docstrings, a good README, refactoring safely with tests.
- **Exercise**: tidy a messy module until the linter and type checker are happy.
- **Capstone step**: type-check and lint the whole project in CI, write the README, and tag version 1.0.

---

## Pace

There is no deadline. A reasonable rhythm is one or two lessons a week, which puts the whole course at roughly six to nine months. Modules 1 and 2 matter most; we slow down there as much as needed. If a lesson takes more than a couple of sittings, that is a sign to split it, and I will.

## What happens next

1. Create an empty GitHub repository (for example `coding-lessons`) and add it to this project.
2. I set up the folder layout and the first lesson (Lesson 0) in it for you to work through.
3. You do the work and commit it yourself; I review, explain, and write the next lesson.

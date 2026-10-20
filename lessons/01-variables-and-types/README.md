# Lesson 1: Variables and types

## The concept

### Variables

A **variable** is a name that points at a value. You create one with `=`:

```python
city = "Lisbon"
population = 545000
```

Read `=` as "now means", not "equals": *`city` now means `"Lisbon"`*. You can point a name at a new value later, and you can use other variables to work out a new one:

```python
apples = 3
apples = apples + 2   # apples now means 5
```

Python runs from top to bottom, so a variable must be created before the line that uses it.

Names can use letters, numbers and `_`, but can't start with a number. By convention, Python names are lowercase with underscores: `monthly_total`, not `MonthlyTotal` or `monthlytotal`.

### Types

Every value has a **type**, which decides what you can do with it. The four you'll use constantly:

| Type | What it is | Examples |
|---|---|---|
| `int` | whole numbers | `3`, `-12`, `2026` |
| `float` | numbers with a decimal point | `3.5`, `0.1`, `-40.0` |
| `str` | text ("string" of characters), in quotes | `"hello"`, `'Tom'`, `"42"` |
| `bool` | yes/no values | `True`, `False` |

`type()` tells you a value's type:

```python
print(type(3))        # <class 'int'>
print(type(3.0))      # <class 'float'>
print(type("3"))      # <class 'str'>
print(type(True))     # <class 'bool'>
```

Note that `3` and `"3"` are different things. One is a number you can do maths with, the other is just a piece of text that happens to look like a number.

### Arithmetic

`+  -  *  /` work as you'd expect. Dividing with `/` always gives a `float`, even when it divides evenly: `10 / 2` is `5.0`.

Floats are stored in binary, so some decimals can't be stored exactly:

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

This isn't a bug in your code. Every programming language does it. For now, just know it happens; we'll deal with it properly when Pocket Ledger handles money in later lessons.

### Printing several things

`print` can take several values separated by commas. It puts a space between them:

```python
name = "Tom"
age = 40
print(name, "is", age)    # Tom is 40
```

## The exercise

Open `lesson_01.py`. It has two parts.

**Part 1: Types.** Create four variables:
- `year`, an `int`
- `height_m`, a `float` (your height in metres)
- `first_name`, a `str`
- `likes_coffee`, a `bool`

**Part 2: Temperature.** The file starts with `celsius = 25`. Below it:
1. Create `fahrenheit`, worked out from `celsius`. The formula is: multiply by 9, divide by 5, add 32.
2. Create `kelvin`, worked out from `celsius`. The formula is: add 273.15.
3. Print two lines in exactly this shape:
   ```
   25 C is 77.0 F
   25 C is 298.15 K
   ```

Your code must **work out** the answers from `celsius`, not type them in. The tests check this by changing `celsius` to other values and running your file again. Try it yourself: change `celsius` to `100`, run the file, and check the answers make sense (water boils at 212 F).

Run it:
```
python3 lessons/01-variables-and-types/lesson_01.py
```

Check it:
```
python3 lessons/01-variables-and-types/test_lesson_01.py
```

## Capstone step

Pocket Ledger starts tracking money. In `pocket_ledger/main.py`, keep the `Pocket Ledger` line at the top, then:

1. Create three variables, `expense_1`, `expense_2` and `expense_3`, for three things you spent money on recently (just the amounts, like `4.5`).
2. Create a variable `total` that adds them up. Work it out from the three variables; don't type the answer in.
3. Print the total, so running the program shows:
   ```
   Pocket Ledger
   Total spent: 18.5
   ```
   (with your own total).

The Lesson 1 tests check this too. Make sure Lesson 0's tests still pass as well.

## Commit

When both lessons' tests pass:

```
git add lessons/01-variables-and-types/lesson_01.py pocket_ledger/main.py
git commit -m "Lesson 1: variables, types and a first total"
git push
```

## Done when

- `python3 lessons/01-variables-and-types/test_lesson_01.py` prints `All tests passed`.
- `python3 lessons/00-your-workspace/test_lesson_00.py` still prints `All tests passed`.
- Your commit is on GitHub.

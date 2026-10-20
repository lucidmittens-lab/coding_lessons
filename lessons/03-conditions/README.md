# Lesson 3: Conditions

Until now your programs ran every line, top to bottom. This lesson lets them make decisions: run some lines only when something is true.

## The concept

### Comparisons

A comparison asks a question and answers with a `bool`, either `True` or `False`:

| Code | Means |
|---|---|
| `a == b` | is a equal to b? (two `=` signs; one `=` is for creating variables) |
| `a != b` | is a different from b? |
| `a < b`, `a > b` | less than, greater than |
| `a <= b`, `a >= b` | less than or equal, greater than or equal |

```python
print(5 > 3)         # True
print(5 == 5.0)      # True
print("a" == "A")    # False, capitals matter
```

### if

`if` runs the lines under it only when the comparison is `True`:

```python
temperature = 30
if temperature > 25:
    print("It's hot")
    print("Drink some water")
print("This line always runs")
```

Two things make this work:
- The `if` line ends with a **colon** `:`.
- The lines that belong to it are **indented** by four spaces. Indentation is how Python knows where the `if` block ends. VS Code adds the four spaces for you after a colon; press Enter, then Backspace when you want to step back out.

### else and elif

`else` runs when the `if` was `False`. `elif` ("else if") tries another question. Python checks each one in order and runs **only the first** that's true:

```python
score = 72
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"     # this one runs; Python stops checking here
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(grade)        # B
```

Because Python stops at the first match, order matters. If `score >= 50` came first, a score of 95 would get a C.

### and, or, not

These combine comparisons:

```python
age = 20
has_id = True
print(age >= 18 and has_id)      # True only if both are True
day = "Sunday"
print(day == "Saturday" or day == "Sunday")   # True if either is True
print(not has_id)                # flips True to False
```

You can store the result in a variable, just like any other value: `is_weekend = day == "Saturday" or day == "Sunday"`.

### A common mistake

```python
if day == "Saturday" or "Sunday":    # wrong
```

This looks right but is always `True`, because Python reads it as `(day == "Saturday") or ("Sunday")`, and a non-empty string counts as true. Write the comparison out in full both times.

## The exercise

Everything you need is also written in the comments of `lesson_03.py`.

**Part 1: Sizing a number.** The file sets `number = 7`. Create a variable `size`:
- `"negative"` if the number is below 0
- `"zero"` if it is 0
- `"small"` if it is above 0 but below 10
- `"large"` if it is 10 or more

Then print a line like `7 is small`.

**Part 2: At the door.** The file sets `age = 25`, `has_ticket = True` and `day = "Saturday"`. Create:
- `can_enter`: `True` when age is at least 18 **and** they have a ticket.
- `is_weekend`: `True` when the day is `"Saturday"` **or** `"Sunday"`.

Then print `Welcome in!` if they can enter, otherwise `Sorry, no entry.`

The tests change all of these starting values, so your code has to make the decisions itself.

Run it:
```
python3 lessons/03-conditions/lesson_03.py
```

Check it:
```
python3 lessons/03-conditions/test_lesson_03.py
```

## Capstone step

Pocket Ledger gets a spending limit. In `pocket_ledger/main.py`:

1. Near the top, add `limit = 50`. (Use any number you like; the tests read whatever you choose.)
2. At the end, after the `Added ...` line, print a warning **only** if the amount is over the limit:
   ```
   Warning: dinner is over your limit of 50.00
   ```
   Use the description, and show the limit with two decimal places. An amount exactly equal to the limit is not over it.

So a run with a big expense looks like:
```
Pocket Ledger
Total spent: 10.68
Amount: 75
Description: dinner
Added dinner: 75.00
Warning: dinner is over your limit of 50.00
```
and a small expense prints no warning at all.

## Commit

When this lesson's tests pass, and Lessons 0 to 2 still pass:

```
git add lessons/03-conditions/lesson_03.py pocket_ledger/main.py
git commit -m "Lesson 3: conditions and a spending limit"
git push
```

## Done when

- `python3 lessons/03-conditions/test_lesson_03.py` prints `All tests passed`.
- Lessons 0, 1 and 2 tests still print `All tests passed`.
- Your commit is on GitHub.

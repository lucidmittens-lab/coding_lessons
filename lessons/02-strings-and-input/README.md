# Lesson 2: Strings and input

So far your programs always do the same thing. This lesson lets them ask the person running them for information, and tidy up the text they get back.

## The concept

### Strings

A string is text inside quotes. Single or double quotes both work; pick whichever avoids a clash with the text:

```python
"It's sunny"      # double quotes, because the text has an apostrophe
'She said "hi"'   # single quotes, because the text has double quotes
```

`+` joins strings together, and `len()` counts the characters:

```python
first = "Pocket"
second = "Ledger"
print(first + " " + second)   # Pocket Ledger
print(len(first))             # 6
```

### String methods

A **method** is an action that belongs to a value. You call it with a dot after the value. Strings have lots of methods; these are the everyday ones:

```python
messy = "   hELLo wORLD   "
print(messy.strip())          # "hELLo wORLD"   removes spaces at both ends
print(messy.lower())          # "   hello world   "
print(messy.upper())          # "   HELLO WORLD   "
print(messy.strip().title())  # "Hello World"   capital at the start of each word
print("a-b-c".replace("-", " "))   # "a b c"
```

Notice `messy.strip().title()`: the result of `strip()` is a new string, and `.title()` is called on that. You can chain methods like this.

Methods never change the original string. `messy` is still messy afterwards. To keep the result, store it: `clean = messy.strip()`.

### f-strings

An **f-string** puts variables straight into text. Write `f` before the quotes and put variables in `{curly brackets}`:

```python
name = "Tom"
age = 30
print(f"{name} is {age} years old")   # Tom is 30 years old
```

Add `:.2f` inside the brackets to show a number with exactly two decimal places, which is perfect for money:

```python
price = 3.5
print(f"Price: {price:.2f}")   # Price: 3.50
print(f"Price: {10 / 3:.2f}")  # Price: 3.33
```

### input()

`input()` shows a prompt, waits for the person to type something and press Enter, and gives back what they typed:

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

Put a space at the end of the prompt, otherwise their typing runs into your text.

### Text is not a number

`input()` **always** gives back a string, even if the person types digits. `"40"` is text, and `"40" + 5` is an error. Convert it first:

```python
age = int(input("Age: "))          # whole numbers
price = float(input("Price: "))    # numbers with decimals
```

If someone types `ten`, `float()` crashes with a `ValueError`. That's fine for now; Lesson 7 shows how to handle it politely.

## The exercise

Open `exercise.py`. It has two parts.

**Part 1: Tidying text.** The file sets `raw_name = "   tOM sMITH   "`. Below it, create:
- `clean_name`: `raw_name` with the spaces removed from both ends and each word capitalised (`"Tom Smith"`).
- `shout`: `clean_name` in capitals (`"TOM SMITH"`).
- `name_length`: how many characters are in `clean_name`.
- `greeting`: an f-string that makes `"Hello, Tom Smith!"`. Then print it.

As in Lesson 1, the tests change `raw_name` to check you worked the answers out rather than typing them in.

**Part 2: Tip calculator.** Ask two questions, using exactly these prompts:
```
Bill amount: 
Tip percent: 
```
Then work out the tip and the total (bill plus tip), and print them with two decimal places. Running it should look like this, where you type `40` and `15`:
```
Bill amount: 40
Tip percent: 15
Tip: 6.00
Total: 46.00
```

Run it:
```
python3 lessons/02-strings-and-input/exercise.py
```

Check it:
```
python3 lessons/02-strings-and-input/test_exercise.py
```

The tests answer the questions for you, so they won't stop and wait for your typing.

## Capstone step

Pocket Ledger starts asking for expenses. In `pocket_ledger/main.py`, keep everything from Lessons 0 and 1, then add to the end:

1. Ask `Amount: ` and store the answer as a number in a variable called `amount`.
2. Ask `Description: ` and store the answer in a variable called `description`, with any spaces at the ends stripped off.
3. Print a confirmation with the amount to two decimal places:
   ```
   Added coffee: 4.50
   ```

So a full run looks like:
```
Pocket Ledger
Total spent: 10.68
Amount: 4.5
Description: coffee
Added coffee: 4.50
```

## Commit

When this lesson's tests pass, and Lessons 0 and 1 still pass:

```
git add lessons/02-strings-and-input/exercise.py pocket_ledger/main.py
git commit -m "Lesson 2: strings, input and adding an expense"
git push
```

## Done when

- `python3 lessons/02-strings-and-input/test_exercise.py` prints `All tests passed`.
- Lessons 0 and 1 tests still print `All tests passed`.
- Your commit is on GitHub.

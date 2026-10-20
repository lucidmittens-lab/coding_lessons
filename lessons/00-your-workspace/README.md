# Lesson 0: Your workspace

Before writing any real code you need three things: Python, an editor to write code in, and a terminal to run it from. This lesson sets them up and gets one tiny program running.

## The concept

**Python** is a program that reads a text file of instructions and carries them out. A file ending in `.py` is just text; nothing happens until you hand it to Python.

**An editor** (we will use VS Code) is where you write those text files. It is like a word processor for code: it colours the code so it is easier to read and points out mistakes.

**A terminal** is a window where you type commands instead of clicking. You will use it to run your programs and, later, to use git.

The command that runs a Python file looks like this:

```
python hello.py
```

That means: "Python, please read `hello.py` and do what it says."

## Step 1: Install the tools

1. **Python 3**: download it from [python.org/downloads](https://www.python.org/downloads/). On Windows, tick **"Add python.exe to PATH"** on the first screen of the installer. On a Mac, the python.org installer is fine.
2. **VS Code**: download it from [code.visualstudio.com](https://code.visualstudio.com/). After it opens, click the Extensions icon on the left (four squares), search for **Python**, and install the one by Microsoft.
3. **Git**: on Windows, install it from [git-scm.com](https://git-scm.com/downloads). On a Mac, open Terminal and type `git --version`; if it is missing, the Mac offers to install it.

Check it all worked. Open a terminal (in VS Code: **Terminal → New Terminal**) and type:

```
python --version
git --version
```

Each should print a version number. If `python` says "not found", try `python3 --version`. If that works, use `python3` everywhere these lessons say `python`.

## Step 2: Get this repository onto your computer

In the terminal, go to a folder where you want to keep your code and run:

```
git clone https://github.com/lucidmittens-lab/coding_lessons.git
cd coding_lessons
code .
```

The last line opens the folder in VS Code. (If `code` is not found, open VS Code and use **File → Open Folder** instead.)

## Step 3: The exercise

Open `lessons/00-your-workspace/lesson_00.py`. It is almost empty. Write **one line** in it that prints exactly:

```
Hello, world!
```

Hint: Python's `print` takes the text you want to show, inside brackets and quotes.

Run it from the terminal, from the top folder of the repository:

```
python lessons/00-your-workspace/lesson_00.py
```

Then try running it with the **▶ Run** button in the top right corner of VS Code. Both do the same thing.

## Step 4: Check your work

Run the tests:

```
python lessons/00-your-workspace/test_lesson_00.py
```

If it says `All tests passed`, you are done with the exercise. If not, read what it says it expected, change your code and try again.

## Step 5: Capstone step

The capstone project is **Pocket Ledger**, an expense tracker you will build up over the whole course. Today it starts as one line.

1. Create a new file at `pocket_ledger/main.py`.
2. Make it print `Pocket Ledger`.
3. Run it: `python pocket_ledger/main.py`.

## Step 6: Your first commit

A **commit** is a saved snapshot of your project, with a note saying what changed. Git keeps every snapshot, so you can always look back or undo.

From the top folder of the repository:

```
git status
```

This lists files that changed. You should see `lesson_00.py` and `pocket_ledger/main.py`.

```
git add lessons/00-your-workspace/lesson_00.py pocket_ledger/main.py
git commit -m "Lesson 0: hello world and the start of Pocket Ledger"
git push
```

`add` chooses which changes go in the snapshot, `commit` takes it, and `push` sends it up to GitHub. The first time you push, git may ask you to sign in to GitHub; follow its prompts.

If any of these steps go wrong, paste the whole message you got into the project thread. Errors on day one are normal and are usually a setup detail, not you.

## Done when

- `python lessons/00-your-workspace/test_lesson_00.py` prints `All tests passed`.
- `python pocket_ledger/main.py` prints `Pocket Ledger`.
- Your commit shows up on GitHub.

# Random Password Generator

## Overview

This project is a simple command-line Random Password Generator written in Python. It asks the user for the desired password length and generates a random password using letters and numbers.

## Features

* Allows the user to choose the password length.
* Generates random characters for each password.
* Uses uppercase and lowercase letters.
* Includes numbers from 0–9.
* Checks that the entered length is a valid whole number.
* Prevents password lengths below 1.
* Uses Python's `secrets` module for random character selection.

## How It Works

The program first asks the user to enter the desired password length.

The `generate_password()` function creates a character pool containing uppercase letters, lowercase letters, and digits. It then uses `secrets.choice()` to randomly select characters until the requested length is reached.

The generated password is then displayed on the screen.

## Example

```text
=== Random Password Generator ===
Enter desired password length: 12

Generated Password:
 a8Kp2Lm9QxT4
```

## Technologies Used

* Python
* `string` module
* `secrets` module
* Functions
* Lists
* Loops
* Exception handling
* User input

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run the Python file:

```bash
python filename.py
```

4. Enter the desired password length.
5. The generated password will be displayed.

## Input Validation

The program handles invalid input by checking whether the entered value is a whole number. It also rejects values smaller than 1 and asks the user to enter the length again.

## Project Purpose

The purpose of this task was to practice Python fundamentals while building a useful command-line application. It demonstrates user input, functions, loops, validation, and the use of Python's built-in modules for generating random passwords.


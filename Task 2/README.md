# Expense Tracker

## Overview

This project is a simple command-line Expense Tracker written in Python. It allows the user to enter expense amounts, keeps a running total, and displays a summary when the user is finished.

## Features

* Enter multiple expense amounts.
* Shows the running total after each entry.
* Counts the number of transactions.
* Uses `quit` to stop entering expenses.
* Handles invalid input without stopping the program.
* Displays the total amount spent at the end.

## How It Works

The program starts by asking the user to enter an expense amount. Each valid amount is added to the total and the transaction count is increased.

If the user enters `quit`, the input process stops and the program displays the number of transactions and the total amount spent.

Invalid inputs are handled using `try-except`, so the program continues running instead of crashing.

## Example

```text
=== Expense Tracker ===
Enter an expense amount, or type 'quit' to stop.

Enter expense (or 'quit'): 500
  Added 500. Running total: 500

Enter expense (or 'quit'): 250
  Added 250. Running total: 750

Enter expense (or 'quit'): quit

=== Summary ===
Transactions logged: 2
Total Spent: 750
```

## Technologies Used

* Python
* Command-line interface
* Variables and arithmetic
* `while` loop
* `if` statements
* `try-except` error handling
* User input

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run the Python file:

```bash
python filename.py
```

4. Enter expense amounts when prompted.
5. Type `quit` when you are finished.

## Project Purpose

The purpose of this task was to practice Python fundamentals by creating a small program that accepts user input, processes data, handles invalid input, and produces a final summary.


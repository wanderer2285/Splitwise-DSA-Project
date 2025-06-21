# Splitwise-DSA-Project

A **Data Structures & Algorithms** implementation of the classic **Splitwise** problem — simplifying group expenses by minimizing the number of transactions needed to settle balances.


##  Overview

This project models a system where multiple users share expenses, and the goal is to calculate **who owes whom** and **how much**, in a way that minimizes total transactions.

It uses a **greedy approach** to match the largest creditor and debtor iteratively until all balances are settled.


##  Features

🔹 Debt simplification using DSA logic  
🔹 Accurate rounding using `Decimal`  
🔹 Clean and readable Python code  
🔹 Console output for easy understanding  
🔹 Ideal for learning **Hash Maps**, **Greedy Strategy**, and **Recursion**


##  Example Scenario

Given these balances after expense calculations:

| Person | Balance |
|--------|---------|
| A      | -5.0    |
| B      | 25.0    |
| C      | -20.0   |
| D      | 25.0    |
| E      | -20.0   |
| F      | -5.0    |

The program outputs:
A needs to pay B: 5.0
C needs to pay B: 20.0
E needs to pay D: 20.0
F needs to pay D: 5.0


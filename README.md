# Splitwise DSA Project (Python)

## Welcome to the Shortest Path or CashFlow-Algorithm-Splitwise Readme!  

The idea is to use Shortest path algorithm where at every step, settle all amounts of one person and recur for remaining n-1 persons.  

  
## Getting Started  
  
For example, if the following weighted directed graph represents some people and the arrows represent debts between them (Alice owes Bob $20 and Charlie $5, Bob owes Charlie $10, etc.):

How to pick the first person? To pick the first person, calculate the net amount for every person where net amount is obtained by subtracting all debts (amounts to pay) from all credits (amounts to be paid). Once net amount for every person is evaluated, find two persons with maximum and minimum net amounts. These two persons are the most creditors and debtors. The person with minimum of two is our first person to be settled and removed from list. Let the minimum of two amounts be x. We pay ‘x’ amount from the maximum debtor to maximum creditor and settle one person. If x is equal to the maximum debit, then maximum debtor is settled, else maximum creditor is settled.

![Problem Statement](https://github.com/soumyasethy/ShortestPath-CashFlow-Algorithm-Splitwise/blob/Images/Screen%20Shot%202017-07-24%20at%208.29.26%20PM.png)

There's no sense in $10 making its way from Alice to Bob and then from Bob to Charlie if Alice could just give it to Charlie directly.

The goal, then, in the general case is to take a debt graph and simplify it (i.e. produce a new graph with the same nodes but different edges).

## How to Use?  
from splitwise import find_path

balances = {
    "A": -5.0,
    "B": 25.0,
    "C": -20.0,
    "D": 25.0,
    "E": -20.0,
    "F": -5.0
}

find_path(balances)
      
**Output**  
C needs to pay B:20.0  
E needs to pay D:20.0  
A needs to pay B:5.0  
F needs to pay D:5.0  

##  Algorithm Logic
1. Compute **net balances** for each person  
   (credits - debits)
2. Identify person with:
   - Maximum credit
   - Maximum debt
3. Transfer the minimum of the two values (`x`)
4. Update balances and **recurse**
5. Repeat until all amounts are settled
This ensures **minimal number of transactions** and **optimal simplification** of the original graph.

##  Tech Concepts Used
- Greedy Algorithm
- Hash Maps / Dictionaries
- Recursive Debt Simplification
- Precision Handling using Python's `decimal.Decimal`        

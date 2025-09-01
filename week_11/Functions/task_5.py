"""
Record multipe expenses in a temporary expense dictionary.

parameters:
expenses: Existing dictionary to store expenses.
items: Key-value pairs of expenses (category=amount).

Example:
    expenses = {}
    record_expenses(expenses, food=2500, transport=1500, books=3000)
    print(expenses {'food'}) # should return 2500.
"""

def record_expenses(expenses, **items):
    for category, amount in items.items():
        expenses[category] = amount
    return expenses

expenses = {}
record_expenses(expenses, food=2500, transport=1500, books=300)
print(expenses) 
print(expenses['food'])  

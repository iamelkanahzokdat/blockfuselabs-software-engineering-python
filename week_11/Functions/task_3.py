#Grocery List Manager
"""
    Adds multiple grocery items to the grocery list.

    Parameters:
    grocery_list (list): The existing list of groceries.
    *items: Any number of grocery items (strings).

    Example:
    groceries = []
    items = "Tomato", "Milk", "Bread"
    add_groceries(groceries, "Tomato", "Milk", "Bread")
    print(groceries)  # Output: ['Tomato', 'Milk', 'Bread']
"""

groceries = []
def add_groceries(grocery_list, *items):
    for item in items:   # loop through the items passed
        grocery_list.append(items)
        add_groceries(groceries, "Tomato", "Milk", "Bread")

print(groceries)   # ['Tomato', 'Milk', 'Bread']

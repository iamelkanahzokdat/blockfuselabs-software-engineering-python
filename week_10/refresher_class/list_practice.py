'''
Create a list called fruits with the values: "apple", "banana", "cherry", "orange", "mango".

Print the list and its length.

Remove the last fruit using .pop() and print the list.

Add "kiwi" to the list using .append().

Insert "pineapple" at position 2.

Remove "banana" from the list using .remove().
'''

fruits = ["apple", "banana", "cherry", "orange", "mango"]

# printing the list and its length
print(fruits, len(fruits))

# removing the last item using .pop() and printing the list
fruits.pop()
print(fruits, len(fruits))

# adding "kiwi" to the list using .append() and printing
fruits.append("kiwi")
print(fruits, len(fruits))

# inserting "pineapple" at position 2
fruits[2] = "pineapple"
print(fruits, len(fruits))

# removing "banana" from the list using .remove()
fruits.remove("banana")
print(fruits, len(fruits))


'''
Create a list numbers containing integers 1 to 10.

Print the list and its length.

Remove the first element using .pop(0).

Insert the number 100 at index 5.

Append 200 to the end of the list.

Remove the number 8 from the list.

'''
# creating a list numbers containing integers 1 to 10 and printing its length.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers, len(numbers))

# removing the first element using .pop(0).
numbers.pop(1)
print(numbers, len(numbers))

# Inserting the number 100 at index 5.
numbers[5] = 100
print(numbers, len(numbers))

# Appending 200 to the end of the list.
numbers.append(200)
print(numbers, len(numbers))

# Removing the number 8 from the list.
numbers.remove(8)
print(numbers, len(numbers))

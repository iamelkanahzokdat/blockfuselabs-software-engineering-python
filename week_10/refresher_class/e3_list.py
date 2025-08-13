noise_makers = []
#noise_makers[0] = "Dorcas"
print(noise_makers, len(noise_makers))

noise_makers.append("Dorcas")

print(noise_makers, len(noise_makers))

noise_makers.append("Bethel")

print(noise_makers, len(noise_makers))

colors = ["blue", "black", "white", "red", "yellow", "green"]
print(colors, len(colors))
colors.pop()
print(colors, len(colors))
colors.append("green")
print(colors, len(colors))
colors.insert(1, "Orange")
print(colors, len(colors))
colors.remove("black")
print(colors, len(colors))
colors.insert(10, "violet")
print(colors, len(colors))

fruits = ["orange", "mango", "apple", "pear"]
print(fruits[0])
print(fruits[-1])

fruits[1] = "grapes"
print(fruits, len(fruits))
#fruits[0] = "pear"
#fruits[-1] = "orange"
#print(fruits, len(fruits))
fruits[0], fruits[-1] = fruits[-1], fruits[0]
print(fruits, len(fruits))
#fruits[0], fruits[-1] = "pear", "orange"
#print(fruits, len(fruits))

#deleting an item by reassigning the index in the variable
print(fruits[0:3])
fruits = fruits[0:3]
print(fruits)

aaron = ["aaron", True, 12, 1.8, ["eating", "sleeping"]]
print(aaron[-1])
print(aaron[4])

print(aaron[-1][-1])

a = [1,2,3,[4,5,[6,7,[8],9]]]
print(a[3][2][2][0])
print(a[3][2][3])
print(a[3])

#b = a[3][2][2][0]
#print(b, b == 8)

y = [1, 2, ["yusuf", False, "9"]]

#print(y[2], type(y[2]))
print(y[2][2], type(y[2][2]))
print(y)
y[2][2] = int(y[2][2]) 
print(y[2][2], type(y[2][2]))

y[2][2] = str(y[2][2]) + "5"
print(y[2][2], type(y[2][2]))
#yusuf[2] += 5 
#print(yusuf[2])



list1 = [42, "hello", 3.14, True, None, [1, 2, 3], {"a": 1, "b": 2}]
print(list1[0:3])
print(list1[3:])
print(list1[:5])
print(list1[2:6])
print(list1[-3:])


list2 = ["apple", 10, False, [4, 5, 6], {"x": "y"}, 7.89, None]
print(list2[1:4])
print(list2[:2])
print(list2[3:])
print(list2[-4:-1])
print(list2[-2:])


list3 = [100, "banana", {"fruit": "mango"}, [9, 8, 7], True, 5.5, None, "end"]
print(list3[:4])
print(list3[4:])
print(list3[2:6])
print(list3[-5:])
print(list3[-7:-3])


list4 = [["nested", "list"], 25, None, {"key": "value"}, False, "string", 0.001]
print(list4[1:5])
print(list4[:3])
print(list4[3:])
print(list4[-4:])
print(list4[-6:-2])


list5 = [True, {"a": [1, 2]}, 50, "middle", 99.99, [10, 20, 30], None, "last"]
print(list5[:5])
print(list5[5:])
print(list5[2:7])
print(list5[-3:])
print(list5[-6:-1])


'''
Given this list:
fruits = ["apple", "banana", "mango", "orange"]

 
Add "grape" to the end of the list.
Insert "cherry" at index 2.
Remove "banana" from the list.
Replace "orange" with "watermelon".
Extend the list with ["pear", "kiwi"].
'''

fruits = ["apple", "banana", "mango", "orange"]

fruits.append("grape")
print(fruits)

fruits[2] = "cherry"
print(fruits)

fruits.remove("banana")
print(fruits)

fruits[2] = "watermelon"
print(fruits)

fruits.append(["pear", "kiwi"])
print(fruits)











'''
Given this list:
data = [10, 20, 30, 40, 50]

Append 60 to the list.
Insert 15 at index 1.
Remove the first element from the list.
Change the value at index 3 to 45.
Add [70, 80] as separate elements to the list.
'''

data = [10, 20, 30, 40, 50]
data.append(60)
print(data)

data[1] = 15
print(data)

data.remove(10)
print(data)

data[3] = 45
print(data)

data.append([70, 80]) 
print(data)

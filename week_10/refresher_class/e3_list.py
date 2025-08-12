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

scores = ()
print(scores, type(scores))

a = (1)
print(a, type(a))

b = (1,)
print(b, type(b))

c = 1,
print(c, type(c))

noise_makers1 = "Dorcas", "Bethel", "yusuf"
print(noise_makers1, type(noise_makers1))

noise_makers2 = ("Dorcas", "Bethel", "yusuf")
print(noise_makers2, type(noise_makers2))

# noise_makers2[0] = "Tk"
# you can not change values in a tuple, you need to typecast it back to a list.

print(noise_makers2)

noise_makers2 = list(noise_makers2)
print(noise_makers2, type(noise_makers2))

noise_makers2[0] = "Tk"
print(noise_makers2)
 
# unpacking into new variables a, b, and c
a, b, c = noise_makers2
print(a)
print(b)
print(c)

# create a variable kingpin, others
# kingpin, others = noise_makers2
# print(kingpin, others)
# it outputs an Error called Value Error, cause we parsed only two variables to unpack three items

kingpin, *others = noise_makers2
print(kingpin)
print(others)

# print the data types 
print(type(kingpin))
print(type(others))


tuple1 = (42, "hello", 3.14, True, None, [1, 2, 3], {"a": 1, "b": 2})
print(tuple1[0:3])
print(tuple1[3:])
print(tuple1[:5])
print(tuple1[2:6])
print(tuple1[-3:])


tuple2 = ("apple", 10, False, [4, 5, 6], {"x": "y"}, 7.89, None)
print(tuple2[1:4])
print(tuple2[:2])
print(tuple2[3:])
print(tuple2[-4:-1])
print(tuple2[-2:])


tuple3 = (100, "banana", {"fruit": "mango"}, [9, 8, 7], True, 5.5, None, "end")
print(tuple3[:4])
print(tuple3[4:])
print(tuple3[2:6])
print(tuple3[-5:])
print(tuple3[-7:-3])


tuple4 = (["nested", "list"], 25, None, {"key": "value"}, False, "string", 0.001)
print(tuple4[1:5])
print(tuple4[:3])
print(tuple4[3:])
print(tuple4[-4:])
print(tuple4[-6:-2])


tuple5 = (True, {"a": [1, 2]}, 50, "middle", 99.99, [10, 20, 30], None, "last")
print(tuple5[:5])
print(tuple5[5:])
print(tuple5[2:7])
print(tuple5[-3:])
print(tuple5[-6:-1])




'''
Given this tuple:
colors = ("red", "blue", "green", "yellow")

Convert the tuple to a list.
Add "purple" to the end.
Replace "blue" with "black".
Convert it back to a tuple.
'''
colors = ("red", "blue", "green", "yellow")
print(type(colors))

# typecasting to class list
colors = list(colors)
print(colors, type(colors))

colors.append("purple")
print(colors)

colors[1] = "black"
print(colors)

# typecasting back to class tuple
colors = tuple(colors)
print(colors, type(colors))






'''
Given this tuple:
numbers = (1, 2, 3, 4, 5)

Concatenate it with another tuple (6, 7, 8).
Slice the first four elements from the new tuple.
Convert the tuple to a list and remove the value 3.
Convert it back to a tuple.
'''

numbers = (1, 2, 3, 4, 5)
numbers_2 = (6, 7, 8)
result = numbers + numbers_2
print(result)

print(result[0:4])

result = list(result)
result.remove(3)
print(result, type(result))

result = tuple(result)
print(result, type(result))


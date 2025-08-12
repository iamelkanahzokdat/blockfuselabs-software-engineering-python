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

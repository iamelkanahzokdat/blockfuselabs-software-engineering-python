'''
num = 1
print(num)
print (id(num))

'''

'''
first_name = input("Enter your first name: \n")
second_name = input("Enter your second name: \n")
user_age = int(input(f"Enter your age: \n"))
are_you_married = input("is_married (yes/no): \n")
user_height = float(input(f"Height(cm): \n"))

print(''------ BIO DATA ------'')

print(f"first name: {first_name}")
print(f"second name: {second_name}")
print(f"Age: {user_age}")
print(f"is_married?: {are_you_married}")
print(f"Your height is: {user_height}cm") 
'''


first_name = "Dre"
second_name = "Nvm"
age = 22
is_married = False
height = 5.6

print(first_name)
print(second_name)
print(age)
print(is_married)
print(height)

print(type(1))
print(type(1.))
print(type(False))
print(type(True))
print(type("m"))

a = 1
b = 2
c = 4
print(id(c))
c = a
print(id(c))

print(a)
print(c)
print(id(c))

m = "m"
n = "n"
d = "m"
print(id(m))
print(id(n))
print(id(d))

num = 1
num -= 10
print(num)

num = True
num = num + 2
print(num)

num = "1"
num = num + str(2)
print(num)
print(type(num))

num = 1
num = bool(1)
print(num)

d = (1/2)
e = (1//2)
print(d, type(d))
print(e, type(e))

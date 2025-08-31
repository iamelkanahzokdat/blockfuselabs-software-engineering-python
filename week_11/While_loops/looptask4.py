# Create a list a = [1,2,3] and assign b to a
#modify b by appending a new number
#print both a and b to show why list share same memory refrences
#Then use copy() or slicing a([:])

a = [1,2,3]

b = a

b.append(4)

print(id(a))
print(id(b))

c = a.copy()

print(id(a))
print(id(b))
print(id(c))

print(a==b==c)

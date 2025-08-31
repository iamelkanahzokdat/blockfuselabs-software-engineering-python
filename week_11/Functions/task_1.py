'''
def incrementBy1 ():
   num += 1
   print(num)



incrementBy1()
'''

def greet(name):
   print(f"Good afternoon {name}")

greet("Elkanah")



def sum(a, b):
   c = a + b
   print('inside the fn:', c)
   return c

result = sum(1,2)
another = sum(4,5)
lets_go_home = sum(9,1)

print("print is outside fn:", result)
print("print is outside fn:", another)
print("print is outside fn:", lets_go_home)

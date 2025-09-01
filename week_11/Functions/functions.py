'''
def adder(a, b, c):
    print(f"a - {a} \n b = {c}")
    # return a + b
adder(1,2,3)
print("=========================")
# adder (c=1, c=2, c=3)
'''
def adder(a = 0, b = 0):
    print(a,b)
    return a + b 

print(adder(1,2))

num = 0

def incrementBy1():
    global num
    num += 1

incrementBy1()
incrementBy1()
incrementBy1()
incrementBy1()
incrementBy1()
incrementBy1()
print(num)

def incrementByNumber(number):
    global num
    num += number


incrementByNumber(5)
print(num)
incrementByNumber(1)
print(num)
incrementByNumber(4)
print(num)





def gradingsystem(score):
    if score >= 70 and score <= 100:
        print("A")
    elif score >= 60 and score < 70:
        print("B")
    elif score >= 50 and score < 60:
        print("C")
    elif score >= 40 and score < 50:
        print("D")
    elif score >= 30 and score < 40:
        print("D")
    elif score >= 20 and score < 30:
        print("D")
    else:
        print("Invalid score")

gradingsystem(48)
gradingsystem(78)
gradingsystem(67)
gradingsystem(34)
gradingsystem(100)
gradingsystem(123)


def countdown(n):
     if n == 0:
          print("Blastoff!: 🚀")
          return
     print(n)

     countdown(n-1)

countdown(10)


def mytodos(*a):
    print(a)
    for item in a:
        print(item)

mytodos("Buy groceries", "Clean the house", "Pay bills", "Walk the dog")
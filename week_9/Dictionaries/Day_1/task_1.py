score = float(input("Enter score: "))

if 70 <= score <= 100:
    print("A")
elif 50 <= score < 70:
    print("B")
elif 40 <= score < 50:
    print ("C")
elif 30 <= score < 40:
    print ("D")
elif 0 <= score < 30:
    print ("F")
else:
    print("Invalid Score")



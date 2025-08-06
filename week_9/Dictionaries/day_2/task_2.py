''' SMARTPHONE PURCHASE:

ask user to input budget

1. check if the budget is atleast $500, if it is, check if the budget is $1000 or more, then recommend "Google Pixel 9pro", otherwise, recommend "Iphone"

2. if budget is below $500, if it is, and atleast $288. then recommend "Redmi" otherwise, recommend "save more".
'''

budget = float(input("Enter your budget to purchase your phone. \n $"))

if budget >= 500:
    if budget >= 1000:
       print("Google Pixel or 9Pro")
    else:
       print("Iphone")
else:
    if budget >= 200:
       print("Redmi") 
    else:
       print("save more")

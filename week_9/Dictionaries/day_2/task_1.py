''' MOVIE TICKET DISCOUNT:
You are building a movie ticketing system.
instruction : ask user for their age:
1. persons 18 or older can buy a ticket".

output: "can buy a ticket"

2. if the are 60 or older they get "senior discount".

output: "senior discount"

3. if they are under 18 and 12 yrs or older, the can buyteen ticket.

output: Teen ticket

otherwise, they can buy "kids ticket"
'''
age = int(input("Enter your age: "))

if age >= 18:
   print("can buy ticket")
   if age >= 60:
      print("Senior Discount")

elif age >= 12 and age < 18:
   print("Teen Ticket")
     
else:
   print('you can buy kids ticket')




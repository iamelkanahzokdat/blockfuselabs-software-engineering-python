code = 7732

attempts = 3

shouldExecute = True

while shouldExecute:
   pin = int(input("Enter your 4 digit pin: "))

   attempts -= 1
   
   if attempts > 0:
      if pin == code:
         print("Access Granted")
         shouldExecute = False
      else: 
         print("Access Denied")
     
   else:
      print("Card Blocked", attempts)
      shouldExecute = False

 


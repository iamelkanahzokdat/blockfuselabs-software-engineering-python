user_db = ["core", "tk", "mp"]

username = input("Enter your name: \n")

if username in user_db:
   print("username exists")

   password = int(input("Enter your Password: "))
   confirm_password = int(input("Confirm Password: "))

   if password == confirm_password:     
      print("Password matched sucessfully")

   else:
      print("Password mismatch")

else:
   print("username does not exists")



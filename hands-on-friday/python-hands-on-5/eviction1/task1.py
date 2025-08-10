"""
Password Match Check
1. Create a variable 'password'
2. prompt the user to input a password
3. Create another variable 'confirm_password'
4. prompt the user to re-enter password
5. compare both passwords, if the match, print "password matched"
6. othwerwise: print "password mismatch"

"""
print("Password Match Check")

password = input("Enter password :")
confirm_password = input("Re-enter password :")

if password == confirm_password:
   print("password matched")

else:
   print("password mismatched")


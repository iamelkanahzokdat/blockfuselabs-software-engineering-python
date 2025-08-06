''' student = {
     "name": "legolas",
     "has_registered: True,
     "has_paid": True,
     "has_internet": False
}

only students that have registered are eligible for exams. any student that has not registered should be denied accesswith message "Access Denied".
1. in as much as students have registered, if the haven't paid fees, the should be denied access to with message "pay your fees".

2. if the have paid and have internet access, message "Allow access", else "check your internet connection"
'''

student = {
    "name": "legolas",
    "has_registered": True,      
    "has_paid": True,
    "has_internet": False
}

if student["has_registered"] == True:
    if student["has_paid"] == True:
       if student["has_internet"] == True:
          print("Allow Access")
       else:
          print("Check Internet Connection.")
else:
   print("Access Denied")



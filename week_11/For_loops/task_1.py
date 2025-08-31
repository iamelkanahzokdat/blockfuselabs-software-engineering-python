'''
students_scores = {
    "Aisha": 95,
    "David": 82,
    "Mary": 99,
    "John": 78,
    "Sarah": 65,
    "Paul": 88,
    "Grace": 100,
    "James": 73,
    "Ruth": 84,
    "Daniel": 90,
    "Michael": 67,
    "Esther": 59,
    "Tunde": 48,
    "Ngozi": 34,
    "Chinedu": 27,
    "Hauwa": 72,
    "Ibrahim": 41,
    "Femi": 53,
    "Victoria": 68,
    "Samuel": 38
}


GRADES
A : 70 - 100
B : 60 - 69
C : 50 - 59
D : 40 - 49
E : 30 - 39
F : 0 - 29 
'''

#Loop through the dictionary and group each student into a grade bucket 

students_scores = {
    "Aisha": 95,
    "David": 82,
    "Mary": 99,
    "John": 78,
    "Sarah": 65,
    "Paul": 88,
    "Grace": 100,
    "James": 73,
    "Ruth": 84,
    "Daniel": 90,
    "Michael": 67,
    "Esther": 59,
    "Tunde": 48,
    "Ngozi": 34,
    "Chinedu": 27,
    "Hauwa": 72,
    "Ibrahim": 41,
    "Femi": 53,
    "Victoria": 68,
    "Samuel": 38
}




grade = {
   "A": [],
   "B": [],
   "C": [],
   "D": [],
   "E": [],
   "F": []
}



for name, score in students_scores.items():

    if 70 <= score <= 100:
       grade["A"].append(name)
   
    elif 60 <= score <= 69:
       grade["B"].append(name)

    elif 50 <= score <= 59:
       grade["C"].append(name)

    elif 40 <= score <= 49:
       grade["D"].append(name)

    elif 30 <= score <= 39:
       grade["E"].append(name)

    else:
      grade["F"].append(name)

for grade, students in grade.items():
   print(f"{grade}: {students}")




A_students = {}
B_students = {}
C_students = {}
D_students = {}
E_students = {}
F_students = {}
for student in students_scores:
   if students_scores[student] >= 70 and students_scores[student] <= 100:
       A_students[student] = students_scores[student]
   elif students_scores[student] >= 60 and students_scores[student] <= 69:
       B_students[student] = students_scores[student]
   elif students_scores[student] >= 50 and students_scores[student] <= 59:
       C_students[student] = students_scores[student]
   elif students_scores[student] >= 40 and students_scores[student] <= 49:
       D_students[student] = students_scores[student]
   elif students_scores[student] >= 30 and students_scores[student] <= 39:
       E_students[student] = students_scores[student]
   else:
       F_students[student] = students_scores[student]
print(f'''A rank students are {A_students}
         B rank students are {B_students}
         C rank students are {C_students}
         D rank students are {E_students}
         E rank students are {D_students}
         F rank students are {F_students}

''')

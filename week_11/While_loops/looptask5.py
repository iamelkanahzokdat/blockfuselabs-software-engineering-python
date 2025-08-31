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

#Loop through the dictionary and group each student into a grade bucket:

GRADES
A : 70 - 100
B : 60 - 69
C : 50 - 59
D : 40 - 49
E : 30 - 39
F : 0 - 29 


shouldExecute = True
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

grade_bucket = {
   "A": [],
   "B": [],
   "C": [],
   "D": [],
   "E": [],
   "F": []
}



while shouldExecute:
 for students_scores in students_scores.items():

    if students_scores.values() >= 70 and <= 100:
       grade_bucket["A"].append(students_scores)
   
    elif students_scores.values() >= 60 and <= 69:
       grade_bucket["B"].append(students_scores)

    elif students_scores.values() >= 50 and <= 59:
       grade_bucket["C"].append(students_scores)

    elif students_scores.values() >= 40 and <= 49:
       grade_bucket["D"].append(students_scores)

    elif students_scores.values() >= 30 and <= 39:
       grade_bucket["E"].append(students_scores)

    else:
      students_scores.values() == 0 and <= 69:
       grade_bucket["F"].append(students_scores)

      shouldExecute = False







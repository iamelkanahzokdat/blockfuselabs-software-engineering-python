scores = {"Alice": [80, 90],
          "Bob": [70, 85], 
          "Charlie": [95]
         }

shouldExecute = True
'''
#Version1
while shouldExecute:
     student_name = input("Enter student name: \n")
     if student_name in scores.keys():
        scores[student_name].append(student_score)
     student_score = int(input("Enter student score: \n"))

     else:
        scores.update({student_name:student_score})

     if student_name == 'exit':
        print(scores)
        shouldExecute = False
'''

#Version2
while shouldExecute:
       student_name = input("Enter student name: \n")
       if student_name == 'exit':
          print(scores)
          shouldExecute = False

       elif student_name in scores.keys():
          student_score = int(input("Enter student score: \n"))
          scores[student_name].append(student_score)
       
       else:
          scores.update({student_name:[student_score]})
       print(scores)

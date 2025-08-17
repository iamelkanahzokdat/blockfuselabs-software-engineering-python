student = {'name': "john", 'age': "20", 'courses': ["biology", "math", "comp sci"]}
print(student)
#student['phone'] = "555-555"
#print(student.get('phone', 'Not found'))

print(student['name'])
print(student['age'])
print(student['courses'])
student.update({'name': "Jane", 'age': "22", 'courses': ["english", "government", "literature"]})
print(student)
print(id(student))
print(len(student))

#print(student.key())
#print(student.value())
#print(student.items())

for key, value in student.items():
   print(key, value)

name, age = student['name'], student['age']
print(name)
print(age)


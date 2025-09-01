# student Profile
"""
create a student profile with dynamic attributes.

parameters:
details: Any arguments representing student details.
(e.g., name, age, grade, hobbies.)

Example:
   Profile = create_student_profile(name="Ada", age=20, grade="A", hobbies=["reading", "coding"])
   profile.name should return "Ada"
"""


def create_student_profile(**details):
    return details

profile = create_student_profile(name="Ada", age=20, grade="A", hobbies=["reading", "coding"])
print(profile)
print(profile['name'])  # Output: Ada
print(profile['age'])   # Output: 20
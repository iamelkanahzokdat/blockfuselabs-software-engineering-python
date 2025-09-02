"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.


import datetime

attendance = {}

def register_student(student_id, name):
    Register a student in the system.
    pass

def mark_present(student_ids):
    Mark multiple students as present for today.
    today = str(datetime.date.today())
    # implement logic
    pass

def mark_absent(student_ids):
    Mark multiple students as absent for today.
    today = str(datetime.date.today())
    implement logic
    pass

def get_report(**kwargs):
    Generate attendance report with optional filters.
    report = {}
    implement logic

    return report
"""


# ANSWERS

import datetime

attendance = {}

def register_student(student_id, name):
    """Register a student in the system."""
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days": []
        }

def mark_present(student_ids):
    """Mark multiple students as present for today."""
    today = str(datetime.date.today())
    for student_id in student_ids:
        if student_id in attendance:
            if today not in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].append(today)
            # remove from absent if it's previously marked
            if today in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].remove(today)

def mark_absent(student_ids):
    """Mark multiple students as absent for today."""
    today = str(datetime.date.today())
    for student_id in student_ids:
        if student_id in attendance:
            if today not in attendance[student_id]["absent_days"]:
                attendance[student_id]["absent_days"].append(today)
            # remove from present if it's previously marked
            if today in attendance[student_id]["present_days"]:
                attendance[student_id]["present_days"].remove(today)

def get_report(**kwargs):
    """Generate attendance report with optional filters."""
    report = {}
    only_present = kwargs.get("only_present", False)
    only_absent = kwargs.get("only_absent", False)

    for student_id, data in attendance.items():
        if only_present and not data["present_days"]:
            continue
        if only_absent and not data["absent_days"]:
            continue
        report[student_id] = data

    return report

register_student(1, "Elkanah")
register_student(2, "Mp")
register_student(3, "Mark")

# Mark attendance
mark_present([1, 2])      
mark_absent([3])          

# Show reports
print("\n--- Full Report ---")
print(get_report())

print("\n--- Only Present ---")
print(get_report(only_present=True))

print("\n--- Only Absent ---")
print(get_report(only_absent=True))
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}


def grade(score):
    if score >= 91 and score <= 100:
        return "Outstanding"
    elif score >= 81 and score <= 90:
        return "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        return "Acceptable"
    elif score <= 70:
        return "Fail"


for student in student_scores:
    current_grade = grade(student_scores[student])
    student_grades[student] = current_grade

print(student_grades)

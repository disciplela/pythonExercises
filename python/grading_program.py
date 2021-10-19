student_scores = {
    'Harry' : 81,
    'Melvin': 32,
    'Tiffany': 99,
    'Kevin': 91,
    'Steve': 79,
}
student_grades = {}
for student in student_scores:
    if student_scores[student] > 91:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] >= 81 and student_scores[student] <= 91:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] >= 71 and student_scores[student] <= 81:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)
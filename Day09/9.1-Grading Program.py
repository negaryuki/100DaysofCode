student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# 🚨 Don't change the code above 👆

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

for student_key in student_scores:
    score = student_scores[student_key]
    if score <= 70:
        student_grades[student_key] = "Fail"
    elif 71 <= score <= 80:
        student_grades[student_key] = "Acceptable"
    elif 81 <= score <= 90:
        student_grades[student_key] = "Exceeds Expectations"
    elif 91 <= score <= 100:
        student_grades[student_key] = "Outstanding"

# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)

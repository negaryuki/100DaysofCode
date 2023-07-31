# write a code that give you the highest score among others

# Don't write here:

student_scores = input("input a list of student scores").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# write below:
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f' The highest score is {highest_score}')

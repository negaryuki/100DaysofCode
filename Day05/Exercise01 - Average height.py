# write a program that calculates the average student height from a list of heights. Round it up

# Don't write here:
student_heights = input("input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# write below:

total_height = 0

for height in student_heights:
    total_height += height

print(f'The sum of heights is {total_height}')
number_data = 0

for number in student_heights:
    number_data += 1
print(f'Number of inserted heights is {number_data}')

average_height = round(total_height / number_data)

print(f'Your average height is {average_height}')



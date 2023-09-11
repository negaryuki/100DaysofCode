# List comprehension: allows codes to be shorter

# new_list ={new_item for item in list}

#-------------------------------------------

numbers = [1,2,3]

# Instead of this:
# new_list = []
# for n in numbers
#  add_1 = n +1
# new_list.append(add_1)
 
new_list =[n+1 for n in numbers]

print(new_list)

#-------------------------------------------

name ="Angela"

new_letter_list =[l for l in name]

print(new_letter_list)

#-------------------------------------------

num = list(range(1,5))
assingmnent1 = [n *2 for n in num]

print(assingmnent1)

# Or:
  
assignment2 =[n *2 for n in range(1,5)]

print(assignment2)

#-------------------------------------------

# Conditional List Comprehension:
# Only performs the code, IF the test passes:
  
# new-list =[new_item for item in list if test]

#-------------------------------------------

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]

# Only return short names like Alex:
  
short_names= [n for n in names if len(n) < 5]

print(short_names)

upper_case_names = [n.upper() for n in names if len(n) > 5]

print(upper_case_names)
#-------------------------------------------
# Dictionary Comprehension:

# new_dict = {new_key:new_value for item in list/range/string}

# new_dict = {new_key:new_value for for (keey,value) in dict.items()}

# new_dict = {new_key:new_value for for (key,value) in dict.items() if test}

#-------------------------------------------
import random

names2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]

student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)

#-------------------------------------------

passed_students= {student:score for (student, score) in student_scores.items() if score > 60}

print(passed_students)

#-------------------------------------------

# Looping through a DataFrame:
  
# Loop through rows of a DataFrame:
# for (index,row) in DataFrame.iterrows():
#    print(row.score) or print(index)

import pandas

student_dict = {
  "student" :["Angela", "James", "Lily"],
  "score" :[ 56, 76, 98]
}

student_data_frame= pandas.DataFrame(student_dict)

for (index,row) in student_data_frame.iterrows():
  print(row.student)
  print(row.score)
  
  if row.student == "James":
    print(row.score)



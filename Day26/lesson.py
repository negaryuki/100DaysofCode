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

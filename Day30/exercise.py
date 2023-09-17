# Exercise01 - we have got a Buggy code, try running the code and it will crash and give an IndexError. 
#use exception handeling and prevent the program from crahsing so that it only prints out a default output like "Fruit Pie"

fruits =["Apple", 'Pear', "Orange"]

def make_pie(index):
  try:
     fruit= fruits[index]
  except IndexError:
    print ("Fruit Pie")
  else:
    print(fruit + " pie")
  
make_pie(4)

#-------------------------------------------------------------------------------
#Exercise02 - we have got a Buggy code, try running the code and it will crash and give an KeyError. 
#use exception handeling and prevent the program from crahsing the reason of the crash is because some post don't have likes at all. Posts without likes can be accounted as 0

fb_posts = [
  {'Likes': 21,'Comments' :2},
  {'Likes': 13,'Comments' :2, "Shares" : 1},
  {'Comments': 33,'Shares' :2},
  {'Comments': 21,'Shares' :1},
  {'Likes': 19,'Comments' :3}
  ]
  
total_likes = 0
  
for posts in fb_posts:
  try:
    total_likes += posts["Likes"]
    
  except KeyError:
    # total_error += 0
    pass
  
print(total_likes)


#-------------------------------------------------------------------------------

# Exercise03 - Error Handeling the NATO Phonetic Program, in case numbers re entered instead of letters

import pandas


# extract data from csv file:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}


def Generate_phonetic():
  word = input("enter a word:\n").upper()
  
# Include en exceptional error so that it won't crash even if we input numbers instea of letters
    
  try:
    output_list  = [phonetic_dict[letter] for letter in word] 
  
  except KeyError:
    print("Sorry! Only use letters")
    Generate_phonetic()
  
  else:
    print(output_list)
    
  
Generate_phonetic()
    

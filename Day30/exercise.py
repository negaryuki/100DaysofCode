# Exercise01 - we have got a Buggy code, try running the code and it will crash and give an IndexError. use exception handeling and prevent the program from crahsing so that it only prints out a default output like "Fruit Pie"

fruits =["Apple", 'Pear', "Orange"]

def make_pie(index):
  fruit= fruits[index]
  print(fruit + "pie")
  
make_pie(4)

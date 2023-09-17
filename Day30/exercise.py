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
  total_likes += posts["Likes"]
    
    

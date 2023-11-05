from bs4 import BeautifulSoup
#import lxml

with open("website.html") as file:
  contents = file.read()
  
  
soup =BeautifulSoup(contents, "html.parser")

# soup.title          ---->   <title> your title </title.
# soup.title.name     ---->   title
# soup.title.string   ---->   your title

# soup.prettify().    ---->   the whole html file  

all_anchor_tags= soup.find_all(name="a")

#-----------------------------------------------------
# in order to get the text of all desired tags:
  
for tag in all_anchor_tags:
  text = tag.getText()
  
print(text)

#-----------------------------------------------------
# in order to get the link of all anchor tags:
  
for tag in all_anchor_tags:
  links = tag.get("href")
  
print(links)

#-----------------------------------------------------
# in order to get specific tags with IDs:

heading = soup.find(name="h1", id="name")
print(heading)

#-----------------------------------------------------
# in order to get specific tags with classes:

section_heading = soup.find(name="h3", class_= "heading")
print(section_heading.get("class"))

#-----------------------------------------------------
# select_one will give the first result, while select gives all results

company_url = soup.select_one(selector="p a")

# to select an Id:
name = soup.select_one(selector="#name")

# to select a class:
head = soup.select(selector=".heading")


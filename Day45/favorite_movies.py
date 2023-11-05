import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles = [movies.getText() for movies in all_movies]

#reverse list:
reversed_list = movie_titles[::-1]

 
print(movie_titles)

print(all_movies)


with open("movies.text", "w") as file:
  for movie in reversed_list:
    file.write(f"{movie}\n")

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the Billboard Hot 100 chart for a specific date
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

# Send an HTTP GET request to the specified URL and store the HTML content
response = requests.get(URL)
website_html = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Prompt the user to input a date in the format YYYY-MM-DD
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Use CSS selectors to select all <h3> elements within a specific hierarchy
# of <li> and <ul> elements, typically containing song names
song_names_info = soup.select("li ul li h3")

# Extract the text content of the selected <h3> elements, stripping any leading or trailing whitespace
song_names = [song.getText().strip() for song in song_names_info]

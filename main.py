from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html_website = response.text

soup = bs(html_website, "html.parser")

movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_titles = [movie.getText() for movie in movies]

cinemas = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for cinema in cinemas:
        file.write(f"{cinema}\n")

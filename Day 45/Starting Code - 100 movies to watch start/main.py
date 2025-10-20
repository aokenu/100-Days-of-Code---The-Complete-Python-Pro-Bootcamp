import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇


# get a http response from the url
response = requests.get(URL)
data = response.raise_for_status
response_code = response.status_code

data = response.text




# Creating an instance of Beautiful Soup
soup = BeautifulSoup(data, 'html.parser')


top_movies = []

# extracting the movie titles using BeautifulSoup
article_gallary = soup.find_all(name='h3', class_='title')

# using list comprehension to loop through the movies list
movie_titles = [top_movies.append(title.text) for title in article_gallary]
print(top_movies)

# saving the movie list to file
with open('./movies.txt', 'w', encoding='utf-8') as file:
    movie_file = file.writelines(movie + "\n" for movie in reversed(top_movies))
    print(movie_file)

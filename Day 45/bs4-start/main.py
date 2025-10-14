from bs4 import BeautifulSoup
# import lxml



with open("Day 45/bs4-start/website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")

title = soup.title
# print(title)

# print(soup.prettify())

print(soup.a)
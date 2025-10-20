from bs4 import BeautifulSoup
import requests
# import lxml



# with open("Day 45/bs4-start/website.html") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")

# title = soup.title
# # print(title)

# # print(soup.prettify())

# # print(soup.a)

# # To find all the tags where the tag name is "a"
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# # To get all the text within the anchor tags
# for tag in all_anchor_tags:
#     print(tag.getText())

# # To get the URLs of the href
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# # Finding h1 elements with id = "name"
# heading = soup.find_all(name="h1", id="name")
# print(heading)


# # Finding h3 elements with class = "class"
# section_heading = soup.find_all(name="h3", class_="heading")
# print(section_heading)


# # To locate the value of "a" tag inside a "p" tag
# company_url = soup.select_one(selector="p a")
# print(company_url.text)


# # To get the value of an id selector
# name = soup.select_one(selector="#name")
# print(name)


# # To locate an element by class
# headings = soup.select(".heading")
# print(headings)


# the url of the website to scrap from
url = "https://news.ycombinator.com/"
response = requests.get(url) # calling the website url
data = response.text

soup = BeautifulSoup(data, 'html.parser') # creating a soup object

article_tag = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in article_tag:
    a_tag = article.find("a")
    text = a_tag.getText()
    link = a_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

upvotes_tags = soup.find_all(name="span", class_="score") 
article_upvotes = [int(upvote.getText().split()[0]) for upvote in upvotes_tags]



# print(article_texts)
# print(article_links)
# print(article_upvotes)


# print(article_texts, article_links, article_upvotes)

largest_number = max(article_upvotes)
print(largest_number)
largest_index = article_upvotes.index(largest_number)

print(article_links[largest_index])
print(article_texts[largest_index])

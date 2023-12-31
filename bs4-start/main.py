from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    title = article_tag.getText()
    article_texts.append(title)
    link = article_tag.a.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

largest_index = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_index])
print(article_links[largest_index])


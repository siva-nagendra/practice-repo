'''
Scraping club excercise 1:
Extract given product detail such as title, desc and price.
WebScraping using requests, BeautifulSoup and lxml.
'''

import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/detail_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
cardBody = soup.find_all("div", class_ = "card-body")
cardText = soup.find("p", class_ = "card-text")
for i in range(len(cardBody)):
    titles = cardBody[i].find_all("h3", class_ = "card-title")
    prices = cardBody[i].find_all("h4")
    description = cardText.text
    for each in range(len(titles)):
        title = titles[each].text
        price = prices[each].text
        print ("Name of the Product :", title, "\nPrice :", price)
        print ("Description :", description)
'''
Scraping club excercise 2:
Extract details such as title and price for single web page of products.
WebScraping using requests, BeautifulSoup and lxml.
'''

import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
cardBody = soup.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")
count = 1
for i in range(len(cardBody)):
    title = cardBody[i].find("h4", class_ = "card-title").text.strip("\n")
    price = cardBody[i].find("h5").text
    print (str(count) + ")", "Item Name:", title, "\nPrice:", price + "\n")
    count += 1
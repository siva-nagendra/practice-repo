'''
Scraping club excercise 2:
Extract details such as title and price for multiple web pages of products.
WebScraping using requests, BeautifulSoup and lxml.
'''

import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

pages = soup.find_all("ul", class_ = "pagination")
urls = []
links = pages[0].find_all("a", class_ = "page-link")
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum == None:
        urls.append(url)
    else:
        x = link.get("href")
        urls.append(x)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "lxml")
    cardBody = soup.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")
    for i in range(len(cardBody)):
        title = cardBody[i].find("h4", class_ = "card-title").text.strip("\n")
        price = cardBody[i].find("h5").text
        print (str(count) + ")", "Item Name:", title, "\nPrice:", price + "\n")
        count += 1

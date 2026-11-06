import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import random
import os
from dotenv import load_dotenv
import csv



load_dotenv()

MY_USER_AGENT = os.getenv('MY_USER_AGENT')



url = "https://www.goodreads.com/quotes"

session = requests.session()

headers = {"User-Agent" : MY_USER_AGENT,
           "Accept-Language": "en-US,en;q=0.9,pt;q=0.8"}

session.headers.update(headers)


quotesArray = []


while True:

    time.sleep(random.uniform(1.5, 3.0))
    
    response = session.get(url)
    
    data = BeautifulSoup(response.text, "html.parser")

    quotesDivs = data.find_all("div", class_="quoteText")
    


    for quote in quotesDivs:
        fullText = quote.text.strip()
        quoteText = fullText.split("―")[0].strip()
        authorName = quote.span.text.strip().rstrip("., ").strip()
        
        if quote.find("a", class_="authorOrTitle"):
            bookName = quote.find("a", class_="authorOrTitle").text.strip()
        else:
            bookName = "None"
        
        
        quotesArray.append({
            "author" : authorName,
            "quote" : quoteText,
            "book" : bookName
        })
    
    
    if data.find("a", class_="next_page"):
        buttonNext = data.find("a", class_="next_page")
        linkRelative = buttonNext["href"]
        
        url = urljoin(url,linkRelative)
    else:
        break
    
    
print(quotesArray)


with open("csv/quotesGoodReads.csv", mode="w", newline="", encoding="utf-8") as file:
    collum = ["author", "quote", "book"]
    
    writter = csv.DictWriter(file, fieldnames=collum)
    
    writter.writeheader()
    
    writter.writerows(quotesArray)

print("file quotesGoodReads.csv created with success!")


# print("response", data)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv


url = "https://quotes.toscrape.com/login"

session = requests.Session()

response = session.get(url)

data = BeautifulSoup(response.text, "html.parser")

form = data.find("form")

input = form.find_all("input")

inputHidden = input[0]
inputUsername = input[1]
inputPassword = input[2]
inputLogin = input[3]


token = inputHidden["value"]

data_login = {
    "csrf_token" : token,
    "username" : "vaida",
    "password" : "vadia",
}

responseLogin = session.post(url, data=data_login)

urlPage = "https://quotes.toscrape.com/page/1/"

dataLogin = BeautifulSoup(responseLogin.text, "html.parser")

linkRelative = None

i = 0 
quotes = []

while True:

    divQuotes = dataLogin.find_all("div", class_="quote")
    
    for quote in divQuotes:
        quoteText = quote.find("span").text
        authorName = quote.find("small").text

        tags = quote.find_all("a", class_="tag")

        quotesTags = []

        for tag in tags: 
            tagText = tag.text
            quotesTags.append(tagText)

        tagsFormatted = ", ".join(quotesTags)
        
        

        quotes.append({
            "author" : authorName,
            "quote" : quoteText,
            "tags" : tagsFormatted
        })


    
    if dataLogin.find("li", class_="next") : 
        botaoNext = dataLogin.find("li", class_="next").a
        linkRelative = botaoNext["href"]
        url_complete = urljoin(urlPage, linkRelative)
        
        responseNewPage =session.get(url_complete)
        responseNewPage.encoding = "utf-8"
        
        dataLogin = BeautifulSoup(responseNewPage.text,"html.parser")
                
        urlPage = url_complete
        
    else:
        break



with open("csv/quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    collum = ["author", "quote", "tags"]
    
    writter = csv.DictWriter(file, fieldnames=collum)
    
    writter.writeheader()
    
    writter.writerows(quotes)

print("file quotes.csv created with success!")
    
print(len(quotes))

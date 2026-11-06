import requests
import random
import os
from dotenv import load_dotenv
import csv

load_dotenv()

url = os.getenv("DISCORD_WEBHOOK_URL")

with open("quotesGoodReads.csv", mode="r", encoding="utf-8") as file:
    
    reader = csv.DictReader(file)
    allQuotes = list(reader)

    
    quoteOfTheDay = random.choice(allQuotes)
    
    book = quoteOfTheDay["book"]
    
    randomColor = random.randint(1, 0xFFFFFF)
    
    if book == "None":
        text_footer = quoteOfTheDay["author"]

    else: 
        text_footer = f"{quoteOfTheDay['author']} - {quoteOfTheDay['book']}"

    
    
    payload = {
        "embeds": [
        {
            "description": quoteOfTheDay["quote"],
            "color": randomColor,  
            "footer": {
                "text": text_footer
            }
        }
    ]
}
    
    
response = requests.post(url, json=payload)
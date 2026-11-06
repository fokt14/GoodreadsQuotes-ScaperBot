# 📚 Goodreads Quotes Discord Bot

A Python script that scrapes quotes from Goodreads or QuotesToScrape, stores them in a structured CSV file, and automatically sends a random daily quote to Discord via Webhooks using GitHub Actions.

---

## Why I built this

I was bored and wanted to do something...

---

## How it works

1. **`scrapper.py`**: Scrapes quotes, authors, and book tags from QuotesToScrape and saves everything to `csv/quotes.csv`.
2. **`goodReadsScrapper.py`**: Scrapes quotes, authors, and books from Goodreads and saves everything to `quotesGoodReads.csv`.
3. **`quoteToServer.py`**: Reads the CSV file, picks a random quote, and sends a formatted message (Embed with a random color) to Discord via Webhook.
4. **GitHub Actions**: Runs `quoteToServer.py` every day at a scheduled time without needing your computer to stay on.

---

## How to run locally

### 1. Install dependencies
In your terminal, create a virtual environment and install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment variables
Create a `.env` file in the project root with your Discord webhook URL and your User-Agent (you can simply copy `.env.example`):

```env
# To find your User-Agent, search "what is my user agent" in your browser
MY_USER_AGENT="YOUR_USER_AGENT"
DISCORD_WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL"
```

### 3. Run scripts

Scrape/update quotes:

```bash
python scrappers/scrapper.py  # Or scrappers/goodReadsScrapper.py
```

Send a quote to Discord:

```bash
python quoteToServer.py
```

---

## Automation on GitHub Actions

To enable automatic daily delivery in the cloud:

1. In your GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. For **Name**, enter: `DISCORD_WEBHOOK_URL`.
4. In **Secret**, paste your Discord Webhook URL and save.

The workflow file at `.github/workflows/daily_quote.yml` runs automatically every day at 07:00 UTC and allows manual triggers from the **Actions** tab.

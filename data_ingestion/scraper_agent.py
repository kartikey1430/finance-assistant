import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_market_headlines():
    api_key = os.getenv("NEWSDATA_API_KEY")
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&category=business&language=en"

    try:
        response = requests.get(url)
        data = response.json()
        results = data.get("results", [])
        headlines = [article["title"] for article in results if "title" in article]
        return headlines[:5]
    except Exception as e:
        print("❌ Error fetching headlines:", e)
        return []

# Test run
if __name__ == "__main__":
    for headline in get_market_headlines():
        print("•", headline)

from data_ingestion.api_agent import get_asia_tech_data

def get_sentiment(change):
    if change > 1:
        return "Positive"
    elif change < -1:
        return "Negative"
    return "Neutral"

def orchestrate():
    print("\U0001F4CA Fetching Asia tech stock data...")
    data = get_asia_tech_data()
    print("\n\U0001F4CA Stock Performance Report:")
    for stock in data:
        sentiment = get_sentiment(stock['change_percent'])
        print(f"\u2022 {stock['ticker']}: {stock['change_percent']}% \u2192 \U0001F4C8 {sentiment}")

if __name__ == "__main__":
    orchestrate()
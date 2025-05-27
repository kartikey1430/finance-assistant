from textblob import TextBlob

def analyze_headlines(headlines: list[str]) -> str:
    insights = []
    for headline in headlines:
        blob = TextBlob(headline)
        polarity = blob.sentiment.polarity
        tone = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
        insights.append(f"• {headline} → Sentiment: {tone}")
    
    return "\n".join(insights)

# Test
if __name__ == "__main__":
    sample = [
        "Gold price prediction for May 26, 2025: Should you buy or sell?",
        "Monsoon rains arrive early in Kerala",
        "JSW Steel Q4 result: Margin expansion, steady growth",
        "Stock market opens lower as yields climb",
        "Zeppto CEO accused of targeting rival firm"
    ]
    print("🧠 Analysis Report:")
    print(analyze_headlines(sample))

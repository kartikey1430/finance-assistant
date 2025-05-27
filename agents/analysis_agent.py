from textblob import TextBlob

from textblob import TextBlob

def analyze_sentiment(change_percent: float) -> str:
    text = f"The stock changed by {change_percent:.2f}%"
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


def analyze_headlines(headlines: list[str]) -> str:
    """
    Analyze multiple headlines and return formatted sentiment report.
    """
    insights = []
    for headline in headlines:
        tone = analyze_sentiment(headline)
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

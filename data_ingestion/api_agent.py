import yfinance as yf

def get_asia_tech_data(tickers=["TSM", "005930.KQ"]):
    result = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        if len(hist) >= 2:
            today = hist['Close'].iloc[-1]
            yesterday = hist['Close'].iloc[-2]
            change = round(((today - yesterday) / yesterday) * 100, 2)
            result.append({
                "ticker": ticker,
                "today_close": round(today, 2),
                "change_percent": change
            })
    return result

if __name__ == "__main__":
    data = get_asia_tech_data()
    for stock in data:
        print(f"{stock['ticker']}: {stock['change_percent']}%")
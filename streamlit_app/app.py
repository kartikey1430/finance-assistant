import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.set_page_config(page_title="Asia Tech Stock Sentiment", page_icon="📊", layout="centered")

# Custom styles
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: 700;
    }
    .positive {
        color: #21ba45;
    }
    .negative {
        color: #db2828;
    }
    .neutral {
        color: #fbbd08;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-font">📈 Asia Tech Stock Sentiment Dashboard</p>', unsafe_allow_html=True)
st.caption("Powered by Yahoo Finance | Visual insights + Sentiment")

tickers = {
    "TSMC": "TSM",
    "Samsung": "005930.KQ",
    "Sony": "6758.T",
    "Tencent": "0700.HK"
}

selected_stock = st.selectbox("Select a Stock", list(tickers.keys()))
ticker_symbol = tickers[selected_stock]

theme = st.radio("Choose Theme", ["Dark", "Light"], horizontal=True)
if theme == "Dark":
    st.markdown("<style>body { background-color: #0e1117; color: white; }</style>", unsafe_allow_html=True)
else:
    st.markdown("<style>body { background-color: white; color: black; }</style>", unsafe_allow_html=True)

if st.button("📊 Fetch & Analyze"):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="7d")

    if len(hist) < 2:
        st.error("Not enough data to evaluate sentiment.")
    else:
        today = hist['Close'].iloc[-1]
        yesterday = hist['Close'].iloc[-2]
        change = round(((today - yesterday) / yesterday) * 100, 2)
        volume = hist['Volume'].iloc[-1]
        sentiment = "Positive" if change > 1 else "Negative" if change < -1 else "Neutral"
        sentiment_icon = "🟢" if sentiment == "Positive" else "🔴" if sentiment == "Negative" else "🟡"
        market_cap = stock.info.get('marketCap', 'N/A')

        st.success("Data fetched successfully!")
        st.markdown(f"""
        ### {selected_stock}
        - **Change %**: <span class="{sentiment.lower()}">{change}%</span>  
        - **Sentiment**: {sentiment_icon} {sentiment}  
        - **Volume**: {volume:,}  
        - **Market Cap**: {market_cap if isinstance(market_cap, str) else f"{market_cap:,}"}
        """, unsafe_allow_html=True)

        # Plot closing prices
        st.subheader("📉 Closing Price Trend")
        fig, ax = plt.subplots()
        hist['Close'].plot(ax=ax, marker='o')
        ax.set_ylabel("Price (USD)")
        ax.set_xlabel("Date")
        ax.set_title(f"{selected_stock} - Last 7 Days")
        st.pyplot(fig)

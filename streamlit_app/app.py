import streamlit as st
from data_ingestion.api_agent import get_asia_tech_data

def get_sentiment(change):
    if change > 1:
        return "Positive"
    elif change < -1:
        return "Negative"
    return "Neutral"

st.set_page_config(page_title="Asia Tech Stock Sentiment")
st.title("\U0001F4C8 Asia Tech Stock Sentiment")
st.markdown("Powered by **Yahoo Finance** + sentiment logic")

if st.button("\U0001F4C8 Fetch Stock Data"):
    with st.spinner("Fetching data..."):
        data = get_asia_tech_data()
        st.success("Data fetched successfully!")

        for stock in data:
            sentiment = get_sentiment(stock['change_percent'])
            st.subheader(stock['ticker'])
            st.write("**Change %:**", f"{stock['change_percent']}%")
            st.write("**Sentiment:** \U0001F4CA", sentiment)

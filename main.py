import streamlit as st
import yfinance as fn


st.write(""" # My first App with
Streamlit """)

st.title ("Stock Market App with*Streamlit*")

st.header("Simple Data Science Web App")
st.sidebar.header("Bek Brace \n Code along with me ...")


# This is a fuction that fetches the company's ticker

def get_ticker(name):
    company = fn.Ticker(name)
    return company




    c1 = get_ticker("AAPL")
    c2 = get_ticker("MSFT")
    c3 = get_ticker("TSLA")

    # Fetching data for dataframe

    apple = fn.download("AAPL", start="2021-12-16", end="2021-12-16")
    microsoft = fn.download("MSFT", start="2021-12-16", end="2021-12-16")
    tesla = fn.download("TSLA", start="2021-12-16", end="2021-12-16")
    


    # Fetching historyical data by valid periods

    data1 = c1.history(period="3mo")
    data2 = c2.history(period="3mo")
    data3 = c3.history(period="3mo")


    #Markdown

    st.write(""" ### Apple """)

    #Detailed summary about Apple

    st.write(c1.info['longBusinessSummary'])

    #Dataframe

    st.write(apple)

    #Chart
    st.line_chart(data.value)


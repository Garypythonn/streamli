import yfinance as yf
import streamlit as st

st.write("""
# Muestra el **precio de cierre** y ***volumen*** de Apple
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
simbolito = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(simbolito)
#get the historical prices for this ticker
datos = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""## Precio de cierre""")
st.line_chart(datos.Close) #Buscar parámetros para poner ejes en español

st.write("""## Volumen""")
st.line_chart(datos.Volume)
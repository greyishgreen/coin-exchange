import streamlit as st
import requests
r = requests.get(f"https://open.er-api.com/v6/latest/TRY")
veri=r.json()

veri=veri.get("rates")
keysList = list(veri.keys())

kur=st.selectbox("please choose the currency to covert FROM", keysList)

r = requests.get(f"https://open.er-api.com/v6/latest/{kur}")
veri=r.json()

veri=veri.get("rates")
keysList2 = list(veri.keys())


miktar=float(st.number_input("please enter the amount "))
coin=st.selectbox("please choose the currency to covert TO", keysList2)
rate= veri.get(coin)
st.write(miktar, kur, "->", miktar*rate, coin)
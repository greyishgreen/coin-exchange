import streamlit as st
kazanc = float(st.number_input("brüt kazancınızı giriniz: "))
if kazanc <= 110000:
  net = kazanc * 85 / 100
elif kazanc <= 230000:
  a = kazanc - 110000
  net = kazanc - 16500 - (a*20/100)
elif kazanc <= 870000:
  a= kazanc - 230000
  net = kazanc - 40500 -(a*27/100)
elif kazanc <= 3000000:
  a= kazanc - 870000
  net = kazanc - 213300 - (a*35/100)
else:
  a = kazanc - 3000000
  net = kazanc - 958800 - (a*40/100)
st.write("net kazancınız:" , net)
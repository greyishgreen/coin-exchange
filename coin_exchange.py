import streamlit as st
import requests
r = requests.get("https://api.coincap.io/v2/assets")
veri=r.json()
veri=veri.get("data")
idler=[]
semboller=[]
idvesembolbirlikte=[]
fiyatlar= []
for i in veri:
    id=i.get("id")
    sembol = i.get("symbol")
    fiyat = float(i.get("priceUsd"))
    idler.append(id)
    semboller.append(sembol)
    fiyatlar.append(fiyat)

for i in range(len(idler)):
    a= idler[i] + "-" + semboller[i]
    idvesembolbirlikte.append(a)

coin1= st.selectbox("from",idvesembolbirlikte )
miktar=st.number_input("miktar: ")
index1=idvesembolbirlikte.index(coin1)
coin2= st.selectbox("to", idvesembolbirlikte)
index2=idvesembolbirlikte.index(coin2)
hesap=fiyatlar[index1]/fiyatlar[index2]
hesap2= miktar * fiyatlar[index1] / fiyatlar[index2]
st.write("1", coin1 , "->", hesap," ", coin2 )
st.write(miktar, coin1, "->", hesap2, coin2)




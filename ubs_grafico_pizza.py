import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('ubs_atualizado.csv', sep = ";")

valores = pd.DataFrame({
    "Estados": df['Nome_UF']
})

#Grafico de Pizza
grafico = px.pie(valores, names = "Estados", title = "Grafico")

st.plotly_chart(grafico)
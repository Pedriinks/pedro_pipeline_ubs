import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('ubs_atualizado.csv', sep = ";")

valores = pd.DataFrame({
    "Municipios": df['Nome_Município'],
    "Quantidade": df['NOME'].value_counts()
})

grafico = px.histogram(valores, x = "Municipios", y = "Quantidade", title = "Histograma")

#st.slider()

st.plotly_chart(grafico)

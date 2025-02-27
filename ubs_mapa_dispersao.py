import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('ubs_atualizado.csv', sep = ";")

latitudes = df['LATITUDE'],
longitudes = df['LONGITUDE']

st.plotly_chart(latitudes, longitudes, use_container_width=True)
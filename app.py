import pandas as pd 
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("vehicles.csv")

st.title("Análise de Dados de Veículos")

if st.button("Mostrar Dados"):
    st.dataframe(car_data)

fig = px.histogram(car_data, x="odometer", color="condition", title="Distribuição do Odômetro")
st.plotly_chart(fig)

fig = px.scatter(car_data, x="odometer", y="price", title="Odômetro x Preço")
st.plotly_chart(fig)

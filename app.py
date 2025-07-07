import pandas as pd
import streamlit as st 
import plotly.express as px 

car_data = pd.read_csv('vehicles_us.csv')

st.header("prueba encabezado")

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)

scattered_button = st.button("Construir cuadro de dipersión")
if scattered_button:
    st.write("se crea cuadro de disperción... miaumiau")

    fig_sc = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_sc, use_container_width=True)
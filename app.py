import pandas as pd
import streamlit as st 
import plotly.express as px 

car_data = pd.read_csv('vehicles_us.csv')

st.header("Análisis Exploratorio de Vehiculos en Venta Dentro de E.E.U.U.")

hist_button = st.button("Mostrar histograma") 

if hist_button:
    st.write("Este histograma muestra la distribución del kilometraje (`odometer`) de los vehículos en venta.")
    
    fig = px.histogram(car_data,
                       x="odometer",
                       nbins=30,
                       title="Distribución del kilometraje (Odometer)",
                       labels= {"odometer": "kilometraje"},
                       color_discrete_sequence=["#636EFA"])
    
    st.plotly_chart(fig, use_container_width=True)

scattered_button = st.button("Mostrar Diagrama de Dipersión")
if scattered_button:
    st.write("Este gráfico muestra la relación entre el kilometraje y el precio de los vehículos.")

    fig_sc = px.scatter(car_data,
                        x="odometer",
                        y="price",
                        title="Relación entre Kilometraje y Precio",
                        labels={"odometer": "Kilometraje", "price": "Precio (USD"},
                        opacity= 0.6,
                        color_discrete_sequence=["#EF553B"])

    st.plotly_chart(fig_sc, use_container_width=True)
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv('./vehicles_us.csv')

# Data Cleaning
filtered_df = df[~df['model_year'].isna()]

st.header("Vehicles' EDA")

# Botones
hist_button = st.button('Make histogram')
disp_button = st.button('Compare price vs year')

# Funcionalidad de los botones

if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creating a histogram for the car sales listings dataset')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=df["model_year"])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Cars in each year')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


if disp_button:
    # Escribir un mensaje en la aplicación
    st.write('Creating a scatter chart')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Scatter(x=filtered_df["model_year"], y=filtered_df['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relation year - price')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
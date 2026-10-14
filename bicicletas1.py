#Librerias que usaremos#
import streamlit as st
import pandas as pd 

#Titulo#
st.title("Bicicletas en la Ciudad")

#Dataframe#
dataframe = pd.read_csv("https://raw.githubusercontent.com/dylsaac/ciencia-de-datos/refs/heads/main/citibike-tripdata.csv",
encoding = "latin1")

#Side Bar#
sidebar = st.sidebar
# Agregamos un titulo y texto al sidebar
sidebar.title("Barra Mike en Tanga")

#Mostrar todos los datos checkbox#
# Creamos una casilla para mostrar el raw data #
mostrar_todos = sidebar.checkbox("Raw Data")

# Si la casilla está seleccionada
if mostrar_todos:

    # Mostramos todos los datos
    st.subheader("Raw Contenido")

    st.dataframe(dataframe)








#autores finales#
st.dataframe(dataframe)
st.write ("Hecho por:")
st.write ("Dylan Isaac Heredia Rodriguez")
st.write ("Mariana Reyes Lobato ")
st.write ("Juan Miguel Sanchez")
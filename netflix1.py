#Librerias que usaremos#
import streamlit as st
import pandas as pd 

#Titulo#
st.title("Netflix.App.SuperChida")

#Dataframe#
dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv",
encoding="latin1",)

#Side Bar#
sidebar = st.sidebar
# Agregamos un titulo y texto al sidebar
sidebar.title("Barra Super Chida")

#Mostrar todos los filmes#
# Creamos una casilla para mostrar todos los filmes
mostrar_todos = sidebar.checkbox("Mostrar todos los filmes")


# Si la casilla está seleccionada
if mostrar_todos:

    # Mostramos todos los datos
    st.subheader("Todos los filmes")

    st.dataframe(dataframe)



#----- BUSCAR FILMES POR TÍTULO ------#

# Texto que escribirá el usuario
titulo = sidebar.text_input("Título del filme:")


# Botón para buscar
buscar = sidebar.button("Buscar filmes")


# Si presionamos el botón
if buscar:

    # Buscamos el título dentro de la columna title
    resultado = dataframe[
        dataframe["name"].str.contains(titulo, case=False, na=False)
    ]

    # Mostramos el resultado
    st.subheader("Resultado de búsqueda")

    st.dataframe(resultado)


#----- BUSCAR POR DIRECTOR ------#
# Obtenemos los directores del dataframe
directores = dataframe["director"].dropna().unique()


# Creamos el menú para seleccionar un director
director = sidebar.selectbox(
    "Seleccionar Director",
    directores
)


#-----FILTRAR DIRECTORES-----#

# BOTON
filtrar = sidebar.button("Filtrar director")


# Si presionamos el botón
if filtrar:

    # Filtramos las películas del director seleccionado
    resultado = dataframe[
        dataframe["director"] == director
    ]

    # Mostramos las películas
    st.subheader("Películas del director")

    st.dataframe(resultado)


#autores finales#
st.dataframe(dataframe)
st.write ("Hecho por:")
st.write ("Dylan Isaac Heredia Rodriguez")
st.write ("Mariana Reyes Lobato ")
st.write ("Juan Miguel Sanchez")
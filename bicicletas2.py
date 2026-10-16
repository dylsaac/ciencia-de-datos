import streamlit as st
import pandas as pd
import numpy as np

#Titulo#
st.title("Bicicletas en la Ciudad")


#Dataframe#
dataframe = pd.read_csv("https://raw.githubusercontent.com/dylsaac/ciencia-de-datos/refs/heads/main/citibike-tripdata.csv",
encoding = "latin1")






#Side Bar#
sidebar = st.sidebar



# Titulo y Texto del Sidebar
sidebar.title("Barra Mike en Tanga")

mostrar_datos = st.sidebar.checkbox("raw datos", value=True)
mostrar_grafica = st.sidebar.checkbox("Recorridos por horA")






# Seleccionar horario
hora = st.sidebar.slider("HoraRio", 0, 23, 17)

datos = dataframe

# Mostrar datos de ese horario
if mostrar_datos:
    st.subheader("Raw")
    st.dataframe(datos)






#Lo HARDCORE#
# Mostrar recorridos por hora
if mostrar_grafica:
    datos["started_at"] = pd.to_datetime(datos["started_at"])
    datos["hora"] = datos["started_at"].dt.hour

    recorridos = datos["hora"].value_counts().sort_index()




    # Tabla 24 Horas
    tabla = pd.DataFrame(index=range(24))
    tabla["Recorridos"] = recorridos
    tabla = tabla.fillna(0)

    st.subheader("Numero de recorridos por hora")
    st.bar_chart(tabla)



    # Recorridos de la Hora
    datos_hora = datos[datos["hora"] == hora]

    st.write("Recorridos a las", hora, "horas:", len(datos_hora))
    st.dataframe(datos_hora)





    # MAPA
    datos["started_at"] = pd.to_datetime(datos["started_at"])
    datos["hora"] = datos["started_at"].dt.hour

    # Filtrar recorridos de la hora seleccionada
    datos_mapa = datos[datos["hora"] == hora]

    # Eliminar registros sin coordenadas
    datos_mapa = datos_mapa.dropna(subset=["start_lat", "start_lng"])

    st.subheader("Mapa de recorridos iniciados a las " + str(hora) + ":00")

    # Mostrar mapa
    st.map(
        datos_mapa,
        latitude="start_lat",
        longitude="start_lng"
    )
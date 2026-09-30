# Importamos la librería Streamlit
import streamlit as st
import datetime
import pandas as pd

#Date
# Dar al usuario la fecha actual
today = datetime.date.today()
today_date = st.date_input('Current date', today)
st.success('Current date: %s' % (today))

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")

#Checkbox
# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = st.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(titanic_data)

selected_town = st.radio("Select Embark Town",
titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)

#Slider
# Select a range of the fare and then display the dataset
optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
"Minimum Fare",
min_value=float(titanic_data['fare'].min()),
max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
"Maximum Fare",
min_value=float(titanic_data['fare'].min()),
max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
(fare_min <= titanic_data['fare'])]

st.dataframe(subset_fare)
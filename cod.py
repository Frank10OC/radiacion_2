import streamlit as st
import pandas as pd
import math
# Crear la aplicación Streamlit
st.title("Cálculo de ω y Actualización del CSV")

# Agregar un campo de entrada para ϕ
phi = st.number_input("Ingrese el valor de ϕ:", min_value=0.0, max_value=90.0, step=0.1)
# Leer el archivo CSV en un DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/radiacion_2/main/dato.csv")
st.write(df)
st.write(df["Declinación Solar"])
# Calcular ω utilizando la fórmula y agregarlo como una nueva columna
df["Hora_Solar"] = np.arccos(-np.tan(np.radians(df["Declinación Solar"])) * np.tan(np.radians(phi)))
# Actualizar la visualización del DataFrame con la nueva columna
st.write(df)

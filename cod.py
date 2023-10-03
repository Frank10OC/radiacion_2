import streamlit as st
import pandas as pd
import math
import numpy as np
# Crear la aplicación Streamlit
st.title("Cálculo de ω y Actualización del CSV")

# Agregar un campo de entrada para ϕ
phi = st.number_input("Ingrese la longitud (ϕ):", min_value=0.0, max_value=90.0, step=0.1)
# Leer el archivo CSV en un DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/Radiacion/main/dato.csv")
st.write(df)
st.write(df["Declinación Solar"])
# Calcular ω utilizando la fórmula y agregarlo como una nueva columna
df["Hora Solar"] = np.arccos(-np.tan(np.radians(df["Declinación Solar"])) * np.tan(np.radians(phi)))
# Actualizar la visualización del DataFrame con la nueva columna
st.write(df)

# Título de la aplicación
st.title("Cálculo de Radiación Solar en la Atmósfera Exterior")
# Conversión de grados a radianes
omega = np.radians(df['Hora Solar'] * 15.0)  # Convertir la hora solar en ángulo horario
delta = np.radians(df['Declinación Solar'])
phi = np.radians(longitud)
# Cálculo de la radiación solar (Ho)
factor = (24 / math.pi) * df['Radiación Solar']
term1 = (math.pi / 180) * omega * np.sin(delta) * np.sin(phi)
term2 = np.cos(delta) * np.cos(phi) * np.sin(omega)
ho = factor * (term1 + term2)
# Agregar los resultados al DataFrame
df['Radiación Solar Exterior'] = ho
# Mostrar el DataFrame con los resultados
st.write("Tabla de datos con Radiación Solar Exterior:")
st.dataframe(df)


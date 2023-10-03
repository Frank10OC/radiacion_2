import streamlit as st
import pandas as pd
import math
import numpy as np
def radianes_a_grados(radianes):
    grados = radianes * (180 / math.pi)
    return grados
st.title("Cálculo de Radiación Solar en la Atmósfera Exterior")
# Crear la aplicación Streamlit
st.write("Cálculo de ángulo horario de salida del Sol")
# Agregar un campo de entrada para ϕ
phi = st.number_input("Ingrese la longitud (ϕ):", min_value=-180.0, max_value=180.0, step=0.000001)
# Leer el archivo CSV en un DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/Radiacion/main/dato.csv")
# Calcular ω utilizando la fórmula y agregarlo como una nueva columna
df["Angulo horario de salida del Sol"] = radianes_a_grados(np.arccos(-np.tan(np.radians(df["Declinación Solar"])) * np.tan(np.radians(phi))))
# Actualizar la visualización del DataFrame con la nueva columna
st.write(df)
# Definir un diccionario de mapeo de nombres de columnas
nuevos_nombres = {'Radiación Solar': 'Intensidad Horaria'}

# Usar el método rename() para cambiar los nombres de las columnas
df = df.rename(columns=nuevos_nombres)

# Título de la aplicación

# Conversión de grados a radianes
omega =np.radians(df['Angulo horario de salida del Sol']) 
delta = np.radians(df['Declinación Solar'])
phi=np.radians(phi)

# Cálculo de la radiación solar (Ho)
factor = (24 / math.pi) * df['Intensidad Horaria']
term1 = (math.pi / 180) * radianes_a_grados(omega) * np.sin(delta) * np.sin(phi)
term2 = np.cos(delta) * np.cos(phi) * np.sin(omega)
ho = factor * (term1 + term2)
# Agregar los resultados al DataFrame
df['Radiación Solar Exterior'] = ho
# Mostrar el DataFrame con los resultados
st.write("Tabla de datos con Radiación Solar Exterior:")
st.dataframe(df)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Gráfico de Áreas con Datos de un CSV")

# Crear el gráfico de áreas
st.area_chart(df[["dia", 'Radiación Solar Exterior']])

# Opcional: Mostrar una tabla con los datos
st.write("Tabla de Datos:")
st.write(df)


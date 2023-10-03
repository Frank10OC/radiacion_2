import streamlit as st
import pandas as pd
import math

# Función para calcular la radiación solar
def calcular_radiacion_solar(N):
    Ics = 4921.2  # Radiación solar extraterrestre en W/m^2
    angulo_solar = 360 * N / 365
    coseno_term = 0.0033 * math.cos(math.radians(angulo_solar))
    radiacion_solar = Ics * (1 + coseno_term)
    return radiacion_solar

# Crear un DataFrame llamado 'operaciones'
operaciones = pd.DataFrame({'N': range(1, 366)})

# Agregar una columna 'RadiacionSolar' para almacenar los resultados
operaciones['RadiacionSolar'] = operaciones['N'].apply(calcular_radiacion_solar)

# Configurar la aplicación Streamlit
st.title('Operaciones con DataFrame')
st.sidebar.header('Configuración')

# Mostrar el DataFrame 'operaciones' en la interfaz
st.write(operaciones)

# Opcional: Guardar el DataFrame 'operaciones' en un archivo CSV
if st.button('Guardar DataFrame'):
    operaciones.to_csv('operaciones_radiacion_solar.csv', index=False)
    st.success('DataFrame guardado en operaciones_radiacion_solar.csv')

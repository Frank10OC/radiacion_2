# Agregar un campo de entrada para ϕ
phi = st.number_input("Ingrese el valor de ϕ:", min_value=0.0, max_value=90.0, step=0.1)
 # Leer el archivo CSV en un DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/Radiacion/main/dato.csv")
# Calcular ω utilizando la fórmula y agregarlo como una nueva columna
df["Hora Solar"] = np.arccos(-np.tan(np.radians(df["Declinación Solar"])) * np.tan(np.radians(phi)))
# Actualizar la visualización del DataFrame con la nueva columna
st.write(df)

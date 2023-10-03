# Crear la aplicación Streamlit
st.title("Cálculo de ω y Actualización del CSV")

# Agregar un componente de carga de archivo CSV
uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

# Agregar un campo de entrada para ϕ
phi = st.number_input("Ingrese el valor de ϕ:", min_value=0.0, max_value=90.0, step=0.1)

# Verificar si se ha cargado un archivo CSV
if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Calcular ω utilizando la fórmula y agregarlo como una nueva columna
    df["Hora Solar"] = np.arccos(-np.tan(np.radians(df["δ"])) * np.tan(np.radians(phi)))

    # Actualizar la visualización del DataFrame con la nueva columna
    st.write(df)

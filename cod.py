phi = st.number_input("Ingrese el valor de ϕ:", min_value=0.0, max_value=90.0, step=0.1)
# Verificar si se ha cargado un archivo CSV
if uploaded_file is not None:
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(uploaded_file)

    # Calcular ω utilizando la fórmula y agregarlo como una nueva columna
    df["Hora Solar"] = np.arccos(-np.tan(np.radians(df["δ"])) * np.tan(np.radians(phi)))

    # Actualizar la visualización del DataFrame con la nueva columna
    st.write(df)

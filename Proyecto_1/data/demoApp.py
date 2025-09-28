import streamlit as st
import pandas as pd
import numpy as np

# Titulo y descripción
st.title(" Mi primera app con Streamlit")
st.write("Aqui probamos datos, gráficos y controles interactivos.")

# Slider para que el usuario elija un número
numero = st.slider("Elige un número", 1, 100, 10)
st.write(f"Has elegido el número: {numero}")

# crear un DataFrame de ejemplo
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Columna A', 'Columna B', 'Columna C']
)

# Mostrar tabla
st.subheader("Tabla de datos aleatorios")
st.dataframe(data)

# Mostrar gráfico de lineas
st.subheader("Gráfico de lineas")
st.line_chart(data)

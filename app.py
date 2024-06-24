import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("Ayemeter")

# Introducir datos
st.sidebar.header("Datos de Entrada")
mood = st.sidebar.slider("Nivel de ánimo (1-10)", 1, 10, 5)
date = st.sidebar.date_input("Fecha")

# Crear DataFrame
data = {
    "Fecha": [date],
    "Ánimo": [mood]
}
df = pd.DataFrame(data)

# Mostrar DataFrame
st.write("### Datos de Entrada", df)

# Gráfica
st.write("### Gráfica de Ánimo")
fig, ax = plt.subplots()
ax.plot(df["Fecha"], df["Ánimo"], marker="o")
st.pyplot(fig)
import streamlit as st
import numpy as np
import pandas as pd

st.title("🏃 Simulador de Running")

# Parámetros de entrada
distancia = st.slider("Distancia objetivo (km)", 5, 42, 10)
ritmo = st.number_input("Ritmo promedio (min/km)", 3.5, 10.0, 5.0)

# Cálculo
tiempo_estimado = distancia * ritmo

st.subheader("Resultados de la simulación")
st.write(f"Distancia: **{distancia} km**")
st.write(f"Ritmo: **{ritmo} min/km**")
st.write(f"Tiempo estimado: **{tiempo_estimado:.1f} minutos**")

# Simulación simple de ritmo durante 30 días
dias = np.arange(1, 31)
rendimiento = np.random.normal(loc=ritmo, scale=0.2, size=len(dias))

df = pd.DataFrame({
    "Día": dias,
    "Ritmo simulado (min/km)": rendimiento
})

st.line_chart(df.set_index("Día"))




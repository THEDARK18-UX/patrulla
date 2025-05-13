import streamlit as st

# Configuración de la página
st.set_page_config(page_title="⚗️ Cálculo Militar de Gases Ideales", layout="centered")

# Título e introducción
st.title("🪖 Cálculo de Gases Ideales para Misiones Militares")
st.markdown("""
Este aplicativo aplica la ley de los gases ideales:  
\[
PV = nRT
\]
para apoyar en el análisis de **condiciones tácticas en altura**, **uso de oxígeno en misiones prolongadas**, y **operaciones en ambientes confinados**.

**Constante de los gases (R)**: 0.0821 L·atm/mol·K
""")

R = 0.0821

# Selección de variable a calcular
opcion = st.selectbox("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Cantidad de sustancia (n)", "Temperatura (T)"])

st.markdown("### 📥 Ingresa los valores conocidos")

# Entradas según lo que se desea calcular
if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.01, format="%.2f")
    n = st.number_input("Cantidad de sustancia (mol)", min_value=0.001, format="%.4f")
    T = st.number_input("Temperatura (K)", min_value=0.1, format="%.2f")

    if st.button("📌 Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"✅ Presión calculada: {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.01, format="%.2f")
    n = st.number_input("Cantidad de sustancia (mol)", min_value=0.001, format="%.4f")
    T = st.number_input("Temperatura (K)", min_value=0.1, format="%.2f")

    if st.button("📌 Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"✅ Volumen calculado: {V:.3f} L")

elif opcion == "Cantidad de sustancia (n)":
    P = st.number_input("Presión (atm)", min_value=0.01, format="%.2f")
    V = st.number_input("Volumen (L)", min_value=0.01, format="%.2f")
    T = st.number_input("Temperatura (K)", min_value=0.1, format="%.2f")

    if st.button("📌 Calcular Moles"):
        n = (P * V) / (R * T)
        st.success(f"✅ Moles calculados: {n:.4f} mol")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.01, format="%.2f")
    V = st.number_input("Volumen (L)", min_value=0.01, format="%.2f")
    n = st.number_input("Cantidad de sustancia (mol)", min_value=0.001, format="%.4f")

    if st.button("📌 Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"✅ Temperatura calculada: {T:.2f} K")

# Información complementaria
st.markdown("---")
st.markdown("""
🧠 **Consejo táctico:**  
En misiones de altura (>3500 msnm), la cantidad de oxígeno disponible disminuye drásticamente. Este aplicativo permite calcular cuántos litros de gas se necesitan para mantener con vida a una patrulla en movimiento bajo diferentes condiciones.

📦 Si deseas calcular **autonomía de cilindros de oxígeno**, podemos incluirlo en una versión avanzada.
""")

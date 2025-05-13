import streamlit as st

# Configuración de la página
st.set_page_config(page_title="🪖 Gases Ideales en Operaciones Militares", layout="centered")
st.title("🪖 Calculadora Militar de Gases Ideales (PV = nRT)")

st.image("https://i.imgur.com/1uKx2pw.jpg", caption="Simulación táctica con uso de oxígeno en altura", use_column_width=True)

st.markdown("""
### 🎖️ Aplicación en el Contexto Militar

Este aplicativo permite calcular cualquiera de las variables de la ecuación de gases ideales, lo que es **esencial en operaciones** donde:
- Se necesita **oxígeno suplementario** en altura.
- Se usan **gases químicos** en simulaciones o entrenamiento CBRN.
- Se calcula la **autonomía de cilindros de oxígeno** en evacuaciones.

**Ecuación base:**
\[
PV = nRT
\]
""")

# Constante universal
R = 0.0821  # L·atm/mol·K

# Elegir qué variable calcular
st.subheader("🛠️ Selecciona qué variable deseas calcular")
opcion = st.selectbox("Variable a calcular:", ["Presión (P)", "Volumen (V)", "Moles (n)", "Temperatura (T)"])

# Descripciones por variable
descripciones = {
    "Presión (P)": "Se usa para determinar la presión necesaria para mantener un gas en un volumen controlado. Útil en tanques o recintos cerrados.",
    "Volumen (V)": "Calcula el volumen que ocupará un gas. Útil para estimar el espacio en cilindros o refugios presurizados.",
    "Moles (n)": "Determina cuánta sustancia de gas se necesita. Útil para calcular el suministro de oxígeno.",
    "Temperatura (T)": "Estima la temperatura en un sistema cerrado. Útil en simulaciones o cámaras hiperbáricas."
}
st.info(descripciones[opcion])

# Entrada de datos según variable elegida
st.subheader("📋 Ingrese los datos conocidos")

if opcion == "Presión (P)":
    V = st.slider("Volumen (L)", 1.0, 100.0, 20.0)
    n = st.slider("Moles (n)", 0.1, 10.0, 2.0)
    T = st.slider("Temperatura (K)", 250, 400, 298)
    if st.button("📌 Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"🧮 Presión: {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.slider("Presión (atm)", 0.5, 10.0, 1.0)
    n = st.slider("Moles (n)", 0.1, 10.0, 2.0)
    T = st.slider("Temperatura (K)", 250, 400, 298)
    if st.button("📌 Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"🧮 Volumen: {V:.3f} L")

elif opcion == "Moles (n)":
    P = st.slider("Presión (atm)", 0.5, 10.0, 1.0)
    V = st.slider("Volumen (L)", 1.0, 100.0, 20.0)
    T = st.slider("Temperatura (K)", 250, 400, 298)
    if st.button("📌 Calcular Moles"):
        n = (P * V) / (R * T)
        st.success(f"🧮 Moles: {n:.4f} mol")

elif opcion == "Temperatura (T)":
    P = st.slider("Presión (atm)", 0.5, 10.0, 1.0)
    V = st.slider("Volumen (L)", 1.0, 100.0, 20.0)
    n = st.slider("Moles (n)", 0.1, 10.0, 2.0)
    if st.button("📌 Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"🧮 Temperatura: {T:.2f} K")

st.markdown("---")
st.markdown("🔧 Esta herramienta es útil para operaciones logísticas, de salud y entrenamiento militar en ambientes controlados o extremos.")

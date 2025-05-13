import streamlit as st

# Configuración de la página
st.set_page_config(page_title="🪖 Gases Ideales para Uso Militar", layout="centered")

# Título e ilustración
st.title("🪖 Aplicación Militar de Gases Ideales")
st.image(
    "https://i.imgur.com/1uKx2pw.jpg",
    caption="Simulación táctica con uso de oxígeno en altura",
    use_container_width=True
)

# Introducción
st.markdown("""
## 🎖️ Uso Estratégico de la Ley de los Gases Ideales

Esta herramienta permite calcular variables clave en situaciones donde los **gases** (como oxígeno, nitrógeno o CO₂) son vitales para:

- Misiones a gran altitud (donde el oxígeno escasea).
- Evaluación de autonomía de cilindros de aire en rescates.
- Entrenamiento CBRN (Químico, Biológico, Radiológico y Nuclear).
- Operaciones en entornos cerrados o submarinos.

**Ley de los Gases Ideales:**
\[
PV = nRT
\]
Donde:
- `P` = Presión (atm)
- `V` = Volumen (L)
- `n` = Cantidad de sustancia (mol)
- `R` = Constante (0.0821 L·atm/mol·K)
- `T` = Temperatura absoluta (K)
""")

R = 0.0821  # Constante universal de los gases en L·atm/mol·K

# Selección de variable a calcular
st.subheader("🛠️ Selecciona la variable a calcular")
opcion = st.selectbox("¿Qué deseas calcular?", ["Presión (P)", "Volumen (V)", "Cantidad de sustancia (n)", "Temperatura (T)"])

# Variables de entrada con sliders (sólo numéricas)
st.subheader("📋 Ingrese los valores conocidos")

if opcion == "Presión (P)":
    volumen = st.slider("Volumen (L)", 1.0, 100.0, 20.0)
    moles = st.slider("Cantidad de sustancia (mol)", 0.1, 10.0, 2.0)
    temperatura = st.slider("Temperatura (K)", 250, 400, 298)
    if st.button("📌 Calcular Presión"):
        presion = (moles * R * temperatura) / volumen
        st.success(f"✅ **Presión:** {presion:.3f} atm")

elif opcion == "Volumen (V)":
    presion = st.slider("Presión (atm)", 0.5, 10.0, 1.0)
    moles = st.slider("Cantidad de sustancia (mol)", 0.1, 10.0, 2.0)
    temperatura = st.slider("Temperatura (K)", 250, 400, 298)
    if st.button("📌 Calcular Volumen"):
        volumen = (moles * R * temperatura) / presion
        st.success(f"✅ **Volumen:** {volumen:.3f} L")

elif opcion == "Cantidad de sustancia (n)":
    presion = st.slider("Presión (atm)", 0.5, 10.0, 1.0)
    volumen = st.slider("Volumen (L)", 1.0, 100.0, 20.0)
    temperatura = st.slider("Temperatura (K)", 250, 400, 298)
    if st.button("📌 Calcular Moles"):
        moles = (presion * volumen) / (R * temperatura)
        st.success(f"✅ **Cantidad de sustancia:** {moles:.4f} mol")

elif opcion == "Temperatura (T)":
    presion = st.slider("Presión (atm)", 0.5, 10.0, 1.0)
    volumen = st.slider("Volumen (L)", 1.0, 100.0, 20.0)
    moles = st.slider("Cantidad de sustancia (mol)", 0.1, 10.0, 2.0)
    if st.button("📌 Calcular Temperatura"):
        temperatura = (presion * volumen) / (moles * R)
        st.success(f"✅ **Temperatura:** {temperatura:.2f} K")

# Pie de página
st.markdown("---")
st.markdown("""
🔍 **Nota:** Esta aplicación está diseñada para fines académicos y estratégicos. Adaptada para entornos militares donde se requiere **precisión en el uso de gases**.

🧠 ¿Quieres calcular la **autonomía de oxígeno** de un cilindro en una patrulla? Pide la siguiente versión avanzada.
""")

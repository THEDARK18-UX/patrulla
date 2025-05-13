import streamlit as st

st.set_page_config(page_title="📐 Gases Ideales Militares", layout="centered")

st.title("🎖️ Aplicación Militar - Ley de los Gases Ideales (PV = nRT)")
st.markdown("Calculadora de gases ideales adaptada a condiciones de **altura, presión y logística militar**.")

st.markdown("---")

st.subheader("🔧 Seleccione qué desea calcular:")
opcion = st.selectbox("Variable desconocida:", ["Cantidad de sustancia (n)", "Presión (P)", "Volumen (V)", "Temperatura (T)"])

# Entrada de datos
col1, col2 = st.columns(2)

with col1:
    P = st.number_input("Presión (atm)", min_value=0.0, value=1.0, step=0.1, format="%.2f")
    V = st.number_input("Volumen (L)", min_value=0.0, value=1.0, step=0.1, format="%.2f")
with col2:
    T = st.number_input("Temperatura (K)", min_value=1.0, value=273.15, step=0.1, format="%.2f")
    R = st.number_input("Constante R (L·atm/mol·K)", value=0.0821, format="%.4f")

resultado = None
formula_utilizada = ""

if st.button("📌 Calcular"):
    try:
        if opcion == "Cantidad de sustancia (n)":
            resultado = (P * V) / (R * T)
            formula_utilizada = f"n = (P × V) / (R × T) = ({P} × {V}) / ({R} × {T})"
        elif opcion == "Presión (P)":
            resultado = (resultado := (R * T * st.number_input("n (mol)", min_value=0.0, value=1.0)) / V)
            formula_utilizada = f"P = (n × R × T) / V"
        elif opcion == "Volumen (V)":
            resultado = (resultado := (st.number_input("n (mol)", min_value=0.0, value=1.0) * R * T) / P)
            formula_utilizada = f"V = (n × R × T) / P"
        elif opcion == "Temperatura (T)":
            resultado = (resultado := (P * V) / (st.number_input("n (mol)", min_value=0.0, value=1.0) * R))
            formula_utilizada = f"T = (P × V) / (n × R)"

        st.success(f"✅ Resultado: {opcion} = {resultado:.4f}")

        # Mostrar botón de verificación
        if st.button("📘 Resolución detallada del problema"):
            st.markdown("### 🧪 Paso a paso:")
            st.code(f"""
Fórmula utilizada: {formula_utilizada}

Sustituyendo valores:
  = {resultado:.4f}

Interpreta el resultado según la variable analizada:
 - Si n: moles de gas presentes en el sistema.
 - Si P: presión interna generada por el gas.
 - Si V: volumen necesario.
 - Si T: temperatura a la que se encuentra el gas.
""", language="python")

    except Exception as e:
        st.error(f"Error en el cálculo: {e}")

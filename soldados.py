import streamlit as st

# Configuración de página
st.set_page_config(page_title="🫁 Oxígeno en Patrulla Militar", layout="centered")
st.title("🫁 Calculadora de Oxígeno - Patrulla Militar en Altura")

# Paso 1: Datos de la misión
st.subheader("🔍 Datos de la Misión")

n_soldados = st.slider("Número de soldados en la patrulla:", 1, 50, 10)
duracion_horas = st.slider("Duración de la misión (horas):", 1, 24, 8)
actividad = st.selectbox("Nivel de esfuerzo físico:",
                         ["Reposo", "Moderado (marcha)", "Alto (combate)"])

# Paso 2: Fijar consumo de oxígeno según actividad
consumo_por_min = {
    "Reposo": 0.5,
    "Moderado (marcha)": 1.0,
    "Alto (combate)": 1.8
}

consumo_min = consumo_por_min[actividad]
vol_total_litros = n_soldados * duracion_horas * 60 * consumo_min
moles_o2 = vol_total_litros / 22.4
masa_o2 = moles_o2 * 32  # g/mol del O2

# Resultado
st.subheader("📊 Resultado del Cálculo")
st.markdown(f"""
- **Soldados**: {n_soldados}  
- **Duración**: {duracion_horas} h  
- **Nivel de esfuerzo**: {actividad}  
- **Consumo total estimado de O₂**:  
  - 🧪 **{vol_total_litros:.1f} L de oxígeno**
  - ⚖️ **{masa_o2:.2f} gramos de O₂**
""")

st.info("Este cálculo asume condiciones normales de presión y temperatura. En altura, el volumen de oxígeno disponible puede disminuir considerablemente.")

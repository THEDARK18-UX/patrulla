import streamlit as st

# Configuración de la página
st.set_page_config(page_title="💨 Ley de Gases Ideales - Militar", layout="centered")
st.title("💨 Cálculo con la Ley de Gases Ideales - Aplicación Militar")

st.markdown("""
Esta aplicación permite calcular una de las variables de la ley de los gases ideales (**PV = nRT**), útil para situaciones como operaciones en altura donde se utiliza oxígeno comprimido.

- **P**: Presión (atm)
- **V**: Volumen (L)
- **n**: Moles de gas (mol)
- **R**: Constante universal de los gases = 0.0821 L·atm/mol·K
- **T**: Temperatura (K)
""")

R = 0.0821

opciones = ["Cantidad de sustancia (n)", "Presión (P)", "Volumen (V)", "Temperatura (T)"]
calculo = st.selectbox("¿Qué deseas calcular?", opciones)

# Entrada de datos según opción
if calculo != "Cantidad de sustancia (n)":
    n = st.number_input("Cantidad de sustancia (n) [mol]", min_value=0.0, format="%.4f")
if calculo != "Presión (P)":
    V = st.number_input("Volumen (V) [L]", min_value=0.0, format="%.2f")
if calculo != "Volumen (V)":
    P = st.number_input("Presión (P) [atm]", min_value=0.0, format="%.2f")
if calculo != "Temperatura (T)":
    T = st.number_input("Temperatura (T) [K]", min_value=1.0, format="%.2f")

resultado = None
verificacion = ""

if st.button("🧮 Calcular"):
    try:
        if calculo == "Cantidad de sustancia (n)":
            resultado = (P * V) / (R * T)
            verificacion = f"n = (P × V) / (R × T)\n  = ({P} × {V}) / ({R} × {T})\n  = {P*V:.4f} / {R*T:.4f}\n  = {resultado:.4f} mol"
        elif calculo == "Presión (P)":
            resultado = (n * R * T) / V
            verificacion = f"P = (n × R × T) / V\n  = ({n} × {R} × {T}) / {V}\n  = {n*R*T:.4f} / {V}\n  = {resultado:.4f} atm"
        elif calculo == "Volumen (V)":
            resultado = (n * R * T) / P
            verificacion = f"V = (n × R × T) / P\n  = ({n} × {R} × {T}) / {P}\n  = {n*R*T:.4f} / {P}\n  = {resultado:.4f} L"
        elif calculo == "Temperatura (T)":
            resultado = (P * V) / (n * R)
            verificacion = f"T = (P × V) / (n × R)\n  = ({P} × {V}) / ({n} × {R})\n  = {P*V:.4f} / {n*R:.4f}\n  = {resultado:.2f} K"

        st.success(f"✅ Resultado: {resultado:.4f} {calculo[-2:] if calculo != 'Temperatura (T)' else 'K'}")
    except Exception as e:
        st.error(f"Error en el cálculo: {e}")

if resultado is not None:
    if st.button("🔍 Verificación detallada"):
        st.markdown(f"""
        ### 📄 Verificación Paso a Paso:
        {verificacion.replace(chr(10), '<br>')}
        """, unsafe_allow_html=True)

st.markdown("""
---
📌 **Aplicación militar**: Este cálculo es útil para determinar el oxígeno disponible en cilindros durante operaciones en altura, rescates o maniobras en condiciones extremas.
""")

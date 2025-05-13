import streamlit as st

st.set_page_config(page_title="📐 Gases Ideales Militares", layout="centered")

st.title("🎖️ Aplicación Militar - Ley de los Gases Ideales (PV = nRT)")
st.markdown("Calculadora adaptada para situaciones militares en altura, presión de tanques, y logística en campo.")

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

# n adicional si hace falta
n_input = None
if opcion in ["Presión (P)", "Volumen (V)", "Temperatura (T)"]:
    n_input = st.number_input("n (mol)", min_value=0.0, value=1.0)

resultado = None
formula_utilizada = ""

if st.button("📌 Calcular"):
    try:
        if opcion == "Cantidad de sustancia (n)":
            resultado = (P * V) / (R * T)
            formula_utilizada = f"n = (P × V) / (R × T) = ({P} × {V}) / ({R} × {T})"
        elif opcion == "Presión (P)":
            resultado = (n_input * R * T) / V
            formula_utilizada = f"P = (n × R × T) / V = ({n_input} × {R} × {T}) / {V}"
        elif opcion == "Volumen (V)":
            resultado = (n_input * R * T) / P
            formula_utilizada = f"V = (n × R × T) / P = ({n_input} × {R} × {T}) / {P}"
        elif opcion == "Temperatura (T)":
            resultado = (P * V) / (n_input * R)
            formula_utilizada = f"T = (P × V) / (n × R) = ({P} × {V}) / ({n_input} × {R})"

        st.success(f"✅ Resultado: {opcion} = {resultado:.4f}")

        if st.button("📘 Resolución detallada del problema"):
            st.markdown("### 🧪 Paso a paso de la resolución:")
            st.code(f"""
Fórmula utilizada:
  {formula_utilizada}

Resultado:
  {opcion} = {resultado:.4f} unidades

Contexto militar:
 - Si n: moles de gas disponibles para respiración.
 - Si P: presión necesaria en cilindros.
 - Si V: volumen que debe tener el contenedor.
 - Si T: temperatura en condiciones extremas.
""", language="python")

    except Exception as e:
        st.error(f"Error en el cálculo: {e}")

# NUEVO BOTÓN: explicación paso a paso antes de resolver
if st.button("🧭 Explicación paso a paso"):
    st.markdown("### 🧠 ¿Cómo se resuelve un problema de gases ideales?")
    st.markdown("""
1. **Identifica los datos conocidos**:
   - Presión (P) en atmósferas.
   - Volumen (V) en litros.
   - Temperatura (T) en kelvin.
   - Constante de los gases (R = 0.0821 L·atm/mol·K).
   - Moles de gas (n), si se conoce.

2. **Selecciona la fórmula adecuada**:
   - Usa `PV = nRT`, y despeja la variable que deseas calcular.

3. **Sustituye los valores numéricos** en la fórmula.

4. **Realiza las operaciones matemáticas**:
   - Multiplica, divide y obtén el resultado con unidades.

5. **Interpreta el resultado** en el contexto militar:
   - ¿Es la presión segura?
   - ¿Es la cantidad de oxígeno suficiente?
   - ¿Requiere ajustar temperatura o volumen?

6. **Verifica si las unidades son coherentes**:
   - Atm, L, mol, K.

> Esta lógica es útil en logística de misiones, supervivencia en altura, uso de oxígeno en evacuaciones, o transporte de materiales en cilindros presurizados.
    """)


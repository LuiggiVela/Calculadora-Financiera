import streamlit as st
import math

st.set_page_config(page_title="Calculadora Financiera", layout="centered")
st.title("📈 Calculadora Financiera")

opciones = [
    "Cuota mensual de un préstamo",
    "Interés compuesto",
    "Valor presente",
    "Valor futuro"
]

opcion = st.selectbox("Selecciona un cálculo:", opciones)

if opcion == opciones[0]:
    monto = st.number_input("Monto del préstamo:", min_value=0.0)
    tasa = st.number_input("Tasa de interés anual (%):", min_value=0.0)
    años = st.number_input("Años del préstamo:", min_value=0)

    if st.button("Calcular cuota mensual"):
        r = tasa / 100 / 12
        n = años * 12
        if r != 0:
            cuota = monto * r * math.pow(1 + r, n) / (math.pow(1 + r, n) - 1)
        else:
            cuota = monto / n
        st.success(f"💵 Cuota mensual: S/ {cuota:.2f}")

elif opcion == opciones[1]:
    principal = st.number_input("Capital inicial:", min_value=0.0)
    tasa = st.number_input("Tasa de interés anual (%):", min_value=0.0)
    años = st.number_input("Número de años:", min_value=0.0)

    if st.button("Calcular monto final"):
        monto = principal * (1 + tasa/100) ** años
        st.success(f"Monto final: S/ {monto:.2f}")

elif opcion == opciones[2]:
    futuro = st.number_input("Valor futuro:", min_value=0.0)
    tasa = st.number_input("Tasa de descuento anual (%):", min_value=0.0)
    años = st.number_input("Años:", min_value=0.0)

    if st.button("Calcular valor presente"):
        presente = futuro / (1 + tasa/100) ** años
        st.success(f"Valor presente: S/ {presente:.2f}")

elif opcion == opciones[3]:
    presente = st.number_input("Valor presente:", min_value=0.0)
    tasa = st.number_input("Tasa de interés anual (%):", min_value=0.0)
    años = st.number_input("Años:", min_value=0.0)

    if st.button("Calcular valor futuro"):
        futuro = presente * (1 + tasa/100) ** años
        st.success(f"Valor futuro: S/ {futuro:.2f}")

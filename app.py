import os
import json
import streamlit as st

from utils.nueva_app import add_app
from utils.stop_app import stop_app
from utils.levantar_app import levantar_app
from utils.revisar_puerto import puerto_disponible

st.title("Interfaz de Control de Desarrollos")

PID_FILE = "desarrollos_pids.json"

if os.path.exists(PID_FILE):
    with open(PID_FILE, "r") as f:
        desarrollos_data = json.load(f)
else:
    desarrollos_data = {}

st_cols_so = st.columns(3)
sist_operativo = st_cols_so[1].selectbox("Selecciona tu Sistema Operativo", options=["Linux", "Windows"])

st.header("Agregar un Nuevo Desarrollo")

st_col_name, st_col_port = st.columns([3, 1])

nombre_input = st_col_name.text_input("Ruta y nombre del Desarrollo (p.ej.:ruta/al/proyecto/app.py)", "")
puerto_input = st_col_port.text_input("Puerto del Desarrollo", "")
config_input = st.text_input("Configuración adicional", "")

if st.button("Agregar"):
    if not nombre_input:
        st.warning("Por favor, ingresa un nombre para el desarrollo.")
    elif not puerto_input.isdigit():
        st.warning("Por favor, ingresa un NÚMERO de puerto válido.")
    elif not puerto_disponible(int(puerto_input), PID_FILE):
        st.warning("El puerto ingresado ya está en uso. Por favor, elige otro.")
    else:
        add_app(nombre_input, puerto_input, config_input, PID_FILE, sist_operativo)

st.header("Desarrollos Actuales")

for keys_desarr, values_desarr in desarrollos_data.items():
    ruta = values_desarr["ruta"]
    puerto = values_desarr["puerto"]
    estado = values_desarr.get("status", "Detenido")

    st_cols_header = st.columns(3)

    with st_cols_header[0]:
        st.markdown(f"**Desarrollo:** {keys_desarr}")

    with st_cols_header[1]:
        color = "#00FF00" if estado == "Ejecutando" else "#FF0000"
        boton_txt = "Tirar" if estado == "Ejecutando" else "Levantar"
        st.markdown(f"<p style='color:{color}; font-weight:bold;'>{estado}</p>", unsafe_allow_html=True)
        st.write("Puerto:", puerto)

    with st_cols_header[2]:
        if estado == "Ejecutando":
            if st.button(f"{boton_txt}", key=f"{keys_desarr}_tirar", use_container_width=True):
                stop_app(keys_desarr, PID_FILE)
        else:
            if st.button(f"{boton_txt}", key=f"{keys_desarr}_levantar", use_container_width=True):
                levantar_app(keys_desarr, PID_FILE, sist_operativo)

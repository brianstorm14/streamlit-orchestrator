import streamlit as st
import subprocess
import sys
import os

st.header("Interfaz de control de desarrollos.")

if "num_desarrollos" not in st.session_state:
    st.session_state.num_desarrollos = 0
    st.session_state.desarrollos = []
    st.session_state.puertos = []

nombre_input = st.text_input("Nombre del Desarrollo", "")
puerto_input = st.text_input("Puerto del Desarrollo", "")

if st.button("Agregar"):
    if nombre_input:
        st.session_state.desarrollos.append(nombre_input)
        if puerto_input.isdigit():
            st.session_state.puertos.append(int(puerto_input))
        else:
            st.session_state.puertos.append(8501 + st.session_state.num_desarrollos)
        st.session_state.num_desarrollos += 1

        script_name = f"{nombre_input}.py"
        if os.path.exists(script_name):
            try:
                st.write(f"Ejecutando {nombre_input}")
                subprocess.Popen(["streamlit","run",script_name,"--server.port",f"{puerto_input}"])
            except Exception as e:
                st.error(f"Error al intentar levantar el script: {e}")
        else:
            st.error(f"El script {script_name} no existe en el directorio.")
    else:
        st.warning("Por favor, ingresa un nombre para el desarrollo.")

for i in range(st.session_state.num_desarrollos):
    st_cols_header = st.columns(3)

    with st_cols_header[0]:
        st.markdown(f"**Desarrollo:** {st.session_state.desarrollos[i]}")

    with st_cols_header[1]:
        estado = "En proceso"
        color = "#32CD32"
        st.markdown(f"<p style='color:{color}; font-weight:bold;'>{estado}</p>", unsafe_allow_html=True)
        st.write("Puerto:", st.session_state.puertos[i])

    with st_cols_header[2]:
        Tirar = st.button(f"Tirar {nombre_input}", key=f"Tirar_{i}", use_container_width=True)
        if Tirar:
            st.write(f"Parando app para Desarrollo {st.session_state.desarrollos[i]}")

import streamlit as st
import subprocess
import sys

from utils.subproceso import ejecutar

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

        st.write(f"Ejecutando app para Desarrollo {nombre_input}")
        subprocess.run([f"{sys.executable}", f"app{st.session_state.num_desarrollos}.py"])
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
        Tirar = st.button(f"Tirar {i + 1}", key=f"Tirar_{i}", use_container_width=True)
        if Tirar:
            st.write(f"Parando app para Desarrollo {st.session_state.desarrollos[i]}")

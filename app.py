import streamlit as st
import subprocess
import sys

from utils.subproceso import ejecutar

st.header("Interfaz de control de desarrollos.")

if "num_desarrollos" not in st.session_state:
    st.session_state.num_desarrollos = 0
    st.session_state.desarrollos = [] 
    st.session_state.puertos = []

if st.button("Agregar"):
    st.session_state.num_desarrollos += 1
    st.session_state.desarrollos.append("")
    st.session_state.puertos.append(None)

for i in range(st.session_state.num_desarrollos):
    st_cols_inputs = st.columns(2)

    with st_cols_inputs[0]:
        st.session_state.desarrollos[i] = st.text_input(
            f"Nombre del Desarrollo {i + 1}",
            value=st.session_state.desarrollos[i],
            key=f"nombre_{i}"
        )

    with st_cols_inputs[1]:
        puerto = st.text_input(
            f"Puerto del Desarrollo {i + 1}",
            value=st.session_state.puertos[i] or f"{8501 + i}",
            key=f"puerto_{i}"
        )
        st.session_state.puertos[i] = int(puerto) if puerto.isdigit() else 8501 + i

for i in range(st.session_state.num_desarrollos):
    st_cols_header = st.columns(3)

    with st_cols_header[0]:
        st.markdown(f"**Desarrollo:** {st.session_state.desarrollos[i]}")

    with st_cols_header[1]:
        estado = "En proceso"
        color = "#32CD32"
        st.markdown(f"<p font-weight:bold;'>{estado}</p>", unsafe_allow_html=True)
        st.write("Puerto:", st.session_state.puertos[i])

    with st_cols_header[2]:
        Levantar = st.button(f"Levantar {i + 1}", key=f"Levantar_{i}", use_container_width=True)
        Tirar = st.button(f"Tirar {i + 1}", key=f"Tirar_{i}", use_container_width=True)

        if Levantar:
            st.write(f"Ejecutando app para Desarrollo {st.session_state.desarrollos[i]}")
            subprocess.run([f"{sys.executable}", f"app{i+1}.py"])

        if Tirar:
            st.write(f"Parando app para Desarrollo {st.session_state.desarrollos[i]}")

import streamlit as st
import streamlit as st
import subprocess
import sys

from utils.subproceso import ejecutar

st.header("Interfaz de control de desarrollos.")

if "num_desarrollos" not in st.session_state:
    st.session_state.num_desarrollos = 0

if st.button("Agregar"):
    st.session_state.num_desarrollos += 1

for i in range(st.session_state.num_desarrollos):
    
    st_cols_header = st.columns(3)

    with st_cols_header[0]:
        st.markdown(f"Desarrollo: {i + 1}")

    port = 8501 + i

    with st_cols_header[1]:
        estado = "Ejecutando"
        color = "#32CD32"
        st.markdown(f"<p style='color:{color}; font-weight:bold;'>{estado}</p>", unsafe_allow_html=True)
        st.write("Puerto:", port)

    with st_cols_header[2]:
        Levantar = st.button(f"Levantar {i + 1}", key=f"Levantar_{i}", use_container_width=True)
        Tirar = st.button(f"Tirar {i + 1}", key=f"Tirar_{i}", use_container_width=True)

        if Levantar:
            st.write(f"Ejecutando app para Desarrollo {i + 1}")
            subprocess.run([f"{sys.executable}", f"app{i+1}.py"])

        if Tirar:
            st.write(f"Parando app para Desarrollo {i + 1}")
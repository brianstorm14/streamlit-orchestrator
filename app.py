import streamlit as st

from utils.nueva_app import add_app
from utils.stop_app import stop_streamlit_app
from utils.revisar_puerto import puerto_disponible

st.header("Interfaz de control de desarrollos.")

if "num_desarrollos" not in st.session_state:
    st.session_state.num_desarrollos = 0
    st.session_state.desarrollos = []
    st.session_state.puertos = []
    st.session_state.config = []

st_cols_inputs = st.columns(2)

nombre_input = st_cols_inputs[0].text_input("Nombre del Desarrollo", "")
puerto_input = st_cols_inputs[1].text_input("Puerto del Desarrollo", "")
config_input = st.text_input("Configuración adicional", "")
PID_FILE = "desarrollos_pids.json"

if st.button("Agregar"):
    if not nombre_input:
        st.warning("Por favor, ingresa un nombre para el desarrollo.")
    elif not puerto_input.isdigit():
        st.warning("Por favor, ingresa un puerto válido (número).")
    elif not puerto_disponible(int(puerto_input)):
        st.warning("El puerto ingresado ya está en uso. Por favor, elige otro.")
    else:
        st.session_state.desarrollos.append(nombre_input)
        st.session_state.puertos.append(int(puerto_input))
        st.session_state.config.append(config_input)
        st.session_state.num_desarrollos += 1

        add_app(nombre_input, puerto_input, config_input, PID_FILE)


for i in range(st.session_state.num_desarrollos):
    st_cols_header = st.columns(3)

    with st_cols_header[0]:
        st.markdown(f"**Desarrollo:** {st.session_state.desarrollos[i]}")

    with st_cols_header[1]:
        estado = "Ejecutando"
        color = "#32CD32"
        st.markdown(f"<p style='color:{color}; font-weight:bold;'>{estado}</p>", unsafe_allow_html=True)
        st.write("Puerto:", st.session_state.puertos[i])

    with st_cols_header[2]:
        Tirar = st.button(f"Tirar {st.session_state.desarrollos[i]}", key=f"Tirar_{i}", use_container_width=True)
        if Tirar:
            st.write(f"Parando el desarrollo {st.session_state.desarrollos[i]}")
            stop_streamlit_app(st.session_state.desarrollos[i], PID_FILE)
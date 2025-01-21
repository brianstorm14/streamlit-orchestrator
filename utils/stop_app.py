import os
import signal
import json
import streamlit as st

def stop_streamlit_app(name, pid_file):
    if not os.path.exists(pid_file):
        st.error("No se encontró el archivo de procesos.")
        return

    try:
        with open(pid_file, "r") as f:
            data = json.load(f)

        if name not in data:
            st.error(f"No se encontró el proceso para {name}.")
            return

        pid = data[name]

        os.killpg(os.getpgid(pid), signal.SIGTERM)
        st.success(f"Proceso {name} detenido con éxito.")

        del data[name]
        with open(pid_file, "w") as f:
            json.dump(data, f)

    except ProcessLookupError:
        st.error("El proceso no está en ejecución.")
    except Exception as e:
        st.error(f"Error al detener el proceso: {e}")

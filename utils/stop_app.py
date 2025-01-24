import os
import signal
import json
import streamlit as st

def stop_app(name, pid_file):
    if not os.path.exists(pid_file):
        st.error("No hay desarrollos activos.")
        return

    try:
        with open(pid_file, "r") as f:
            data = json.load(f)

        if name not in data:
            st.error(f"No se encontró el desarrollo {name}.")
            return

        pid = data[name].get("pid")
        if not isinstance(pid, int):
            st.error(f"PID inválido para {name}.")
            return

        os.killpg(os.getpgid(pid), signal.SIGTERM)
        st.success(f"El desarrollo {name} fue detenido con éxito.")

        del data[name]
        with open(pid_file, "w") as f:
            json.dump(data, f)

    except ProcessLookupError:
        st.error("El desarrollo no está en ejecución.")
    except Exception as e:
        st.error(f"Error al detener el desarrollo: {e}")

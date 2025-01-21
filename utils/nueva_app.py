import os
import subprocess
import json
import streamlit as st

def add_streamlit_app(name, puerto, pid_file):
    script_name = f"{name}.py"
    if os.path.exists(script_name):
        try:
            st.write(f"Ejecutando {name}")
            process = subprocess.Popen(
                ["streamlit", "run", script_name, "--server.port", f"{puerto}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid,
            )

            if os.path.exists(pid_file):
                with open(pid_file, "r") as f:
                    data = json.load(f)
            else:
                data = {}

            data[name] = process.pid

            with open(pid_file, "w") as f:
                json.dump(data, f)

        except Exception as e:
            st.error(f"Error al intentar levantar el script: {e}")
    else:
        st.error(f"El script {script_name} no fue encontrado.")

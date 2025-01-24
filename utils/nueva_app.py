import os
import subprocess
import json
import streamlit as st

from utils.config_input import parsear_config
from utils.config_input import configuracion

def add_app(name, puerto, config, pid_file):
    nombre_script = f"{name}.py"
    if os.path.exists(nombre_script):
        try:
            config_dict = parsear_config(config)

            config_args = []
            for key, value in config_dict.items():
                config_args.extend(configuracion(key, value))
            
            command = ["streamlit", "run", nombre_script, "--server.port", f"{puerto}"] + config_args

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid,
            )

            data = {}
            if os.path.exists(pid_file):
                with open(pid_file, "r") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        st.warning(f"El archivo {pid_file} está vacío o es incorrecto.")
                        data = {}

            data[name] = {"pid": process.pid, "puerto": puerto, **config_dict}

            with open(pid_file, "w") as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            st.error(f"Error al intentar levantar el script: {e}")
    else:
        st.error(f"El script {nombre_script} no fue encontrado.")


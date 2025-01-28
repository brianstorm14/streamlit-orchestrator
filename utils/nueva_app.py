import os
import subprocess
import json
import platform
import streamlit as st

from utils.config_input import parsear_config
from utils.config_input import configuracion

def add_app(name, puerto, config, pid_file):
    ruta_proyecto, nombre_script = os.path.split(name)
    sistema_operativo = platform.system()

    if not os.path.exists(os.path.join(ruta_proyecto, nombre_script)):
        st.error(f"{nombre_script} no fue encontrado en {ruta_proyecto}.")
        return
    
    try:
        
        config_dict = parsear_config(config)
        
        config_args = []

        for key, value in config_dict.items():
            config_args.extend(configuracion(key, value))

        if sistema_operativo == "Windows":
            script_file = f"{nombre_script}.bat"
            script_content = f"""
            @echo off
            cd {ruta_proyecto}
            call venv\\Scripts\\activate
            streamlit run {nombre_script} --server.port {puerto} {' '.join(config_args)}
            """
        else:
            script_file = f"{nombre_script}.sh"
            script_content = f"""
            # bash
            cd {ruta_proyecto}
            source venv/bin/activate
            streamlit run {nombre_script} --server.port {puerto} {' '.join(config_args)}
            """

        with open(script_file, "w") as f:
            f.write(script_content)

        process = subprocess.Popen(
            script_file if sistema_operativo == "Windows" else ["bash", script_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True if sistema_operativo == "Windows" else None,
            preexec_fn=os.setsid if sistema_operativo != "Windows" else None,
        )

        data = {}
        if os.path.exists(pid_file):
            with open(pid_file, "r") as f:
                data = json.load(f)

        data[nombre_script] = {
            "pid": process.pid,
            "puerto": puerto,
            "nombre": nombre_script,
            **config_dict
        }

        with open(pid_file, "w") as f:
            json.dump(data, f, indent=4)

        st.success(f"{nombre_script} iniciado en el puerto {puerto}.")

    except Exception as e:
        st.error(f"Error al intentar levantar el script: {e}")

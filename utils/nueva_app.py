import os
import subprocess
import json
import platform
import streamlit as st

from utils.config_input import parsear_config
from utils.config_input import configuracion

def add_app(name, puerto, config, pid_file, so):
    ruta_proyecto, nombre_script = os.path.split(name)

    config_dict = parsear_config(config)
    
    config_args = []

    for key, value in config_dict.items():
        config_args.extend(configuracion(key, value))

    script_bat = f"{nombre_script}.bat"
    script_content_bat = f"""
    @echo off
    cd {ruta_proyecto}
    call venv\\Scripts\\activate
    streamlit run {nombre_script} --server.port {puerto} {' '.join(config_args)}
    """

    with open(script_bat, "w") as f:
        f.write(script_content_bat)

    script_sh = f"{nombre_script}.sh"
    script_content_sh = f"""
    # bash
    cd {ruta_proyecto}
    source venv/bin/activate
    streamlit run {nombre_script} --server.port {puerto} {' '.join(config_args)}
    """

    with open(script_sh, "w") as f:
        f.write(script_content_sh)

    if so == "Windows":
        process = subprocess.Popen(
            script_bat,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
    else:
        process = subprocess.Popen(
            ["bash", script_sh],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid
        )

    data = {}
    if os.path.exists(pid_file):
        with open(pid_file, "r") as f:
            data = json.load(f)

    data[nombre_script] = {
        "nombre": nombre_script,
        "pid": process.pid,
        "puerto": puerto,
        "status": "Ejecutando",
        **config_dict
    }

    with open(pid_file, "w") as f:
        json.dump(data, f, indent=4)

    st.success(f"Desarrollo {nombre_script} fue iniciado con éxito")
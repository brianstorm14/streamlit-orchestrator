import os
import json
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

    if os.path.exists(pid_file):
        with open(pid_file, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[nombre_script] = {
        "pid": None,
        "puerto": puerto,
        "nombre": nombre_script,
        "ruta": name,
        "status": "Detenido",
        **config_dict
    }

    with open(pid_file, "w") as f:
        json.dump(data, f, indent=4)

    st.success(f"{nombre_script} agregado en el JSON :D")
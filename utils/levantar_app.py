import os
import subprocess

from utils.config_input import configuracion

def levantar_app(info, so):
    ruta_completa = info["ruta_completa"]
    puerto = info["puerto"]
    
    ruta_proyecto, nombre_script = os.path.split(ruta_completa)

    config_dict = {
        k: v 
        for k, v in info.items() if k not in ["ruta_completa", "puerto", "pid", "status", "nombre"]
    }

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
    #!/bin/bash
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

    return process.pid

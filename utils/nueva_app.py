import os
import subprocess
import json
import streamlit as st

from utils.config_input import parsear_config
from utils.config_input import configuracion

def add_app(name, puerto, config, pid_file):
    ruta_proyecto, nombre_script = os.path.split(name)
    script_sh = f"{nombre_script}.sh"

    if os.path.exists(os.path.join(ruta_proyecto, nombre_script)):
        try:
            config_dict = parsear_config(config)

            config_args = []
            for key, value in config_dict.items():
                config_args.extend(configuracion(key, value))
            
            # ruta_entorno = os.path.join(ruta_proyecto, "venv")

            with open(script_sh, "w") as sh_file:
                sh_file.write(f"#!/bin/bash\n")
                sh_file.write(f"cd {ruta_proyecto}\n")
                sh_file.write(f"source venv/bin/activate\n")
                sh_file.write(f"streamlit run {nombre_script} --server.port {puerto} {' '.join(config_args)}\n")
            
            os.chmod(script_sh, 0o775)

            process = subprocess.Popen(
                ["bash", script_sh],
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

            data[nombre_script] = {
                "pid": process.pid,
                "puerto": puerto,
                "nombre": nombre_script,
                "ruta_proyecto": ruta_proyecto,
                "config": config_dict,
            }

            with open(pid_file, "w") as f:
                json.dump(data, f, indent=4)

            st.success(f"El desarrollo {nombre_script} fue levantado con éxito.")
        except Exception as e:
            st.error(f"Error al intentar levantar el script: {e}")
    else:
        st.error(f"El script {nombre_script} no fue encontrado en la ruta especificada.")

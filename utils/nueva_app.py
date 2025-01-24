import os
import subprocess
import json
import streamlit as st

from utils.config_input import parsear_config

def add_app(name, puerto, config, pid_file):
    nombre_script = f"{name}.py"
    if os.path.exists(nombre_script):
        try:
            config_dict = parsear_config(config)

            def configuracion(key, value):
                args = []
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        args.extend(configuracion(f"{key}.{sub_key}", sub_value))
                else:
                    args.append(f"--{key}")
                    args.append(str(value))
                return args

            config_args = []
            for key, value in config_dict.items():
                config_args.extend(configuracion(key, value))
            
            command = ["streamlit", "run", nombre_script, "--server.port", f"{puerto}"] + config_args
            st.write(f"Comando ejecutado: {' '.join(command)}")

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid,
            )

            stdout, stderr = process.communicate()
            st.write(f"STDOUT: {stdout.decode('utf-8')}")
            st.write(f"STDERR: {stderr.decode('utf-8')}")

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


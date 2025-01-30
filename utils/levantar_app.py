import os
import json
import subprocess
import streamlit as st

def levantar_app(name, pid_file, so):
    
    with open(pid_file, "r") as f:
        data = json.load(f)

    desarrollo = data[name]
    script = f"{name}.bat" if so == "Windows" else f"{name}.sh"

    if so == "Windows":
        process = subprocess.Popen(
            script,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
    else:
        process = subprocess.Popen(
            ["bash", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid
        )

    desarrollo["pid"] = process.pid
    desarrollo["status"] = "Ejecutando"

    with open(pid_file, "w") as f:
        json.dump(data, f, indent=4)

    st.success(f"{name} fue levantado :D.")

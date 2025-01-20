import os
import subprocess
import streamlit as st

def add_streamlit_app(name, puerto):
    script_name = f"{name}.py"
    if os.path.exists(script_name):
        try:
            st.write(f"Ejecutando {name}")
            subprocess.Popen(["streamlit","run",script_name,"--server.port",f"{puerto}"])
        except Exception as e:
            st.error(f"Error al intentar levantar el script: {e}")
    else:
        st.error(f"El script {script_name} no existe en el directorio.")
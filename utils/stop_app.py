import os
import signal
import json
import streamlit as st

def stop_app(name, pid_file):
        
        with open(pid_file, "r") as f:
            data = json.load(f)

        pid = data[name].get("pid")

        os.killpg(os.getpgid(pid), signal.SIGTERM)
        st.success(f"El desarrollo {name} fue detenido.")

        data[name]["status"] = "Detenido"
        
        with open(pid_file, "w") as f:
            json.dump(data, f, indent = 4)
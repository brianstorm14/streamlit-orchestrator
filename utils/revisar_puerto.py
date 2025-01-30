import os
import json
import streamlit as st

def puerto_disponible(puerto, PID_FILE):
    if not os.path.exists(PID_FILE):
        return True

    with open(PID_FILE, "r") as f:
        datos_desarrollos = json.load(f)

    for values in datos_desarrollos.values():
        if str(values["puerto"]) == str(puerto):
            return False

    return True
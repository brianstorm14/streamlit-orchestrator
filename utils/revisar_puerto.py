import socket
import streamlit as st

def puerto_disponible(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("0.0.0.0", port))
            return True
    except OSError:
        return False
    except Exception as e:
        st.error(f"Error al verificar el puerto: {e}")
        return False
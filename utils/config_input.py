import streamlit as st

def parsear_config(config_str):
    config_dict = {}
    if config_str.strip():
        try:
            parts = config_str.strip().split("--")
            for part in parts:
                if part:
                    key_value = part.strip().split(" ", 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        keys = key.split(".")
                        current_level = config_dict
                        for k in keys[:-1]:
                            if k not in current_level:
                                current_level[k] = {}
                            current_level = current_level[k]
                        current_level[keys[-1]] = value
        except Exception as e:
            st.error(f"Error al procesar la configuración: {e}")
    return config_dict
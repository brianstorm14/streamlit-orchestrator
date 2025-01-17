import subprocess

def ejecutar():
    subprocess.Popen(["streamlit", "run", "app2.py"], shell=True)
    
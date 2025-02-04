# Orquestador de Streamlit

## Tabla de Contenidos

- [Acerca del Proyecto](#acerca-del-proyecto)
- [Desarrollo del Proyecto](#desarrollo-del-proyecto)
  - [Prerequisitos](#prerequisitos)
  - [Iniciando](#iniciando) 
  - [Instalación](#instalación)   
  - [Ejecución](#ejecución)  
- [Uso del proyecto](#uso-del-proyecto)
- [Contacto](#contacto)
- [Licencia](#licencia)

---

## Acerca del Proyecto

El **Orquestador de Aplicaciones** es una herramienta diseñada para facilitar el despliegue, configuración y administración de múltiples aplicaciones desarrolladas en **Streamlit**. 

Este proyecto busca optimizar el proceso de gestión de aplicaciones al ofrecer una plataforma intuitiva que minimiza la necesidad de tareas técnicas complejas.

### Características principales:
- Añadir aplicaciones especificando su ruta y nombre del proyecto, puerto y configuraciones adicionales.
- Visualizar y gestionar una lista de aplicaciones en ejecución o detenidas mediante una interfaz amigable.
- Iniciar o detener aplicaciones previamente registradas.

La aplicación está desarrollada en **Python** utilizando **Streamlit** para la interfaz web.

---

## Desarrollo del proyecto

### Prerequisitos

 - Python (v. 3.9+)
 - Pandas (v. 1.4.3)
 - Streamlit (v. 1.19)

### Iniciando

Sigue estos pasos para configurar y ejecutar el Orquestador de aplicaciones en Streamlit

1. **Navega al directorio del proyecto:**
   ```bash
   cd ruta/al/proyecto/streamlit.orchestrator
   ```

### Instalación

1. **Crea un entorno virtual de Python**
   ```bash
   python3 -m venv venv
   ```

2. **Accede al entorno virtual:**
   Para Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
   Para Windows:
   ```bash
   source venv\Scripts\activate
   ```

3. **Instala los requisitos:**
     ```bash
   pip install -r requirements.txt
   ```

### Ejecución
1. **Ejecuta la aplicación:**
   ```bash
   streamlit run app.py
   ```
   - La interfaz se desplegará en tu navegador en http://localhost:8501, donde te permitirá usar el orquestador.

---

## Uso del proyecto

1. **Añade un desarrollo:**
   - **Selecciona el Sistema Operativo en uso.**
   - Completa los datos para añadir un desarrollo:
      - **Introduce la ruta y el nombre de la aplicación.** Ejemplo: /ruta/al/proyecto/app.py
      - **Introduce el puerto en el cual desplegarás la aplicación.** *(Nota: El orquestador usa el puerto 8501 por defecto)*
      - **Añade cualquier configuración adicional necesaria (Opcional).** Ejemplo: --theme.base light
      - Haz clic en **Añadir** para agregar la aplicación.

2. **Gestión de Aplicaciones:**
   - **Visualización:** Consulta la lista de aplicaciones agregadas, que muestra el nombre y el puerto de cada una.
   - **Iniciar aplicación:** Haz click en **LEVANTAR** para ejecutar una aplicación que esté en estado **DETENIDO.**
   - **Detener aplicación:** Haz click en **TIRAR** para detener una aplicación que esté en estado **EJECUTANDO.**

---

## Contacto

- Brian De Anda Mariscal - https://github.com/briandeanda
- Project Link - https://github.com/brianstorm14/streamlit-orchestrator.git

---

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).  
Consulta el archivo `LICENSE` para más detalles.
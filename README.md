# project_7
app_web

### Paso 1: Requisitos previos del proyecto

- Creé una cuenta de GitHub e inicialicé un nuevo repositorio con archivos README.md y .gitignore.
- Se instalaron los paquetes necesarios, incluidos pandas, streamlit y plotly-express.
- Creé una cuenta de Render.com y la vinculé a GitHub.
- Instalé y configuré VS Code, configurando el intérprete de Python para que coincida con el entorno virtual.

- ### Paso 2: Adquisición de datos

- Descargué el conjunto de datos de publicidad de automóviles (vehicles_us.csv) y lo colocó en el directorio raíz del proyecto.

### Paso 3: Análisis exploratorio de datos

- Creé un cuaderno Jupyter EDA.ipynb para realizar análisis de datos exploratorios.
- Creé histogramas y diagramas de dispersión usando la biblioteca plotly-express.
- Las visualizaciones se crearon primero en el cuaderno Jupyter y luego se integraron en la aplicación web.

### Paso 4: Desarrollo de aplicaciones web

- Creé un archivo app.py en el directorio raíz del proyecto.
- Módulos necesarios importados como streamlit, pandas y plotly_express.
- Cargué los datos CSV en un DataFrame de pandas.
- Se incorporaron varios componentes optimizados a la aplicación, como encabezados, histogramas, diagramas de dispersión y casillas de verificación.
- Archivo README actualizado para incluir una descripción básica del proyecto e instrucciones para que otros usuarios ejecuten el proyecto en su máquina local.

### Paso 5: Implementación para renderizar

- Se agregó un archivo de configuración optimizado al repositorio de GitHub.
- Creé un nuevo servicio web vinculado al repositorio de GitHub en Render.
- Configuré el servicio web Render para instalar los paquetes necesarios y ejecutar el archivo app.py.
- Implementé la versión final de la aplicación en Render.

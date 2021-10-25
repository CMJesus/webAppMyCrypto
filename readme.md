<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/CMJesus/webAppMyCrypto">
    <img src="appRegistro/static/broker.jpeg" alt="Logo" width="240" height="160">
  </a>

<!-- PROJECT DESCRIPTION -->
<h1 align="center">REGISTRO DE INVERSIONES EN CRYPTOMONEDAS</h1>
  <p align="justify">
    App_Registro - ATH_MY_CRYPTO (el "Proyecto"):
    <br />
    <br />
    El Proyecto trata de una aplicación web, configurada desde una arquitectura "modelo - vista - controlador" (en adelante, la "WebApp").
    <br />
    <br />
    En este contexto, el Proyecto configura una WebApp que consta de tres pantallas de navegación, las que mostrarán; (i) una pantalla de navegación "Inicio", donde tendremos un registro de las transacciones que efectuemos en aras de alcanzar rentabilidad en nuestras inversiones, así como; (ii) una plantilla de navegación "Nuevo", que nos dará paso a un formulario donde podremos realizar nuevas transacciones, y, por último; (iii) una última plantilla de navegación "Status", que procesará la información indicada en el registro indicado en el numeral primero anterior, y finalmente ofrecerá distintas operaciones para cononcer el status de nuestras inversitones.     
  </p>
  <br />
</div>

<!-- TECHNICAL DESCRIPTION -->
## Construida con el siguiente "framework":
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) 

<br />
<br />

# Instrucciones para la instalación de la WebApp (pre-requisitos):

1. Clonar el siguiente repositorio en red local (nuestro pc):
    ```sh
    git clone https://github.com/CMJesus/webAppMyCrypto
    ```

2. Abrir el editor de texto con el que trabajemos ("Visual Studio Code"). Acto seguido,abrir el archivo en el que hayamos alojado el repositorio clonado (en adelante, el "Archivo").

3. Una vez en el Archivo, abriremos una nueva terminal, donde crearemos el entorno virtual para nuestro Archivo. Posteriormente, procederemos a activar dicho entorno virtual:
    - Creación: ```python(3) -m venv venv```
    - Activación (macOs): ```. venv/bin/activate```

3. Instalar Flask en nuestro terminal:
    ```
    pip install flask
    ```

6. Instalar las dependencias del Proyecto con pip:
    ```
    pip install -r requirements.txt
    ```

    Comprobar si las dependencias se han instalado correctamente:
    ```
    pip freeze
    ```

5. Crearemos las siguientes variables de entorno:
    - ```FLASK_APP```
    - ```FLASK_ENV```
    
    Para ello, haremos una copia del archivo ".env_template", renombrándolo a ".env". Una vez duplicado y renombrado, la variable "FLASK_APP" no necesitará ser editada; en cambio, para la variable "FLASK_ENV", habrá que indicar únicamente "development".

6. Configurar la consulta a la API:
    - Renombrar el fichero "config_template.py" a "config.py".
    - Respetar los campos establecidos para RUTA_BASE_DATOS y para URL_CONSULTA.
    - Indicar clave secreta para el campo "SECRET_KEY".
    - Solicitar una "apikey" gratuita en la siguiente dirección:
        * https://www.coinapi.io
    - Una vez hayamos obtenido una "apikey", introducir dicha apikey entre las comillas indicadas para dicho campo. 

7. Base de Datos (librería de python sqlite3).
    - En Archivo, crear una carpeta bajo la rúbrica "data".
    - En data, crear un nuevo archivo formato ".db", denominado "mycrypto.db", tal y como se indica en config_template.py (no renombrado).
    - Una vez creado el archivo mycrypto.db, crear tabla según indicaciones de archivo "initial.sql", alojado en la carpeta "migrations". Ejecutar:
        ```
        .read migrations/initial.sql
        ```
    - En el fichero config.py ya tenemos indicada la ruta base de datos al haber denominado el archivo de la forma indiciada.

<br />

# Instrucciones para la ejecución de la WebApp:
Una vez realizado lo indicado anteriormente, ejecutar en la terminal el siguiente mandato: ```flask run```

<br />

<!-- CONTACT -->
## Contacto:

Nombre: Jesús Capitán Minguet - jcapitanminguet@gmail.com

Link del Proyecto: [https://github.com/CMJesus/webAppMyCrypto](https://github.com/CMJesus/webAppMyCrypto)

<p align="right">(<a href="#top">back to top</a>)</p>
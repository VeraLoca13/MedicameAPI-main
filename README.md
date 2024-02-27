# REST API con Python, Flask y PostgreSQL

REST API con Python, Flask y PostgreSQL. Usaremos el protocolo HTTP junto con los métodos GET, POST, PUT y DELETE y el formato JSON para enviar y recibir datos; además, aprende a probarla utilizando un cliente REST como Insomnia.

<hr/>

Primero, crear un entorno virtual:
### `python -m virtualenv env`

Para instalar los paquetes necesarios:
### `pip install -r requirements.txt`

Crear un archivo .env (en la raíz del proyecto) para las variables de entorno:

### `SECRET_KEY=SECRET_KEY`
### `PGSQL_HOST=host`
### `PGSQL_USER=user`
### `PGSQL_PASSWORD=password`
### `PGSQL_DB=database`

Descarga de PostgreSQL: https://www.postgresql.org/download/
Si quereis probarlo con docker, dejo en la raiz el docker-compose.yaml
Para ejecutarlo desde el terminal ejecutar
### `docker-compose up -d`
<br/>
Descarga de Insomnia: https://insomnia.rest/download
<br/>
o
<br/>
Postman para probar el API :https://www.postman.com/downloads/
<br/>
<br/>
En el fichero sql está la copia de la base de datos para el ejemplo
<br/>
<br/>
para ejecutar la aplicacion desde la carpeta raiz del proyecto
python src/app.py
<hr/>


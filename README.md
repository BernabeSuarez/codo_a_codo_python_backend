# Trabajo final Fullstack Python

# Aplicación de Gestión de Películas con Flask

Esta es una aplicación web simple para la gestión de películas, desarrollada con Flask y MySQL. La aplicación permite a los usuarios registrarse, iniciar sesión y gestionar (crear, leer, actualizar y eliminar) información sobre películas.

## Características

- **Autenticación de usuarios**: Registro, inicio de sesión y cierre de sesión.
- **Gestión de películas**: Agregar, listar, actualizar y eliminar películas.
- **Protección de rutas**: Las rutas para gestionar películas están protegidas y solo accesibles para usuarios autenticados.

## Tecnologías Utilizadas

- **Backend**: Python, Flask
- **Base de Datos**: MySQL
- **Frontend**: HTML, Jinja2, Bootstrap 5
- **Manejo de variables de entorno**: Python-dotenv

## Requisitos

- Python 3.x
- MySQL
- Pip (para instalar dependencias de Python)

## Instalación y Configuración

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno. Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes líneas:

   ```plaintext
   MYSQL_HOST=tu_host
   MYSQL_USER=tu_usuario
   MYSQL_PASSWORD=tu_contraseña
   MYSQL_DB=tu_base_de_datos
   CAC_PYTHON_KEY=una_llave_secreta
   ```

5. Crea la base de datos y las tablas necesarias. Puedes usar el siguiente script SQL como referencia:

   ```sql
   CREATE DATABASE tu_base_de_datos;
   USE tu_base_de_datos;

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       email VARCHAR(100) NOT NULL UNIQUE,
       password VARCHAR(100) NOT NULL
   );

   CREATE TABLE peliculas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       titulo VARCHAR(255) NOT NULL,
       anio INT NOT NULL,
       descripcion TEXT NOT NULL,
       portada VARCHAR(255) NOT NULL,
       categoria VARCHAR(100) NOT NULL
   );
   ```

## Ejecución de la Aplicación

1. Asegúrate de que el entorno virtual esté activado y las dependencias instaladas.
2. Ejecuta la aplicación:

   ```bash
   flask run
   ```

3. Abre tu navegador y ve a `http://127.0.0.1:5000/` para ver la aplicación en funcionamiento.

## Uso

- **Página principal**: Lista de películas (requiere inicio de sesión).
- **Registro**: `http://127.0.0.1:5000/register`
- **Inicio de sesión**: `http://127.0.0.1:5000/login`
- **Agregar película**: `http://127.0.0.1:5000/agregar` (requiere inicio de sesión)
- **Ver películas**: `http://127.0.0.1:5000/peliculas` (requiere inicio de sesión)
- **Ver detalle de película**: `http://127.0.0.1:5000/peliculas/<id>` (requiere inicio de sesión)
- **Eliminar película**: `http://127.0.0.1:5000/peliculas/<id>/delete` (requiere inicio de sesión)
- **Actualizar película**: `http://127.0.0.1:5000/peliculas/<id>/update` (requiere inicio de sesión)

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

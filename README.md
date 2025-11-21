# Sistema de Registro y Login en Python

Proyecto simple creado para demostrar un sistema básico de autenticación con conexión a PostgreSQL.

## 🚀 Funcionalidades
- Registro de usuarios
- Inicio de sesión con validación de credenciales
- Contraseñas cifradas con SHA-256
- Creación automática de la tabla `users` si no existe

## 🛠 Tecnologías utilizadas
- **Python 3**
- **PostgreSQL**
- **psycopg2**
- **VS Code**

## 📂 Estructura del proyecto
login-project/
│── db.py # Conexión a PostgreSQL y creación de tabla
│── auth.py # Registro y autenticación
│── main.py # Menú principal
│── README.md


## 📦 Instalación de dependencias

Asegúrate de tener instalado:

- Python 3
- PostgreSQL
- pip

Luego instala `psycopg2`:


## 🗄 Configuración de la base de datos

En PostgreSQL:

```sql
CREATE DATABASE login_system;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

Edita el archivo db.py y coloca tu contraseña:
password="TU_CONTRASEÑA"

Cómo ejecutar el programa
En la terminal, dentro de la carpeta del proyecto:
python main.py

Verás un menú:

1. Registrar usuario
2. Iniciar sesión
3. Salir

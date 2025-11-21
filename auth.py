from db import get_connection
import hashlib

def hash_password(password):
    """
    Convierte la contraseña a un hash SHA-256.
    Esto protege la contraseña: no se guarda en texto plano.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        hashed = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed)
        )
        conn.commit()
        print("\nUsuario registrado correctamente.\n")
    except Exception as e:
        print("\nError: el usuario ya existe o hubo un problema.\n")
    finally:
        cursor.close()
        conn.close()

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)
    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, hashed)
    )
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        print("\nInicio de sesión exitoso.\n")
        return True
    else:
        print("\nCredenciales incorrectas.\n")
        return False

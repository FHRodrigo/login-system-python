import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="login_system",
        user="postgres",
        password="admin123"  # <-- reemplaza esto con tu contraseña real
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

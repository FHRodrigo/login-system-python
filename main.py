from db import create_table
from auth import register_user, login

def main():
    # Crear tabla automáticamente si no existe
    create_table()

    while True:
        print("=== SISTEMA DE LOGIN ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            register_user(username, password)

        elif option == "2":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            login(username, password)

        elif option == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()

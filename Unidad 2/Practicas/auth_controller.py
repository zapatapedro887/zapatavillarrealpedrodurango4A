# auth_controller.py

from database import crear_conexion
from mysql.connector import Error

def validar_credenciales(usuario, password):
    
    conexion = crear_conexion()
    
    if not conexion:
        # No se pudo conectar a la base de datos
        return None 

    resultado = None
    try:
        # 1. Crea un cursor para ejecutar comandos SQL
        cursor = conexion.cursor() 
        
        # 2. La consulta SQL: Busca en la tabla 'usuario' la fila que coincide con el usuario y password
        consulta = "SELECT * FROM usuario WHERE usuario = %s AND password = %s"
        
        # 3. Ejecuta la consulta, pasando los valores de usuario y password de forma segura
        cursor.execute(consulta, (usuario, password))
        
        # 4. Obtiene la primera fila que coincide (el usuario)
        resultado = cursor.fetchone()
        
    except Error as e:
        # Manejo de errores de SQL
        print(f"Error al ejecutar la consulta SQL: {e}")
        resultado = None
        
    finally:
        # 5. Cierra la conexión SIEMPRE
        if conexion and conexion.is_connected():
            conexion.close()
            
    # 6. Devuelve: La fila del usuario (si lo encontró) o None (si no lo encontró)
    return resultado
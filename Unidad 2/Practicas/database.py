import mysql.connector 
from mysql.connector import Error 

def crear_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "poo_project_p2" 
        )
        
        if conexion.is_connected():
            print('Conexión MYSQL exitosa')
            
    except Error as e:
        print(f"Error al conectar el tipo de: {e}") 
        
    return conexion

# Ejemplo de cómo usar la función:
# if __name__ == '__main__':
#     db_conn = crear_conexion()
#     if db_conn:
#         db_conn.close()
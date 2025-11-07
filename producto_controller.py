
from database import crear_conexion

def ver_productos():
    conexion = crear_conexion()
    if not conexion:
        return []
    cursor = conexion.cursor()
    cursor.execute("SELECT id, usuario FROM producto")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

def agregar_productos(username, password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre_usuario, descripcion, stock, precio, status, marca, proveedor) VALUES (%s, %s)", (username, password))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear un productos. Tipo de error {e}")
        return False

def actualizar_productos(id_usuario, new_usuario, new_password):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET usuario = %s, password = %s WHERE id = %s", (new_usuario, new_password, id_usuario))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar usuario. Tipo de error: {e}")
        return False

def eliminar_productos(id_usuario):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar usuario. Tipo de error: {e}")
        return False
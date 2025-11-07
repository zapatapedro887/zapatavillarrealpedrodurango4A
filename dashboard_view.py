import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, root, username):
        self.username = username
        self.root = root # CORRECTO: Usa el root pasado desde el login
        
        # Configuración de la ventana principal
        self.root.title(f"Bienvenido {self.username}")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        self.crear_elementos() 
        
        # ¡LÍNEA ELIMINADA! El mainloop lo maneja el login_view.py después de la transición.
        # self.root.mainloop() 

    def crear_elementos(self):
        tk.Label(self.root, text = f"Hola {self.username}", font=("Arial", 22, "bold")).pack(pady=10)
        tk.Button(self.root, text="Ver Usuarios", width=20, command=self.ver_usuarios).pack(pady=20)
        tk.Button(self.root, text="Agregar Usuarios", width=20, command=self.agregar_usuarios).pack(pady=20)
        tk.Button(self.root, text="Actualizar Usuarios", width=20, command=self.actualizar_usuarios).pack(pady=20)
        tk.Button(self.root, text="Eliminar Usuarios", width=20 , command=self.eliminar_usuarios).pack(pady=20)
        tk.Button(self.root, text="Cerrar Sesión", width=50 , command=self.cerrar_sesion).pack(pady=20)

    
    def ver_usuarios(self):
        messagebox.showinfo("Acción", "Función: Ver Usuarios")

    def agregar_usuarios(self):
        messagebox.showinfo("Acción", "Función: Agregar Usuarios")
        
    def actualizar_usuarios(self):
        messagebox.showinfo("Acción", "Función: Actualizar Usuarios")
        
    def eliminar_usuarios(self):
        messagebox.showinfo("Acción", "Función: Eliminar Usuarios")
        
    def cerrar_sesion(self):
        # Esta función debe cerrar la ventana y luego terminar el mainloop que la inició
        self.root.destroy()
        messagebox.showinfo("Sesión", "Has cerrado la sesión.")

# El bloque de prueba es correcto si quieres probar el dashboard directamente
if __name__ == "__main__":
    root_test = tk.Tk()
    App = DashboardApp(root_test, "usuario")
    root_test.mainloop() # El mainloop debe estar fuera de la clase para las pruebas
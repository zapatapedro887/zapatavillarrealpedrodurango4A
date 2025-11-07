"""
import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales 
from user_view import UserApp

class LoginApp:
    def __init__(self, root):
        self.root = root;
        self.root.title("Inicio de sesión")
        self.root.geometry("600x400")
        self.root.resizable(True, True)


        #Encabezado
        tk.Label(root, text="Bienvenido al sistema", font=("Arial", 16, "bold")).pack(pady=16)

        # Campos de texto
        tk.Label(root, text="Ingresa tu nombre de usuario:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Ingresa tu contraseña:").pack()
        self.password_entry = tk.Entry(root)
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Iniciar sesión", command=self.login).pack(pady=20)
        

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showinfo("Faltan datos. Favor de ingresar usuario y contraseña")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            self.root.destroy()
            App = UserApp(usuario)
        else:
            messagebox.showerror("Acceso denegado", "Tus datos son incorrectos, no se pudo ingresar.")



"""

import tkinter as tk
from tkinter import messagebox
from dashboard_view import DashboardApp 
from auth_controller import validar_credenciales # Esta importación es ignorada en la validación

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        self.root.configure(bg="white")
        
        # Llama al método para crear todos los widgets
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="Bienvenido al sistema", font=("arial", 16, "bold")).pack(pady=16)
        tk.Label(self.root, text="Ingresa tu nombre de usuario: ").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        
        # 🔑 Punto clave: Oculta la contraseña
        tk.Label(self.root, text="Ingresa tu contraseña: ").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Button(self.root, text="Iniciar Sesión", command=self.login).pack(pady=20)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showinfo("Faltan Datos", "Favor de ingresar usuario y contraseña.")
            return

        # 🛑 Validación de credenciales codificadas
        if usuario == "usuario123" and password == "1234":
            messagebox.showinfo("Acceso Permitido", f"Bienvenido {usuario}")
            self.root.destroy()
            
            # Nota: Usas una variable 'username' que no está definida aquí, 
            # debería ser 'usuario' si sigues la lógica de tu código.
            dashboard_root = tk.Tk() 
            DashboardApp(dashboard_root, usuario) 
            
            # Mantiene el Dashboard abierto y funcionando
            dashboard_root.mainloop() 
        else:
            messagebox.showerror("Acceso Denegado", "Tus datos son incorrectos.")


if __name__ == '__main__':
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
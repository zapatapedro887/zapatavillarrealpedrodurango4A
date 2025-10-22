import tkinter as tk
from tkinter import messagebox
from dashboard_view import DashboardApp 
from auth_controller import validar_credenciales

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

        if usuario == "usuario123" and password == "1234":
            messagebox.showinfo("Acceso Permitido", f"Bienvenido {usuario}")
            self.root.destroy()
            dashboard_root = tk.Tk() 
            
            # Mantiene el Dashboard abierto y funcionando
            dashboard_root.mainloop() 
        else:
            messagebox.showerror("Acceso Denegado", "Tus datos son incorrectos.")


if __name__ == '__main__':
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
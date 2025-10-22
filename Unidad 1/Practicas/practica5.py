#practica5 sigleton
#ejemplo de patron de diseño singleton-sistema de registro de logs

class logger:
    #atributo para guardar la unica instancia 
    _instancia = None
#metodo new controla el objeto antes del init se segura que solo exista una unica instancia de loger 
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            #abrimos un archivos de logs en modo "append"
            cls._instancia.archivo = open ("app.log", "a")
        #devuelve siempre a la misma instancia
        return cls._instancia 
    
    def registro(self, mensaje):
        self.archivo.write(mensaje)
        self.archivo.flush() #forza al archivo para guardarse en el codigo

registro1= logger() #creamos la unica instancia singleton 
registro2 = logger() #devuelve la misma instancia sin crear la nueva 

registro1.registro("inicio de sesion en la aplicacion")
registro2.registro("el usuario se autentico")

print(registro1 is registro2) #True o False
#si me regresa True: es el mismo objeto en memoria
 

class tiket:
    def __init__(self,id,tipo,prioridad):
        self.id=id
        self.tipo=tipo
        self.prioridad=prioridad
        self.estado = "pendiente"

class empleado:
    def __init__(self,nombre):
        self.nombre = nombre
    def trabajar_en_tiket(self, tiket):
        print(f"el empleado {self.nombre} revisa el tiket {tiket.id}")

class desarrollador(empleado):
    def trabajar_en_tiket(self, tiket):
        if tiket.tipo == "sofware":
            tiket.estado = "resuelto"
            print (f"el tiket {tiket.id} fue resuelto por {self.nombre}")
        else:
            print("este tiket no se puede hacer por el usuario")

class tester ( empleado):
    def trabajar_en_tiket(self, tiket):
        if tiket.tipo == "prueba":
            tiket.estado = "resuelto"
            print (f"el tiket {tiket.id } fue resuelto por {self.nombre}")
        else:
            print("este tiket no se puede resolver por este usuario")

class projectmanager(empleado):
    def asignar_tiket(self, tiket, empleado):
        print (f" {self.nombre} asigno el tiket {tiket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_tiket(tiket)


tiket1 = tiket (1,"sofware", "alta")
tiket2 = tiket (2, "prueba", "baja")

developer1 = desarrollador("carlos")
tester1 = tester ("juanillo")
pm =projectmanager("manuelita")

pm.asignar_tiket(tiket1, developer1)

# agregar un menu interactivo con while y con if para:
# crear tiket
# ver los tiket
# asignar un tiket
# salir del programa


#Practica 2 clases emtodos y atributos

class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__cuenta = None  #atributo privado
    
    def consultar_saldo(self):
        if self.__cuenta:
            print(f"el saldo de {self.nombre} es {self.__cuenta.mostrar_saldo()} ")
        else:
            print(f"{self.nombre} no tiene una cuenta creada")

    def asignar_cuenta(self,cuenta):
        self.__cuenta = cuenta 
        print(f"{self.nombre} ahora tiene una cuenta bancaria ")

    def presentarse(self):
        print(f"hola, mi nombre es {self.nombre} mi apellido es {self.apellido} y mi edad es {self.edad}")

    def cumplir_anios(self):
        self.edad += 1
        print (f"esa persona cumplio {self.edad} anios")


estudiante1 = Persona("miguel", "luna", 19)

estudiante2 =Persona("edgar", "alfredo", 19)

estudiante1.presentarse()
estudiante2.presentarse()

#CUENTA BANCARIA

class cuenta_bancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo 

    def mostrar_saldo(self):
        return self.__saldo
    
    def depositar(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"se deposito la cantidad de {cantidad}")
        else:
            print("ingresa una cantidad valida")

    def retirar(self, cantidad):
        if  0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"se retiro la cantidad de {self.cantidad} nuevo saldo: {self.__saldo}")
        else:
            print("saldo insuficiente")

cuenta1 = cuenta_bancaria("001", 500)

estudiante1.asignar_cuenta(cuenta1)
estudiante1.consultar_saldo()

#EJERCICIO 1
#crear un objeto distinto una clase, objeto 
#minimo 3 atributos y 3 metodos

class robot:
    def __init__(self,altura,color,edad):
        self.altura = altura
        self.color = color
        self.edad = edad

    def presentarse(self):
        print(f"hola, mido {self.altura} mi color es {self.color} y mi edad es {self.edad}")

    def cumplir_anios(self):
        self.edad += 1
        print (f"ese robot tiene {self.edad} anios de edad")

robot1 = robot("200cm", "cafe", 5)

robot2 = robot("10cm", "plata", 2)

robot1.presentarse()
robot2.presentarse()

class robot:
    def __init__(self,barrer,objetos,cocinar):
        self.barrer = barrer
        self.objetos = objetos
        self.cocinar = cocinar

    def barre(self):
        print(f"el robot agarra {self.barrer} y barre")
    
    def objeto(self):
        print(f"el robot dice la tabla del 1 {self.objetos}")

    def cocina(self):
        print(f"el robot agarra {self.cocinar} y lo coina")

robot3 = robot("escoba", "1x1 = 1", "huevos")

robot3.barre()
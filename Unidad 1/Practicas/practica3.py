class pago_tarjeta:
    def procesar_pago(self, cantidad):
        input("ingresa tu nombre: ")
        return f"procesando pago de {cantidad} con tarjeta "
    
class paypal:
    def procesar_pago(self,cantidad):
        return f"procesando pago de {cantidad} con paypal"

class cheque:
    def procesar_pago(self,cantidad):
        return f"procesando pago de {cantidad} con cheque"
    
class efectivo:
    def procesar_pago(self,cantidad):
        return f"procesando pago de {cantidad} con efectivo"
    
class deposito:
    def procesar_pago(self,cantidad):
        return f"procesando pago de {cantidad} con deposito mas {+20} pesos por comision"

metodos_pago = [pago_tarjeta(), paypal(), cheque(), efectivo()]

for m in metodos_pago:
    print(m.procesar_pago(500))

#procesar diferentes canitdades en cada opcion de pago 
#100 con tarjeta, 400 con paypal, 600 con deposito y 5000 con cheque
    
pago1= pago_tarjeta()
pago2= paypal()
pago3= cheque()
pago4 = efectivo()
pago5 = deposito()

print(pago1.procesar_pago(100))
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(600))
print(pago4.procesar_pago(5000))
print(pago5.procesar_pago(5000))



productos = ["computadora", "telefono", "tablet"]
precios = [1000, 700, 500]

def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

print("Bienvenido a CafeInt")
nombre = input("Ingresa tu nombre: ")

cantidades = []
print("Selecciona tu pedido:")

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} quieres? "))
    cantidades.append(cantidad)

total = calcular_total(cantidades, precios)

print("\n----- TICKET DE COMPRA -----")
print(f"Cliente: {nombre}")
for i in range(len(productos)):
    if cantidades[i] > 0:
        subtotal = cantidades[i] * precios[i]
        print(f"{cantidades[i]} x {productos[i]} - ${subtotal}")
print("-----------------------------")
print(f"TOTAL: ${total}")
print("-----------------------------")

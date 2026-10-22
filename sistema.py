from utils import calcular_subtotal
from utils import aplicar_descuento
listatot = []
for i in range(3):
    precio = int(input(f'Ingrese el precio del producto {i + 1}: '))
    cant = int(input(f'Ingrese la cantidad del producto {i + 1}: '))
    calcular_subtotal(precio, cant)
    subtotal = calcular_subtotal(precio, cant)
    aplicar_descuento(subtotal)
    total = aplicar_descuento(subtotal)
    listatot.append(total)
for n in listatot:
    print(n)

    
def calcular_subtotal(precio, cant):
    subtotal = precio * cant
    return subtotal
def aplicar_descuento(subtotal):
    if subtotal >= 20000:
        total = subtotal - subtotal * 0.1
        return total
    else:
        total = subtotal
        return total
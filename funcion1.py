# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto
# y devuelva el valor del producto con un aumento del 5%.
# Realizar la llamada desde el main.

def aplicarAumento(precio:int):
    aumento = precio + precio * 0.05
    print(aumento)


aplicarAumento(100)

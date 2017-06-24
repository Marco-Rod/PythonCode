"""
Dado un valor entero cualquiera
se debe generar una lista
la cual debe tener una salida similar
a:
Ejemplo: valor ingresado 5 salida 24531
"""

x = 5
lista = [item for item in range(1, x+1) if item % 2 == 0]+[item for item in range(1, x+1) if item % 2 != 0][::-1]
final = ''.join(str(l) for l in lista)
print(final)

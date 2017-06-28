#Ejercicio 1
#Escribir una función [cuadrados] que recibiendo una secuencia
#de numeros, devuelve la lista de los cuadrados de esos
#numeros, en el mismo orden.
#Ejemplo: cuadrados([4,1,5.2,3,8])
#[16, 1, 27.04000000000003, 9 64]
#Hacer dos versiones: Una usando un bucle explicito, y la otra
#mediante definición de listas por complensión.

def cuadrados(lista):
    """ Recibe una secuencia de numeros que
    devuelve una lista de los cuadrados
    de estos numero en el mismo orden.
    """
    lista_final = [valor**2 for valor in lista]
    return lista_final

r = cuadrados([4, 1, 5.2, 3, 8])
print(r)

def cuadrados_dos(lista):
    """ Recibe una secuencia de numeros que
    devuelve una lista de los cuadrados
    de estos numero en el mismo orden.
    """
    nueva_lista = []
    for l in lista:
        cuadrado = l**2
        nueva_lista.append(cuadrado)
    return nueva_lista

re = cuadrados_dos([4, 1, 5.2, 3, 8])
print(re)
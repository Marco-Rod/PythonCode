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
    de estos numeros en el mismo orden.
    """
    lista_final = [valor**2 for valor in lista]
    return lista_final

#r = cuadrados([4, 1, 5.2, 3, 8])
#print(r)

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

#re = cuadrados_dos([4, 1, 5.2, 3, 8])
#print(re)


#Ejercicio 2
#Definir una función [vocales_consonantes],
#que reciba una cadena de caracteres (en mayuscula)
#y escribe por pantalla, una a una, si sus letras
#son vocales o consonantes.
#Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# ...

def vocales_consonantes(palabra):
    """
    Retorna un listado indicando
    si es consonante o vocal cada una
    de las letras que contiene la palabra
    que recibe como argumento. (palbra)
    """
    resultado = [print(letra, " Es vocal") if letra in ('A', 'E', 'I', 'O', 'U')\
    else print(letra, " Es consonante") for letra in palabra]
    return resultado

#vocales_consonantes('INTELIGENCIA')


#Ejercicio 3
#Usando como tecnica principal
#la definición de secuencias por comprensión
#definir las siguientes funciones:

#a) Dada una lista de numeros naturales, la suma
#de los cuadrados de los numeros pares de la lista.
#Ejemplo:
#>>> suma_cuadrados([9,4,2,6,8,1])
#120
def suma_cuadrados(lista):
    """
    Retorna el total de los cuadrados
    de los numeros pares de una lista.
    """
    r = [valor**2 for valor in lista if valor % 2 == 0]
    resultado = sum(r)
    return resultado

# resultado = suma_cuadrados([9, 4, 2, 6, 8, 1])
# print(resultado)

#b) Dada una lista de numeros l=[a(1),.....a(n)], calcular
#el sumatorio de i=1 hasta n de i*a(i).
#Ejemplo:
#>>> suma_formula([2,4,6,8,10])
#110

#c) Dados dos listas numericas de la misma longitud,
#representando dos puntos n-dimensionales, calcular
#la distancia euclidea entre ellos.

#Ejemplo:
#>>> distancia([3,1,2],[1,2,1])
#2.449489742783178

#d) Dada una lista y una función de un argumento, devolver
#la lista de los resultados de aplicar la funcion a cada
#elemento de la lista.

#Ejemplo:
#>>> map_mio(abs,[-2, -3, -4, -1])
#[2, 3, 4, 1]

#e) Dada un par de listas (de la misma longitud) y una función
#de dos argumentos, devolver la lista de los resultados de aplicar
#la funcion a cada par de elementos que ocupan la misma posición
#en las listas de entrada.

#Ejemplo:

#>>> map2_mio((lambda x, y: x+y), [1,2,3,4],[5,2,7,9])
#>>> [6, 4, 10, 13]

#f) Dada una lista de numeros contar el numero de elementos
#que sean multiplos de tres y distintos de cero.

#Ejemplo:
#>>> m3_no_nulos([4,0,6,7,0,9,18])
#3

#g) Dadas dos listas de la misma longitud, contar en numero
# de posiciones en las que coinciden los elementos de ambas listas

#Ejemplo:
#>>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
#3

#h) Dadas dos listas de la misma longitud, devolver un diccionario
#que tiene como claves las posiciones en las que coinciden los elementos
#de ambas listas, y como valor de esas claves, el elemento coincidente.

#Ejemplos:
#>>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
#{1: 2, 3: 8, 4: 9}
#>>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
#{1: 8, 2: 1, 3: 2, 4: 1}



#Hacer un programa que le pida una cadena al usuario y la imprimia al revés.
def invertir_palabra(palabra):
    """
    Retorna una palabra al revés
    """
    return palabra[::-1]

#resultado = invertir_palabra("Esto es así")
#print(resultado)

#Hacer un programa que le pida al usuario y muestre ese numero menos dos, mas dos, multiplicado por dos
#dividico por dos, dividido por dos en forma entera y elevado a la potencia de dos.
#Ejemplo: 7 : 5, 9, 14, 3, 3.5, 49

def operaciones_numero(numero):
    digito = 2
    resta = numero - 2
    suma = numero + 2
    mult = numero * 2
    div = numero / 2
    div2 = numero // 2
    pot = numero ** 2
    resultado = [resta, suma, mult, div, div2, pot]
    return resultado

#resultado = operaciones_numero(7)
#print(resultado)

#Pedirle un numero al usuario, elevarlo al cuadrado y mostrar los digitos al reves y separados
#por espacio. por ejemplo: si el usuario ingresa 17, la salida tiene que ser: 9 8 2.

def numero_elevado(numero):
    proceso = numero ** 2
    proceso = str(proceso)
    valor = proceso[::-1]
    resultado = valor.replace(""," ")
    return resultado

# resultado = numero_elevado(17)
# print(resultado)

def figuras_geometricas(base, altura, radio):
    base = base * 2
    altura = altura * 2
    perimetro = base + altura
    area = base * altura
    perimetro_cir = 2 * 3.14 * radio
    area_cir = 3.14 * radio * 2
    return (perimetro_cir, area_cir, area)

# resultado = figuras_geometricas(2, 4, 2)
# print(resultado)


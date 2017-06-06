#! /usr/bin/python

#USANDO LISTAS COMO PILAS
#Declaramos la primera lista vacia
list_one = []

#Con el metodo append insertamos elementos en la lista
list_one.append("A")
list_one.append("E")
list_one.append("I")
list_one.append("O")
list_one.append("U")
print(list_one)

#Declaramos una segunda lista
list_two = []
#Insertamos elementos en la segunda lista
list_two.append("a")
list_two.append("e")
list_two.append("i")
list_two.append("o")
list_two.append("u")
print(list_two)

""""Con el metodo extend insertamos en la segunda lista
todos los elementos que la primera lista contiene"""
list_two.extend(list_one)
print(list_two)

#Con el metodo insert agregamos elementos en una posicion especifica de la lista
list_two.insert(0, "Minusculas")
list_two.insert(6, "Mayusculas")
print(list_two)

#Con el metodo remove se elimina el primer elemento encontrado de acuerdo al parametro
#list_two.remove("a")
#print(list_two)

#Con el metodo remove se elimina el elemento que se encuentra en la posicion indicada NOTA: Si no se especifica la posicion se elimina el ultimo valor de la lista
list_two.pop(6)
print(list_two)

#Con el metodo clear se limpian todos los valores que contiene la lista
# list_two.clear()
# print(list_two)

#Devuelve el lemento dado, y opcionalmete se puede delimitar la busqueda por posiciones
print(list_two.index("A",0,7))

#Devuelve el numero de veces que el valor dado se encuentra en la lista
print(list_two.count("A"))

#Invierte los valores de una lista in situ
list_two.sort()
print(list_two)

#Invierte los valores de la lista
list_two.reverse()
print(list_two)

#Devuelve una copia superficial de la lista
list_two.copy()
print(list_two)

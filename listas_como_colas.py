#! /usr/bin/python

#LISTAS COMO COLAS

from collections import deque

list_one = deque(["A","E","I","O","U"])
list_one.append("a")
list_one.append("e")

#Elimia el primer valor insertado
list_one.popleft()

print(list_one)

list_one.popleft()

print(list_one)

#Imprimiendo valores eliminados
print ("Desde la derecha:")
d = deque("ABCDEFG")
while True:
    try:
        print(d.pop())#Elimina los valores en la lista desde el ultimo insertaddo
    except Exception:
        break

print("Desde la izquierda:")
d = deque("ABCDEFG")
while True:
    try:
        print(d.popleft())#Elimina los valores en la lista desde la izquierda(primera valor insertado)
    except Exception:
        break

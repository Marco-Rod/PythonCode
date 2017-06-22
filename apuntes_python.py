#Apuntes Python
""" Información y conceptos sobre python
Funcion = "Hace cosas, produce un resultado, ejecuta una acción en concreta"
Metodo = "Un metodo se define de manera simple como:\n
Las cosas que podemos hacer con un objeto.\n Un metodo es una funcion"
Notacion_de_punto = "En python todo es considerado un objeto,
por lo tanto la manera de acceder a sus atributos y metodos es por medio de un punto \n
al contener estos metodos y atributos tambien se puede seguir asi sucesivamente de manera infinita."
Nota = "Todo atributo/método es a su vez un nuevo objeto
que cuenta con sus propios atrubutos/métodos."
"""
string = "hola, mundo."

"""Primer Metodo para las Strings
str.capitalize()
Este metodo nos devuelve la misma string
pero con el primer caracter de la cadena,
el correspondiente al indice 0, str[0], en mayusculas.
"""
string.capitalize()
"""
Segundo Metodo para las Strings
str.Center(ancho, caracter de relleno)
Este metodo nos permite centrar una string entre un caracter (solo uno) que asignemos,
a la izquierda y derecha de nuestra cadena, el primer argumento de la cadena es el largo
total de la cadena
y segundo el caracter que seleecionemos para rellenar la string a ambos lados
"""
string.center(5,'$')

"""
Nota2: por norma general, siempre podemos introducir cualquier método como argumento
en una función print().
"""

"""
Tercer Metodo para las Strings
str.count(sub, indice de inicio, indice final)
Este metodo cuenta el numero de veces que un caracter se encuentra dentro de una cadena
dependiendo el indice especificado. Estos argumentos son separados por comas.
"""
string.count("o", 0, 12)
string.count("ho", 0, 12) #se pueden coloca un substring con dos caracteres literales.
string.count("h", -1, -8) #no cuenta de atras hacia adelante.
string.count("h", -8, -1) #pero de adelante hacia atrás con negativos si.
string.count("h", 0, 1000) #no importa que exceda el indice final el largo de la string.


"""
Cuarto Metodo para las strings
str.endswith(sufijo,indice de inicio, indice final)
Este metodo trabaja con booleanos. devuelve True si nuestra string acaba con el sufijo
que le hayamos pasado previamente como argumento. se pueden utilizar indices de inicio
y final para acortar la busqueda del interprete en un pedazo en concreto (optativo).
"""
string.endswith("mundo", 0, 11)

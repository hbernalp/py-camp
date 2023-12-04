#!/usr/bin/python3

tipo1 = 100             #int - Entero - numero
tipo2 = 34325.256       # float - dooble - decimal
tipo3 = "hola mundo"    #str - string - cadena
tipo4 = True            #bool - booleano
tipo5 = (1,2,3,4,5,6)   #tuple - Tupla  'en la tupla no se pueden moificar los valores en ninguin lugar es como una CONSTANTE'
tipo6 = [1,2,3,4,5,6]   #list - lista - Array - vector   'Aqui se pueden cambiar los datos del Arreglo en cualquier moemnto'
tipo7 = {               #dict - Diccionario - Objeto - Mapa
    "key1": "hola",
    "key2": "hola2"
}

print (type(tipo6))

#Reasignado un valor en la lista
tipo6[2] = 50
print(tipo6)
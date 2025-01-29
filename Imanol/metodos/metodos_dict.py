diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs" : 100000
}

#nos devuelve un objeto  dict_item
claves = diccionario.keys()
 
#GET sirve para que no te salga error sino mas bien NONE, pero el programa continua 
valor = diccionario.get ("sdf")

#elimando todo del diccionario 
#diccionario.clear()

#elimando un elemento del diccionario 
diccionario.pop("subs") #lo borra

print(diccionario)
#obteniendo un elemento del diccionario dict_item iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
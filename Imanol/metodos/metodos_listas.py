
#creando una lista list ()
lista = list(["hola","dalto",34,True])

#devuelve la cantidad de elementos de lista 
resultado = len(lista)

#agregando un elemento a la lista
agregando_con_apped = lista.append("JAJAJAJAJA")

#agregando un elemnto a la lista en un indice especifico 
lista.insert(4,"TOMA MAMA") #el numero ayuda para ver donde lo queremos meter 

#agregando varios a la misma lista 
lista.extend([False,2030]) #le estamos pasando una lista 

#elimando un elemnto de lista (por su indice)

print(len(lista))

lista.pop(0) #tambien puedo borrar si pongo -1 etc.

print(len(lista))

#removiendo un elemento de la lista por su valor 
lista.remove("TOMA MAMA")

#eliminando todo los elementos de la lista 
#lista.clear()

#oerdenando la lista (si usamos el parametro REVERSE=TRUE lo ordena en reversa)
#lista.sort() #no lee los textos solo numeros, Si acepta TRUE FALSE

#invirtiendo los elementos de una lista 
lista.reverse() #invierte no importa como lo acomodes 

#verificando si un elemento se encuentra en lista 
elemento_encontrando = lista.index (True)

print(elemento_encontrando)


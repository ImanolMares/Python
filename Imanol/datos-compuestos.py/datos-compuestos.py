#creaando una lista (se pueden modificar
lista = ["Imanol Mares", "Soy Imanol", True, 1.85]

#creando una tupla (no pueden modificar)
tupla =("Imanol Mares", "Soy Imanol", True, 1.85)

#esto es valido 
lista[3] = "Maquinola"

#esto no es valido 
#tupla[3] = "Maquinola"

print(lista [0]) #Sirve para escoger que de la lista

#creando un cojunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Imanol Mares", "Soy Imanol", True, 1.85}
print(conjunto)

#craendo un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario ={
    "nombre" : "Imanol Mares",
    "deporte" : "Futbol",
    "esta_emocionado": True,
}

print(diccionario["esta_emocionado"])


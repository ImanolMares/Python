cadena1 = "hola soy Imanol"
cadena2 = "bienvenido a la universidad"

#Dir - duvuelve la lista de atributos validos del objeto pasado 
#print(dir (cadena1))

resultado = cadena2.upper() #UPPER SIRVE PARA PONER EN MAYUSCULAS 
#Los metodo funciona 1. DATO 2. El punto 3. Los ()

print(resultado)
#LOWER convierte en miniscula 

#Primera letra en Mayuscula 
primera_letra_en_mayuscula = cadena1.capitalize()
print(primera_letra_en_mayuscula) 

#buscamos una cadena en otra cadena, si no hay nada duevuelve -1
Busqueda_find = cadena1.find("o") #Busca la Letra 
print(Busqueda_find) #busacmos una cadena en otra INDEX, pero no devuelve nada

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()
print(es_numerico)

#El espacio se debe quitar sino no es un alfa numerico 
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count()

#Contamos con cuantos caracteres tiene una cadena LEN es una funcion
contar_caracteres = len()

#verificamos si una cadena empiza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith()

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith()

#remplaza un pedazo de cadena dada por otra dada,por otra
cadena_nueva = cadena1.replace() # Respeta los espacios para que cambie el texto

#separa cadenas con la cadena que le pasemos
cadena_separada = cadena1.split() #agrega corchetes 

print(termina_con)
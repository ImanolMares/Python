with open('archivos\\texto_de_imanol.txt','w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Jajajajaa te la recontra teclee")
    
    #agregando 2 lineas con writelines
    archivo.writelines([" - Hola maestro como andas\n"," - Tengo hambre\n"])
    
    #agregando otras 2 lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])
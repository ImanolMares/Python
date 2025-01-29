ingreso_mensual = 300

#Esta es la primera codicion 
if ingreso_mensual > 10000:
    print("estas bien cualquier parte del mundo")
    if ingreso_mensual < 7000 :
        print("estas bien economicamente")
    else :                               
        print("estas gastando mucho")
# if ingreso mensual - gasto mensaul < 0
# elif ingreso mensual - gasto mensaul > 3000
# Tienes que agregar dos cantidades 
    
#Sino se cumple la primera condicion se untiliza esta segunda condicion
elif ingreso_mensual > 1000 :
  print("estas bien en latinoamerica")

elif ingreso_mensual > 500 :
  print("estas bien en argentina")
  
elif ingreso_mensual > 200 :
  print("estas bien en venezuela") 
  
else:
    print("Eres pobre")
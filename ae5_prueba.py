import random
import time
Clientes={"nombres":["Liliana","Clara","Vicente","Diego","Alberto","Daniel","Julio","Francisca","Camila","Emilio"],
"edad":[34,45,19,27,35,42,29,37,32,36],
"id":["165","166","167","168","169","170","171","172","173","174"]}
Productos={"nombres":["te","cafe","jugo","cerveza","vino","vodka","tequila","ron","bebida","energetica"],
"precios":[1500,2200,2000,2500,4000, 5000,3000,4000,2000,2500],
"color":["verde","negro","morado","dorado","rojo","blanco","amarillo","cafe","naranjo","rosa"],
"id":["1","2","3","4","5","6","7","8","9","10"]}

tamaño_clientes=10  
tamaño_productos=10

#print(Clientes.get("nombres")) #Mostrar  clientes
#print(Productos.get("nombres"))#Mostrar listado de productos
#print(Clientes.keys()) #Mostrar claves
#print(Clientes.values()) #Mostrar valores
#print(Productos.items())
#ELiminar clientes
print(Clientes["nombres"])
print (Clientes.items())
#Elige el indice a eliminar de la lista
cliente_eliminado=random.randint(0,9) 
print("El cliente eliminado está en el índice:",cliente_eliminado,"de la lista nombres en el diccionario, y es",Clientes["nombres"][cliente_eliminado])
#del Clientes["nombres"][cliente_eliminado] #Elimina de la lista de nombres
#del Clientes["edad"][cliente_eliminado] #Elimina de la lista de edad
#del Clientes["id"][cliente_eliminado] #elimina de la lista de clientes
print(Clientes.get("nombres"))
print(Clientes.get("edad"))
print(Clientes.get("id"))
print (Clientes.items())
#Eliminar ultimo producto agregado
producto_eliminado=Productos["nombres"][9]
print("El producto eliminado está en el índice:9 de la lista de productos, y es",producto_eliminado)
del Productos["nombres"][9]
del Productos["precios"][9]
del Productos["color"][9]
del Productos["id"][9]
print(Productos.items())
#Mostrar claves del diccionario Clientes
print(Clientes.keys())
time.sleep(2)
print(Clientes.values())
time.sleep(3)
#Mostrar claves del diccionario Productos
print(Productos.keys())
time.sleep(2)
print(Productos.values())
time.sleep(3)
#Mostrar id de los clientes
print("El id de los clientes es:",Clientes.get("id"))
#Modifique todos los ID de los clientes. Agregue la siguiente linea _piloto.
lista_id=Clientes["id"]
nuevo_id=[lista_id[0]+("_pilot"),lista_id[1]+("_pilot"),lista_id[2]+("_pilot"),lista_id[3]+("_pilot"),lista_id[4]+("_pilot"),
lista_id[5]+("_pilot"),lista_id[6]+("_pilot"),lista_id[7]+("_pilot"),lista_id[8]+("_pilot"),lista_id[9]+("_pilot")]
print("Los nuevos id de los clientes son:",nuevo_id)
#Eliminar los ultimos ID_clientes en el listado.
del Clientes["id"][6:9]
print("Los id eliminados son:",Clientes["id"][6:9],"y corresponden a",Clientes["nombres"][6:9])





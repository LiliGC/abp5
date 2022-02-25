import random
import time
#Creamos los diccionarios Clientes y productos.
Clientes={"nombres":["Liliana","Clara","Vicente","Diego","Alberto","Daniel","Julio","Francisca","Camila","Emilio"],
"edad":[34,45,19,27,35,42,29,37,32,36],
"id":["165","166","167","168","169","170","171","172","173","174"]}
Productos={"nombres":["te","cafe","jugo","cerveza","vino","vodka","tequila","ron","bebida","energetica"],
"precios":[1500,2200,2000,2500,4000, 5000,3000,4000,2000,2500],
"color":["verde","negro","morado","dorado","rojo","blanco","amarillo","cafe","naranjo","rosa"],
"id":["1","2","3","4","5","6","7","8","9","10"]}

tamaño_clientes=10  
tamaño_productos=10

#Mostrar  clientes
print("El listado de Clientes está compuesto por:")

print(Clientes.get("nombres"))

#Mostrar listado de productos

print("El listado de Productos está compuesto por:")
print(Productos.get("nombres"))
#print(Clientes.keys()) #Mostrar claves
#print(Clientes.values()) #Mostrar valores
#print(Productos.items())

#ELiminar clientes: Primero me muestra la lista de clientes:
print(Clientes["nombres"])

#Elige el indice a eliminar de la lista
cliente_eliminado=random.randint(0,9) 
print("El cliente eliminado está en el índice:",cliente_eliminado,"de la lista nombres en el diccionario, y es",Clientes["nombres"][cliente_eliminado])
#Elimina de la lista de nombres
del Clientes["nombres"][cliente_eliminado] 
#Elimina de la lista de edad
del Clientes["edad"][cliente_eliminado] 
#elimina de la lista de clientes
del Clientes["id"][cliente_eliminado] 
print(Clientes.get("nombres"))
print(Clientes.get("edad"))
print(Clientes.get("id"))

#Eliminar ultimo producto agregado
producto_eliminado=Productos["nombres"][9]
print("El producto eliminado está en el índice:9 digite la lista de productos, y es",producto_eliminado)
del Productos["nombres"][9]
del Productos["precios"][9]
del Productos["color"][9]
del Productos["id"][9]
print(Productos.items())

#Mostrar claves del diccionario Clientes
for key in Clientes.keys():
    print (key)
    time.sleep(2)

for value in Clientes.values():
    print(value)
    time.sleep(3)

#Mostrar claves del diccionario Productos
for key in Productos.keys():
    print(key)
    time.sleep(2)

for value in Productos.values():
    print(value)
    time.sleep(3)

#Mostrar id de los clientes
print("El id de los clientes es:",Clientes.get("id"))

#Modifique todos los ID de los clientes. Agregue la siguiente linea _piloto. Aqui debo sacar la de cliente eliminado o hacemos una copia del diccionario para eliminar de ahi.
lista_id=Clientes["id"]
nuevo_id=[lista_id[0]+("_pilot"),lista_id[1]+("_pilot"),lista_id[2]+("_pilot"),lista_id[3]+("_pilot"),lista_id[4]+("_pilot"),
lista_id[5]+("_pilot"),lista_id[6]+("_pilot"),lista_id[7]+("_pilot"),lista_id[8]+("_pilot"),lista_id[9]+("_pilot")]
print("Los nuevos id de los clientes son:",nuevo_id)

#Eliminar los ultimos ID_clientes en el listado.
print("Los id eliminados son:",Clientes["id"][-4::],"y corresponden a",Clientes["nombres"][-4::])
del Clientes["id"][-4::]
print("Los id que quedan en la lista son:",Clientes["id"])





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

#Mostrar  clientes
print("Bienvenido a Te lo Vendo Market","\n")
print("El listado de Clientes está compuesto por:","\n")

print(Clientes.get("nombres"),"\n")

#Mostrar listado de productos

print("El listado de Productos está compuesto por:\n")
print(Productos.get("nombres"),"\n")

#print(Productos.items())

#ELiminar clientes: Primero me muestra la lista de clientes:
print("Los clientes registados son",Clientes["nombres"],"\n")

#Elige el indice a eliminar de la lista
cliente_eliminado=random.randint(0,9) 
print("El cliente eliminado está en el índice:",cliente_eliminado,"de la lista nombres en el diccionario, y es",Clientes["nombres"][cliente_eliminado],"\n")
#Elimina de la lista de nombres
del Clientes["nombres"][cliente_eliminado] 
#Elimina de la lista de edad
del Clientes["edad"][cliente_eliminado] 
#elimina de la lista de clientes
del Clientes["id"][cliente_eliminado] 
print("Los datos del Diccionario Clientes luego de la actualización:","\n")
print(Clientes.get("nombres"))
print(Clientes.get("edad"))
print(Clientes.get("id"),"\n")

#Eliminar ultimo producto agregado
producto_eliminado=Productos["nombres"][-1]
print("El producto eliminado está en el índice:-1 y es",producto_eliminado,"\n")
del Productos["nombres"][-1]
del Productos["precios"][-1]
del Productos["color"][-1]
del Productos["id"][-1]

#Mostrar claves del diccionario Clientes
print("Las claves del diccionario de Clientes son las siguientes:","\n")
for key in Clientes.keys():
    print (key)
    time.sleep(2)
print("\n","Los valores del diccionario de  Clientes son los siguientes:","\n")
for value in Clientes.values():
    print(value)
    time.sleep(3)

#Mostrar claves del diccionario Productos
print("\n","Las claves del diccionario Productos son las siguientes:","\n")
for key in Productos.keys():
    print(key)
    time.sleep(2)
print("Los valores del diccionario Productos son los siguientes:","\n")
for value in Productos.values():
    print(value)
    time.sleep(3)

#Mostrar id de los clientes existentes
print("\n","Los id de los clientes son:",Clientes.get("id"))

#Modifique todos los ID de los clientes. Agregue la siguiente linea _piloto. 
# Aqui creo una lista con los nuevos id con la que luego actualizo el diccionario Clientes.
lista_nuevoid=[]
for i in Clientes["id"]:
    nuevo_id=(i+"_piloto")
    lista_nuevoid.append(nuevo_id)
print(lista_nuevoid,"\n")
up_dict={"id":lista_nuevoid}
Clientes.update(up_dict)
print("Los nuevos id de los clientes son:",Clientes["id"],"\n")

#Eliminar los ultimos ID_clientes en el listado.
print("Los id eliminados son:",Clientes["id"][-4::],"y corresponden a",Clientes["nombres"][-4::])
del Clientes["id"][-4::]
print("Los id que quedan en la lista son:",Clientes["id"])





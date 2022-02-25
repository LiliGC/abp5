import random
import time
#Creamos los diccionarios Clientes y productos con listas vacias en su interior.
Clientes={"nombres":[],"edad":[],"id":[]}
Productos={"nombres":[],"precio":[],"color":[],"id":[]}
Compras={"nombres":[],"cantidad":[]}
#Definimos el tamaño para las listas del diccionario
tamaño_clientes=10  
tamaño_productos=5
#Leemos los datos y los agregamos los clientes
print("-------------Bienvenido a Te lo Vendo Market---------------","\n")
for i in range(tamaño_clientes):
    print("Ingrese los datos del cliente",i+1)
    nombre=input("Nombre: ").title()
    edad=int(input("edad: "))
    id=input("Id: ")
    #La primera lista es para los nombres de los clientes
    Clientes["nombres"].append(nombre)
    #La segunda lista es para las edades de los clientes
    Clientes["edad"].append(edad)
    #La tercera lista es para los identificación (id) de los clientes
    Clientes["id"].append(id)
#Leemos los datos y agregamos los productos al inventario
for i in range(tamaño_productos):
    print("Ingrese los datos del producto",i+1)
    nombre=input("Nombre: ").title()
    precio=int(input("precio: "))
    color=input("color: ").lower()
    id=input("Id: ")
    #La primera lista es para los nombres de los productos
    Productos["nombres"].append(nombre)
    #La segunda lista es para las edades de los productos
    Productos["precio"].append(precio)
    #La tercera lista es para los identificación (id) de los productos
    Productos["color"].append(color)
    #La cuarta lista es para la identificación(id) de los productos
    Productos["id"].append(id)

#Mostrar los valores en el diccionario Clientes
for i in range(tamaño_clientes):
    print("Mostrando los datos del cliente", i+1)
    print("Nombre:",Clientes["nombres"][i], "id:",Clientes["id"][i],"\n") 

#Mostrar listado de productos
print("Mostrando listado de productos:","\n")
print(Productos.get("nombres"),Productos.get("precios"),"\n")

#Eliminar Clientes al azar usando random.
cliente_eliminado=random.randint(0,9)
print("El cliente eliminado está en el índice:",cliente_eliminado,"de la lista nombres en el diccionario, y es",Clientes["nombres"][cliente_eliminado],"\n")
del Clientes["nombres"][cliente_eliminado]
del Clientes["edad"][cliente_eliminado]
del Clientes["id"][cliente_eliminado]

#Eliminar ultimo producto agregado
producto_eliminado=Productos["nombres"][-1]
print("El producto eliminado está en el índice: -1 de la lista de productos, y es",producto_eliminado,"\n")
del Productos["nombres"][-1]
del Productos["precios"][-1]
del Productos["color"][-1]
del Productos["id"][-1]
print("Los productos que quedan disponibles son",Productos.items(),"\n")

#Mostrar claves del diccionario Clientes
print("Las claves del diccionario Cliente son las siguientes:","\n")
for key in Clientes.keys():
    print (key)
    time.sleep(2)
print("Los valores del diccionario Cliente son los siguientes:","\n")
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

#Mostrar id de los clientes
print("Los id de los clientes son:",Clientes.get("id"),"\n")

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

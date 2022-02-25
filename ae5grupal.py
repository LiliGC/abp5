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
for i in range(tamaño_clientes):
    print("Ingrese los datos de la persona",i+1)
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
    print("Nombre:",Clientes["nombres"][i], "id",Clientes["id"][i]) 
#Mostrar listado de productos
print("Mostrando listado de productos:")
print(Productos.get("nombres"),Productos.get("precios"))
#Eliminar Clientes
cliente_eliminado=random.randint(0,9)
print("El cliente eliminado está en el índice:",cliente_eliminado,"de la lista nombres en el diccionario, y es",Clientes["nombres"][cliente_eliminado])
del Clientes["nombres"][cliente_eliminado]
del Clientes["edad"][cliente_eliminado]
del Clientes["id"][cliente_eliminado]
#Eliminar ultimo producto agregado
producto_eliminado=Productos["nombres"][4]
print("El producto eliminado está en el índice:4 de la lista de productos, y es",producto_eliminado)
del Productos["nombres"][4]
del Productos["precios"][4]
del Productos["color"][4]
del Productos["id"][4]
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
print(Clientes["id"][-4::])
del Clientes["id"][-4::]
print("Los id eliminados son:",Clientes["id"],"y corresponden a",Clientes["nombres"][-4::])

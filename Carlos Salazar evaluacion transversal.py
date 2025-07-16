
productos ={        '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
                           }

stock =      {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }

"""
HPp=2
acerr=3
Asuss=2
Delll=1
"""

def stock_marca():  
  while True:
    try:
      marca=input("Ingrese marca a consultar:").upper()
      for calve,valor in productos.items(): 
        if valor[0]=="HP":
         print(valor[0])
         print("El stock es: 2")
        elif valor[0]=="ACER":
         print(valor[0] )
         print("El stock : 3") 
        elif valor[0]=="ASUS":
            print(valor[0])
            print("El stock es: 2") 
        elif valor[0]=="DELL":
            print(valor[0])
            print("El stock es: 1") 
    except ValueError:
     print("Producto no encontrado")

def Busqueda_precio():
 while True:
   try:
    precio_minimo=int(input("Ingrese precio minimo: "))
   except ValueError:
     print("Debe ingresar valores enteros!!")
   while True:
        try:
         precio_maximo=int(input("Ingrese precio maximo: "))
         return
        except ValueError:
         print("Debe ingresar valores enteros!!") 

def Listado_de_productos():
   for clave,valor in productos.items():
    print(f"{clave} - {valor[0]} - {valor[1]} - {valor[2]} - {valor[3]} - {valor[4]} - {valor[5]} - {valor[6]}  ")

def salir():
  print("Saliendo del sistema.")
  exit()

def menu():
   while True:  
        print("\n***MENU PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        
        opc=input("Ingrese opción ")
        
        if opc == "1" : #Muestra un stock de una marca en especifico
         stock_marca()
        elif opc == "2" : # Busca un producto ingresando un precio minimo y maximo
         Busqueda_precio()
        elif opc== "3" : # Enlista todos los productos
         Listado_de_productos()
        elif opc == "4" : #salir
         salir()
        else:
         print("Opcion invalida")
menu()

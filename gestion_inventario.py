"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: _______________________________________
Fecha: __________________________________________

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    nombre = None
    contacto = None
       
    def __init__(self, nombre: str, contacto: str):
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
       return f"Proveedor:{self.nombre} ({self.contacto})"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    codigo = None
    nombre = None
    precio = None
    stock = None
    proveedor = None

    def __init__(self, codigo:str, nombre: str, precio:float, stock:int, proveedor:Proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def __str__(self):
        return f"[{self.codigo}]  {self.nombre} - {self.precio} € ( {self.stock} uds.) {self.proveedor}"

# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    nombre_fichero = None
    productos = []

    def __init__(self, nombre_fichero:str):
       self.nombre_fichero = nombre_fichero

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """

        with open(self.nombre_fichero, "r", encoding="utf-8") as archivo:
            self.productos = json.load(archivo)
        
        # para pruebas
        for i in self.productos:
            print(i)

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        
        with open(self.nombre_fichero, "w", encoding="utf-8") as archivo:
            json.dump(self.productos, archivo, indent=2)

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        for i in self.productos:
            if i["codigo"] == producto.codigo:
                print(" Error el producto ya existe")
                return 0

        self.productos.append(producto)
        self.guardar()

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        for i in self.productos:
            print(f"[{i["codigo"]}]  {i["nombre"]} - {i["precio"]} € ( {i["stock"]} uds.)")

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        for producto in self.productos:
            if producto["codigo"] == codigo:
                return producto
            else:
                return None

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        pass

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        i = 0
        for producto in self.productos:
            if producto["codigo"] == codigo:
                self.productos.remove(producto)
            else:
                return None
        
        self.guardar()

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # Aviso que por ahora todo lo que "guarda" corrompe el archivo
    inventario = Inventario("inventario.json")
    inventario.cargar()

    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida
    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                codigo = input("¿Que codigo tiene el producto?: ")
                nombre = input("¿Como se llama el producto?: ")
                precio = int(input("¿Cuanto vale el producto?: "))
                stock = int(input("¿Cuatas unidades hay?: "))
                proveedor = Proveedor("test", "test")

                producto = Producto(codigo, nombre, precio, stock, proveedor)
                inventario.anadir_producto(producto)
            case "2":
                inventario.mostrar()
            case "3":
                codigo = input("¿Que codigo quires buscar?: ")
                print(inventario.buscar(codigo))
            case "4":
                pass
            case "5":
                codigo = input("¿Que codigo quires eliminar?: ")
                inventario.eliminar(codigo)
            case "6":
                pass
            case "7":
                pass
            case "8":
                exit()
            case _:
                print("¿Que se supone que has escrito aqui?")

if __name__ == "__main__":
    main()

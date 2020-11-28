from prettytable import PrettyTable
from bdCategorias import (
    connection,
    getCategoriaBD,
    insertCategoriaBD,
    searchCategoriaById,
    updateCategoriaBD,
    deleteCategoriaBD,
)


class tablaCategorias:
    def __init__(self):
        self.getAllCategorias()

    def getAllCategorias(self):
        result = getCategoriaBD()

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for categoria in result:
            table.add_row([categoria["idCategoriasProductos"], categoria["nombre"]])
        print(table)
        table.clear()

    def addNewCategoria(self):
        print("Se está añadiendo una nueva categoría:")
        nombre = input("Nombre: ")
        insertCategoriaBD(nombre)
        print(" ")
        print("-----------Se agregó correctamente la categoría----------")
        print(" ")
        self.getAllCategorias()

    def updateCategoria(self):
        print("Se está actualizando la información de una categoría: ")
        self.getAllCategorias()
        id = int(input("Id de la categoría a actualizar: "))
        categoria = searchCategoriaById(id)

        update = int(input("¿Desea actualizar el nombre? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Nombre anterior: {categoria['nombre']}")
            nombre = input("Nuevo nombre: ")
        else:
            nombre = categoria["nombre"]
        updateCategoriaBD(nombre, id)
        print(" ")
        print("-----------Se actualizó correctamente la categoría----------")
        print(" ")
        self.getAllCategorias()

    def deleteCategoria(self):
        print("Se está eliminando una categoría: ")
        self.getAllCategorias()
        id = int(input("Id de la categoría a eliminar: "))
        deleteCategoriaBD(id)
        print(" ")
        print("-----------Se eliminó correctamente la categoría----------")
        print(" ")
        self.getAllCategorias()

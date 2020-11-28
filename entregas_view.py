from prettytable import PrettyTable
from bdEntregas import (
    connection,
    getEntregaBD,
    insertEntregaBD,
    searchEntregaById,
    updateEntregaBD,
    deleteEntregaBD,
)


class tablaEntregas:
    def __init__(self):
        self.getAllEntregas()

    def getAllEntregas(self):
        result = getEntregaBD()

        table = PrettyTable()
        table.field_names = ["Id", "IdFactura", "Fecha", "Hora", "Lugar"]

        for entrega in result:
            table.add_row(
                [
                    entrega["idEntregas"],
                    entrega["idFacturas"],
                    entrega["fecha"],
                    entrega["hora"],
                    entrega["lugar"],
                ]
            )
        print(table)
        table.clear()

    def addNewEntrega(self):
        print("Se está añadiendo una nueva entrega:")
        idFactura = input("IdFactura: ")
        fecha = input("Fecha: ")
        hora = input("Hora: ")
        lugar = input("Lugar: ")
        insertEntregaBD(idFactura, fecha, hora, lugar)
        print(" ")
        print("-----------Se agregó correctamente la entrega----------")
        print(" ")
        self.getAllEntregas()

    def updateEntrega(self):
        print("Se está actualizando la información de una entrega: ")
        self.getAllEntregas()
        id = int(input("Id de la entrega a actualizar: "))
        entrega = searchEntregaById(id)

        update = int(input("¿Desea actualizar el idFactura? 0.No, 1.Sí: "))
        if update == 1:
            print(f"IdFactura anterior: {entrega['idFacturas']}")
            idFactura = input("Nuevo IdFactura: ")
        else:
            idFactura = entrega["idFacturas"]

        update = int(input("¿Desea actualizar la fecha? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Fecha anterior: {entrega['fecha']}")
            fecha = input("Nueva fecha: ")
        else:
            fecha = entrega["fecha"]

        update = int(input("¿Desea actualizar la hora? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Hora anterior: {entrega['hora']}")
            hora = input("Nueva hora: ")
        else:
            hora = entrega["hora"]

        update = int(input("¿Desea actualizar el lugar? 0.No, 1.Sí: "))
        if update == 1:
            print(f"Lugar anterior: {entrega['lugar']}")
            lugar = input("Nuevo lugar: ")
        else:
            lugar = entrega["lugar"]
        updateEntregaBD(idFactura, fecha, hora, lugar, id)
        print(" ")
        print("-----------Se actualizó correctamente la entrega----------")
        print(" ")
        self.getAllEntregas()

    def deleteEntrega(self):
        print("Se está eliminando una entrega: ")
        self.getAllEntregas()
        id = int(input("Id de la entrega a eliminar: "))
        deleteEntregaBD(id)
        print(" ")
        print("-----------Se eliminó correctamente la entrega----------")
        print(" ")
        self.getAllEntregas()

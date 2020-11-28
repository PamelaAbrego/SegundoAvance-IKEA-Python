from menuAdministrador import MenuAdministrador

print("----------------------------")
print("Bienvenido a IKEA")
print("----------------------------")
while True:
    print("Menú:")
    print("0 - Salir. ")
    print("1 - Ingresar como Administrador.")
    print("2 - Ingresar como Cliente.")

    option = int(input("Opción: "))

    if option == 0:
        print("------------------------------------------")
        print("Saliendo de IKEA.")
        print("------------------------------------------")
        break
    if option == 1:
        print("------------------------------------------")
        MenuAdministrador()
        print("------------------------------------------")
    if option == 2:
        print("------------------------------------------")
        print("MENU CLIENTES EN CONSTRUCCIÓN")
        print("------------------------------------------")
        # Se colocará el menú de registro, ya sea para ingresar con cuenta existente o para crear una nueva.
        # Luego de ingresar, se mostrará un menú con todos los procesos que puede realizar un cliente.
        pass
        print("------------------------------------------")

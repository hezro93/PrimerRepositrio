"""Base de datos de empleados."""

import datetime as dt
from clases_ejercicio2 import Emplado


def imprimir_menu():
    """Función para imprimir el menú de opciones."""
    print("Menú de opciones")
    print("(1) Añadir empleado")
    print("(2) Borrar un empleado")
    print("(3) Mostrar lista de empleados")
    print("(4) Mostrar detalles de un empleado")
    print("(5) Mostrar empleados de cumpleaños")
    print("(6) Terminar")


def add_empleado(d_empleados):
    """Función para agregar un empleado al diccionario de empleados."""
    more = "si"
    while more == "si":
        print("Introduce los datos del empleado:")
        tipo_empleado = input("Introduce el tipo de empleado (fijo/temporal): ")
        tipo_empleado_lower = tipo_empleado.lower()
        if tipo_empleado_lower == "fijo":
            nombre = input("Introduce el nombre del empleado: ")
            nif = input("Introduce el NIF: ")
            if not nif in d_empleados:
                nacimiento = input("Introduce fecha de nacimiento (dd/mm/aaaa): ")
                sueldo_base_mensual = input("Introduce sueldo base mensual: ")
                alta = input("Introduce el año de alta en la empresa: ")
                complemento_anual = input("Introduce el complemento anual: ")
                baja = "fijo"
                d_empleados[nif] = Emplado(
                    nif,
                    nombre,
                    nacimiento,
                    sueldo_base_mensual,
                    alta,
                    baja,
                    complemento_anual,
                    tipo_empleado_lower,
                )
            else:
                print("Ese NIF ya está en la base de datos de empleados.")
        elif tipo_empleado_lower == "temporal":
            nombre = input("Introduce el nombre del empleado: ")
            nif = input("Introduce el NIF: ")
            if not nif in d_empleados:
                nacimiento = input("Introduce fecha de nacimiento (dd/mm/aaaa): ")
                sueldo_mensual = input("Introduce sueldo mensual: ")
                alta = input("Introduce fecha de alta (dd/mm/aaaa): ")
                baja = input("Introduce fecha de baja (dd/mm/aaaa): ")
                complemento_anual = "temporal"
                d_empleados[nif] = Emplado(
                    nif,
                    nombre,
                    nacimiento,
                    sueldo_mensual,
                    alta,
                    baja,
                    complemento_anual,
                    tipo_empleado_lower,
                )
            else:
                print("Ese NIF ya está en la base de datos de empleados.")
        else:
            print("ERROR al introducir el tipo de empleado (fijo/temporal)")
        more = input("¿Quieres añadir un nuevo empleado a la base de datos (Si/No)? ").lower()


def borrar_empleado(d_empleados):
    """Función para borrar un empleado de la base de datos."""
    more = "si"
    while more == "si":
        nif = input("Introduce el nif del empelado que quieres borrar: ")
        if nif in d_empleados:
            del d_empleados[nif]
        else:
            print("Este empleado no está en la base de datos.")
        more = input("¿Quieres eliminar otro empleado de la base de datos (Si/No)? ").lower()


def mostrar_lista_empleados(d_empleados):
    """Función para mostrar la lista de empleados registrados en la base de datos."""
    for nif, empleado in d_empleados.items():
        print(f"{nif:15} {empleado.nombre} - {empleado.tipo}")


def mostrar_detalle_empleado(d_empleados):
    """Función para mostrar detalles de un empleado."""
    more = "si"
    while more == "si":
        nif = input("Introduce el nif del empelado: ")
        if nif in d_empleados:
            if d_empleados[nif].tipo == "fijo":
                print(f"Nombre: {d_empleados[nif].nombre}")
                print(f"NIF: {d_empleados[nif].nif}")
                print(f"Fecha nacimiento: {d_empleados[nif].nacimiento}")
                print(f"Tipo: empleado {d_empleados[nif].tipo}")
                print(f"Año de alta: {d_empleados[nif].alta}")
                print(f"Sueldo base: {d_empleados[nif].sueldo_base_mensual}")
                print(f"Complemento anual: {d_empleados[nif].complemento_anual}")
                print(f"Sueldo mensual: {d_empleados[nif].calcular_sueldo_mensual()}")
            else:
                print(f"Nombre: {d_empleados[nif].nombre}")
                print(f"NIF: {d_empleados[nif].nif}")
                print(f"Fecha nacimiento: {d_empleados[nif].nacimiento}")
                print(f"Tipo: empleado {d_empleados[nif].tipo}")
                fecha_alta = d_empleados[nif].alta.split("/")
                año_alta = fecha_alta[2]
                print(f"Año de alta: {año_alta}")
                print(f"Sueldo base: {d_empleados[nif].baja}")
                print(f"Sueldo mensual: {d_empleados[nif].sueldo_base_mensual}")
        else:
            print("Este empleado no está en la base de datos.")
        more = input("¿Quieres ver detalles de otro empleado de la base de datos (Si/No)? ").lower()


def cumples_del_mes(d_empleados):
    """Esta función muestra los empleados que están de cumpleaños en el mes."""
    more = "si"
    print("estoy en funcion cumpleaños")
    while more == "si":
        mes_seleccionado = input("Introduce un mes (1 - 12): ")
        cumples = 0
        for nif, empleado in d_empleados.items():
            nacimiento_empleado = d_empleados[nif].nacimiento.split("/")
            mes_empleado = nacimiento_empleado[1]
            print(mes_empleado)
            if mes_empleado == mes_seleccionado:
                print(f"{empleado.nombre} - {empleado.nacimiento}")
                cumples = 1
        if cumples == 0:
            print("En el mes seleccionado no hay cumpleaños.")
        more = input("¿Quieres ver los cumpleaños de otro mes (Si/No)? ").lower()


def main():
    """Esta es la función principal."""
    d_empleados = {}
    opcion = 0
    while opcion != 6:
        imprimir_menu()
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            add_empleado(d_empleados)
        elif opcion == 2:
            borrar_empleado(d_empleados)
        elif opcion == 3:
            mostrar_lista_empleados(d_empleados)
        elif opcion == 4:
            mostrar_detalle_empleado(d_empleados)
        elif opcion == 5:
            cumples_del_mes(d_empleados)


if __name__ == "__main__":
    main()

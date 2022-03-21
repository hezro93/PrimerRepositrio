"""Clases del ejercicio 2."""

import datetime as dt


class Emplado:
    """Clase que define un Empleado."""

    def __init__(self, nif, nombre, nacimiento, sueldo_base_mensual, alta, baja, complemento_anual, tipo):
        """Inicializa la clase Empleado."""
        self.nif = nif
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.sueldo_base_mensual = sueldo_base_mensual
        self.alta = alta
        self.baja = baja
        self.complemento_anual = complemento_anual
        self.tipo = tipo

    def calcular_sueldo_mensual(self):
        """Calcular el precio de una subscripción según la cantidad ed meses."""
        fecha_actual = dt.date.today()
        actual_year = fecha_actual.year
        sueldo_mensual_actual = float(self.sueldo_base_mensual) + float(self.complemento_anual) * (
            actual_year - int(self.alta)
        )
        return sueldo_mensual_actual

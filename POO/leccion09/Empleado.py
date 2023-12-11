class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.edad = sueldo
    # sobreescribimos el metoso __str__
    def __str__(self):
        return f"Empleado: [Nombre: {self.nombre} Edad: {self.edad}]"

    def mostrar_detalles(self):
        return self.__str__()


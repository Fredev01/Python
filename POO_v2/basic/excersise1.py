""" 
This module is for class Estudiante
"""


class Estudiante:
    """ 
    Class Estudiante
    """

    def __init__(self, nombre: str, edad: int, grado: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def get_data(self):
        """ 
            This function is for get the data
        """
        return f"""
            =====================================
            =       DATOS DEL ESTUDIANTE        =
            =   Nombre: {self.nombre}           =
            =   Edad: {self.edad}               =
            =   Grado: {self.grado}             =
            =====================================
            """

    def estudiar(self):
        """ 
        This method is for saludar
        """
        print(f'El estudiante {self.nombre} esta estudiando')


try:
    print("Ingrese los datos")
    nombre: str = input("Nombre: ")
    edad: int = int(input("Edad: "))
    grado: str = input("Grado: ")
    estudiante: Estudiante = Estudiante(nombre, edad, grado)
    message: str = """
    ===============================
    =    Elija una opcion         =
    =    - Estudiar               =
    ===============================
          """
    print(estudiante.get_data())
    print(message)
    opcion: str = input("Opcion: ")

    while opcion.lower() != "estudiar":
        print("Ingresa una opcion valida!")
        opcion = input("Opcion: ")

    else:
        estudiante.estudiar()

except Exception as e:
    print("Ocurrio un error!")

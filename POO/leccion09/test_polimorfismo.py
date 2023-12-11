from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Angel", 70000)
imprimir_detalles(empleado)

gerente = Gerente("Alfredo", 100000, "Sistemas")
imprimir_detalles(gerente)
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion Objeto cuadrado".center(40, "-"))
cuadrado1 = Cuadrado(lado=6, color="azul")
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f"Calculo area cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)
# MRO - Method Resolution Order
# print(Cuadrado.mro())

print("Creacion Objeto rectangulo".center(40, "-"))
rectangulo1 = Rectangulo(ancho=5, alto=8, color="verde")
rectangulo1.alto = -4
print(f"Calculo area cuadrado: {rectangulo1.calcular_area()}")
print(rectangulo1)

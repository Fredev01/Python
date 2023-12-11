from Monitor import Monitor
from computadora import Computadora
from orden import Orden
from raton import Raton
from teclado import Teclado

teclado1 = Teclado("HP", "USB")
raton1 = Raton("Acer", "USB")
monitor1 = Monitor("ASUS", 14)
computadora1 = Computadora("ASUS", monitor1, teclado1, raton1)

teclado2 = Teclado("Lenovo", "bluetooth")
raton2 = Raton("Huawei", "bluetooth")
monitor2 = Monitor("Apple", 26)
computadora2 = Computadora("MackBook", monitor2, teclado2, raton2)

teclado3 = Teclado("HP", "USB")
raton3 = Raton("HP", "USB")
monitor3 = Monitor("HP", 16)
computadora3 = Computadora("HP", monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
# print(orden1)
orden1.agregar_computadoras(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)
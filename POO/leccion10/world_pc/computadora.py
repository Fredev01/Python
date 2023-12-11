from world_pc.Monitor import Monitor
from world_pc.raton import Raton
from world_pc.teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        """


if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("Acer", "USB")
    monitor1 = Monitor("ASUS", "USB")
    computadora1 = Computadora("ASUS", monitor1, teclado1, raton1)
    print(computadora1)
    teclado2 = Teclado("Lenovo", "bluetooth")
    raton2 = Raton("Huawei", "bluetooth")
    monitor2 = Monitor("Apple", 26)
    computadora2 = Computadora("MackBook", monitor2, teclado2, raton2)
    print(computadora2)

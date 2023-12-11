class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

def pedir_datos():
    ancho = int(input("Proporciona el ancho: "))
    alto = int(input("Proporciona el alto: "))
    profundo = int(input("Proporciona lo profundo: "))
    return (ancho, alto, profundo)
def mostrar_resultados(obj):
    print(f"Volumen cubo: {obj.calcular_volumen()}")
datos = pedir_datos()
cubo1 = Cubo(datos[0], datos[1], datos[2])
mostrar_resultados(cubo1)


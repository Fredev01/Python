class Rectangulo:
    """
    clase Rectangulo para calcular el area de un rectangulo
     --atributos--
       base, altura
    --metodos--
        calcular_area
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
def resultados():
    base = float(input("Proporciona la base: "))
    altura = float(input("Proporciona la altura: "))
    rectangulo = Rectangulo(base, altura)
    print(f"Area  rectangulo: {rectangulo.calcular_area():.4f}")
resultados()


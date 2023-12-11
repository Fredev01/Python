class Aritmetica:
    """
    clase Aritmetica para realizar las operaciones de suma, resta, etc.
    """
    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b
    def sumar(self):
        return self.operando_a + self.operando_b
    def restar(self):
        return self.operando_a - self.operando_b
    def multiplicar(self):
        return self.operando_a * self.operando_b
    def dividir(self):
        return self.operando_a / self.operando_b

aritmetica1 = Aritmetica(8, 5)
print(f"suma: {aritmetica1.sumar()} resta:{aritmetica1.restar()} multiplicar:{aritmetica1.multiplicar()} dividir:{aritmetica1.dividir()}")
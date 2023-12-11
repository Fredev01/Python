class Persona:
    def __init__(self,nombre,apellido,edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}")

persona_1 = Persona("Angel", "Lopez", 18, "1928301", 7, m="manzana")
persona_2 = Persona("Brenda","Lopez",19)
persona_1.mostrar_detalle()
persona_2.mostrar_detalle()





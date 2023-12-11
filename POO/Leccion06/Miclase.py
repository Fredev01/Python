class Miclase:
    varible_clase = "mi variable clase"

    def __init__(self, variable_instancia):
        self.variable_instacia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(Miclase.varible_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.varible_clase)


#Miclase.metodo_estatico()
Miclase.metodo_clase()
"""
mi_clase = Miclase("varible del objeto")
print(mi_clase.variable_instacia)
print(mi_clase.varible_clase)
print(mi_clase.varible_clase)
mi_clase.varible_clase = " obj1 sobreescribio la varible"
mi_clase2 = Miclase("varible del objeto2")
print(mi_clase2.variable_instacia)
print(mi_clase2.varible_clase)
"""


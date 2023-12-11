"""
Proporciona tu edad:
0-10: La infancia es increible
10-20: Muchos cambios y mucho estudio
20-30: Amor y Comienza el trabajo...

Cualquier otro valor: Etapa de vida no reconocida

"""

edad = int(input("Proporciona tu edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = "La infancia es increible..."
elif 10 <= edad < 20:
    mensaje = " Muchos cambios y mucho estudio..."
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo..."
else:
    mensaje = "Etapa de vida no reconocida"
print(f"Tu edad es: {edad}, {mensaje}")

"""
Desarrollar una tienda de libros
nombre del libro
id del libro (int)
precio del libro(float)
indicar si el encvio es gratuito (bool)
por ultimo imprimir los datos solicitados


"""
import envio as envio

print("Proporcione los siguientes datos del libro:")
nombre_libro = input("Proporciona el nombre: ")
id_libro = int(input("Proporciona el ID: "))
precio_libro = float(input("Proporciona el precio: "))
envio_gratuito = input("Indica si el libro es gratuito (True/False): ")

if envio_gratuito == "True":
    envio_gratuito = True
elif envio_gratuito == "False":
    envio_gratuito = False
else:
    envio_gratuito = "Valor incorrecto, debe escribir True/False"
print(f'''
    Nombre: {nombre_libro},
    ID: {id_libro},
    Precio: {precio_libro},
    Envio Gratuito?: {envio_gratuito}
''')



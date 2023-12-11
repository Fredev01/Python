import psycopg2

conexion = psycopg2.connect(user='postgres', password='@programing', host='127.0.0.1', port='5432', database='test_db')

"""
# Consultar registros en la base de datos
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id IN %s'
            entrada = input('Porporciona los id\'s  a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
"""

"""
# Agregar registros en la base de datos
#   commit guarda los cambios en la base de datos
#   al usar with, el commit se ejecuta en automatico, asi que no hay que colocarlo manualmente
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('Marcos', 'Gutu', 'mgutu@gmail.com'),
                ('Jose', 'Quintana', 'jquintana@gmail.com'),
                ('Ana', 'Gonzalez', 'agonzalez@gmail.com'),

            )
            cursor.executemany(sentencia, valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

"""

"""
# Actualizar un registro en la BD

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
            valores = (
                ('Brenda Monica', 'Sanchez', 'bmsanchez@gmail.com', 2),
                ('Daniel', 'Gomez', 'dgomez@gmail.com', 3),
                ('Leonardo', 'Solorzano', 'lsolorzano@gmail.com', 4)

            )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

"""

# Eliminar registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id IN%s'
            entrada = input("Proporciona los id_persona a eliminar (separados por comas): ")
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
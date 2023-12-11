import psycopg2 as bd

conexion:bd = bd.connect(user='postgres', password='@programing', host='127.0.0.1', port='5432', database='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia:str = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Aguilar', 'maguilar@gmail.com')
    cursor.execute(sentencia, valores)  # execute the sentence SQL

    sentencia:str = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s'
    valores = ('Brenda', 'Lopez', 'blopez@gmail.com', 2)
    cursor.execute(sentencia, valores)
    conexion.commit()
    print("Termina la transaccion, se hizo commit")
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()

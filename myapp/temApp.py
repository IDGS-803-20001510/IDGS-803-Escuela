from db import get_connection

try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumnos()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)

# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumno(%s)',(2,))
#         resultset=cursor.fetchall()
#         #for row in resultset:
#         print(resultset)
#     connection.close()
    
# except Exception as ex:
#     print(ex)

# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumno(%s,%s,%s)',("nombre","apellidos","correo"))
#     connection.commit()    
#     connection.close()
    
# except Exception as ex:
#     print(ex)
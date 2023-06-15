"""
Inserte los siguientes registros dentro de la base de datos creada en la clase anterior, corregir los errores que impidan la instrucción.

No se sabe con certeza el lanzamiento de las cohortes N° 1245 y N° 1246, se solicita que las elimine de la tabla.

Se ha decidido retrasar el comienzo de la cohorte N°1243, por lo que la nueva fecha de inicio será el 16/05. Se le solicita modificar la fecha de inicio de esos alumnos.

El alumno N° 165 solicito el cambio de su Apellido por “Ramirez”.

El área de Learning le solicita un listado de alumnos de la Cohorte N°1243 que incluya la fecha de ingreso.

Como parte de un programa de actualización, el área de People le solicita un listado de los instructores que dictan la carrera de Full Stack Developer.

Se desea saber que alumnos formaron parte de la cohorte N° 1235. Elabore un listado.
Del listado anterior se desea saber quienes ingresaron en el año 2019.

La siguiente consulta permite acceder a datos de otras tablas y devolver un listado con la carrera a la cual pertenece cada alumno:

SELECT alumnos.nombre, apellido, fechaNacimiento, carreras.nombre
FROM alumnos
INNER JOIN cohortes
ON cohorte=idCohorte
INNER JOIN carreras
ON carrera = idCarrera

"""

import mysql.connector
from mysql.connector import Error

# * Carrea: ID, Nombre.<br>
# * Cohorte: ID, Código, Carrera, Fecha de Inicio, Fecha de Finalización, Instructor.<br>
# * Instructores: ID, Cédula de identidad, Nombre, Apellido, Fecha de Nacimiento, Fecha de Incorporación.<br>
# * Alumnos: ID, Cédula de identidad, Nombre, Apellido, Fecha de Nacimiento, Fecha de Ingreso, Cohorte.<br>

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='henry',
                                         user='root',
                                         password='password')
 
    cursor = connection.cursor()
    # result = cursor.execute(SQL_query, multi=True)

    with open('M2/Clase06/registros_henry.sql', 'r') as sql_file:
      queries = sql_file.read().split(';')

      for query in queries:
        if query.strip():
          result_iterator = cursor.execute(query, multi=True)
          for res in result_iterator:
            print("Running query: ", res)  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows" )

        # result_iterator = cursor.execute(sql_file.read(), multi=True)
        
    with open('M2/Clase06/registros_henry.sql', 'r') as sql_file:
      queries = sql_file.read().split(';')

      for query in queries:
        if query.strip():
          result_iterator = cursor.execute(query, multi=True)
          for res in result_iterator:
            print("Running query: ", res)  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows" )

        # result_iterator = cursor.execute(sql_file.read(), multi=True)      

    connection.commit()
    cursor.close()
    connection.close()


    print("Laptop Table created successfully ")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

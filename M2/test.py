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
    
    with open('M2/homework5.sql', 'r') as sql_file:
        result_iterator = cursor.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            print("Running query: ", res)  # Will print out a short representation of the query
            print(f"Affected {res.rowcount} rows" )

    connection.commit()
    cursor.close()
    connection.close()
    
    print("Laptop Table created successfully ")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
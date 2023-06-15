import mysql.connector
import csv
import requests
import pandas as pd
from mysql.connector import Error

CSV_URL = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ente-de-turismo/oferta-establecimientos-gastronomicos/oferta_gastronomica.csv'

download = requests.get(CSV_URL)
decoded_content = download.content.decode('utf-8')
file = list(csv.reader(decoded_content.splitlines(), delimiter=','))
cols = file[0]
del(file[0])
df = pd.DataFrame(file, columns=cols).drop_duplicates(subset=['id'])

try:
  connection = mysql.connector.connect(host='localhost',
                                        database='henry',
                                        user='root',
                                        password='password'              
                                        )                                   

  cursor = connection.cursor()
  groups = [df[i:i+100] for i in range(0, len(df), 100)]

  cursor.execute("TRUNCATE TABLE locales")
  for group in groups:
    query = 'INSERT INTO locales(nombre, categoria, direccion, barrio, comuna) VALUES'
    values = []
    for _, row in group.iterrows():
        values.append(f'''(
          "{row["nombre"]}",
          "{row["categoria"]}",
          "{row["direccion_completa"]}",
          "{row["barrio"]}",
          "{row["comuna"]}")
          ''')
    
    query += ', '.join(values)
    result_iterator = cursor.execute(query, multi=True)
    for res in result_iterator:
      print("Running query: ", res) 
      print(f"Affected {res.rowcount} rows" )

  cursor.close()
  connection.commit()
  connection.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()


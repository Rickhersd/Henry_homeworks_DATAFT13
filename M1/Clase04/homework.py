# A partir del CSV hospitales2.csv, generar un archivo CSV de salida, que contenga los siguientes campos en este orden:
# latitude
# longitude
# name
# label
# Con los correspondientes datos extraídos del CSV original, el campo name tiene que corresponder con la dirección del hospital, y el campo label con el nombre del hospital.

import pandas as pd

#El metodo loads de shapely servirá para extraer puntos geográficos (WKT) del .csv
from shapely.wkt import loads

file = pd.read_csv('./M1/Clase04/hospitales2.csv')
df = pd.DataFrame(file)

datos_dict = {
  'latitude': df['WKT'].apply(lambda x: loads(x).x), 
  'longitude': df['WKT'].apply(lambda x: loads(x).y), 
  'name': df['DOM_NORMA'], 
  'label': df['NOM_MAP']
}

file.close()

pd.DataFrame(datos_dict).to_csv('./M1/Clase04/salida_hospitales.csv', index=False)

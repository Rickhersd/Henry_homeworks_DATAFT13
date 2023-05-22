# 1. Considere el siguiente areglo que contiene la altura de un grupo de estudiantes de Henry y cálcule:

import numpy as np
import math 
import matplotlib.pyplot as plt
import pandas as pd

muestra = np.array( [[1.85, 1.8, 1.8 , 1.8],
                     [1.73,  1.7, 1.75, 1.76],
                     [ 1.65, 1.69,  1.67 ,  1.6],
                     [1.54,  1.57, 1.58, 1.59],
                     [ 1.4 , 1.42,  1.45, 1.48]]) 

def to_list(matriz):
    return [val for row in matriz for val in row]

def media(list):
    return sum(list) / len(list)

def mediana(list):

    if (len(list) % 2 == 0):
        num_1 = list[int(len(list) / 2)]
        num_2 = list[int((len(list) / 2) - 1)]
        return (num_1 + num_2) / 2
    
    if (len(list) % 2 == 1):
        return list[math.ceil(len(list) / 2)]
    
def moda(lista):
    dict = {}
    moda, max_count = [], 0
    for n in lista:
        if dict.get(n) == None :
            dict[n] = 1
            if max_count == 0: max_count = 1
            continue
        dict[n] += 1
        if dict[n] > max_count: 
            max_count = dict[n]

    for x in dict:
        if dict[x] == max_count:
            moda.append(x)
    
    return moda

def varianza(datos:list):
    media_general = media(datos)
    return sum([(val - media_general) ** 2 for val in datos ]) / (len(datos) - 1)

def desvio_estandar(datos: list):
    return math.sqrt(varianza(datos))

print(media(to_list(muestra)))
print(mediana(to_list(muestra)))
print(moda(to_list(muestra)))
print(varianza(to_list(muestra)))
print(desvio_estandar(to_list(muestra)))

# 2. Convierta el arreglo en una lista y realice un Histograma de 5 intervalos. ¿Tiene distribución normal?.

plt.hist(to_list(muestra), bins=5, edgecolor='black', linewidth=1.2, alpha=0.7)
plt.xlabel('Altura')
plt.ylabel('Numero de estudiantes')
plt.title('Histograma de cinco intervalos')

plt.tight_layout()
# plt.show()

# 3. Utilizando pandas describa el dataframe.

df = pd.DataFrame(muestra, index = range(1,6), columns = ['col1', 'col2','col3','col4'])
print(df.describe())

# 4. Con los siguientes datos construye un df y un array que permitan describir adecuadamente la muestra.

ingreso_en_miles = [10.5, 6.8, 20.7, 18.2, 8.6, 25.8, 22.2, 5.9, 7.6, 11.8]
years_de_estudio = [17,18,21,16,16,21,16,14,18,18]

arr = np.array([[ingreso_en_miles[x], years_de_estudio[x]] for x in range(0, len(ingreso_en_miles))])
df = pd.DataFrame(arr, index = range(1,11), columns=['ingreso en Miles', 'Años de estudio' ])

print(arr)
print(df)

# 'Ingreso en miles' : 10.5	6.8	20.7	18.2	8.6	25.8	22.2	5.9	7.6	11.8 
# 'Años de estudio': 17	18	21	16	16	21	16	14	18	18 <br>

# 5. Realice un histograma de 6 secciones para 'Ingreso en miles' y 'Años de estudio'.

plt.hist(df['ingreso en Miles'], bins=5, edgecolor='black')
plt.xlabel('Ingreso en miles')
plt.ylabel('Frecuencia')
plt.title('Histograma de Ingresos')
# plt.show()

plt.hist(years_de_estudio, bins=6, edgecolor='black')
plt.xlabel('Years de estudio')
plt.ylabel('Frecuencia')
plt.title('Histograma de Years de Estudio')
# plt.show()

# 6. Cálcula la media de 'Ingreso en miles' (df) utilizando pandas.

print(df['ingreso en Miles'].mean())

# 7. Cálcula la media de 'Ingreso en miles' (array) utilizando numpy.

print(arr[0][:].mean())

# 8. Agregue los siguientes valores extremos al df [ 50, 35 ], [ 120, 30 ]. ¿En cuanto vario la media?, ¿Qué conclusiones obtiene de este resultado sobre la media?.

df.loc[len(df)] = [ 50, 35 ]
df.loc[len(df) + 1] = [ 120, 30 ]

print(df['ingreso en Miles'].mean())
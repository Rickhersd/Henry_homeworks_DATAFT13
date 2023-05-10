import numpy as np

# Ejercicio 2
# 2.1 Escribir un arreglo con números enteros del 0 al 9. Pista: arange
# 2.2 Escribir un arreglo con 100 números equiespaciados del 0 al 9. Pista: linspace

array = np.arange(0, 10)
print('Ejercicio 2.1, Respuesta: ', array, '\n')

array = np.linspace(0, 9, 100)
print('Ejercicio 2.2, Respuesta: \n\n',array, '\n')

# Ejercicio 3:
# Escribir un arreglo con números enteros del 10 al 100 y seleccionar aquellos que son divisibles por 3<br>
# Pista: mask

# Aqui una mascara es un filtro para los arreglos. Numpy tiene un modulo especial para eso ".ma", y este incluye infinidad de metodos 
# para filtrar arreglos.
array = np.arange(10, 101)
masked_array = np.ma.masked_where(array % 3 != 0, array)
print('Ejercicio 3, Respuesta: \n\n', masked_array, '\n')

# Tambien se le puede pasar directamente una mascara al array dentro de la llaves de la siguiente forma:
masked_array = array[(array % 3) == 0]
print('Solucion 2, Respuesta: \n\n', masked_array, '\n')

# Ejercicio 4:
# Crear un arreglo de ceros de `shape` (5,10).
# Reemplazar la segunda y cuarta fila con unos
# Reemplazar la tercera y octava columna con dos (2).

shape_array = np.zeros([5, 10], dtype = int)
print('Ejercicio 4, \n\n Arreglo inicial \n', shape_array, '\n')

# Esta sintaxis se interpreta asi: estamos tomando unicamente las columnas 1 y 3 del arreglo bidimensional, y esto nos devuelve dos arreglos.
# y al pasarle como segundo parametro :, le estamos indicando que queremos tomar todos los elementos de esos arreglos. Ya con esto, podemos
# hacer el cambio.
shape_array[[1, 3], :] = 1

# El metodo transpose devuelve la matriz transpuesta, es decir, invierte la matriz y las filas
# se vuelven columnas y las columnas se vuelven filas. De esta manera, podemos trabajar con el arreglo facilmente.
# Nota: esto no muta el arreglo, por lo que al hacer el cambio, este seguira en sus
# dimensiones iniciales tras terminar la linea de codigo
shape_array.transpose()[[2,7], :] = 2
print('Arreglo final: respuesta \n', shape_array)
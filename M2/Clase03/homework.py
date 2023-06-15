# 1. Suponga dos eventos, A y B, y que P(A) = 0.50, P(B) = 0.60 y P(A ∩ B) = 0.40.<br>
# - a. Halle P(A | B).


print(0.4 / 0.6 )

# - b. Halle P(B | A).

print(0.4 / 0.5 ) 

# - c. ¿A y B son independientes? ¿Por qué sí o por qué no?

"Son dependientes"

# 2. Suponga dos eventos, A y B, que son mutuamente excluyentes. Admita, además, que P(A) = 0.30 y P(B) = 0.40.<br>
# - a. Obtenga P(A ∩ B). ¿Existe intersección entre los dos conjuntos?.

'la probabilidad es 0 por que no hay interseccion'

# - b. Calcule P(A | B).

print(0.30)

# - c. Un estudiante de estadística argumenta que los conceptos de eventos mutuamente excluyentes y eventos independientes son en realidad lo mismo y que si los eventos son mutuamente excluyentes deben ser también independientes. ¿Está usted de acuerdo? Use la información sobre las probabilidades para justificar su respuesta.

'se equivoca, por dos eventos mutuamente exclyentens tambien pueden ser dependientes'

# Dada la siguiente tabla:<br>
# ![Sucesos](../_src/assets/sucesos.PNG)<br>


# 3. Si en la concesionaria se seleccionan dos ventas con reposición (Los sucesos son independientes.). Hallar la probabilidad de que las ventas sean:<br>
 
#   - a. La primera de un comprador de “menos de 40 años” y la segunda de uno de "entre 40 y 50 años". 

print(30/80 * 34/80)
  
#   - b. las dos sean de autos "nacionales".

print(50/80**2)

# 4. Si la selección de las dos ventas se realiza sin reposición. Hallar la probabilidad de que las ventas sean:<br>
#   Los sucesos son condicionales.

#  - a. la primera de un comprador de “menos de 40 años” y la segunda de uno de "entre 40 y 50 años".
print((30/80) * (34/79))

#  - b. las dos sean de autos "nacionales".
print(50/80 * 50/79,2)

# 5. Si la selección de las dos ventas se realiza sin reposición. Hallar la probabilidad de que las ventas sean:<br>
#   Los sucesos son condicionales.
  
#  - a. De un comprador de “menos de 40 años” y de uno de "entre 40 y 50 años". Sin importar el orden.

print((30/80) * (34/79) + (34/80) * (30/79))

#  6. Debido al aumento de los costos de los seguros, en un país 43 millones de personas, hay personas que no cuentan con un seguro médico. En la tabla siguiente se muestran datos muestrales representativos de la cantidad de personas que cuentan con seguro médico:<br>
#  ![Seguro](../_src/assets/seguro.PNG)

# - a. Con estos datos elabore una tabla de probabilidad conjunta y úsela para responder las preguntas restantes.

import pandas as pd

data = dict( yes =[750, 950], no=[170, 130 ])
df = pd.DataFrame(data, index=['18 a 34', '35 0 mayor'])
print(df)

# - b. ¿Qué indican las probabilidades marginales acerca de la edad de la población?



# - c. ¿Cuál es la probabilidad de que una persona tomada en forma aleatoria no tenga seguro médico?

total_poblacion = sum(df.sum())
print(total)

# - d. Si la persona tiene entre 18 y 34 años, ¿cuál es la probabilidad de que no tenga seguro médico?



# - e. Si la persona tiene 35 años o más ¿cuál es la probabilidad de que no tenga seguro médico?
# - f. Si la persona no tiene seguro médico, ¿cuál es la probabilidad de que tenga entre 18 y 34 años?


import math 

# 1. Lanza una moneda al aire 10 veces, ¿cuantos resultados posibles forman parte del espacio muestral?.

print(2**10)

# 2. En un aeropuerto se tiene a 10 pasajeros esperando en la sala de preembarque, la polícia debe controlar a 3 de ellos. ¿Cuantas combinaciones posibles se pueden obtener?.

combinaciones = 3
elementos = 10

print(math.factorial(elementos)/(math.factorial(combinaciones)*(math.factorial(elementos-combinaciones))))

# 3. La Agencia Nacional de Seguridad Vial realizó una investigación para saber si los conductores de están usando sus cinturones de seguridad. Los datos muestrales fueron los siguientes:<br>
# Conductores que emplean el cinturón <br>

# ![Ejercicio](../_src/assets/ejercicio3.PNG)

# - a) ¿Qué metodo cree que se utilizo para asignar probabilidades?.
# - b) Construya un cuadro similar, pero con la asignación de probabilidades.
# - c) ¿Cuál sería el mejor método pára estimar la probabilidad de que en Estados Unidos un conductor lleve puesto el cinturón?.
# - d) Un año antes, la probabilidad en Argentina de que un conductor llevara puesto el cinturón era 0.75. El director de ANSV, se esperaba que la probabilidad llegara a 0.78. ¿Estará satisfecho con los resultados del estudio? (Utilizar tabla adjunta (![Ejercicio](../_src/assets/ejercicio3.PNG))
# - e) ¿Cuál es la probabilidad de que se use el cinturón en las distintas regiones del país? ¿En qué región se usa más el cinturón?(Utilizar misma tabla que el ejercicio anterior).

import pandas as pd
regiones = ['norte', 'noreste', 'sur', 'centro']
yes = [148, 162, 296, 252]
no = [52, 54, 74, 48]
data = dict( yes= yes, no = no)
df = pd.DataFrame( data,index=regiones)
df = df/(sum(df.sum()))
df.loc[5] = sum(df['yes']), sum(df['no'])
df.rename(index={5:'total'}, inplace=True)
df = df.assign(Total = df.yes + df.no)
print(df)

# 4. Crear una funcion que permita calcular a probabilidad de los siguientes eventos en un baraja de 52 cartas.<br>
# - Obtener una carta roja.<br>
# - Obtener una carta negra.<br>
# - Obtener una pica.<br>
# - Obtener un trébol.<br>
# - Obtener un corazón.<br>
# - Obtener un diamante.<br>

def prop(category):
    if category == 'roja' or category == 'negra':
        return 26 / 52
    if category in ['pica', 'diamante', 'trebol', 'corazon']:
        return 12 / 52
    return 'invalid value'

print(prop('roja'))
print(prop('diamante'))

# 5. La probabilidad de que salga un 7 o un 8 al seleccionar una carta de una baraja de las 52 cartas que contiene el mazo. 

print(8/52)

# 6. La probabilidad de tu país gane el mundial de fútbol.<br>

print(1/32) # asumiendo que todos los paises jueguen exactamente igual

# 7. Un experimento que tiene tres resultados es repetido 50 veces y se ve que E1 aparece 20 veces, E2 13 veces y E3 17 veces. Asigne probabilidades a los resultados.<br>

print('El:' + str(20/50))
print('El:' + str(13/50))
print('El:' + str(17/50))
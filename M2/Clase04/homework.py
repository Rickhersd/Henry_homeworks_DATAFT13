# 1. Considera el experimento que consiste en un empleado que arma un producto.

#   - a. Defina la variable aleatoria que represente el tiempo en minutos requerido para armar el producto.<br>



#   - b. ¿Qué valores toma la variable aleatoria?<br>



#   - c. ¿Es una variable aleatoria discreta o continua?<br>



# 2. Considera el experimento que consiste en lanzar una moneda dos veces.

#   - a. Enumere los resultados experimentales.

'resultados experimentales = 4 {CC, CS, SS, SC}'

from scipy import stats
from math import factorial

def funcion_binomial(k,n,p):
  num_exitos = factorial(n) 
  num_eventos = factorial (k) * factorial(n-k) 
  exitos_fracaso = pow(p,k) * pow(1-p,(n-k)) 

  binomial = (num_exitos / num_eventos) * exitos_fracaso

  return binomial

# print(stats.binom.pmf())
# print(funcion_binomial())


#   - b. Defina una variable aleatoria que represente el número de caras en los dos lanzamientos.

'P(X = 0)'

#   - c. Dé el valor que la variable aleatoria tomará en cada uno de los resultados experimentales.



#   - d. ¿Es una variable aleatoria discreta o continua?


# 3. Considera las decisiones de compra de los próximos tres clientes que lleguen a la tienda de ropa Martin Clothing Store. De acuerdo con la experiencia, el gerente de la tienda estima que la probabilidad de que un cliente realice una compra es 0.30.
#  
#   - a. Describa si cumple con las reglas para clasificarlo como un experimiento binomial.
#   - b. ¿Cuál es la probabilidad de que dos de los próximos tres clientes realicen una compra?

print(funcion_binomial(2, 3, 0.30))

#   - c. ¿Cuál es la probabilidad de que cuatro de los próximos diez clientes realicen una compra?

print(funcion_binomial(4, 10, 0.30))

# 4.  A la oficina de reservaciones de una aerolínea regional llegan 48 llamadas por hora.

#DISTRIBUCIÓN DE POISSON
def probabilidad_poisson(lamba_np,x):
    probabilidad = (pow(2.71,-lamba_np) * pow(lamba_np,x))/factorial(x)
    return probabilidad

# - a. Calcule la probabilidad de recibir cinco llamadas en un lapso de 5 minutos.

print(probabilidad_poisson(((48/60) * 5), 5))

# - b. Estime la probabilidad de recibir exactamente 10 llamadas en un lapso de 15 minutos.

print(probabilidad_poisson(((48*15/60)), 10))

# - c. Suponga que no hay ninguna llamada en espera. Si el agente de viajes necesitará 5 minutos para la llamada que está atendiendo, ¿cuántas llamadas habrá en espera para cuando él termine? ¿Cuál es la probabilidad de que no haya ninguna llamada en espera?

print((48/60) * 5)
print(probabilidad_poisson(((48/60) * 5), 0))

# - d. Si en este momento no hay ninguna llamada, ¿cuál es la probabilidad de que el agente de viajes pueda tomar 3 minutos de descanso sin ser interrumpido por una llamada?

print(probabilidad_poisson(((48/60) * 3), 0) * 100)

# 5. En una encuesta realizada por Gallup Organization, se les preguntó a los interrogados, “Cuál es el deporte que prefieres ver”. Futbol y básquetbol ocuparon el primero y segundo lugar de preferencia (www.gallup.com, 3 de enero de 2004). Si en un grupo de 10 individuos, siete prefieren futbol y tres prefieren básquetbol. Se toma una muestra aleatoria de tres de estas personas.

def probabilidad_hipergeometrica(N,X,n,x):
  Xx = factorial(X)/(factorial(x)*factorial(X-x))
  NX_nx= factorial(N-X)/(factorial(n-x)*factorial((N-X)-(n-x)))
  Nn = factorial(N)/(factorial(n)*factorial(N-n))
  hipergeometrica = (Xx * NX_nx)/Nn

  return hipergeometrica

# - a. ¿Cuál es la probabilidad de que exactamente dos prefieren el futbol?

print(probabilidad_hipergeometrica(10, 7, 3, 2))


# - b. ¿De que la mayoría (ya sean dos o tres) prefiere el futbol?

prop1 = (probabilidad_hipergeometrica(10, 7, 3, 3))
prop2 = (probabilidad_hipergeometrica(10, 7, 3, 2))
print(prop1 + prop2 )


# 6. La probabilidad de que a un estudiante le guste este modulo es de 0.7 (en Henry somos optimistas), cual es la probabilidad de que les guste este módulo a 6 de los 10 estudiantes.<br>
 
print(funcion_binomial(6, 10, 0.7))

# 7. De todos los push a Git en un Henry Challenge, el 90% lo envía a término. Si se envían 9 ¿cuál es la probabilidad de que 7 lleguen a término?.<br>

print(funcion_binomial(7, 9, 0.90))

# 8. En relación con el enunciado anterior cálcule la probabilidad de que 7 o más lleguen a término.<br>

print(sum([funcion_binomial(x, 9, 0.90) for x in range(7, 10)]))

# Distribución de Poisson:<br>
# 9. La cantidad de alumnos promedio que se ausentan en un día de clases en la carrera de Data Science es de 10. Calcular cual es la probabilidad de que se ausenten 7 alumnos.<br>

print(probabilidad_poisson(10, 7))

# En una cola en el banco, llaman en promedio 2 personas cada 8 minutos. ¿Cuál es la probabilidad de que en esos 8 minutos llamen a más de 1 persona?


# 10. Cuando inicia una clase, los estudiantes ingresan a un ritmo de 5 estudiantes por minuto. Calcular cual es la probabilidad de que ingresen 7 estudiantes por minuto.<br>

print(probabilidad_poisson((5), 7))


print('check')

# Se tienen 4 canicas blancas y 4 canicas negras dentro de un frasco, luego de manera aleatoria se sacan dos canicas, una detrás de la otra. ¿Cuál es la probabilidad de que ambas sean de un mismo color?

print(round(probabilidad_poisson(2, 2), 2) )

from scipy.stats import poisson

lambd = 2  # Promedio de camiones que pasan cada 5 minutos

print(round(1 - poisson.cdf(1, lambd), 2 ))
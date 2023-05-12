# 1. Tarea
# Implementar un juego, que consista en apilar números enteros del 1 al 20, de forma aleatoria, para lo cual debe usarse una estructura de Pila. 
# Luego, el usuario debe elegir un número de veces en que se va a quitar elementos de la pila, los cuales, sumados entre sí, no deben superar el valor de 50.
# El usuario pierde si la suma supera ese valor. Si no lo supera, gana, pero su calificación será 10 menos el número elementos que falten quitar para todavía no superar 50.
# El programa debe informar si perdió, y si ganó, con qué calificación lo hizo.

# Consideraciones:
# a. Se puede usar la función input() para obtener una entrada de teclado.
# b. Se puede usar la el modulo random para obtener valores aleatorios.

import random

class juego_pilas():

  def __init__(self) -> None:
    self.__shuffled_numbers = []
    self.__picked_numbers = []
    self.__times = 0
    self.__calification = 10

  def start_game(self):
    self.__push_shuffled_numbers()
    self.__ask_times()

    while(self.__times):
      self.__pick_number()
      self.__times -= 1 

    self.__check_result()
    
  def __pick_number(self):
    picked_number = self.__shuffled_numbers.pop()
    self.__picked_numbers.append(picked_number)
    
  def __check_result(self):
    sum_result = sum(self.__picked_numbers)
    if (sum_result > 50):
      return print("Has perdido campeón")
      
    self.__calification = 10

    while (sum_result <= 50):

      if (self.__picked_numbers):
        sum_result += self.__picked_numbers.pop()
      else:
        sum_result += self.__shuffled_numbers.pop()

      if (sum_result <= 50):
        self.__calification -= 11

    return print('Has ganado con: ', self.__calification, ' puntos')

  def __ask_times(self):
    print('Cuantos numeros deseas tomar')
    self.__times = int(input())
  
  def __push_shuffled_numbers(self):
    number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
    random.shuffle(number_list)
    self.__shuffled_numbers.extend(number_list)
    
juego = juego_pilas()
juego.start_game()

# 2) Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
# Las opciones posibles son:
# Llenar la jarra de 3 litros
# Llenar la jarra de 5 litros
# Vaciar la jarra de 3 litros
# Vaciar la jarra de 5 litros
# Verter el contenido de la jarra de 3 litros en la de 5 litros
# Verter el contenido de la jarra de 5 litros en la de 3 litros

# Nota: Esto se hizo usando colas, ya que era el tema de la clase, 
# Pero en la práctica, es mucho más facil sólo usar números para medir los litros y tiene mas sentido.

class Jarra():

  def __init__ (self, max_capacity): 
    self.content = [] # variable para almacenar la cantidad de agua en litros, cada litro sera un item por cumplir que sea una cola 
    self.max_capacity = max_capacity # Limite de agua de la jarra.

  def verter(self, liters):  # metodo para verter toda el agua, liters indica cuando agua sera vaciada
    while(liters): # Por cada iteracion se vertira un litro.
      if not len(self.content): # Esta condicion evalua que haya agua que vertir. En caso de que la cantidad de entrada sea mayor que la posee internamnete, retorna para evitar errores.
        return
      self.content.pop(0)
      liters -= 1

  def llenar(self, liters): # Metodo para llenar la jarra, liters indica cuanto se llenara
    while(liters):
      if (len(self.content) == self.max_capacity): # condicion para evitar que la jarra se desborde
        return
      self.content.append(1) 
      liters -= 1

  def get_espacio_vacio(self): # Esto devuelve cuanto espacio vacio hay dentro
    return self.max_capacity - len(self.content)
  
  def get_litros_llenados(self): # Esto devleve cuanta agua hay dentro
    return len(self.content)
   
    
class Juego_jarras():

  def __init__(self):
    self.jarra_cinco = Jarra(5) # Como son dos jarras, creados dos intacias con diferentes capacidades maximas
    self.jarra_tres = Jarra(3)

  def start_game(self):

    while(True): # le pedimos al usuario que escoja una opcion. las cuales fueron dadas en el encunciado
      print('Que deseas hacer')
      print ("1. Llenar la jarra 3 de 3 litros")
      print ("2. Llenar la jarra 5 de 5 litros")
      print ("3. Vaciar la jarra 3 de 3 litros")
      print ("4. Vaciar la jarra 5 de 4 litros")
      print ("5. Verter el contenido de la jarra de 3 litros en la de 5 litros")
      print ("6. Verter el contenido de la jarra de 5 litros en la de 3 litros")

      opcion = int(input()) # le pedimos que ingrese el valor. Esto arrojará error si no es Int, pero no me quise alargar mucho

      # Evaluamos lo que pidio el usuario. Cada accion esta relacionada con las opciones de arriba
      if opcion == 1:
        self.jarra_tres.llenar(3)
      elif opcion == 2:
        self.jarra_cinco.llenar(5)
      elif opcion == 3:
        self.jarra_tres.verter(3)
      elif opcion == 4:
        self.jarra_cinco.verter(5)
      elif opcion == 5:
        self.intercambiar_liquidos(self.jarra_tres, self.jarra_cinco) # Este metodo es interno de la clase juego_jarras
      elif opcion == 6:
        self.intercambiar_liquidos(self.jarra_cinco, self.jarra_tres)
      else:
        print ("Elige una opción válida")
    
      print('En jarra de 3 litros hay ', self.jarra_tres.get_litros_llenados(), ' litros')
      print('En jarra de 5 litros hay', self.jarra_cinco.get_litros_llenados(), ' litros\n')

      if self.jarra_cinco.get_litros_llenados() == 4:
        print('Lo has conseguido')
        return

  # Esta funcion se encarga de intercambiar liquidos, y para ellos recibe dos Objetos Jarras. La sintaxis del : Jarra es un tipado datos, y se hace para indicar que tipo de datos deben entrar en la funcion. En este caso dos jarras
  def intercambiar_liquidos(self, jarra_origen: Jarra, jarra_destino: Jarra): # 
    litros_jarra_origen = jarra_origen.get_litros_llenados() # Obtenemos cuantos ligros hay en una jarra
    litros_avalibles_jarra_destino = jarra_destino.get_espacio_vacio() # Obtemos cuantos litros permite la segunda

    cantidad = 0

    # Para evitar problemas con las cantidades, nos aseguramos que la jarra de destino tenga capacidad para vertir la de origen.
    # Si la jarra de destino solo tiene espacio para dos litros, pero la otra tiene cinco. Solo vertiremos dos en la primera y la segunda se quedaria en tres
    # Caso contrario, si la origen tiene esta tres y la segunda tiene uno y admite hasta cinco. La de origen perdera sus tres y la destino se llenaría hasta cuatro.    
    if litros_jarra_origen > litros_avalibles_jarra_destino:
      cantidad = litros_avalibles_jarra_destino
    else:
      cantidad = litros_jarra_origen
    
    jarra_origen.verter(cantidad) # Vaciamos la de origen
    jarra_destino.llenar(cantidad) # Llenamos la de destino

juego_jarra = Juego_jarras()
juego_jarra.start_game()
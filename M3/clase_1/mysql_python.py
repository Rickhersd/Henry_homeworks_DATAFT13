#Material adicional
#Mostrar conexión entre python y MySql
import mysql.connector
from mysql.connector import Error

# 1. Crear un procedimiento que recibe como parametro una fecha y muestre la cantidad de ordenes ingresadas en esa fecha.<br>
# 2. Crear una función que calcule el valor nominal de un margen bruto determinado por el usuario a partir del precio de lista de los productos.<br>
# 3. Obtner un listado de productos en orden alfabético que muestre cuál debería ser el valor de precio de lista, si se quiere aplicar un margen bruto del 20%, utilizando la función creada en el punto 2, sobre el campo StandardCost. Mostrando tambien el campo ListPrice y la diferencia con el nuevo campo creado.<br>
# 4. Crear un procedimiento que reciba como parámetro una fecha desde y una hasta, y muestre un listado con los Id de los diez Clientes que más costo de transporte tienen entre esas fechas (campo Freight).<br>
# 5. Crear un procedimiento que permita realizar la insercción de datos en la tabla shipmethod.<br>

try:
  connection = mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='password')
  
  def get_orders(date):
    query = f'''
      DELIMITER // 

      DROP PROCEDURE IF EXISTS GET_ORDERS_BY_DATE //
      CREATE PROCEDURE IF NOT EXISTS GET_ORDERS_BY_DATE(IN FECHA date)
      BEGIN
        SELECT COUNT(*)
        FROM salesorderheader
        WHERE date(OrderDate) = date(FECHA);
      END //

      CALL GET_ORDERS_BY_DATE('2002-01-01') //
    '''

  def get_orders(date):
    query = f'''
      DROP PROCEDURE IF EXISTS INSERT_DATA //
      CREATE PROCEDURE IF NOT EXISTS INSERT_DATA(IN new_name varchar(50), IN base double,IN rate double)
      BEGIN
        INSERT INTO shipmethod(Name, ShipBase, ShipRate, ModifiedDate) 
        Values(new_name, base, rate, Now());
      END //
    '''


  def get_orders(date):
    query = f'''
      DROP FUNCTION IF EXISTS CALC_MARGEN //
      CREATE FUNCTION IF NOT EXISTS CALC_MARGEN(PRICE DECIMAL(15, 3), MARGEN DECIMAL(15,3)) RETURNS DECIMAL(15, 3)
      BEGIN
        DECLARE VALUE DECIMAL(15, 3);
        SET VALUE = PRICE * MARGEN;
        RETURN VALUE;
      END //
    '''

  def get_orders(date):
    query = f'''
      DROP PROCEDURE IF EXISTS CLIENT_LIST //
      CREATE PROCEDURE IF NOT EXISTS CLIENT_LIET(IN DATE_FROM DATE, IN DATE_TO DATE)
      BEGIN
        SELECT CustomerID, sum(Freight) as total 
        from salesorderheader
        WHERE date(OrderDate) between DATE_FROM and  DATE_TO
        GROUP BY CustomerID
        ORDER BY total desc 
        LIMIT 10
      END //
    '''

  def get_list(date):
    query = f'''
      Select ProductID, Name, ListPrice, CALC_MARGEN(StandardCost, 1.2) as Propuesta, ListPrice - CALC_MARGEN(StandardCost, 1.2) as Diferencia from product //
    '''

  cursor = connection.cursor()

  connection.commit()
  cursor.close()
  connection.close()

except Error as e:
  print("Error while connecting to MySQL", e)

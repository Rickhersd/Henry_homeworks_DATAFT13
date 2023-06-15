DELIMITER //

-- ejercicio 1
DROP PROCEDURE IF EXISTS GET_ORDERS_BY_DATE //
CREATE PROCEDURE IF NOT EXISTS GET_ORDERS_BY_DATE(IN FECHA date)
BEGIN
SELECT COUNT(*)
FROM salesorderheader
WHERE date(OrderDate) = date(FECHA);
END //

-- ejercicio 2
DROP FUNCTION IF EXISTS CALC_MARGEN //
CREATE FUNCTION IF NOT EXISTS CALC_MARGEN(PRICE DECIMAL(15, 3), MARGEN DECIMAL(15,3)) RETURNS DECIMAL(15, 3)
BEGIN
    DECLARE VALUE DECIMAL(15, 3);
    SET VALUE = PRICE * MARGEN;
    RETURN VALUE;
END //

-- ejercicio 3
Select ProductID, Name, ListPrice, CALC_MARGEN(StandardCost, 1.2) as Propuesta, ListPrice - CALC_MARGEN(StandardCost, 1.2) as Diferencia 
from product //

-- ejercicio 4
DROP PROCEDURE IF EXISTS CLIENT_LIST //
CREATE PROCEDURE IF NOT EXISTS CLIENT_LIST(IN DATE_FROM DATE, IN DATE_TO DATE)
BEGIN
    SELECT CustomerID, sum(Freight) as total 
    from salesorderheader
    WHERE date(OrderDate) between DATE_FROM and  DATE_TO
    GROUP BY CustomerID
    ORDER BY total desc 
    LIMIT 10;
END //

-- ejercicio 5
DROP PROCEDURE IF EXISTS INSERT_DATA //
CREATE PROCEDURE IF NOT EXISTS INSERT_DATA(IN new_name varchar(50), IN base double,IN rate double)
BEGIN
    INSERT INTO shipmethod(Name, ShipBase, ShipRate, ModifiedDate) 
    Values(new_name, base, rate, Now());
END //
  
DELIMITER ;
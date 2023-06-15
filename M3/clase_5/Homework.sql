-- ### Limpieza, Valores faltantes

-- 6) Normalizar los nombres de los campos y colocar el tipo de dato adecuado para cada uno en cada una de las tablas. Descartar columnas que consideres que no tienen relevancia.

/* Corrigiendo los ID*/

ALTER TABLE cliente CHANGE ID IdCliente INT(10) NOT NULL AUTO_INCREMENT;
ALTER TABLE empleado CHANGE IDEmpleado IdEmpleado INT(10) NOT NULL AUTO_INCREMENT;
ALTER TABLE cliente CHANGE ID IdCliente INT(10) NOT NULL AUTO_INCREMENT;
ALTER TABLE cliente CHANGE ID  INT(10) NOT NULL AUTO_INCREMENT;
ALTER TABLE cliente DROP COLUMN col10;


-- 7) Buscar valores faltantes y campos inconsistentes en las tablas sucursal, proveedor, empleado y cliente. De encontrarlos, deberás corregirlos o desestimarlos. Propone y realiza una acción correctiva sobre ese problema.



-- 8) Utilizar la funcion provista 'UC_Words' (Homework_Utiles.sql) para modificar a letra capital los campos que contengan descripciones para todas las tablas.


-- 9) Chequear la consistencia de los campos precio y cantidad de la tabla de ventas.


-- 10) Chequear que no haya claves duplicadas, y de encontrarla en alguna de las tablas, proponer una solución.

-- ### Normalización

-- 10) Generar dos nuevas tablas a partir de la tabla 'empelado' que contengan las entidades Cargo y Sector.


-- 11) Generar una nueva tabla a partir de la tabla 'producto' que contenga la entidad Tipo de Producto.

-- 7. Utilizar la funcion provista 'UC_Words' (Homework_Utiles.sql) para modificar a letra capital los campos que contengan descripciones para todas las tablas.

-- 8. Utilizar el procedimiento provisto 'Llenar_Calendario' (Homework_Utiles.sql) para poblar la tabla de calendario.
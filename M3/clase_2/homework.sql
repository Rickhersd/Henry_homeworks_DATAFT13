-- 1. Obtener un listado contactos que hayan ordenado productos de la subcategoría "Mountain Bikes", entre los años 2000 y 2003, cuyo método de envío sea "CARGO TRANSPORT 5"

SELECT 
    DISTINCT concat(contact.LastName, ' ', contact.FirstName) as nombre
FROM salesorderheader as orderHead

LEFT JOIN contact 
    On orderHead.ContactID = contact.ContactID

LEFT JOIN shipmethod 
    On orderHead.ShipMethodID = shipmethod.ShipMethodID

LEFT JOIN salesorderdetail as orderDtl
    ON orderHead.SalesOrderID = orderDtl.SalesOrderID

LEFT JOIN product as prod
    On orderDtl.ProductID = prod.ProductID

LEFT JOIN productsubcategory as prodSub 
    ON prod.ProductSubcategoryID = prodSub.ProductSubcategoryID

where prodSub.Name = 'Mountain Bikes' 
and shipmethod.Name = 'CARGO TRANSPORT 5'
and year(orderHead.OrderDate) BETWEEN 2002 and 2003;

SELECT 
    DISTINCT concat(contact.LastName, ' ', contact.FirstName) as nombre
FROM salesorderheader as orderHead

INNER JOIN contact 
    On contact.ContactID =orderHead.ContactID 

INNER JOIN shipmethod 
    On orderHead.ShipMethodID = shipmethod.ShipMethodID

INNER JOIN salesorderdetail as orderDtl
    ON orderHead.SalesOrderID = orderDtl.SalesOrderID

INNER JOIN product as prod
    On orderDtl.ProductID = prod.ProductID

INNER JOIN productsubcategory as prodSub 
    ON prod.ProductSubcategoryID = prodSub.ProductSubcategoryID

where prodSub.Name = 'Mountain Bikes' 
and shipmethod.Name = 'CARGO TRANSPORT 5'
and year(orderHead.OrderDate) BETWEEN 2000 and 2003

Order By nombre;

-- 2. Obtener un listado contactos que hayan ordenado productos de la subcategoría "Mountain Bikes", entre los años 2000 y 2003 con la cantidad de productos adquiridos y ordenado por este valor, de forma descendente

SELECT DISTINCT
    concat(contact.FirstName, ' ',contact.LastName )  as Nombre,
    Sum(orderDtl.OrderQty) as cantidad
FROM salesorderheader as orderHead

LEFT JOIN contact 
    On orderHead.ContactID = contact.ContactID

LEFT JOIN salesorderdetail as orderDtl
    ON orderHead.SalesOrderID = orderDtl.SalesOrderID

LEFT JOIN product as prod
    On orderDtl.ProductID = prod.ProductID

LEFT JOIN productsubcategory as prodSub 
    ON prod.ProductSubcategoryID = prodSub.ProductSubcategoryID

where prodSub.Name = 'Mountain Bikes' 
    and year(orderHead.OrderDate) BETWEEN 2002 and 2003

GROUP BY Nombre
ORDER BY Cantidad DESC;

SELECT c.LastName, c.FirstName, SUM(d.OrderQty) as Cantidad
FROM salesorderheader h
JOIN contact c
ON (h.ContactID = c.ContactID)
JOIN salesorderdetail d
ON (h.SalesOrderID = d.SalesOrderID)
JOIN product p
ON (d.ProductID = p.ProductID)
JOIN productsubcategory s
ON (p.ProductSubcategoryID = s.ProductCategoryID)
WHERE YEAR(h.OrderDate) BETWEEN 2002 AND 2003
AND s.Name = 'Mountain Bikes'
GROUP BY c.LastName, c.FirstName
ORDER BY Cantidad DESC;

SELECT c.LastName, c.FirstName, SUM(d.OrderQty) as Cantidad
FROM salesorderheader h
JOIN contact c
ON (h.ContactID = c.ContactID)
JOIN salesorderdetail d
ON (h.SalesOrderID = d.SalesOrderID)
JOIN product p
ON (d.ProductID = p.ProductID)
JOIN productsubcategory s
ON (p.ProductSubcategoryID = s.ProductCategoryID)
WHERE YEAR(h.OrderDate) BETWEEN 2000 AND 2003
AND s.Name = 'Mountain Bikes'
GROUP BY c.LastName, c.FirstName
ORDER BY Cantidad DESC;

-- 3. Obtener un listado de cual fue el volumen de compra (cantidad) por año y método de envío 

SELECT DISTINCT
    year(orderHead.OrderDate) as year_order, 
    shipmethod.Name as Metodo,
    Sum(orderDtl.OrderQty) as volumen
FROM salesorderheader as orderHead

INNER JOIN shipmethod 
    On orderHead.ShipMethodID = shipmethod.ShipMethodID

INNER JOIN salesorderdetail as orderDtl
    ON orderHead.SalesOrderID = orderDtl.SalesOrderID

GROUP BY year_order, Metodo;

-- 4. Obtener un listado por categoría de productos, con el valor total de ventas y productos vendidos.

SELECT DISTINCT
    prodcategory.Name as Categoria,
    round(Sum(orderDtl.LineTotal), 2) as Valor_total,
    Sum(orderDtl.OrderQty) as Cantidad_productos_vendidos

FROM salesorderheader as orderHead

LEFT JOIN shipmethod 
    On orderHead.ShipMethodID = shipmethod.ShipMethodID

LEFT JOIN salesorderdetail as orderDtl
    ON orderHead.SalesOrderID = orderDtl.SalesOrderID

LEFT JOIN product as prod
    On orderDtl.ProductID = prod.ProductID

LEFT JOIN productsubcategory as prodSub 
    ON prod.ProductSubcategoryID = prodSub.ProductSubcategoryID

LEFT JOIN productcategory as prodcategory 
    ON prodSub.ProductCategoryID = prodcategory.ProductCategoryID

GROUP BY Categoria;

-- 5. Obtener un listado por país (según la dirección de envío), con el valor total de ventas y productos vendidos, sólo para aquellos países donde se enviaron más de 15 mil productos

SELECT DISTINCT
    countryregion.Name as Pais,
    round(Sum(orderDtl.LineTotal), 2) as Valor_total,
    Sum(orderDtl.OrderQty) as Cantidad_productos_vendidos

FROM salesorderheader as orderHead

LEFT JOIN shipmethod 
    On orderHead.ShipMethodID = shipmethod.ShipMethodID

LEFT JOIN salesorderdetail as orderDtl
    ON orderHead.SalesOrderID = orderDtl.SalesOrderID

LEFT JOIN address
    On orderHead.ShipToAddressID  = address.AddressID

LEFT JOIN stateprovince
    On address.StateProvinceID  = stateprovince.StateProvinceID

LEFT JOIN countryregion
    On stateprovince.CountryRegionCode = countryregion.CountryRegionCode 

GROUP BY Pais
having Sum(orderDtl.OrderQty) > 15000;

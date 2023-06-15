DELETE FROM cohorte WHERE idCohorte in (1245, 1246) 

UPDATE cohorte
SET fechaInicio = '2022-05-16'
WHERE idCohorte = 1243;

UPDATE alumno
SET apellido = 'Ramirez '
Where idAlumno = 165;

SELECT nombre, fechaIngreso FROM alumno 
INNER JOIN cohorte on cohorte.idCohorte = alumno.idCohorte
WHERE idCohorte = 1243;

SELECT * FROM instructor 
INNER JOIN carrera on carrera.idCarrera = instructor.idCarrera
WHERE carrera.nombre = 'Full Stack Developer';

SELECT * FROM alumno WHERE idCohorte = 1235;

SELECT * FROM alumno WHERE idCohorte = 1235 AND YEAR(fechaIngreso) = 2019;

-- a. ¿Que campos permiten que se puedan acceder al nombre de la carrera?

-- el campo nombre de la tabla carrera

-- b. ¿Que tipo de ralación existe entre el nombre la tabla cohortes y alumnos?



-- c. ¿Proponga dos opciones para filtrar el listado solo por los alumnos que pertenecen a 'Full Stack Developer', utilizando LIKE y NOT LIKE?,¿Cual de las dos opciones es la manera correcta de hacerlo?, ¿Por que? 
 
-- d. ¿Proponga dos opciones para filtrar el listado solo por los alumnos que pertenecen a 'Full Stack Developer', utilizando " = " y " != "? ¿Cual de las dos opciones es la manera correcta de hacerlo?, ¿Por que? 
 
-- e. ¿Como emplearía el filtrado utilizando el campo idCarrera?


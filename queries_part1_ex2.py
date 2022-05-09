CREATE ROLE admin_uvg;

GRANT UPDATE, DELETE, SELECT
ON	asignaciones 
TO	admin_uvg;

CREATE USER user_campus_central PASSWORD '123';
CREATE USER user_campus_altiplano PASSWORD '456';

GRANT admin_uvg TO user_campus_central;
GRANT admin_uvg TO user_campus_altiplano;


SELECT	*
FROM	asignaciones;

SELECT *
FROM asignaciones;

--psycopg2.errors.InsufficientPrivilege: permiso denegado a la tabla asignaciones
CREATE ROLE admin_uvg;

GRANT UPDATE, DELETE 
ON	asignaciones 
TO	admin_uvg;

CREATE USER user_campus_central PASSWORD '123';
CREATE USER user_campus_altiplano PASSWORD '456';

GRANT admin_uvg TO user_campus_central;
GRANT admin_uvg TO user_campus_altiplano;
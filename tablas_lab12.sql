CREATE TABLE estudiantes (
	carnet 			VARCHAR ( 10 ),
	nombres 		VARCHAR ( 70 ) ,
	apellidos 		VARCHAR ( 70 ),
	correo 			VARCHAR ( 70 ),
	user_password	VARCHAR ( 70 )
);

DROP TABLE asignaciones;

CREATE TABLE cursos (
	codigo		VARCHAR ( 10 ),
	nombre		VARCHAR ( 70 ),
	creditos	INT
);

CREATE TABLE asignaciones (
	carnet_estudiante	VARCHAR ( 10 ),
	semestre			INT,
	codigo_curso		VARCHAR ( 10 ),
	year				INT,
	carnet_catedratico	VARCHAR ( 10 )
);

CREATE TABLE catedraticos (
	carnet VARCHAR ( 10 ),
	nombres VARCHAR ( 70 ) ,
	apellidos VARCHAR ( 70 )
);
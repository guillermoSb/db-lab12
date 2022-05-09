## Crear funcion para crear a usuario
## Crear funcion para que se asigne

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import make_dsn


def createUser(carnet, nombres, apellidos, mail, password):
    conn = psycopg2.connect("host=localhost dbname=lab12 user=postgres password=October19")  # Connect to the Database
    cur = conn.cursor()

    cur.execute("INSERT INTO estudiantes (carnet, nombres, apellidos, correo, user_password) \
                 VALUES (%s, %s, %s, %s, %s)", (carnet, nombres, apellidos, mail, password))

    query = sql.SQL("CREATE USER {0} \
                 WITH PASSWORD {1} \
                 VALID UNTIL '2022-05-09T22:25:17-06:00'").format(
                     sql.Identifier(mail),
                     sql.Literal(password),
    )
    cur.execute(query.as_string(conn))


    query2 = sql.SQL("GRANT      INSERT \
                 ON         asignaciones \
                 TO {0}").format(
                    sql.Identifier(mail)
                    )
    cur.execute(query2.as_string(conn))
    
    conn.commit()

def assignCourse(carnet, semestre, codigo_curso, year, mail, password, carnet_catedratico):
    dsn = make_dsn('host=localhost dbname=lab12', user=mail, password=password)
    conn = psycopg2.connect(dsn)

    cur = conn.cursor()

    cur.execute('INSERT INTO asignaciones (carnet_estudiante, semestre, codigo_curso, year, carnet_catedratico) \
                 VALUES (%s, %s, %s, %s, %s)', (carnet, semestre, codigo_curso, year, carnet_catedratico))
    conn.commit()

def updateAssignment(carnet, codigoCurso,semestre, mail, password):
    dsn = make_dsn('host=localhost dbname=lab12', user=mail, password=password)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute('UPDATE asignaciones SET semestre = %s\
                     WHERE carnet = %s AND codigo_curso = %s', (semestre, carnet, codigoCurso))
    conn.commit()

def menu():
    print('\n1. Crear cuenta')
    print('2. Asignarse a curso')
    print('3. Actualizar el semestre de una asignacion')
    print('4. Salir')

menu()
option = int(input('\nIngrese una opcion: '))

while option != 5:
    if option == 1:
        carnet = input("\nIngrese su numero de carnet: ")
        nombres = input("Ingrese sus nombres: ")
        apellidos = input("Ingrese sus apellidos: ")
        mail = input("Ingrese su correo: ")
        password = input("Ingrese una contraseña: ")
        createUser(carnet, nombres, apellidos, mail, password)
    elif option == 2:
        mail = input("\n Ingrese su correo: ")
        password = input("Ingrese su contrasenia: ")
        carnet = input("Ingrese su numero de carnet: ")
        semestre = input("Ingrese semestre: ")
        codigo_curso = input("Ingrese el codigo del curso: ")
        year = input("Ingrese el año: ")
        carnet_catedratico = input("Ingrese el carnet del catedratico: ")
        assignCourse(carnet, semestre, codigo_curso, year, mail, password, carnet_catedratico)
    elif option == 3:
        mail = input("Ingrese su correo: ")
        password = input("Ingrese su contrasenia: ")
        carnet = input("Ingrese el carnet del estudiante que desea actualizar: ")
        codigo_curso = input("Ingrese el codigo del curso de la asignacion que desea actualizar: ")
        semestre = input("Ingrese el nuevo numero de semestre para esta asignacion: ")
        updateAssignment(carnet, codigo_curso, semestre, mail, password)
    elif option == 4:
        print("Saliendo.")
        break;
    else:
        print('Opcion invalida')

    print()
    menu()
    option = int(input('\nIngrese una opcion: '))




#GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;



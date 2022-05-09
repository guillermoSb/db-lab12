import psycopg2
from psycopg2 import sql
from psycopg2.extensions import make_dsn


def updateAssignment(carnet, codigoCurso, semestre, mail, password):
    dsn = make_dsn('host=localhost dbname=lab12', user=mail, password=password)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute('UPDATE asignaciones \
                 SET semestre = %s\
                 WHERE carnet_estudiante = %s AND codigo_curso = %s', (semestre, carnet, codigoCurso))
    conn.commit()

def deleteAssigment(carnet, codigoCurso, mail, password):
    dsn = make_dsn('host=localhost dbname=lab12', user=mail, password=password)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute('DELETE FROM asignaciones \
                 WHERE carnet_estudiante = %s AND codigo_curso = %s', (carnet, codigoCurso))
    conn.commit()

def addAssigment(carnet, semestre, codigo_curso, year, mail, password, carnet_catedratico):
    dsn = make_dsn('host=localhost dbname=lab12', user=mail, password=password)
    conn = psycopg2.connect(dsn)

    cur = conn.cursor()

    cur.execute('INSERT INTO asignaciones (carnet_estudiante, semestre, codigo_curso, year, carnet_catedratico) \
                 VALUES (%s, %s, %s, %s, %s)', (carnet, semestre, codigo_curso, year, carnet_catedratico))
    conn.commit()

def menu():
    print('\n1. Modificar curso')
    print('2. Borrar curso')
    print('3. Ingresar asignacion')
    print('4. Salir')



menu()
option = int(input('\nIngrese una opcion: '))

while option != 5:
    if option == 1:
        optionAdmin = int(input('\nSeleccione un administrador\n1. Administrador Campus Central\n2. Administrador Campus Altiplano\n'))
        if optionAdmin == 1:
            username = 'user_campus_central'
            password = '123'
        elif optionAdmin == 2:
            username = 'user_campus_altiplano'
            password = '456'
        else:
            print('Opcion invalida')
            break;
        carnet = input("Ingrese el carnet del estudiante que desea actualizar: ")
        codigo_curso = input("Ingrese el codigo del curso de la asignacion que desea actualizar: ")
        semestre = input("Ingrese el nuevo numero de semestre para esta asignacion: ")
        updateAssignment(carnet, codigo_curso, semestre, username, password)
    elif option == 2:
        optionAdmin = input('Seleccione un administrador\n1. Administrador Campus Central\n2. Administrador Campus Altiplano')
        if optionAdmin == 1:
            username = 'user_campus_central'
            password = '123'
        elif optionAdmin == 2:
            username = 'user_campus_altiplano'
            password = '456'
        else:
            print('Opcion invalida')
        carnet = input("Ingrese el carnet del estudiante que desea actualizar: ")
        codigo_curso = input("Ingrese el codigo del curso de la asignacion que desea actualizar: ")
        deleteAssigment(carnet, codigo_curso, username, password)
    elif option == 3:
        optionAdmin = input('Seleccione un administrador\n1. Administrador Campus Central\n2. Administrador Campus Altiplano')
        if optionAdmin == 1:
            username = 'user_campus_central'
            password = '123'
        elif optionAdmin == 2:
            username = 'user_campus_altiplano'
            password = '456'
        else:
            print('Opcion invalida')
        carnet = input("Ingrese el carnet del estudiante que desea actualizar: ")
        codigo_curso = input("Ingrese el codigo del curso de la asignacion que desea actualizar: ")
        semestre = input("Ingrese el nuevo numero de semestre para esta asignacion: ")
        year = input("Ingrese el año de asignacion: ")
        carnet_catedratico = input("Ingrese el carnet del catedratico que imparte el curso: ")
        addAssigment(carnet, semestre, codigo_curso, year, username, password, carnet_catedratico)
    elif option == 4:
        print("Saliendo.")
        break;
    else:
        print('Opcion invalida')

    print()
    menu()
    option = int(input('\nIngrese una opcion: '))

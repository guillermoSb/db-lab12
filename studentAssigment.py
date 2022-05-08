## Crear funcion para crear a usuario
## Crear funcion para que se asigne

import psycopg2

def createUser(carnet, nombres, apellidos, mail, password):
    conn = psycopg2.connect("host=localhost dbname=lab12 user=postgres password=October19")  # Connect to the Database
    cur = conn.cursor()

    cur.execute("INSERT INTO estudiantes (carnet, nombres, apellidos, correo, user_password) \
                 VALUES (%s, %s, %s, %s, %s)", (carnet, nombres, apellidos, mail, password))

    cur.execute("CREATE USER %s \
                 WITH PASSWORD %s \
                 VALID UNTIL '2022-05-08T15:15:17-06:00';", (mail, password))

    cur.execute("GRANT      INSERT \
                 ON         asignaciones \
                 TO         %s';", (mail))

def assignCourse(carnet, semestre, codigo_curso, year, mail, password, carnet_catedratico):
    conn = psycopg2.connect("host=localhost dbname=lab12 user=%s password=%s", (mail, password))  
    cur = conn.cursor()

    cur.execute('INSERT INTO asignaciones (carnet_estudiante, semestre, codigo_curso, year, carnet_catedratico) \
                 VALUES (%s, %s, %s, %s, %s)', (carnet, semestre, codigo_curso, year, carnet_catedratico))


def menu():
    print('\n1. Crear cuenta')
    print('2. Asignarse a curso')
    print('3. Salir')

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
        mail = ("\n Ingrese su correo")
        password = input("Ingrese su contrasenia: ")
        carnet = input("Ingrese su numero de carnet: ")
        semestre = input("Ingrese semestre: ")
        codigo_curso = input("Ingrese el codigo del curso: ")
        year = input("Ingrese el año: ")
        carnet_catedratico = input("Ingrese el carnet del catedratico: ")
        assignCourse(carnet, semestre, codigo_curso, year, mail, password, carnet_catedratico)

    else:
        print('Opcion invalida')

    print()
    menu()
    option = int(input('\nIngrese una opcion: '))




#GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;



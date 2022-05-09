import psycopg2

conn = psycopg2.connect("host=localhost dbname=analysis user=postgres password=123456")  # Connect to the Database
cur = conn.cursor()  # Cursor used to perform database queries


carnet_estudiante = input("Ingrese el carnet: ")
semestre = input("Ingrese el semestre (1 o 2): ")
codigo_curso = input("Ingrese el codigo del curso: ")
year = input("Ingrese el año: ")
nota = input("Ingrese la nota: ")
carnet_catedratico = input("Ingrese el carnet del catedrático: ")


import psycopg2

conn = psycopg2.connect("dbname=lab11 user=postgres")  # Connect to the Database
cur = conn.cursor()  # Cursor used to perform database queries


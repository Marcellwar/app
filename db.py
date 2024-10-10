import psycopg2
from psycopg2 import OperationalError
import os

DATABASE_URL = os.getenv('DATABASE_URL')
def get_db_connection():
    try:
        # Conexión usando la URL de la base de datos
        conn = psycopg2.connect(DATABASE_URL)
        print("Conexión a PostgreSQL exitosa")
        return conn
    except OperationalError as e:
        print(f"La conexión a PostgreSQL falló: {e}")
        return None
import psycopg2
import os

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="inventario_tienda",
        user="postgres",
        password="admin123"
    )
    return conn

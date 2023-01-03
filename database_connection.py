"""Conexión con la base de datos

Database connection
"""

import sqlite3
from sqlite3 import Error


def connect():
    try:
        connection = sqlite3.connect('contact_book_database.db')
        return connection
    except Error:
        print('Error de conexión')

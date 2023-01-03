'''Creacion de tablas de la base de datos

Create database tables
'''


tables = [
    '''CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(45) NOT NULL,
        apellido_p TEXT(45) NOT NULL,
        apellido_m TEXT(45),
        telefono TEXT(10) DEFAULT '',
        email TEXT(45) DEFAULT '') 
        ''',
]


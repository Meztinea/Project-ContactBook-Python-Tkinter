from database_connection import connect
connection = connect()

## Funciones revisadas y necesarias

# Crea todas las tablas que se encuentran dentro del archivo crear_tablas
# Recibe una lista de sentencias para crear tablas
def crear_tablas_sql(connection, lista_sentencias):
    for sentencia in lista_sentencias:
        connection = connect()
        sql_statement_1(connection, sentencia)


# Retorna una lista de tuplas, cada tupla es un contacto - Concatena el nombre y apellidos de los contactos
def traer_contactos(connection):
    statement = '''SELECT id, nombre || ' ' || apellido_p || ' ' || apellido_m, telefono, email from contactos '''
    datos = sql_statement_3(connection, statement)
    return datos


# Recibe el id del contacto seleccionado para editar
# Retorna todos los datos del contacto seleccionado
def traer_contacto_id_editar(connection, id_contacto):
    statement = '''SELECT * from contactos WHERE id = ''' + str(id_contacto)
    contacto = sql_statement_3(connection, statement)
    return contacto












# Use for CREATE TABLE --
def sql_statement_1(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    connection.commit()
    # connection.close()


# Use for INSERT INTO -- UPDATE -- DELETE
def sql_statement_2(connection, statement, data):
    cursor = connection.cursor()
    cursor.execute(statement, data)
    connection.commit()
    # connection.close()


# Use for SELECT --
def sql_statement_3(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    data = cursor.fetchall()
    # cursor.close()
    return data




def traer_contacto_id(connection, id_contacto):
    statement = '''SELECT * from contactos WHERE id = ''' + str(id_contacto)
    datos = sql_statement_3(connection, statement)
    contacto = (datos[0][0], datos[0][1] + ' ' + datos[0][2] + ' ' + datos[0][3], datos[0][4])
    return contacto




def actualizar_contacto(connection, nombre, apellido_p, apellido_m, telefono, email, id, ):
    statement = 'UPDATE contactos SET nombre = ?, apellido_p = ?, apellido_m = ?, telefono = ?, email = ? WHERE id = ?'
    data = (nombre, apellido_p, apellido_m, telefono, email, id)
    sql_statement_2(connection, statement, data)


def agregar_contacto(connection, nombre, apellido_paterno, apellido_materno, telefono, email):
    statement = 'INSERT INTO contactos (nombre, apellido_p, apellido_m, telefono, email) VALUES(?, ?, ?, ?, ?)'
    data = (nombre, apellido_paterno, apellido_materno, telefono, email)
    sql_statement_2(connection, statement, data)




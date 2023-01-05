from database_connection import connect
connection = connect()


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


# Recibe los datos de un nuevo contacto para almacenarlos en la base de datos
# Realiza conexión con la base de datos e inserta los datos
def agregar_contacto(connection, nombre, apellido_paterno, apellido_materno, telefono, email):
    statement = 'INSERT INTO contactos (nombre, apellido_p, apellido_m, telefono, email) VALUES(?, ?, ?, ?, ?)'
    data = (nombre, apellido_paterno, apellido_materno, telefono, email)
    sql_statement_2(connection, statement, data)


# Recibe los datos de un contacto existente para poder actualizarlos
# Identifica al contacto por su id e inserta los nuevos datos
def actualizar_contacto(connection, nombre, apellido_p, apellido_m, telefono, email, id, ):
    statement = 'UPDATE contactos SET nombre = ?, apellido_p = ?, apellido_m = ?, telefono = ?, email = ? WHERE id = ?'
    data = (nombre, apellido_p, apellido_m, telefono, email, id)
    sql_statement_2(connection, statement, data)


# Recibe el id de un contacto y procede a eliminarlo de la base de datos
def eliminar_contacto_id(connection, id_contacto):
    statement = 'DELETE from contactos WHERE id = ?' 
    data = (id_contacto, )
    sql_statement_2(connection, statement, data)

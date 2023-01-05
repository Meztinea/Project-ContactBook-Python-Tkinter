from tkinter import Tk, LabelFrame, Label, Button, Entry, Frame, ttk, messagebox
from sentencias_sql import *
from crear_tablas import tables


class Agenda(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.c_t = '#FFFFFF'  # Color texto
        self.c_r = '#0C1633'  # Color relleno
        self.c_r_e = '#BCB8B1'  # Color relleno entry
        self.c_t_e = '#000000'  # '#2B2D42'  # Color texto entry
        self.id_contacto = ''
        self.frame_principal = LabelFrame(self.master, font=(
            'Arial', 20), bg=self.c_r, fg=self.c_t)
        self.frame_principal.place(relx=0.02, rely=0.02,
                                   relwidth=0.96, relheight=0.96)
        crear_tablas_sql(connection, tables)
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta Buscar contacto
        Label(self.frame_principal, text='Buscar Contacto : ', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.02, relwidth=0.18, relheight=0.10)

        # Entry Buscar Contacto
        self.buscar_contacto = Entry(
            self.frame_principal, fg=self.c_t_e, bg=self.c_r_e)
        self.buscar_contacto.place(
            relx=0.24, rely=0.02, relwidth=0.50, relheight=0.10)
        self.buscar_contacto.bind('<KeyRelease>', self.buscar_contactos)

        # Treeview lista de contactos
        self.treeview = ttk.Treeview(
            self.frame_principal, height=5, columns=('#1', '#2', '#3'))
        self.treeview.place(relx=0.03, rely=0.14,
                            relwidth=0.94, relheight=0.72)
        self.treeview.heading('#0', text='No.', anchor='c')
        self.treeview.heading('#1', text='Nombre', anchor='c')
        self.treeview.heading('#2', text='Teléfono', anchor='c')
        self.treeview.heading('#3', text='Email', anchor='c')
        self.treeview.column('#0', width=5, anchor='c')
        self.treeview.column('#1', width=170, anchor='w')
        self.treeview.column('#2', width=50, anchor='c')
        self.treeview.column('#3', width=120, anchor='w')
        self.treeview.bind('<<TreeviewSelect>>', self.seleccion_treeview)
        self.lista_contactos = traer_contactos(connection)
        self.actualizar_treeview_contactos(self.lista_contactos)

        # Botones Agregar - Editar - Eliminar
        Button(self.frame_principal, text='Agregar Contacto', fg=self.c_t, bg=self.c_r,
               command=self.agregar_contacto).place(relx=0.03, rely=0.88, relwidth=0.29, relheight=0.10)
        Button(self.frame_principal, text='Editar Contacto', fg=self.c_t, bg=self.c_r,
               command=self.editar_contacto).place(relx=0.35, rely=0.88, relwidth=0.29, relheight=0.10)
        Button(self.frame_principal, text='Eliminar Contacto', fg=self.c_t, bg=self.c_r,
               command=self.eliminar_contacto).place(relx=0.67, rely=0.88, relwidth=0.30, relheight=0.10)

    # Frame para agregar un nuevo contacto
    def agregar_contacto(self):
        self.ventana_contacto = Tk()
        self.ventana_contacto.title('Agregar Contacto')
        self.ventana_contacto.geometry('300x350')
        self.ventana_contacto.configure(background='#0C1633')
        self.ventana_contacto.minsize(height=350, width=300)
        # Etiquetas 
        Label(self.ventana_contacto, text='Agregar Nuevo Contacto', fg=self.c_t, bg=self.c_r,
              anchor='c', font=('Arial', 16)).place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)
        Label(self.ventana_contacto, text='* Campos obligatorios', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.17, relwidth=0.45, relheight=0.05)
        Label(self.ventana_contacto, text='Nombre *', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.25, relwidth=0.35, relheight=0.08)
        Label(self.ventana_contacto, text='Apellido Paterno *', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.36, relwidth=0.35, relheight=0.08)
        Label(self.ventana_contacto, text='Apellido Materno', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.47, relwidth=0.35, relheight=0.08)
        Label(self.ventana_contacto, text='Teléfono', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.58, relwidth=0.35, relheight=0.08)
        Label(self.ventana_contacto, text='Email', fg=self.c_t, bg=self.c_r,
              anchor='w').place(relx=0.03, rely=0.69, relwidth=0.35, relheight=0.08)
        # Entrys
        self.nombre_contacto = Entry(
            self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
        self.nombre_contacto.place(
            relx=0.43, rely=0.25, relwidth=0.54, relheight=0.08)
        self.apellido_p_contacto = Entry(
            self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
        self.apellido_p_contacto.place(
            relx=0.43, rely=0.36, relwidth=0.54, relheight=0.08)
        self.apellido_m_contacto = Entry(
            self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
        self.apellido_m_contacto.place(
            relx=0.43, rely=0.47, relwidth=0.54, relheight=0.08)
        self.telefono_contacto = Entry(
            self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
        self.telefono_contacto.place(
            relx=0.43, rely=0.58, relwidth=0.54, relheight=0.08)
        self.email_contacto = Entry(
            self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
        self.email_contacto.place(
            relx=0.43, rely=0.69, relwidth=0.54, relheight=0.08)
        self.telefono_contacto.bind('<KeyRelease>', self.dar_formato_telefono)
        # Botón
        Button(self.ventana_contacto, text='Guardar y Salir', fg=self.c_t, bg=self.c_r,
               command=self.guardar_nuevo_contacto).place(relx=0.27, rely=0.82, relwidth=0.46, relheight=0.13)

    # Frame para editar a un contacto
    def editar_contacto(self):
        if self.id_contacto == '':
            messagebox.showerror(
                title='Error', message='Seleccione un contacto')
        else:
            self.contacto = traer_contacto_id_editar(
                connection, self.id_contacto)
            self.ventana_contacto = Tk()
            self.ventana_contacto.title('Editar Contacto')
            self.ventana_contacto.geometry('300x350')
            self.ventana_contacto.configure(background='#0C1633')
            self.ventana_contacto.minsize(height=350, width=300)
            # Etiquetas
            Label(self.ventana_contacto, text='Editar Datos de Contacto', fg=self.c_t, bg=self.c_r,
              anchor='c', font=('Arial', 16)).place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)
            Label(self.ventana_contacto, text='* Campos obligatorios', fg=self.c_t, bg=self.c_r,
                anchor='w').place(relx=0.03, rely=0.17, relwidth=0.45, relheight=0.05)
            Label(self.ventana_contacto, text='Nombre *', fg=self.c_t, bg=self.c_r,
                anchor='w').place(relx=0.03, rely=0.25, relwidth=0.35, relheight=0.08)
            Label(self.ventana_contacto, text='Apellido Paterno *', fg=self.c_t, bg=self.c_r,
                anchor='w').place(relx=0.03, rely=0.36, relwidth=0.35, relheight=0.08)
            Label(self.ventana_contacto, text='Apellido Materno', fg=self.c_t, bg=self.c_r,
                anchor='w').place(relx=0.03, rely=0.47, relwidth=0.35, relheight=0.08)
            Label(self.ventana_contacto, text='Teléfono', fg=self.c_t, bg=self.c_r,
                anchor='w').place(relx=0.03, rely=0.58, relwidth=0.35, relheight=0.08)
            Label(self.ventana_contacto, text='Email', fg=self.c_t, bg=self.c_r,
                anchor='w').place(relx=0.03, rely=0.69, relwidth=0.35, relheight=0.08)
            # Entrys
            self.nombre_contacto = Entry(
                self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
            self.nombre_contacto.place(
                relx=0.43, rely=0.25, relwidth=0.54, relheight=0.08)
            self.apellido_p_contacto = Entry(
                self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
            self.apellido_p_contacto.place(
                relx=0.43, rely=0.36, relwidth=0.54, relheight=0.08)
            self.apellido_m_contacto = Entry(
                self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
            self.apellido_m_contacto.place(
                relx=0.43, rely=0.47, relwidth=0.54, relheight=0.08)
            self.telefono_contacto = Entry(
                self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
            self.telefono_contacto.place(
                relx=0.43, rely=0.58, relwidth=0.54, relheight=0.08)
            self.email_contacto = Entry(
                self.ventana_contacto, fg=self.c_t_e, bg=self.c_r_e)
            self.email_contacto.place(
                relx=0.43, rely=0.69, relwidth=0.54, relheight=0.08)
            self.telefono_contacto.bind(
                '<KeyRelease>', self.dar_formato_telefono)
            # Botón
            Button(self.ventana_contacto, text='Guardar y Salir', fg=self.c_t, bg=self.c_r,
                   command=self.guardar_cambios_contacto).place(relx=0.27, rely=0.82, relwidth=0.46, relheight=0.13)
            # Ingresa en los entry los datos del contacto a editar
            self.actualizar_entry(self.nombre_contacto, self.contacto[0][1])
            self.actualizar_entry(
                self.apellido_p_contacto, self.contacto[0][2])
            self.actualizar_entry(
                self.apellido_m_contacto, self.contacto[0][3])
            self.actualizar_entry(self.telefono_contacto, self.contacto[0][4])
            self.actualizar_entry(self.email_contacto, self.contacto[0][5])


    # Frame para eliminar un contacto
    def eliminar_contacto(self):
        if self.id_contacto == '':
            messagebox.showerror(
                title='Error', message='Seleccione un contacto en la lista')
        else:
            # Agregar el código para eliminar a un contacto
            #self.contacto = traer_contacto_id(connection, self.id_contacto)
            pass

    def validar_contacto(self, nombre, apellido_p, telefono):
        campos_obligatorios = self.validar_nombre_apellidos(nombre, apellido_p)
        telefono_valido = self.validar_telefono(telefono)

        if campos_obligatorios == True and telefono_valido == True:
            return True


    def validar_nombre_apellidos(self, nombre, apellido_p):
        if nombre == '' or apellido_p == '':
            Label(self.ventana_contacto, text='Error: Revise los campos obligatorios', fg='red',
                  bg=self.c_r, anchor='w').place(relx=0.03, rely=0.75, relwidth=0.94, relheight=0.05)
        else:
            return True


# Recibe el nombre, apellido_p y apellido_m para darle formato 
# Quita las tildes, Convierte primer letra en mayúsculas
    def dar_formato_nombre(self):
        nombre = self.nombre_contacto.get()
        apellido_p = self.apellido_p_contacto.get()
        apellido_m = self.apellido_m_contacto.get()
        telefono = self.telefono_contacto.get()
        email = self.email_contacto.get()
        
        caracteres_1, caracteres_2 = 'áéíóúüÁÉÍÓÚÜ', 'aeiouuAEIOUU'
        hacer_cambio = str.maketrans(caracteres_1, caracteres_2)
        nombre = str.title(nombre.translate(hacer_cambio))
        apellido_p = str.title(apellido_p.translate(hacer_cambio))
        apellido_m = str.title(apellido_m.translate(hacer_cambio))
        contacto = {'nombre': nombre, 'apellido_p': apellido_p, 'apellido_m': apellido_m,
                           'telefono': telefono, 'email': email}
        return contacto




# Validación de datos y query para editar / actualizar contacto
    def guardar_cambios_contacto(self):
        contacto = self.dar_formato_nombre()
        datos_validados = self.validar_contacto(contacto['nombre'], contacto['apellido_p'],
                                                contacto['telefono'])

        if datos_validados == True:
            actualizar_contacto(connection, contacto['nombre'], contacto['apellido_p'],
                                contacto['apellido_m'], contacto['telefono'], contacto['email'], self.contacto[0][0])
            self.lista_contactos = traer_contactos(connection)
            self.actualizar_treeview_contactos(self.lista_contactos)
            self.ventana_contacto.destroy()

    # Validacion de datos y query para agregar contacto

    def guardar_nuevo_contacto(self):
        nombre = self.nombre_contacto.get()
        apellido_p = self.apellido_p_contacto.get()
        apellido_m = self.apellido_m_contacto.get()
        telefono = self.telefono_contacto.get()
        email = self.email_contacto.get()
        datos_validados = self.validar_contacto(nombre, apellido_p, telefono)

        caracteres_1, caracteres_2 = 'áéíóúüÁÉÍÓÚÜ', 'aeiouuAEIOUU'
        hacer_cambio = str.maketrans(caracteres_1, caracteres_2)
        nombre = nombre.translate(hacer_cambio)
        nombre = str.title(nombre)
        apellido_p = apellido_p.translate(hacer_cambio)
        apellido_p = str.title(apellido_p)
        apellido_m = apellido_m.translate(hacer_cambio)
        apellido_m = str.title(apellido_m)

        if datos_validados == True:
            agregar_contacto(connection, nombre, apellido_p,
                             apellido_m, telefono, email)
            self.lista_contactos = traer_contactos(connection)
            self.actualizar_treeview_contactos(self.lista_contactos)
            self.ventana_contacto.destroy()




############################    Funciones   revisadas       ###########################

# Recibe una lista de tuplas, cada tupla es un contacto, la tupla contiene 4 elementos
# Actualiza el treeview que se muestra como lista de contactos en la GUI
    def actualizar_treeview_contactos(self, lista):
        self.treeview.delete(*self.treeview.get_children())
        for i in range(len(lista)):
            self.treeview.insert('', 'end', text=lista[i][0], values=(
                lista[i][1], lista[i][2], lista[i][3]))


# Recibe un evento de input en el Entry Buscar Contacto, con los datos recibidos busca coincidencias
# Busca en una lista de tuplas las coincidencias de contactos en la base de datos

    def buscar_contactos(self, event):
        contacto_buscar = event.widget.get()

        if contacto_buscar == '':
            datos = self.lista_contactos

        else:
            contactos_coincidencias = []
            for contacto in self.lista_contactos:
                if contacto_buscar.lower() in contacto[1].lower():
                    contactos_coincidencias.append(contacto)

        self.actualizar_treeview_contactos(contactos_coincidencias)


# Da formato al número de teléfono para aceptar solo entradas de 10 digitos y separados por guión
# Incluye los - (guión medio) al escribir el número de teléfono en agregar / editar contacto
    def dar_formato_telefono(self, event):
        entrada = event.widget.get()
        if len(entrada) == 3:
            entrada_modificada = entrada + '-'
            self.actualizar_entry(self.telefono_contacto, entrada_modificada)
        if len(entrada) == 7:
            entrada_modificada = entrada + '-'
            self.actualizar_entry(self.telefono_contacto, entrada_modificada)
        if len(entrada) == 10:
            entrada_modificada = entrada + '-'
            self.actualizar_entry(self.telefono_contacto, entrada_modificada)
        if len(entrada) >= 13:
            entrada = entrada.replace('-', '')
            entrada_modificada = entrada[0:3] + '-' + \
                entrada[3:6] + '-' + entrada[6:8] + '-' + entrada[8:10]
            self.actualizar_entry(self.telefono_contacto, entrada_modificada)

# Funcion abstracta que recibe el nombre de una variable self (Entry de Tkinter) 
# y el dato que se va a ingresar dentro del Entry
# Función que permite ver los datos del contacto que se va a editar
    def actualizar_entry(self, variable, dato):
        variable.delete(0, 'end')
        variable.insert(0, dato)


# Identifica el id del contacto seleccionado en la lista treeview para poder editarlo
# Modifica la variable self.id_contacto para almacenar el id del contacto
    def seleccion_treeview(self, event):
        fila_seleccionada = event.widget.focus()
        datos = self.treeview.item(fila_seleccionada)
        self.id_contacto = datos['text']

# Recibe el número de telefono ingresado en el Entry de teléfono
# Función para validar que el teléfono incluye solamente números y guión medio
# Valida la longitud del número telefónico - Lanza error al no pasar la validación
    def validar_telefono(self, telefono):
        tel_numerico = None
        
        for i in telefono:
            if i.isdigit() or i == '-':
                tel_numerico = True
            else:
                tel_numerico = False
                break
            

        if telefono != '' and (tel_numerico == False or len(telefono) != 13):
            Label(self.ventana_contacto, text='Error: Teléfono inválido', fg='red', bg=self.c_r,
                  anchor='w').place(relx=0.03, rely=0.75, relwidth=0.94, relheight=0.05)
        else:
            return True





if __name__ == "__main__":
    ventana = Tk()
    ventana.title('Contact Book by @Meztinea')
    ventana.geometry('540x310')
    ventana.configure(background='#BCB8B1')  # CCD5AE
    ventana.minsize(height=310, width=540)

    app = Agenda(ventana)
    app.mainloop()

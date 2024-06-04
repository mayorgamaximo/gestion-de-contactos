import tkinter as tk
from tkinter import ttk, messagebox
from Objetos.Contacto import Contacto
from Objetos.DiccionarioContactos import ListaContactos

# Funcion para verificar el contacto
def verificar_contacto(nombre):
    for contacto in listaContactos:
        if contacto.nombre.lower() == nombre.lower():
            return True
    return False

# Funcion para agregar el contacto
def agregar_contacto():
    nombre_ingresado = entryNombre.get()
    telefono_ingresado = entryTelefono.get()
    correo_ingresado = entryCorreo.get()

    # Verificar si alguno de los campos esta vacío
    if not nombre_ingresado or not telefono_ingresado or not correo_ingresado:
        messagebox.showerror("Error", "Debe completar todos los campos para agregar un contacto")
        return  # Salir de la funcion si hay campos vacios

    if verificar_contacto(nombre_ingresado):
        messagebox.showerror("Error", "Ya existe un contacto con el mismo nombre")
    else:
        nuevo_contacto = Contacto(nombre_ingresado, telefono_ingresado, correo_ingresado)
        listaContactos.append(nuevo_contacto)
        tree.insert("", "end", values=(nombre_ingresado, telefono_ingresado, correo_ingresado))
        messagebox.showinfo("Agregar Contacto", "Contacto agregado exitosamente")

    entryNombre.delete(0, tk.END)
    entryTelefono.delete(0, tk.END)
    entryCorreo.delete(0, tk.END)


# Función para eliminar contactos
def eliminar_contactos():
    # Obtener los elementos seleccionados en la vista de arbol
    selected_items = tree.selection()

    # Verificar si hay elementos seleccionados
    if selected_items:
        # Obtener el primer elemento seleccionado (solo se elimina uno a la vez)
        selected_item = selected_items[0]
        # Obtener el indice del elemento seleccionado en la vista de arbol
        item_indice = tree.index(selected_item)

        # Verificar si el indice es valido (dentro del rango de la lista de contactos)
        if 0 <= item_indice < len(listaContactos):
            # Eliminar el contacto correspondiente de la lista de contactos
            listaContactos.pop(item_indice)
            # Eliminar el elemento seleccionado de la vista de arbol
            tree.delete(selected_item)
            # Mostrar un cuadro de dialogo informativo de exito
            messagebox.showinfo("Eliminar Contacto", "Contacto eliminado exitosamente")
        else:
            # Mostrar un cuadro de dialogo de error si el índice no es valido
            messagebox.showerror("Error", "No se pudo eliminar el contacto")
    else:
        # Mostrar un cuadro de dialogo de error si no se selecciono ningun contacto
        messagebox.showerror("Error", "Ningún contacto seleccionado")

# Funcion para abrir la ventana de edicion
def ventana_editar_contacto():
    selected_items = tree.selection()

    if selected_items:
        selected_item = selected_items[0]
        ventanaEditar = tk.Toplevel()
        ventanaEditar.title("Editar Contacto")
        item_index = tree.index(selected_item)
        contacto_seleccionado = listaContactos[item_index]

        labelEditarNombre = tk.Label(ventanaEditar, text="Nombre:", font=("Arial", 15))
        labelEditarNombre.grid(row=0, column=0)
        entryEditarNombre = tk.Entry(ventanaEditar, font=("Arial", 15))
        entryEditarNombre.grid(row=0, column=1)
        entryEditarNombre.insert(0, contacto_seleccionado.nombre)

        labelEditarTelefono = tk.Label(ventanaEditar, text="Telefono:", font=("Arial", 15))
        labelEditarTelefono.grid(row=1, column=0)
        entryEditarTelefono = tk.Entry(ventanaEditar, font=("Arial", 15))
        entryEditarTelefono.grid(row=1, column=1)
        entryEditarTelefono.insert(0, contacto_seleccionado.telefono)

        labelEditarCorreo = tk.Label(ventanaEditar, text="Correo:", font=("Arial", 15))
        labelEditarCorreo.grid(row=2, column=0)
        entryEditarCorreo = tk.Entry(ventanaEditar, font=("Arial", 15))
        entryEditarCorreo.grid(row=2, column=1)
        entryEditarCorreo.insert(0, contacto_seleccionado.correo)

        def guardar_cambios():
            nuevo_nombre = entryEditarNombre.get()
            nuevo_telefono = entryEditarTelefono.get()
            nuevo_correo = entryEditarCorreo.get()

            contacto_seleccionado.nombre = nuevo_nombre
            contacto_seleccionado.telefono = nuevo_telefono
            contacto_seleccionado.correo = nuevo_correo

            tree.item(selected_item, values=(nuevo_nombre, nuevo_telefono, nuevo_correo))
            messagebox.showinfo("Editar Contacto", "Cambios guardados exitosamente")
            ventanaEditar.destroy()

        botonGuardarCambios = tk.Button(ventanaEditar, text="Guardar Cambios", font=("Arial", 15), command=guardar_cambios)
        botonGuardarCambios.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Funcion para buscar contactos
def buscar_contactos():
    encontrados = False
    texto = ""
    nombre_buscar = entryNombre.get().lower()
    
    if nombre_buscar:
        for contacto in listaContactos:
            if nombre_buscar in contacto.nombre.lower():
                texto += f"Nombre: {contacto.nombre} \n"
                texto += f"Telefono: {contacto.telefono} \n"
                texto += f"Correo: {contacto.correo} \n"
                encontrados = True

    if encontrados:
        messagebox.showinfo("Contacto encontrado: ", texto)
    else:
        messagebox.showerror("ERROR", "ESTE CONTACTO NO SE ENCUENTRA")

# Funcion para mostrar la lista de contactos
def mostrar_contactos():
    ventanaContactos = tk.Tk()
    ventanaContactos.title("Lista de Contactos")

    tree = ttk.Treeview(ventanaContactos, columns=("Nombre", "Telefono", "Correo"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Telefono", text="Telefono")
    tree.heading("Correo", text="Correo")

    for contacto in listaContactos:
        tree.insert("", "end", values=(contacto.nombre, contacto.telefono, contacto.correo))

    tree.column("Nombre", width=200)
    tree.column("Telefono", width=150)
    tree.column("Correo", width=250)

    tree.pack(padx=20, pady=20)

    ventanaContactos.mainloop()

# Funcion para preguntar si desea guardar cambios al salir
def boton_salir():
    respuesta = messagebox.askyesno("Guardar cambios", "¿Desea guardar los cambios?")
    if respuesta:
        # Implementa aqui la logica para guardar los cambios
        pass
    ventanaPrincipal.destroy()

# Configuracion inicial
listaContactos = []
ventanaPrincipal = tk.Tk()
ventanaPrincipal.configure(bg="#36393F")
ventanaPrincipal.title("Sistema de gestion de contactos")

tree = ttk.Treeview(ventanaPrincipal, columns=("Nombre", "Telefono", "Correo"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Telefono", text="Telefono")
tree.heading("Correo", text="Correo")

labelTitulo = tk.Label(ventanaPrincipal, text="CONTAC STUDIO", font=("Arial", 30), fg="white", bg="#36393F")
labelNombre = tk.Label(ventanaPrincipal, text="Ingrese Nombre:", font=("Arial", 20), fg="white", bg="#36393F")
entryNombre = tk.Entry(ventanaPrincipal, font=("Arial", 20), bg="#2C2F33", fg="white")
labelTelefono = tk.Label(ventanaPrincipal, text="Ingrese Telefono:", font=("Arial", 20), fg="white", bg="#36393F")
entryTelefono = tk.Entry(ventanaPrincipal, font=("Arial", 20), bg="#2C2F33", fg="white")
labelCorreo = tk.Label(ventanaPrincipal, text="Ingrese Correo:", font=("Arial", 20), fg="white", bg="#36393F")
entryCorreo = tk.Entry(ventanaPrincipal, font=("Arial", 20), bg="#2C2F33", fg="white")

buttonContactoAgregar = tk.Button(ventanaPrincipal, text="Agregar Contacto", font=("Arial", 15), bg="#7289DA", fg="white", command=agregar_contacto)
buttonContactoEliminar = tk.Button(ventanaPrincipal, text="Eliminar Contacto", font=("Arial", 15), bg="#7289DA", fg="white", command=eliminar_contactos)
buttonContactoBuscar = tk.Button(ventanaPrincipal, text="Buscar Contacto", font=("Arial", 15), bg="#7289DA", fg="white", command=buscar_contactos)
buttonMostrarLista = tk.Button(ventanaPrincipal, text="Mostrar Lista", font=("Arial", 15), bg="#7289DA", fg="white", command=mostrar_contactos)
buttonEditarContacto = tk.Button(ventanaPrincipal, text="Editar Contacto", font=("Arial", 15), bg="#7289DA", fg="white", command=ventana_editar_contacto)
buttonSalir = tk.Button(ventanaPrincipal, text="Salir", font=("Arial", 15), bg="#7289DA", fg="white", command=boton_salir)

# Colocar los widgets en la ventana
tree.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
labelTitulo.grid(row=1, column=1, padx=20, pady=20)
labelNombre.grid(row=2, column=0, padx=20, pady=20)
entryNombre.grid(row=2, column=1, padx=20, pady=20)
labelTelefono.grid(row=3, column=0, padx=20, pady=20)
entryTelefono.grid(row=3, column=1, padx=20, pady=20)
labelCorreo.grid(row=4, column=0, padx=20, pady=20)
entryCorreo.grid(row=4, column=1, padx=20, pady=20)
buttonContactoAgregar.grid(row=5, column=0, padx=20, pady=20)
buttonContactoBuscar.grid(row=5, column=2, padx=20, pady=20)
buttonContactoEliminar.grid(row=5, column=1, padx=20, pady=20)
buttonMostrarLista.grid(row=6, column=0, padx=20, pady=20)
buttonEditarContacto.grid(row=6, column=1, padx=20, pady=20)
buttonSalir.grid(row=6, column=2, padx=20, pady=20)

ventanaPrincipal.mainloop()

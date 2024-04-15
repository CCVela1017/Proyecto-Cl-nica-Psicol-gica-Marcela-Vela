import datetime
import customtkinter
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


fecha_actual = datetime.datetime.now()
mes_actual = fecha_actual.month
anio_actual = fecha_actual.year

fecha_ahorita = str(mes_actual) + str(anio_actual)

def cargar_base_de_datos_de_estado_resultados():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM estado_de_resultados')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        lista = []
        for item in data:
            contador = 0
            for datos in item:
                if contador == 4:
                    lista.append(datos)
                contador += 1
        return lista
    except Exception as ex:
        print(ex)
        lista = []
        return lista


def cargar_base_de_datos_utilidad_bruta():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM utilidad_bruta')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        lista = []
        for item in data:
            fecha_evaluado = item[6]
            if str(fecha_ahorita) == str(fecha_evaluado):
                lista = item
        return lista
    except Exception as ex:
        print(ex)


def cargar_base_de_datos_ventas():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM facturas_ventas')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        return data
    except Exception as ex:
        print(ex)


def cargar_base_de_datos_compras():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM facturas_compras')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        return data
    except Exception as ex:
        print(ex)


def obtener_columna(my_tree):
    total = 0
    for item in my_tree.get_children():
        valor = float(my_tree.item(item, "values")[4])
        total += valor
    return total


def textos(lugar, total_vendido, total_comprado, lista_utilidad_bruta):
    editar = False
    lista_estados_resultados = cargar_base_de_datos_de_estado_resultados()
    """Servicios vendidos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Servicios dados:",
                                      font=("times new roman", 22, "bold"))
    etiqueta.place(x=39, y=23)

    """Productos adquiridos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Productos adquiridos:",
                                      font=("times new roman", 22, "bold"))
    etiqueta.place(x=419, y=23)

    """Ganancias y Pérdidas"""
    lb_total_vendido = customtkinter.CTkLabel(master=lugar, text="total vendido: " + str(total_vendido),
                                              font=(" ", 32))
    lb_total_vendido.place(x=39, y=300)

    lb_total_comprado = customtkinter.CTkLabel(master=lugar, text="total comprado: " + str(total_comprado),
                                               font=(" ", 32))
    lb_total_comprado.place(x=39, y=350)


    lb_alquiler = customtkinter.CTkLabel(master=lugar, text='Alquiler: ' + str(lista_utilidad_bruta[1]), font=(" ", 32))
    lb_alquiler.pack(pady=400, padx=400, )
    lb_alquiler.place(x=39, y=400)

    lb_energeticos = customtkinter.CTkLabel(master=lugar, text='Energeticos: ' + str(lista_utilidad_bruta[2]),
                                            font=(" ", 32))
    lb_energeticos.pack(pady=400, padx=400, )
    lb_energeticos.place(x=39, y=450)

    lb_transporte = customtkinter.CTkLabel(master=lugar, text='Transporte: ' + str(lista_utilidad_bruta[3]),
                                           font=(" ", 32))
    lb_transporte.pack(pady=400, padx=400)
    lb_transporte.place(x=39, y=500)

    lb_red = customtkinter.CTkLabel(master=lugar, text='Red: ' + str(lista_utilidad_bruta[4]), font=(" ", 32))
    lb_red.pack(pady=400, padx=400)
    lb_red.place(x=39, y=550)

    lb_planilla = customtkinter.CTkLabel(master=lugar, text='Planilla: ' + str(lista_utilidad_bruta[5]), font=(" ", 32))
    lb_planilla.pack(pady=400, padx=400)
    lb_planilla.place(x=39, y=600)

    total_sin_isr = total_vendido - total_comprado - float(lista_utilidad_bruta[7])

    lb_total_sin_isr = customtkinter.CTkLabel(master=lugar, text='Total SIN ISR: ' + str(total_sin_isr), font=(" ", 32))
    lb_total_sin_isr.pack(pady=400, padx=400)
    lb_total_sin_isr.place(x=39, y=650)

    total_con_isr = total_vendido - (total_vendido * 0.05) - total_comprado - float(lista_utilidad_bruta[7])

    lb_total_con_isr = customtkinter.CTkLabel(master=lugar, text='Total Con ISR: ' + str(total_con_isr), font=(" ", 32))
    lb_total_con_isr.pack(pady=400, padx=400)
    lb_total_con_isr.place(x=450, y=650)

    conexion = sqlite3.connect('src/database')
    cursor = conexion.cursor()

    if lista_estados_resultados != []:
        editar = True

    if editar is False:
        try:
            cursor.execute("INSERT INTO estado_de_resultados (comprado, "
                           "vendido, "
                           "utilidad_bruta, "
                           "fecha, "
                           "total_con_iva, "
                           "total_sin_iva) "
                           "VALUES (?, ?, ?, ?, ?, ?)",
                           (total_vendido, total_comprado, lista_utilidad_bruta[7], fecha_ahorita,
                            total_con_isr, total_sin_isr))
            messagebox.showinfo('¡Datos Ingresados Correctamente!', 'Los datos ingresados fueron '
                                                                    'enviados correctamente a la base de datos.')
            conexion.commit()
            conexion.close()
        except Exception as ex:
            messagebox.showerror('¡Datos Ingresados Incorrectamente!', 'Vaya, parece que un campo '
                                                                       'no coincide con la base de datos, verifica los '
                                                                       'datos ingresados.')

            print(ex)
            conexion.commit()
            conexion.close()

    else:
        try:
            cursor.execute("UPDATE estado_de_resultados SET comprado = ?, "
                           "vendido = ?, "
                           "utilidad_bruta = ?, "
                           "fecha = ?, "
                           "total_con_iva = ?, "
                           "total_sin_iva = ?",
                           (total_vendido, total_comprado, lista_utilidad_bruta[7], fecha_ahorita,
                            total_con_isr, total_sin_isr))
            conexion.commit()  # Guarda los cambios en la base de datos
            messagebox.showinfo('¡Datos Modificados Correctamente!',
                                'Los datos ingresados fueron enviados correctamente a la base de datos.')
        except sqlite3.Error as ex:
            messagebox.showerror('¡Error al Modificar Datos!',
                                 'parece que un campo no coincide con la base de datos, verifica los datos ingresados.')
            print(ex)
        finally:
            if conexion:
                conexion.close()

def tabla1(lugar):
    """Tabla"""
    tabla = Frame(lugar)
    tabla.pack(pady=70)

    tabla.place(x=39, y=91)

    tabla_scroll = Scrollbar(tabla)
    tabla_scroll.pack(side=RIGHT, fill=Y)
    my_tree = ttk.Treeview(tabla, yscrollcommand=tabla_scroll.set, selectmode='extended')

    my_tree.pack()

    tabla_scroll.config(command=my_tree.yview)

    my_tree['columns'] = (
        'No. Factura', 'Nombre', 'NIT', 'Fecha', 'Total')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('No. Factura', anchor=W, width=90)
    my_tree.column('Nombre', anchor=W, width=100)
    my_tree.column('NIT', anchor=W, width=60)
    my_tree.column('Fecha', anchor=W, width=80)
    my_tree.column('Total', anchor=W, width=80)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('No. Factura', text='No. Factura', anchor=W)
    my_tree.heading('Nombre', text='Nombre', anchor=W)
    my_tree.heading('NIT',  text='NIT', anchor=W)
    my_tree.heading('Fecha', text='Fecha', anchor=W)
    my_tree.heading('Total', text='Total', anchor=W)

    my_tree.tag_configure('oddrow', background='black')
    my_tree.tag_configure('evenrow', background='lightblue')

    count = 0
    data = cargar_base_de_datos_ventas()

    for record in data:
        fecha = " "
        fecha_a_evaluar = " "
        if count % 2 == 0:
            fecha_a_evaluar = str(record[6] + record[7])
            if fecha_a_evaluar == fecha_ahorita:
                fecha = str(record[5] + "/" + record[6] + "/" + record[7])
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], fecha, record[8],
                                       ), tags=('evenrow',))

        else:
            fecha_a_evaluar = str(record[6] + record[7])
            if fecha_a_evaluar == fecha_ahorita:
                fecha = str(record[5] + "/" + record[6] + "/" + record[7])
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[0], record[1], record[3], fecha, record[8],
                                       ), tags=('oddrow',))
        count += 1
    ventas_totales = obtener_columna(my_tree)
    return ventas_totales


def tabla2(lugar):
    """Tabla"""
    tabla = Frame(lugar)
    tabla.pack(pady=70)

    tabla.place(x=519, y=91)

    tabla_scroll = Scrollbar(tabla)
    tabla_scroll.pack(side=RIGHT, fill=Y)
    my_tree_2 = ttk.Treeview(tabla, yscrollcommand=tabla_scroll.set, selectmode='extended')

    my_tree_2.pack()

    tabla_scroll.config(command=my_tree_2.yview)

    my_tree_2['columns'] = (
        'Num', 'Proveedor', 'Producto', 'Fecha', 'Total')

    my_tree_2.column('#0', width=0, stretch=NO)
    my_tree_2.column('Num', anchor=W, stretch=NO, width=80)
    my_tree_2.column('Proveedor', anchor=W, stretch=NO, width=100)
    my_tree_2.column('Producto', anchor=W, stretch=NO, width=100)
    my_tree_2.column('Fecha', anchor=W, stretch=NO, width=80)
    my_tree_2.column('Total', anchor=W, stretch=NO, width=70)

    my_tree_2.heading('#0', text='', anchor=W)
    my_tree_2.heading('Num', text='Num', anchor=W)
    my_tree_2.heading('Proveedor', text='Proveedor', anchor=W)
    my_tree_2.heading('Producto', text='Producto', anchor=W)
    my_tree_2.heading('Fecha', text='Fecha', anchor=W)
    my_tree_2.heading('Total', text='Total', anchor=W)

    my_tree_2.tag_configure('oddrow', background='black')
    my_tree_2.tag_configure('evenrow', background='lightblue')

    count = 0
    data = cargar_base_de_datos_compras()
    for record in data:
        fecha = " "
        fecha_a_evaluar = " "
        if count % 2 == 0:
            fecha_a_evaluar = str((record[5]) + record[6])
            if fecha_a_evaluar == fecha_ahorita:
                fecha = str(record[4] + "/" + record[5] + "/" + record[6])
                my_tree_2.insert(parent='', index='end', iid=count, text='',
                                 values=(record[1], record[2], record[3], fecha, record[7],
                                         ), tags=('evenrow',))
        else:
            fecha_a_evaluar = str(record[5] + record[6])
            if fecha_a_evaluar == fecha_ahorita:
                fecha = str(record[4] + "/" + record[5] + "/" + record[6])
                my_tree_2.insert(parent='', index='end', iid=count, text='',
                                 values=(record[0], record[1], record[3], fecha, record[7],
                                         ), tags=('oddrow',))
        count += 1
    compras_totales = obtener_columna(my_tree_2)
    return compras_totales


def main_estado_resultados():
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    lista_utilidad_bruta = (cargar_base_de_datos_utilidad_bruta())
    root.title("Estado de resultados")
    root.iconbitmap('icon.ico')
    root.wm_attributes("-topmost", True)

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10, padx=10, fill='both', expand=True)

    ventas_totales = tabla1(frame)
    compras_totales = tabla2(frame)

    textos(frame, ventas_totales, compras_totales, lista_utilidad_bruta)

    root.geometry('840x720')
    root.mainloop()

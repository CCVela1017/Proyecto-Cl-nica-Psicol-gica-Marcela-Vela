import datetime

import customtkinter
import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
from ventas import productos_vendidos
from compras import productos_comprados


fecha_actual = datetime.datetime.now()
mes_actual = fecha_actual.month
anio_actual = fecha_actual.year

fecha_ahorita = str(mes_actual) + str(anio_actual)



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


def boton(lugar):
    """Visualizar"""
    actualizar = customtkinter.CTkButton(master=lugar, text="Visualizar", height=80, width=50,
                                         font=("times new roman", 20, "bold"),
                                         fg_color="#3E4446")
    actualizar.place(x=630, y=280)

def textos(lugar):
    """Servicios vendidos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Servicios dados:",
                                      font=("times new roman", 22, "bold"))
    etiqueta.place(x=39, y=23)

    """Productos adquiridos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Productos adquiridos:",
                                      font=("times new roman", 22, "bold"))
    etiqueta.place(x=419, y=23)

    """Ganancias y Pérdidas"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Este mes obtuvo una:",
                                      font=("times new roman", 32, "bold"))
    etiqueta.place(x=50, y=300)


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

    return


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


def ganancia_perdida(lugar):
    pass


def main_estado_resultados():
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root.title("Estado de resultados")
    root.iconbitmap('icon.ico')
    root.wm_attributes("-topmost", True)

    marco = customtkinter.CTkFrame(master=root, width=780, height=430)
    marco.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    textos(marco)
    tabla1(marco)
    tabla2(marco)
    boton(marco)
    ganancia_perdida(marco)

    root.geometry('800x450')
    root.mainloop()

import customtkinter
import tkinter
from tkinter import *
from tkinter import ttk

from ventas import productos_vendidos
from compras import productos_comprados

def boton(lugar):
    """Visualizar"""
    actualizar = customtkinter.CTkButton(master=lugar, text="Visualizar", height=80, width=50,
                                         font=("times new roman", 20, "bold"),
                                         fg_color="#3E4446")
    actualizar.place(x=630, y=280)

def textos(lugar):
    """Servicios vendidos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Servicios/Productos vendidos:",
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
    global my_tree
    my_tree = ttk.Treeview(tabla, yscrollcommand=tabla_scroll.set, selectmode='extended')

    my_tree.pack()

    tabla_scroll.config(command=my_tree.yview)

    my_tree['columns'] = (
        'Servicio/Producto', 'Costo unitario', 'Cantidad', 'Total')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Servicio/Producto', anchor=W, width=150)
    my_tree.column('Costo unitario', anchor=W, width=100)
    my_tree.column('Cantidad', anchor=W, width=80)
    my_tree.column('Total', anchor=W, width=80)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Servicio/Producto', text='Servicio/Producto', anchor=W)
    my_tree.heading('Costo unitario', text='Costo unitario', anchor=W)
    my_tree.heading('Cantidad', text='Cantidad', anchor=W)
    my_tree.heading('Total', text='Total', anchor=W)

    my_tree.tag_configure('oddrow', background='black')
    my_tree.tag_configure('evenrow', background='lightblue')

    count = 0

    for indice in productos_vendidos:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                             values=(indice[1], indice[3], str(indice[0]) + ' unidades'
                                     , str(indice[2])), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                             values=(indice[1], indice[3], str(indice[0]) + ' unidades'
                                     , str(indice[2])), tags=('oddrow',))
        count += 1


def tabla2(lugar):
    """Tabla"""
    tabla = Frame(lugar)
    tabla.pack(pady=70)

    tabla.place(x=519, y=91)

    tabla_scroll = Scrollbar(tabla)
    tabla_scroll.pack(side=RIGHT, fill=Y)
    global my_tree
    my_tree = ttk.Treeview(tabla, yscrollcommand=tabla_scroll.set, selectmode='extended')

    my_tree.pack()

    tabla_scroll.config(command=my_tree.yview)

    my_tree['columns'] = (
        'Producto', 'Costo unitario', 'Cantidad', 'Total')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Producto', anchor=W, stretch=NO ,width=120)
    my_tree.column('Costo unitario', anchor=W, stretch=NO ,width=100)
    my_tree.column('Cantidad', anchor=W, stretch=NO ,width=80)
    my_tree.column('Total', anchor=W, stretch=NO ,width=70)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Producto', text='Producto', anchor=W)
    my_tree.heading('Costo unitario', text='Costo unitario', anchor=W)
    my_tree.heading('Cantidad', text='Cantidad', anchor=W)
    my_tree.heading('Total', text='Total', anchor=W)

    my_tree.tag_configure('oddrow', background='black')
    my_tree.tag_configure('evenrow', background='lightblue')

    count = 0

    for indice in productos_comprados:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(indice[0], indice[1], str(indice[2]) + ' unidades'
                                   , str(indice[3])), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(indice[0], indice[1], str(indice[2]) + ' unidades'
                                   , str(indice[3])), tags=('oddrow',))
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

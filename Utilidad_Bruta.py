import customtkinter
import tkinter
from tkinter import *
from tkinter import ttk




def rellenartabla():
    pass
    for _ in ():
            my_tree.insert("", "end", values=(_))
def agregartabla(lugar):
    """Tabla"""
    tabla = Frame(lugar)
    tabla.pack(pady=70)

    tabla.place(x=494, y=230)

    tabla_scroll = Scrollbar(tabla)
    tabla_scroll.pack(side=RIGHT, fill=Y)
    global my_tree
    my_tree = ttk.Treeview(tabla, yscrollcommand=tabla_scroll.set, selectmode='extended')

    my_tree.pack()

    tabla_scroll.config(command=my_tree.yview)

    my_tree['columns'] = (
        'Gasto', 'Costo unitario', 'Cantidad', 'Total' )

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Gasto', anchor=W, width=60)
    my_tree.column('Costo unitario', anchor=W, width=100)
    my_tree.column('Cantidad', anchor=W, width=60)
    my_tree.column('Total', anchor=W, width=60)


    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Gasto', text='Gasto', anchor=W)
    my_tree.heading('Costo unitario', text='Costo unitario', anchor=W)
    my_tree.heading('Cantidad', text='Cantidad', anchor=W)
    my_tree.heading('Total', text='Total', anchor=W)


    my_tree.tag_configure('oddrow', background='black')
    my_tree.tag_configure('evenrow', background='lightblue')

    for idx, fila_id in enumerate(my_tree.get_children()):
        if idx % 2 == 0:
            my_tree.item(fila_id, tags=('evenrow',))
        else:
            my_tree.item(fila_id, tags=('oddrow',))


def agregartexto(lugar):

    """*-*-*-*-*-*-* Etiquetas *-*-*-*-*-*-*"""
    """Gastos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Gastos:", font=("times new roman", 28, "bold"))
    etiqueta.place( x=64, y=65)


    """*-*-*-*-*-*-* Cuadros de texto *-*-*-*-*-*-*"""
    """Gastos"""
    ingresar_gasto = customtkinter.CTkEntry(master=lugar, placeholder_text="Gastos", width=200,
                                      height=35, font=("Times New Roman", 20, "bold"))
    ingresar_gasto.place(x=160, y=65)





    """*-*-*-*-*-*-* Etiquetas *-*-*-*-*-*-*"""
    """Gastos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Costo Unitario:", font=("times new roman", 28, "bold"))
    etiqueta.place(x=64, y=130)

    """*-*-*-*-*-*-* Cuadros de texto *-*-*-*-*-*-*"""
    """Gastos"""
    ingresar_costo = customtkinter.CTkEntry(master=lugar, placeholder_text="Costo", width=100,
                                            height=35, font=("Times New Roman", 20, "bold"))
    ingresar_costo.place(x=260, y=130)



    """*-*-*-*-*-*-* Etiquetas *-*-*-*-*-*-*"""
    """Gastos"""
    etiqueta = customtkinter.CTkLabel(master=lugar, text="Cantidad:", font=("times new roman", 28, "bold"))
    etiqueta.place(x=394, y=65)

    """*-*-*-*-*-*-* Cuadros de texto *-*-*-*-*-*-*"""
    """Gastos"""
    ingresar_cantidad = customtkinter.CTkEntry(master=lugar, placeholder_text="Cantidad", width=100,
                                            height=35, font=("Times New Roman", 20, "bold"))
    ingresar_cantidad.place(x=520, y=65)







def agregarbotones(lugar):
    """*-*-*-*-*-*-* Botones *-*-*-*-*-*-*"""
    """Aprobar"""
    actualizar = customtkinter.CTkButton(master=lugar, text="Aceptar", height=100, width=150,
                                         font=("times new roman", 20, "bold"),
                                         fg_color="#086EB9")
    actualizar.place(x=179, y=230)



def utilidad_bruta():
    """Apariencia de la ventana"""
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    ventana = customtkinter.CTkToplevel()
    ventana.title("Utilidad Bruta")
    ventana.wm_attributes("-topmost", False)

    ventana.geometry("732x523")

    """Se crea el marco y todo lo que va a contener"""
    """Marco"""
    marco = customtkinter.CTkFrame(master=ventana, width=684, height=475)
    marco.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    agregartabla(marco)
    agregarbotones(marco)
    agregartexto(marco)


    """Se inicia la ventana"""
    ventana.mainloop()

utilidad_bruta()

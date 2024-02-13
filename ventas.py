import random
from tkinter import ttk
from tkinter import *
import customtkinter
import sqlite3
global texto_imagen


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=90, fill='both', ipady=0)

    return frame


def frame_2(ventana):
    frame = customtkinter.CTkFrame(master=ventana, width=800, height=350)
    frame.pack(pady=10, padx=90, fill='both')

    return frame


def frame_3(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=90, fill='both')
    return frame


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    frame2 = frame_2(ventana)
    frame3 = frame_3(ventana)
    color = "#3E4446"
    labels_parte1(frame)
    labels_parte2(frame2)
    labels_parte3(frame3)
    # Variables a usar
    # IB
    ventana.mainloop()
    return


def multiplicar_datos(cantidad, precio):
    resultado = cantidad * precio
    return resultado


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Ventas")
    ventana.geometry('1270x800+50x50')
    ventana.iconbitmap('icon.ico')
    return ventana


def labels_parte1(frame):
    lb_datos_fac = customtkinter.CTkLabel(master=frame, text='Datos de Facturación',
                                          font=("Times New Roman", 50, "bold"))
    lb_datos_fac.pack(pady=400, padx=400, )
    lb_datos_fac.place(x=10, y=0)

    lb_no_fac = customtkinter.CTkLabel(master=frame, text='No.Factura', font=("Times New Roman", 30))
    lb_no_fac.pack(pady=400, padx=400, )
    lb_no_fac.place(x=10, y=60)

    no_fac = str(random.randint(1, 1000))
    entry_no_fac = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 15))
    entry_no_fac.pack(pady=400, padx=400, )
    entry_no_fac.place(x=175, y=64)
    entry_no_fac.insert(0, no_fac)
    entry_no_fac.configure(state="disable")

    lb_name = customtkinter.CTkLabel(master=frame, text='Nombre', font=("Times New Roman", 30))
    lb_name.pack(pady=400, padx=400, )
    lb_name.place(x=10, y=103)

    entry_name = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 15)
                                        , placeholder_text='Ingrese el Nombre.')
    entry_name.pack(pady=400, padx=400, )
    entry_name.place(x=175, y=107)

    lb_nit = customtkinter.CTkLabel(master=frame, text='Nit', font=("Times New Roman", 30))
    lb_nit.pack(pady=400, padx=400, )
    lb_nit.place(x=10, y=145)

    entry_nit = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 15),
                                       placeholder_text='Ingrese NIT.')
    entry_nit.pack(pady=400, padx=400, )
    entry_nit.place(x=175, y=149)

    confirm_button = customtkinter.CTkButton(master=frame, font=("Times New Roman", 18), text='Confirmar cliente',
                                             height=40)
    confirm_button.pack(pady=400, padx=400, )
    confirm_button.place(x=350, y=100)


def labels_parte2(frame):

    data_ = []
    conexion = sqlite3.connect('src/database')
    cursor = conexion.cursor()
    cursor.execute('SELECT Nombre FROM objetos_de_inventario WHERE servicio = 1')
    rows = cursor.fetchall()
    for row in rows:
        data_.append(row[0])

    conexion.close()

    lb_servicio = customtkinter.CTkLabel(master=frame, text='Servicios: ', font=("Times New Roman", 40, "bold"))
    lb_servicio.pack(pady=400, padx=400, )
    lb_servicio.place(x=10, y=10)

    lb_insumos = customtkinter.CTkLabel(master=frame, text='Insumos: ', font=("Times New Roman", 40, "bold"))
    lb_insumos.pack(pady=400, padx=400, )
    lb_insumos.place(x=10, y=100)

    lb_insumos2 = customtkinter.CTkLabel(master=frame, text='Vista Previa: ', font=("Times New Roman", 40, "bold"))
    lb_insumos2.pack(pady=400, padx=400, )
    lb_insumos2.place(x=680, y=10)

    combo_box = customtkinter.CTkComboBox(master=frame, values=data_, width=250)
    combo_box.pack(pady=400, padx=400)
    combo_box.place(x=50, y=70)

    def get_service():

        global count2
        data_u = []
        conexion_u = sqlite3.connect('src/database')
        cursor_u = conexion.cursor()
        cursor_u.execute(f'SELECT Nombre, Descripción, costo_uni FROM objetos_de_inventario WHERE Nombre = "{str(combo_box.get())}"')
        rows_ = cursor_u.fetchall()
        for r in rows_:
            data_u.append(r)

        conexion_u.close()

        for record_ in data_u:
            if count2 % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count2, text='',
                               values=(record_[0], record_[1]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count2, text='',
                               values=(record_[0], record_[1]), tags=('oddrow',))
            count2 += 1

    boton_add = customtkinter.CTkButton(master=frame,  text='Añadir servicio', font=("Times New Roman", 12, "bold")
                                        , command=get_service)
    boton_add.pack(pady=400, padx=400)
    boton_add.place(x=310, y=70)

    boton_add2 = customtkinter.CTkButton(master=frame, text='+', font=("Times New Roman", 40, "bold"), width=55)
    boton_add2.pack(pady=400, padx=400)
    boton_add2.place(x=595, y=160)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',
                    background='#D3D3D3',
                    foreground='black',
                    rowheight=25,
                    fieldbackground='#D3D3D3',
                    font=('Times New Roman', 12))
    style.configure('Treeview.Heading', font=('Times New Roman', 12))

    style.map('Treeview',
              background=[('selected', '#347083')])

    tree_frame = Frame(frame)
    tree_frame.pack(pady=70)
    tree_frame.place(x=70, y=200)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('Nombre', 'Descripción', 'Existencia', 'Costo/U')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Nombre', anchor=W, stretch=NO)
    my_tree.column('Descripción', anchor=W)
    my_tree.column('Existencia', anchor=W, stretch=NO, width=120)
    my_tree.column('Costo/U', anchor=W, stretch=NO, width=120)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Nombre', text='Nombre', anchor=W)
    my_tree.heading('Descripción', text='Descripción', anchor=W)
    my_tree.heading('Existencia', text='Existencia', anchor=W)
    my_tree.heading('Costo/U', text='Costo/U', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')

    # EVENTO CUANDO SE ESCRIBE EN EL TEXT BOX

    data_ = []
    conexion = sqlite3.connect('src/database')
    cursor = conexion.cursor()
    cursor.execute('SELECT Nombre, Descripción, Cantidad, costo_uni FROM objetos_de_inventario WHERE servicio = 0')
    rows = cursor.fetchall()
    for row in rows:
        data_.append(row)

    count = 0

    for record in data_:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], str(record[2]) + ' unidades'
                                   , 'Q' + str(record[3])), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], str(record[2]) + ' unidades'
                                   , 'Q' + str(record[3])), tags=('oddrow',))
        count += 1

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',
                    background='#D3D3D3',
                    foreground='black',
                    rowheight=25,
                    fieldbackground='#D3D3D3',
                    font=('Times New Roman', 12))
    style.configure('Treeview.Heading', font=('Times New Roman', 12))

    style.map('Treeview',
              background=[('selected', '#347083')])

    tree_frame = Frame(frame)
    tree_frame.pack(pady=70)
    tree_frame.place(x=850, y=80)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('Nombre', 'Cantidad')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Nombre', anchor=W, stretch=NO)
    my_tree.column('Cantidad', anchor=W)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Nombre', text='Nombre', anchor=W)
    my_tree.heading('Cantidad', text='Cantidad', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')

    # EVENTO CUANDO SE ESCRIBE EN EL TEXT BOX



def labels_parte3(frame):
    lb_sub_total = customtkinter.CTkLabel(master=frame, text='Sub Total:  ', font=("Times New Roman", 40, "bold"))
    lb_sub_total.pack(pady=400, padx=400, )
    lb_sub_total.place(x=10, y=10)

    lb_descuento_total = customtkinter.CTkLabel(master=frame, text='Descuento:  ', font=("Times New Roman", 40, "bold"))
    lb_descuento_total.pack(pady=400, padx=400, )
    lb_descuento_total.place(x=10, y=60)

    lb_total = customtkinter.CTkLabel(master=frame, text='TOTAL:  ', font=("Times New Roman", 40, "bold"))
    lb_total.pack(pady=400, padx=400, )
    lb_total.place(x=10, y=110)

    factura_button = customtkinter.CTkButton(master=frame, font=("Times New Roman", 18), text='Facturar', height=100)
    factura_button.pack(pady=400, padx=400, )
    factura_button.place(x=870, y=45)

    cotizar_button = customtkinter.CTkButton(master=frame, font=("Times New Roman", 18), text='Cotizar', height=100)
    cotizar_button.pack(pady=400, padx=400, )
    cotizar_button.place(x=700, y=45)

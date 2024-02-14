import random
from tkinter import ttk
from tkinter import *
import customtkinter
import sqlite3
global texto_imagen
global lista_sumatoria


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
    labels_parte1(frame)
    labels_parte2(frame2, frame3)
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

    entry_name = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 15),
                                        placeholder_text='Ingrese el Nombre.')
    entry_name.pack(pady=400, padx=400, )
    entry_name.place(x=175, y=107)

    lb_nit = customtkinter.CTkLabel(master=frame, text='Nit', font=("Times New Roman", 30))
    lb_nit.pack(pady=400, padx=400, )
    lb_nit.place(x=10, y=145)

    lb_ciudad = customtkinter.CTkLabel(master=frame, text='Dirección', font=("Times New Roman", 30))
    lb_ciudad.pack(pady=400, padx=400, )
    lb_ciudad.place(x=350, y=60)

    entry_nit = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 15),
                                       placeholder_text='Ingrese NIT.')
    entry_nit.pack(pady=400, padx=400, )
    entry_nit.place(x=175, y=149)

    entry_dress = customtkinter.CTkEntry(master=frame, font=("Times New Roman", 15),
                                         placeholder_text='Ingrese la Ciudad')
    entry_dress.pack(pady=400, padx=400, )
    entry_dress.place(x=480, y=65)

    confirm_button = customtkinter.CTkButton(master=frame, font=("Times New Roman", 18), text='Confirmar cliente',
                                             height=40)
    confirm_button.pack(pady=400, padx=400, )
    confirm_button.place(x=350, y=140)


def labels_parte2(frame, frame_3):
    # selected record
    def select_record(tipo):
        selected = my_tree_2.focus()
        values = my_tree_2.item(selected, 'values')
        if tipo == 1:
            return values[0]
        elif tipo == 2:
            return values[3]

    data_ = []
    conexion = sqlite3.connect('src/database')
    cursor = conexion.cursor()
    cursor.execute('SELECT Nombre FROM objetos_de_inventario WHERE servicio = 1')
    rows = cursor.fetchall()
    for row in rows:
        data_.append(row[0])

    conexion.close()

    lb_cantidad = customtkinter.CTkLabel(master=frame, text='Cantidad: ', font=("Times New Roman", 40))
    lb_cantidad.pack(pady=400, padx=400, )
    lb_cantidad.place(x=310, y=10)

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
        servicio = str(combo_box.get())
        cantidad = int(ib_cantidad.get())
        if servicio == "Prueba de Orientación Vocacional":
            precio_1 = 250
        elif servicio == "Terapia Individual":
            precio_1 = 150
        elif servicio == "Terapia de Pareja":
            precio_1 = 200
        elif servicio == "Pruebas de IQ":
            precio_1 = 150
        elif servicio == "Test de Ansiedad STAI":
            precio_1 = 150
        total = precio_1 * cantidad
        print(total)
        my_tree.insert('', 'end', values=(servicio, cantidad, precio_1, total))

    boton_add = customtkinter.CTkButton(master=frame,  text='Añadir servicio', font=("Times New Roman", 12, "bold")
                                        , command=get_service)
    boton_add.pack(pady=400, padx=400)
    boton_add.place(x=510, y=70)

    ib_cantidad = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese la cantidad')
    ib_cantidad.pack(pady=12, padx=10)
    ib_cantidad.place(x=315, y=70)

    def get_service_2():
        nombre = select_record(1)
        cantidad = 1
        precio = int(select_record(2))
        total = precio * cantidad
        my_tree.insert('', 'end', values=(nombre, cantidad, precio, total))

    boton_add2 = customtkinter.CTkButton(master=frame, text='+', font=("Times New Roman", 40, "bold"), width=55,
                                         command=get_service_2)
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

    my_tree_2 = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    my_tree_2.pack()

    tree_scroll.config(command=my_tree_2.yview)

    my_tree_2['columns'] = ('Nombre', 'Descripción', 'Existencia', 'Costo/U')

    my_tree_2.column('#0', width=0, stretch=NO)
    my_tree_2.column('Nombre', anchor=W, stretch=NO)
    my_tree_2.column('Descripción', anchor=W)
    my_tree_2.column('Existencia', anchor=W, stretch=NO, width=120)
    my_tree_2.column('Costo/U', anchor=W, stretch=NO, width=120)

    my_tree_2.heading('#0', text='', anchor=W)
    my_tree_2.heading('Nombre', text='Nombre', anchor=W)
    my_tree_2.heading('Descripción', text='Descripción', anchor=W)
    my_tree_2.heading('Existencia', text='Existencia', anchor=W)
    my_tree_2.heading('Costo/U', text='Costo/U', anchor=W)

    my_tree_2.tag_configure('oddrow', background='white')
    my_tree_2.tag_configure('evenrow', background='lightblue')

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
            my_tree_2.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], str(record[2]) + ' unidades'
                                   , str(record[3])), tags=('evenrow',))
        else:
            my_tree_2.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], str(record[2]) + ' unidades'
                                   , str(record[3])), tags=('oddrow',))
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

    my_tree['columns'] = ('Nombre', 'Cantidad', 'Precio', 'Total')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Nombre', anchor=W, stretch=NO)
    my_tree.column('Cantidad', anchor=W, width=75)
    my_tree.column('Precio', anchor=W, width=125)
    my_tree.column('Total', anchor=W, width=125)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Nombre', text='Nombre', anchor=W)
    my_tree.heading('Cantidad', text='Cantidad', anchor=W)
    my_tree.heading('Precio', text='Precio', anchor=W)
    my_tree.heading('Total', text='Total', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')

    def obtener_columna(columna):
        valores_columna = []
        for item in my_tree.get_children():
            valor = my_tree.item(item, "values")[columna]
            valores_columna.append(valor)
        return valores_columna

    def generar_matriz():
        columna1 = obtener_columna(3)
        sub_total = 0
        descuento = 0
        for i in columna1:
            sub_total += int(i)
        total_final = sub_total - descuento
        label_subtotal = customtkinter.CTkLabel(master=frame_3, text=str(sub_total), font=("Times New Roman", 40, "bold"))
        label_subtotal.pack(pady=400, padx=400, )
        label_subtotal.place(x=300, y=10)

        label_descuento = customtkinter.CTkLabel(master=frame_3, text=str(descuento), font=("Times New Roman", 40, "bold"))
        label_descuento.pack(pady=400, padx=400, )
        label_descuento.place(x=300, y=60)

        label_total = customtkinter.CTkLabel(master=frame_3, text=str(total_final), font=("Times New Roman", 40, "bold"))
        label_total.pack(pady=400, padx=400, )
        label_total.place(x=300, y=110)

    button_generar = customtkinter.CTkButton(master=frame, text='CONFIRMAR', font=("Times New Roman", 30, "bold"),
                                             width=15, command=generar_matriz)
    button_generar.pack(pady=12, padx=10)
    button_generar.place(x=680, y=300)

    def factura():
        pass

        def base_de_datos():

            pass



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

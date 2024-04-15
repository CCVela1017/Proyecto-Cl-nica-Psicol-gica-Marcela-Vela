import customtkinter
from tkinter import ttk
from tkinter import *
from financiero.pdf_balance import BalancePDF
import datetime
import sqlite3

caja = 0
bancos = 0
papeleria = 0
mob = 0
patriomonio = 17590
utilidades = 0
mes = ''
anio = datetime.datetime.now().year

def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def frame_2(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=0, padx=60, fill='both', ipady=80, side='top')
    return frame


def frame_3(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=0, padx=60, fill='both', ipady=80, side='bottom')
    return frame


def cargar_datos():
    root = customtkinter.CTkToplevel()

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root.title("Balance general")
    root.iconbitmap('icon.ico')
    root.wm_attributes("-topmost", True)
    root.geometry('800x465')

    return root


def main_balance():
    root = cargar_datos()
    frame = customtkinter.CTkFrame(master=root)
    root.wm_attributes("-topmost", False)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    cargar_tabla_ac(frame)
    cargar_tabla_anc(frame)
    cargar_tabla_otros(frame)
    labels_entry(frame)

    btn_print = customtkinter.CTkButton(master=frame, text='Imprimir PDF', width=475, command=print_balance,
                                        state='normal')
    btn_print.pack(pady=100, padx=10)
    btn_print.place(x=140, y=390)

    root.mainloop()


def print_balance():
    # Ejemplo de balance
    dict_balance = {
        'month': str(mes),
        'year': str(anio),
        'caja': str(caja),
        'banco': str(bancos),
        'papeleria': str(papeleria),
        'mobiliario': str(mob),
        'capital_s': str(patriomonio),
        'utilidades_r': str(round(utilidades, 2)),
        'total': str(caja + bancos + papeleria + mob),
    }
    pddf = BalancePDF(dict_balance)
    pddf.print_balance()


def cargar_tabla_anc(frame):
    def activo_nc() -> int:
        try:

            mob_equip1 = 0

            conexion2 = sqlite3.connect('src/database')
            cursor1 = conexion2.cursor()
            cursor1.execute("SELECT cantidad *  (costo - (costo * 0.2)) FROM objetos_de_equipo WHERE ID <= 7")
            filas_mob = cursor1.fetchall()

            for fila in filas_mob:
                mob_equip1 += fila[0]

            conexion2.close()

            return mob_equip1

        except Exception as ex:
            print(ex)

    style = ttk.Style()

    style.theme_use("default")

    style.configure("Treeview",
                    background="#2a2d2e",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#343638",
                    bordercolor="#343638",
                    borderwidth=0,
                    font=('Times New Roman', 15))
    style.map('Treeview', background=[('selected', '#22559b')])

    style.configure("Treeview.Heading",
                    background="#565b5e",
                    foreground="white",
                    relief="flat",
                    font=('Times New Roman', 15))
    style.map("Treeview.Heading",
              background=[('active', '#3484F0')])

    tree_frame = ttk.Frame(frame)
    tree_frame.pack(pady=25)
    tree_frame.place(y=220, x=180)

    my_tree = ttk.Treeview(tree_frame, selectmode='extended', height=1)

    my_tree.pack()

    my_tree['columns'] = ('Código', 'Cuenta', 'Débito', 'Crédito')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Código', anchor=W, stretch=NO, width=65)
    my_tree.column('Cuenta', anchor=W, stretch=NO)
    my_tree.column('Débito', anchor=W, stretch=NO)
    my_tree.column('Crédito', anchor=W, stretch=NO, width=120)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Código', text='Código', anchor=W)
    my_tree.heading('Cuenta', text='Cuenta', anchor=W)
    my_tree.heading('Débito', text='Débito', anchor=W)
    my_tree.heading('Crédito', text='Crédito', anchor=W)

    '''Vector de ejemplo'''
    global mob
    mob = activo_nc()

    data = [['1224', 'Mobiliario y Equipo', str(mob), '']]

    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        count += 1

    return


def cargar_tabla_ac(frame):
    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',
                    background='#D3D3D3',
                    foreground='black',
                    rowheight=25,
                    fieldbackground='#D3D3D3')
    style.map('Treeview',
              background=[('selected', '#347083')])

    tree_frame = Frame(frame)
    tree_frame.pack(pady=25)
    tree_frame.place(y=70, x=180)

    my_tree = ttk.Treeview(tree_frame, selectmode='extended', height=3)
    my_tree.pack()

    my_tree['columns'] = ('Código', 'Cuenta', 'Débito', 'Crédito')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Código', anchor=W, stretch=NO, width=65)
    my_tree.column('Cuenta', anchor=W, stretch=NO)
    my_tree.column('Débito', anchor=W, stretch=NO)
    my_tree.column('Crédito', anchor=W, stretch=NO, width=120)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Código', text='Código', anchor=W)
    my_tree.heading('Cuenta', text='Cuenta', anchor=W)
    my_tree.heading('Débito', text='Débito', anchor=W)
    my_tree.heading('Crédito', text='Crédito', anchor=W)

    '''Vector de ejemplo'''
    def activos() -> tuple:
        try:

            caja1 = 0
            bancos1 = 0
            papeleria1 = 0

            conexion = sqlite3.connect('src/database')
            cursor = conexion.cursor()
            fecha = datetime.datetime.now()
            global mes
            mes = fecha.month
            cursor.execute("SELECT monto_total FROM facturas_ventas WHERE mes = ? and forma_pago = 'Caja'"
                           , (str(mes),))
            filas_caja = cursor.fetchall()

            for fila in filas_caja:
                caja1 += fila[0]

            cursor.execute("SELECT monto_total FROM facturas_ventas WHERE mes = ? and forma_pago = 'Transferencia'"
                           , (str(mes),))

            filas_banco = cursor.fetchall()

            for fila in filas_banco:
                bancos1 += fila[0]

            cursor.execute("SELECT costo_uni * cantidad FROM objetos_de_inventario WHERE "
                           "Nombre = 'Hojas de pruebas proyectivas'")

            filas_papeles = cursor.fetchall()

            for fila in filas_papeles:
                papeleria1 += fila[0]

            conexion.close()

            return caja1, bancos1, papeleria1

        except Exception as ex:
            print(ex)
    global caja
    caja = activos()[0]
    global bancos
    bancos = activos()[1]
    global papeleria
    papeleria = activos()[2]

    data = [['1111', 'Caja', str(caja), ''],
            ['1112', 'Bancos', str(bancos), ''],
            ['1174', 'Papelería y útiles', str(papeleria), '']]

    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        count += 1

    return


def cargar_tabla_otros(frame):
    style = ttk.Style()

    style.theme_use("default")

    style.configure("Treeview",
                    background="#2a2d2e",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#343638",
                    bordercolor="#343638",
                    borderwidth=0,
                    font=('Times New Roman', 15))
    style.map('Treeview', background=[('selected', '#22559b')])

    style.configure("Treeview.Heading",
                    background="#565b5e",
                    foreground="white",
                    relief="flat",
                    font=('Times New Roman', 15))
    style.map("Treeview.Heading",
              background=[('active', '#3484F0')])

    tree_frame = Frame(frame)
    tree_frame.pack(pady=25)
    tree_frame.place(y=315, x=180)

    my_tree = ttk.Treeview(tree_frame, selectmode='extended', height=2)
    my_tree.pack()

    my_tree['columns'] = ('Código', 'Cuenta', 'Débito', 'Crédito')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('Código', anchor=W, stretch=NO, width=65)
    my_tree.column('Cuenta', anchor=W, stretch=NO)
    my_tree.column('Débito', anchor=W, stretch=NO)
    my_tree.column('Crédito', anchor=W, stretch=NO, width=120)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('Código', text='Código', anchor=W)
    my_tree.heading('Cuenta', text='Cuenta', anchor=W)
    my_tree.heading('Débito', text='Débito', anchor=W)
    my_tree.heading('Crédito', text='Crédito', anchor=W)

    '''Vector de ejemplo'''
    global utilidades
    utilidades = caja + bancos + papeleria + mob - patriomonio

    data = [['3210', 'Capital Social', '', '17590'],
            ['', 'Utilidades retenidas', '', round(utilidades, 2)]]

    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
        count += 1

    return


def labels_entry(frame):
    lb_ac = customtkinter.CTkLabel(master=frame, text="Activos Corrientes: ", font=("Times New Roman", 20))
    lb_ac.pack(pady=400, padx=400)
    lb_ac.place(x=145, y=20)

    lb_nac = customtkinter.CTkLabel(master=frame, text="Activos No Corrientes: ", font=("Times New Roman", 20))
    lb_nac.pack(pady=400, padx=400)
    lb_nac.place(x=145, y=140)

    lb_otras = customtkinter.CTkLabel(master=frame, text="Patrimonio Neto: ", font=("Times New Roman", 20))
    lb_otras.pack(pady=400, padx=400)
    lb_otras.place(x=145, y=220)

    lb_sumas = customtkinter.CTkLabel(master=frame, text="Sumas Iguales: ", font=("Times New Roman", 20))
    lb_sumas.pack(pady=400, padx=400)
    lb_sumas.place(x=145, y=340)

    en_cred = customtkinter.CTkEntry(master=frame, width=100,
                                     height=10, placeholder_text=str(caja + bancos + papeleria + mob))
    en_cred.pack(pady=100, padx=10)
    en_cred.place(x=350, y=345)

    en_deb = customtkinter.CTkEntry(master=frame, width=100,
                                    height=10, placeholder_text=str(patriomonio + utilidades))
    en_deb.pack(pady=100, padx=10)
    en_deb.place(x=510, y=345)

import customtkinter
import sqlite3
from tkinter import ttk
from tkinter import *


def cargar_base_de_datos():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM estado_de_resultados')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        return data
    except Exception as ex:
        print(ex)

def front_end(frame, frame2):

    def filter_table(event):
        filtro = str(txt_id.get())
        my_tree.delete(*my_tree.get_children())

        # Filtrar y mostrar solo las filas que contienen el filtro
        for fila in data:
            if filtro.lower() in str(fila[4]):  # Suponiendo que la primera columna es la que queremos filtrar
                my_tree.insert('', 'end', values=fila)

        # COLOREA LAS TABLAS QUE SE FILTRAN

        for idx, fila_id in enumerate(my_tree.get_children()):
            if idx % 2 == 0:
                my_tree.item(fila_id, tags=('evenrow',))
            else:
                my_tree.item(fila_id, tags=('oddrow',))

    lb_historial = customtkinter.CTkLabel(master=frame, text='Historial de Resultados', font=("Times New Roman", 20))
    lb_historial.pack(pady=400, padx=400, )
    lb_historial.place(x=10, y=10)

    lb_busqueda = customtkinter.CTkLabel(master=frame, text='Busqueda por fecha: ', font=("Times New Roman", 20))
    lb_busqueda.pack(pady=400, padx=400, )
    lb_busqueda.place(x=10, y=50)

    txt_id = customtkinter.CTkEntry(master=frame, placeholder_text='Mes, Año')
    txt_id.pack(pady=12, padx=10)
    txt_id.place(x=200, y=50)

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

    tree_frame = ttk.Frame(frame2)
    tree_frame.pack(pady=25)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')

    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('ID', 'Comprado', 'Vendido', 'Utilidad Bruta', 'Fecha', 'Total con IVA', 'Total sin IVA')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('ID', anchor=W, stretch=NO, width=35)
    my_tree.column('Comprado', anchor=W, stretch=NO)
    my_tree.column('Vendido', anchor=W, stretch=NO)
    my_tree.column('Utilidad Bruta', anchor=W, stretch=NO)
    my_tree.column('Fecha', anchor=W, stretch=NO, width=120)
    my_tree.column('Total con IVA', anchor=W, stretch=NO)
    my_tree.column('Total sin IVA', anchor=W, stretch=NO)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('ID', text='ID', anchor=W)
    my_tree.heading('Comprado', text='Comprado', anchor=W)
    my_tree.heading('Vendido', text='Vendido', anchor=W)
    my_tree.heading('Utilidad Bruta', text='Utilidad Bruta', anchor=W)
    my_tree.heading('Fecha', text='Fecha', anchor=W)
    my_tree.heading('Total con IVA', text='Total con IVA', anchor=W)
    my_tree.heading('Total sin IVA', text='Total sin IVA', anchor=W)

    data = cargar_base_de_datos()

    # EVENTO CUANDO SE ESCRIBE EN EL TEXT BOX

    txt_id.bind("<KeyRelease>", filter_table)

    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], 'Q' + str(record[1]), 'Q' + str(record[2]), 'Q' + str(record[3]),
                                   record[4], 'Q' + str(round(record[5], 1)), 'Q' + str(record[6])), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], 'Q' + str(record[1]), 'Q' + str(record[2]), 'Q' + str(record[3]),
                                   record[4], 'Q' + str(round(record[5], 1)), 'Q' + str(record[6])), tags=('ODDROW',))
        count += 1

    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTkToplevel()
    root.wm_attributes("-topmost", True)
    root.title("Historial de Resultados")
    root.iconbitmap('icon.ico')
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, height=200, width=20)
    frame2.pack(pady=130, padx=10, fill='both', expand=True)

    front_end(frame, frame2)

    root.geometry('1300x550')
    root.mainloop()

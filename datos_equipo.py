import customtkinter
import sqlite3
from tkinter import ttk
from tkinter import *


def cargar_base_de_datos():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM objetos_de_equipo')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            data.append(row)
        return data
    except Exception as ex:
        print(ex)

def front_end(frame, frame2):

    lb_datos_inventario = customtkinter.CTkLabel(master=frame, text='Equipo', font=("Times New Roman", 20))
    lb_datos_inventario.pack(pady=400, padx=400, )
    lb_datos_inventario.place(x=10, y=10)

    lb_busqueda = customtkinter.CTkLabel(master=frame, text='Busqueda ', font=("Times New Roman", 20))
    lb_busqueda.pack(pady=400, padx=400, )
    lb_busqueda.place(x=10, y=50)

    cb_busqueda = customtkinter.CTkComboBox(master=frame, font=("Times New Roman", 20),
                                            values=['ID', 'Nombre'])
    cb_busqueda.pack(pady=400, padx=400, )
    cb_busqueda.place(x=400, y=10)

    lb_combo = customtkinter.CTkLabel(master=frame, text='Buscar por: ', font=("Times New Roman", 20))
    lb_combo.pack(pady=400, padx=400, )
    lb_combo.place(x=300, y=10)

    txt_id = customtkinter.CTkEntry(master=frame, placeholder_text='Buscar')
    txt_id.pack(pady=12, padx=10)
    txt_id.place(x=100, y=50)

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

    tree_frame = Frame(frame2)
    tree_frame.pack(pady=10)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')
    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('ID', 'Nombre', 'Caracteristicas', 'Costo sin IVA', 'Costo con IVA', 'No.Serie')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('ID', anchor=W, stretch=NO)
    my_tree.column('Nombre', anchor=W, stretch=NO)
    my_tree.column('Caracteristicas', anchor=W, stretch=NO)
    my_tree.column('Costo sin IVA', anchor=W, stretch=NO)
    my_tree.column('Costo con IVA', anchor=W, stretch=NO)
    my_tree.column('No.Serie', anchor=W, stretch=NO)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('ID', text='ID', anchor=W)
    my_tree.heading('Nombre', text='Nombre', anchor=W)
    my_tree.heading('Caracteristicas', text='Caracteristicas', anchor=W)
    my_tree.heading('Costo sin IVA', text='Costo sin IVA', anchor=W)
    my_tree.heading('Costo con IVA', text='Costo con IVA', anchor=W)
    my_tree.heading('No.Serie', text='No.Serie', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')

    data = cargar_base_de_datos()

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3],
                                   record[4], record[5]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3],
                                   record[4], record[5]), tags=('oddrow',))
        count += 1

    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.title("Datos de Equipo")
    root.iconbitmap('icon.ico')
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, height=200, width=20)
    frame2.pack(pady=100, padx=10, fill='both', expand=True)

    front_end(frame, frame2)

    root.geometry('1280x550')
    root.mainloop()


main_window()

import customtkinter
import sqlite3
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import os
from io import BytesIO


def cargar_base_de_datos():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM objetos_de_inventario WHERE servicio = 0')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        return data
    except Exception as ex:
        print(ex)


def add_image(frame):
    image_path = os.path.join(os.path.dirname(__file__), 'icon.png')
    image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100, 100))
    image_label = customtkinter.CTkLabel(master=frame, image=image, text='')
    image_label.place(x=800, y=10)

    return


def front_end(frame, frame2):
    def show_image(event):
        y = event.y
        item = int(my_tree.identify_row(y))
        serie_row = data[item][6]

        # extrae la imagen desde la base de datos
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute("SELECT Imagen FROM objetos_de_inventario WHERE Serie = ?", (serie_row,))

        datos_imagen = cursor.fetchone()[0]

        if datos_imagen:
            image = customtkinter.CTkImage(light_image=Image.open(BytesIO(datos_imagen)), size=(100, 100))
        else:
            image_path = os.path.join(os.path.dirname(__file__), 'icon.png')
            image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(100, 100))
            pass

        image_label = customtkinter.CTkLabel(master=frame, image=image, text='')
        image_label.place(x=800, y=10)

        conexion.close()

    def filter_table(event):

        i = 0
        if cb_busqueda.get() == 'ID':
            pass
        elif cb_busqueda.get() == 'Nombre':
            i = 1
        filtro = str(txt_id.get())
        my_tree.delete(*my_tree.get_children())

        # Filtrar y mostrar solo las filas que contienen el filtro
        for fila in data:

            if i == 0:
                if filtro.lower() in str(fila[i]):  # Suponiendo que la primera columna es la que queremos filtrar
                    my_tree.insert('', 'end', values=fila)
            else:
                if filtro.lower() in str(fila[i].lower()):
                    my_tree.insert('', 'end', values=fila)

        # COLOREA LAS TABLAS QUE SE FILTRAN

        for idx, fila_id in enumerate(my_tree.get_children()):
            if idx % 2 == 0:
                my_tree.item(fila_id, tags=('evenrow',))
            else:
                my_tree.item(fila_id, tags=('oddrow',))

    lb_datos_inventario = customtkinter.CTkLabel(master=frame, text='Inventarios', font=("Times New Roman", 20))
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

    lb_image = customtkinter.CTkLabel(master=frame, text='Imagen:\nejemplo ', font=("Times New Roman", 20))
    lb_image.pack(pady=400, padx=400, )
    lb_image.place(x=700, y=10)

    add_image(frame)

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
    tree_frame.pack(pady=25)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended')

    my_tree.pack()

    tree_scroll.config(command=my_tree.yview)

    my_tree['columns'] = ('ID', 'Nombre', 'Descripción', 'Costo', 'Cantidad', 'Proveedor', 'Serie')

    my_tree.column('#0', width=0, stretch=NO)
    my_tree.column('ID', anchor=W, stretch=NO, width=45)
    my_tree.column('Nombre', anchor=W, stretch=NO)
    my_tree.column('Descripción', anchor=W, stretch=NO)
    my_tree.column('Costo', anchor=W, stretch=NO, width=120)
    my_tree.column('Cantidad', anchor=W, stretch=NO, width=120)
    my_tree.column('Proveedor', anchor=W, stretch=NO)
    my_tree.column('Serie', anchor=W, stretch=NO)

    my_tree.heading('#0', text='', anchor=W)
    my_tree.heading('ID', text='ID', anchor=W)
    my_tree.heading('Nombre', text='Nombre', anchor=W)
    my_tree.heading('Descripción', text='Descripción', anchor=W)
    my_tree.heading('Costo', text='Costo', anchor=W)
    my_tree.heading('Cantidad', text='Cantidad', anchor=W)
    my_tree.heading('Proveedor', text='Proveedor', anchor=W)
    my_tree.heading('Serie', text='Serie', anchor=W)

    my_tree.tag_configure('oddrow', background='white')
    my_tree.tag_configure('evenrow', background='lightblue')

    data = cargar_base_de_datos()

    # EVENTO CUANDO SE ESCRIBE EN EL TEXT BOX

    txt_id.bind("<KeyRelease>", filter_table)

    my_tree.bind("<ButtonRelease-1>", show_image)


    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3],
                                   record[4], record[5], record[6]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3],
                                   record[4], record[5], record[6]), tags=('oddrow',))
        count += 1

    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTkToplevel()
    root.wm_attributes("-topmost", True)
    root.title("Datos de Inventario")
    root.iconbitmap('icon.ico')
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, height=200, width=20)
    frame2.pack(pady=130, padx=10, fill='both', expand=True)

    front_end(frame, frame2)

    root.geometry('1280x550')
    root.mainloop()

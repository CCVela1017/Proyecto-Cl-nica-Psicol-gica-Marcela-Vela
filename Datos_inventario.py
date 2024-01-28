import customtkinter
import sqlite3
from tkinter import ttk


def main():
    # creación de ventana y cosas basicas
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    root = customtkinter.CTk()
    root.title("Datos de inventario")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    # cargar frontend
    front_end(frame)

    root.geometry("1280x720")
    root.mainloop()
    return


def cargar_base_de_datos(table):
    try:
        conexion = sqlite3.connect("src/database")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM objetos_de_inventario")
        rows = cursor.fetchall()
        for row in rows:
            data = row
            table.insert(parent='', index=0, values=data)

    except Exception as ex:
        print(ex)

    return


def front_end(frame):

    # front
    # labels
    lb_datos_inventario = customtkinter.CTkLabel(master=frame, text='Datos de inventario', font=("Arial", 20))
    lb_datos_inventario.pack(pady=400, padx=400,)
    lb_datos_inventario.place(x=10, y=10)

    lb_busqueda = customtkinter.CTkLabel(master=frame, text='Busqueda ', font=("Arial", 20))
    lb_busqueda.pack(pady=400, padx=400,)
    lb_busqueda.place(x=10, y=50)

    # text boxs
    txt_id = customtkinter.CTkEntry(master=frame, placeholder_text='ID de objeto')
    txt_id.pack(pady=12, padx=10)
    txt_id.place(x=120, y=50)

    # generar tablas

    table = ttk.Treeview(master=frame, columns=('ID', 'Nombre', 'Caracteristicas'), show='headings')
    table.heading('ID', text='ID')
    table.heading('Nombre', text='Nombre')
    table.heading('Caracteristicas', text='Caracteristicas')
    table.pack()
    table.place(x=0, y=150)
    cargar_base_de_datos(table)
    return


main()

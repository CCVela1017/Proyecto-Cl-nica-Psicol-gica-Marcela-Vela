import customtkinter

from tkinter import ttk


def front_end(frame):
    lb_datos_inventario = customtkinter.CTkLabel(master=frame, text='Equipo', font=("Arial", 20))
    lb_datos_inventario.pack(pady=400, padx=400, )
    lb_datos_inventario.place(x=10, y=10)

    lb_busqueda = customtkinter.CTkLabel(master=frame, text='Busqueda ', font=("Arial", 20))
    lb_busqueda.pack(pady=400, padx=400, )
    lb_busqueda.place(x=10, y=50)

    txt_id = customtkinter.CTkEntry(master=frame, placeholder_text='ID de objeto')
    txt_id.pack(pady=12, padx=10)
    txt_id.place(x=120, y=50)

    table = ttk.Treeview(master=frame, columns=('ID', 'Nombre', 'Caracteristicas', 'Costo sin IVA',
                                                'Costo con IVA', 'No.Serie'), show='headings')
    table.heading('ID', text='ID')
    table.heading('Nombre', text='Nombre')
    table.heading('Caracteristicas', text='Caracteristicas')
    table.heading('Costo sin IVA', text='Costo sin IVA')
    table.heading('Costo con IVA', text='Costo con IVA')
    table.heading('No.Serie', text='No.Serie')
    table.pack()
    table.place(x=0, y=150)

    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.title("Datos de Equipo")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    front_end(frame)

    root.geometry('1280x720')
    root.mainloop()


main_window()

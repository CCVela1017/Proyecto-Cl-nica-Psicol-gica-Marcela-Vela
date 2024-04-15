import sqlite3
from tkinter import messagebox

import customtkinter
import datetime


def cargar_base_de_datos_utilidad_bruta():
    try:
        data = []
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM utilidad_bruta')
        rows = cursor.fetchall()
        for row in rows:
            data.append(row)
        lista = []
        for item in data:
            contador = 0
            for datos in item:
                if contador == 6:
                    lista.append(datos)
                contador += 1
        return lista
    except Exception as ex:
        print(ex)


def main_utilidad():
    root = customtkinter.CTk()
    lista_de_fechas = cargar_base_de_datos_utilidad_bruta()
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    editar = False
    root.title("Utilidad Bruta")
    root.iconbitmap('icon.ico')
    frame = customtkinter.CTkFrame(master=root)
    root.wm_attributes("-topmost", True)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, fg_color="#212121", width=50)
    frame2.pack(pady=10, padx=8, fill='both', expand=True, side='right')

    fecha_actual = datetime.datetime.now()
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year

    fecha = str(mes_actual) + str(anio_actual)

    ib_alquiler = customtkinter.CTkEntry(master=frame, placeholder_text='A')
    ib_alquiler.pack(pady=12, padx=10)
    ib_alquiler.place(x=150, y=75)

    ib_energeticos = customtkinter.CTkEntry(master=frame, placeholder_text='E')
    ib_energeticos.pack(pady=12, padx=10)
    ib_energeticos.place(x=150, y=110)

    ib_transporte = customtkinter.CTkEntry(master=frame, placeholder_text='T')
    ib_transporte.pack(pady=12, padx=10)
    ib_transporte.place(x=150, y=145)

    ib_red = customtkinter.CTkEntry(master=frame, placeholder_text='R')
    ib_red.pack(pady=12, padx=10)
    ib_red.place(x=150, y=180)

    ib_planillla = customtkinter.CTkEntry(master=frame, placeholder_text='P', state="disabled")
    ib_planillla.pack(pady=12, padx=10)
    ib_planillla.place(x=150, y=210)

    def guardar_datos():
        global editar
        alquiler = int(ib_alquiler.get())
        energia = int(ib_energeticos.get())
        transporte = int(ib_transporte.get())
        red = int(ib_red.get())
        root.geometry('370x365')
        total = int(alquiler + energia + transporte + red)

        lb_total = customtkinter.CTkLabel(master=frame, text='Total: ' + str(total), font=(" ", 25))
        lb_total.pack(pady=400, padx=400)
        lb_total.place(x=10, y=275)

        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        for i in lista_de_fechas:
            if str(i) == str(fecha):
                editar = True

        if editar is False:
            try:
                cursor.execute("INSERT INTO utilidad_bruta (costo_alquiler, "
                               "costo_energia, "
                               "costo_transporte, "
                               "costo_red, "
                               "costo_planilla, "
                               "fecha, "
                               "total) "
                               "VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (alquiler, energia, transporte, red, 0, fecha, total))
                messagebox.showinfo('¡Datos Ingresados Correctamente!', 'Los datos ingresados fueron '
                                                                        'enviados correctamente a la base de datos.')

            except Exception as ex:
                messagebox.showerror('¡Datos Ingresados Incorrectamente!', 'Vaya, parece que un campo '
                                                                           'no coincide con la base de datos, verifica los '
                                                                           'datos ingresados.')

                print(ex)
                conexion.commit()
                conexion.close()

        else:
            try:
                cursor.execute("UPDATE utilidad_bruta SET costo_alquiler = ?, "
                               "costo_energia = ?, "
                               "costo_transporte = ?, "
                               "costo_red = ?, "
                               "costo_planilla = ?, "
                               "fecha = ?, "
                               "total = ?",
                               (alquiler, energia, transporte, red, 0, fecha, total))
                conexion.commit()  # Guarda los cambios en la base de datos
                messagebox.showinfo('¡Datos Modificados Correctamente!',
                                    'Los datos ingresados fueron enviados correctamente a la base de datos.')
            except sqlite3.Error as ex:
                messagebox.showerror('¡Error al Modificar Datos!',
                                     'parece que un campo no coincide con la base de datos, verifica los datos ingresados.')
                print(ex)
            finally:
                if conexion:
                    conexion.close()

    button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar",
                                               command=guardar_datos)
    button_confirmar.pack(pady=10, padx=10)
    button_confirmar.place(x=150, y=250)

    labels(frame)

    frame.pack()
    root.geometry('370x350')
    root.mainloop()


def labels(frame):
    lb_utilidad_bruta = customtkinter.CTkLabel(master=frame, text='Utilidad Bruta',
                                               font=("Times New Roman", 50, "bold"))
    lb_utilidad_bruta.pack(pady=400, padx=400, )
    lb_utilidad_bruta.place(x=10, y=0)

    lb_alquiler = customtkinter.CTkLabel(master=frame, text='Alquiler', font=(" ", 25))
    lb_alquiler.pack(pady=400, padx=400, )
    lb_alquiler.place(x=10, y=75)

    lb_energeticos = customtkinter.CTkLabel(master=frame, text='Energeticos', font=(" ", 25))
    lb_energeticos.pack(pady=400, padx=400, )
    lb_energeticos.place(x=10, y=110)

    lb_transporte = customtkinter.CTkLabel(master=frame, text='Transporte', font=(" ", 25))
    lb_transporte.pack(pady=400, padx=400)
    lb_transporte.place(x=10, y=145)

    lb_red = customtkinter.CTkLabel(master=frame, text='Red', font=(" ", 25))
    lb_red.pack(pady=400, padx=400)
    lb_red.place(x=10, y=180)

    lb_planilla = customtkinter.CTkLabel(master=frame, text='Planilla', font=(" ", 25))
    lb_planilla.pack(pady=400, padx=400)
    lb_planilla.place(x=10, y=210)

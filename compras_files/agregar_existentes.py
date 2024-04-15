import customtkinter
from tkcalendar import DateEntry


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    # inputbox box
    ib_id = customtkinter.CTkEntry(master=frame, placeholder_text='')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=125, y=70)

    def mostrar_producto():
        ventana.geometry('1000x300')
        name_producto = " SI "
        labels_parte2(frame, name_producto)

        ib_cantidad = customtkinter.CTkEntry(master=frame, placeholder_text='')
        ib_cantidad.pack(pady=12, padx=10)
        ib_cantidad.place(x=150, y=125)

        ib_no_factura = customtkinter.CTkEntry(master=frame, placeholder_text='')
        ib_no_factura.pack(pady=12, padx=10)
        ib_no_factura.place(x=150, y=160)

        cal = DateEntry(frame, width=50, bg="darkblue", fg="white", year=2024, height=50)
        cal.place(x=185, y=240)

        button_confirmar = customtkinter.CTkButton(master=frame, text="Confirmar", fg_color=color)
        button_confirmar.pack(pady=10, padx=10)
        button_confirmar.place(x=10, y=225)


    # button
    button_buscar = customtkinter.CTkButton(master=frame, text="Buscar", fg_color=color,
                                            command=mostrar_producto)
    button_buscar.pack(pady=10, padx=10)
    button_buscar.place(x=275, y=70)

    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Menú Compras")
    ventana.geometry('1000x150')
    ventana.iconbitmap('icon.ico')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def labels_parte1(frame):
    lb_agregar_prod = customtkinter.CTkLabel(master=frame, text='Agregar a Productos Existentes',
                                             font=("Times New Roman", 50, "bold"))
    lb_agregar_prod.pack(pady=400, padx=400, )
    lb_agregar_prod.place(x=10, y=0)

    lb_id_del_producto = customtkinter.CTkLabel(master=frame, text='ID del producto', font=(" ", 15))
    lb_id_del_producto.pack(pady=400, padx=400, )
    lb_id_del_producto.place(x=10, y=70)


def labels_parte2(frame, name_producto):
    lb_name_del_producto = customtkinter.CTkLabel(master=frame, text='Nombre del Producto: ' + str(name_producto),
                                                  font=(" ", 15))
    lb_name_del_producto.pack(pady=400, padx=400, )
    lb_name_del_producto.place(x=10, y=100)

    lb_cantidad_a_agregar = customtkinter.CTkLabel(master=frame, text='Cantidad a agregar', font=(" ", 15))
    lb_cantidad_a_agregar.pack(pady=400, padx=400, )
    lb_cantidad_a_agregar.place(x=10, y=125)

    lb_no_factura = customtkinter.CTkLabel(master=frame, text='No. Factura', font=(" ", 15))
    lb_no_factura.pack(pady=400, padx=400, )
    lb_no_factura.place(x=10, y=150)

    lb_ingrese_fecha = customtkinter.CTkLabel(master=frame, text='Fecha de Compra:', font=(" ", 15))
    lb_ingrese_fecha.pack(pady=400, padx=400)
    lb_ingrese_fecha.place(x=10, y=185)

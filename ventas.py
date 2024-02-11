import customtkinter
global texto_imagen


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=0)

    return frame


def frame_2(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)

    return frame


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    frame2 = frame_2(ventana)
    color = "#3E4446"
    labels_parte1(frame)
    labels_parte2(frame2)
    # IB
    ib_id = customtkinter.CTkEntry(master=frame, placeholder_text='')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=155, y=65)

    ib_name = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese el nombre del cliente', width=500)
    ib_name.pack(pady=12, padx=10)
    ib_name.place(x=120, y=105)

    ib_nit = customtkinter.CTkEntry(master=frame, placeholder_text='NIT del cliente')
    ib_nit.pack(pady=12, padx=10)
    ib_nit.place(x=60, y=145)

    cb_servicio = customtkinter.CTkComboBox(master=frame2, font=("Times New Roman", 20),
                                            values=['Terapia Individual', 'Terapia de Pareja',
                                                    'Orientación Vocacional'], width=400)
    cb_servicio.pack(pady=400, padx=400, )
    cb_servicio.place(x=125, y=15)

    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Ventas")
    ventana.geometry('950x750')
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

    lb_name = customtkinter.CTkLabel(master=frame, text='Nombre', font=("Times New Roman", 30))
    lb_name.pack(pady=400, padx=400, )
    lb_name.place(x=10, y=100)

    lb_nit = customtkinter.CTkLabel(master=frame, text='Nit', font=("Times New Roman", 30))
    lb_nit.pack(pady=400, padx=400, )
    lb_nit.place(x=10, y=140)


def labels_parte2(frame):
    lb_datos_ser = customtkinter.CTkLabel(master=frame, text='Servicio ', font=("Times New Roman", 30, "bold"))
    lb_datos_ser.pack(pady=400, padx=400, )
    lb_datos_ser.place(x=10, y=10)

    lb_costo_ser = customtkinter.CTkLabel(master=frame, text='Costo: ', font=("Times New Roman", 30, "bold"))
    lb_costo_ser.pack(pady=400, padx=400, )
    lb_costo_ser.place(x=570, y=10)


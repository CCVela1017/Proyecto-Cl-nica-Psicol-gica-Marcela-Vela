import customtkinter

global texto_imagen


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=90, fill='both', ipady=0)

    return frame


def frame_2(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=90, fill='both', ipady=110)
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
    color = "#3E4446"
    labels_parte1(frame)
    labels_parte2(frame2)
    labels_parte3(frame3)
    # Variables a usar
    cantidad_terapia_individual: float = 0
    cantidad_terapia_pareja: float = 0
    cantidad_orientacion_voc: float = 0
    sub_total: float = 0
    descuento: float = 0
    total: float = 0
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
    # IB PARTE 2

    ib_terapia_indiv = customtkinter.CTkEntry(master=frame2, placeholder_text='')
    ib_terapia_indiv.pack(pady=12, padx=10)
    ib_terapia_indiv.place(x=550, y=65)

    ib_terapia_pareja = customtkinter.CTkEntry(master=frame2, placeholder_text='')
    ib_terapia_pareja.pack(pady=12, padx=10)
    ib_terapia_pareja.place(x=550, y=110)

    ib_pruebas_orientacion = customtkinter.CTkEntry(master=frame2, placeholder_text='')
    ib_pruebas_orientacion.pack(pady=12, padx=10)
    ib_pruebas_orientacion.place(x=550, y=160)

    ib_prueba_iq = customtkinter.CTkEntry(master=frame2, placeholder_text='')
    ib_prueba_iq.pack(pady=12, padx=10)
    ib_prueba_iq.place(x=550, y=215)

    ib_test_ansiedad = customtkinter.CTkEntry(master=frame2, placeholder_text='')
    ib_test_ansiedad.pack(pady=12, padx=10)
    ib_test_ansiedad.place(x=550, y=265)

    button_confirm = customtkinter.CTkButton(master=frame2, text="Confirmar", fg_color=color, width=145, height=45)
    button_confirm.pack(pady=100, padx=10)
    button_confirm.place(x=550, y=310)

    lb_subtotal = customtkinter.CTkLabel(master=frame3, text='Q. ' + str(sub_total),
                                         font=("Times New Roman", 40))
    lb_subtotal.pack(pady=400, padx=400, )
    lb_subtotal.place(x=340, y=10)

    lb_descuento = customtkinter.CTkLabel(master=frame3, text='Q. ' + str(descuento),
                                          font=("Times New Roman", 40))
    lb_descuento.pack(pady=400, padx=400, )
    lb_descuento.place(x=340, y=60)

    lb_total = customtkinter.CTkLabel(master=frame3, text='Q. ' + str(total),
                                      font=("Times New Roman", 40, "bold"))
    lb_total.pack(pady=400, padx=400, )
    lb_total.place(x=340, y=100)

    button_generate_fact = customtkinter.CTkButton(master=frame3, text="Generar Factura", fg_color=color, width=145, height=45)
    button_generate_fact.pack(pady=100, padx=10)
    button_generate_fact.place(x=550, y=100)

    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Ventas")
    ventana.geometry('950x800+50x50')
    ventana.iconbitmap('icon.ico')
    ventana.resizable(0, 0)
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
    lb_costo_ser.place(x=340, y=10)

    lb_cantidad = customtkinter.CTkLabel(master=frame, text='Cantidad: ', font=("Times New Roman", 30, "bold"))
    lb_cantidad.pack(pady=400, padx=400, )
    lb_cantidad.place(x=550, y=10)

    lb_terapia_ind = customtkinter.CTkLabel(master=frame, text='Terapia Individual             Q. 150.00',
                                            font=("Times New Roman", 30))
    lb_terapia_ind.pack(pady=400, padx=400, )
    lb_terapia_ind.place(x=10, y=60)

    lb_terapia_pareja = customtkinter.CTkLabel(master=frame, text='Terapia de Pareja              Q. 200.00  ',
                                               font=("Times New Roman", 30))
    lb_terapia_pareja.pack(pady=400, padx=400, )
    lb_terapia_pareja.place(x=10, y=110)

    lb_orientacion_voc = customtkinter.CTkLabel(master=frame, text='Orientación Vocacional     Q.  250.00',
                                                font=("Times New Roman", 30))
    lb_orientacion_voc.pack(pady=400, padx=400, )
    lb_orientacion_voc.place(x=10, y=160)

    lb_pruebas_de_iq = customtkinter.CTkLabel(master=frame, text='Pruebas de IQ                   Q.  150.00',
                                              font=("Times New Roman", 30))
    lb_pruebas_de_iq.pack(pady=400, padx=400, )
    lb_pruebas_de_iq.place(x=10, y=210)

    lb_test_ansiedad = customtkinter.CTkLabel(master=frame, text='Test de ansiedad                Q.  150.00',
                                              font=("Times New Roman", 30))
    lb_test_ansiedad.pack(pady=400, padx=400, )
    lb_test_ansiedad.place(x=10, y=260)


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


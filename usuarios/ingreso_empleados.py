import customtkinter
from tkcalendar import DateEntry

global texto_imagen


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    frame2 = frame_2(ventana)
    color = "#3E4446"
    labels_parte1(frame, frame2)

    def confirm() -> dict:
        data = {'nombres': ib_nombres.get(), 'apellidos': ib_apellidos.get(),
                'direccion': ib_direccion.get(), 'tel': ib_tel.get(),
                'num_dpi': ib_num_dpi.get(), 'correo': ib_corre_elec.get(),
                'estado_civil': cb_estado_civil.get(), 'fecha': cal.get()}

        return data

    def register() -> dict:
        data = {}
        return data
    # IB
    ib_nombres = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese los nombres ', width=200, height=35)
    ib_nombres.pack(pady=12, padx=10)
    ib_nombres.place(x=135, y=63)

    ib_apellidos = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese los apellidos', width=200, height=35)
    ib_apellidos.pack(pady=100, padx=10)
    ib_apellidos.place(x=480, y=63)

    ib_direccion = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese su dirección actual', width=580,
                                          height=35)
    ib_direccion.pack(pady=100, padx=10)
    ib_direccion.place(x=230, y=151)

    ib_tel = customtkinter.CTkEntry(master=frame, placeholder_text='Ingreso Num')
    ib_tel.pack(pady=100, padx=10)
    ib_tel.place(x=75, y=198)

    ib_num_dpi = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese El DPI', width=180, height=35)
    ib_num_dpi.pack(pady=100, padx=10)
    ib_num_dpi.place(x=300, y=198)

    ib_corre_elec = customtkinter.CTkEntry(master=frame, placeholder_text='Ingreso de Correo electronico Personal',
                                           width=400)
    ib_corre_elec.pack(pady=100, padx=10)
    ib_corre_elec.place(x=170, y=300)

    cb_estado_civil = customtkinter.CTkComboBox(master=frame, font=("Times New Roman", 20),
                                                values=['Solter@', 'Casad@'], width=200)
    cb_estado_civil.pack(pady=400, padx=400, )
    cb_estado_civil.place(x=200, y=250)

    cal = DateEntry(frame, width=50, bg="darkblue", fg="white", year=2023, height=50)
    cal.place(x=350, y=140)
    # confirmación
    button_confirm_1 = customtkinter.CTkButton(master=frame, text="Confirmar", fg_color=color, width=180, height=45
                                               , command=confirm)
    button_confirm_1.pack(pady=100, padx=10)
    button_confirm_1.place(x=630, y=295)

    # parte 2

    cb_nivel_academico = customtkinter.CTkComboBox(master=frame2, font=("Times New Roman", 20),
                                                   values=['Ninguno', 'Primaria', 'Básico', 'Bachiller', 'Pre Grado',
                                                           'Post Grado'], width=200)
    cb_nivel_academico.pack(pady=400, padx=400, )
    cb_nivel_academico.place(x=225, y=10)

    ib_cantidad_de_idiomas = customtkinter.CTkEntry(master=frame2, placeholder_text='Cantidad',
                                                    width=100)
    ib_cantidad_de_idiomas.pack(pady=100, padx=10)
    ib_cantidad_de_idiomas.place(x=725, y=15)

    cb_puesto = customtkinter.CTkComboBox(master=frame2, font=("Times New Roman", 20),
                                          values=['Administrador', 'Gerente', 'Recepcionista'], width=200)
    cb_puesto.pack(pady=400, padx=400, )
    cb_puesto.place(x=115, y=53)

    cb_turno = customtkinter.CTkComboBox(master=frame2, font=("Times New Roman", 20),
                                         values=['Diurno', 'Nocturno', 'Mixto'], width=200)
    cb_turno.pack(pady=400, padx=400, )
    cb_turno.place(x=550, y=53)

    ib_num_horas = customtkinter.CTkEntry(master=frame2, placeholder_text='Horas', width=180, height=35)
    ib_num_horas.pack(pady=100, padx=10)
    ib_num_horas.place(x=240, y=100)

    ib_salud = customtkinter.CTkEntry(master=frame2, placeholder_text='Salario', width=180, height=35)
    ib_salud.pack(pady=100, padx=10)
    ib_salud.place(x=550, y=100)

    button_confirm_2 = customtkinter.CTkButton(master=frame2, text="Registrar Usuario", fg_color='#1D5DEC', width=830,
                                               height=35, command=register)
    button_confirm_2.pack(pady=100, padx=10)
    button_confirm_2.place(x=10, y=145)

    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Registro de nuevos asociados")
    ventana.geometry('975x575')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=100)
    return frame


def frame_2(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=0, padx=60, fill='both', ipady=80)
    return frame


def labels_parte1(frame, frame_2):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Registro de nuevos asociados',
                                        font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    lb_nombres = customtkinter.CTkLabel(master=frame, text='Nombres', font=("Times New Roman", 30))
    lb_nombres.pack(pady=400, padx=400, )
    lb_nombres.place(x=10, y=60)

    lb_apellidos = customtkinter.CTkLabel(master=frame, text='Apellidos', font=("Times New Roman", 30))
    lb_apellidos.pack(pady=400, padx=400)
    lb_apellidos.place(x=350, y=60)

    lb_direccion_actual = customtkinter.CTkLabel(master=frame, text='Dirección Actual', font=("Times New Roman", 30))
    lb_direccion_actual.pack(pady=400, padx=400)
    lb_direccion_actual.place(x=10, y=150)

    lb_telefonos = customtkinter.CTkLabel(master=frame, text='Tel.', font=("Times New Roman", 30))
    lb_telefonos.pack(pady=400, padx=400)
    lb_telefonos.place(x=10, y=195)

    lb_dpi = customtkinter.CTkLabel(master=frame, text='DPI', font=("Times New Roman", 30))
    lb_dpi.pack(pady=400, padx=400)
    lb_dpi.place(x=240, y=198)

    lb_correo_electronico = customtkinter.CTkLabel(master=frame, text='Correo Elec.', font=("Times New Roman", 30))
    lb_correo_electronico.pack(pady=400, padx=400)
    lb_correo_electronico.place(x=10, y=300)

    lb_estado_civil = customtkinter.CTkLabel(master=frame, text='Estado Civil', font=("Times New Roman", 30))
    lb_estado_civil.pack(pady=400, padx=400)
    lb_estado_civil.place(x=10, y=250)

    # label 2

    lb_ingrese_fecha = customtkinter.CTkLabel(master=frame, text='Fecha de nacimiento:', font=("Times New Roman", 30))
    lb_ingrese_fecha.pack(pady=400, padx=400)
    lb_ingrese_fecha.place(x=10, y=100)

    lb_nivel_academico = customtkinter.CTkLabel(master=frame_2, text='Nivel Acádemico', font=("Times New Roman", 30))
    lb_nivel_academico.pack(pady=400, padx=400)
    lb_nivel_academico.place(x=10, y=10)

    lb_cantidad_de_idiomas = customtkinter.CTkLabel(master=frame_2, text='Cantidad De Idiomas',
                                                    font=("Times New Roman", 30))
    lb_cantidad_de_idiomas.pack(pady=400, padx=400)
    lb_cantidad_de_idiomas.place(x=450, y=10)

    lb_puesto = customtkinter.CTkLabel(master=frame_2, text='Puesto', font=("Times New Roman", 30))
    lb_puesto.pack(pady=400, padx=400)
    lb_puesto.place(x=10, y=50)

    lb_turno = customtkinter.CTkLabel(master=frame_2, text='Turno', font=("Times New Roman", 30))
    lb_turno.pack(pady=400, padx=400)
    lb_turno.place(x=450, y=50)

    lb_horas = customtkinter.CTkLabel(master=frame_2, text='Horas de Trabajo', font=("Times New Roman", 30))
    lb_horas.pack(pady=400, padx=400)
    lb_horas.place(x=10, y=100)

    lb_salario = customtkinter.CTkLabel(master=frame_2, text='Salario', font=("Times New Roman", 30))
    lb_salario.pack(pady=400, padx=400)
    lb_salario.place(x=450, y=100)



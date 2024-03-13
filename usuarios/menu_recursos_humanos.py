import customtkinter

global texto_imagen
from usuarios import ingreso_empleados
from usuarios import mostrar_empleados


def open_ingreso():
    ingreso_empleados.main()


def open_mostrar():
    mostrar_empleados.main()


def main():
    ventana = cargar_datos()
    frame = frame1(ventana)
    color = "#3E4446"
    labels_parte1(frame)

    button_ingreso = customtkinter.CTkButton(master=frame, text="Ingreso", fg_color=color, height=150,
                                             command=open_ingreso)
    button_ingreso.pack(pady=100, padx=10)
    button_ingreso.place(x=10, y=100)

    button_mostrar = customtkinter.CTkButton(master=frame, text="Mostrar", fg_color=color, height=150,
                                             command=open_mostrar)
    button_mostrar.pack(pady=100, padx=10)
    button_mostrar.place(x=200, y=100)

    ventana.mainloop()

    return


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Recursos Humanos")
    ventana.geometry('1000x300')
    ventana.iconbitmap('icon.ico')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)
    return frame


def labels_parte1(frame):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Menú Usuarios', font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

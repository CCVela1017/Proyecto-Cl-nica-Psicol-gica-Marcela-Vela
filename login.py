import customtkinter
from werkzeug.security import check_password_hash
from tkinter import *
from tkinter import messagebox
import menu_principal
from PIL import Image
import os

ventana = Toplevel(background='#1a1a1a')

vector_ejemplo = [['Eduardo', 'pbkdf2:sha256:600000$RgGwUg'
                              'LipocaPSMN$aa01597732c3c7620'
                              'f507faf8342f15669421ba1290d32ca0eee21d5aa23108f', 'Empleado'],
                  ['admin', 'pbkdf2:sha256:600000$crwhOFcA1'
                             'B61eQbU$617433519ed6f80d03a7a9'
                             '638130dbc4cd1084b72a0c55b4b6a31f0c4b58d4ba', 'Administrador']
                  ]

'''
contraseña Eduardo: Kazul102934_ii_4y47hd6
contraseña Andrea: 1234
'''


def confirm_user_pass():
    user = entrada_usuario.get()
    passwd = entrada_contrasena.get()
    found_user = False
    j = 0
    for i in vector_ejemplo:
        if i[0] == user:
            found_user = True
            break
        else:
            j += 1

    if found_user:
        saved_passwd = vector_ejemplo[j][1]
        if check_password_hash(saved_passwd, passwd):
            ventana.withdraw()
            menu_principal.main_window(vector_ejemplo[j][2])
        else:
            messagebox.showerror('Acceso denegado', 'El nombre de usuario o contraseña son incorrectos.')
    else:
        messagebox.showerror('Acceso denegado', 'El nombre de usuario o contraseña son incorrectos.')
        entrada_usuario.delete(0, END)
        entrada_usuario.insert(0, '')
        entrada_contrasena.delete(0, END)
        entrada_contrasena.insert(0, '')
        entrada_usuario._activate_placeholder()
        entrada_contrasena._activate_placeholder()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

"""Ventana"""

ventana.geometry("950x600")
ventana.title("Inicio de sesión")
ventana.iconbitmap("icon.ico")
ventana.resizable(False, False)

"""Imagen de la izquierda"""
image_path = os.path.join(os.path.dirname(__file__), 'icon.png')
image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(450, 450))
image_label = customtkinter.CTkLabel(master=ventana, image=image)
image_label.place(x=45, y=85)

"""Marco"""
marco = customtkinter.CTkFrame(master=ventana, width=400, height=500)
marco.pack(side=RIGHT)

"""*-*-*-*-*-*-* Opciones en el marco *-*-*-*-*-*-*"""
etiqueta = customtkinter.CTkLabel(master=marco, text="Inicio de Sesión",
                                  font=("Times New Roman", 30, "bold"), text_color="white")
etiqueta.place(x=90, y=90)

"""Cuadro de texto usuario"""
entrada_usuario = customtkinter.CTkEntry(master=marco, placeholder_text="Nombre de Usuario", width=300,
                                     height=35, font=("Times New Roman", 20, "bold"))
entrada_usuario.pack(pady=12, padx=10)
entrada_usuario.place(x=40, y=150)
"""*Carcater obligatorio"""
usuario_obligatorio = customtkinter.CTkLabel(master=marco, text="*El nombre de usuario es de carácter obligatorio", text_color="red",
                                font=("Times New Roman", 15, "bold"))
usuario_obligatorio.place(x=25, y=185)

"""Cuadro de texto contraseña"""
entrada_contrasena = customtkinter.CTkEntry(master=marco, placeholder_text="Contraseña", width=300,
                                     height=35, font=("Times New Roman", 20, "bold"), show='●')
entrada_contrasena.pack(pady=12, padx=10)
entrada_contrasena.place(x=40, y=230)
"""*Carcater obligatorio"""
contrasena_obligatoria = customtkinter.CTkLabel(master=marco, text="*La contraseña es de carácter obligatorio", text_color="red",
                                font=("Times New Roman", 15, "bold"))
contrasena_obligatoria.place(x=25, y=275)

"""Botón para aceptar"""
aceptar = customtkinter.CTkButton(master=marco, text="Aceptar", height=25, width=300, font=("times new roman", 20),
                                fg_color="#086EB9", command=confirm_user_pass)
aceptar.place(x=35, y=340)

ventana.mainloop()




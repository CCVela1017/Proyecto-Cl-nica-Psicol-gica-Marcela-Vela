import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

"""Ventana"""
ventana = customtkinter.CTk()
ventana.geometry("925x600")
ventana.title("Inicio de sesión")
ventana.iconbitmap("icon.ico")
ventana.resizable(False, False)

"""Imagen de la izquierda"""
imagen = PhotoImage(file="icon.png")
nombre_imagen = customtkinter.CTkLabel(master=ventana,image=imagen)
nombre_imagen.place(x=20, y=55)

"""Marco"""
marco = customtkinter.CTkFrame(master=ventana, width=400, height=500)
marco.pack(side=RIGHT)

"""*-*-*-*-*-*-* Opciones en el marco *-*-*-*-*-*-*"""
etiqueta = customtkinter.CTkLabel(master=marco, text="Inicio de Sesión",
                                  font=("Times New Roman", 30, "bold"), text_color="white")
etiqueta.place(x=90, y=5)

"""Cuadro de texto usuario"""
entrada_usuario = customtkinter.CTkEntry(master=marco, placeholder_text="Nombre de Usuario", width=300,
                                     height=35, font=("Times New Roman", 20, "bold"))
entrada_usuario.pack(pady=12, padx=10)
entrada_usuario.place(x=40, y=80)
"""*Carcater obligatorio"""
usuario_obligatorio = customtkinter.CTkLabel(master=marco, text="*El nombre de usuario es de carácter obligatorio", text_color="red",
                                font=("Times New Roman", 15, "bold"))
usuario_obligatorio.place(x=25, y=115)

"""Cuadro de texto contraseña"""
entrada_contrasena = customtkinter.CTkEntry(master=marco, placeholder_text="Contraseña", width=300,
                                     height=35, font=("Times New Roman", 20, "bold"))
entrada_contrasena.pack(pady=12, padx=10)
entrada_contrasena.place(x=40, y=160)
"""*Carcater obligatorio"""
contrasena_obligatoria = customtkinter.CTkLabel(master=marco, text="*La contraseña es de carácter obligatorio", text_color="red",
                                font=("Times New Roman", 15, "bold"))
contrasena_obligatoria.place(x=25, y=200)

"""Botón para recordar"""
recordar = customtkinter.CTkCheckBox(master=marco, text="Recuérdame siempre").place(x=25, y=235)

"""Botón para aceptar"""
aceptar = customtkinter.CTkButton(master=marco, text="Aceptar", height=25, width=300, font=("times new roman", 20),
                                fg_color="#086EB9")
aceptar.place(x=25, y=285)

ventana.mainloop()
import customtkinter
from PIL import Image
import os
import sqlite3
from tkinter import messagebox

import hashlib


def menu_form(info: dict):

    img_path = os.path.join(os.path.dirname(__file__), 'show_pswd.png')
    image = customtkinter.CTkImage(light_image=Image.open(img_path), size=(15, 15))

    def buttons(image2, last_data: dict):

        def clean():
            ib_user.delete(0, 'end')
            ib_password.delete(0, 'end')
            ib_password2.delete(0, 'end')

        def encrypt_password(passwd: str) -> str:
            pswd_bytes = passwd.encode('utf-8')

            sha_256_hash = hashlib.sha256()

            sha_256_hash.update(pswd_bytes)

            encrypted_pswd = sha_256_hash.hexdigest()

            return encrypted_pswd

        def upload_data():

            conexion = sqlite3.connect('src/database')
            cursor = conexion.cursor()
            cursor.execute("SELECT user FROM users WHERE user = ?", (ib_user.get(),))

            cursor2 = conexion.cursor()
            cursor2.execute("SELECT password FROM users WHERE Puesto = 'Administrador' and password = ?",
                            (encrypt_password(ib_password2.get()),))
            repeat_user = cursor.fetchone()
            correct_admin = cursor2.fetchone()

            if correct_admin:
                if repeat_user:
                    messagebox.showerror('Usuario Duplicado', 'Ya existe una persona con el usuario insertado'
                                                              ', vuelve a intentarlo.')
                    clean()
                else:
                    password_crypted = encrypt_password(ib_password.get())
                    last_data.update({'user': ib_user.get(), 'psw': password_crypted})

                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO users (Nombres, "
                                   "Apellidos, "
                                   "Fecha_nac, "
                                   "Direccion, "
                                   "Tel, "
                                   "DPI, "
                                   "Estado_civil,"
                                   "Correo,"
                                   "Nivel_acad,"
                                   "Puesto,"
                                   "Turno,"
                                   "Horas_tra,"
                                   "salario,"
                                   "cant_idiom,"
                                   "user,"
                                   "password) "
                                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                   (last_data['nombres'], last_data['apellidos'], last_data['fecha']
                                    , last_data['direccion'], last_data['tel'], last_data['num_dpi']
                                    , last_data['estado_civil'], last_data['correo'], last_data['academico']
                                    , last_data['puesto'], last_data['turno'], last_data['horas']
                                    , last_data['salario'], last_data['idiomas'], last_data['user']
                                    , last_data['psw']))
                    messagebox.showinfo('¡Datos Ingresados Correctamente!', 'Los datos ingresados fueron '
                                                                            'enviados correctamente a la base de datos.')
                    conexion.commit()

                    clean()
            else:
                messagebox.showerror('Error de Validación', 'La contraseña ingresada no corresponde al a'
                                                            'administrador del sistema, vuelve a ingresarla.')
                ib_password2.delete(0, 'end')

            conexion.close()

        def toggle_password_visibility():
            current_show_state = ib_password.cget("show")
            if current_show_state == "●":
                ib_password.configure(show="")
            else:
                ib_password.configure(show="●")

        def toggle_password_visibility2():
            current_show_state = ib_password2.cget("show")
            if current_show_state == "●":
                ib_password2.configure(show="")
            else:
                ib_password2.configure(show="●")

        lb_user = customtkinter.CTkLabel(master=frame, text='Usuario:', font=("Times New Roman", 25))
        lb_user.pack(pady=400, padx=400)
        lb_user.place(x=15, y=10)

        ib_user = customtkinter.CTkEntry(master=frame, placeholder_text='Usuario', width=200, height=35)
        ib_user.pack(pady=12, padx=10)
        ib_user.place(x=200, y=10)

        lb_psd = customtkinter.CTkLabel(master=frame, text='Contraseña:', font=("Times New Roman", 25))
        lb_psd.pack(pady=400, padx=400)
        lb_psd.place(x=15, y=63)

        ib_password = customtkinter.CTkEntry(master=frame, placeholder_text='Contraseña', width=200, height=35,
                                             show="●")
        ib_password.pack(pady=12, padx=10)
        ib_password.place(x=200, y=63)

        button_show_pswd = customtkinter.CTkButton(master=frame, height=35, width=35, image=image2, text='',
                                                   command=toggle_password_visibility, fg_color="#FFFFFF")

        button_show_pswd.pack(pady=34, padx=10)
        button_show_pswd.place(x=430, y=63)

        lb_psd2 = customtkinter.CTkLabel(master=frame, text='Administrador:', font=("Times New Roman", 25))
        lb_psd2.pack(pady=400, padx=400)
        lb_psd2.place(x=15, y=116)

        ib_password2 = customtkinter.CTkEntry(master=frame, placeholder_text='Contraseña de Administrador', width=200
                                              , height=35, show="●")
        ib_password2.pack(pady=12, padx=10)
        ib_password2.place(x=200, y=116)

        button_show_pswd2 = customtkinter.CTkButton(master=frame, height=35, width=35, image=image2, text='',
                                                    command=toggle_password_visibility2, fg_color="#FFFFFF")

        button_show_pswd2.pack(pady=34, padx=10)
        button_show_pswd2.place(x=430, y=116)

        button_confirm = customtkinter.CTkButton(master=frame, height=40, width=450, text='Contratar Persona',
                                                 command=upload_data, fg_color="#2596be")

        button_confirm.pack(pady=34, padx=10)
        button_confirm.place(x=15, y=173)

        return

    root = customtkinter.CTkToplevel()

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root.title("Creación de Usuarios")
    frame = customtkinter.CTkFrame(master=root)
    root.wm_attributes("-topmost", True)
    root.grab_set()

    frame.pack(pady=10, padx=10, fill='both', expand=True)

    buttons(image, info)
    frame.pack()

    root.geometry('500x250')
    root.mainloop()

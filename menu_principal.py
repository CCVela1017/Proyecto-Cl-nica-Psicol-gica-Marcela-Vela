import os

import customtkinter
from PIL import Image

import compras
import datos_equipo
import datos_inventario
import ventas

root = customtkinter.CTk()


def add_image(frame):
    image_path = os.path.join(os.path.dirname(__file__), 'icon.png')
    image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(500, 500))
    image_label = customtkinter.CTkLabel(master=frame, image=image)
    image_label.place(x=55, y=85)

    return


def open_inventory():
    datos_inventario.main_window()


def open_equipment():
    datos_equipo.main_window()


def open_shop():
    compras.main()


def open_ventas():
    ventas.main()


def buttons(frame):
    button_1 = customtkinter.CTkButton(master=frame, text='Inventario', height=100, width=150, font=("Arial", 20),
                                       command=open_inventory, fg_color="#3E4446")
    button_2 = customtkinter.CTkButton(master=frame, text='Equipo', height=100, width=150, font=("Arial", 20),
                                       command=open_equipment, fg_color="#3E4446")
    button_3 = customtkinter.CTkButton(master=frame, text='Compras', height=100, width=150, font=("Arial", 20),
                                       command=open_shop, fg_color="#3E4446")

    button_4 = customtkinter.CTkButton(master=frame, text='Ventas', height=100, width=100, font=("Arial", 20),
                                       command=open_ventas, fg_color="#3E4446")

    button_1.pack(pady=34, padx=10)
    button_2.pack(pady=34, padx=10)
    button_3.pack(pady=34, padx=10)
    button_4.pack(pady=34, padx=90)
    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root.title("Menú Principal")
    root.iconbitmap('icon.ico')
    frame = customtkinter.CTkFrame(master=root)
    root.wm_attributes("-topmost", False)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, fg_color="#212121", width=50)
    frame2.pack(pady=10, padx=10, fill='both', expand=True, side='right')
    frame3 = customtkinter.CTkFrame(master=frame, fg_color="#212121")
    frame3.pack(pady=20, padx=20, fill='both', expand=True, side='left')

    add_image(frame3)

    buttons(frame2)

    frame.pack()
    root.geometry('1300x700')
    root.mainloop()


main_window()

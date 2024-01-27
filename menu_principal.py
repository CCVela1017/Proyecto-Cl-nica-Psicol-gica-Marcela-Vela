import customtkinter
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import os


def add_image(frame, root):
    image_path = os.path.join(os.path.dirname(__file__), 'icon.png')
    image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(500, 500))
    image_label = customtkinter.CTkLabel(master=frame, image=image, text='')
    image_label.place(x=55, y=85)

    return


def buttons(frame):
    button_1 = customtkinter.CTkButton(master=frame, text='Inventario', height=175, width=200, font=("Arial", 20))
    button_2 = customtkinter.CTkButton(master=frame, text='Equipo', height=175, width=200, font=("Arial", 20))
    button_3 = customtkinter.CTkButton(master=frame, text='Compras', height=175, width=200, font=("Arial", 20))

    button_1.pack(pady=20, padx=10)
    button_2.pack(pady=20, padx=10)
    button_3.pack(pady=20, padx=10)

    return


def main_window():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.title("Menú Principal")
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, fg_color='dark gray', width=50)
    frame2.pack(pady=10, padx=10, fill='both', expand=True, side='right')
    frame3 = customtkinter.CTkFrame(master=frame)
    frame3.pack(pady=20, padx=20, fill='both', expand=True, side='left')

    def presionar():
        print('Hola')

    add_image(frame3, root)


    buttons(frame2)

    root.geometry('1300x700')
    root.mainloop()


main_window()
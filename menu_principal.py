import os
import customtkinter
from tkinter import *
from PIL import Image
import compras
import datos_equipo
import datos_inventario
import ventas
from financiero import financiero
from usuarios import menu_recursos_humanos




def add_image(frame):
    image_path = os.path.join(os.path.dirname(__file__), 'icon.png')
    image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(450, 450))
    image_label = customtkinter.CTkLabel(master=frame, image=image, text='')
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


def open_menu_recursos():
    menu_recursos_humanos.main()


def open_financiero():
    financiero.main_financiero()


def buttons(frame, access: str):
    state: dict = {}
    if access == 'Recepcionista':
        state = {'inventory': 'normal',
                 'equipment': 'disabled',
                 'shop': 'disabled',
                 'ventas': 'normal',
                 'users': 'disabled',
                 'financial': 'disabled'}
    elif access == 'Administrador':
        state = {'inventory': 'normal',
                 'equipment': 'normal',
                 'shop': 'normal',
                 'ventas': 'normal',
                 'users': 'normal',
                 'financial': 'normal'}
    elif access == 'Gerente':
        state = {'inventory': 'normal',
                 'equipment': 'normal',
                 'shop': 'normal',
                 'ventas': 'normal',
                 'users': 'disabled',
                 'financial': 'normal'}

    button_1 = customtkinter.CTkButton(master=frame, text='Inventario', height=75, width=150, font=("Arial", 20),
                                       command=open_inventory, fg_color="#3E4446", state=state['inventory'])
    button_2 = customtkinter.CTkButton(master=frame, text='Equipo', height=75, width=150, font=("Arial", 20),
                                       command=open_equipment, fg_color="#3E4446", state=state['equipment'])
    button_3 = customtkinter.CTkButton(master=frame, text='Compras', height=75, width=150, font=("Arial", 20),
                                       command=open_shop, fg_color="#3E4446", state=state['shop'])

    button_4 = customtkinter.CTkButton(master=frame, text='Ventas', height=75, width=150, font=("Arial", 20),
                                       command=open_ventas, fg_color="#3E4446", state=state['ventas'])

    button_5 = customtkinter.CTkButton(master=frame, text='Recursos\nHumanos', height=75, width=150, font=("Arial", 20),
                                       command=open_menu_recursos, fg_color="#3E4446", state=state['users'])

    button_6 = customtkinter.CTkButton(master=frame, text='Financiero', height=75, width=150, font=("Arial", 20),
                                       command=open_financiero, fg_color="#3E4446", state=state['financial'])

    button_1.pack(pady=15, padx=5)
    button_2.pack(pady=15, padx=5)
    button_3.pack(pady=15, padx=5)
    button_4.pack(pady=15, padx=5)
    button_5.pack(pady=15, padx=5)
    button_6.pack(pady=15, padx=5)

    return


def main_window(access_lvl: str):
    root = Toplevel(background='#1a1a1a')
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

    buttons(frame2, access_lvl)

    frame.pack()
    root.geometry('1400x855')
    root.mainloop()



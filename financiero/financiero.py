import customtkinter

from financiero.balance import main_balance
from financiero.estado_resultados import main_estado_resultados
from financiero.historial import main_historial
from financiero.utilidad import main_utilidad

root = customtkinter.CTk()


def open_eresultados():
    main_estado_resultados()


def open_utilidad():
    main_utilidad()


def open_balance():
    main_balance()


def open_historial():
    main_historial()


def buttons(frame, frame2):

    button_1 = customtkinter.CTkButton(master=frame, text='Estado de resultados', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_eresultados)
    button_2 = customtkinter.CTkButton(master=frame2, text='Utilidad bruta', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_utilidad)

    button_4 = customtkinter.CTkButton(master=frame, text='Balance general', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_balance)

    button_5 = customtkinter.CTkButton(master=frame2, text='Historial de resultados', height=125, width=250, font=("Arial", 15),
                                       fg_color="#3E4446", command=open_historial)

    button_1.pack(pady=34, padx=10)
    button_2.pack(pady=34, padx=10)
    button_4.pack(pady=34, padx=10)
    button_5.pack(pady=34, padx=10)

    return


def main_financiero():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root.title("Menú principal financiero")
    root.iconbitmap('icon.ico')
    frame = customtkinter.CTkFrame(master=root)
    root.wm_attributes("-topmost", True)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    frame2 = customtkinter.CTkFrame(master=frame, fg_color="#212121", width=50)
    frame2.pack(pady=10, padx=8, fill='both', expand=True, side='right')
    frame3 = customtkinter.CTkFrame(master=frame, fg_color="#212121")
    frame3.pack(pady=20, padx=8, fill='both', expand=True, side='left')

    buttons(frame3, frame2)

    frame.pack()
    root.geometry('800x450')
    root.mainloop()

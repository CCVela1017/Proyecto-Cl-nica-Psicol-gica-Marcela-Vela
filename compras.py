import customtkinter
import tkinter as tk


def main():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTk()
    ventana.title("Compras")
    ventana.geometry('1280x720')
    ventana.iconbitmap('icon.ico')
    # frame
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=20, padx=60, fill='both', expand=True)
    front_end(frame)

    ventana.mainloop()
    return


def front_end(frame):
    lb_id = customtkinter.CTkLabel(master=frame, text='Codigo', font=("Times New Roman", 30))
    lb_id.pack(pady=400, padx=400, )
    lb_id.place(x=10, y=10)

    return


main()

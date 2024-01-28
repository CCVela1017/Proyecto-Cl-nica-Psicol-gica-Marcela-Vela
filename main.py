import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title("Inicio de Sesión")
root.iconbitmap('icon.ico')
root.geometry('500*350')

def login():
    print('Test')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Inicio de Sesión')
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Nombre de usuario')
entry1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Contraseña', show='*')
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Iniciar Sesión', command=login)
button.pack(pady=12, padx=10)

root.mainloop()
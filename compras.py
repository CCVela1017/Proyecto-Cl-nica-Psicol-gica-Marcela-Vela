import os.path
import tkinter
import customtkinter
from PIL import Image


def main():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTk()
    ventana.title("Compras")
    ventana.geometry('950x600')
    ventana.iconbitmap('icon.ico')
    # frame
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=60, fill='both', ipady=35)
    frame2 = customtkinter.CTkFrame(master=ventana)
    frame2.pack(pady=0, padx=60, fill='both', ipady=60)
    color = "#3E4446"

    # labels
    # parte 1
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Ingreso', font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    lb_id = customtkinter.CTkLabel(master=frame, text='Codigo', font=("Times New Roman", 30))
    lb_id.pack(pady=400, padx=400, )
    lb_id.place(x=10, y=60)

    lb_name_product = customtkinter.CTkLabel(master=frame, text='Producto', font=("Times New Roman", 30))
    lb_name_product.pack(pady=400, padx=400)
    lb_name_product.place(x=290, y=60)

    lb_proveedor = customtkinter.CTkLabel(master=frame, text='Proveedor', font=("Times New Roman", 30))
    lb_proveedor.pack(pady=400, padx=400)
    lb_proveedor.place(x=10, y=110)

    lb_precio = customtkinter.CTkLabel(master=frame, text='Precio', font=("Times New Roman", 30))
    lb_precio.pack(pady=400, padx=400)
    lb_precio.place(x=515, y=110)

    lb_select_img = customtkinter.CTkLabel(master=frame, text='Seleccionar Imagen', font=("Times New Roman", 30))
    lb_select_img.pack(pady=400, padx=400)
    lb_select_img.place(x=10, y=160)

    lb_cantidad = customtkinter.CTkLabel(master=frame, text='Cantidad', font=("Times New Roman", 30))
    lb_cantidad.pack(pady=400, padx=400)
    lb_cantidad.place(x=512, y=160)

    # IB
    ib_id = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Codigo')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=110, y=67)

    ib_name = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Nombre del producto', width=400,
                                     height=35)
    ib_name.pack(pady=100, padx=10)
    ib_name.place(x=410, y=63)

    ib_proveedor = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Nombre del proveedor', width=350,
                                          height=35)
    ib_proveedor.pack(pady=100, padx=10)
    ib_proveedor.place(x=150, y=113)

    ib_precio = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese el precio', width=180, height=35)
    ib_precio.pack(pady=100, padx=10)
    ib_precio.place(x=630, y=113)

    ib_cantidad = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese la cantidad', width=180,
                                         height=35)
    ib_cantidad.pack(pady=100, padx=10)
    ib_cantidad.place(x=630, y=160)

    # buttons

    button_select_img = customtkinter.CTkButton(master=frame, text="seleccionar", fg_color=color)
    button_select_img.pack(pady=100, padx=10)
    button_select_img.place(x=260, y=167)

    button_confirm_1 = customtkinter.CTkButton(master=frame, text="Confirmar", fg_color=color, width=180, height=45)
    button_confirm_1.pack(pady=100, padx=10)
    button_confirm_1.place(x=630, y=200)
    # # texto de muestreo:
    txt_mostrar: str = "Codigo:  Producto: Proveedor: Precio: Cantidad: "
    precio = 10
    cantidad = 10
    total = str(precio * cantidad)

    # # # parte dos

    # lb
    lb_confirm = customtkinter.CTkLabel(master=frame2, text='Confirmación', font=("Times New Roman", 50, "bold"))
    lb_confirm.pack(pady=400, padx=400, )
    lb_confirm.place(x=10, y=10)

    lb_mostrar_datos = customtkinter.CTkLabel(master=frame2, text=txt_mostrar, font=("Times New Roman", 20),
                                              fg_color=color)
    lb_mostrar_datos.pack(pady=12, padx=10)
    lb_mostrar_datos.place(x=10, y=70)

    lb_precio_confi = customtkinter.CTkLabel(master=frame2, text='Precio:      ' + str(precio),
                                             font=("Times New Roman", 30))
    lb_precio_confi.pack(pady=400, padx=400)
    lb_precio_confi.place(x=445, y=100)

    lb_cantidad_confi = customtkinter.CTkLabel(master=frame2, text='Cantidad:  ' + str(cantidad),
                                               font=("Times New Roman", 30))
    lb_cantidad_confi.pack(pady=400, padx=400)
    lb_cantidad_confi.place(x=440, y=150)

    lb_total_confi = customtkinter.CTkLabel(master=frame2, text="TOTAL:    " + total, font=("Times New Roman", 30))
    lb_total_confi.pack(pady=400, padx=400)
    lb_total_confi.place(x=440, y=200)

    # imagen
    img_path = os.path.join(os.path.dirname(__file__), 'imagenes/imagen_carga.png')
    image = customtkinter.CTkImage(light_image=Image.open(img_path), size=(150, 150))
    img_label = customtkinter.CTkLabel(frame2, image=image)
    img_label.place(x=130, y=130)
    # botones

    button_confirm_2 = customtkinter.CTkButton(master=frame2, text="Confirmar", fg_color=color, width=180, height=45)
    button_confirm_2.pack(pady=100, padx=10)
    button_confirm_2.place(x=630, y=240)

    button_edit = customtkinter.CTkButton(master=frame2, text="Editar", fg_color=color, width=180, height=45)
    button_edit.pack(pady=100, padx=10)
    button_edit.place(x=440, y=240)

    ventana.mainloop()

    return


main()

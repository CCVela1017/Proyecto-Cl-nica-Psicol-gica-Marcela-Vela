import os.path
from tkinter import messagebox

import customtkinter
from PIL import Image
from tkinter import filedialog
import shutil
import os
import sqlite3

import ventas

global texto_imagen

def main():
    window = load_data()
    frame = frame_one(window)
    second_frame = frame_two(window)
    color = "#3E4446"
    label_one(frame, second_frame)

    """IB"""
    ib_id = customtkinter.CTkEntry(master=frame, placeholder_text='TEXTO')
    ib_id.pack(pady=12, padx=10)
    ib_id.place(x=110, y=67)
    ib_name = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Nombre del producto', width=400,
                                     height=35)
    ib_name.pack(pady=100, padx=10)
    ib_name.place(x=410, y=63)
    ib_desc = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese una descripción del producto', width=480,
                                     height=35)
    ib_desc.pack(pady=100, padx=10)
    ib_desc.place(x=330, y=106)

    ib_proveedor = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese Nombre del proveedor', width=350,
                                          height=35)
    ib_proveedor.pack(pady=100, padx=10)
    ib_proveedor.place(x=150, y=153)

    ib_precio = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese el precio', width=180, height=35)
    ib_precio.pack(pady=100, padx=10)
    ib_precio.place(x=630, y=153)

    ib_cantidad = customtkinter.CTkEntry(master=frame, placeholder_text='Ingrese la cantidad', width=180,
                                         height=35)
    ib_cantidad.pack(pady=100, padx=10)
    ib_cantidad.place(x=630, y=200)

    ib_num_factura = customtkinter.CTkEntry(master=frame, placeholder_text='CF/NUM. DE FACTURA',
                                            width=180, height=35)
    ib_num_factura.pack(pady=100, padx=10)
    ib_num_factura.place(x=200, y=245)

    lb_precio_confi = customtkinter.CTkLabel(master=second_frame, text='Precio:',
                                             font=("Times New Roman", 30))
    lb_precio_confi.pack(pady=400, padx=400)
    lb_precio_confi.place(x=445, y=140)

    lb_cantidad_confi = customtkinter.CTkLabel(master=second_frame, text='Cantidad:',
                                               font=("Times New Roman", 30))
    lb_cantidad_confi.pack(pady=400, padx=400)
    lb_cantidad_confi.place(x=440, y=190)

    lb_total_confi = customtkinter.CTkLabel(master=second_frame, text="TOTAL:",
                                            font=("Times New Roman", 30))
    lb_total_confi.pack(pady=400, padx=400)
    lb_total_confi.place(x=440, y=240)

    def seleccionar_imagen():
        get_image = filedialog.askopenfilenames(title="SELECT IMAGE",
                                                filetypes=(("png", "*.png"), ("jpg", "*.jpg"), ("Allfile", "*.*")))

        texto = str(get_image)
        texto_final = ""
        for i in range(2, len(texto) - 3):
            texto_final += texto[i]
        print(texto_final)
        ruta_imagen_origen = str(texto_final)
        ruta_carpeta_destino = 'imagenes'
        if not os.path.exists(ruta_carpeta_destino):
            os.makedirs(ruta_carpeta_destino)

        shutil.copy(ruta_imagen_origen, ruta_carpeta_destino)
        texto_alrevez = ""
        for i in range(len(texto_final)):
            texto_alrevez += texto_final[-i-1]
        texto_final_alrevez = ""
        for i in range(len(texto_alrevez)):
            if texto_alrevez[i] == "/":
                break
            texto_final_alrevez += texto_alrevez[i]
        texto_image = ""
        for i in range(len(texto_final_alrevez)):
            texto_image += texto_final_alrevez[-i-1]
        global texto_imagen
        texto_imagen = texto_image

        button_select_img = customtkinter.CTkButton(master=frame, text="Seleccionar", fg_color=color,
                                                    command=seleccionar_imagen)
        button_select_img.pack(pady=100, padx=10)
        button_select_img.place(x=260, y=207)

        lb_mostrar_datos = customtkinter.CTkLabel(master=second_frame, text="", font=("Times New Roman", 20))

        lb_mostrar_datos.pack(pady=12, padx=10)
        lb_mostrar_datos.place(x=10, y=70)

        imagen_carga = 'imagenes/imagen_carga.png'

        # imagen
        img_path = os.path.join(os.path.dirname(__file__), imagen_carga)
        image = customtkinter.CTkImage(light_image=Image.open(img_path), size=(150, 150))
        img_label = customtkinter.CTkLabel(second_frame, image=image, text="")
        img_label.place(x=130, y=150)

    def confirmacion_1():
        # definir variables
        id_code = ib_id.get()
        producto = ib_name.get()
        descripcion = ib_desc.get()
        proveedor = ib_proveedor.get()
        precio = int(ib_precio.get())
        cantidad = int(ib_cantidad.get())
        numero_de_factura = ib_num_factura.get()
        total = precio * cantidad
        print(texto_imagen + " 1231")

        # texto mostrar
        txt_mostrar = ("Codigo: " + id_code + " - Producto: " + producto + " - Descripción: " + descripcion +
                       " - Numero de factura:" + numero_de_factura + '\n' + " - Proveedor: " + proveedor)

        # label mostrar datos
        lb_mostrar_datos.configure(text=txt_mostrar, fg_color=color)
        imagen_carga2 = 'imagenes/' + texto_imagen
        img_path2 = os.path.join(os.path.dirname(__file__), imagen_carga2)
        image.configure(light_image=Image.open(img_path2), size=(150, 150))

        lb_precio_confi.configure(text=f'Precio:       Q{precio}')
        lb_cantidad_confi.configure(text=f'Cantidad:       Q{cantidad}')
        lb_total_confi.configure(text=f'TOTAL:      Q{total}')

        # desactivar input box
        ib_id.configure(state="disable")
        ib_name.configure(state="disable")
        ib_desc.configure(state="disable")
        ib_proveedor.configure(state="disable")
        ib_precio.configure(state="disable")
        ib_cantidad.configure(state="disable")
        ib_num_factura.configure(state="disable")

    def reset_all():
        ib_id.configure(state="normal")
        ib_name.configure(state="normal")
        ib_desc.configure(state="normal")
        ib_proveedor.configure(state="normal")
        ib_precio.configure(state="normal")
        ib_cantidad.configure(state="normal")
        ib_num_factura.configure(state="normal")

        ib_id.delete(0, 'end')
        ib_name.delete(0, 'end')
        ib_desc.delete(0, 'end')
        ib_proveedor.delete(0, 'end')
        ib_precio.delete(0, 'end')
        ib_cantidad.delete(0, 'end')
        ib_num_factura.delete(0, 'end')

        lb_mostrar_datos.configure(text="", fg_color=color)
        image.configure(light_image=Image.open(imagen_carga), size=(150, 150))

        lb_precio_confi.configure(text='Precio:')
        lb_cantidad_confi.configure(text='Cantidad:')
        lb_total_confi.configure(text='TOTAL:')

    def confirmacion_2():
        source_image = f'imagenes/{texto_imagen}'
        with open(source_image, 'rb') as archivo:
            datos_imagen = archivo.read()

        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO objetos_de_inventario (Nombre, "
                           "Descripción, "
                           "Costo, "
                           "Cantidad, "
                           "Proveedor, "
                           "Serie, "
                           "Imagen) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (ib_name.get(),
                            ib_desc.get(),
                            int(ib_precio.get()),
                            int(ib_cantidad.get()),
                            ib_proveedor.get(),
                            ib_id.get(),
                            sqlite3.Binary(datos_imagen)))
            messagebox.showinfo('¡Datos Ingresados Correctamente!', 'Los datos ingresados fueron '
                                                                    'enviados correctamente a la base de datos.')
        except Exception as ex:
            messagebox.showerror('¡Datos Ingresados Incorrectamente!', 'Vaya, parece que un campo'
                                                                       'no coincide con la base de datos, verifica los '
                                                                       'datos ingresados.')
            reset_all()
            print(ex)

        conexion.commit()
        conexion.close()
        reset_all()

    def editar():
        # activar input box
        ib_id.configure(state="normal")
        ib_name.configure(state="normal")
        ib_desc.configure(state="normal")
        ib_proveedor.configure(state="normal")
        ib_precio.configure(state="normal")
        ib_cantidad.configure(state="normal")
        ib_num_factura.configure(state="normal")
        lb_mostrar_datos.configure(text="", fg_color="transparent")

        imagen_carga2 = 'imagenes/imagen_carga.png'
        img_path2 = os.path.join(os.path.dirname(__file__), imagen_carga2)
        image.configure(light_image=Image.open(img_path2), size=(150, 150))

    # confirmación
    button_confirm_1 = customtkinter.CTkButton(master=frame, text="Confirmar", fg_color=color, width=180, height=45,
                                               command=confirmacion_1)
    button_confirm_1.pack(pady=100, padx=10)
    button_confirm_1.place(x=630, y=240)

    button_confirm_2 = customtkinter.CTkButton(master=second_frame, text="Confirmar", fg_color=color, width=180,
                                               height=45,
                                               command=confirmacion_2)
    button_confirm_2.pack(pady=100, padx=10)
    button_confirm_2.place(x=630, y=280)

    button_edit = customtkinter.CTkButton(master=second_frame, text="Editar", fg_color=color, width=180, height=45,
                                          command=editar)
    button_edit.pack(pady=100, padx=10)
    button_edit.place(x=440, y=280)

    window.mainloop()

    return

def load_data():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    # root
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Compras")
    ventana.geometry('950x750')
    ventana.iconbitmap('icon.ico')

    return ventana

def frame_one(window):
    frame = customtkinter.CTkFrame(master=window)
    frame.pack(pady=10, padx=60, fill='both', ipady=60)

    return frame
def frame_two(window):
    frame = customtkinter.CTkFrame(master=window)
    frame.pack(pady=0, padx=60, fill='both', ipady=80)
    return frame

def label_one(frame, second_frame):
    lb_inbreso = customtkinter.CTkLabel(master=frame, text='Ingreso', font=("Times New Roman", 50, "bold"))
    lb_inbreso.pack(pady=400, padx=400, )
    lb_inbreso.place(x=10, y=0)

    lb_id = customtkinter.CTkLabel(master=frame, text='Codigo', font=("Times New Roman", 30))
    lb_id.pack(pady=400, padx=400, )
    lb_id.place(x=10, y=60)

    lb_name_product = customtkinter.CTkLabel(master=frame, text='Producto', font=("Times New Roman", 30))
    lb_name_product.pack(pady=400, padx=400)
    lb_name_product.place(x=290, y=60)

    lb_des_product = customtkinter.CTkLabel(master=frame, text='Descripción del producto', font=("Times New Roman", 30))
    lb_des_product.pack(pady=400, padx=400)
    lb_des_product.place(x=10, y=105)

    lb_proveedor = customtkinter.CTkLabel(master=frame, text='Proveedor', font=("Times New Roman", 30))
    lb_proveedor.pack(pady=400, padx=400)
    lb_proveedor.place(x=10, y=150)

    lb_precio = customtkinter.CTkLabel(master=frame, text='Precio', font=("Times New Roman", 30))
    lb_precio.pack(pady=400, padx=400)
    lb_precio.place(x=515, y=160)

    lb_select_img = customtkinter.CTkLabel(master=frame, text='Seleccionar Imagen', font=("Times New Roman", 30))
    lb_select_img.pack(pady=400, padx=400)
    lb_select_img.place(x=10, y=200)

    lb_cantidad = customtkinter.CTkLabel(master=frame, text='Cantidad', font=("Times New Roman", 30))
    lb_cantidad.pack(pady=400, padx=400)
    lb_cantidad.place(x=512, y=210)

    lb_num_factura = customtkinter.CTkLabel(master=frame, text='Num. Factura', font=("Times New Roman", 30))
    lb_num_factura.pack(pady=400, padx=400)
    lb_num_factura.place(x=10, y=245)

    # lb
    lb_confirm = customtkinter.CTkLabel(master=second_frame, text='Confirmación', font=("Times New Roman", 50, "bold"))
    lb_confirm.pack(pady=400, padx=400, )
    lb_confirm.place(x=10, y=10)

    lb_precio_confi = customtkinter.CTkLabel(master=second_frame, text='Precio:      ',
                                             font=("Times New Roman", 30))
    lb_precio_confi.pack(pady=400, padx=400)
    lb_precio_confi.place(x=445, y=140)

    lb_cantidad_confi = customtkinter.CTkLabel(master=second_frame, text='Cantidad:  ',
                                               font=("Times New Roman", 30))
    lb_cantidad_confi.pack(pady=400, padx=400)
    lb_cantidad_confi.place(x=440, y=190)

    lb_total_confi = customtkinter.CTkLabel(master=second_frame, text="TOTAL:    ", font=("Times New Roman", 30))
    lb_total_confi.pack(pady=400, padx=400)
    lb_total_confi.place(x=440, y=240)

ventas.main()

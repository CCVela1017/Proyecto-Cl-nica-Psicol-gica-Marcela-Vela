
import random
from fpdf import FPDF
import datetime
import sqlite3

# Diccionario para el membrete

letterhead = {
    'Name': 'CLINICA PSICOLÓGICA MARCELA VELA',
    'Nit': '16846212',
    'Dirección': 'Centro Médico de Occidente, Calle "A" 19-46, zona 3., Quetzaltenango, Guatemala'
}


# Clase factura (recibe información de consumidor, lista de servicios)
class Bill:
    def __init__(self, customer: dict, services: list):
        self.customer = customer
        self.bill_num = str(random.randint(1, 1000))
        self.services = services
        self.total = 0

    def register_bill(self):
        conexion = sqlite3.connect('src/database')
        cursor = conexion.cursor()

        try:
            cursor.execute("INSERT INTO facturas_ventas (numero, "
                           "name_cliente, "
                           "nit_cliente, "
                           "dir_cliente, "
                           "dia, "
                           "mes, "
                           "anio, "
                           "monto_total, "
                           "forma_pago) "
                           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (self.customer["no"],
                            self.customer["name"],
                            self.customer["nit"],
                            self.customer["dir"],
                            datetime.datetime.today().date().day,
                            datetime.datetime.today().date().month,
                            datetime.datetime.today().date().year,
                            self.total,
                            self.customer["fpago"]))

        except Exception as ex:
            print(ex)

        conexion.commit()
        conexion.close()

    def print_bill(self):

        pdf = FPDF()
        pdf.set_font('times', size=10)
        pdf.add_page()

        # Titulo de la factura
        pdf.cell(40, 10, f'FACTURA NO.{self.customer["no"]}', ln=1)

        # Membrete
        # ln = salto de linea
        pdf.cell(40, 10, f'{letterhead["Name"]}', ln=1)
        pdf.cell(40, 10, f'Nit: {letterhead["Nit"]}', ln=1)
        pdf.cell(40, 10, f'Dirección: {letterhead["Dirección"]}', ln=1)

        # Pongo imagen (x, y, width, height)
        pdf.image('icon.png', 155, 5, 42, 42)

        # Tabla de información sobre el cliente
        with pdf.table(text_align='CENTER') as tabla:
            fila = tabla.row()
            fila.cell(f'No. {self.customer["no"]}')
            fila.cell(f'Nombre:\n {self.customer["name"]}')
            fila.cell(f'NIT:\n{self.customer["nit"]}')
            fila.cell(f'Dirección:\n{self.customer["dir"]}')

        # Fila de enzabezados (Cantidad, Servicios, Monto)
        with pdf.table(text_align='CENTER') as tabla:
            fila = tabla.row()
            fila.cell('Cantidad')
            fila.cell('Servicios')
            fila.cell('Monto')

        # Se crea la tabla donde se verán los servicios
        with pdf.table(text_align='LEFT') as tabla:
            # Ciclo para mostrar cada servicio (self.services es una matriz cada fila es un servicio vendido)
            for i in self.services:
                fila = tabla.row()
                # Muestro cantidad
                fila.cell(str(i[0]))
                # Muestro nombre del servicio
                fila.cell(i[1])
                # Muestro monto del servicio
                fila.cell('Q' + str(i[2]))
                # Le sumo el monto al todal de la factura
                self.total += i[2]

            # Creo una fila para mostrar el total de factura
            fila = tabla.row()
            fila.cell('TOTAL', colspan=2)
            fila.cell('Q' + str(self.total), colspan=1)
            # Agrego una fila para mostrar la fecha de compra
            fila = tabla.row()
            fila.cell(f'Fecha de generación: {datetime.datetime.today().date()}', colspan=3)
        # Genero factura en un pdf
        pdf.output(f'factura{self.bill_num}.pdf')

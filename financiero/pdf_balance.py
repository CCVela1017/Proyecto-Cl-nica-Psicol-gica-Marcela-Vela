from fpdf import FPDF

class BalancePDF:
    def __init__(self, balance: dict):
        self.balance = balance

    def print_balance(self):

        pdf = FPDF()
        pdf.set_font('times', size=10)
        pdf.add_page()

        # Titulo de la factura
        pdf.cell(40, 10, f'BALANCE GENERAL', ln=1)

        # Membrete
        # ln = salto de linea
        pdf.cell(40, 10, f'Fecha: {self.balance["month"]}/{self.balance["year"]}', ln=1)

        # Pongo imagen (x, y, width, height)
        pdf.image('icon.png', 170, 6, 21, 21)

        with pdf.table(text_align='CENTER') as tabla:
            fila = tabla.row()
            fila.cell('Código')
            fila.cell('Cuenta')
            fila.cell('Débito')
            fila.cell('Crédito')

        with pdf.table(text_align='CENTER') as tabla:
            fila = tabla.row()
            fila.cell('ACTIVOS CORRIENTES', colspan=4)
            fila = tabla.row()
            fila.cell('1111')
            fila.cell('Caja')
            fila.cell(f'Q{self.balance["caja"]}')
            fila.cell('')
            fila = tabla.row()
            fila.cell('1112')
            fila.cell('Bancos')
            fila.cell(f'Q{self.balance["banco"]}')
            fila.cell('')
            fila = tabla.row()
            fila.cell('1174')
            fila.cell('Papelería y Útiles')
            fila.cell(f'Q{self.balance["papeleria"]}')
            fila.cell('')
            fila = tabla.row()
            fila.cell('ACTIVOS NO CORRIENTES', colspan=4)
            fila = tabla.row()
            fila.cell('1224')
            fila.cell('Mobiliario y Equipo')
            fila.cell(f'Q{self.balance["mobiliario"]}')
            fila.cell('')
            fila = tabla.row()
            fila.cell('OTROS', colspan=4)
            fila = tabla.row()
            fila.cell('3100')
            fila.cell('Patrimonio Neto')
            fila.cell(f'Q{self.balance["patrimonio"]}')
            fila.cell('')
            fila = tabla.row()
            fila.cell('3210')
            fila.cell('Capital Social')
            fila.cell(f'Q{self.balance["capital_s"]}')
            fila.cell('')
            fila = tabla.row()
            fila.cell('')
            fila.cell('Utilidades retenidas')
            fila.cell('')
            fila.cell(f'Q{self.balance["utilidades_r"]}')
            fila = tabla.row()
            fila.cell('Sumas iguales', colspan=2)
            fila.cell(self.balance["total"])
            fila.cell(self.balance["total"])

        # Genero factura en un pdf
        pdf.output(f'LibroBalance{self.balance["month"]}{self.balance["year"]}.pdf')


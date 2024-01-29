import os
from datetime import datetime

from PyQt6 import QtSql
from reportlab.pdfgen import canvas

import var
from Facturas import *
from Facturas.facturacion_repository import Facturacion_Repository
from informes import informes


class Facturacion_informes:
    def report_facturas(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_factura.pdf'
            var.report = canvas.Canvas('Facturacion\\' + nombre)
            titulo = 'Factura Cliente'
            informes.top_informe(titulo)
            informes.foot_informe(titulo)
            items = ['Id Viaje', 'Origen', 'Destino', 'Kilometros', 'Tarifa', 'Total']

            def print_Titulo(items):
                var.report.drawString(60, 675, str(items[0]))  # IdViaje
                var.report.drawString(120, 675, str(items[1]))  # Origen
                var.report.drawString(200, 675, str(items[2]))  # Destino
                var.report.drawString(300, 675, str(items[3]))  # Kilometros
                var.report.drawString(410, 675, str(items[4]))  # Tarifa
                var.report.drawString(480, 675, str(items[5]))  # Total
                var.report.line(50, 670, 525, 670)

            print_Titulo(items)
            print(var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
            lineas_de_viajes = Facturacion_Repository.recupera_lineas_de_viaje(var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
            print(lineas_de_viajes)
            y = 635
            for linea_de_viaje in lineas_de_viajes:
                if y <= 80:
                    var.report.showPage()  # creamos una pagina nueva
                    informes.top_informe(titulo)
                    informes.foot_informe(titulo)
                    print_Titulo(items)
                    var.report.setFont('Helvetica', size=7)
                    y = 635
                var.report.drawString(80, y, str(linea_de_viaje[0])) #idViaje
                var.report.drawString(120, y, str(linea_de_viaje[1])) #Origen
                var.report.drawString(200, y, str(linea_de_viaje[2])) #Destino
                var.report.drawString(300, y, str(linea_de_viaje[3])) #Kilometros
                var.report.drawString(410, y, str(linea_de_viaje[4])) #Tarifa
                var.report.drawString(480, y, str((linea_de_viaje[3]*linea_de_viaje[4]))) #Total
                y -= 20

            var.report.save()
            root_path = '.\\Facturacion\\'
            for file in os.listdir(root_path):
                if file.endswith(nombre):
                    os.startfile('%s%s' % (root_path, file))
        except Exception as e:
            print("error en la ejecucion del informe", e)
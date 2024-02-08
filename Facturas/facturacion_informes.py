import os
from datetime import datetime

from PyQt6 import QtSql
from PyQt6.QtGui import QBrush, QColor
from reportlab.pdfgen import canvas

import Ventanas
import var
from Facturas import *
from Facturas import facturacion
from Facturas.facturacion_repository import Facturacion_Repository
from informes import informes


class Facturacion_informes:
    def report_facturas(self):
        """
        Método para generar y mostrar un informe de factura para un cliente seleccionado.

        :param self: Referencia al objeto actual.
        :type self: object

        :return: None

        Descripción:
        Este método genera un informe de factura para un cliente seleccionado en la interfaz.
        Primero verifica si se ha seleccionado una factura en la tabla de facturas. Si no se ha seleccionado ninguna, muestra un mensaje de advertencia y termina la ejecución del método.
        Luego, obtiene la fecha actual y crea un nombre único para el archivo PDF del informe.
        Después, inicializa el lienzo del informe y establece el título de la factura.
        Rellena los datos del cliente en el informe.
        Agrega los encabezados de las columnas y recupera las líneas de viaje asociadas a la factura seleccionada.
        Itera sobre las líneas de viaje y agrega sus datos al informe, calculando el subtotal, el IVA y el total de la factura.
        Guarda el informe como un archivo PDF y lo muestra en el sistema de archivos del usuario.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:

            if var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0) is None:
                Ventanas.Ventanas.mensaje_warning("Selecciona una factura para imprimir")
                return
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_factura.pdf'
            var.report = canvas.Canvas('Facturacion\\' + nombre)
            titulo = 'Factura Cliente'
            informes.top_informe_factura(titulo)
            Facturacion_informes.rellenar_datos_cliente(self)
            informes.foot_informe(titulo)
            items = ['Id Viaje', 'Origen', 'Destino', 'Kilometros', 'Tarifa', 'Total']

            def print_Titulo(items):
                var.report.drawCentredString(85, 625, str(items[0]))  # IdViaje
                var.report.drawCentredString(155, 625, str(items[1]))  # Origen
                var.report.drawCentredString(255, 625, str(items[2]))  # Destino
                var.report.drawCentredString(335, 625, str(items[3]))  # Kilometros
                var.report.drawCentredString(415, 625, str(items[4]))  # Tarifa
                var.report.drawCentredString(485, 625, str(items[5]))  # Total
                var.report.line(50, 620, 525, 620)

            print_Titulo(items)
            print(var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
            lineas_de_viajes = Facturacion_Repository.recupera_lineas_de_viaje(
                var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
            print(lineas_de_viajes)
            y = 605
            precio_subtotal = 0
            for numerofila, linea_de_viaje in enumerate(lineas_de_viajes):
                if y <= 120:
                    var.report.showPage()  # creamos una pagina nueva
                    informes.top_informe_factura(titulo)
                    Facturacion_informes.rellenar_datos_cliente(self)
                    informes.foot_informe(titulo)
                    print_Titulo(items)
                    var.report.setFont('Helvetica', size=7)
                    y = 605
                var.report.setFont('Helvetica', size=10)
                var.report.drawCentredString(85, y, str(linea_de_viaje[0]))  # idViaje
                var.report.drawCentredString(155, y, str(linea_de_viaje[1]))  # Origen
                var.report.drawCentredString(255, y, str(linea_de_viaje[2]))  # Destino
                var.report.drawCentredString(335, y, str(linea_de_viaje[3]))  # Kilometros
                var.report.drawCentredString(415, y, str(linea_de_viaje[4]))  # Tarifa
                var.report.drawCentredString(485, y, str((linea_de_viaje[3] * linea_de_viaje[4])))  # Total
                precio_subtotal += (linea_de_viaje[3] * linea_de_viaje[4])
                y -= 20
                if numerofila == len(lineas_de_viajes) - 1:
                    var.report.setFont('Helvetica-Bold', size=12)
                    var.report.drawString(400, y - 10, "Subtotal:")
                    var.report.drawString(400, y - 30, "IVA 21%:")
                    var.report.drawString(400, y - 50, "Total:")
                    var.report.setFont('Helvetica', size=10)
                    var.report.drawRightString(500, y - 10, str(round(precio_subtotal,2))+"€")
                    var.report.drawRightString(500, y - 30, str(round(precio_subtotal*0.21,2))+"€")
                    var.report.drawRightString(500, y - 50, str(round((precio_subtotal*0.21)+precio_subtotal,2))+"€")

            var.report.save()
            root_path = '.\\Facturacion\\'
            for file in os.listdir(root_path):
                if file.endswith(nombre):
                    os.startfile('%s%s' % (root_path, file))
        except Exception as e:
            print("error en la ejecucion del informe", e)

    def rellenar_datos_cliente(datos_cliente_factura):
        """
        Método para rellenar los datos del cliente en el informe de factura.

        :param datos_cliente_factura: Lista que contiene los datos del cliente para la factura.
        :type datos_cliente_factura: list

        :return: None

        Descripción:
        Este método rellena los datos del cliente en el informe de factura.
        Recupera los datos del cliente utilizando el método `recuperar_datos_cliente_factura()` del repositorio de facturación.
        Luego, establece la fuente y el tamaño de la letra para los encabezados y los datos del cliente en el informe.
        Finalmente, imprime los datos del cliente en posiciones específicas en el informe.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:

            datos_cliente_factura = Facturacion_Repository.recuperar_datos_cliente_factura()
            var.report.setFont('Helvetica-Bold', size=14)
            var.report.drawString(210, 785, 'Datos del Cliente')
            var.report.setFont('Helvetica-Bold', size=7)
            var.report.drawString(210, 770, 'Nº de factura')
            var.report.drawString(210, 755, 'Fecha de la factura')
            var.report.drawString(210, 740, 'Razón Social')
            var.report.drawString(210, 725, 'Direccion')
            var.report.drawString(210, 710, 'Telefono')
            var.report.drawString(210, 695, 'Provincia')
            var.report.drawString(210, 680, 'Municipio')
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(290, 770, str(datos_cliente_factura[0]))
            var.report.drawString(290, 755, str(datos_cliente_factura[1]))
            var.report.drawString(290, 740, str(datos_cliente_factura[2]))
            var.report.drawString(290, 725, str(datos_cliente_factura[3]))
            var.report.drawString(290, 710, str(datos_cliente_factura[4]))
            var.report.drawString(290, 695, str(datos_cliente_factura[5]))
            var.report.drawString(290, 680, str(datos_cliente_factura[6]))

        except Exception as e:
            print("Eror a la hora de printear los datos de un cliente",e)



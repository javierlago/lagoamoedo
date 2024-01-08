from datetime import datetime

from PyQt6 import QtSql
from reportlab.pdfgen import canvas
import var,os,shutil
import var
from svglib.svglib import svg2rlg
import sqlite3



class informes:




    def reportclientes(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoclientes.pdf'
            var.report = canvas.Canvas('informes\\'+nombre)
            titulo = 'Listado de Clientes'
            informes.top_informe(titulo)
            informes.foot_informe(titulo)
            items = ['Codigo','DNI','Razon','Municipico','Provincia','Baja Cliente']
            def print_Titulo(items):
                var.report.drawString(60,675,str(items[0]))
                var.report.drawString(120,675,str(items[1]))
                var.report.drawString(180,675,str(items[2]))
                var.report.drawString(240,675,str(items[3]))
                var.report.drawString(300,675,str(items[4]))
                var.report.drawString(360,675,str(items[5]))
                var.report.line(50, 670, 50, 670)
            print_Titulo(items)

            #Obtencion de datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select codigo ,dnicliente,razon, muniCliente, provCliente,bajaCliente from listadoclientes order by razon')
            var.report.setFont('Helvetica',size=9)
            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <=80:
                        var.report.showPage() #creamos una pagina nueva
                        informes.top_informe(titulo)
                        informes.foot_informe(titulo)
                        print_Titulo(items)
                        var.report.line(50,670,50,670)
                        var.report.drawString(60, j, query.value(0))
                        var.report.drawString(120, j, query.value(0))
                        var.report.drawString(240, j, query.value(1))
                        var.report.drawString(300, j, query.value(2))
                        var.report.drawString(360, j, query.value(3))
                        var.report.drawString(360, j, query.value(4))
                        j +=10
                    var.report.line(50, 670, 50, 670)
                    var.report.drawString(60, j, str(query.value(0)))
                    var.report.drawString(120, j, str(query.value(0)))
                    var.report.drawString(240, j, str(query.value(1)))
                    var.report.drawString(300, j, str(query.value(2)))
                    var.report.drawString(360, j, str(query.value(3)))
                    var.report.drawString(360, j, str(query.value(4)))
                    j += 10








            ## var.report.drawString(250,250,'Mi primer informe')
            var.report.save()
            root_path = '.\\informes\\'
            for file in os.listdir(root_path):
                if file.endswith(nombre):
                    os.startfile('%s%s' % (root_path, file))
        except Exception as e:
            print(e)


    def top_informe(titulo):
        try:

            logo = '.\\img\\taxiIcon.png'
            var.report.line(50, 800, 525, 800)
            var.report.setFont('Helvetica-Bold', size=14)
            var.report.drawString(55, 785, 'Trasnsportes Teis')
            var.report.drawString(240, 695, titulo)
            var.report.line(50, 690, 525, 690)
            var.report.drawImage(logo, 440, 725, width=45, height=45)
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(55, 770, 'CIF:A12345678')
            var.report.drawString(55, 755, 'Avd Galicia 101')
            var.report.drawString(55, 740, 'Vigo - 36216 - España')
            var.report.drawString(55, 725, 'Telefono: 986 123 456')
            var.report.drawString(55, 710, 'e-mail carteis@gmail.com')


        except Exception as e:
            print(e)



    def foot_informe(titulo):
        try:
            var.report.line(50,50,525,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Bold', size=7)
            var.report.drawString(50,40,str(fecha))
            var.report.drawString(250,40,str(titulo))
            var.report.drawString(490,40,str('Pagina %s' % var.report.getPageNumber()))
        except Exception as e :
            print(e)




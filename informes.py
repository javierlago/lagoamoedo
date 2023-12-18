from datetime import datetime
from reportlab.pdfgen import canvas
import var,os,shutil
import var
from svglib.svglib import svg2rlg



class informes:

    def reportclientes(self):
        try:
            var.report = canvas.Canvas('informes\\listado.pdf')
            titulo = 'Listado de Clientes'
            informes.top_informe(titulo)
            informes.foot_informe(titulo)
            var.report.drawString(250,250,'Mi primer informe')
            var.report.save()
            root_path = '.\\informes'
            for file in os.listdir(root_path):
                if file.endswith('informes\\listado.pdf'):
                    os.startfile('%s%s'%(root_path, file))
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




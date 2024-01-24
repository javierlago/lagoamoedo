
import WindowCalendar
import drivers
import eventos
import informes
import var
from AcercaDeWindow import Ui_AcercaDe
from VentanaPrint import Ui_menu_printear
from VentanaSalir import Ui_ventanaSalir
from PyQt6 import QtWidgets



class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = WindowCalendar.Ui_WindowCalendar()
        var.calendar.setupUi(self)
        var.calendar.calendarWidget.selectedDate()
        var.calendar.calendarWidget.clicked.connect(drivers.Drivers.carga_fecha)


class SalirVentana(QtWidgets.QDialog):
    def __init__(self):
        super(SalirVentana, self).__init__()
        var.ventana_salir = Ui_ventanaSalir()
        var.ventana_salir.setupUi(self)
        var.ventana_salir.btnAcept.clicked.connect(eventos.Eventos.salir)
        var.ventana_salir.btnCancelar.clicked.connect(eventos.Eventos.hide_salir)


class Acerca(QtWidgets.QDialog):
    def __init__(self):
        super(Acerca, self).__init__()
        var.acercade = Ui_AcercaDe()
        var.acercade.setupUi(self)
        var.acercade.pushButton.clicked.connect(eventos.Eventos.salir_acerca_de)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()


class print_dialog(QtWidgets.QDialog):
    def __init__(self):
        super(print_dialog, self).__init__()
        var.print_facturas = Ui_menu_printear()
        var.print_facturas.setupUi(self)
        var.print_facturas.pushButton.clicked.connect(self.panel_informes)
        self.boton1= var.print_facturas.radioButton
        self.boton2= var.print_facturas.radioButton_2
    def panel_informes(self):
        try:

            if self.boton1.isChecked():
                informes.informes.reportclientes(self)
                self.hide()
            elif self.boton2.isChecked():
                informes.informes.report_conductores(self)
                self.hide()


        except Exception as error:
            print("Mierda",error)
from datetime import *
import WindowCalendar
import drivers
import eventos
import var
from AcercaDeWindow import Ui_AcercaDe
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

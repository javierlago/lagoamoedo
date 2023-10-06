from datetime import datetime
import sys



import eventos
import var
from WindowCalendar import *
from MainWindow import *
from AcercaDeWindow import *
from VentanaSalir import  *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

        var.ui = Ui_MainWindow()
        var.ui.setupUi(self) #metodo encargado de genera la interfaz
        var.calendar = Calendar()
        var.acercade = Acerca()
        var.ventana_salir = SalirVentana()

        '''
        ZONA DE EVENTOS
        
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)


        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.abrirAcercaDe)
        '''
        zona de eventos salir
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_WindowCalendar()
        var.calendar.setupUi(self)
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year

class  SalirVentana(QtWidgets.QDialog):
    def __init__(self):
        super(SalirVentana, self).__init__()
        var.ventana_salir = Ui_ventanaSalir()
        var.ventana_salir.setupUi(self)
        var.ventana_salir.btnAcept.clicked.connect(eventos.Eventos.salir)
        var.ventana_salir.btnCancelar.clicked.connect(eventos.Eventos.hideSalir)




class Acerca(QtWidgets.QDialog):
    def __init__(self):
        super(Acerca, self).__init__()
        var.acercade = Ui_AcercaDe()
        var.acercade.setupUi(self)
        var.acercade.pushButton.clicked.connect(eventos.Eventos.salirAcercaDe)







if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())



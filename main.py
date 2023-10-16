import sys
from MainWindow import *
from windowaux import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # metodo encargado de genera la interfaz
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
        var.ui.Salir.triggered.connect(eventos.Eventos.showSalir)
        """
        zona de eventos cajas
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDNI)

        """
        eventos de la menubar
        """
        var.ui.Salir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.btnLimpiar.triggered.connect(eventos.Eventos.limpiar)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

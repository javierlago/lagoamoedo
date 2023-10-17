import sys
from MainWindow import *
from windowaux import *
import locale
import var
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


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
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrir_calendar)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.abrir_acerca_de)

        '''
        zona de eventos salir
        '''
        var.ui.Salir.triggered.connect(eventos.Eventos.show_salir)

        """
        zona de eventos cajas
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDNI)

        """
        
        eventos de la menubar
        
        """
        var.ui.Salir.triggered.connect(eventos.Eventos.show_salir)
        var.ui.btnLimpiar.triggered.connect(eventos.Eventos.limpiar)
        '''
        
        status var
    
        '''

        eventos.Eventos.cargastatusbar(self)
        eventos.Eventos.cargaprov()

        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.sel_estado)
    def closeEvent(self, event):

            mbox = QtWidgets.QMessageBox.information(self, "Salir", "Estas seguro de salir?",
                                                     QtWidgets.QMessageBox.StandardButton.Yes |
                                                     QtWidgets.QMessageBox.StandardButton.No)

            if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
                app.quit()
            if mbox == QtWidgets.QMessageBox.StandardButton.No:
                event.ignore()




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

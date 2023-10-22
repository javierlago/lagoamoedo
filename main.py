import sys

from PyQt6.QtWidgets import QApplication

from MainWindow import *
from windowaux import *
import locale
import var
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # metodo encargado de genera la interfaz
        screen = QApplication.primaryScreen().geometry()
        self.setMaximumSize(screen.width(), screen.height())
        var.calendar = Calendar()
        var.acercade = Acerca()
        var.ventana_salir = SalirVentana()

        '''
        
        ZONA DE EVENTOS
        
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrir_calendar)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.abrir_acerca_de)
        var.ui.btnaltaDriver.clicked.connect(drivers.Drivers.alta_driver)

        '''
        zona de eventos salir
        '''
        var.ui.actionSalir.triggered.connect(eventos.Eventos.show_salir)

        """
        zona de eventos cajas
        """
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validar_dni)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.format_caja_texto)
        var.ui.txtDni_2.editingFinished.connect(eventos.Eventos.format_caja_texto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.format_caja_texto)

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

        '''
        eventos de tablas  
        '''
        eventos.Eventos.resize_tabDriver2(self)


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
    app = QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())

from datetime import datetime
import sys

import eventos
import var
from WindowCalendar import *
from MainWindow import *




class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self) #metodo encargado de genera la interfaz
        var.calendar = Calendar()

        '''
        ZONA DE EVENTOS
        
        '''
        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        '''
        zona de eventos salir
        '''
        var.ui.actiongit Salir.triggered.connect(eventos.Eventos.salir)

class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_WindowCalendar()
        var.calendar.setupUi(self)
        day = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())



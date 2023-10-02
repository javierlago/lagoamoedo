import eventos
from MainWindow import *
import sys, var
class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self) #metodo encargado de genera la interfaz
        '''
        ZONA DE EVENTOS
        
        '''
        var.ui.btnSalir.clicked.connect(eventos.Eventos.saludar)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())



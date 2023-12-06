from PyQt6.QtGui import QIcon
from PyQt6.uic.properties import QtWidgets
from PyQt6 import QtWidgets

class Ventanas:

    def mensaje_warning(mensaje):
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText(mensaje)
            icon = QIcon('./img/taxiIcon.png')
            mbox.setWindowIcon(icon)
            mbox.exec()
        except Exception as error:
            print(error)
    def ventana_info(mensaje):
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText(mensaje)
            icon = QIcon('./img/taxiIcon.png')
            mbox.setWindowIcon(icon)
            mbox.exec()
        except Exception as error :
            print("Fallo en la ventana info",error)
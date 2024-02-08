from PyQt6.QtGui import QIcon
from PyQt6.uic.properties import QtWidgets
from PyQt6 import QtWidgets

class Ventanas:


    def mensaje_warning( mensaje):
        """
            Función para mostrar un mensaje de advertencia en una ventana emergente.

            :param mensaje: El mensaje de advertencia a mostrar.
            :type mensaje: str

            :return: None

            Descripción:
            Esta función muestra un mensaje de advertencia en una ventana emergente. El mensaje puede ser cualquier texto proporcionado como argumento.
            """
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

    def ventana_info( mensaje):
        """
           Función para mostrar un mensaje de información en una ventana emergente.

           :param mensaje: El mensaje de información a mostrar.
           :type mensaje: str

           :return: None

           Descripción:
           Esta función muestra un mensaje de información en una ventana emergente. El mensaje puede ser cualquier texto proporcionado como argumento.
           """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText(mensaje)
            icon = QIcon('./img/taxiIcon.png')
            mbox.setWindowIcon(icon)
            mbox.exec()
        except Exception as error:
            print("Fallo en la ventana info", error)



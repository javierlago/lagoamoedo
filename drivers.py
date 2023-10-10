import var
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
class Drivers():
    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDate.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("erro en carga fecha", error)





    def validarDNI(self=None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {"X": "0", "Y": "1", "Z": "2"}
            numeros = "1234567890"

            if len(dni) == 9:  # comprueba que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni

                if dni[0] in dig_ext:  # reemplazas la letra por el numero correspondiente
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    # comprueba que no haya letras en el medio

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                   #  var.ui.lblCheckDNI.setStyleSheet('color:green;')
                    # var.ui.lblCheckDNI.setText('V')
                   var.ui.lblCheckDNI.setScaledContents(True)
                   var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/OkIco.svg"))

                else:
                    #var.ui.lblCheckDNI.setStyleSheet('color:red;')
                    ##var.ui.lblCheckDNI.setText('X')
                    var.ui.lblCheckDNI.setScaledContents(True)
                    var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                    var.ui.txtDni.setText("")
                    var.ui.txtDni.setFocus()
            else:
              #  var.ui.lblCheckDNI.setStyleSheet('color:red;')
               # var.ui.lblCheckDNI.setText('X')
                var.ui.lblCheckDNI.setScaledContents(True)
                var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                var.ui.txtDni.setText("")
                var.ui.txtDni.setFocus()
        except Exception as error:
            print("error en validar dni: ", error)


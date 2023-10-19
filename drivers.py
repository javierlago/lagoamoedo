import var
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime


class Drivers():
    def carga_fecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDate.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("erro en carga fecha", error)

    def validar_dni(self=None):
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
                    # var.ui.lblCheckDNI.setStyleSheet('color:red;')
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

    def alta_driver(self):
        try:
            driver = [var.ui.txtDni_2, var.ui.txtNombre, var.ui.txtMovil]
            newdriver = []
            newdriver.append(1)
            for i in driver:
                newdriver.append(i.text().title())

            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]

            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())

            newdriver.append(str("-".join(licencias)))
            index = 0
            var.ui.tabDriver2.setRowCount(index+1)
            var.ui.tabDriver2.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newdriver[0])))
            var.ui.tabDriver2.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newdriver[1])))
            var.ui.tabDriver2.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newdriver[2])))
            var.ui.tabDriver2.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newdriver[3])))
            var.ui.tabDriver2.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newdriver[4])))




            print(newdriver)



        except Exception as error:
            print("error alta cliente", error)

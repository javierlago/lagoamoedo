import re

import conexion
import var
from PyQt6 import QtGui, QtWidgets, QtCore


class Drivers:

    def validar_tlf(self=None):
        try:
            tlf = var.ui.txtMovil.text()

            # str(tlf).format('{9d}')
            # if len(tlf) != 9 and tlf != type(int)
            regex = r'^\d{9}$'

            if not re.match(regex, tlf):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Telefono icorrecto introducir nueve digitos')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.exec()
                var.ui.txtMovil.setText('')
                var.ui.txtMovil.setFocus()

            else:
                var.ui.txtMovil.setText(tlf)

        except Exception as error:
            print("error en validar telf: ", error)

        def validar_salario(self=None):
            sal = var.ui.txtSalario.text()
            rxTlf = r'^$'

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
                    var.ui.lblCheckDNI.show()
                    var.ui.lblCheckDNI.setScaledContents(True)
                    var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                    var.ui.txtDni.setText("")
                    var.ui.txtDni.setFocus()
            else:
                #  var.ui.lblCheckDNI.setStyleSheet('color:red;')
                # var.ui.lblCheckDNI.setText('X')
                var.ui.lblCheckDNI.show()
                var.ui.lblCheckDNI.setScaledContents(True)
                var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                var.ui.txtDni.setText("")
                var.ui.txtDni.setFocus()
        except Exception as error:
            print("error en validar dni: ", error)

    def alta_driver(self):
        try:
            driver = [var.ui.txtDni.text(), var.ui.txtDate.text(), var.ui.txtDni_2.text(), var.ui.txtNombre.text(),
                      var.ui.txtDireccion.text(), var.ui.cmbProvincia.currentText(),
                      var.ui.cmbLocalidad.currentText(), var.ui.txtMovil.text(), var.ui.txtSalario.text()]

            licencias = list()
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]

            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())

            driver.append(str("-".join(licencias)))

            # print(driver)
            conexion.Conexion.guardardri(driver)

        except Exception as error:
            print("error alta cliente", error)


    def cargartabla(registros):
        try:
            for registro in registros:
                index = 0
                var.ui.tabDrivers.setRowCount(index + 1)
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("Error completar tabla ", error)

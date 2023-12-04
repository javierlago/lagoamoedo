import re

from PyQt6.QtGui import QColor, QBrush, QIcon

import conexion
import drivers
import eventos

import var
from PyQt6 import QtGui, QtWidgets, QtCore


class Drivers:





    def borrar_datos(self):
        try:
            dni = var.ui.txtDni.text()
            print(dni)
            conexion.Conexion.borrarDriver(dni)
            conexion.Conexion.mostrardrivers()
        except Exception as error:
            print("Error al dar de baja a un conductor", error)



    def modif_driver(self):
        try:
            driver = drivers.Drivers.recuperar_datos()

            conexion.Conexion.modificar(driver)
            conexion.Conexion.mostrardrivers()



        except Exception as error:
            print("Error al modificar el conductor", error)

    def  get_from_dni (self):
        try:
            obteivo = None
            dni = var.ui.txtDni.text()
            drivers.Drivers.carga_driver(conexion.Conexion.buscar_segun_dni(dni))
            registro = conexion.Conexion.buscar_segun_dni(dni)
            if registro[11] == '':
                var.ui.rbtAlta.setChecked(True)
            else:
                var.ui.rbtBaja.setChecked(True)
            conexion.Conexion.mostrardrivers()


            for row in range(var.ui.tabDriver2.rowCount()):
                item = var.ui.tabDriver2.item(row, 0)
                if item and item.text() == str(registro[0]):
                    brush = QColor(247, 181, 0)
                    for col in range(var.ui.tabDriver2.columnCount()):
                        current_item = var.ui.tabDriver2.item(row, col)
                        if current_item is not None:
                            current_item.setBackground(brush)
                            obteivo = current_item
            var.ui.tabDriver2.scrollToItem(obteivo)
        except Exception as error:
            print("Error al cargar segun el DNI",error)

    def get_from_tab(self):
        try:
            # Limpiar el estilo de todas las filas
            for r in range(var.ui.tabDriver2.rowCount()):
                for c in range(var.ui.tabDriver2.columnCount()):
                    item = var.ui.tabDriver2.item(r, c)
                    if item is not None:
                        item.setBackground(QBrush(QColor(0, 0, 0, 0)))

            # Establecer el fondo amarillo solo para la fila seleccionada
            row = var.ui.tabDriver2.currentRow()
            for c in range(var.ui.tabDriver2.columnCount()):
                item = var.ui.tabDriver2.item(row, c)
                if item is not None:
                    item.setBackground(QBrush(QColor("#CCA963")))

            codigo = var.ui.tabDriver2.item(row, 0).text()
            if var.ui.tabDriver2.item(row,5).text() != '':
                var.ui.frame.show()
            else:
                var.ui.frame.hide()
            registro = conexion.Conexion.buscar_segun_codigo(codigo)
            drivers.Drivers.carga_driver(registro)

        except Exception as error:
            print("Error al cargar desde la tabla", error)




    def carga_driver(registro):

        try:
            if  registro == None:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('El dni no se encuentra en la base de datos')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                icon = QIcon('./img/taxiIcon.png')
                msg.setWindowIcon(icon)
                msg.exec()
            else:
                datos = [var.ui.lblCodDB, var.ui.txtDni, var.ui.txtDate, var.ui.txtDni_2, var.ui.txtNombre,
                         var.ui.txtDireccion,
                         var.ui.cmbProvincia, var.ui.cmbLocalidad, var.ui.txtMovil, var.ui.txtSalario]

                for i, dato in enumerate(datos):
                    if i == 6 or i == 7:
                        # Verificar si dato es un QComboBox
                            dato.setCurrentText(str(registro[i]))
                    else:
                        dato.setText(str(registro[i]))
                if 'A' in registro[10]:
                    var.ui.chkA.setChecked(True)
                else:
                    var.ui.chkA.setChecked(False)

                if 'B' in registro[10]:
                    var.ui.chkB.setChecked(True)
                else:
                    var.ui.chkB.setChecked(False)
                if 'C' in registro[10]:
                    var.ui.chkC.setChecked(True)
                else:
                    var.ui.chkC.setChecked(False)
                if 'D' in registro[10]:
                    var.ui.chkD.setChecked(True)
                else:
                    var.ui.chkD.setChecked(False)
                var.ui.txtDate_2.setText(str(registro[11]))
                var.ui.lblCheckDNI.show()
                var.ui.lblCheckDNI.setScaledContents(True)
                var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/OkIco.svg"))

                for fila in range(var.ui.tabDriver2.rowCount()):
                    if var.ui.tabDriver2.item(fila,0) == str(registro[0]):
                        print("hola")
                        var.ui.tabDriver2.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                        var.ui.tabDriver2.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                        var.ui.tabDriver2.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                        var.ui.tabDriver2.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                        var.ui.tabDriver2.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                        var.ui.tabDriver2.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                        var.ui.tabDriver2.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[5])))
                        var.ui.tabDriver2.item(fila, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabDriver2.item(fila, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabDriver2.item(fila, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabDriver2.setItem(fila,0).setBackground(247, 181, 0)
                        var.ui.tabDriver2.setItem(fila,1).setBackground(247, 181, 0)
                        var.ui.tabDriver2.setItem(fila,2).setBackground(247, 181, 0)
                        var.ui.tabDriver2.setItem(fila,3).setBackground(247, 181, 0)
                        var.ui.tabDriver2.setItem(fila,4).setBackground(247, 181, 0)



        except Exception as error:
            print("Error al cargar datos: ", error)

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
                icon = QIcon('./img/taxiIcon.png')
                msg.setWindowIcon(icon)
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
    def carga_fechaBaja(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDate_2.setText(str(data))
            var.calendarBaja.hide()
        except Exception as error:
            print("erro en carga fecha", error)

    def validar_dni(dni):
        try:
            #dni = var.ui.txtDni.text()
            dni = dni.upper()
            #var.ui.txtDni.setText(dni)
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
                    return True

                else:
                    # var.ui.lblCheckDNI.setStyleSheet('color:red;')
                    # var.ui.lblCheckDNI.setText('X')
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


    def recuperar_datos(self=None):
        driver =[var.ui.lblCodDB.text(),var.ui.txtDni.text(), var.ui.txtDate.text(), var.ui.txtDni_2.text(), var.ui.txtNombre.text(),
                      var.ui.txtDireccion.text(), var.ui.cmbProvincia.currentText(),
                      var.ui.cmbLocalidad.currentText(), var.ui.txtMovil.text(), var.ui.txtSalario.text()]
        licencias = list()
        chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]

        for i in chklicencia:
            if i.isChecked():
                licencias.append(i.text())

        driver.append(str("-".join(licencias)))
        driver.append(var.ui.txtDate_2.text())
        print(driver)

        return driver

    def validar_datos(listadeDatos):
        for i in range(len(listadeDatos) - 1):
            if listadeDatos[i].strip() == '':
                return False
        return True

    def alta_driver(self):
        try:
            driver = drivers.Drivers.recuperar_datos(self)
            driver.remove(driver[0])
            print("printeo del metodo")
            print(drivers.Drivers.validar_datos(driver))
            print("printeo del driver")
            print (driver)
            if not drivers.Drivers.validar_datos(driver):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = "Campos vacíos"
                mbox.setText(mensaje)
                icon = QIcon('./img/taxiIcon.png')
                mbox.setWindowIcon(icon)
                mbox.exec()
            else:
                if conexion.Conexion.guardardri(driver):
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)  # Cambié el icono a Information
                    mbox.setText('Empleado dado de alta')
                    icon = QIcon('./img/taxiIcon.png')
                    mbox.setWindowIcon(icon)
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("El DNI ya se encuentra en la base de datos")
                    mbox.exec()

            conexion.Conexion.mostrardrivers()
            eventos.Eventos.limpiar()

        except Exception as error:
            print("error alta cliente", error)

    @staticmethod
    def cargartabla(registros):

        try:
            nuevoRegistros = list()
            if (var.ui.rbtAlta.isChecked()):
                var.ui.frame.hide()
                for registro in registros:
                    if registro[5] == '':
                        nuevoRegistros.append(registro)
            elif (var.ui.rbtBaja.isChecked()):
                var.ui.frame.show()
                for registro in registros:
                    if registro[5] != '':
                        nuevoRegistros.append(registro)
            elif (var.ui.rbtTodos.isChecked()):
                var.ui.frame.hide()
                nuevoRegistros = registros

            if len(nuevoRegistros) == 0:
                var.ui.tabDriver2.setRowCount(0)
            else:
                index = 0
                for registro in nuevoRegistros:
                    var.ui.tabDriver2.setRowCount(index + 1)
                    var.ui.tabDriver2.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.tabDriver2.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                    var.ui.tabDriver2.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                    var.ui.tabDriver2.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                    var.ui.tabDriver2.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                    var.ui.tabDriver2.setItem(index, 5,QtWidgets.QTableWidgetItem(str(registro[5])))
                    var.ui.tabDriver2.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDriver2.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDriver2.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabDriver2.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index += 1
        except Exception as error:
            print("Error completar tabla ", error)

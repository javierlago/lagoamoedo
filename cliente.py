import locale
import re

from PyQt6.QtGui import QColor, QBrush, QIcon

import cliente
import conexion
import drivers
import eventos

import var
from PyQt6 import QtGui, QtWidgets, QtCore


class Cliente:

    def alta_cliente(self):
        try:
            new_cliente = cliente.Cliente.recuperar_datos(self)
            print(new_cliente)
            if not drivers.Drivers.validar_datos(new_cliente):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = "Campos vacíos"
                mbox.setText(mensaje)
                icon = QIcon('./img/taxiIcon.png')
                mbox.setWindowIcon(icon)
                mbox.exec()
            else:
                if conexion.Conexion.guardarCliente(new_cliente):
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

    def validar_datos(listadeDatos):
        for i in range(len(listadeDatos) - 1):
            if listadeDatos[i].strip() == '':
                return False
        return True

    def validar_tlf(self=None):
        try:
            tlf = var.ui.txtMovil_Cliente.text()

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
                var.ui.txtMovil_Cliente.setText('')
                var.ui.txtMovil_Cliente.setFocus()

            else:
                var.ui.txtMovil_Cliente.setText(tlf)

        except Exception as error:
            print("error en validar telf: ", error)

    def validar_dni(dni):
        try:
            # dni = var.ui.txtDni_3.text()
            dni = dni.upper()
            # var.ui.txtDni_3.setText(dni)
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
                    #  var.ui.lblCheckDNI_Cliente.setStyleSheet('color:green;')
                    # var.ui.lblCheckDNI_Cliente.setText('V')
                    var.ui.lblCheckDNI_Cliente.setScaledContents(True)
                    var.ui.lblCheckDNI_Cliente.setPixmap(QtGui.QPixmap("img/OkIco.svg"))
                    return True

                else:
                    # var.ui.lblCheckDNI_Cliente.setStyleSheet('color:red;')
                    # var.ui.lblCheckDNI_Cliente.setText('X')
                    var.ui.lblCheckDNI_Cliente.show()
                    var.ui.lblCheckDNI_Cliente.setScaledContents(True)
                    var.ui.lblCheckDNI_Cliente.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                    var.ui.txtDni_3.setText("")
                    var.ui.txtDni_3.setFocus()
            else:
                #  var.ui.lblCheckDNI_Cliente.setStyleSheet('color:red;')
                # var.ui.lblCheckDNI_Cliente.setText('X')
                var.ui.lblCheckDNI_Cliente.show()
                var.ui.lblCheckDNI_Cliente.setScaledContents(True)
                var.ui.lblCheckDNI_Cliente.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                var.ui.txtDni_3.setText("")
                var.ui.txtDni_3.setFocus()
        except Exception as error:
            print("error en validar dni: ", error)

    def recuperar_datos(self=None):
        driver = [var.ui.txtDni_3.text(),var.ui.txtRazonSocial.text(), var.ui.txtDireccion_Cliente.text(),
                  var.ui.txtMovil_Cliente.text(),var.ui.cmbProvincia_Cliente.currentText(),
                  var.ui.cmbLocalidad_Cliente.currentText(), var.ui.txtDate_Cliente.text()]
        print(driver)
        return driver

    @staticmethod
    def cargartabla(registros):

        try:
            nuevoRegistros = list()
            if (var.ui.rbtAltaCliente.isChecked()):
                for registro in registros:
                    if registro[4] == '':
                        nuevoRegistros.append(registro)
            elif (var.ui.rbtBajaCliente.isChecked()):
                for registro in registros:
                    if registro[4] != '':
                        nuevoRegistros.append(registro)
            elif (var.ui.rbtTodosCliente.isChecked()):
                nuevoRegistros = registros

            if len(nuevoRegistros) == 0:
                var.ui.tabClientes.setRowCount(0)
            else:
                print(nuevoRegistros)
                index = 0
                for registro in nuevoRegistros:
                    var.ui.tabClientes.setRowCount(index + 1)
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                    var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index += 1
        except Exception as error:
            print("Error completar tabla ", error)
            
            
    def get_from_tab(self):
        try:
            # Limpiar el estilo de todas las filas
            for r in range(var.ui.tabClientes.rowCount()):
                for c in range(var.ui.tabClientes.columnCount()):
                    item = var.ui.tabClientes.item(r, c)
                    if item is not None:
                        item.setBackground(QBrush(QColor(0, 0, 0, 0)))

            # Establecer el fondo amarillo solo para la fila seleccionada
            row = var.ui.tabClientes.currentRow()
            for c in range(var.ui.tabClientes.columnCount()):
                item = var.ui.tabClientes.item(row, c)
                if item is not None:
                    item.setBackground(QBrush(QColor("#CCA963")))

            codigo = var.ui.tabClientes.item(row, 0).text()

            registro = conexion.Conexion.buscar_segun_codigo_cliente(codigo)
            cliente.Cliente.carga_cliente(registro)

        except Exception as error:
            print("Error al cargar desde la tabla", error)


    def carga_cliente(registro):
        try:
            print(registro)
            if registro == None:
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
                datos = [var.ui.lblCodDB_Cliente,var.ui.txtDni_3, var.ui.txtRazonSocial, var.ui.txtDireccion_Cliente,
                  var.ui.txtMovil_Cliente,var.ui.cmbProvincia_Cliente,
                  var.ui.cmbLocalidad_Cliente, var.ui.txtDate_Cliente]

                for i, dato in enumerate(datos):
                    if i == 5 or i == 6:
                        # Verificar si dato es un QComboBox
                        dato.setCurrentText(str(registro[i]))
                    else:
                        dato.setText(str(registro[i]))




                var.ui.lblCheckDNI.show()
                var.ui.lblCheckDNI.setScaledContents(True)
                var.ui.lblCheckDNI.setPixmap(QtGui.QPixmap("img/OkIco.svg"))

                for fila in range(var.ui.tabClientes.rowCount()):
                    if var.ui.tabClientes.item(fila, 0) == str(registro[0]):
                        
                        var.ui.tabClientes.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                        var.ui.tabClientes.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                        var.ui.tabClientes.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                        var.ui.tabClientes.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                        var.ui.tabClientes.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                        var.ui.tabClientes.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                        var.ui.tabClientes.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[5])))
                        var.ui.tabClientes.item(fila, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(fila, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.item(fila, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        var.ui.tabClientes.setItem(fila, 0).setBackground(247, 181, 0)
                        var.ui.tabClientes.setItem(fila, 1).setBackground(247, 181, 0)
                        var.ui.tabClientes.setItem(fila, 2).setBackground(247, 181, 0)
                        var.ui.tabClientes.setItem(fila, 3).setBackground(247, 181, 0)




        except Exception as error:
            print("Error al cargar datos: ", error)

    def get_from_dni(self):
        try:
            obteivo = None
            dni = var.ui.txtDni_3.text()
            cliente.Cliente.carga_cliente(conexion.Conexion.buscar_segun_dni_cliente(dni))
            registro = conexion.Conexion.buscar_segun_dni_cliente(dni)
            if registro[7] == '':
                var.ui.rbtAlta.setChecked(True)
            else:
                var.ui.rbtBaja.setChecked(True)
            conexion.Conexion.mostrarclientes()

            for row in range(var.ui.tabClientes.rowCount()):
                item = var.ui.tabClientes.item(row, 0)
                if item and item.text() == str(registro[0]):
                    brush = QColor(247, 181, 0)
                    for col in range(var.ui.tabClientes.columnCount()):
                        current_item = var.ui.tabClientes.item(row, col)
                        if current_item is not None:
                            current_item.setBackground(brush)
                            obteivo = current_item
            var.ui.tabClientes.scrollToItem(obteivo)
        except Exception as error:
            print("Error al cargar segun el DNI", error)
    
    
    
    
    
    
    
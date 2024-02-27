import locale
import re

from PyQt6.QtGui import QColor, QBrush, QIcon

import Ventanas
import cliente
import conexion
import drivers
import eventos
import Ventanas
from Facturas import facturacion_repository, facturacion

import var
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox


class Cliente:

    def baja_cliente(self):
        '''
        Metodo para borrar un cliente en la base de datos.En caso de que no esten todos lo campos completos del cliente a borrar
        se mostrara una ventana de aviso, indicando que faltan campos por completar.
        :return:
        :rtype:
        '''
        try:

            cliente_baja = cliente.Cliente.recuperar_datos()
            if Cliente.validar_datos(cliente_baja):
                conexion.Conexion.borrarCliente(cliente_baja[0])
                conexion.Conexion.mostrarclientes()
            else:
                Ventanas.Ventanas.mensaje_warning("Campos Vacios")
        except Exception as error:
            print("Error en el metodo baja_cliente", error)

    def alta_cliente(self):
        '''
        Metodo con el que se dara de alta a un cliente.El metodo mostrara una ventana de aviso en caso de que no se completaran los campos necesarios para dar de alta a un cliente.

        :return:
        :rtype:
        '''
        try:
            new_cliente = cliente.Cliente.recuperar_datos(self)

            if not drivers.Drivers.validar_datos(new_cliente):
                Ventanas.Ventanas.mensaje_warning("Campos vacios")
            else:
                if conexion.Conexion.guardarCliente(new_cliente):
                    Ventanas.Ventanas.ventana_info('Cliente dado de alta')
                    conexion.Conexion.mostrarclientes()

                else:
                    Ventanas.Ventanas.mensaje_warning("El DNI ya se encuentra en la base de datos")

            conexion.Conexion.mostrardrivers()
            eventos.Eventos.limpiar()

        except Exception as error:
            print("error alta cliente", error)

    def validar_datos(listadeDatos):
        '''
        Metodo para validar que una lista no contenga campos vacios.
        :param: Lista
        :return: Devuelve True en caso de que ninguna de las posiciones de la lista este vacia.
        :rtype: Boolean
        '''
        for i in range(len(listadeDatos) - 1):
            if listadeDatos[i].strip() == '':
                return False
        return True

    def validar_tlf(self=None):
        '''
        Validacion de un numero de telefono segun un patron.El nuemero tiene que estar compuesto de 9 numeros.
        :return:
        :rtype:
        '''
        try:
            tlf = var.ui.txtMovil_Cliente.text()

            # str(tlf).format('{9d}')
            # if len(tlf) != 9 and tlf != type(int)
            regex = r'^\d{9}$'

            if not re.match(regex, tlf):
                Ventanas.Ventanas.mensaje_warning('Telefono icorrecto introducir nueve digitos')
                var.ui.txtMovil_Cliente.setText('')
                var.ui.txtMovil_Cliente.setFocus()

            else:
                var.ui.txtMovil_Cliente.setText(tlf)

        except Exception as error:
            print("error en validar telf: ", error)

    def validar_dni(dni):
        '''
            Validación de un **DNI** según el algoritmo de validación español.
            En caso de ser valido pondra un imagen y si es falso pondra otra.Este medoto no dejara mover el cursor de esta caja de texto mientras el **DNI** introducido no sea el correcto.
            :param dni: String que tiene que ser al menos de 9 caracteres.
            :return: True si el DNI es válido, False en caso contrario.
            :rtype: bool
            '''
        try:

            dni = dni.upper()

            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {"X": "0", "Y": "1", "Z": "2"}
            numeros = "1234567890"

            if len(dni) == 9:  # comprueba que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni

                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:

                    var.ui.lblCheckDNI_Cliente.setScaledContents(True)
                    var.ui.lblCheckDNI_Cliente.setPixmap(QtGui.QPixmap("img/OkIco.svg"))
                    return True

                else:

                    var.ui.lblCheckDNI_Cliente.show()
                    var.ui.lblCheckDNI_Cliente.setScaledContents(True)
                    var.ui.lblCheckDNI_Cliente.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                    var.ui.txtDni_3.setText("")
                    var.ui.txtDni_3.setFocus()
            else:
                var.ui.lblCheckDNI_Cliente.show()
                var.ui.lblCheckDNI_Cliente.setScaledContents(True)
                var.ui.lblCheckDNI_Cliente.setPixmap(QtGui.QPixmap("img/CancelIco.ico"))
                var.ui.txtDni_3.setText("")
                var.ui.txtDni_3.setFocus()
        except Exception as error:
            print("error en validar dni: ", error)

    def recuperar_datos(self=None):
        '''
        Este metodo recoge todos los datos que hay en las cajas de texto en en panel del cliente.
        :return: Devuelve una lista con todos los datos del cliente que estan en las cajas de texto.
        :rtype: List
        '''

        driver = [var.ui.txtDni_3.text(), var.ui.txtRazonSocial.text(), var.ui.txtDireccion_Cliente.text(),
                  var.ui.txtMovil_Cliente.text(), var.ui.cmbProvincia_Cliente.currentText(),
                  var.ui.cmbLocalidad_Cliente.currentText(), var.ui.txtDate_Cliente.text()]

        return driver

    @staticmethod
    def cargartabla(registros):
        '''
        Metodo para cargar la tabla de clientes con todos los clientes que existen en la base de datos.

        :param registros:
        :type registros:
        :return:
        :rtype:
        '''

        try:
            nuevoRegistros = list()
            if (var.ui.rbtAltaCliente.isChecked()):
                var.ui.frame_baja.hide()
                for registro in registros:
                    if registro[4] == '':
                        nuevoRegistros.append(registro)
            elif (var.ui.rbtBajaCliente.isChecked()):
                var.ui.frame_baja.show()
                for registro in registros:
                    if registro[4] != '':
                        nuevoRegistros.append(registro)
            elif (var.ui.rbtTodosCliente.isChecked()):
                var.ui.frame_baja.hide()

                nuevoRegistros = registros

            if len(nuevoRegistros) == 0:
                var.ui.tabClientes.setRowCount(0)
            else:

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
        '''
        Metodo para recoger los datos de una fila seleccionada y pasarlos al panel del cliente, tambien colorea la fila que se ha seleccionao.
        '''
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
                    item.setBackground(QBrush(QColor(243, 220, 173)))

            codigo = var.ui.tabClientes.item(row, 0).text()

            registro = conexion.Conexion.buscar_segun_codigo_cliente(codigo)
            cliente.Cliente.carga_cliente(registro)

        except Exception as error:
            print("Error al cargar desde la tabla", error)

    def carga_cliente(registro):
        '''
        Metodo para cargar un cliente en  que se encuentra en la base de datos.En caso de que ese cliente no exita en la base de datos, se muestra una ventana indicando al usuario que ese cliente no existe en la base de datos.
        :param:Recibe por parametro un un registro que contiene los datos del cliente.
        '''
        try:

            if registro == None:
                Ventanas.Ventanas.mensaje_warning('El dni no se encuentra en la base de datos')
            else:
                ##var.ui.txt_cif_cliente.setText(str(registro[1]))
                datos = [var.ui.lblCodDB_Cliente, var.ui.txtDni_3, var.ui.txtRazonSocial, var.ui.txtDireccion_Cliente,
                         var.ui.txtMovil_Cliente, var.ui.cmbProvincia_Cliente,
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
        '''
        Metodo que recoge los datos de un Text Box y verifica que el dni existe y es valido.Si existe el dni se desplaza hasta la fila en la que se encuentra ese DNI.
        '''
        try:
            objetivo = None
            if var.ui.txtDni_3.text() != '':
                dni = var.ui.txtDni_3.text()
            elif var.ui.txt_cif_cliente != '':
                dni = var.ui.txt_cif_cliente.text()

            cliente.Cliente.carga_cliente(conexion.Conexion.buscar_segun_dni_cliente(dni))
            if var.ui.txt_cif_cliente.text() != '':
                facturacion.Facturacion.cargartabla(
                    facturacion_repository.Facturacion_Repository.recuperar_facturas_segun_dni(dni))

            registro = conexion.Conexion.buscar_segun_dni_cliente(dni)
            if registro[7] == '':
                var.ui.rbtAltaCliente.setChecked(True)
            else:
                var.ui.rbtBajaCliente.setChecked(True)
            conexion.Conexion.mostrarclientes()

            for row in range(var.ui.tabClientes.rowCount()):
                item = var.ui.tabClientes.item(row, 0)
                if item and item.text() == str(registro[0]):
                    brush = QColor(243, 220, 173)
                    for col in range(var.ui.tabClientes.columnCount()):
                        current_item = var.ui.tabClientes.item(row, col)
                        if current_item is not None:
                            current_item.setBackground(brush)
                            objetivo = current_item
            if objetivo != None:
                var.ui.tabClientes.scrollToItem(objetivo)
        except Exception as error:
            print("Error al cargar segun el DNI", error)

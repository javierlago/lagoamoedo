from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QHeaderView, QMessageBox
from PyQt6.uic.properties import QtWidgets, QtCore, QtGui

import Ventanas
import conexion
import drivers
from Facturas import facturacion_repository

import var
from PyQt6 import QtWidgets, QtSql, QtCore
from PyQt6 import *


class Facturacion:

    def crear_registro(self):
        """
         Método para recoger los datos del viaje.

         :param self: Referencia al objeto actual.
         :type self: object

         :return: Una lista que contiene la provincia y localidad de origen, y la provincia y localidad de destino del viaje.
         :rtype: list

         Descripción:
         Este método recoge los datos del viaje seleccionados por el usuario y devuelve una lista con estos datos.
         """
        try:

            registroFactura = [var.ui.txt_cif_cliente.text(), var.ui.txt_fecha_factura.text(),
                               var.ui.cmb_listado_conductores.currentText().split("  ||  ")[0]]
            return registroFactura
        except Exception as error:
            print("Errore en la recogida de datos de la factura", error)

    def recoger_datos_viaje(self):
        """
           Método para recoger los datos del viaje seleccionados por el usuario.

           :param self: Referencia al objeto actual.
           :type self: object

           :return: Una lista que contiene la provincia de origen, provincia de destino, localidad de origen y localidad de destino del viaje.
           :rtype: list

           Descripción:
           Este método recoge los datos del viaje seleccionados por el usuario a través de los comboboxes correspondientes y los devuelve en una lista.
           """
        try:
            datos_viaje = [var.ui.cmb_provincia_origen.currentText(), var.ui.cmb_provincia_destino.currentText(),
                           var.ui.cmb_localidad_origen.currentText(), var.ui.cmb_localidad_destino.currentText()]
            return datos_viaje
        except Exception as error:
            print("Error en la recuperacion de datos del vieaje", error)

    def cargartabla(registros):
        """
        Método para cargar registros en una tabla.

        :param registros: Lista de registros a cargar en la tabla.
        :type registros: list

        Descripción:
        Este método carga los registros proporcionados en una tabla de la interfaz de usuario. Itera sobre los registros y los inserta en la tabla fila por fila.
        """

        try:

            if registros == None:
                var.ui.tab_facturas.setRowCount(0)
            else:
                index = 0

                for registro in registros:
                    var.ui.tab_facturas.setRowCount(index + 1)
                    var.ui.tab_facturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    var.ui.tab_facturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                    btn_borrar_linea = QtWidgets.QPushButton()
                    btn_borrar_linea.setFixedSize(30, 28)
                    btn_borrar_linea.setIcon(QtGui.QIcon('./img/papelera.png'))
                    btn_borrar_linea.clicked.connect(Facturacion.eliminar_linea_factura)
                    var.ui.tab_facturas.setCellWidget(index, 2, btn_borrar_linea)
                    var.ui.tab_facturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tab_facturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tab_facturas.horizontalHeader().setSectionResizeMode(2,
                                                                                QHeaderView.ResizeMode.ResizeToContents)

                    index += 1
        except Exception as error:
            print("Error completar tabla ", error)

    def mostrar_datos_factura(self):
        """
        Método para mostrar los datos de una factura en los campos correspondientes de la interfaz.

        Descripción:
        Este método oculta el botón de modificar viaje y limpia los campos de provincia, localidad y kilómetros.
        Además, limpia el estilo de todas las filas de la tabla de facturas y establece un fondo amarillo para la fila seleccionada.
        Posteriormente, recupera el código del conductor y la fecha de la factura seleccionada en la tabla de facturas,
        y muestra estos datos junto con el número de factura y el CIF del cliente en los campos de la interfaz.
        """

        try:
            var.ui.btn_modificar_viaje.setVisible(False)
            var.ui.cmb_provincia_origen.setCurrentText('')
            var.ui.cmb_provincia_destino.setCurrentText('')
            var.ui.cmb_localidad_origen.setCurrentText('')
            var.ui.cmb_localidad_destino.setCurrentText('')
            var.ui.txt_kilometros.setText("")
            fecha = ""
            codigo = ""
            # Limpiar el estilo de todas las filas
            for r in range(var.ui.tab_facturas.rowCount()):
                for c in range(var.ui.tab_facturas.columnCount()):
                    item = var.ui.tab_facturas.item(r, c)
                    if item is not None:
                        item.setBackground(QBrush(QColor(0, 0, 0, 0)))

            # Establecer el fondo amarillo solo para la fila seleccionada
            row = var.ui.tab_facturas.currentRow()
            print(row)
            print(var.ui.tab_facturas.item(row, 0).text())
            query = QtSql.QSqlQuery()
            query.prepare("select idConductor,fechaFactura from facturas where numFactura = :numFactura")
            query.bindValue(":numFactura", var.ui.tab_facturas.item(row, 0).text())
            if query.exec():
                if query.next():
                    codigo = query.value(0)
                    fecha = query.value(1)

            for c in range(var.ui.tab_facturas.columnCount()):
                item = var.ui.tab_facturas.item(row, c)
                if item is not None:
                    item.setBackground(QBrush(QColor(247, 181, 0)))
            registro = conexion.Conexion.buscar_segun_codigo(codigo)
            var.ui.txt_numero_factura.setText(var.ui.tab_facturas.item(row, 0).text())
            var.ui.txt_cif_cliente.setText(var.ui.tab_facturas.item(row, 1).text())
            var.ui.txt_fecha_factura.setText(fecha)
            var.ui.cmb_listado_conductores.setCurrentText(registro[0] + "  ||  " + registro[3])


        except Exception as error:
            print("Error al cargar desde la tabla", error)

    def calcular_tarifa(self=None):
        """
        Método para calcular la tarifa según el tipo de viaje seleccionado.

        :param self: Referencia al objeto actual.
        :type self: object

        :return: La tarifa calculada según el tipo de viaje.
        :rtype: float

        Descripción:
        Este método calcula la tarifa del viaje según el tipo de viaje seleccionado en los comboboxes de provincia y localidad de origen y destino.
        Si la provincia de origen es diferente a la provincia de destino, se establece la tarifa nacional y se devuelve 0.8.
        Si la localidad de origen es diferente a la localidad de destino pero la provincia es la misma, se establece la tarifa provincial y se devuelve 0.4.
        Si la localidad de origen y destino son iguales, se establece la tarifa local y se devuelve 0.2.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:
            array_destinos = [var.ui.cmb_provincia_origen.currentText(), var.ui.cmb_provincia_destino.currentText(),
                              var.ui.cmb_localidad_origen.currentText(), var.ui.cmb_localidad_destino.currentText()]

            if array_destinos[0] != array_destinos[1]:
                var.ui.rbt_tarifa_nacional.setChecked(True)
                return 0.8
            elif array_destinos[2] != array_destinos[3]:
                var.ui.rbt_tarifa_provincia.setChecked(True)
                return 0.4
            else:
                var.ui.rbt_tarifa_local.setChecked(True)
                return 0.2


        except Exception as error:
            print("Error en el metodo calcular tarifa", error)

    def insertar_datos_viaje(last_insert):
        try:
            print(str(last_insert))
            datos_linea_de_factura: list = [var.ui.txt_numero_factura.text(), var.ui.cmb_localidad_origen.currentText(),
                                            var.ui.cmb_localidad_destino.currentText(), var.ui.txt_kilometros.text(),
                                            str(Facturacion.calcular_tarifa())]
            if datos_linea_de_factura[0] == "":
                datos_linea_de_factura[0] = str(last_insert)
                print(drivers.Drivers.validar_datos(datos_linea_de_factura))
                print(int(last_insert))
            if drivers.Drivers.validar_datos(datos_linea_de_factura):
                facturacion_repository.Facturacion_Repository.insert_line_de_viaje(datos_linea_de_factura)
                Facturacion.rellenar_tabla_lineas_viaje(self=None)
            else:
                Ventanas.Ventanas.mensaje_warning("Debes rellenar todos los campos")
        except Exception as error:
            print("Error a la hora de recuperar los datos", error)

    def rellenar_tabla_lineas_viaje(self):
        """
        Método para insertar datos de un viaje en la base de datos.

        :param last_insert: Último identificador insertado en la base de datos.
        :type last_insert: int

        :return: None

        Descripción:
        Este método inserta los datos de un viaje en la base de datos. Los datos incluyen el número de factura, localidad de origen, localidad de destino, kilómetros y tarifa.
        Si el número de factura está vacío, se utiliza el último identificador insertado. Luego, se valida la información del viaje.
        Si los datos son válidos, se insertan en la base de datos y se actualiza la tabla de líneas de viaje en la interfaz.
        En caso contrario, se muestra un mensaje de advertencia indicando que se deben completar todos los campos.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:
            lineas_de_viaje = facturacion_repository.Facturacion_Repository.recupera_lineas_de_viaje(
                var.ui.txt_numero_factura.text())
            for i in range(var.ui.tab_lineas_de_viaje.columnCount()):
                if i == 1 or i == 2 or i == 3 or i == 6:
                    var.ui.tab_lineas_de_viaje.horizontalHeader().setSectionResizeMode(i,
                                                                                       QHeaderView.ResizeMode.ResizeToContents)
                else:
                    var.ui.tab_lineas_de_viaje.horizontalHeader().setSectionResizeMode(i,
                                                                                       QHeaderView.ResizeMode.Stretch)
            var.ui.tab_lineas_de_viaje.setRowCount(len(lineas_de_viaje))
            for fila in range(len(lineas_de_viaje)):

                for columna in range(var.ui.tab_lineas_de_viaje.columnCount()):
                    if columna == 5:
                        var.ui.tab_lineas_de_viaje.setItem(fila, columna, QtWidgets.QTableWidgetItem(
                            str(round(lineas_de_viaje[fila][3] * lineas_de_viaje[fila][4], 2))))
                        var.ui.tab_lineas_de_viaje.item(fila, columna).setTextAlignment(
                            QtCore.Qt.AlignmentFlag.AlignCenter)
                    elif columna == 6:
                        btn_borrar_linea_viaje = QtWidgets.QPushButton()
                        btn_borrar_linea_viaje.setFixedSize(30, 28)
                        btn_borrar_linea_viaje.setIcon(QtGui.QIcon('./img/papelera.png'))
                        var.ui.tab_lineas_de_viaje.setCellWidget(fila, columna, btn_borrar_linea_viaje)
                        btn_borrar_linea_viaje.clicked.connect(Facturacion.eliminar_linea_de_viaje)
                    else:
                        var.ui.tab_lineas_de_viaje.setItem(fila, columna, QtWidgets.QTableWidgetItem(
                            str(lineas_de_viaje[fila][columna])))
                        var.ui.tab_lineas_de_viaje.item(fila, columna).setTextAlignment(
                            QtCore.Qt.AlignmentFlag.AlignCenter)

            var.ui.txt_subtotal.setText(
                str(round(Facturacion.calculo_factura_de_viaje(var.ui.tab_lineas_de_viaje), 2)) + " €")
            iva = (Facturacion.calculo_factura_de_viaje(var.ui.tab_lineas_de_viaje) * 0.21)
            var.ui.txt_iva.setText(str(round(iva, 2)) + " €")
            total = (iva + Facturacion.calculo_factura_de_viaje(var.ui.tab_lineas_de_viaje))
            var.ui.txt_total.setText(str(round(total, 2)) + " €")
            print(total)


        except Exception as error:
            print("Error completar tabla ", error)

    def eliminar_linea_de_viaje(self):
        """
        Método para eliminar una línea de viaje.

        :param self: Referencia al objeto actual.
        :type self: object

        :return: None

        Descripción:
        Este método muestra un mensaje de advertencia preguntando al usuario si desea eliminar la línea de viaje seleccionada.
        Si el usuario confirma la eliminación, se borra la línea de viaje de la base de datos y se elimina de la tabla en la interfaz.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:

            mensaje = QMessageBox()
            mensaje.setText("¿Deseas eliminar este viaje?")
            mensaje.setWindowTitle("Lineas de viaje")
            mensaje.setIcon(QMessageBox.Icon.Warning)
            mensaje.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            resultado = mensaje.exec()
            if resultado == QMessageBox.StandardButton.Ok:
                facturacion_repository.Facturacion_Repository.borra_linea_de_viaje(
                    var.ui.tab_lineas_de_viaje.item(var.ui.tab_lineas_de_viaje.currentRow(), 0).text())
                var.ui.tab_lineas_de_viaje.removeRow(var.ui.tab_lineas_de_viaje.currentRow())

        except Exception as error:
            print("Error en el metodo de borrado de linea de viaje", error)

    def calculo_factura_de_viaje(tabla):
        """
        Método para calcular el total de la factura de un viaje.

        :param tabla: Tabla que contiene los datos de los viajes.
        :type tabla: QTableWidget

        :return: El total de la factura del viaje.
        :rtype: float

        Descripción:
        Este método calcula el total de la factura sumando los importes de cada línea de viaje en la tabla proporcionada.
        Itera sobre todas las filas de la tabla, obtiene el importe de cada línea y lo suma al presupuesto total.
        Finalmente, devuelve el presupuesto total de la factura.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:
            presupuesto = 0
            for a in range(tabla.rowCount()):
                print(tabla.item(a, 5).text())
                presupuesto += float(tabla.item(a, 5).text())
            return presupuesto
        except Exception as error:
            print("Error en el metodo de suma del total", error)

    def seleccionar_linea_de_viaje(self):
        """
        Método para seleccionar una línea de viaje.

        :param self: Referencia al objeto actual.
        :type self: object

        :return: None

        Descripción:
        Este método selecciona una línea de viaje en la tabla de líneas de viaje de la interfaz.
        Primero recoge los datos de la fila seleccionada, luego muestra el botón de modificar viaje y limpia el fondo de todas las filas de la tabla.
        Después, resalta la fila seleccionada estableciendo un fondo amarillo.
        A continuación, obtiene las provincias correspondientes a las localidades de origen y destino de la línea de viaje seleccionada y las establece en los comboboxes de provincia de origen y destino.
        Finalmente, establece las localidades de origen y destino y los kilómetros en los campos correspondientes de la interfaz.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:

            datos_fila_seleccionada = Facturacion.recoger_datos_linea_viaje(self)
            var.ui.btn_modificar_viaje.setVisible(True)
            for r in range(var.ui.tab_lineas_de_viaje.rowCount()):
                for c in range(var.ui.tab_lineas_de_viaje.columnCount()):
                    item = var.ui.tab_lineas_de_viaje.item(r, c)
                    if item is not None:
                        item.setBackground(QBrush(QColor(0, 0, 0, 0)))
            row_number = var.ui.tab_lineas_de_viaje.currentRow()
            for colunm_number in range(var.ui.tab_lineas_de_viaje.columnCount()):
                item = var.ui.tab_lineas_de_viaje.item(row_number, colunm_number)
                if item is not None:
                    item.setBackground(QBrush(QColor(247, 181, 0)))
            provincia_origen = conexion.Conexion.provincia_segun_municipio(datos_fila_seleccionada[1])
            provincia_destino = conexion.Conexion.provincia_segun_municipio(datos_fila_seleccionada[2])
            var.ui.cmb_provincia_origen.setCurrentText(provincia_origen)
            var.ui.cmb_provincia_destino.setCurrentText(provincia_destino)
            var.ui.cmb_localidad_origen.setCurrentText(datos_fila_seleccionada[1])
            var.ui.cmb_localidad_destino.setCurrentText(datos_fila_seleccionada[2])
            var.ui.txt_kilometros.setText(datos_fila_seleccionada[3])
        except Exception as error:
            print("Error en el metodo de seleccionar lineas de viaje", error)

    def recoger_datos_linea_viaje(self):
        """
        Método para recoger los datos de una línea de viaje seleccionada en la tabla.

        :param self: Referencia al objeto actual.
        :type self: object

        :return: Una lista que contiene los datos de la línea de viaje seleccionada.
        :rtype: list

        Descripción:
        Este método recoge los datos de una línea de viaje seleccionada en la tabla de líneas de viaje de la interfaz.
        Itera sobre los elementos de la fila seleccionada en la tabla y los agrega a una lista.
        Además, establece un fondo amarillo para resaltar la fila seleccionada en la tabla.
        Finalmente, devuelve la lista con los datos de la fila seleccionada.
        """

        row_number = var.ui.tab_lineas_de_viaje.currentRow()
        datos_fila_seleccionada: list = []
        for colunm_number in range(var.ui.tab_lineas_de_viaje.columnCount()):
            item = var.ui.tab_lineas_de_viaje.item(row_number, colunm_number)
            if item is not None:
                item.setBackground(QBrush(QColor(247, 181, 0)))
                datos_fila_seleccionada.append(item.text())
        return datos_fila_seleccionada

    def limpiar_panel_viajes(self):
        """
        Método para limpiar los campos del panel de viajes.

        :param self: Referencia al objeto actual.
        :type self: object

        :return: None

        Descripción:
        Este método limpia los campos del panel de viajes en la interfaz.
        Establece el texto vacío en los comboboxes de provincia y localidad de origen y destino, así como en el campo de kilómetros.
        En caso de error, imprime un mensaje de error en la consola.
        """

        try:
            var.ui.cmb_provincia_origen.setCurrentText('')
            var.ui.cmb_provincia_destino.setCurrentText('')
            var.ui.cmb_localidad_origen.setCurrentText('')
            var.ui.cmb_localidad_destino.setCurrentText('')
            var.ui.txt_kilometros.setText('')

        except Exception as error:
            print("Error en el metodo limpiar panel viajes")

    @staticmethod
    def limpiar_panel_facturas(self):
        try:
            var.ui.txt_cif_cliente.setText("")
            var.ui.txt_fecha_factura.setText("")
            var.ui.txt_numero_factura.setText("")
            var.ui.cmb_listado_conductores.setCurrentText('')
        except Exception as error:
            print("Error al limpiar el panel de facturas", error)

    @staticmethod
    def limpiar_panel_solo_viajes(self):
        try:
            var.ui.txt_kilometros.setText("")
            var.ui.cmb_provincia_origen.setCurrentText('')
            var.ui.cmb_provincia_destino.setCurrentText('')
            var.ui.cmb_localidad_origen.setCurrentText('')
            var.ui.cmb_localidad_destino.setCurrentText('')
        except Exception as error:
            print("Error al limpiar el panel de facturas", error)

    def eliminar_linea_factura(self):
        try:
            mensaje = QMessageBox()
            mensaje.setText("¿Deseas eliminar esta factura?")
            mensaje.setWindowTitle("Facturas")
            mensaje.setIcon(QMessageBox.Icon.Warning)
            mensaje.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            resultado = mensaje.exec()
            print(var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
            if resultado == QMessageBox.StandardButton.Ok:
                facturacion_repository.Facturacion_Repository.borrar_factura(
                    var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
                var.ui.tab_facturas.removeRow(var.ui.tab_facturas.currentRow())
        except Exception as error:
            print("Error en el metodo eliminar_linea_factura",error)

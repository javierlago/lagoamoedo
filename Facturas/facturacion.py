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
        try:

            registroFactura = [var.ui.txt_cif_cliente.text(), var.ui.txt_fecha_factura.text(),
                               var.ui.cmb_listado_conductores.currentText().split("  ||  ")[0]]
            return registroFactura
        except Exception as error:
            print("Errore en la recogida de datos de la factura", error)

    def recoger_datos_viaje(self):
        try:
            datos_viaje = [var.ui.cmb_provincia_origen.currentText(), var.ui.cmb_provincia_destino.currentText(),
                           var.ui.cmb_localidad_origen.currentText(), var.ui.cmb_localidad_destino.currentText()]
            return datos_viaje
        except Exception as error:
            print("Error en la recuperacion de datos del vieaje", error)

    def cargartabla(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tab_facturas.setRowCount(index + 1)
                var.ui.tab_facturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tab_facturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tab_facturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tab_facturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                index += 1
        except Exception as error:
            print("Error completar tabla ", error)

    def mostrar_datos_factura(self):
        try:
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
        try:
            print("Calculando tarifa")
            print(var.ui.cmb_provincia_origen.currentText())
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
        try:

            lineas_de_viaje = facturacion_repository.Facturacion_Repository.recupera_lineas_de_viaje(
                var.ui.txt_numero_factura.text())
            for i in range(var.ui.tab_lineas_de_viaje.columnCount()):
                if  i == 1 or i == 2 or i == 3 or i == 6:
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
                            str(lineas_de_viaje[fila][3] * lineas_de_viaje[fila][4])))
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

            var.ui.txt_subtotal.setText(str(Facturacion.calculo_factura_de_viaje(var.ui.tab_lineas_de_viaje)))
            iva = (Facturacion.calculo_factura_de_viaje(var.ui.tab_lineas_de_viaje)*0.21)
            var.ui.txt_iva.setText(str(round(iva,2)))
            total = (iva + Facturacion.calculo_factura_de_viaje(var.ui.tab_lineas_de_viaje))
            var.ui.txt_total.setText(str(round(total, 2)))
            print(total)


        except Exception as error:
            print("Error completar tabla ", error)

    def eliminar_linea_de_viaje(self):
        try:
            mensaje = QMessageBox()
            mensaje.setText("¿Deseas eliminar este viaje?")
            mensaje.setWindowTitle("Lineas de viaje")
            mensaje.setIcon(QMessageBox.Icon.Warning)
            mensaje.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            resultado = mensaje.exec()
            if resultado == QMessageBox.StandardButton.Ok:
                print(var.ui.tab_lineas_de_viaje.item(var.ui.tab_lineas_de_viaje.currentRow(), 0).text())
                facturacion_repository.Facturacion_Repository.borra_linea_de_viaje(
                    var.ui.tab_lineas_de_viaje.item(var.ui.tab_lineas_de_viaje.currentRow(), 0).text())
                var.ui.tab_lineas_de_viaje.removeRow(var.ui.tab_lineas_de_viaje.currentRow())

        except Exception as error:
            print("Error en el metodo de borrado de linea de viaje", error)
    def calculo_factura_de_viaje(tabla):
        try:
            presupuesto = 0
            for a in range(tabla.rowCount()):
                print(tabla.item(a,5).text())
                presupuesto += float(tabla.item(a,5).text())
            return presupuesto
        except Exception as error:
            print("Error en el metodo de suma del total",error)






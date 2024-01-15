from PyQt6.uic.properties import QtWidgets, QtCore
from PyQt6 import QtGui, QtWidgets, QtCore
import conexion
import var


class facturacion:

    def crear_registro(self=None):
        try:

            registroFactura = [var.ui.txt_cif_cliente.text(),var.ui.txt_fecha_factura.text(), var.ui.cmb_listado_conductores.currentText().split("  ||  ")[0]]
            return registroFactura
        except Exception as error:
            print("Errore en la recogida de datos de la factura",error)




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

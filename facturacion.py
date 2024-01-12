import conexion
import var


class facturacion:

    def crear_registro(self=None):
        try:

            registroFactura = [var.ui.txt_cif_cliente.text(),var.ui.txt_fecha_factura.text(), var.ui.cmb_listado_conductores.currentText().split("  ||  ")[0]]
            return registroFactura
        except Exception as error:
            print("Errore en la recogida de datos de la factura",error)


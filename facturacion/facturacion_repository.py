from PyQt6 import QtSql

import Ventanas
import conexion
import var
import facturacion
class Facturacion_Repository:

    def insert_line_de_viaje(registro):

        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into viajes(idFactura, origen, destino, kms, tarifa) VALUES (:idFactura, :origen, :destino, :kms, :tarifa)')
            query.bindValue(":idFactura", int(registro[0]))
            query.bindValue(":origen", registro[1])
            query.bindValue(":destino", registro[2])
            query.bindValue(":kms", int(registro[3]))
            query.bindValue(":tarifa", registro[4])
            if query.exec():
                print("Se han introducido los datos")
        except Exception as erro:
            print(query.lastError().text(), erro, "Error en el insert de viajes")



    def insert_factura(self):
        try:
            registro = facturacion.Facturacion.crear_registro()
            for i in registro:
                if i == "":
                    Ventanas.Ventanas.mensaje_warning("Campos Vacios")
                    return

            if conexion.Conexion.dni_existe(registro[0]) is False:
                Ventanas.Ventanas.mensaje_warning("Cliente no se encuentra en la base de datos")
                return
            if conexion.Conexion.dni_existe_no_esta_baja(registro[0]) is False:
                Ventanas.Ventanas.mensaje_warning("El cliente del que deseas facturar esta dado de baja")
                return
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into facturas (dniCliente,fechaFactura, idConductor) VALUES (:dniCliente, :fechaFactura, :idConductor)')
            query.bindValue(':dniCliente', registro[0])
            query.bindValue(':fechaFactura', registro[1])
            query.bindValue(':idConductor', registro[2])
            query.exec()
            Ventanas.Ventanas.ventana_info("Se ha creado una factura")
            conexion.Conexion.cargar_facturas()
        except Exception as error:
            Ventanas.Ventanas.mensaje_warning("No se ha insertado nada en la tabla")
            print("Error en la insercion en la tabla de facturas", error)
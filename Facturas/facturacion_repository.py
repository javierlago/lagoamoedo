from typing import List, Any

from PyQt6 import QtSql

import Ventanas
import conexion
import drivers
import var

from Facturas import facturacion


class Facturacion_Repository:

    def insert_line_de_viaje(registro):

        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into viajes(idFactura, origen, destino, kms, tarifa) VALUES (:idFactura, :origen, :destino, :kms, :tarifa)')
            query.bindValue(":idFactura", int(registro[0]))
            query.bindValue(":origen", registro[1])
            query.bindValue(":destino", registro[2])
            query.bindValue(":kms", int(registro[3]))
            query.bindValue(":tarifa", float(registro[4]))
            if query.exec():
                print("Se han introducido los datos")
        except Exception as erro:
            Ventanas.Ventanas.mensaje_warning("Debes seleccionar una factuta")
            print(erro, "Error en el insert de viajes")



    def insert_factura(self):
        try:
            if not drivers.Drivers.validar_datos(facturacion.Facturacion.crear_registro(self)):
                    Ventanas.Ventanas.mensaje_warning("Campos Vacios")
                    return
            if not drivers.Drivers.validar_datos(facturacion.Facturacion.recoger_datos_viaje(self)):
                    Ventanas.Ventanas.mensaje_warning("Debes añadir al menos un viaje para crear una factura")
                    return

            registro = facturacion.Facturacion.crear_registro(self)
            if Facturacion_Repository.comprobarr_factura_existe(var.ui.txt_numero_factura.text()):
                Ventanas.Ventanas.mensaje_warning("Fatura ya existe")
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
            print(str(query.lastInsertId()))
            facturacion.Facturacion.insertar_datos_viaje(query.lastInsertId())

            Ventanas.Ventanas.ventana_info("Se ha creado una factura")
            conexion.Conexion.cargar_facturas()
        except Exception as error:
            Ventanas.Ventanas.mensaje_warning("No se ha insertado nada en la tabla")
            print("Error en la insercion en la tabla de facturas", error)


    def recupera_lineas_de_viaje(idFactura):
        try:
            print(idFactura)
            lineas_de_viaje :list = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from viajes where idFactura = :idFactura')
            query.bindValue(':idFactura',idFactura)
            if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        row.pop(1)
                        lineas_de_viaje.append(row)
            return lineas_de_viaje

        except Exception as error:
            print("Error en la el metodo recuperar todas las lineas de viaje de una factura" , error, query.lastError().text())

    def borra_linea_de_viaje(id_viaje):
        try:
            print(id_viaje)
            query_borrar_linea_de_viaje = QtSql.QSqlQuery()
            query_borrar_linea_de_viaje.prepare('delete from viajes where idViaje = :idViaje')
            query_borrar_linea_de_viaje.bindValue(':idViaje', id_viaje)
            query_borrar_linea_de_viaje.exec()
            if query_borrar_linea_de_viaje.exec():
                print("Se ha eliminado el viaje")
        except Exception as erro:
            print("Error en el metodo de borrar una linea de viaje",erro)


    def comprobarr_factura_existe(id_Factura):
        try:
            query_verificar_factura_existe = QtSql.QSqlQuery()
            query_verificar_factura_existe.prepare('select * from facturas where numFactura = :nunFactura')
            query_verificar_factura_existe.bindValue(':nunFactura',id_Factura)
            if query_verificar_factura_existe.exec() and query_verificar_factura_existe.next():
                return True

        except Exception as error:
            print("Error al validar la existencia de una factura")


    def recuperar_datos_cliente_factura(self=None):
        try:
            print(var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 1).text())
            datos_factura = []
            query_datos_factura = QtSql.QSqlQuery()
            query_datos_factura.prepare('select * from facturas where numFactura = :numFactura')
            query_datos_factura.bindValue(':numFactura', var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 0).text())
            if query_datos_factura.exec():
                while query_datos_factura.next():
                    row = [query_datos_factura.value(i) for i in range(query_datos_factura.record().count())]
                    datos_factura.append(row)
            print(datos_factura)
            datos_cliente = conexion.Conexion.buscar_segun_dni_cliente(var.ui.tab_facturas.item(var.ui.tab_facturas.currentRow(), 1).text())
            print(datos_cliente)
            datos_cliente_factura = [datos_factura[0][0],datos_factura[0][2],datos_cliente[2],datos_cliente[3],datos_cliente[4],datos_cliente[5],datos_cliente[6]]
            return datos_cliente_factura
        except Exception as error:
            print("Error en el metodo de creadcion del array datos factura datos cliente",error)



    def modificar_viaje(self):
        try:
           print(str(facturacion.Facturacion.calcular_tarifa(self)))
           datos_linea_viaje = facturacion.Facturacion.recoger_datos_linea_viaje(self)
           datos_linea_viaje_para_comparar = [datos_linea_viaje[1],datos_linea_viaje[2],datos_linea_viaje[3]]
           datos_panel_linea: list[Any] = [var.ui.cmb_localidad_origen.currentText(),var.ui.cmb_localidad_destino.currentText(),var.ui.txt_kilometros.text()]
           if datos_linea_viaje_para_comparar==datos_panel_linea:
               Ventanas.Ventanas.ventana_info("No has modificado datos del viaje")
           else:
               query_modificar_linea_de_viaje = QtSql.QSqlQuery()
               query_modificar_linea_de_viaje.prepare('update viajes set origen = :origen  ,destino = :destino ,kms =:kms ,tarifa = :tarifa where idViaje = :idViaje')
               query_modificar_linea_de_viaje.bindValue(':origen',str(datos_panel_linea[0]))
               query_modificar_linea_de_viaje.bindValue(':destino',str(datos_panel_linea[1]))
               query_modificar_linea_de_viaje.bindValue(':kms',int(datos_panel_linea[2]))
               query_modificar_linea_de_viaje.bindValue(':tarifa',float(facturacion.Facturacion.calcular_tarifa(self)))
               query_modificar_linea_de_viaje.bindValue(':idViaje', int(datos_linea_viaje[0]))
           try:
               if query_modificar_linea_de_viaje.exec():
                    Ventanas.Ventanas.ventana_info("Se ha modificado la linea de viaje")
                    facturacion.Facturacion.rellenar_tabla_lineas_viaje(self)
                    var.ui.btn_modificar_viaje.setVisible(False)
                    facturacion.Facturacion.limpiar_panel_viajes(self)
               else:
                   print("no se ha modificado nada")
           except QtSql.QSqlError as error:
               print(error)

        except Exception as error:
            print("Error en la modificación de una linea de viaje",error)


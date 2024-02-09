from typing import List, Any

from PyQt6 import QtSql

import Ventanas
import conexion
import drivers
import var

from Facturas import facturacion


class Facturacion_Repository:



    def recuperar_facturas_segun_dni(dni):
        try:
            listado_de_facturas = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from facturas where dniCliente = :dniCliente")
            query.bindValue(":dniCliente", str(dni))
            if query.exec():
               while query.next():
                    registro = [query.value(i) for i in range(query.record().count())]
                    listado_de_facturas.append(registro)

            if len(listado_de_facturas)==0:
                Ventanas.Ventanas.mensaje_warning("El cliente no tiene facturas en la base de datos")
                return
            else:
                return listado_de_facturas
        except Exception as erro:
            print(erro)




    def insert_line_de_viaje(registro):
        """
        Método para insertar una línea de viaje en la base de datos.

        :param registro: Lista que contiene los datos de la línea de viaje a insertar.
        :type registro: list

        :return: None

        Descripción:
        Este método inserta una nueva línea de viaje en la base de datos.
        Prepara la consulta SQL para la inserción de los datos de la línea de viaje utilizando los parámetros proporcionados.
        Vincula los valores del registro a los marcadores de posición en la consulta SQL.
        Ejecuta la consulta SQL y muestra un mensaje de éxito si la inserción se realiza correctamente.
        En caso de error, muestra una advertencia al usuario y imprime el error en la consola.
        """

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
        """
        Método para insertar una factura en la base de datos.

        :return: None

        Descripción:
        Este método inserta una nueva factura en la base de datos utilizando los datos proporcionados por el usuario.
        Realiza varias validaciones antes de la inserción para garantizar la integridad de los datos.
        Si algún dato no cumple con las validaciones, muestra un mensaje de advertencia correspondiente.
        Prepara la consulta SQL para la inserción de la factura con los datos proporcionados.
        Ejecuta la consulta SQL para insertar la factura en la base de datos.
        Llama al método para insertar los datos de viaje relacionados con la factura recién creada.
        Muestra un mensaje de éxito después de la inserción y actualiza la lista de facturas en la interfaz.
        En caso de error, muestra un mensaje de advertencia y registra el error en la consola.
        """

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
        """
        Método para recuperar las líneas de viaje asociadas a una factura.

        :param idFactura: El ID de la factura para la cual se recuperarán las líneas de viaje.
        :type idFactura: int
        :return: Una lista de listas que contiene las líneas de viaje asociadas a la factura.
        :rtype: list

        Descripción:
        Este método recupera todas las líneas de viaje asociadas a una factura específica de la base de datos.
        Prepara una consulta SQL para seleccionar todas las líneas de viaje que corresponden al ID de la factura proporcionado.
        Ejecuta la consulta SQL y recorre los resultados para construir una lista de listas que contiene las líneas de viaje.
        Por cada fila en los resultados de la consulta, se crea una lista con los valores de cada columna, excluyendo el ID de la factura.
        Añade esta lista de valores a la lista principal de líneas de viaje.
        Devuelve la lista de líneas de viaje al finalizar.
        En caso de error, muestra un mensaje de error en la consola y registra el error específico de la consulta SQL.
        """

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
        """
        Método para eliminar una línea de viaje de la base de datos.

        :param id_viaje: El ID de la línea de viaje que se va a eliminar.
        :type id_viaje: int

        Descripción:
        Este método elimina una línea de viaje específica de la base de datos.
        Prepara una consulta SQL para eliminar la línea de viaje con el ID proporcionado.
        Ejecuta la consulta SQL y comprueba si se ejecuta correctamente.
        Imprime un mensaje indicando que la línea de viaje se ha eliminado si la consulta se ejecuta con éxito.
        En caso de error, muestra un mensaje de error en la consola y registra el error específico.
        """

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
        """
        Método para comprobar si una factura existe en la base de datos.

        :param id_Factura: El ID de la factura que se va a comprobar.
        :type id_Factura: int

        :return: True si la factura existe, False de lo contrario.
        :rtype: bool

        Descripción:
        Este método verifica si una factura con el ID especificado existe en la base de datos.
        Prepara una consulta SQL para seleccionar todas las filas de la tabla de facturas donde el número de factura coincida con el ID proporcionado.
        Ejecuta la consulta SQL y comprueba si se ejecuta correctamente y si hay resultados.
        Si la consulta se ejecuta correctamente y se encuentra al menos una fila, devuelve True, lo que indica que la factura existe.
        En caso de error, imprime un mensaje de error en la consola y registra el error específico.
        """

        try:
            query_verificar_factura_existe = QtSql.QSqlQuery()
            query_verificar_factura_existe.prepare('select * from facturas where numFactura = :nunFactura')
            query_verificar_factura_existe.bindValue(':nunFactura',id_Factura)
            if query_verificar_factura_existe.exec() and query_verificar_factura_existe.next():
                return True

        except Exception as error:
            print("Error al validar la existencia de una factura")


    def recuperar_datos_cliente_factura(self=None):
        """
        Método para recuperar los datos del cliente asociado a una factura.

        :return: Una lista con los datos del cliente asociado a la factura actual.
        :rtype: list

        Descripción:
        Este método recupera los datos del cliente asociado a la factura actualmente seleccionada en la tabla de facturas.
        Obtiene el número de factura de la fila actualmente seleccionada en la tabla de facturas.
        Prepara una consulta SQL para seleccionar todas las filas de la tabla de facturas donde el número de factura coincida con el número obtenido.
        Ejecuta la consulta SQL y recupera todos los registros de la factura actual.
        Obtiene el DNI del cliente asociado a la factura a partir de los datos recuperados de la factura.
        Utiliza el DNI del cliente para recuperar los datos completos del cliente desde la base de datos.
        Crea una lista con los datos combinados de la factura y el cliente, y la devuelve.
        En caso de error, imprime un mensaje de error en la consola y registra el error específico.
        """

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
        """
        Método para modificar un viaje en la base de datos.

        :return: None
        :rtype: None

        Descripción:
        Este método permite modificar los detalles de un viaje en la base de datos.
        Primero, calcula la tarifa del viaje actual utilizando el método `calcular_tarifa` de la clase `Facturacion`.
        Luego, recoge los datos del viaje actualmente seleccionado desde la interfaz de usuario.
        Los compara con los datos introducidos en el panel de edición de viajes para determinar si se han realizado cambios.
        Si no se han realizado cambios, muestra un mensaje informativo y no realiza ninguna modificación.
        En caso contrario, prepara una consulta SQL para actualizar los detalles del viaje en la base de datos.
        Ejecuta la consulta SQL y, si tiene éxito, muestra un mensaje de confirmación, actualiza la tabla de viajes en la interfaz de usuario y limpia el panel de edición de viajes.
        En caso de error durante el proceso de modificación, imprime un mensaje de error en la consola.

        Raises:
        Exception: Si se produce un error durante el proceso de modificación del viaje.

        """


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


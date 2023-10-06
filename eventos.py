import sys

import var


class Eventos():


    @staticmethod
    def abrirCalendar(self):

        try:
            var.calendar.show()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def abrirAcercaDe(self):

        try:
            var.acercade.show()
        except Exception as error:
            print("erro en abrir", error)

    @staticmethod
    def showSalir(self):
        try:
            var.ventana_salir.show()
        except Exception as error:
            print("erro en abrir", error)

    def hideSalir(self):
        try:
            var.ventana_salir.hide()
        except Exception as error:
            print("erro en abrir", error)


    @staticmethod
    def salirAcercaDe(self):

        try:
            var.acercade.hide()
        except Exception as error:
            print("erro en abrir", error)
    @staticmethod
    def salir(self):

        try:
            sys.exit()
        except Exception as error:
            print("erro en abrir", error)

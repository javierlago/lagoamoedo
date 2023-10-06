import sys

import var


class Eventos():
    def salir(self):
        try:
            sys.exit(0)
        except Exception as error:
            print(error, "en módulo eventos")

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
    def salirAcercaDe(self):

        try:
            var.acercade.hide()
        except Exception as error:
            print("erro en abrir", error)
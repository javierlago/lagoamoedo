import var

class Eventos():
    def saludar(self):
        try:
            var.ui.lblTitle.setText("Hola has usado el boton")
        except Exception as error:
            print(error, "en módulo eventos")
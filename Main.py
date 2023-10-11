from ventana_ui import *
from Datos import *

#Hereda las clases de la ventana_ui
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #Método de inicialización
    def __init__(self, *args, **kwargs):
        #Constructor
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        #Configuración de la interfaz
        self.setupUi(self)
        #Por defecto marcaremos el botón ES por defecto
        #Cuando no esta enabled significara en el programa que esta pulsado
        self.es.setEnabled(False)
        #Eventos al hacer click en los botones
        self.chiste.clicked.connect(self.btnChiste)
        self.es.clicked.connect(self.btnES)
        self.en.clicked.connect(self.btnEN)
        self.traducir.clicked.connect(self.btnTraducir)
    def btnChiste(self):
        #Se hace una comprobación para ver si el chiste marcado esta en ES o EN
        if self.es.isEnabled():
            esp=False
        else:
            esp=True
        text = printJoke(esp)
        #Ponemos en el textBrowser el texto
        self.textBrowser.setText(text)
    def btnES(self):
        #Si marcamos un boton habilitamos el otro
        self.es.setEnabled(False)
        self.en.setEnabled(True)
    def btnEN(self):
        #Si marcamos un boton habilitamos el otro
        self.en.setEnabled(False)
        self.es.setEnabled(True)
    def btnTraducir(self):
        #Se traduce el texto del textBrowser
        self.textBrowser.setText(translate(self.textBrowser.toPlainText()))
    def despCategory(self):
        categoria=""
        return categoria
    def despFlag(self):
        flag=""
        return flag
    def search(self):
        search=""
        return search

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
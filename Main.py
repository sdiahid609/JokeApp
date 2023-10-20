import platform
import os
from ventana import *
from Datos import *

if platform.system() == 'Linux':
    os.environ['QT_QPA_PLATFORM'] = 'xcb'
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
        #Eventos al hacer click en los botones
        self.esp=False
        self.esBtn.clicked.connect(self.btnES)
        self.chiste.clicked.connect(self.btnChiste)
        self.traducir.clicked.connect(self.btnTraducir)

        try:
            # Intenta cargar la fuente "Noto Serif CJK KR"
            font = QtGui.QFont("Noto Serif CJK KR")
            self.setFont(font)
        except Exception as e:
            # En caso de error, utiliza una fuente por defecto
            font = QtGui.QFont("Arial")  # Puedes cambiar "Arial" por la fuente que desees
            self.setFont(font)
            
    def btnChiste(self):
        content = self.lineEdit.text()
        selected_category = self.comboBox.currentText()
        text = printJoke(self, selected_category, content)
        #Ponemos en el textBrowser el texto
        self.textBrowser.setText(text)
        self.lineEdit.setText("")
    def btnES(self):
        if(self.esp):
            self.esBtn.setStyleSheet("border-radius: 10px;\n"
    "background-color: rgb(255, 255, 255);\n"
    "image: url(:/Bandera/Bandera-de-Reino-Unido.png);\n"
    "\n"
    "")
        else:
            self.esBtn.setStyleSheet("border-radius: 10px;\n"
    "background-color: rgb(255, 255, 255);\n"
    "image: url(:/Bandera/espana.png);\n"
    "\n"
    "")
        self.esp = not self.esp
    def btnTraducir(self):
        #Se traduce el texto del textBrowser
        self.textBrowser.setText(translate(self.textBrowser.toPlainText()))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
from ventana_ui import *
from Datos import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.chiste.clicked.connect(self.actualizar)
    def actualizar(self):
        text = printJoke()
        self.textBrowser.setText(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
from ventana_ui import *
from Datos import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.es.setEnabled(False)
        self.chiste.clicked.connect(self.btnChiste)
        self.es.clicked.connect(self.btnES)
        self.en.clicked.connect(self.btnEN)
    def btnChiste(self):
        if self.es.isEnabled():
            esp=False
        else:
            esp=True
        text = printJoke(esp)
        self.textBrowser.setText(text)
    def btnES(self):
        self.es.setEnabled(False)
        self.en.setEnabled(True)
    def btnEN(self):
        self.en.setEnabled(False)
        self.es.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
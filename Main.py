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
        self.traducir.clicked.connect(self.btnTraducir)
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
    def btnTraducir(self):
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
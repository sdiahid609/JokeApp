# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(776, 369)
        MainWindow.setMinimumSize(QtCore.QSize(776, 369))
        MainWindow.setMaximumSize(QtCore.QSize(776, 369))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chiste = QtWidgets.QPushButton(self.centralwidget)
        self.chiste.setGeometry(QtCore.QRect(60, 270, 181, 61))
        self.chiste.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.chiste.setToolTipDuration(9)
        self.chiste.setObjectName("chiste")
        self.traducir = QtWidgets.QPushButton(self.centralwidget)
        self.traducir.setGeometry(QtCore.QRect(530, 270, 181, 61))
        self.traducir.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.traducir.setToolTipDuration(9)
        self.traducir.setObjectName("traducir")
        self.es = QtWidgets.QPushButton(self.centralwidget)
        self.es.setGeometry(QtCore.QRect(270, 270, 101, 61))
        self.es.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.es.setToolTipDuration(9)
        self.es.setObjectName("es")
        self.en = QtWidgets.QPushButton(self.centralwidget)
        self.en.setGeometry(QtCore.QRect(400, 270, 101, 61))
        self.en.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.en.setToolTipDuration(9)
        self.en.setObjectName("en")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 30, 631, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JokeApp"))
        self.chiste.setText(_translate("MainWindow", "Contar chiste"))
        self.traducir.setText(_translate("MainWindow", "Traducir"))
        self.es.setText(_translate("MainWindow", "ES"))
        self.en.setText(_translate("MainWindow", "EN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
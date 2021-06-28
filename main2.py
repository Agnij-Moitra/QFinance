from PyQt5 import QtCore, QtGui, QtWidgets
from os import remove


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("MainWindow_2")
        MainWindow_2.resize(1346, 785)
        MainWindow_2.setFixedSize(1346, 784)
        MainWindow_2.setToolTipDuration(-8)
        self.centralwidget = QtWidgets.QWidget(MainWindow_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_graph = QtWidgets.QLabel(self.centralwidget)
        self.label_graph.setGeometry(QtCore.QRect(0, 0, 1341, 771))
        self.label_graph.setText("")
        self.label_graph.setPixmap(QtGui.QPixmap("graph.png"))
        self.label_graph.setScaledContents(True)
        self.label_graph.setObjectName("label_graph")
        MainWindow_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1346, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_2)
        self.statusbar.setObjectName("statusbar")
        MainWindow_2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)
        try:
            remove("graph.png")
        except FileNotFoundError:
            pass

    def retranslateUi(self, MainWindow_2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_2.setWindowTitle(_translate("QFinance", "QFinance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_2()
    ui.setupUi(MainWindow_2)
    MainWindow_2.show()
    sys.exit(app.exec_())
    
    
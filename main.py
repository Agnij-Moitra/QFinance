from numpy import floor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import pickle
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.open = None
        self.high = None
        self.low = None

    def linear_reg(self):
        with open("module_pickle", "rb") as f:
            reg = pickle.load(f)

        return reg.predict([[self.open, self.high, self.low]])

    def pushButton_handler(self):
        vals = list(
            map(float, self.stock_names.text().replace(" ", "").split(",")))
        self.open = vals[0]
        self.high = vals[1]
        self.low = vals[2]
        predicted = self.linear_reg()
        result = int(floor(
            int(self.val_budget.text().replace(" ", "").replace(",", "")) / predicted[0]))
        self.show_popup(
            "QFinance", f"Please consider buying {result} stocks and the predicted close price is {predicted[0]}", "info")

    def show_popup(self, title, content, type):
        msg = QMessageBox()
        msg.setWindowTitle(str(title))
        msg.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        msg.setText(str(content))

        if type == "info":
            msg.setIcon(QMessageBox.Information)

        if type == "warning":
            msg.setIcon(QMessageBox.Warning)

        exit_show_popup = msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 877)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-300, -230, 1581, 1141))
        self.bg.setAutoFillBackground(False)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("m-b-m-ZzOa5G8hSPI-unsplash.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setWordWrap(True)
        self.bg.setObjectName("bg")
        self.stock_names = QtWidgets.QLineEdit(self.centralwidget)
        self.stock_names.setGeometry(QtCore.QRect(830, 450, 421, 81))
        self.stock_names.setStyleSheet("font: 8.25pt \"Arial\";\n"
                                       "")
        self.stock_names.setText("")
        self.stock_names.setObjectName("stock_names")
        self.stock_names.setStyleSheet("font: 18pt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 30, 381, 91))
        self.label.setStyleSheet("font: 18pt \"Arial\";\n"
                                 "color: white;\n"
                                 "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                 "border-radius: 25px;\n"
                                 "background: rgb(255,0,0, 0.9);\n"
                                 "padding: 20px;\n"
                                 "width: 200px;\n"
                                 "height: 150px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 130, 811, 91))
        self.label_3.setStyleSheet("font: 18pt \"Arial\";\n"
                                   "color: black;\n"
                                   "/*text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;*/\n"
                                   "border-radius: 25px;\n"
                                   "background: rgb(0,255,255, 0.6);\n"
                                   "padding: 20px;\n"
                                   "width: 200px;\n"
                                   "height: 150px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.stock_names_label = QtWidgets.QLabel(self.centralwidget)
        self.stock_names_label.setGeometry(
            QtCore.QRect(30, 390, 771, 201))
        self.stock_names_label.setAutoFillBackground(False)
        self.stock_names_label.setStyleSheet("font: 18pt \"Arial\";\n"
                                             "color: black;\n"
                                             "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                             "border-radius: 25px;\n"
                                             "background: rgb(0,255,255, 0.4);\n"
                                             "padding: 20px;\n"
                                             "width: 200px;\n"
                                             "height: 150px;")
        self.stock_names_label.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.stock_names_label.setScaledContents(True)
        self.stock_names_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_names_label.setWordWrap(True)
        self.stock_names_label.setOpenExternalLinks(True)
        self.stock_names_label.setObjectName("stock_names_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 660, 341, 71))
        self.pushButton.setStyleSheet("font: 18pt \"Arial\";\n"
                                      "color: black;\n"
                                      "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                      "border-radius: 25px;\n"
                                      "background: rgb(0,255,255, 0.5);\n"
                                      "padding: 20px;\n"
                                      "width: 200px;\n"
                                      "height: 150px;")
        self.pushButton.setObjectName("pushButton")
        self.stock_names_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.stock_names_label_2.setGeometry(
            QtCore.QRect(170, 240, 531, 131))  # 190, 520, 531, 131
        self.stock_names_label_2.setAutoFillBackground(False)
        self.stock_names_label_2.setStyleSheet("font: 18pt \"Arial\";\n"
                                               "color: black;\n"
                                               "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                               "border-radius: 25px;\n"
                                               "background: rgb(0,255,255, 0.4);\n"
                                               "padding: 20px;\n"
                                               "width: 200px;\n"
                                               "height: 150px;")
        self.stock_names_label_2.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.stock_names_label_2.setScaledContents(True)
        self.stock_names_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_names_label_2.setWordWrap(True)
        self.stock_names_label_2.setOpenExternalLinks(True)
        self.stock_names_label_2.setObjectName("stock_names_label_2")
        self.val_budget = QtWidgets.QLineEdit(self.centralwidget)
        self.val_budget.setGeometry(QtCore.QRect(
            830, 270, 421, 81))  # 830, 530, 421, 81
        self.val_budget.setStyleSheet("font: 18pt \"Arial\";\n"
                                      "")
        self.val_budget.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.pushButton_handler)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("QFinance", "QFinance"))
        self.label.setText(_translate("MainWindow", "QFinance"))
        self.label_3.setText(_translate(
            "MainWindow", "This app will predict the closing value of a stock"))
        self.stock_names_label.setText(_translate(
            "MainWindow", "Enter a comma separated in format: Open Price, High, Low"))
        self.pushButton.setText(_translate(
            "MainWindow", "Find The Best Stocks"))

        self.stock_names_label_2.setText(_translate(
            "MainWindow", r"Please enter the budget in INR(₹)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


'''
350.05, 357.90, 341.10 -- 16th June
348.40, 352.90, 342.25 -- 17th June
'''

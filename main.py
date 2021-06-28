#!/usr/bin/env python
# encoding: utf-8

from numpy import floor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import pandas as pd
from sklearn.linear_model import LinearRegression
# import pickle
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from PyQt5.QtWidgets import *
from main2 import Ui_MainWindow_2
from os import remove

try:
    remove("graph.png")
except FileNotFoundError:
    pass


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.open = None
        self.high = None
        self.low = None
        self.name = None

    def linear_reg(self):
        # with open("module_pickle", "rb") as f:
        #     reg = pickle.load(f)

        STOCK_NAME = self.name

        # In[43]:

        yahoo_data_final = pdr.data.get_data_yahoo(STOCK_NAME, start='2020-01-01')
        yahoo_data_final.to_csv("df.csv")
        del yahoo_data_final
        df = pd.read_csv("df.csv")

        # In[44]:

        df.Open = df.Open.fillna(df.Open.median())
        df.High = df.High.fillna(df.High.median())
        df.Low = df.Low.fillna(df.Low.median())
        df.Close = df.Close.fillna(df.Close.median())

        # In[45]:

        regression = LinearRegression()
        regression.fit(df[["Open", "High", "Low"]], df.Close)

        # In[46]:

        PRE_CLOSE = []
        for i in range(len(df["Close"])):
            temp = (df["Date"][i], (regression.predict([[df["Open"][i], df["High"][i], df["Low"][i]]])))
            PRE_CLOSE.append(temp)
            
        perdicted = pd.DataFrame(PRE_CLOSE, columns=["Date", "Close"])
        del PRE_CLOSE
        del temp

        plt.style.use("seaborn-whitegrid")
        fig = plt.gcf()
        fig.set_size_inches(50, 15)
        plt.title(f"Actual vs Predicted Prices of {STOCK_NAME}", fontsize=100)
        plt.xlabel("Date →", fontsize=50)
        plt.yticks(fontsize=50)
        plt.xticks(fontsize=50)
        plt.xticks(rotation=90)
        plt.ylabel("Price →", fontsize=50)
        plt.tight_layout()
        cmap = "coolwarm"
        last = int(-14)
        plt.scatter(df["Date"][last:], df["Close"][last:], marker=".", c=df["Close"][last:], 
                    cmap=cmap, edgecolor="black", linewidth=0.5, s=1000)

        plt.plot(df["Date"][last:], df["Close"][last:], '-', markersize=2000)

        plt.plot(perdicted["Date"][last:], perdicted["Close"][last:], '^', markersize=20)
        plt.plot(perdicted["Date"][last:], perdicted["Close"][last:], "--", markersize=30)

        plt.legend(["Actual", "Predicted"], loc=2, prop={'size': 50})

        plt.colorbar().ax.tick_params(labelsize=50)
        try:
            remove("graph.png")
        except FileNotFoundError:
            pass
        

        plt.savefig("graph.png", dpi=250, bbox_inches="tight");

        # In[41]:

        del perdicted
        del df
        del STOCK_NAME

        # In[25]:

        return regression.predict([[self.open, self.high, self.low]])

    def pushButton_handler(self):
        vals = list(
            map(float, self.stock_names.text().replace(" ", "").split(",")))
        self.open = vals[0]
        self.high = vals[1]
        self.low = vals[2]
        self.name = self.val_stock_code.text()
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

    def pushButton_handler2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 877)
        MainWindow.setFixedSize(1270, 877)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-300, -290, 1581, 1141))
        self.bg.setAutoFillBackground(False)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("m-b-m-ZzOa5G8hSPI-unsplash.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setWordWrap(True)
        self.bg.setObjectName("bg")
        self.stock_names = QtWidgets.QLineEdit(self.centralwidget)
        self.stock_names.setGeometry(QtCore.QRect(830, 570, 421, 81))
        self.stock_names.setStyleSheet("font: 18pt \"Arial\";\n"
                                       "background: rgb(255, 255, 255, 0.4);")
        self.stock_names.setText("")
        self.stock_names.setObjectName("stock_names")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 30, 381, 91))
        self.label.setStyleSheet("font: 18pt \"Arial\";\n"
                                "color: white;\n"
                                "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                "border-radius: 25px;\n"
                                "background: rgb(0,100, 255, 0.8);\n"
                                "padding: 20px;\n"
                                "width: 200px;\n"
                                "height: 150px;")  
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 140, 811, 91))
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
            QtCore.QRect(10, 510, 771, 201))
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
        self.pushButton.setGeometry(QtCore.QRect(320, 730, 341, 71))
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
            QtCore.QRect(160, 390, 541, 111))  # 190, 520, 531, 131
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
            830, 400, 421, 81))  # 830, 530, 421, 81
        self.val_budget.setStyleSheet("font: 18pt \"Arial\";\n"
                                      "background: rgb(255, 255, 255, 0.4);")
        self.val_budget.setText("")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 730, 341, 71))
        self.pushButton_2.setStyleSheet("font: 18pt \"Arial\";\n"
                                        "color: black;\n"
                                        "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                        "border-radius: 25px;\n"
                                        "background: rgb(0,255,255, 0.5);\n"
                                        "padding: 20px;\n"
                                        "width: 200px;\n"
                                        "height: 150px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.stock_names_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.stock_names_label_3.setGeometry(QtCore.QRect(170, 250, 541, 111))
        self.stock_names_label_3.setAutoFillBackground(False)
        self.stock_names_label_3.setStyleSheet("font: 18pt \"Arial\";\n"
                                                "color: black;\n"
                                                "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                                "border-radius: 25px;\n"
                                                "background: rgb(0,255,255, 0.4);\n"
                                                "padding: 20px;\n"
                                                "width: 200px;\n"
                                                "height: 150px;")
        self.stock_names_label_3.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.stock_names_label_3.setScaledContents(True)
        self.stock_names_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_names_label_3.setWordWrap(True)
        self.stock_names_label_3.setOpenExternalLinks(True)
        self.stock_names_label_3.setObjectName("stock_names_label_3")
        self.val_stock_code = QtWidgets.QLineEdit(self.centralwidget)
        self.val_stock_code.setGeometry(QtCore.QRect(830, 270, 421, 81))
        self.val_stock_code.setStyleSheet("font: 18pt \"Arial\";\n"
                                        "background: rgb(255, 255, 255, 0.4);")
        self.val_stock_code.setText("")
        self.val_stock_code.setObjectName("val_stock_code")

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
        self.pushButton_2.clicked.connect(self.pushButton_handler2)

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

        self.pushButton_2.setText(_translate("MainWindow", "Show Graph"))
        self.stock_names_label_3.setText(_translate("MainWindow", "Please enter the stock code"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

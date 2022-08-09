# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\theco\Desktop\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.BtnLoad.setGeometry(QtCore.QRect(300, 400, 75, 23))
        self.BtnLoad.setObjectName("BtnLoad")
        self.BtnPlot = QtWidgets.QPushButton(self.centralwidget)
        self.BtnPlot.setGeometry(QtCore.QRect(300, 430, 75, 23))
        self.BtnPlot.setObjectName("BtnPlot")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 0, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Title.setFont(font)
        self.Title.setFrameShape(QtWidgets.QFrame.Panel)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 281, 411))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionReadme = QtWidgets.QAction(MainWindow)
        self.actionReadme.setObjectName("actionReadme")
        self.actionEnd = QtWidgets.QAction(MainWindow)
        self.actionEnd.setObjectName("actionEnd")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEnd)
        self.menuHelp.addAction(self.actionReadme)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Visualization v1.0"))
        self.BtnLoad.setText(_translate("MainWindow", "Load"))
        self.BtnPlot.setText(_translate("MainWindow", "Plot"))
        self.Title.setText(_translate("MainWindow", "Data Visualisation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionReadme.setText(_translate("MainWindow", "Readme"))
        self.actionEnd.setText(_translate("MainWindow", "End"))
        self.BtnLoad.clicked.connect(self.BtnLoad_handler)
        self.BtnPlot.clicked.connect(self.BtnPlot_handler)


    def BtnPlot_handler(self):
        file = QFileDialog.getOpenFileName()
        path = file[0]
        print(path)
        data = pd.read_csv(path)

        data['Date'] = pd.to_datetime(data['Date'], format='%Y/%m/%d %H:%M:%S')

        date = data['Date']
        humidity = data['Humidity']
        temperature = data['Temperature']

        ##calculate mean values
        humidity_mean = [np.mean(humidity)] * len(humidity)
        temperature_mean = [np.mean(temperature)] * len(temperature)

        ##formatting mean strings
        humidity_mean_str = format(np.mean(humidity), '.2f')
        temperature_mean_str = format(np.mean(temperature), '.2f')

        ##plot lines
        plt.plot_date(date, humidity, label='Humidity (%)', marker=',', linestyle='solid')
        plt.plot(date, temperature_mean, label=temperature_mean_str + ' C', marker=' ', linestyle='--')
        plt.plot_date(date, temperature, label='Temperature (C)', marker=',', linestyle='solid')
        plt.plot(date, humidity_mean, label=humidity_mean_str + ' %', marker=' ', linestyle='--')

        plt.title(label='Data Visualization', loc='left')
        plt.legend()
        plt.tight_layout()
        plt.gcf().autofmt_xdate()

        plt.show()

 #   def End_handler(self):
 #       sys.exit(app.exec_())

    def BtnLoad_handler(self):
        print("Load Pressed")
        self.open_dialog_box()

    def open_dialog_box(self):
        file = QFileDialog.getOpenFileName()
        path = file[0]
        print(path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Windows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ComSetBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ComSetBox.setObjectName("ComSetBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ComSetBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ScanPortButton = QtWidgets.QPushButton(self.ComSetBox)
        self.ScanPortButton.setObjectName("ScanPortButton")
        self.verticalLayout_3.addWidget(self.ScanPortButton)
        self.OpenPortButton = QtWidgets.QPushButton(self.ComSetBox)
        self.OpenPortButton.setObjectName("OpenPortButton")
        self.verticalLayout_3.addWidget(self.OpenPortButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.COMLabel = QtWidgets.QLabel(self.ComSetBox)
        self.COMLabel.setObjectName("COMLabel")
        self.gridLayout_2.addWidget(self.COMLabel, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.COMCB = QtWidgets.QComboBox(self.ComSetBox)
        self.COMCB.setObjectName("COMCB")
        self.verticalLayout_2.addWidget(self.COMCB)
        self.BAUDCB = QtWidgets.QComboBox(self.ComSetBox)
        self.BAUDCB.setObjectName("BAUDCB")
        self.verticalLayout_2.addWidget(self.BAUDCB)
        self.DataBitCB = QtWidgets.QComboBox(self.ComSetBox)
        self.DataBitCB.setObjectName("DataBitCB")
        self.verticalLayout_2.addWidget(self.DataBitCB)
        self.ParityCB = QtWidgets.QComboBox(self.ComSetBox)
        self.ParityCB.setObjectName("ParityCB")
        self.verticalLayout_2.addWidget(self.ParityCB)
        self.StopBitCB = QtWidgets.QComboBox(self.ComSetBox)
        self.StopBitCB.setObjectName("StopBitCB")
        self.verticalLayout_2.addWidget(self.StopBitCB)
        self.FloCtrlCB = QtWidgets.QComboBox(self.ComSetBox)
        self.FloCtrlCB.setObjectName("FloCtrlCB")
        self.verticalLayout_2.addWidget(self.FloCtrlCB)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 6, 1)
        self.BAUDLabel = QtWidgets.QLabel(self.ComSetBox)
        self.BAUDLabel.setObjectName("BAUDLabel")
        self.gridLayout_2.addWidget(self.BAUDLabel, 1, 0, 1, 1)
        self.DataLabel = QtWidgets.QLabel(self.ComSetBox)
        self.DataLabel.setObjectName("DataLabel")
        self.gridLayout_2.addWidget(self.DataLabel, 2, 0, 1, 1)
        self.ParityLabel = QtWidgets.QLabel(self.ComSetBox)
        self.ParityLabel.setObjectName("ParityLabel")
        self.gridLayout_2.addWidget(self.ParityLabel, 3, 0, 1, 1)
        self.StopLabel = QtWidgets.QLabel(self.ComSetBox)
        self.StopLabel.setObjectName("StopLabel")
        self.gridLayout_2.addWidget(self.StopLabel, 4, 0, 1, 1)
        self.FloCtrlLabel = QtWidgets.QLabel(self.ComSetBox)
        self.FloCtrlLabel.setObjectName("FloCtrlLabel")
        self.gridLayout_2.addWidget(self.FloCtrlLabel, 5, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addWidget(self.ComSetBox)
        self.LogBox = QtWidgets.QGroupBox(self.centralwidget)
        self.LogBox.setObjectName("LogBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LogBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LogBrowser = QtWidgets.QTextBrowser(self.LogBox)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setItalic(False)
        self.LogBrowser.setFont(font)
        self.LogBrowser.setObjectName("LogBrowser")
        self.gridLayout.addWidget(self.LogBrowser, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpenFileButton = QtWidgets.QPushButton(self.LogBox)
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.horizontalLayout.addWidget(self.OpenFileButton)
        self.FileLineEdit = QtWidgets.QLineEdit(self.LogBox)
        self.FileLineEdit.setObjectName("FileLineEdit")
        self.horizontalLayout.addWidget(self.FileLineEdit)
        self.SendButton = QtWidgets.QPushButton(self.LogBox)
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout.addWidget(self.SendButton)
        self.CleanButton = QtWidgets.QPushButton(self.LogBox)
        self.CleanButton.setObjectName("CleanButton")
        self.horizontalLayout.addWidget(self.CleanButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.LogBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSaveLog = QtWidgets.QAction(MainWindow)
        self.actionSaveLog.setObjectName("actionSaveLog")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSaveLog)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAX32664-Tool v0.1"))
        self.ComSetBox.setTitle(_translate("MainWindow", "串口设置"))
        self.ScanPortButton.setText(_translate("MainWindow", "扫描串口"))
        self.OpenPortButton.setText(_translate("MainWindow", "打开串口"))
        self.COMLabel.setText(_translate("MainWindow", "端口号"))
        self.BAUDLabel.setText(_translate("MainWindow", "波特率"))
        self.DataLabel.setText(_translate("MainWindow", "数据位"))
        self.ParityLabel.setText(_translate("MainWindow", "校验位"))
        self.StopLabel.setText(_translate("MainWindow", "停止位"))
        self.FloCtrlLabel.setText(_translate("MainWindow", "流控制"))
        self.LogBox.setTitle(_translate("MainWindow", "调试信息"))
        self.OpenFileButton.setText(_translate("MainWindow", "打开文件"))
        self.SendButton.setText(_translate("MainWindow", "发送文件"))
        self.CleanButton.setText(_translate("MainWindow", "清除显示"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.actionOpen_File.setText(_translate("MainWindow", "打开文件"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSaveLog.setText(_translate("MainWindow", "保存Log"))
        self.actionSaveLog.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionHelp.setText(_translate("MainWindow", "关于软件"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scriptLattesGUI.ui'
#
# Created: Thu Feb 27 08:32:37 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 635)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtGui.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 20, 691, 31))
        self.input.setObjectName("input")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 691, 16))
        self.label.setObjectName("label")
        self.filechooser = QtGui.QPushButton(self.centralwidget)
        self.filechooser.setGeometry(QtCore.QRect(700, 20, 81, 31))
        self.filechooser.setObjectName("filechooser")
        self.runner = QtGui.QPushButton(self.centralwidget)
        self.runner.setGeometry(QtCore.QRect(250, 60, 311, 31))
        self.runner.setObjectName("runner")
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(2, 80, 801, 541))
        self.tabs.setObjectName("tabs")
        self.output_tab = QtGui.QWidget()
        self.output_tab.setObjectName("output_tab")
        self.scrollOutput = QtGui.QScrollArea(self.output_tab)
        self.scrollOutput.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.scrollOutput.setWidgetResizable(True)
        self.scrollOutput.setObjectName("scrollOutput")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.out = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.out.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.out.setObjectName("out")
        self.scrollOutput.setWidget(self.scrollAreaWidgetContents)
        self.tabs.addTab(self.output_tab, "")
        self.error_tab = QtGui.QWidget()
        self.error_tab.setObjectName("error_tab")
        self.scrollArea_2 = QtGui.QScrollArea(self.error_tab)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 799, 499))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.errors = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.errors.setGeometry(QtCore.QRect(0, 0, 791, 501))
        self.errors.setObjectName("errors")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabs.addTab(self.error_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ScriptLattes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Escolha um arquivo de configuração", None, QtGui.QApplication.UnicodeUTF8))
        self.filechooser.setText(QtGui.QApplication.translate("MainWindow", "Escolher", None, QtGui.QApplication.UnicodeUTF8))
        self.runner.setText(QtGui.QApplication.translate("MainWindow", "Executar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.output_tab), QtGui.QApplication.translate("MainWindow", "Saída", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.error_tab), QtGui.QApplication.translate("MainWindow", "Erros", None, QtGui.QApplication.UnicodeUTF8))


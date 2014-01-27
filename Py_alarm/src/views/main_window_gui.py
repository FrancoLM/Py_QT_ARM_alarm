# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Jan 25 23:49:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 509)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/thermometer_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtGui.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 661, 471))
        self.main_frame.setStyleSheet("QFrame#main_frame{\n"
"    background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgb(250, 250, 250);\n"
"}\n"
"")
        self.main_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.chart_frame = QtGui.QFrame(self.main_frame)
        self.chart_frame.setGeometry(QtCore.QRect(10, 90, 421, 371))
        self.chart_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.chart_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.chart_frame.setObjectName("chart_frame")
        self.chart_temp_label = QtGui.QLabel(self.chart_frame)
        self.chart_temp_label.setGeometry(QtCore.QRect(20, 320, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        self.chart_temp_label.setFont(font)
        self.chart_temp_label.setStyleSheet("color: rgb(68, 68, 68);")
        self.chart_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chart_temp_label.setObjectName("chart_temp_label")
        self.frame = QtGui.QFrame(self.chart_frame)
        self.frame.setGeometry(QtCore.QRect(30, 30, 361, 281))
        self.frame.setStyleSheet("border:2px solid grey;")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.current_temp_frame = QtGui.QFrame(self.main_frame)
        self.current_temp_frame.setGeometry(QtCore.QRect(440, 90, 201, 181))
        self.current_temp_frame.setStyleSheet("")
        self.current_temp_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.current_temp_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.current_temp_frame.setObjectName("current_temp_frame")
        self.current_temp_value = QtGui.QLabel(self.current_temp_frame)
        self.current_temp_value.setGeometry(QtCore.QRect(0, 30, 111, 91))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(72)
        font.setWeight(50)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.current_temp_value.setFont(font)
        self.current_temp_value.setStyleSheet("color: rgb(68, 68, 68);")
        self.current_temp_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.current_temp_value.setObjectName("current_temp_value")
        self.current_temp_label = QtGui.QLabel(self.current_temp_frame)
        self.current_temp_label.setGeometry(QtCore.QRect(10, 130, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        self.current_temp_label.setFont(font)
        self.current_temp_label.setStyleSheet("color: rgb(68, 68, 68);")
        self.current_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_temp_label.setObjectName("current_temp_label")
        self.degree_label = QtGui.QLabel(self.current_temp_frame)
        self.degree_label.setGeometry(QtCore.QRect(110, 30, 41, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setWeight(75)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.degree_label.setFont(font)
        self.degree_label.setStyleSheet("color: rgb(68, 68, 68);")
        self.degree_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.degree_label.setObjectName("degree_label")
        self.max_temp_frame = QtGui.QFrame(self.main_frame)
        self.max_temp_frame.setGeometry(QtCore.QRect(440, 280, 201, 181))
        self.max_temp_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.max_temp_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.max_temp_frame.setObjectName("max_temp_frame")
        self.max_temp_value = QtGui.QLabel(self.max_temp_frame)
        self.max_temp_value.setGeometry(QtCore.QRect(0, 20, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(72)
        font.setWeight(50)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.max_temp_value.setFont(font)
        self.max_temp_value.setStyleSheet("color: rgb(68, 68, 68);")
        self.max_temp_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_temp_value.setObjectName("max_temp_value")
        self.max_temp_label = QtGui.QLabel(self.max_temp_frame)
        self.max_temp_label.setGeometry(QtCore.QRect(10, 130, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        self.max_temp_label.setFont(font)
        self.max_temp_label.setStyleSheet("color: rgb(68, 68, 68);")
        self.max_temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.max_temp_label.setObjectName("max_temp_label")
        self.set_max_temp_button = QtGui.QToolButton(self.max_temp_frame)
        self.set_max_temp_button.setGeometry(QtCore.QRect(160, 10, 31, 31))
        self.set_max_temp_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.set_max_temp_button.setStyleSheet("QToolButton {\n"
"    background-color: rgb(250, 250, 250);;\n"
"    font: 10pt \"Trebuchet MS\";\n"
"    border:none;\n"
"    /*border-bottom:1px solid black;*/\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(209, 209, 227);\n"
"}\n"
"QToolButton:active {\n"
"\n"
"}")
        self.set_max_temp_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/tool_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/tool_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.set_max_temp_button.setIcon(icon1)
        self.set_max_temp_button.setIconSize(QtCore.QSize(23, 23))
        self.set_max_temp_button.setArrowType(QtCore.Qt.NoArrow)
        self.set_max_temp_button.setObjectName("set_max_temp_button")
        self.degree_label_2 = QtGui.QLabel(self.max_temp_frame)
        self.degree_label_2.setGeometry(QtCore.QRect(110, 20, 41, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(72)
        font.setWeight(75)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.degree_label_2.setFont(font)
        self.degree_label_2.setStyleSheet("color: rgb(68, 68, 68);")
        self.degree_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.degree_label_2.setObjectName("degree_label_2")
        self.deactivate_alarm_button = QtGui.QToolButton(self.max_temp_frame)
        self.deactivate_alarm_button.setEnabled(True)
        self.deactivate_alarm_button.setGeometry(QtCore.QRect(160, 80, 31, 31))
        self.deactivate_alarm_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.deactivate_alarm_button.setStyleSheet("QToolButton#deactivate_alarm_button {\n"
"    background-color: rgb(250, 250, 250);;\n"
"    font: 10pt \"Trebuchet MS\";\n"
"    border:none;\n"
"    /*border-bottom:1px solid black;*/\n"
"}\n"
"QToolButton#deactivate_alarm_button:hover {\n"
"    background-color: rgb(209, 209, 227);\n"
"}\n"
"QToolButton#deactivate_alarm_button:active {\n"
"\n"
"}")
        self.deactivate_alarm_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/cancel_alarm_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/icons/cancel_alarm_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deactivate_alarm_button.setIcon(icon2)
        self.deactivate_alarm_button.setIconSize(QtCore.QSize(18, 18))
        self.deactivate_alarm_button.setArrowType(QtCore.Qt.NoArrow)
        self.deactivate_alarm_button.setObjectName("deactivate_alarm_button")
        self.title_label = QtGui.QLabel(self.main_frame)
        self.title_label.setGeometry(QtCore.QRect(80, 10, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(26)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background-color: rgb(85, 163, 151);")
        self.title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")
        self.app_icon_button = QtGui.QPushButton(self.main_frame)
        self.app_icon_button.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.app_icon_button.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(133, 139, 162);\n"
"\n"
"    font: 10pt \"Trebuchet MS\";\n"
"    border:none;\n"
"    width:75%;\n"
"    height:25%;\n"
"    /*border-bottom:1px solid black;*/\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}\n"
"QPushButton:active {\n"
"\n"
"}")
        self.app_icon_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/thermometer_icon_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.app_icon_button.setIcon(icon3)
        self.app_icon_button.setIconSize(QtCore.QSize(60, 60))
        self.app_icon_button.setObjectName("app_icon_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_save_temperature_chart = QtGui.QAction(MainWindow)
        self.action_save_temperature_chart.setObjectName("action_save_temperature_chart")
        self.action_app_tutorial = QtGui.QAction(MainWindow)
        self.action_app_tutorial.setObjectName("action_app_tutorial")
        self.action_set_new_max_temp = QtGui.QAction(MainWindow)
        self.action_set_new_max_temp.setObjectName("action_set_new_max_temp")
        self.action_exit_app = QtGui.QAction(MainWindow)
        self.action_exit_app.setObjectName("action_exit_app")
        self.actionDesactivar_alarma = QtGui.QAction(MainWindow)
        self.actionDesactivar_alarma.setEnabled(False)
        self.actionDesactivar_alarma.setObjectName("actionDesactivar_alarma")
        self.menuFile.addAction(self.actionDesactivar_alarma)
        self.menuFile.addAction(self.action_save_temperature_chart)
        self.menuFile.addAction(self.action_set_new_max_temp)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit_app)
        self.menuHelp.addAction(self.action_app_tutorial)
        self.menuHelp.addAction(self.action_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Temperature Center", None, QtGui.QApplication.UnicodeUTF8))
        self.chart_temp_label.setText(QtGui.QApplication.translate("MainWindow", "Gráfico de Temperaturas", None, QtGui.QApplication.UnicodeUTF8))
        self.current_temp_value.setToolTip(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.current_temp_value.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.current_temp_value.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.current_temp_label.setText(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_label.setToolTip(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_label.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_label.setText(QtGui.QApplication.translate("MainWindow", "°", None, QtGui.QApplication.UnicodeUTF8))
        self.max_temp_value.setToolTip(QtGui.QApplication.translate("MainWindow", "Temperatura Límite", None, QtGui.QApplication.UnicodeUTF8))
        self.max_temp_value.setText(QtGui.QApplication.translate("MainWindow", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.max_temp_label.setText(QtGui.QApplication.translate("MainWindow", "Temperatura Límite", None, QtGui.QApplication.UnicodeUTF8))
        self.set_max_temp_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Establecer un nuevo valor de Temperatura Límite", None, QtGui.QApplication.UnicodeUTF8))
        self.set_max_temp_button.setStatusTip(QtGui.QApplication.translate("MainWindow", "Haz click en este botón para establecer un nuevo valor de Temperatura Límite", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_label_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_label_2.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Temperatura Actual", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_label_2.setText(QtGui.QApplication.translate("MainWindow", "°", None, QtGui.QApplication.UnicodeUTF8))
        self.deactivate_alarm_button.setToolTip(QtGui.QApplication.translate("MainWindow", "Desactivar alarma", None, QtGui.QApplication.UnicodeUTF8))
        self.deactivate_alarm_button.setStatusTip(QtGui.QApplication.translate("MainWindow", "Haz click en este botón para desactivar la alarma", None, QtGui.QApplication.UnicodeUTF8))
        self.title_label.setText(QtGui.QApplication.translate("MainWindow", "   Monitor de Temperaturas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_temperature_chart.setText(QtGui.QApplication.translate("MainWindow", "Guardar historial de Temperaturas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_temperature_chart.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_app_tutorial.setText(QtGui.QApplication.translate("MainWindow", "Cómo utilizar la aplicación...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_app_tutorial.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.action_set_new_max_temp.setText(QtGui.QApplication.translate("MainWindow", "Nuevo valor de Temperatura Límite...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit_app.setText(QtGui.QApplication.translate("MainWindow", "Salir de la aplicación", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDesactivar_alarma.setText(QtGui.QApplication.translate("MainWindow", "Desactivar alarma", None, QtGui.QApplication.UnicodeUTF8))

import resource_file_rc

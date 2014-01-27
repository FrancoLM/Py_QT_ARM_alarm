# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_max_temp_dialog.ui'
#
# Created: Sun Jan 26 23:07:09 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_new_max_temp_dialog(object):
    def setupUi(self, new_max_temp_dialog):
        new_max_temp_dialog.setObjectName("new_max_temp_dialog")
        new_max_temp_dialog.resize(301, 130)
        self.frame = QtGui.QFrame(new_max_temp_dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 301, 131))
        self.frame.setStyleSheet("QFrame{background-color: rgb(226, 226, 226);}\n"
"")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(10, 90, 281, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("QPushButton {\n"
"    background-color: rgb(250, 250, 250);;\n"
"    font: 10pt \"Trebuchet MS\";\n"
"    border:none;\n"
"    width:75%;\n"
"    height:25%;\n"
"    /*border-bottom:1px solid black;*/\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(209, 209, 227);\n"
"}\n"
"QPushButton:active {\n"
"\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"border:none;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.max_temp_prompt_label = QtGui.QLabel(self.frame)
        self.max_temp_prompt_label.setGeometry(QtCore.QRect(10, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.max_temp_prompt_label.setFont(font)
        self.max_temp_prompt_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.max_temp_prompt_label.setStyleSheet("color: rgb(68, 68, 68);")
        self.max_temp_prompt_label.setTextFormat(QtCore.Qt.AutoText)
        self.max_temp_prompt_label.setScaledContents(False)
        self.max_temp_prompt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.max_temp_prompt_label.setWordWrap(True)
        self.max_temp_prompt_label.setObjectName("max_temp_prompt_label")
        self.degree_sign_label = QtGui.QLabel(self.frame)
        self.degree_sign_label.setGeometry(QtCore.QRect(153, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(15)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.degree_sign_label.setFont(font)
        self.degree_sign_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.degree_sign_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.degree_sign_label.setTextFormat(QtCore.Qt.AutoText)
        self.degree_sign_label.setScaledContents(False)
        self.degree_sign_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.degree_sign_label.setWordWrap(True)
        self.degree_sign_label.setObjectName("degree_sign_label")

        self.retranslateUi(new_max_temp_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), new_max_temp_dialog.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), new_max_temp_dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(new_max_temp_dialog)
        new_max_temp_dialog.setTabOrder(self.lineEdit, self.buttonBox)

    def retranslateUi(self, new_max_temp_dialog):
        new_max_temp_dialog.setWindowTitle(QtGui.QApplication.translate("new_max_temp_dialog", "Ingrese Temperatura Máxima", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("new_max_temp_dialog", "old value", None, QtGui.QApplication.UnicodeUTF8))
        self.max_temp_prompt_label.setText(QtGui.QApplication.translate("new_max_temp_dialog", "Ingrese un nuevo valor de temperatura máxima", None, QtGui.QApplication.UnicodeUTF8))
        self.degree_sign_label.setText(QtGui.QApplication.translate("new_max_temp_dialog", "°", None, QtGui.QApplication.UnicodeUTF8))

import resource_file_rc

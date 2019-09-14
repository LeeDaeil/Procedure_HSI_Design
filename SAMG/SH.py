# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SH.ui',
# licensing of 'SH.ui' applies.
#
# Created: Sat Sep 14 09:39:19 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(2562, 1363)
        MainForm.setStyleSheet("background-color: rgb(217, 225, 232);")
        self.Bar_1 = QtWidgets.QFrame(MainForm)
        self.Bar_1.setGeometry(QtCore.QRect(0, 0, 411, 1361))
        self.Bar_1.setStyleSheet("background-color: #d9e1e8;\n"
"border: none;\n"
"border-right: 2px solid black;")
        self.Bar_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Bar_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bar_1.setObjectName("Bar_1")
        self.Info_frame = QtWidgets.QFrame(self.Bar_1)
        self.Info_frame.setGeometry(QtCore.QRect(10, 10, 391, 131))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.Info_frame.setFont(font)
        self.Info_frame.setStyleSheet("border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"border: 1px solid black;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #56a, stop: 0.5 #2b90d9);")
        self.Info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info_frame.setObjectName("Info_frame")
        self.L_CT = QtWidgets.QLabel(self.Info_frame)
        self.L_CT.setGeometry(QtCore.QRect(10, 40, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.L_CT.setFont(font)
        self.L_CT.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.L_CT.setObjectName("L_CT")
        self.T_time = QtWidgets.QLabel(self.Info_frame)
        self.T_time.setGeometry(QtCore.QRect(260, 40, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.T_time.setFont(font)
        self.T_time.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_time.setAlignment(QtCore.Qt.AlignCenter)
        self.T_time.setObjectName("T_time")
        self.T_time_flow = QtWidgets.QLabel(self.Info_frame)
        self.T_time_flow.setGeometry(QtCore.QRect(260, 70, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.T_time_flow.setFont(font)
        self.T_time_flow.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_time_flow.setAlignment(QtCore.Qt.AlignCenter)
        self.T_time_flow.setObjectName("T_time_flow")
        self.L_AT = QtWidgets.QLabel(self.Info_frame)
        self.L_AT.setGeometry(QtCore.QRect(10, 70, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.L_AT.setFont(font)
        self.L_AT.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.L_AT.setObjectName("L_AT")
        self.T_date = QtWidgets.QLabel(self.Info_frame)
        self.T_date.setGeometry(QtCore.QRect(260, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.T_date.setFont(font)
        self.T_date.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_date.setAlignment(QtCore.Qt.AlignCenter)
        self.T_date.setObjectName("T_date")
        self.L_P = QtWidgets.QLabel(self.Info_frame)
        self.L_P.setGeometry(QtCore.QRect(10, 100, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.L_P.setFont(font)
        self.L_P.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.L_P.setObjectName("L_P")
        self.T_plant_label = QtWidgets.QLabel(self.Info_frame)
        self.T_plant_label.setGeometry(QtCore.QRect(260, 100, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.T_plant_label.setFont(font)
        self.T_plant_label.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.T_plant_label.setAlignment(QtCore.Qt.AlignCenter)
        self.T_plant_label.setObjectName("T_plant_label")
        self.L_CD = QtWidgets.QLabel(self.Info_frame)
        self.L_CD.setGeometry(QtCore.QRect(10, 10, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.L_CD.setFont(font)
        self.L_CD.setStyleSheet("border-top-left-radius: none;\n"
"font: 14pt \"Arial\";\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;\n"
"color: rgb(255, 255, 255);")
        self.L_CD.setObjectName("L_CD")
        self.Pur_frame = QtWidgets.QFrame(self.Bar_1)
        self.Pur_frame.setGeometry(QtCore.QRect(10, 150, 391, 1211))
        self.Pur_frame.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(217, 225, 232);\n"
"border: 1px solid black;")
        self.Pur_frame.setObjectName("Pur_frame")
        self.B_1 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_1.setGeometry(QtCore.QRect(10, 20, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_1.setFont(font)
        self.B_1.setMouseTracking(False)
        self.B_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.B_1.setAutoFillBackground(False)
        self.B_1.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;    \n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_1.setShortcut("")
        self.B_1.setObjectName("B_1")
        self.B_2 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_2.setGeometry(QtCore.QRect(10, 130, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_2.setFont(font)
        self.B_2.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_2.setObjectName("B_2")
        self.B_3 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_3.setGeometry(QtCore.QRect(10, 240, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_3.setFont(font)
        self.B_3.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_3.setObjectName("B_3")
        self.B_4 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_4.setGeometry(QtCore.QRect(10, 350, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_4.setFont(font)
        self.B_4.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_4.setObjectName("B_4")
        self.B_5 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_5.setGeometry(QtCore.QRect(10, 460, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_5.setFont(font)
        self.B_5.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_5.setObjectName("B_5")
        self.B_6 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_6.setGeometry(QtCore.QRect(10, 570, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_6.setFont(font)
        self.B_6.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_6.setObjectName("B_6")
        self.B_7 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_7.setGeometry(QtCore.QRect(10, 680, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_7.setFont(font)
        self.B_7.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_7.setObjectName("B_7")
        self.B_8 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_8.setGeometry(QtCore.QRect(10, 790, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_8.setFont(font)
        self.B_8.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_8.setObjectName("B_8")
        self.B_9 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_9.setGeometry(QtCore.QRect(10, 900, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_9.setFont(font)
        self.B_9.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton {\n"
"    text-align: left;\n"
"}")
        self.B_9.setObjectName("B_9")
        self.per_num_9 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_9.setGeometry(QtCore.QRect(270, 900, 101, 71))
        self.per_num_9.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_9.setProperty("intValue", 0)
        self.per_num_9.setObjectName("per_num_9")
        self.B_10 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_10.setGeometry(QtCore.QRect(10, 1150, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_10.setFont(font)
        self.B_10.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_10.setObjectName("B_10")
        self.B_11 = QtWidgets.QPushButton(self.Pur_frame)
        self.B_11.setGeometry(QtCore.QRect(200, 1150, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.B_11.setFont(font)
        self.B_11.setStyleSheet("QPushButton{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    background-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(188, 188, 188);\n"
"}")
        self.B_11.setObjectName("B_11")
        self.per_num_10 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_10.setGeometry(QtCore.QRect(270, 790, 101, 71))
        self.per_num_10.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_10.setProperty("intValue", 0)
        self.per_num_10.setObjectName("per_num_10")
        self.per_num_11 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_11.setGeometry(QtCore.QRect(270, 680, 101, 71))
        self.per_num_11.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_11.setProperty("intValue", 0)
        self.per_num_11.setObjectName("per_num_11")
        self.per_num_12 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_12.setGeometry(QtCore.QRect(270, 570, 101, 71))
        self.per_num_12.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_12.setProperty("intValue", 0)
        self.per_num_12.setObjectName("per_num_12")
        self.per_num_13 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_13.setGeometry(QtCore.QRect(270, 460, 101, 71))
        self.per_num_13.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_13.setProperty("intValue", 0)
        self.per_num_13.setObjectName("per_num_13")
        self.per_num_14 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_14.setGeometry(QtCore.QRect(270, 350, 101, 71))
        self.per_num_14.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_14.setProperty("intValue", 0)
        self.per_num_14.setObjectName("per_num_14")
        self.per_num_15 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_15.setGeometry(QtCore.QRect(270, 240, 101, 71))
        self.per_num_15.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_15.setProperty("intValue", 0)
        self.per_num_15.setObjectName("per_num_15")
        self.per_num_16 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_16.setGeometry(QtCore.QRect(270, 130, 101, 71))
        self.per_num_16.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_16.setProperty("intValue", 0)
        self.per_num_16.setObjectName("per_num_16")
        self.per_num_17 = QtWidgets.QLCDNumber(self.Pur_frame)
        self.per_num_17.setGeometry(QtCore.QRect(270, 20, 101, 71))
        self.per_num_17.setStyleSheet("border-top-left-radius: none;\n"
"border-top-right-radius: none;\n"
"border: none;\n"
"background: none;")
        self.per_num_17.setProperty("intValue", 0)
        self.per_num_17.setObjectName("per_num_17")
        self.stackedWidget = QtWidgets.QStackedWidget(MainForm)
        self.stackedWidget.setGeometry(QtCore.QRect(420, 80, 1311, 1281))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.bp_0 = QtWidgets.QWidget()
        self.bp_0.setObjectName("bp_0")
        self.sa_step_10 = QtWidgets.QScrollArea(self.bp_0)
        self.sa_step_10.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_10.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(217, 225, 232);\n"
"border: 1px solid black;")
        self.sa_step_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sa_step_10.setWidgetResizable(True)
        self.sa_step_10.setObjectName("sa_step_10")
        self.sa_7_w_13 = QtWidgets.QWidget()
        self.sa_7_w_13.setGeometry(QtCore.QRect(0, 0, 1299, 1279))
        self.sa_7_w_13.setMinimumSize(QtCore.QSize(0, 0))
        self.sa_7_w_13.setObjectName("sa_7_w_13")
        self.sa_step_10.setWidget(self.sa_7_w_13)
        self.stackedWidget.addWidget(self.bp_0)
        self.bp_1 = QtWidgets.QWidget()
        self.bp_1.setObjectName("bp_1")
        self.sa_step_1 = QtWidgets.QScrollArea(self.bp_1)
        self.sa_step_1.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_1.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(217, 225, 232);\n"
"border: 1px solid black;")
        self.sa_step_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sa_step_1.setWidgetResizable(True)
        self.sa_step_1.setObjectName("sa_step_1")
        self.sa_7_w_8 = QtWidgets.QWidget()
        self.sa_7_w_8.setGeometry(QtCore.QRect(0, 0, 1299, 1279))
        self.sa_7_w_8.setMinimumSize(QtCore.QSize(0, 0))
        self.sa_7_w_8.setObjectName("sa_7_w_8")
        self.pushButton_17 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_17.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pur_title_5 = QtWidgets.QLabel(self.sa_7_w_8)
        self.pur_title_5.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_5.setFont(font)
        self.pur_title_5.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_5.setObjectName("pur_title_5")
        self.pushButton_18 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_18.setGeometry(QtCore.QRect(70, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pur_title_6 = QtWidgets.QLabel(self.sa_7_w_8)
        self.pur_title_6.setGeometry(QtCore.QRect(100, 140, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_6.setFont(font)
        self.pur_title_6.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_6.setObjectName("pur_title_6")
        self.pushButton_23 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_23.setGeometry(QtCore.QRect(70, 275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_26 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_26.setGeometry(QtCore.QRect(70, 385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_29 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_29.setGeometry(QtCore.QRect(70, 495, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_32 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_32.setGeometry(QtCore.QRect(70, 605, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pur_title_72 = QtWidgets.QLabel(self.sa_7_w_8)
        self.pur_title_72.setGeometry(QtCore.QRect(100, 250, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_72.setFont(font)
        self.pur_title_72.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_72.setObjectName("pur_title_72")
        self.pur_title_73 = QtWidgets.QLabel(self.sa_7_w_8)
        self.pur_title_73.setGeometry(QtCore.QRect(100, 360, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_73.setFont(font)
        self.pur_title_73.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_73.setObjectName("pur_title_73")
        self.pur_title_74 = QtWidgets.QLabel(self.sa_7_w_8)
        self.pur_title_74.setGeometry(QtCore.QRect(100, 470, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_74.setFont(font)
        self.pur_title_74.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_74.setObjectName("pur_title_74")
        self.pur_title_75 = QtWidgets.QLabel(self.sa_7_w_8)
        self.pur_title_75.setGeometry(QtCore.QRect(100, 580, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_75.setFont(font)
        self.pur_title_75.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_75.setObjectName("pur_title_75")
        self.pushButton_118 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_118.setGeometry(QtCore.QRect(1170, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_118.setFont(font)
        self.pushButton_118.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_118.setObjectName("pushButton_118")
        self.pushButton_123 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_123.setGeometry(QtCore.QRect(1170, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_123.setFont(font)
        self.pushButton_123.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_123.setObjectName("pushButton_123")
        self.pushButton_128 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_128.setGeometry(QtCore.QRect(1170, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_128.setFont(font)
        self.pushButton_128.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_128.setObjectName("pushButton_128")
        self.pushButton_135 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_135.setGeometry(QtCore.QRect(1170, 510, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_135.setFont(font)
        self.pushButton_135.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_135.setObjectName("pushButton_135")
        self.pushButton_137 = QtWidgets.QPushButton(self.sa_7_w_8)
        self.pushButton_137.setGeometry(QtCore.QRect(1170, 620, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_137.setFont(font)
        self.pushButton_137.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_137.setObjectName("pushButton_137")
        self.sa_step_1.setWidget(self.sa_7_w_8)
        self.stackedWidget.addWidget(self.bp_1)
        self.bp_2 = QtWidgets.QWidget()
        self.bp_2.setObjectName("bp_2")
        self.sa_step_2 = QtWidgets.QScrollArea(self.bp_2)
        self.sa_step_2.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_2.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sa_step_2.setWidgetResizable(True)
        self.sa_step_2.setObjectName("sa_step_2")
        self.sa_7_w_7 = QtWidgets.QWidget()
        self.sa_7_w_7.setGeometry(QtCore.QRect(0, 0, 1299, 1279))
        self.sa_7_w_7.setObjectName("sa_7_w_7")
        self.pushButton_36 = QtWidgets.QPushButton(self.sa_7_w_7)
        self.pushButton_36.setGeometry(QtCore.QRect(1170, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_34 = QtWidgets.QPushButton(self.sa_7_w_7)
        self.pushButton_34.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_38 = QtWidgets.QPushButton(self.sa_7_w_7)
        self.pushButton_38.setGeometry(QtCore.QRect(1170, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.sa_7_w_7)
        self.pushButton_39.setGeometry(QtCore.QRect(20, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_39.setObjectName("pushButton_39")
        self.label_5 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_5.setGeometry(QtCore.QRect(50, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_7.setGeometry(QtCore.QRect(100, 290, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_7.setObjectName("label_7")
        self.label_31 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_31.setGeometry(QtCore.QRect(50, 250, 1221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_31.setMargin(0)
        self.label_31.setIndent(-1)
        self.label_31.setOpenExternalLinks(False)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_32.setGeometry(QtCore.QRect(50, 320, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_33.setGeometry(QtCore.QRect(100, 320, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_33.setTextFormat(QtCore.Qt.AutoText)
        self.label_33.setScaledContents(True)
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_34.setGeometry(QtCore.QRect(100, 440, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_34.setObjectName("label_34")
        self.label_8 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_8.setGeometry(QtCore.QRect(680, 290, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_8.setObjectName("label_8")
        self.label_35 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_35.setGeometry(QtCore.QRect(680, 320, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.pur_title_7 = QtWidgets.QLabel(self.sa_7_w_7)
        self.pur_title_7.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_7.setFont(font)
        self.pur_title_7.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_7.setWordWrap(True)
        self.pur_title_7.setObjectName("pur_title_7")
        self.pur_title_8 = QtWidgets.QLabel(self.sa_7_w_7)
        self.pur_title_8.setGeometry(QtCore.QRect(50, 140, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_8.setFont(font)
        self.pur_title_8.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_8.setWordWrap(True)
        self.pur_title_8.setObjectName("pur_title_8")
        self.label_36 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_36.setGeometry(QtCore.QRect(50, 440, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_37.setGeometry(QtCore.QRect(680, 440, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_38.setGeometry(QtCore.QRect(50, 560, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_39.setGeometry(QtCore.QRect(50, 680, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_40.setGeometry(QtCore.QRect(50, 800, 51, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_41.setGeometry(QtCore.QRect(100, 560, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_41.setScaledContents(False)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_42.setGeometry(QtCore.QRect(100, 680, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_43.setGeometry(QtCore.QRect(100, 800, 581, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_44.setGeometry(QtCore.QRect(680, 560, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_44.setWordWrap(True)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_45.setGeometry(QtCore.QRect(680, 680, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_45.setWordWrap(True)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.sa_7_w_7)
        self.label_46.setGeometry(QtCore.QRect(680, 800, 591, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_46.setWordWrap(True)
        self.label_46.setObjectName("label_46")
        self.sa_step_2.setWidget(self.sa_7_w_7)
        self.stackedWidget.addWidget(self.bp_2)
        self.bp_3 = QtWidgets.QWidget()
        self.bp_3.setObjectName("bp_3")
        self.sa_step_3 = QtWidgets.QScrollArea(self.bp_3)
        self.sa_step_3.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_3.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sa_step_3.setWidgetResizable(True)
        self.sa_step_3.setObjectName("sa_step_3")
        self.sa_7_w_9 = QtWidgets.QWidget()
        self.sa_7_w_9.setGeometry(QtCore.QRect(0, 0, 1299, 1279))
        self.sa_7_w_9.setObjectName("sa_7_w_9")
        self.pushButton_45 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_45.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_40 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_40.setGeometry(QtCore.QRect(1170, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_44 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_44.setGeometry(QtCore.QRect(1170, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_43 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_43.setGeometry(QtCore.QRect(20, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_46 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_46.setGeometry(QtCore.QRect(20, 275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_47.setGeometry(QtCore.QRect(1170, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_48.setGeometry(QtCore.QRect(1170, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.sa_7_w_9)
        self.pushButton_49.setGeometry(QtCore.QRect(20, 385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pur_title_9 = QtWidgets.QLabel(self.sa_7_w_9)
        self.pur_title_9.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_9.setFont(font)
        self.pur_title_9.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_9.setWordWrap(True)
        self.pur_title_9.setObjectName("pur_title_9")
        self.pur_title_10 = QtWidgets.QLabel(self.sa_7_w_9)
        self.pur_title_10.setGeometry(QtCore.QRect(50, 140, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_10.setFont(font)
        self.pur_title_10.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_10.setWordWrap(True)
        self.pur_title_10.setObjectName("pur_title_10")
        self.pur_title_11 = QtWidgets.QLabel(self.sa_7_w_9)
        self.pur_title_11.setGeometry(QtCore.QRect(50, 250, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_11.setFont(font)
        self.pur_title_11.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_11.setWordWrap(True)
        self.pur_title_11.setObjectName("pur_title_11")
        self.pur_title_12 = QtWidgets.QLabel(self.sa_7_w_9)
        self.pur_title_12.setGeometry(QtCore.QRect(50, 360, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_12.setFont(font)
        self.pur_title_12.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_12.setWordWrap(True)
        self.pur_title_12.setObjectName("pur_title_12")
        self.sa_step_3.setWidget(self.sa_7_w_9)
        self.stackedWidget.addWidget(self.bp_3)
        self.bq_4 = QtWidgets.QWidget()
        self.bq_4.setObjectName("bq_4")
        self.sa_step_4 = QtWidgets.QScrollArea(self.bq_4)
        self.sa_step_4.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_4.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sa_step_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sa_step_4.setWidgetResizable(True)
        self.sa_step_4.setObjectName("sa_step_4")
        self.sa_7_w_10 = QtWidgets.QWidget()
        self.sa_7_w_10.setGeometry(QtCore.QRect(0, 0, 1299, 1279))
        self.sa_7_w_10.setObjectName("sa_7_w_10")
        self.pushButton_52 = QtWidgets.QPushButton(self.sa_7_w_10)
        self.pushButton_52.setGeometry(QtCore.QRect(1170, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.sa_7_w_10)
        self.pushButton_53.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.sa_7_w_10)
        self.pushButton_54.setGeometry(QtCore.QRect(70, 175, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_56 = QtWidgets.QPushButton(self.sa_7_w_10)
        self.pushButton_56.setGeometry(QtCore.QRect(70, 415, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_58 = QtWidgets.QPushButton(self.sa_7_w_10)
        self.pushButton_58.setGeometry(QtCore.QRect(1170, 440, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_62 = QtWidgets.QPushButton(self.sa_7_w_10)
        self.pushButton_62.setGeometry(QtCore.QRect(20, 295, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_62.setObjectName("pushButton_62")
        self.pur_title_14 = QtWidgets.QLabel(self.sa_7_w_10)
        self.pur_title_14.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_14.setFont(font)
        self.pur_title_14.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_14.setWordWrap(True)
        self.pur_title_14.setObjectName("pur_title_14")
        self.pur_title_13 = QtWidgets.QLabel(self.sa_7_w_10)
        self.pur_title_13.setGeometry(QtCore.QRect(100, 140, 1061, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_13.setFont(font)
        self.pur_title_13.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_13.setWordWrap(True)
        self.pur_title_13.setObjectName("pur_title_13")
        self.pur_title_15 = QtWidgets.QLabel(self.sa_7_w_10)
        self.pur_title_15.setGeometry(QtCore.QRect(50, 270, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_15.setFont(font)
        self.pur_title_15.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_15.setWordWrap(True)
        self.pur_title_15.setObjectName("pur_title_15")
        self.pur_title_16 = QtWidgets.QLabel(self.sa_7_w_10)
        self.pur_title_16.setGeometry(QtCore.QRect(100, 380, 1061, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_16.setFont(font)
        self.pur_title_16.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_16.setWordWrap(True)
        self.pur_title_16.setObjectName("pur_title_16")
        self.sa_step_4.setWidget(self.sa_7_w_10)
        self.stackedWidget.addWidget(self.bq_4)
        self.bp_5 = QtWidgets.QWidget()
        self.bp_5.setObjectName("bp_5")
        self.sa_step_5 = QtWidgets.QScrollArea(self.bp_5)
        self.sa_step_5.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_5.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_step_5.setWidgetResizable(True)
        self.sa_step_5.setObjectName("sa_step_5")
        self.sa_7_w_11 = QtWidgets.QWidget()
        self.sa_7_w_11.setGeometry(QtCore.QRect(0, 0, 1288, 2162))
        self.sa_7_w_11.setMinimumSize(QtCore.QSize(0, 2162))
        self.sa_7_w_11.setObjectName("sa_7_w_11")
        self.pushButton_65 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_65.setGeometry(QtCore.QRect(20, 55, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_66.setGeometry(QtCore.QRect(70, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_68 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_68.setGeometry(QtCore.QRect(120, 275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_79 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_79.setGeometry(QtCore.QRect(120, 385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_81 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_81.setGeometry(QtCore.QRect(120, 495, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_89 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_89.setGeometry(QtCore.QRect(120, 605, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_89.setFont(font)
        self.pushButton_89.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_96 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_96.setGeometry(QtCore.QRect(70, 715, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_96.setFont(font)
        self.pushButton_96.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_101 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_101.setGeometry(QtCore.QRect(70, 825, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_101.setFont(font)
        self.pushButton_101.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_103 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_103.setGeometry(QtCore.QRect(120, 1045, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_103.setFont(font)
        self.pushButton_103.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_109 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_109.setGeometry(QtCore.QRect(120, 935, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_109.setFont(font)
        self.pushButton_109.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_109.setObjectName("pushButton_109")
        self.pushButton_112 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_112.setGeometry(QtCore.QRect(70, 1155, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_112.setFont(font)
        self.pushButton_112.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_112.setObjectName("pushButton_112")
        self.pushButton_114 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_114.setGeometry(QtCore.QRect(120, 1265, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_114.setFont(font)
        self.pushButton_114.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_114.setObjectName("pushButton_114")
        self.pushButton_117 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_117.setGeometry(QtCore.QRect(120, 1385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_117.setFont(font)
        self.pushButton_117.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_117.setObjectName("pushButton_117")
        self.pushButton_121 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_121.setGeometry(QtCore.QRect(120, 1135, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_121.setFont(font)
        self.pushButton_121.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_121.setObjectName("pushButton_121")
        self.pushButton_125 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_125.setGeometry(QtCore.QRect(70, 1725, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_125.setFont(font)
        self.pushButton_125.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_125.setObjectName("pushButton_125")
        self.pushButton_129 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_129.setGeometry(QtCore.QRect(20, 1615, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_129.setFont(font)
        self.pushButton_129.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_129.setObjectName("pushButton_129")
        self.pushButton_131 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_131.setGeometry(QtCore.QRect(70, 1835, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_131.setFont(font)
        self.pushButton_131.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_131.setObjectName("pushButton_131")
        self.pushButton_134 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_134.setGeometry(QtCore.QRect(70, 1945, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_134.setFont(font)
        self.pushButton_134.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_134.setObjectName("pushButton_134")
        self.pushButton_145 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_145.setGeometry(QtCore.QRect(20, 2055, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_145.setFont(font)
        self.pushButton_145.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_145.setObjectName("pushButton_145")
        self.pushButton_163 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_163.setGeometry(QtCore.QRect(1170, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_163.setFont(font)
        self.pushButton_163.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_163.setObjectName("pushButton_163")
        self.pur_title_18 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_18.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_18.setFont(font)
        self.pur_title_18.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pur_title_18.setWordWrap(True)
        self.pur_title_18.setObjectName("pur_title_18")
        self.pur_title_19 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_19.setGeometry(QtCore.QRect(100, 140, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_19.setFont(font)
        self.pur_title_19.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_19.setWordWrap(True)
        self.pur_title_19.setObjectName("pur_title_19")
        self.pur_title_20 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_20.setGeometry(QtCore.QRect(150, 250, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_20.setFont(font)
        self.pur_title_20.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pur_title_20.setWordWrap(True)
        self.pur_title_20.setObjectName("pur_title_20")
        self.pur_title_21 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_21.setGeometry(QtCore.QRect(150, 360, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_21.setFont(font)
        self.pur_title_21.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_21.setWordWrap(True)
        self.pur_title_21.setObjectName("pur_title_21")
        self.pur_title_22 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_22.setGeometry(QtCore.QRect(150, 470, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_22.setFont(font)
        self.pur_title_22.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_22.setWordWrap(True)
        self.pur_title_22.setObjectName("pur_title_22")
        self.pur_title_23 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_23.setGeometry(QtCore.QRect(150, 580, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_23.setFont(font)
        self.pur_title_23.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_23.setWordWrap(True)
        self.pur_title_23.setObjectName("pur_title_23")
        self.pur_title_24 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_24.setGeometry(QtCore.QRect(100, 690, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_24.setFont(font)
        self.pur_title_24.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_24.setWordWrap(True)
        self.pur_title_24.setObjectName("pur_title_24")
        self.pur_title_25 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_25.setGeometry(QtCore.QRect(100, 800, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_25.setFont(font)
        self.pur_title_25.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_25.setWordWrap(True)
        self.pur_title_25.setObjectName("pur_title_25")
        self.pur_title_26 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_26.setGeometry(QtCore.QRect(150, 910, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_26.setFont(font)
        self.pur_title_26.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_26.setWordWrap(True)
        self.pur_title_26.setObjectName("pur_title_26")
        self.pur_title_28 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_28.setGeometry(QtCore.QRect(150, 1020, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_28.setFont(font)
        self.pur_title_28.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_28.setWordWrap(True)
        self.pur_title_28.setObjectName("pur_title_28")
        self.pur_title_29 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_29.setGeometry(QtCore.QRect(100, 1130, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_29.setFont(font)
        self.pur_title_29.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_29.setWordWrap(True)
        self.pur_title_29.setObjectName("pur_title_29")
        self.pur_title_30 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_30.setGeometry(QtCore.QRect(150, 1240, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_30.setFont(font)
        self.pur_title_30.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_30.setWordWrap(True)
        self.pur_title_30.setObjectName("pur_title_30")
        self.pur_title_31 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_31.setGeometry(QtCore.QRect(150, 1350, 1011, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_31.setFont(font)
        self.pur_title_31.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_31.setWordWrap(True)
        self.pur_title_31.setObjectName("pur_title_31")
        self.pur_title_32 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_32.setGeometry(QtCore.QRect(150, 1470, 1011, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_32.setFont(font)
        self.pur_title_32.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_32.setWordWrap(True)
        self.pur_title_32.setObjectName("pur_title_32")
        self.pur_title_33 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_33.setGeometry(QtCore.QRect(50, 1590, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_33.setFont(font)
        self.pur_title_33.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_33.setWordWrap(True)
        self.pur_title_33.setObjectName("pur_title_33")
        self.pur_title_34 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_34.setGeometry(QtCore.QRect(100, 1700, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_34.setFont(font)
        self.pur_title_34.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_34.setWordWrap(True)
        self.pur_title_34.setObjectName("pur_title_34")
        self.pur_title_35 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_35.setGeometry(QtCore.QRect(100, 1810, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_35.setFont(font)
        self.pur_title_35.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_35.setWordWrap(True)
        self.pur_title_35.setObjectName("pur_title_35")
        self.pur_title_36 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_36.setGeometry(QtCore.QRect(100, 1920, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.pur_title_36.setFont(font)
        self.pur_title_36.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_36.setWordWrap(True)
        self.pur_title_36.setObjectName("pur_title_36")
        self.pur_title_37 = QtWidgets.QLabel(self.sa_7_w_11)
        self.pur_title_37.setGeometry(QtCore.QRect(50, 2030, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_37.setFont(font)
        self.pur_title_37.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_37.setWordWrap(True)
        self.pur_title_37.setObjectName("pur_title_37")
        self.pushButton_331 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_331.setGeometry(QtCore.QRect(1070, 2100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_331.setFont(font)
        self.pushButton_331.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(119, 138, 219);\n"
"border: 1px solid black;")
        self.pushButton_331.setObjectName("pushButton_331")
        self.pushButton_330 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_330.setGeometry(QtCore.QRect(1070, 870, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_330.setFont(font)
        self.pushButton_330.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(119, 138, 219);\n"
"border: 1px solid black;")
        self.pushButton_330.setObjectName("pushButton_330")
        self.pushButton_377 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_377.setGeometry(QtCore.QRect(1070, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_377.setFont(font)
        self.pushButton_377.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(119, 138, 219);\n"
"border: 1px solid black;")
        self.pushButton_377.setObjectName("pushButton_377")
        self.pushButton_61 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_61.setGeometry(QtCore.QRect(1170, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_77 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_77.setGeometry(QtCore.QRect(1170, 1280, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_78.setGeometry(QtCore.QRect(1170, 1400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_80 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_80.setGeometry(QtCore.QRect(1170, 1520, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_86 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_86.setGeometry(QtCore.QRect(1170, 2070, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_87.setGeometry(QtCore.QRect(1170, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_63 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_63.setGeometry(QtCore.QRect(1170, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_88 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_88.setGeometry(QtCore.QRect(1170, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_91 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_91.setGeometry(QtCore.QRect(1170, 470, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_64 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_64.setGeometry(QtCore.QRect(1170, 510, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_93 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_93.setGeometry(QtCore.QRect(1170, 580, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_93.setFont(font)
        self.pushButton_93.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_67 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_67.setGeometry(QtCore.QRect(1170, 620, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_69 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_69.setGeometry(QtCore.QRect(1170, 950, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_95 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_95.setGeometry(QtCore.QRect(1170, 910, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_95.setFont(font)
        self.pushButton_95.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_73 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_73.setGeometry(QtCore.QRect(1170, 1060, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_97 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_97.setGeometry(QtCore.QRect(1170, 1020, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_97.setFont(font)
        self.pushButton_97.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_97.setObjectName("pushButton_97")
        self.pushButton_98 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_98.setGeometry(QtCore.QRect(1170, 1700, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_98.setFont(font)
        self.pushButton_98.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_98.setObjectName("pushButton_98")
        self.pushButton_74 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_74.setGeometry(QtCore.QRect(1170, 1740, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_75.setGeometry(QtCore.QRect(1170, 1850, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_99 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_99.setGeometry(QtCore.QRect(1170, 1810, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_99.setFont(font)
        self.pushButton_99.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_76 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_76.setGeometry(QtCore.QRect(1170, 1960, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_100 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_100.setGeometry(QtCore.QRect(1170, 1920, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_100.setFont(font)
        self.pushButton_100.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_122 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_122.setGeometry(QtCore.QRect(120, 1505, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_122.setFont(font)
        self.pushButton_122.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_122.setObjectName("pushButton_122")
        self.pushButton_379 = QtWidgets.QPushButton(self.sa_7_w_11)
        self.pushButton_379.setGeometry(QtCore.QRect(970, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_379.setFont(font)
        self.pushButton_379.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(119, 138, 219);\n"
"border: 1px solid black;")
        self.pushButton_379.setObjectName("pushButton_379")
        self.sa_step_5.setWidget(self.sa_7_w_11)
        self.stackedWidget.addWidget(self.bp_5)
        self.bp_6 = QtWidgets.QWidget()
        self.bp_6.setObjectName("bp_6")
        self.sa_step_6 = QtWidgets.QScrollArea(self.bp_6)
        self.sa_step_6.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_6.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.sa_step_6.setWidgetResizable(True)
        self.sa_step_6.setObjectName("sa_step_6")
        self.sa_7_w_12 = QtWidgets.QWidget()
        self.sa_7_w_12.setGeometry(QtCore.QRect(0, 0, 1299, 1279))
        self.sa_7_w_12.setObjectName("sa_7_w_12")
        self.pushButton_160 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_160.setGeometry(QtCore.QRect(70, 275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_160.setFont(font)
        self.pushButton_160.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_160.setObjectName("pushButton_160")
        self.pushButton_148 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_148.setGeometry(QtCore.QRect(70, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_148.setFont(font)
        self.pushButton_148.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_148.setObjectName("pushButton_148")
        self.pushButton_147 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_147.setGeometry(QtCore.QRect(70, 385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_147.setFont(font)
        self.pushButton_147.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_147.setObjectName("pushButton_147")
        self.pushButton_151 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_151.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_151.setFont(font)
        self.pushButton_151.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_151.setObjectName("pushButton_151")
        self.label = QtWidgets.QLabel(self.sa_7_w_12)
        self.label.setGeometry(QtCore.QRect(50, 470, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_2.setGeometry(QtCore.QRect(50, 500, 321, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_3.setGeometry(QtCore.QRect(50, 720, 321, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_4.setGeometry(QtCore.QRect(50, 930, 321, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_9.setGeometry(QtCore.QRect(370, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_10.setGeometry(QtCore.QRect(370, 930, 201, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_11.setGeometry(QtCore.QRect(370, 720, 201, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_12.setGeometry(QtCore.QRect(370, 500, 201, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_13.setGeometry(QtCore.QRect(570, 470, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_14.setGeometry(QtCore.QRect(570, 500, 691, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.pur_title_27 = QtWidgets.QLabel(self.sa_7_w_12)
        self.pur_title_27.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_27.setFont(font)
        self.pur_title_27.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_27.setWordWrap(True)
        self.pur_title_27.setObjectName("pur_title_27")
        self.pur_title_38 = QtWidgets.QLabel(self.sa_7_w_12)
        self.pur_title_38.setGeometry(QtCore.QRect(100, 140, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_38.setFont(font)
        self.pur_title_38.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_38.setWordWrap(True)
        self.pur_title_38.setObjectName("pur_title_38")
        self.pur_title_39 = QtWidgets.QLabel(self.sa_7_w_12)
        self.pur_title_39.setGeometry(QtCore.QRect(100, 250, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_39.setFont(font)
        self.pur_title_39.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_39.setWordWrap(True)
        self.pur_title_39.setObjectName("pur_title_39")
        self.pur_title_40 = QtWidgets.QLabel(self.sa_7_w_12)
        self.pur_title_40.setGeometry(QtCore.QRect(100, 360, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_40.setFont(font)
        self.pur_title_40.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_40.setWordWrap(True)
        self.pur_title_40.setObjectName("pur_title_40")
        self.pushButton_165 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_165.setGeometry(QtCore.QRect(1170, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_165.setFont(font)
        self.pushButton_165.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_165.setObjectName("pushButton_165")
        self.label_47 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_47.setGeometry(QtCore.QRect(570, 720, 691, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_47.setWordWrap(True)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.sa_7_w_12)
        self.label_48.setGeometry(QtCore.QRect(570, 930, 691, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);")
        self.label_48.setWordWrap(True)
        self.label_48.setObjectName("label_48")
        self.pushButton_102 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_102.setGeometry(QtCore.QRect(1170, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_102.setFont(font)
        self.pushButton_102.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_105 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_105.setGeometry(QtCore.QRect(1170, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_105.setFont(font)
        self.pushButton_105.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_378 = QtWidgets.QPushButton(self.sa_7_w_12)
        self.pushButton_378.setGeometry(QtCore.QRect(1070, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_378.setFont(font)
        self.pushButton_378.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(119, 138, 219);\n"
"border: 1px solid black;")
        self.pushButton_378.setObjectName("pushButton_378")
        self.sa_step_6.setWidget(self.sa_7_w_12)
        self.stackedWidget.addWidget(self.bp_6)
        self.bp_7 = QtWidgets.QWidget()
        self.bp_7.setObjectName("bp_7")
        self.sa_step_7 = QtWidgets.QScrollArea(self.bp_7)
        self.sa_step_7.setGeometry(QtCore.QRect(0, 0, 1301, 1271))
        self.sa_step_7.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_step_7.setWidgetResizable(True)
        self.sa_step_7.setObjectName("sa_step_7")
        self.sa_7_w = QtWidgets.QWidget()
        self.sa_7_w.setGeometry(QtCore.QRect(0, 0, 1288, 2350))
        self.sa_7_w.setMinimumSize(QtCore.QSize(0, 2350))
        self.sa_7_w.setObjectName("sa_7_w")
        self.pushButton_181 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_181.setGeometry(QtCore.QRect(120, 385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_181.setFont(font)
        self.pushButton_181.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_181.setObjectName("pushButton_181")
        self.pushButton_164 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_164.setGeometry(QtCore.QRect(120, 495, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_164.setFont(font)
        self.pushButton_164.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_164.setObjectName("pushButton_164")
        self.pushButton_171 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_171.setGeometry(QtCore.QRect(70, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_171.setFont(font)
        self.pushButton_171.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_171.setObjectName("pushButton_171")
        self.pushButton_174 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_174.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_174.setFont(font)
        self.pushButton_174.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_174.setObjectName("pushButton_174")
        self.pushButton_176 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_176.setGeometry(QtCore.QRect(120, 275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_176.setFont(font)
        self.pushButton_176.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_176.setObjectName("pushButton_176")
        self.pushButton_177 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_177.setGeometry(QtCore.QRect(70, 605, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_177.setFont(font)
        self.pushButton_177.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_177.setObjectName("pushButton_177")
        self.pushButton_182 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_182.setGeometry(QtCore.QRect(120, 940, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_182.setFont(font)
        self.pushButton_182.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_182.setObjectName("pushButton_182")
        self.pushButton_170 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_170.setGeometry(QtCore.QRect(120, 1050, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_170.setFont(font)
        self.pushButton_170.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_170.setObjectName("pushButton_170")
        self.pushButton_180 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_180.setGeometry(QtCore.QRect(70, 715, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_180.setFont(font)
        self.pushButton_180.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_180.setObjectName("pushButton_180")
        self.pushButton_189 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_189.setGeometry(QtCore.QRect(120, 830, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_189.setFont(font)
        self.pushButton_189.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_189.setObjectName("pushButton_189")
        self.pushButton_193 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_193.setGeometry(QtCore.QRect(120, 1265, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_193.setFont(font)
        self.pushButton_193.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_193.setObjectName("pushButton_193")
        self.pushButton_196 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_196.setGeometry(QtCore.QRect(120, 1160, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_196.setFont(font)
        self.pushButton_196.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_196.setObjectName("pushButton_196")
        self.pushButton_199 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_199.setGeometry(QtCore.QRect(70, 1375, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_199.setFont(font)
        self.pushButton_199.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_199.setObjectName("pushButton_199")
        self.pushButton_202 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_202.setGeometry(QtCore.QRect(120, 1485, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_202.setFont(font)
        self.pushButton_202.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_202.setObjectName("pushButton_202")
        self.pushButton_204 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_204.setGeometry(QtCore.QRect(120, 1710, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_204.setFont(font)
        self.pushButton_204.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_204.setObjectName("pushButton_204")
        self.pushButton_208 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_208.setGeometry(QtCore.QRect(120, 1600, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_208.setFont(font)
        self.pushButton_208.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_208.setObjectName("pushButton_208")
        self.pushButton_210 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_210.setGeometry(QtCore.QRect(20, 1820, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_210.setFont(font)
        self.pushButton_210.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_210.setObjectName("pushButton_210")
        self.label_15 = QtWidgets.QLabel(self.sa_7_w)
        self.label_15.setGeometry(QtCore.QRect(40, 1900, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.sa_7_w)
        self.label_16.setGeometry(QtCore.QRect(40, 1960, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.sa_7_w)
        self.label_17.setGeometry(QtCore.QRect(40, 2040, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.sa_7_w)
        self.label_18.setGeometry(QtCore.QRect(40, 2120, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.sa_7_w)
        self.label_19.setGeometry(QtCore.QRect(40, 2200, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.sa_7_w)
        self.label_20.setGeometry(QtCore.QRect(170, 1900, 991, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.sa_7_w)
        self.label_21.setGeometry(QtCore.QRect(170, 1960, 991, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.sa_7_w)
        self.label_22.setGeometry(QtCore.QRect(170, 2200, 991, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.sa_7_w)
        self.label_23.setGeometry(QtCore.QRect(170, 2120, 991, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.sa_7_w)
        self.label_24.setGeometry(QtCore.QRect(170, 2040, 991, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("border-top-left-radius: 0px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.pur_title_41 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_41.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_41.setFont(font)
        self.pur_title_41.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_41.setWordWrap(True)
        self.pur_title_41.setObjectName("pur_title_41")
        self.pur_title_42 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_42.setGeometry(QtCore.QRect(100, 140, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_42.setFont(font)
        self.pur_title_42.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_42.setWordWrap(True)
        self.pur_title_42.setObjectName("pur_title_42")
        self.pur_title_43 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_43.setGeometry(QtCore.QRect(150, 250, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_43.setFont(font)
        self.pur_title_43.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_43.setWordWrap(True)
        self.pur_title_43.setObjectName("pur_title_43")
        self.pur_title_44 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_44.setGeometry(QtCore.QRect(150, 360, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_44.setFont(font)
        self.pur_title_44.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_44.setWordWrap(True)
        self.pur_title_44.setObjectName("pur_title_44")
        self.pur_title_45 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_45.setGeometry(QtCore.QRect(150, 470, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_45.setFont(font)
        self.pur_title_45.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_45.setWordWrap(True)
        self.pur_title_45.setObjectName("pur_title_45")
        self.pur_title_46 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_46.setGeometry(QtCore.QRect(100, 580, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_46.setFont(font)
        self.pur_title_46.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_46.setWordWrap(True)
        self.pur_title_46.setObjectName("pur_title_46")
        self.pur_title_47 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_47.setGeometry(QtCore.QRect(100, 690, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_47.setFont(font)
        self.pur_title_47.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_47.setWordWrap(True)
        self.pur_title_47.setObjectName("pur_title_47")
        self.pur_title_48 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_48.setGeometry(QtCore.QRect(150, 1020, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_48.setFont(font)
        self.pur_title_48.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_48.setWordWrap(True)
        self.pur_title_48.setObjectName("pur_title_48")
        self.pur_title_49 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_49.setGeometry(QtCore.QRect(150, 800, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_49.setFont(font)
        self.pur_title_49.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_49.setWordWrap(True)
        self.pur_title_49.setObjectName("pur_title_49")
        self.pur_title_50 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_50.setGeometry(QtCore.QRect(150, 910, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_50.setFont(font)
        self.pur_title_50.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_50.setWordWrap(True)
        self.pur_title_50.setObjectName("pur_title_50")
        self.pur_title_51 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_51.setGeometry(QtCore.QRect(150, 1130, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_51.setFont(font)
        self.pur_title_51.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_51.setWordWrap(True)
        self.pur_title_51.setObjectName("pur_title_51")
        self.pur_title_52 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_52.setGeometry(QtCore.QRect(150, 1240, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_52.setFont(font)
        self.pur_title_52.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_52.setWordWrap(True)
        self.pur_title_52.setObjectName("pur_title_52")
        self.pur_title_53 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_53.setGeometry(QtCore.QRect(100, 1350, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_53.setFont(font)
        self.pur_title_53.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_53.setWordWrap(True)
        self.pur_title_53.setObjectName("pur_title_53")
        self.pur_title_54 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_54.setGeometry(QtCore.QRect(150, 1680, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_54.setFont(font)
        self.pur_title_54.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_54.setWordWrap(True)
        self.pur_title_54.setObjectName("pur_title_54")
        self.pur_title_55 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_55.setGeometry(QtCore.QRect(150, 1460, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_55.setFont(font)
        self.pur_title_55.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_55.setWordWrap(True)
        self.pur_title_55.setObjectName("pur_title_55")
        self.pur_title_56 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_56.setGeometry(QtCore.QRect(150, 1570, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_56.setFont(font)
        self.pur_title_56.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_56.setWordWrap(True)
        self.pur_title_56.setObjectName("pur_title_56")
        self.pur_title_57 = QtWidgets.QLabel(self.sa_7_w)
        self.pur_title_57.setGeometry(QtCore.QRect(50, 1790, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_57.setFont(font)
        self.pur_title_57.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_57.setWordWrap(True)
        self.pur_title_57.setObjectName("pur_title_57")
        self.pushButton_110 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_110.setGeometry(QtCore.QRect(1170, 2000, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_110.setFont(font)
        self.pushButton_110.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_110.setObjectName("pushButton_110")
        self.pushButton_113 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_113.setGeometry(QtCore.QRect(1170, 2080, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_113.setFont(font)
        self.pushButton_113.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_113.setObjectName("pushButton_113")
        self.pushButton_116 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_116.setGeometry(QtCore.QRect(1170, 2170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_116.setFont(font)
        self.pushButton_116.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_116.setObjectName("pushButton_116")
        self.pushButton_119 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_119.setGeometry(QtCore.QRect(1170, 2250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_119.setFont(font)
        self.pushButton_119.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_119.setObjectName("pushButton_119")
        self.pushButton_120 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_120.setGeometry(QtCore.QRect(1170, 1720, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_120.setFont(font)
        self.pushButton_120.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_120.setObjectName("pushButton_120")
        self.pushButton_124 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_124.setGeometry(QtCore.QRect(1170, 1610, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_124.setFont(font)
        self.pushButton_124.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_124.setObjectName("pushButton_124")
        self.pushButton_126 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_126.setGeometry(QtCore.QRect(1170, 1500, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_126.setFont(font)
        self.pushButton_126.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_126.setObjectName("pushButton_126")
        self.pushButton_133 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_133.setGeometry(QtCore.QRect(1170, 1280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_133.setFont(font)
        self.pushButton_133.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_133.setObjectName("pushButton_133")
        self.pushButton_136 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_136.setGeometry(QtCore.QRect(1170, 1170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_136.setFont(font)
        self.pushButton_136.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_136.setObjectName("pushButton_136")
        self.pushButton_140 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_140.setGeometry(QtCore.QRect(1170, 1060, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_140.setFont(font)
        self.pushButton_140.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_140.setObjectName("pushButton_140")
        self.pushButton_142 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_142.setGeometry(QtCore.QRect(1170, 950, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_142.setFont(font)
        self.pushButton_142.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_142.setObjectName("pushButton_142")
        self.pushButton_143 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_143.setGeometry(QtCore.QRect(1170, 840, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_143.setFont(font)
        self.pushButton_143.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_143.setObjectName("pushButton_143")
        self.pushButton_152 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_152.setGeometry(QtCore.QRect(1170, 620, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_152.setFont(font)
        self.pushButton_152.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_152.setObjectName("pushButton_152")
        self.pushButton_153 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_153.setGeometry(QtCore.QRect(1170, 510, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_153.setFont(font)
        self.pushButton_153.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_153.setObjectName("pushButton_153")
        self.pushButton_155 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_155.setGeometry(QtCore.QRect(1170, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_155.setFont(font)
        self.pushButton_155.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_155.setObjectName("pushButton_155")
        self.pushButton_161 = QtWidgets.QPushButton(self.sa_7_w)
        self.pushButton_161.setGeometry(QtCore.QRect(1170, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_161.setFont(font)
        self.pushButton_161.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_161.setObjectName("pushButton_161")
        self.sa_step_7.setWidget(self.sa_7_w)
        self.stackedWidget.addWidget(self.bp_7)
        self.bp_8 = QtWidgets.QWidget()
        self.bp_8.setObjectName("bp_8")
        self.sa_step_8 = QtWidgets.QScrollArea(self.bp_8)
        self.sa_step_8.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_step_8.setWidgetResizable(True)
        self.sa_step_8.setObjectName("sa_step_8")
        self.sa_7_w_4 = QtWidgets.QWidget()
        self.sa_7_w_4.setGeometry(QtCore.QRect(0, 0, 1288, 1717))
        self.sa_7_w_4.setMinimumSize(QtCore.QSize(0, 1717))
        self.sa_7_w_4.setObjectName("sa_7_w_4")
        self.pushButton_217 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_217.setGeometry(QtCore.QRect(70, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_217.setFont(font)
        self.pushButton_217.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_217.setObjectName("pushButton_217")
        self.pushButton_220 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_220.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_220.setFont(font)
        self.pushButton_220.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_220.setObjectName("pushButton_220")
        self.label_25 = QtWidgets.QLabel(self.sa_7_w_4)
        self.label_25.setGeometry(QtCore.QRect(90, 250, 250, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_25.setObjectName("label_25")
        self.textBrowser = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser.setGeometry(QtCore.QRect(340, 250, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_26 = QtWidgets.QLabel(self.sa_7_w_4)
        self.label_26.setGeometry(QtCore.QRect(90, 330, 250, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.sa_7_w_4)
        self.label_27.setGeometry(QtCore.QRect(90, 460, 250, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.sa_7_w_4)
        self.label_28.setGeometry(QtCore.QRect(90, 540, 250, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.sa_7_w_4)
        self.label_29.setGeometry(QtCore.QRect(90, 650, 250, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.sa_7_w_4)
        self.label_30.setGeometry(QtCore.QRect(90, 760, 250, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.label_30.setObjectName("label_30")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(340, 330, 411, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_223 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_223.setGeometry(QtCore.QRect(20, 885, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_223.setFont(font)
        self.pushButton_223.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_223.setObjectName("pushButton_223")
        self.pushButton_226 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_226.setGeometry(QtCore.QRect(70, 995, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_226.setFont(font)
        self.pushButton_226.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_226.setObjectName("pushButton_226")
        self.pushButton_228 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_228.setGeometry(QtCore.QRect(120, 1215, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_228.setFont(font)
        self.pushButton_228.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_228.setObjectName("pushButton_228")
        self.pushButton_232 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_232.setGeometry(QtCore.QRect(120, 1105, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_232.setFont(font)
        self.pushButton_232.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_232.setObjectName("pushButton_232")
        self.pushButton_236 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_236.setGeometry(QtCore.QRect(20, 1325, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_236.setFont(font)
        self.pushButton_236.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_236.setObjectName("pushButton_236")
        self.pushButton_237 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_237.setGeometry(QtCore.QRect(70, 1435, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_237.setFont(font)
        self.pushButton_237.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_237.setObjectName("pushButton_237")
        self.pushButton_241 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_241.setGeometry(QtCore.QRect(70, 1545, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_241.setFont(font)
        self.pushButton_241.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_241.setObjectName("pushButton_241")
        self.pushButton_273 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_273.setGeometry(QtCore.QRect(70, 1655, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_273.setFont(font)
        self.pushButton_273.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_273.setObjectName("pushButton_273")
        self.pur_title_58 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_58.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_58.setFont(font)
        self.pur_title_58.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_58.setWordWrap(True)
        self.pur_title_58.setObjectName("pur_title_58")
        self.pur_title_59 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_59.setGeometry(QtCore.QRect(100, 140, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_59.setFont(font)
        self.pur_title_59.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_59.setWordWrap(True)
        self.pur_title_59.setObjectName("pur_title_59")
        self.pur_title_60 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_60.setGeometry(QtCore.QRect(50, 860, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_60.setFont(font)
        self.pur_title_60.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_60.setWordWrap(True)
        self.pur_title_60.setObjectName("pur_title_60")
        self.pur_title_61 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_61.setGeometry(QtCore.QRect(100, 970, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_61.setFont(font)
        self.pur_title_61.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_61.setWordWrap(True)
        self.pur_title_61.setObjectName("pur_title_61")
        self.pur_title_63 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_63.setGeometry(QtCore.QRect(150, 1080, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_63.setFont(font)
        self.pur_title_63.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_63.setWordWrap(True)
        self.pur_title_63.setObjectName("pur_title_63")
        self.pur_title_64 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_64.setGeometry(QtCore.QRect(150, 1190, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_64.setFont(font)
        self.pur_title_64.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_64.setWordWrap(True)
        self.pur_title_64.setObjectName("pur_title_64")
        self.pur_title_62 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_62.setGeometry(QtCore.QRect(50, 1300, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_62.setFont(font)
        self.pur_title_62.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_62.setWordWrap(True)
        self.pur_title_62.setObjectName("pur_title_62")
        self.pur_title_65 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_65.setGeometry(QtCore.QRect(100, 1410, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_65.setFont(font)
        self.pur_title_65.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_65.setWordWrap(True)
        self.pur_title_65.setObjectName("pur_title_65")
        self.pur_title_66 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_66.setGeometry(QtCore.QRect(100, 1520, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_66.setFont(font)
        self.pur_title_66.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_66.setWordWrap(True)
        self.pur_title_66.setObjectName("pur_title_66")
        self.pur_title_67 = QtWidgets.QLabel(self.sa_7_w_4)
        self.pur_title_67.setGeometry(QtCore.QRect(100, 1630, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_67.setFont(font)
        self.pur_title_67.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_67.setWordWrap(True)
        self.pur_title_67.setObjectName("pur_title_67")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_3.setGeometry(QtCore.QRect(340, 460, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(340, 540, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(340, 650, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(340, 760, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_7.setGeometry(QtCore.QRect(750, 250, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_8.setGeometry(QtCore.QRect(750, 460, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_9.setGeometry(QtCore.QRect(750, 760, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_10.setGeometry(QtCore.QRect(750, 650, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_10.setFont(font)
        self.textBrowser_10.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_11.setGeometry(QtCore.QRect(750, 330, 411, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_11.setFont(font)
        self.textBrowser_11.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.sa_7_w_4)
        self.textBrowser_12.setGeometry(QtCore.QRect(750, 540, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.textBrowser_12.setFont(font)
        self.textBrowser_12.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.pushButton_162 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_162.setGeometry(QtCore.QRect(1170, 1120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_162.setFont(font)
        self.pushButton_162.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_162.setObjectName("pushButton_162")
        self.pushButton_167 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_167.setGeometry(QtCore.QRect(1170, 1230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_167.setFont(font)
        self.pushButton_167.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_167.setObjectName("pushButton_167")
        self.pushButton_168 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_168.setGeometry(QtCore.QRect(1170, 1450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_168.setFont(font)
        self.pushButton_168.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_168.setObjectName("pushButton_168")
        self.pushButton_169 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_169.setGeometry(QtCore.QRect(1170, 1560, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_169.setFont(font)
        self.pushButton_169.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_169.setObjectName("pushButton_169")
        self.pushButton_172 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_172.setGeometry(QtCore.QRect(1170, 1670, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_172.setFont(font)
        self.pushButton_172.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_172.setObjectName("pushButton_172")
        self.pushButton_178 = QtWidgets.QPushButton(self.sa_7_w_4)
        self.pushButton_178.setGeometry(QtCore.QRect(1170, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_178.setFont(font)
        self.pushButton_178.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_178.setObjectName("pushButton_178")
        self.sa_step_8.setWidget(self.sa_7_w_4)
        self.stackedWidget.addWidget(self.bp_8)
        self.bp_9 = QtWidgets.QWidget()
        self.bp_9.setObjectName("bp_9")
        self.sa_step_9 = QtWidgets.QScrollArea(self.bp_9)
        self.sa_step_9.setGeometry(QtCore.QRect(0, 0, 1301, 1281))
        self.sa_step_9.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_step_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sa_step_9.setWidgetResizable(True)
        self.sa_step_9.setObjectName("sa_step_9")
        self.sa_7_w_5 = QtWidgets.QWidget()
        self.sa_7_w_5.setGeometry(QtCore.QRect(0, 0, 1288, 1794))
        self.sa_7_w_5.setMinimumSize(QtCore.QSize(0, 1794))
        self.sa_7_w_5.setObjectName("sa_7_w_5")
        self.pushButton_278 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_278.setGeometry(QtCore.QRect(20, 55, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_278.setFont(font)
        self.pushButton_278.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_278.setObjectName("pushButton_278")
        self.pushButton_271 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_271.setGeometry(QtCore.QRect(70, 165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_271.setFont(font)
        self.pushButton_271.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_271.setObjectName("pushButton_271")
        self.pushButton_281 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_281.setGeometry(QtCore.QRect(70, 275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_281.setFont(font)
        self.pushButton_281.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_281.setObjectName("pushButton_281")
        self.pushButton_286 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_286.setGeometry(QtCore.QRect(70, 385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_286.setFont(font)
        self.pushButton_286.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_286.setObjectName("pushButton_286")
        self.pushButton_287 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_287.setGeometry(QtCore.QRect(70, 495, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_287.setFont(font)
        self.pushButton_287.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_287.setObjectName("pushButton_287")
        self.pushButton_290 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_290.setGeometry(QtCore.QRect(120, 605, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_290.setFont(font)
        self.pushButton_290.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_290.setObjectName("pushButton_290")
        self.pushButton_295 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_295.setGeometry(QtCore.QRect(120, 715, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_295.setFont(font)
        self.pushButton_295.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_295.setObjectName("pushButton_295")
        self.pushButton_300 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_300.setGeometry(QtCore.QRect(70, 825, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_300.setFont(font)
        self.pushButton_300.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_300.setObjectName("pushButton_300")
        self.pushButton_302 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_302.setGeometry(QtCore.QRect(120, 1055, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_302.setFont(font)
        self.pushButton_302.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_302.setObjectName("pushButton_302")
        self.pushButton_303 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_303.setGeometry(QtCore.QRect(120, 945, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_303.setFont(font)
        self.pushButton_303.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_303.setObjectName("pushButton_303")
        self.pushButton_306 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_306.setGeometry(QtCore.QRect(120, 1165, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_306.setFont(font)
        self.pushButton_306.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_306.setObjectName("pushButton_306")
        self.pushButton_310 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_310.setGeometry(QtCore.QRect(120, 1605, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_310.setFont(font)
        self.pushButton_310.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_310.setObjectName("pushButton_310")
        self.pushButton_311 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_311.setGeometry(QtCore.QRect(70, 1275, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_311.setFont(font)
        self.pushButton_311.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_311.setObjectName("pushButton_311")
        self.pushButton_312 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_312.setGeometry(QtCore.QRect(120, 1495, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_312.setFont(font)
        self.pushButton_312.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_312.setObjectName("pushButton_312")
        self.pushButton_317 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_317.setGeometry(QtCore.QRect(120, 1385, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_317.setFont(font)
        self.pushButton_317.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_317.setObjectName("pushButton_317")
        self.pushButton_321 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_321.setGeometry(QtCore.QRect(20, 1725, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_321.setFont(font)
        self.pushButton_321.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_321.setObjectName("pushButton_321")
        self.pur_title_68 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_68.setGeometry(QtCore.QRect(50, 30, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_68.setFont(font)
        self.pur_title_68.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_68.setWordWrap(True)
        self.pur_title_68.setObjectName("pur_title_68")
        self.pur_title_69 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_69.setGeometry(QtCore.QRect(100, 140, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_69.setFont(font)
        self.pur_title_69.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_69.setWordWrap(True)
        self.pur_title_69.setObjectName("pur_title_69")
        self.pur_title_70 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_70.setGeometry(QtCore.QRect(100, 250, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_70.setFont(font)
        self.pur_title_70.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_70.setWordWrap(True)
        self.pur_title_70.setObjectName("pur_title_70")
        self.pur_title_71 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_71.setGeometry(QtCore.QRect(100, 360, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_71.setFont(font)
        self.pur_title_71.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_71.setWordWrap(True)
        self.pur_title_71.setObjectName("pur_title_71")
        self.pur_title_76 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_76.setGeometry(QtCore.QRect(100, 470, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_76.setFont(font)
        self.pur_title_76.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_76.setWordWrap(True)
        self.pur_title_76.setObjectName("pur_title_76")
        self.pur_title_77 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_77.setGeometry(QtCore.QRect(150, 580, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_77.setFont(font)
        self.pur_title_77.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_77.setWordWrap(True)
        self.pur_title_77.setObjectName("pur_title_77")
        self.pur_title_78 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_78.setGeometry(QtCore.QRect(150, 690, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_78.setFont(font)
        self.pur_title_78.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_78.setWordWrap(True)
        self.pur_title_78.setObjectName("pur_title_78")
        self.pur_title_79 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_79.setGeometry(QtCore.QRect(100, 800, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_79.setFont(font)
        self.pur_title_79.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_79.setWordWrap(True)
        self.pur_title_79.setObjectName("pur_title_79")
        self.pur_title_80 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_80.setGeometry(QtCore.QRect(150, 910, 1011, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_80.setFont(font)
        self.pur_title_80.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_80.setWordWrap(True)
        self.pur_title_80.setObjectName("pur_title_80")
        self.pur_title_81 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_81.setGeometry(QtCore.QRect(150, 1030, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_81.setFont(font)
        self.pur_title_81.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_81.setWordWrap(True)
        self.pur_title_81.setObjectName("pur_title_81")
        self.pur_title_82 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_82.setGeometry(QtCore.QRect(150, 1140, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_82.setFont(font)
        self.pur_title_82.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_82.setWordWrap(True)
        self.pur_title_82.setObjectName("pur_title_82")
        self.pur_title_83 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_83.setGeometry(QtCore.QRect(150, 1580, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_83.setFont(font)
        self.pur_title_83.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_83.setWordWrap(True)
        self.pur_title_83.setObjectName("pur_title_83")
        self.pur_title_84 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_84.setGeometry(QtCore.QRect(150, 1360, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_84.setFont(font)
        self.pur_title_84.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_84.setWordWrap(True)
        self.pur_title_84.setObjectName("pur_title_84")
        self.pur_title_85 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_85.setGeometry(QtCore.QRect(150, 1470, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_85.setFont(font)
        self.pur_title_85.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_85.setWordWrap(True)
        self.pur_title_85.setObjectName("pur_title_85")
        self.pur_title_86 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_86.setGeometry(QtCore.QRect(100, 1250, 1061, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_86.setFont(font)
        self.pur_title_86.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_86.setWordWrap(True)
        self.pur_title_86.setObjectName("pur_title_86")
        self.pur_title_87 = QtWidgets.QLabel(self.sa_7_w_5)
        self.pur_title_87.setGeometry(QtCore.QRect(50, 1690, 1111, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title_87.setFont(font)
        self.pur_title_87.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title_87.setWordWrap(True)
        self.pur_title_87.setObjectName("pur_title_87")
        self.pushButton_324 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_324.setGeometry(QtCore.QRect(1070, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_324.setFont(font)
        self.pushButton_324.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(119, 138, 219);\n"
"border: 1px solid black;")
        self.pushButton_324.setObjectName("pushButton_324")
        self.pushButton_166 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_166.setGeometry(QtCore.QRect(1170, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_166.setFont(font)
        self.pushButton_166.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_166.setObjectName("pushButton_166")
        self.pushButton_173 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_173.setGeometry(QtCore.QRect(1170, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_173.setFont(font)
        self.pushButton_173.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_173.setObjectName("pushButton_173")
        self.pushButton_175 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_175.setGeometry(QtCore.QRect(1170, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_175.setFont(font)
        self.pushButton_175.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_175.setObjectName("pushButton_175")
        self.pushButton_179 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_179.setGeometry(QtCore.QRect(1170, 620, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_179.setFont(font)
        self.pushButton_179.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_179.setObjectName("pushButton_179")
        self.pushButton_183 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_183.setGeometry(QtCore.QRect(1170, 730, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_183.setFont(font)
        self.pushButton_183.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_183.setObjectName("pushButton_183")
        self.pushButton_184 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_184.setGeometry(QtCore.QRect(1170, 960, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_184.setFont(font)
        self.pushButton_184.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_184.setObjectName("pushButton_184")
        self.pushButton_185 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_185.setGeometry(QtCore.QRect(1170, 1070, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_185.setFont(font)
        self.pushButton_185.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_185.setObjectName("pushButton_185")
        self.pushButton_186 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_186.setGeometry(QtCore.QRect(1170, 1180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_186.setFont(font)
        self.pushButton_186.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_186.setObjectName("pushButton_186")
        self.pushButton_187 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_187.setGeometry(QtCore.QRect(1170, 1400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_187.setFont(font)
        self.pushButton_187.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_187.setObjectName("pushButton_187")
        self.pushButton_188 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_188.setGeometry(QtCore.QRect(1170, 1510, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_188.setFont(font)
        self.pushButton_188.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_188.setObjectName("pushButton_188")
        self.pushButton_190 = QtWidgets.QPushButton(self.sa_7_w_5)
        self.pushButton_190.setGeometry(QtCore.QRect(1170, 1620, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_190.setFont(font)
        self.pushButton_190.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pushButton_190.setObjectName("pushButton_190")
        self.sa_step_9.setWidget(self.sa_7_w_5)
        self.stackedWidget.addWidget(self.bp_9)
        self.Gui_title = QtWidgets.QLabel(MainForm)
        self.Gui_title.setGeometry(QtCore.QRect(420, 10, 731, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.Gui_title.setFont(font)
        self.Gui_title.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.Gui_title.setScaledContents(False)
        self.Gui_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Gui_title.setObjectName("Gui_title")
        self.pur_title = QtWidgets.QLabel(MainForm)
        self.pur_title.setGeometry(QtCore.QRect(1160, 10, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.pur_title.setFont(font)
        self.pur_title.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid black;")
        self.pur_title.setText("")
        self.pur_title.setAlignment(QtCore.Qt.AlignCenter)
        self.pur_title.setObjectName("pur_title")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(MainForm)
        self.stackedWidget_2.setGeometry(QtCore.QRect(1730, 10, 821, 671))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.sa_FBD_0 = QtWidgets.QScrollArea(self.page)
        self.sa_FBD_0.setGeometry(QtCore.QRect(0, 0, 821, 671))
        self.sa_FBD_0.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(217, 225, 232);\n"
"")
        self.sa_FBD_0.setWidgetResizable(True)
        self.sa_FBD_0.setObjectName("sa_FBD_0")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 819, 669))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sa_FBD_0.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_2.addWidget(self.page)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(MainForm)
        self.stackedWidget_3.setGeometry(QtCore.QRect(1730, 690, 821, 671))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.sa_TBD_0 = QtWidgets.QScrollArea(self.page_3)
        self.sa_TBD_0.setGeometry(QtCore.QRect(0, 0, 781, 671))
        self.sa_TBD_0.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: #d9e1e8;")
        self.sa_TBD_0.setWidgetResizable(True)
        self.sa_TBD_0.setObjectName("sa_TBD_0")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 779, 669))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.sa_TBD_0.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_3.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.sa_TBD_1 = QtWidgets.QScrollArea(self.page_4)
        self.sa_TBD_1.setGeometry(QtCore.QRect(0, 0, 821, 671))
        self.sa_TBD_1.setStyleSheet("border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(217, 225, 232);\n"
"")
        self.sa_TBD_1.setWidgetResizable(True)
        self.sa_TBD_1.setObjectName("sa_TBD_1")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 819, 669))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.sa_TBD_1.setWidget(self.scrollAreaWidgetContents_3)
        self.stackedWidget_3.addWidget(self.page_4)

        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtWidgets.QApplication.translate("MainForm", "SAMG", None, -1))
        self.L_CT.setText(QtWidgets.QApplication.translate("MainForm", "Current Time          :", None, -1))
        self.T_time.setText(QtWidgets.QApplication.translate("MainForm", "HH:MM:SS", None, -1))
        self.T_time_flow.setText(QtWidgets.QApplication.translate("MainForm", "HH:MM:SS", None, -1))
        self.L_AT.setText(QtWidgets.QApplication.translate("MainForm", "SAMG Entry Time  :", None, -1))
        self.T_date.setText(QtWidgets.QApplication.translate("MainForm", "YYYY:MM:DD", None, -1))
        self.L_P.setText(QtWidgets.QApplication.translate("MainForm", "Plant                        :", None, -1))
        self.T_plant_label.setText(QtWidgets.QApplication.translate("MainForm", "Plant name", None, -1))
        self.L_CD.setText(QtWidgets.QApplication.translate("MainForm", "Current Date          :", None, -1))
        self.B_1.setText(QtWidgets.QApplication.translate("MainForm", "Ⅰ. 목적", None, -1))
        self.B_2.setText(QtWidgets.QApplication.translate("MainForm", "Ⅱ. 수행 조건", None, -1))
        self.B_3.setText(QtWidgets.QApplication.translate("MainForm", "Ⅲ. 예상 발전소 거동", None, -1))
        self.B_4.setText(QtWidgets.QApplication.translate("MainForm", "Ⅳ. 비상운전절차와의 관계", None, -1))
        self.B_5.setText(QtWidgets.QApplication.translate("MainForm", "Ⅴ. 이용 가능 수단 확인", None, -1))
        self.B_6.setText(QtWidgets.QApplication.translate("MainForm", "Ⅵ. 전략 수행 여부 결정", None, -1))
        self.B_7.setText(QtWidgets.QApplication.translate("MainForm", "Ⅶ. 전략 수행 방법 결정", None, -1))
        self.B_8.setText(QtWidgets.QApplication.translate("MainForm", "Ⅷ. 전략 수행", None, -1))
        self.B_9.setText(QtWidgets.QApplication.translate("MainForm", "Ⅸ. 전략 종결", None, -1))
        self.B_10.setText(QtWidgets.QApplication.translate("MainForm", "제어-01", None, -1))
        self.B_11.setText(QtWidgets.QApplication.translate("MainForm", "이전 지침서", None, -1))
        self.pushButton_17.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_5.setText(QtWidgets.QApplication.translate("MainForm", "증기발생기 급수 주입의 목적은 다음과 같다.", None, -1))
        self.pushButton_18.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_6.setText(QtWidgets.QApplication.translate("MainForm", "● Reactor Coolant System (RCS) 열 제거", None, -1))
        self.pushButton_23.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_26.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_29.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_32.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_72.setText(QtWidgets.QApplication.translate("MainForm", "● RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함", None, -1))
        self.pur_title_73.setText(QtWidgets.QApplication.translate("MainForm", "● 증기발생기 튜브의 크립 파손 방지", None, -1))
        self.pur_title_74.setText(QtWidgets.QApplication.translate("MainForm", "● 증기발생기로 방출된 핵분열생성물의 세정(Scrubbing)", None, -1))
        self.pur_title_75.setText(QtWidgets.QApplication.translate("MainForm", "● 증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급", None, -1))
        self.pushButton_118.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_123.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_128.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_135.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_137.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_36.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_34.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_38.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_39.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainForm", "구분", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainForm", "운전모드 구분", None, -1))
        self.label_31.setText(QtWidgets.QApplication.translate("MainForm", "발전소 상태 점검표", None, -1))
        self.label_32.setText(QtWidgets.QApplication.translate("MainForm", "A", None, -1))
        self.label_33.setText(QtWidgets.QApplication.translate("MainForm", "운전모드 1(출력운전), 2(기동), 3(고온대기)\n"
"운전모드 4(고온정지) - 증기발생기로 열을 제거 하고 있을 때", None, -1))
        self.label_34.setText(QtWidgets.QApplication.translate("MainForm", "운전모드 4(고온정지) - 정지냉각계통으로 열을 제거 하고 있을 때\n"
"운전모드 5(상온정지) - RCS에 대형 개구부가 존재하지 않을 때", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainForm", "발전소 상태", None, -1))
        self.label_35.setText(QtWidgets.QApplication.translate("MainForm", "o 정지냉각계통 운전조건까지 RCS 감압 및 냉각이 이루어지지 \n"
"않았으며, 증기발생기로 열을 제거하고 있는 발전소 상태", None, -1))
        self.pur_title_7.setText(QtWidgets.QApplication.translate("MainForm", "● 발전소 상태가 A 또는 B이고 어느 하나라도 증기발생기 수위가 협역수위 지시기로 68% 이하일 때", None, -1))
        self.pur_title_8.setText(QtWidgets.QApplication.translate("MainForm", "● 발전소 상태가 C이고 핵분열생성물의 방출이 있는 증기발생기 수위가 협역수위 지시기로68% 이하일 때", None, -1))
        self.label_36.setText(QtWidgets.QApplication.translate("MainForm", "B", None, -1))
        self.label_37.setText(QtWidgets.QApplication.translate("MainForm", "o 정지냉각계통 운전조건까지 RCS 감압 및 냉각이 이루어져 \n"
"정지냉각계통으로 열을 제거하고 있는 발전소 상태\n"
"o RCS에 대형 개구부(예: 가압기 Manway)가 존재하지 않는 \n"
"발전소 상태", None, -1))
        self.label_38.setText(QtWidgets.QApplication.translate("MainForm", "C", None, -1))
        self.label_39.setText(QtWidgets.QApplication.translate("MainForm", "D", None, -1))
        self.label_40.setText(QtWidgets.QApplication.translate("MainForm", "E", None, -1))
        self.label_41.setText(QtWidgets.QApplication.translate("MainForm", "운전모드 5(상온정지) - RCS에 대형 개구부가 존재하며 노즐댐이 \n"
"설치되지 않았을 때", None, -1))
        self.label_42.setText(QtWidgets.QApplication.translate("MainForm", "운전모드 5(상온정지) - 노즐댐이 설치되었을 때\n"
"운전모드 6(핵연료재장전) - 원자로용기 내에 핵연료가 위치할 때", None, -1))
        self.label_43.setText(QtWidgets.QApplication.translate("MainForm", "운전모드 6(핵연료재장전) - 원자로용기 내에 핵연료가 없을 때", None, -1))
        self.label_44.setText(QtWidgets.QApplication.translate("MainForm", "o RCS에 대형 개구부(예: 가압기 Manway)가 존재하며 저온관과 고온관에 노즐댐이 설치되어 있지 않는 발전소 상태", None, -1))
        self.label_45.setText(QtWidgets.QApplication.translate("MainForm", "o 증기발생기 1차측 정비용 출입구가 제거되고 이후 저온관과 \n"
"고온관에 노즐댐이 설치되어 있는 발전소 상태*\n"
"o 원자로용기 내에 핵연료가 위치하고 있거나 핵연료 재장전 \n"
"작업이 진행 중인 발전소 상태", None, -1))
        self.label_46.setText(QtWidgets.QApplication.translate("MainForm", "o 핵연료 인출 작업을 완료하고 원자로용기 내 모든 핵연료가 \n"
"사용후연료저장조로 이송된 발전소 상태", None, -1))
        self.pushButton_45.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_40.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_44.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_43.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_46.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_47.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_48.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_49.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_9.setText(QtWidgets.QApplication.translate("MainForm", "● 증기발생기 수위 상승", None, -1))
        self.pur_title_10.setText(QtWidgets.QApplication.translate("MainForm", "● 증기발생기 증기 유량 증가", None, -1))
        self.pur_title_11.setText(QtWidgets.QApplication.translate("MainForm", "● 노심 출구와 고온관의 온도 감소", None, -1))
        self.pur_title_12.setText(QtWidgets.QApplication.translate("MainForm", "● 증기발생기 튜브 상부에 수소 축적", None, -1))
        self.pushButton_52.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_53.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_54.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_56.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_58.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_62.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_14.setText(QtWidgets.QApplication.translate("MainForm", "● 상충성", None, -1))
        self.pur_title_13.setText(QtWidgets.QApplication.translate("MainForm", "비상운전절차서에는 급수가 있는 증기발생기가 있을 경우에 급수가 없는 증기발생기에는 급수를 주입하지 않고 있으나, 중대사고관리지침서에서는 증기발생기 튜브의 크립 파손을 방지하기 위하여 급수가 없는 증기발생기에도 급수 주입을 고려한다.", None, -1))
        self.pur_title_15.setText(QtWidgets.QApplication.translate("MainForm", "● 일치성", None, -1))
        self.pur_title_16.setText(QtWidgets.QApplication.translate("MainForm", "이 전략은 기능회복절차서 회복-06, “노심 및 RCS 열 제거”와 일치한다.\n"
" 증기발생기의 급속한 감압으로 발생할 수 있는 증기발생기에서의 불필요한 열응력 증가를 피하기 위하여 세심한 주의가 필요하며 정상적인 증기발생기 운전 절차도 이 지침에 적용될 수 있다.", None, -1))
        self.pushButton_65.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_66.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_68.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_79.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_81.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_89.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_96.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_101.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_103.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_109.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_112.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_114.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_117.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_121.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_125.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_129.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_131.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_134.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_145.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_163.setText(QtWidgets.QApplication.translate("MainForm", "단계 이동", None, -1))
        self.pur_title_18.setText(QtWidgets.QApplication.translate("MainForm", "1. 증기발생기에 급수를 주입하기 위한 유용한 수단을 파악한다.", None, -1))
        self.pur_title_19.setText(QtWidgets.QApplication.translate("MainForm", "가. 증기발생기 고압 급수 주입 경로의 이용가능성을 확인한다.", None, -1))
        self.pur_title_20.setText(QtWidgets.QApplication.translate("MainForm", "터빈 구동 보조급수 펌프 (AF-PP01A, AF-PP01B)", None, -1))
        self.pur_title_21.setText(QtWidgets.QApplication.translate("MainForm", "전동기 구동 보조급수 펌프 (AF-PP02A, AF-PP02B)", None, -1))
        self.pur_title_22.setText(QtWidgets.QApplication.translate("MainForm", "터빈 구동 주급수펌프 (FW-PP01, FW-PP02, FW-PP03)", None, -1))
        self.pur_title_23.setText(QtWidgets.QApplication.translate("MainForm", "기동용 급수 펌프 (FW-PP07)", None, -1))
        self.pur_title_24.setText(QtWidgets.QApplication.translate("MainForm", "나. 증기발생기 고압 급수 주입 수단이 하나라도 있으면 단계 3으로 간다.", None, -1))
        self.pur_title_25.setText(QtWidgets.QApplication.translate("MainForm", "다. 증기발생기 저압 급수 주입 경로의 이용 가능성을 확인한다.", None, -1))
        self.pur_title_26.setText(QtWidgets.QApplication.translate("MainForm", "급수 승압 펌프 (FW-PP04, FW-PP05, FW-PP06)", None, -1))
        self.pur_title_28.setText(QtWidgets.QApplication.translate("MainForm", "소방 펌프차", None, -1))
        self.pur_title_29.setText(QtWidgets.QApplication.translate("MainForm", "라. 증기발생기에 급수를 주입할 수단이 더이상 없으면 다음을 수행한다.", None, -1))
        self.pur_title_30.setText(QtWidgets.QApplication.translate("MainForm", "1) 증기발생기에 급수를 주입할 수 없는 원인을 밝힌다.", None, -1))
        self.pur_title_31.setText(QtWidgets.QApplication.translate("MainForm", "2) 증기발생기에 급수를 주입할 수 있는 수단을 복구할 수 있는 조치들의 우선 순위를 정하고,적절한 복구조치를\n"
"시작하도록 OSC 또는 주제어실에 지시한다.", None, -1))
        self.pur_title_32.setText(QtWidgets.QApplication.translate("MainForm", "3) 전략수행제어도로 돌아간다. 단 이 지침서가 다른 완화지침서 수행 도중에 발생한 부정적 영향을 완화하기\n"
"위하여 수행되었다면 이전 수행 중이던 완화지침서로 돌아간다.", None, -1))
        self.pur_title_33.setText(QtWidgets.QApplication.translate("MainForm", "2. 증기발생기를 감압하기 위한 유용한 수단을 파악한다.", None, -1))
        self.pur_title_34.setText(QtWidgets.QApplication.translate("MainForm", "터빈우회 복수기 밸브 (MS-V1001, MS-V1002, MS-V1003, MS-V1004, MS-V1005, MS-V1006)", None, -1))
        self.pur_title_35.setText(QtWidgets.QApplication.translate("MainForm", "터빈우회 대기 밸브 (MS-V1007, MS-V1008)", None, -1))
        self.pur_title_36.setText(QtWidgets.QApplication.translate("MainForm", "주증기 대기 방출 밸브 (MS-V171, MS-V172, MS-V173, MS-V174)", None, -1))
        self.pur_title_37.setText(QtWidgets.QApplication.translate("MainForm", "3. 발전소 상태가 A 또는 B인 경우에는 이용 가능한 증기발생기 급수 주입량이 붕괴열을 제거하기에 적당한가를 결정한다.", None, -1))
        self.pushButton_331.setText(QtWidgets.QApplication.translate("MainForm", "계산표", None, -1))
        self.pushButton_330.setText(QtWidgets.QApplication.translate("MainForm", "붙임 B", None, -1))
        self.pushButton_377.setText(QtWidgets.QApplication.translate("MainForm", "붙임 E", None, -1))
        self.pushButton_61.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_77.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_78.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_80.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_86.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_87.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_63.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_88.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_91.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_64.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_93.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_67.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_69.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_95.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_73.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_97.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_98.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_74.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_75.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_99.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_76.setText(QtWidgets.QApplication.translate("MainForm", "이용불가", None, -1))
        self.pushButton_100.setText(QtWidgets.QApplication.translate("MainForm", "이용가능", None, -1))
        self.pushButton_122.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_379.setText(QtWidgets.QApplication.translate("MainForm", "붙임 A", None, -1))
        self.pushButton_160.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_148.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_147.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_151.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainForm", "적용시점", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainForm", "급수가 고갈된 고온의 SG에 급수 \n"
"할 때\n"
"   ○ SG광역수위가 1% 이하", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainForm", "튜브가 파손되거나 누출이 있는 \n"
"SG로 급수할 때", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainForm", "급수가 고갈된 고온의 SG를 \n"
"감압할 때\n"
"  ○ 감압중인 SG 광역수위가 1% \n"
"이하이고, RCS 압력이 SG 압력 \n"
"이상일 때\n"
"  ○ 발전소 상태 A 또는 B 일때", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainForm", "부정적 영향", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainForm", "증기발생기 튜브 크립 파손", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("MainForm", "증기발생기 튜브 \n"
"누출부로 \n"
"핵분열생성물 방출", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainForm", "증기발생기 열충격", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainForm", "완화 조치", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainForm", "o 급수 주입의 초기에는 주입량을 초기 10분 동안 6.3 ℓ/s(22.7 m3/hr, 100 gpm) 정도로 제한한다.\n"
"(발전소 상태 A, B 또는 C에서 적용)\n"
"o SG 튜브 파손의 영향이 최소화되는 시간에 SG광역수위가 1%로 지시될 때까지 급수가 고갈된 단 1대의 SG에 급수를 주입한다.\n"
"(발전소 상태 A 또는 B에서 적용)\n"
"o SG 튜브 파손의 영향을 최소화하기 위해 격리가 가능한 SG에만 급수를 주입한다.\n"
"(발전소 상태 A 또는 B에서 적용)", None, -1))
        self.pur_title_27.setText(QtWidgets.QApplication.translate("MainForm", "4. 증기발생기 급수 주입에 의한 부정적인 영향을 파악하고 수용가능한지 평가한다.", None, -1))
        self.pur_title_38.setText(QtWidgets.QApplication.translate("MainForm", "가. 발생 가능한 부정적 영향을 파악하고 평가한다.", None, -1))
        self.pur_title_39.setText(QtWidgets.QApplication.translate("MainForm", "나. 부정적 영향이 문제되지 않는다고 판단되면 단계 6으로 간다.", None, -1))
        self.pur_title_40.setText(QtWidgets.QApplication.translate("MainForm", "다. 부정적 영향을 완화하기 위한 조치들을 평가한다.", None, -1))
        self.pushButton_165.setText(QtWidgets.QApplication.translate("MainForm", "단계 이동", None, -1))
        self.label_47.setText(QtWidgets.QApplication.translate("MainForm", "o 건전한 SG에만 급수하고 비등시킨다. (발전소 상태 A 또는 B에서 적용)\n"
"o SG 1차측에서 2차측으로 냉각재 누설을 최소화 하기 위하여 RCS를 \n"
"감압한다. (완화-02, “원자로냉각재계통 감압” 사용), (발전소 상태 A 또는 B에서 적용)\n"
"o 복수기로 증기를 배출하여 SG를 감압한다. \n"
"(발전소 상태 A, B 또는 C에서 적용)", None, -1))
        self.label_48.setText(QtWidgets.QApplication.translate("MainForm", "o SG 튜브 파손의 영향을 최소화하기 위하여 급수가 고갈되고 고온인 \n"
"증기발생기 1대만을 감압한다.\n"
"o SG 압력이 급수원의 차단수두 이하일 때 가능한한 빨리 급수 주입량을 \n"
"복구한다. SG에 급수주입 초기에는 주입량을 초기 10분 동안 \n"
"6.3 ℓ/s (22.7 m3/hr, 100 gpm)정도로 제한한다.\n"
"o RCS를 감압한다(완화-02, “원자로냉각재계통감압” 사용)", None, -1))
        self.pushButton_102.setText(QtWidgets.QApplication.translate("MainForm", "평가", None, -1))
        self.pushButton_105.setText(QtWidgets.QApplication.translate("MainForm", "평가", None, -1))
        self.pushButton_378.setText(QtWidgets.QApplication.translate("MainForm", "붙임 E", None, -1))
        self.pushButton_181.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_164.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_171.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_174.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_176.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_177.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_182.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_170.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_180.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_189.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_193.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_196.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_199.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_202.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_204.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_208.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_210.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("MainForm", "변수", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("MainForm", "유량", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("MainForm", "급수가 고갈된 증기발생기 수위", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("MainForm", "급수 주입 기간", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("MainForm", "증기발생기 감압", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("MainForm", "제한사항", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("MainForm", "o 급수가 고갈된 SG에 급수 주입시 급수 주입의 초기 10분 동안은 열응력 방지를 위해 주입량을 6.3 ℓ/s(22.7 m3/hr, 100 gpm) 이하로 제한한다.\n"
"o 급수원의 재충수율", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("MainForm", "o 증기발생기 압력이 급수원의 차단수두(Shut off Head)보다 낮게 되면 즉시 급수 주입을 시작한다.", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("MainForm", "o 급수원 재고량\n"
"o 펌프 성능유지를 위한 조건", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("MainForm", "o 증기발생기 1대 이상에 급수가 고갈되었을 때 증기발생기 광역 수위가 1%로 지시될 때까지 하나의 증기발생기에만 급수를 시작한다.", None, -1))
        self.pur_title_41.setText(QtWidgets.QApplication.translate("MainForm", "6. 증기발생기 급수 주입 경로를 선정한다.", None, -1))
        self.pur_title_42.setText(QtWidgets.QApplication.translate("MainForm", "가. 발전소 상태가 A 또는 B에서는 급수 주입을 할 증기발생기를 다음 순서에 따라 선정한다.", None, -1))
        self.pur_title_43.setText(QtWidgets.QApplication.translate("MainForm", "1) 건전한 증기발생기(들)", None, -1))
        self.pur_title_44.setText(QtWidgets.QApplication.translate("MainForm", "2) 고장난 증기발생기(들)", None, -1))
        self.pur_title_45.setText(QtWidgets.QApplication.translate("MainForm", "3) 튜브가 파손된 증기발생기(들)", None, -1))
        self.pur_title_46.setText(QtWidgets.QApplication.translate("MainForm", "나. 발전소 상태가 C에서는 핵분열생성물이 방출되는 증기발생기에만 급수를 주입한다.", None, -1))
        self.pur_title_47.setText(QtWidgets.QApplication.translate("MainForm", "다. 선정된 증기발생기의 급수 주입 경로를 다음 순서에 따라 결정한다.", None, -1))
        self.pur_title_48.setText(QtWidgets.QApplication.translate("MainForm", "3) 주급수 펌프(급수원 : 탈기기저장탱크)", None, -1))
        self.pur_title_49.setText(QtWidgets.QApplication.translate("MainForm", "1) 보조급수 펌프(급수원 : 보조급수저장탱크, CST 또는 원수저장탱크)", None, -1))
        self.pur_title_50.setText(QtWidgets.QApplication.translate("MainForm", "2) 기동용 급수펌프(급수원 : 탈기기저장탱크)", None, -1))
        self.pur_title_51.setText(QtWidgets.QApplication.translate("MainForm", "4) 급수 승압펌프(급수원 : 탈기기저장탱크)", None, -1))
        self.pur_title_52.setText(QtWidgets.QApplication.translate("MainForm", "5) 소방 펌프차(급수원 : 소방 탱크차)", None, -1))
        self.pur_title_53.setText(QtWidgets.QApplication.translate("MainForm", "라. 증기발생기 감압이 필요할 때는 다음 순서로 실시한다.", None, -1))
        self.pur_title_54.setText(QtWidgets.QApplication.translate("MainForm", "3) 주증기 대기 방출 밸브", None, -1))
        self.pur_title_55.setText(QtWidgets.QApplication.translate("MainForm", "1) 터빈우회 복수기 밸브", None, -1))
        self.pur_title_56.setText(QtWidgets.QApplication.translate("MainForm", "2) 터빈우회 대기 밸브", None, -1))
        self.pur_title_57.setText(QtWidgets.QApplication.translate("MainForm", "7. 증기발생기에 급수를 실시할 때의 제한사항들을 파악한다.", None, -1))
        self.pushButton_110.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_113.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_116.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_119.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_120.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_124.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_126.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_133.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_136.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_140.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_142.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_143.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_152.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_153.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_155.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_161.setText(QtWidgets.QApplication.translate("MainForm", "결정", None, -1))
        self.pushButton_217.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_220.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("MainForm", "선정된 증기발생기", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.a</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.a.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.4</p></body></html>", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("MainForm", "선정된 급수주입 경로", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("MainForm", "선정된 감압 경로", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("MainForm", "급수 주입시 제한사항", None, -1))
        self.label_29.setText(QtWidgets.QApplication.translate("MainForm", "특별히 감시해야 할 변수", None, -1))
        self.label_30.setText(QtWidgets.QApplication.translate("MainForm", "기타 필요한 정보", None, -1))
        self.textBrowser_2.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5</p></body></html>", None, -1))
        self.pushButton_223.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_226.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_228.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_232.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_236.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_237.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_241.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_273.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_58.setText(QtWidgets.QApplication.translate("MainForm", "8. 증기발생기 급수 주입을 실시하도록 주제어실에 지시한다.", None, -1))
        self.pur_title_59.setText(QtWidgets.QApplication.translate("MainForm", "가. 주제어실에 다음과 같은 정보를 제공한다.", None, -1))
        self.pur_title_60.setText(QtWidgets.QApplication.translate("MainForm", "9. 주제어실에서 증기발생기의 급수 주입을 성공적으로 실시하였는가 확인한다.", None, -1))
        self.pur_title_61.setText(QtWidgets.QApplication.translate("MainForm", "가. 감시하여야 할 변수는 다음과 같다.", None, -1))
        self.pur_title_63.setText(QtWidgets.QApplication.translate("MainForm", "o 광역수위 : 증가", None, -1))
        self.pur_title_64.setText(QtWidgets.QApplication.translate("MainForm", "o 압력 : 안정적 그리고 급수주입펌프 차단 수두 미만", None, -1))
        self.pur_title_62.setText(QtWidgets.QApplication.translate("MainForm", "10. 추가적인 완화 조치들이 필요한 지를 결정한다.", None, -1))
        self.pur_title_65.setText(QtWidgets.QApplication.translate("MainForm", "가. 실제로 발생한 부정적 영향을 파악한다.", None, -1))
        self.pur_title_66.setText(QtWidgets.QApplication.translate("MainForm", "나. 실제로 발생한 부정적 영향을 완화할 수 있는 조치들을 평가한다.", None, -1))
        self.pur_title_67.setText(QtWidgets.QApplication.translate("MainForm", "다. 발전소 상태 A 또는 B에서 부정적 영향을 완화할 수 있는 조치들이 있으면 수행하도록 주제어실에 지시한다.", None, -1))
        self.textBrowser_3.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p></body></html>", None, -1))
        self.textBrowser_4.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>", None, -1))
        self.textBrowser_5.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p></body></html>", None, -1))
        self.textBrowser_6.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-</p></body></html>", None, -1))
        self.textBrowser_7.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수동입력 가능</p></body></html>", None, -1))
        self.textBrowser_8.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수동입력 가능</p></body></html>", None, -1))
        self.textBrowser_9.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수동입력 가능</p></body></html>", None, -1))
        self.textBrowser_10.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수동입력 가능</p></body></html>", None, -1))
        self.textBrowser_11.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수동입력 가능</p></body></html>", None, -1))
        self.textBrowser_12.setHtml(QtWidgets.QApplication.translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">수동입력 가능</p></body></html>", None, -1))
        self.pushButton_162.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_167.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_168.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_169.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_172.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_178.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_278.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_271.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_281.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_286.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_287.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_290.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_295.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_300.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_302.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_303.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_306.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_310.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_311.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_312.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_317.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pushButton_321.setText(QtWidgets.QApplication.translate("MainForm", "●", None, -1))
        self.pur_title_68.setText(QtWidgets.QApplication.translate("MainForm", "12. 증기발생기 급수 주입으로 인한 장기 관심사항을 확인한다.", None, -1))
        self.pur_title_69.setText(QtWidgets.QApplication.translate("MainForm", "가. 장기 관심사항들은 붙임 D를 참조한다.", None, -1))
        self.pur_title_70.setText(QtWidgets.QApplication.translate("MainForm", "나. 장기 관심사항을 감시하기 위한 다른 변수들이 있는지 파악한다.", None, -1))
        self.pur_title_71.setText(QtWidgets.QApplication.translate("MainForm", "다. 추가적인 장기 관심사항들을 파악한다.", None, -1))
        self.pur_title_76.setText(QtWidgets.QApplication.translate("MainForm", "라. 가능한 회복 조치를 평가한다.", None, -1))
        self.pur_title_77.setText(QtWidgets.QApplication.translate("MainForm", "1) 권고된 범위를 벗어난 변수들에 대한 가능한 회복조치를 파악한다.", None, -1))
        self.pur_title_78.setText(QtWidgets.QApplication.translate("MainForm", "2) 적절한 회복조치를 선정한다.", None, -1))
        self.pur_title_79.setText(QtWidgets.QApplication.translate("MainForm", "마. 복구된 기기들을 사용할 필요가 있는가 평가한다.", None, -1))
        self.pur_title_80.setText(QtWidgets.QApplication.translate("MainForm", "1) 현재 전략을 대신하여 복구된 기기들을 (현재 사용하고 있지 않음)가지고 사용하여 대체 전략을 수행할 수 있는가를 결정한다.", None, -1))
        self.pur_title_81.setText(QtWidgets.QApplication.translate("MainForm", "2) 현재 전략을 대체전략으로 교체하는 데 따른 이점을 평가한다.", None, -1))
        self.pur_title_82.setText(QtWidgets.QApplication.translate("MainForm", "3) 대체전략을 수행하여야 되는가를 결정한다.", None, -1))
        self.pur_title_83.setText(QtWidgets.QApplication.translate("MainForm", "3) 현재 전략을 종료하고 대체 전략을 수행하기 위한 계통의 재배열", None, -1))
        self.pur_title_84.setText(QtWidgets.QApplication.translate("MainForm", "1) 전략이 수행된 후 그 전략이 장기간 지속되는 것을 확실하게 하기 위하여 취해야 하는 조치", None, -1))
        self.pur_title_85.setText(QtWidgets.QApplication.translate("MainForm", "2) 전략에서 요구하는 기능을 수행하기 위한 계통의 재배열", None, -1))
        self.pur_title_86.setText(QtWidgets.QApplication.translate("MainForm", "바. 회복조치를 수행하도록 주제어실에 지시한다.", None, -1))
        self.pur_title_87.setText(QtWidgets.QApplication.translate("MainForm", "13. 전략수행제어도로 돌아간다. 단 이 지침서가 다른 완화지침서 수행 도중에 발생한 부정적 영향을완화하기 위하여 수행되었다면 이전 수행 중이던 완화지침서로 돌아간다.", None, -1))
        self.pushButton_324.setText(QtWidgets.QApplication.translate("MainForm", "붙임 D", None, -1))
        self.pushButton_166.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_173.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_175.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_179.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_183.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_184.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_185.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_186.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_187.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_188.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.pushButton_190.setText(QtWidgets.QApplication.translate("MainForm", "확인", None, -1))
        self.Gui_title.setText(QtWidgets.QApplication.translate("MainForm", "완화-01 _ \"증기발생기 급수주입\"", None, -1))


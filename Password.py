# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Password.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius : 20px")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(50, 64, 70, 50)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.main_frame)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(19, 0, 9, 14)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.passcode_frame = QtWidgets.QFrame(self.frame_8)
        self.passcode_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passcode_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passcode_frame.setObjectName("passcode_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.passcode_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 16, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.passcode_label = QtWidgets.QLabel(self.passcode_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passcode_label.sizePolicy().hasHeightForWidth())
        self.passcode_label.setSizePolicy(sizePolicy)
        self.passcode_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.passcode_label.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    font: bold 25px;\n"
"}")
        self.passcode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.passcode_label.setObjectName("passcode_label")
        self.horizontalLayout_6.addWidget(self.passcode_label)
        self.verticalLayout_3.addWidget(self.passcode_frame)
        self.result_frame = QtWidgets.QFrame(self.frame_8)
        self.result_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.result_frame.setStyleSheet("background-color: transparent;")
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.result_frame)
        self.horizontalLayout_2.setContentsMargins(94, 20, 57, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.display_line = QtWidgets.QLineEdit(self.result_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_line.sizePolicy().hasHeightForWidth())
        self.display_line.setSizePolicy(sizePolicy)
        self.display_line.setMinimumSize(QtCore.QSize(0, 40))
        self.display_line.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(180, 180, 180);\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    font: bold 15px;\n"
"}")
        self.display_line.setText("")
        self.display_line.setReadOnly(True)
        self.display_line.setObjectName("display_line")
        self.horizontalLayout_2.addWidget(self.display_line)
        self.button_ok = QtWidgets.QPushButton(self.result_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ok.sizePolicy().hasHeightForWidth())
        self.button_ok.setSizePolicy(sizePolicy)
        self.button_ok.setMinimumSize(QtCore.QSize(50, 50))
        self.button_ok.setMaximumSize(QtCore.QSize(50, 70))
        self.button_ok.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    font: bold 15px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(180, 180, 180);\n"
"}")
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_2.addWidget(self.button_ok)
        self.verticalLayout_3.addWidget(self.result_frame)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.keypad_frame = QtWidgets.QFrame(self.main_frame)
        self.keypad_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_frame.setObjectName("keypad_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.keypad_frame)
        self.verticalLayout_6.setContentsMargins(30, -1, 30, 10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_123 = QtWidgets.QFrame(self.keypad_frame)
        self.frame_123.setStyleSheet("background-color: transparent;")
        self.frame_123.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_123.setObjectName("frame_123")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_123)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_1 = QtWidgets.QPushButton(self.frame_123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QtCore.QSize(80, 80))
        self.button_1.setMaximumSize(QtCore.QSize(80, 80))
        self.button_1.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_1.setObjectName("button_1")
        self.horizontalLayout_3.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.frame_123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QtCore.QSize(80, 80))
        self.button_2.setMaximumSize(QtCore.QSize(80, 80))
        self.button_2.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_2.setObjectName("button_2")
        self.horizontalLayout_3.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(self.frame_123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QtCore.QSize(80, 80))
        self.button_3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_3.setObjectName("button_3")
        self.horizontalLayout_3.addWidget(self.button_3)
        self.verticalLayout_6.addWidget(self.frame_123)
        self.frame_456 = QtWidgets.QFrame(self.keypad_frame)
        self.frame_456.setStyleSheet("background-color: transparent;")
        self.frame_456.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_456.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_456.setObjectName("frame_456")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_456)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_4 = QtWidgets.QPushButton(self.frame_456)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QtCore.QSize(80, 80))
        self.button_4.setMaximumSize(QtCore.QSize(80, 80))
        self.button_4.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_4.setObjectName("button_4")
        self.horizontalLayout.addWidget(self.button_4)
        self.button_5 = QtWidgets.QPushButton(self.frame_456)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QtCore.QSize(80, 80))
        self.button_5.setMaximumSize(QtCore.QSize(80, 80))
        self.button_5.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_5.setObjectName("button_5")
        self.horizontalLayout.addWidget(self.button_5)
        self.button_6 = QtWidgets.QPushButton(self.frame_456)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QtCore.QSize(80, 80))
        self.button_6.setMaximumSize(QtCore.QSize(80, 80))
        self.button_6.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_6.setObjectName("button_6")
        self.horizontalLayout.addWidget(self.button_6)
        self.verticalLayout_6.addWidget(self.frame_456)
        self.frame_789 = QtWidgets.QFrame(self.keypad_frame)
        self.frame_789.setStyleSheet("background-color: transparent;")
        self.frame_789.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_789.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_789.setObjectName("frame_789")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_789)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_7 = QtWidgets.QPushButton(self.frame_789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QtCore.QSize(80, 80))
        self.button_7.setMaximumSize(QtCore.QSize(80, 80))
        self.button_7.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_4.addWidget(self.button_7)
        self.button_8 = QtWidgets.QPushButton(self.frame_789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QtCore.QSize(80, 80))
        self.button_8.setMaximumSize(QtCore.QSize(80, 80))
        self.button_8.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_8.setObjectName("button_8")
        self.horizontalLayout_4.addWidget(self.button_8)
        self.button_9 = QtWidgets.QPushButton(self.frame_789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QtCore.QSize(80, 80))
        self.button_9.setMaximumSize(QtCore.QSize(80, 80))
        self.button_9.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_9.setObjectName("button_9")
        self.horizontalLayout_4.addWidget(self.button_9)
        self.verticalLayout_6.addWidget(self.frame_789)
        self.frame_0 = QtWidgets.QFrame(self.keypad_frame)
        self.frame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_0.setObjectName("frame_0")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_0 = QtWidgets.QPushButton(self.frame_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setMinimumSize(QtCore.QSize(80, 80))
        self.button_0.setMaximumSize(QtCore.QSize(80, 80))
        self.button_0.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 40px;\n"
"    border-color: rgb(180, 180, 180);\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 85, 85);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.button_0.setObjectName("button_0")
        self.horizontalLayout_5.addWidget(self.button_0)
        self.verticalLayout_6.addWidget(self.frame_0)
        self.verticalLayout_2.addWidget(self.keypad_frame)
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.passcode_label.setText(_translate("MainWindow", "Enter Passcode"))
        self.button_ok.setText(_translate("MainWindow", "OK"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_0.setText(_translate("MainWindow", "0"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_window(object):
    def setupUi(self, register_window, calendar_widget):
        register_window.setObjectName("register_window")
        register_window.resize(491, 390)
        self.centralwidget = QtWidgets.QWidget(register_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.register_button_back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setBold(True)
        font.setWeight(75)
        self.register_button_back.setFont(font)
        self.register_button_back.setObjectName("register_button_back")
        self.horizontalLayout_2.addWidget(self.register_button_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        #self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget = calendar_widget
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_2.addWidget(self.calendarWidget)
        register_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(register_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 26))
        self.menubar.setObjectName("menubar")
        register_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(register_window)
        self.statusbar.setObjectName("statusbar")
        register_window.setStatusBar(self.statusbar)

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "Register"))
        self.register_button_back.setText(_translate("register_window", "Back"))
        self.label.setText(_translate("register_window", "Register Well-being"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_window = QtWidgets.QMainWindow()
    ui = Ui_register_window()
    ui.setupUi(register_window)
    register_window.show()
    sys.exit(app.exec_())

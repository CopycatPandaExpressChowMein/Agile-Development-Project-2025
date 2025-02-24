# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Statistics.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statistics_window(object):
    def setupUi(self, statistics_window, algorithm_handler):
        statistics_window.setObjectName("statistics_window")
        statistics_window.resize(803, 828)
        self.centralwidget = QtWidgets.QWidget(statistics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statistics_button_back = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.statistics_button_back.setFont(font)
        self.statistics_button_back.setObjectName("statistics_button_back")
        self.horizontalLayout.addWidget(self.statistics_button_back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.statistics_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(40)
        self.statistics_label.setFont(font)
        self.statistics_label.setWordWrap(False)
        self.statistics_label.setObjectName("statistics_label")
        self.horizontalLayout_2.addWidget(self.statistics_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(250, 250))
        self.frame.setMaximumSize(QtCore.QSize(250, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_2.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 1, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_3.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_4.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout.addWidget(self.frame_4, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        statistics_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(statistics_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
        self.menubar.setObjectName("menubar")
        statistics_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(statistics_window)
        self.statusbar.setObjectName("statusbar")
        statistics_window.setStatusBar(self.statusbar)

        self.retranslateUi(statistics_window)
        QtCore.QMetaObject.connectSlotsByName(statistics_window)

    def retranslateUi(self, statistics_window):
        _translate = QtCore.QCoreApplication.translate
        statistics_window.setWindowTitle(_translate("statistics_window", "Statistics"))
        self.statistics_button_back.setText(_translate("statistics_window", "Back"))
        self.statistics_label.setText(_translate("statistics_window", "Statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statistics_window = QtWidgets.QMainWindow()
    ui = Ui_statistics_window()
    ui.setupUi(statistics_window)
    statistics_window.show()
    sys.exit(app.exec_())

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_welcome_window(object):
    def setupUi(self, welcome_window):
        welcome_window.setObjectName("welcome_window")
        welcome_window.resize(317, 239)
        welcome_window.setMinimumSize(QtCore.QSize(317, 239))
        welcome_window.setMaximumSize(QtCore.QSize(317, 239))
        self.centralwidget = QtWidgets.QWidget(parent=welcome_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_login_welcome = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_login_welcome.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.pushButton_login_welcome.setObjectName("pushButton_login_welcome")
        self.label_name_welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name_welcome.setGeometry(QtCore.QRect(40, 80, 81, 16))
        self.label_name_welcome.setObjectName("label_name_welcome")
        self.label_ATM_welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_ATM_welcome.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.label_ATM_welcome.setObjectName("label_ATM_welcome")
        self.lineEdit_pin_welcome = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_pin_welcome.setGeometry(QtCore.QRect(150, 110, 131, 20))
        self.lineEdit_pin_welcome.setAutoFillBackground(False)
        self.lineEdit_pin_welcome.setInputMask("")
        self.lineEdit_pin_welcome.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_pin_welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_pin_welcome.setObjectName("lineEdit_pin_welcome")
        self.label_account_pin_welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_account_pin_welcome.setGeometry(QtCore.QRect(40, 110, 71, 16))
        self.label_account_pin_welcome.setObjectName("label_account_pin_welcome")
        self.lineEdit_name_welcome = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_name_welcome.setGeometry(QtCore.QRect(150, 80, 131, 20))
        self.lineEdit_name_welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_name_welcome.setObjectName("lineEdit_name_welcome")
        self.label_welcome_welcome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_welcome_welcome.setGeometry(QtCore.QRect(30, 40, 261, 16))
        self.label_welcome_welcome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_welcome_welcome.setObjectName("label_welcome_welcome")
        welcome_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=welcome_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        welcome_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=welcome_window)
        self.statusbar.setObjectName("statusbar")
        welcome_window.setStatusBar(self.statusbar)

        self.retranslateUi(welcome_window)
        QtCore.QMetaObject.connectSlotsByName(welcome_window)

    def retranslateUi(self, welcome_window):
        _translate = QtCore.QCoreApplication.translate
        welcome_window.setWindowTitle(_translate("welcome_window", "MainWindow"))
        self.pushButton_login_welcome.setText(_translate("welcome_window", "Login"))
        self.label_name_welcome.setText(_translate("welcome_window", "Account Name:"))
        self.label_ATM_welcome.setText(_translate("welcome_window", "ATM"))
        self.label_account_pin_welcome.setText(_translate("welcome_window", "Account PIN:"))
        self.label_welcome_welcome.setText(_translate("welcome_window", "Welcome! Please enter your credentials."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome_window = QtWidgets.QMainWindow()
    ui = Ui_welcome_window()
    ui.setupUi(welcome_window)
    welcome_window.show()
    sys.exit(app.exec())
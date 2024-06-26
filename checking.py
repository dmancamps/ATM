# Form implementation generated from reading ui file 'checking.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_checking_window(object):
    def setupUi(self, checking_window):
        checking_window.setObjectName("checking_window")
        checking_window.resize(276, 305)
        checking_window.setMinimumSize(QtCore.QSize(276, 305))
        checking_window.setMaximumSize(QtCore.QSize(276, 305))
        self.centralwidget = QtWidgets.QWidget(parent=checking_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_balance_line_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_balance_line_checking.setGeometry(QtCore.QRect(34, 190, 91, 16))
        self.label_balance_line_checking.setObjectName("label_balance_line_checking")
        self.label_top_dollar_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_top_dollar_checking.setGeometry(QtCore.QRect(144, 190, 16, 16))
        self.label_top_dollar_checking.setObjectName("label_top_dollar_checking")
        self.radioButton_withdraw_checking = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_withdraw_checking.setGeometry(QtCore.QRect(44, 80, 82, 17))
        self.radioButton_withdraw_checking.setObjectName("radioButton_withdraw_checking")
        self.radioButton_deposit_checking = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_deposit_checking.setGeometry(QtCore.QRect(154, 80, 82, 17))
        self.radioButton_deposit_checking.setObjectName("radioButton_deposit_checking")
        self.label_amount_line_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_amount_line_checking.setGeometry(QtCore.QRect(44, 110, 47, 13))
        self.label_amount_line_checking.setObjectName("label_amount_line_checking")
        self.label_bottom_dollar_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_bottom_dollar_checking.setGeometry(QtCore.QRect(154, 110, 16, 16))
        self.label_bottom_dollar_checking.setObjectName("label_bottom_dollar_checking")
        self.lineEdit_dollar_amount_checking = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_dollar_amount_checking.setGeometry(QtCore.QRect(164, 110, 71, 20))
        self.lineEdit_dollar_amount_checking.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_dollar_amount_checking.setObjectName("lineEdit_dollar_amount_checking")
        self.pushButton_submit_checking = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_submit_checking.setGeometry(QtCore.QRect(30, 150, 75, 23))
        self.pushButton_submit_checking.setObjectName("pushButton_submit_checking")
        self.label_balance_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_balance_checking.setGeometry(QtCore.QRect(160, 190, 81, 20))
        self.label_balance_checking.setText("")
        self.label_balance_checking.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_balance_checking.setObjectName("label_balance_checking")
        self.label_ATM_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_ATM_checking.setGeometry(QtCore.QRect(130, 10, 47, 13))
        self.label_ATM_checking.setObjectName("label_ATM_checking")
        self.label_welcome_checking = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_welcome_checking.setGeometry(QtCore.QRect(50, 29, 181, 31))
        self.label_welcome_checking.setText("")
        self.label_welcome_checking.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_welcome_checking.setWordWrap(True)
        self.label_welcome_checking.setObjectName("label_welcome_checking")
        self.pushButton_exit_checking = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_exit_checking.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.pushButton_exit_checking.setObjectName("pushButton_exit_checking")
        checking_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=checking_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName("menubar")
        checking_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=checking_window)
        self.statusbar.setObjectName("statusbar")
        checking_window.setStatusBar(self.statusbar)

        self.retranslateUi(checking_window)
        QtCore.QMetaObject.connectSlotsByName(checking_window)

    def retranslateUi(self, checking_window):
        _translate = QtCore.QCoreApplication.translate
        checking_window.setWindowTitle(_translate("checking_window", "MainWindow"))
        self.label_balance_line_checking.setText(_translate("checking_window", "Balance:"))
        self.label_top_dollar_checking.setText(_translate("checking_window", "$"))
        self.radioButton_withdraw_checking.setText(_translate("checking_window", "Withdraw"))
        self.radioButton_deposit_checking.setText(_translate("checking_window", "Deposit"))
        self.label_amount_line_checking.setText(_translate("checking_window", "Amount:"))
        self.label_bottom_dollar_checking.setText(_translate("checking_window", "$"))
        self.lineEdit_dollar_amount_checking.setText(_translate("checking_window", "0"))
        self.pushButton_submit_checking.setText(_translate("checking_window", "Submit"))
        self.label_ATM_checking.setText(_translate("checking_window", "ATM"))
        self.pushButton_exit_checking.setText(_translate("checking_window", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    checking_window = QtWidgets.QMainWindow()
    ui = Ui_checking_window()
    ui.setupUi(checking_window)
    checking_window.show()
    sys.exit(app.exec())

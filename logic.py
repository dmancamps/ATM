from PyQt6.QtWidgets import *
from welcome import *
from option import *
from checking import *
from savings import *


class WelcomeLogic(QMainWindow, Ui_welcome_window):

    def __init__(self):
        super().__init__()
        self.saved_name = None
        self.saved_pin = None
        self.savings_balance = None
        self.checking_balance = None
        self.option_window = None
        self.reoccurrences = None
        self.setupUi(self)

        self.pushButton_login_welcome.clicked.connect(lambda: self.login())

    def login(self):
        entered_name = self.lineEdit_name_welcome.text().lower()
        entered_pin = self.lineEdit_pin_welcome.text()

        with open("saved_accounts", "r") as file:
            accounts = file.readlines()

        for account in accounts:
            data = account.strip().split(",")
            saved_name, saved_pin, checking_balance, savings_balance, reoccurrences = data
            if entered_name == saved_name.lower() and entered_pin == saved_pin:
                self.saved_name = saved_name
                self.saved_pin = saved_pin
                self.checking_balance = checking_balance
                self.savings_balance = savings_balance
                self.reoccurrences = reoccurrences
                self.open_option_window()

        self.label_welcome_welcome.setText("Credentials are incorrect. Please try again.")

    def open_option_window(self):
        self.option_window = OptionLogic(self.saved_name, self.saved_pin, self.checking_balance,
                                         self.savings_balance, self.reoccurrences)
        self.option_window.show()
        self.hide()


class OptionLogic(QMainWindow, Ui_option_window):
    def __init__(self, saved_name, saved_pin, checking_balance, savings_balance, reoccurrences):
        super().__init__()
        self.checking_window = None
        self.savings_window = None
        self.setupUi(self)
        self.saved_name = saved_name
        self.saved_pin = saved_pin
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        self.reoccurrences = reoccurrences

        self.pushButton_option.clicked.connect(self.enter)

    def enter(self):
        if self.radioButton_checking_option.isChecked():
            self.checking_window = CheckingLogic(self.saved_name, self.saved_pin, self.checking_balance,
                                                 self.savings_balance, self.reoccurrences)
            self.checking_window.show()
            self.hide()
        else:
            self.savings_window = SavingsLogic(self.saved_name, self.saved_pin, self.checking_balance,
                                               self.savings_balance, self.reoccurrences)
            self.savings_window.show()
            self.hide()


class CheckingLogic(QMainWindow, Ui_checking_window):
    def __init__(self, saved_name, saved_pin, checking_balance, savings_balance, reoccurrences):
        super().__init__()
        self.lineEdit_name_welcome = None
        self.saved_name = saved_name
        self.saved_pin = saved_pin
        self.checking_balance = float(checking_balance)
        self.savings_balance = float(savings_balance)
        self.reoccurrences = int(reoccurrences)
        self.setupUi(self)

        self.label_welcome_checking.setText(f"Welcome {self.saved_name}!")
        self.update()
        self.pushButton_submit_checking.clicked.connect(lambda: self.submit())
        self.pushButton_exit_checking.clicked.connect(lambda: self.exit())

    def update(self):
        formatted_balance_checking = "${:.2f}".format(self.checking_balance)
        self.label_balance_checking.setText(str(formatted_balance_checking))

    def submit(self):
        amount = float(self.lineEdit_dollar_amount_checking.text())
        if self.radioButton_withdraw_checking.isChecked():
            if 0 < amount <= self.checking_balance:
                self.checking_balance -= amount
                self.label_welcome_checking.setText(f"Withdrew ${amount}")
            else:
                self.label_welcome_checking.setText("Please enter valid amount.")
                return
        elif self.radioButton_deposit_checking.isChecked():
            if amount <= 0:
                self.label_welcome_checking.setText("Please enter valid amount.")
                return
            else:
                self.checking_balance += amount
                self.label_welcome_checking.setText(f"Deposited ${amount}")

        with open("saved_accounts", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for i, line in enumerate(lines):
                data = line.strip().split(",")
                saved_name, saved_pin, checking_balance, savings_balance, reoccurrences = data
                if saved_name.lower() == self.saved_name.lower():
                    lines[i] = (f"{self.saved_name},{self.saved_pin},{self.checking_balance:.2f},"
                                f"{self.savings_balance:.2f},{self.reoccurrences}\n")
            file.truncate(0)
            file.writelines(lines)
        self.update()

    def exit(self):
        self.close()


class SavingsLogic(QMainWindow, Ui_savings_window):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, saved_name, saved_pin, checking_balance, savings_balance, reoccurrences):
        super().__init__()
        self.saved_name = saved_name
        self.saved_pin = saved_pin
        self.checking_balance = float(checking_balance)
        self.savings_balance = float(savings_balance)
        self.reoccurrences = int(reoccurrences)
        self.setupUi(self)

        self.label_welcome_savings.setText(f"Welcome {self.saved_name}!")
        self.update()
        self.pushButton_submit_savings.clicked.connect(lambda: self.submit())
        self.pushButton_exit_savings.clicked.connect(lambda: self.exit())

    def update(self):
        formatted_balance_savings = "${:.2f}".format(self.savings_balance)
        self.label_balance_savings.setText(str(formatted_balance_savings))

    def submit(self):
        amount = float(self.lineEdit_dollar_amount_savings.text())
        if self.radioButton_withdraw_savings.isChecked():
            if amount > 0 and (self.savings_balance - amount) >= self.MINIMUM:
                if self.checkBox_recurring_savings.isChecked():
                    times = self.spinBox_times_savings.value()
                    total_amount = amount * times
                    self.savings_balance -= total_amount
                    self.label_welcome_savings.setText(f"Withdrew ${total_amount}")
                else:
                    self.savings_balance -= amount
                    self.label_welcome_savings.setText(f"Withdrew ${amount}")
            else:
                self.label_welcome_savings.setText("Please enter valid amount. Minimum is $100")
                return
        elif self.radioButton_deposit_savings.isChecked():
            if amount <= 0:
                self.label_welcome_savings.setText("Please enter valid amount.")
                return
            else:
                if self.checkBox_recurring_savings.isChecked():
                    times = self.spinBox_times_savings.value()
                    self.reoccurrences += times
                    total_amount = amount * times
                    self.savings_balance += total_amount
                    self.label_welcome_savings.setText(f"Deposited ${total_amount}")
                    if self.reoccurrences >= 6:
                        interest = self.savings_balance * SavingsLogic.RATE
                        self.savings_balance += interest
                        self.reoccurrences -= 6
                else:
                    self.reoccurrences += 1
                    self.savings_balance += amount
                    self.label_welcome_savings.setText(f"Deposited ${amount}")
                    if self.reoccurrences == 6:
                        interest = self.savings_balance * SavingsLogic.RATE
                        self.savings_balance += interest
                        self.reoccurrences = 0

        with open("saved_accounts", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for i, line in enumerate(lines):
                data = line.strip().split(",")
                saved_name, saved_pin, checking_balance, savings_balance, reoccurrences = data
                if saved_name.lower() == self.saved_name.lower():
                    lines[i] = (f"{self.saved_name},{self.saved_pin},{self.checking_balance:.2f},"
                                f"{self.savings_balance:.2f},{self.reoccurrences}\n")
            file.truncate(0)
            file.writelines(lines)
        self.update()

    def exit(self):
        self.close()

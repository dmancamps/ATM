from logic import *


def main():
    application = QApplication([])
    window_welcome = WelcomeLogic()
    window_welcome.show()
    application.exec()


if __name__ == "__main__":
    main()

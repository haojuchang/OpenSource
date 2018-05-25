from PyQt5.QtWidgets import QMainWindow, QApplication
import chatroomUI
import sys

class Main(QMainWindow, chatroomUI.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.setText("Send")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

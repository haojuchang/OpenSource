from PyQt5.QtWidgets import QMainWindow, QApplication
import layout
import sys

class Main(QMainWindow, layout.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.add.setText("Add")
        self.below_btn.setText("Del")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

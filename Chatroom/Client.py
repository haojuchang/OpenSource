import socket
import threading

from variables import *
from Example4_Qt import *
from PyQt5.QtCore import QThread, pyqtSignal

class FQThread(QThread):
    message = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.nickname = None
        self.FQ = FQThread()
        self.FQ.message.connect(self.appendMessage)
        self.GUI = Main()
        self.GUI.pushButton.clicked.connect(self.sendMessage)
        self.GUI.pushButton_2.clicked.connect(self.setNickname)
        self.GUI.up_pass.clicked.connect(self.updatePWD)
        self.GUI.show()
        self.GUI.lineEdit.setDisabled(True)
        self.GUI.pushButton.setDisabled(True)

    def sendMessage(self):
        try:
            if self.nickname is not None:
                myword = self.GUI.lineEdit.text()
                self.sock.send((self.nickname + ": " + myword).encode())
                self.GUI.textBrowser.append("\t\t\t" + myword + ":" + self.nickname)
                self.GUI.lineEdit.setText("")
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')

    def recvMessage(self):
        while True:
            try:
                received_messages = self.sock.recv(1024)

                if self.nickname is not None or received_messages == b'Welcome to chat room!':
                    received_messages = received_messages.decode()
                    self.FQ.message.emit(received_messages)
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

    def setNickname(self):
        self.nickname = self.GUI.lineEdit_2.text()
        message = '#NAME#,{nickname}'.format(nickname=self.nickname)
        self.GUI.textBrowser.append("Now Lets Chats, {nickname}".format(nickname=self.nickname))
        self.sock.send(message.encode())
        self.GUI.pushButton_2.setDisabled(True)
        self.GUI.lineEdit_2.setDisabled(True)
        self.GUI.lineEdit.setDisabled(False)
        self.GUI.pushButton.setDisabled(False)

    def appendMessage(self, data):
        self.GUI.textBrowser.append(data)

    def updatePWD(self):
        udPWD = self.GUI.ch_pass.text()
        message = '#updatePWD#,%s,%s' % (self.nickname, udPWD)
        self.sock.send(message.encode())

def main():
    app = QApplication(sys.argv)
	
    c = Client(HOST, 5555)
    th1 = threading.Thread(target=c.recvMessage)
    th1.setDaemon(True)
    th1.start()
    th1.join

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

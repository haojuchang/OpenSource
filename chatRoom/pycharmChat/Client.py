import socket
import threading

from variables import *

from Example4_Qt import *


class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.nickname = None

        app = QApplication(sys.argv)
        MainWindow = Main()
        MainWindow.show()
        sys.exit(app.exec_())

    def sendThreadFunc(self):
        while True:
            try:
                if self.nickname is not None:
                    myword = input()
                    self.sock.send((self.nickname + ": " + myword).encode())
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                received_messages = self.sock.recv(1024)

                if self.nickname is not None or received_messages == b'Welcome to chat room!':
                    received_messages = received_messages.decode()

                    print(received_messages)
            except ConnectionAbortedError:
                print('Server closed this connection!')
                break

            except ConnectionResetError:
                print('Server is closed!')
                break

    def setNickname(self):
        self.nickname = input("Input your nickname: ")
        message = '#NAME#,{nickname}'.format(nickname=self.nickname)
        print("Now Lets Chats, {nickname}".format(nickname=self.nickname))

        self.sock.send(message.encode())


def main():
    c = Client(HOST, 5550)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()

    c.setNickname()
    t.join()


if __name__ == "__main__":
    main()

# -*- encoding: utf-8 -*-
import socket
import threading
from datetime import datetime


class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                connection.send(b'Welcome to chat room!')
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
                self.tellOthers(connection.fileno(), "SYSTEM: in the chat room")

            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    now = datetime.now()
                    my_time = "   [%s:%s:%s]" % (now.hour, now.minute, now.second)
                    recvedMsg = recvedMsg + my_time
                    self.tellOthers(connNumber, recvedMsg)
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.tellOthers(myconnection.fileno(), "SYSTEM: someone leave the chat room")
                    self.mylist.remove(myconnection)
                except:
                    pass

                myconnection.close()
                return

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass


def main():
    s = Server('140.138.145.43', 5550)
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()


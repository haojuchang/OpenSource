# -*- encoding: utf-8 -*-
import socket
import threading
from datetime import datetime

from variables import *
from layout_Qt import *
from InitDB import *

class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        self.MDB = DataBaseChatRoom()
        self.GUI = Main()
        self.GUI.show()
        self.mylist = list()
        self.nicknames = dict()

        print('Server', socket.gethostbyname(host), 'listening ...')

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

                if '#NAME#' in recvedMsg:
                    nickname = recvedMsg.split(',')[1]
                    announcement = "SYSTEM: {nickname} in the chat room".format(nickname=nickname)
                    self.tellOthers(myconnection.fileno(), announcement)
                    self.nicknames[myconnection] = nickname
                elif '#updatePWD#' in recvedMsg:
                    user = recvedMsg.split(',')
                    self.MDB.updataUser(user[1], user[2])
                elif recvedMsg:
                    now = datetime.now()
                    my_time = "[{hour}:{minute}:{second}]".format(hour=now.hour, minute=now.minute, second=now.second)
                    recvedMsg = recvedMsg + "   " + my_time + "   " + str(len(self.mylist))
                    self.tellOthers(connNumber, recvedMsg)

            except (OSError, ConnectionResetError):
                try:
                    nickname = self.nicknames[myconnection]
                    announcement = "SYSTEM: {nickname} leave the chat room".format(nickname=nickname)
                    self.tellOthers(myconnection.fileno(), announcement)

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

    def showUsers(self):
        users = self.MDB.loadData()
        i = 1
        for u in users:
            self.GUI.showbox(u["uname"], i)
            i += 1

def main():
    s = Server(HOST, 5555)
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

import socket
import threading

class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.nickname = None

    def sendThreadFunc(self):
        while True:
            try:
                if self.nickname != None:
                    myword = input()
                    self.sock.send((self.nickname + ": " + myword).encode())
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                print(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')
    
    def setNickname(self, nickname):
        self.nickname = nickname
        # self.sock.send(b'2,%s' %nickname)

def main():
    c = Client('140.138.145.43', 5550)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    nickname = input("Input your nickname: ")
    c.setNickname(nickname)
    t.join()

if __name__ == "__main__":
    main()

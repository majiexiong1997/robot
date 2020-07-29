


import socket

class socket_server:
    def __init__(self):

        self.s = socket.socket()
        host = socket.gethostname()
        port = 11111
        self.s.bind((host, port))
        self.s.listen(5)
    def server(self):
        c, addr = self.s.accept()
        while True:
            ret = c.recv(1024).decode('utf-8')
            print(ret)
            if ret == 'bye':
                c.send(b'bye')
                break
            print('链接地址{}'.format(addr))
            msg = input('<<')
            c.send('发送消息{}'.format(msg).encode('utf-8'))





if __name__ == '__main__':
    socket_server().server()

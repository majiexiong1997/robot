


# import socket
#
# class socket_server:
#     def __init__(self):
#
#         self.s = socket.socket()
#         host = socket.gethostname()
#         port = 11111
#         self.s.bind((host, port))
#         self.s.listen(5)
#     def server(self):
#         c, addr = self.s.accept()
#         while True:
#             ret = c.recv(1024).decode('utf-8')
#             print(ret)
#             if ret == 'bye':
#                 c.send(b'bye')
#                 break
#             print('链接地址{}'.format(addr))
#             msg = input('<<')
#             c.send('发送消息{}'.format(msg).encode('utf-8'))
#
#
#
#
#
# if __name__ == '__main__':
#     socket_server().server()
from config.yaml_loding import *

r = read_robot().yaml_load('./config/robot_list.yml')
print(r)
for i in range(0,100):
    account = 'admin' + str(i)
    password = 'test' + str(i)
    set_dict = {
        'robot{}'.format(i):
            [account,password]
    }
    read_robot().yaml_write('./config/robot_list.yml',set_dict)
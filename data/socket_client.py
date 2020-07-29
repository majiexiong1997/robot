import socket
from log.test_log import *

class SocketClient():
    def __init__(self, host=socket.gethostname(), port=11111):
        '''
        :param host: 地址
        :param port: 端口
        :param connect: 当前链接状态
        :param client_value:  最大连接数
        :param coding: 编码格式
        :param size : 收发数据大小
        '''
        self.host = host
        self.port = port
        self.connect = False
        self.client_value = 5
        self.size = 1024
        self.coding = 'utf-8'

        self.sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sc.connect((self.host, self.port))

    def connect_to(self):
        '''链接服务器'''
        try:
            if not self.connect:
                while True:
                    self.send_msg()
                    self.get_msg()
                    self.connect = True
                    if self.ret == "bye":
                        self.broken_link()
                        break
            else:
                self.error()
        except:
            pass


    def broken_link(self):
        '''断开链接'''
        if self.connect:
            self.sc.close()
            LOG.debug('已断开链接')

    def check_broken_link(self):
        '''检查是否断开链接'''
        if not self.connect:
            self.connect_to()
        else:
            LOG.debug('当前已链接服务器')

    def send_msg(self):
        '''发送消息'''
        info = input('>>')
        self.sc.send(info.encode(self.coding))

    def get_msg(self):
        '''接收消息'''
        self.ret = self.sc.recv(self.size).decode(self.coding)
        print(self.ret)

    def error(self):
        '''报错处理'''
        LOG.error('异常错误，请查看配置')
        pass


if __name__ == '__main__':
    SocketClient().connect_to()

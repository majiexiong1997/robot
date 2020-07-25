
class robot:

    def __init__(self,account,password,server_ip,server_port):

        self.m_account = account  # 账号
        self.m_password = password  # 密码
        self.m_account_id = 0  # 账号id
        self.is_new = True  # 是否未登陆
        self.login_index = 0  # 登陆序号
        self.m_server_ip = server_ip  # 服务器地址
        self.m_server_port = server_port  # 服务器端口
        self.m_connect = False  # 链接对象
        self.robot_list = [
            self.m_connect ,
            self.m_password,
            self.m_account_id,
            self.is_new,
            self.login_index,
            self.m_server_ip,
            self.m_server_port,
            self.m_connect
        ]
    def get_robot(self):
        for j in self.robot_list:
            print(j)



if __name__ == '__main__':
    robot(1,1,1,1).get_robot()



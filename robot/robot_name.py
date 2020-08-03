from config.yaml_loding import *
from config.robot_config import *
from data.mysql_db import db_connect
from log.test_log import *
from game.login_module import *
from timeit import timeit
from config.frame_config import *


class Robot(db_connect):
    '''机器人实例
        account_list 账号列表
        password_list 密码列表
        robot_list 机器人列表
    '''
    account_list = []
    password_list = []
    robot_list = []

    def __init__(self):
        '''
        :param
            'login_index'   # 机器人序号
            'm_connect'     # 链接状态
            'm_account'     # 账号
            'm_password'    # 密码
            'm_account_id'  # 账号ID
            'is_new': True  #是否未登陆过
            'm_server_ip'   # 服务器IP
            'm_server_port' # 服务器端口
        '''
        self.robot_list = []
        self.robot_dict = {
            'login_index': 0,
            'm_connect': False,
            'm_account': '',
            'm_password': '',
            'm_account_id': 0,
            'is_new': True,
            'm_server_ip': config_table['server_ip'],
            'm_server_port': config_table['server_port'],
            'action_now': 'off_login'

        }
        '''机器人行为'''
        self.action_type = 0  #行为类型
        self.action_step = 0  #当前行为步骤
        self.module_step = 0

    def __len__(self):
        return len(self.robot_dict)

    def __getitem__(self, item):
        return self.robot_dict[item]

    def __setitem__(self, key, value):
        self.robot_dict[key] = value

    def __delitem__(self, key):
        del self.robot_dict[key]

    def on_robot(self):
        '''输入机器人数量
        :return  start_index 起始值
                 end_index 结束值
        '''
        self.start_index = int(input('输入开始的机器人数量'))
        self.end_index = int(input('输入结束的机器人数量'))
        try:
            if self.start_index > self.end_index:
                LOG.error('起始数字比end_index大，重新输入')

            return self.start_index, self.end_index
        except:
            pass

    def read_robot(self):
        '''读取配置中机器人
        :return
                account_list  #机器人账号
                password_list #机器人密码
        '''
        yaml_type = yaml.safe_load(open('../config/robot_list.yml'))
        robot_list = yaml_type
        for i in robot_list:
            self.account_list.append(robot_list[i][0])
            self.password_list.append(robot_list[i][1])

        return self.account_list, self.password_list

    def create_robot(self):
        '''创建机器人'''
        self.on_robot()
        self.read_robot()
        try:
            if self.end_index > len(self.account_list):
                LOG.error('没有那么多账号')
            else:
                for i in range(self.start_index, self.end_index):
                    test = self.robot_dict.copy()
                    test['login_index'] = i
                    test['m_account'] = self.account_list[i]
                    test['m_password'] = self.password_list[i]
                    self.robot_list.append(test)
        except:
            print('未知异常')

    def create_robot_account(self, account, password):
        pass


    def robot_start(self):
        '''启动机器人'''
        self.create_robot()
        for robot in self.robot_list:
            try:
                if robot['is_new']:
                    login().login_req()
                    LOG.debug('启动所有机器人，当前登陆机器人{}'.format(robot['login_index']))
                    robot['is_new'] = False
                    robot['action_now'] = 'login'
                else:
                    print('当前账号已登录')
            except:
                pass

    def robot_stop(self):
        '''关闭机器人'''
        for robot in self.robot_list:
            try:
                if not robot['is_new']:
                    login().login_quit()
                    LOG.debug('关闭所有机器人,当前退出机器人{}'.format(robot['login_index']))
                    robot['is_new'] = True
                    robot['action_now'] = 'off_login'
                else:
                    print('当前账号已退出')
            except:
                pass
    def robot_remove(self):
        '''
        移除指定机器人
        :return:
        '''
        remove_index = int(input('输入需要删除的机器人')) - 1
        self.robot_list.pop(remove_index)
        return self.robot_list
    def robot_clear(self):
        '''
        删除所有机器人
        :return:
        '''
        return self.robot_list.clear()



    def robot_start_action(self):
        '''机器人开始行为'''
        self.robot_start()
        print(self.robot_list)
        for robot in self.robot_list:
            if not robot['is_new']:
                robot['action_now'] = action_type['start_script']
        print(self.robot_list)


    def robot_stop_action(self):
        '''机器人停止行为'''
        # self.robot_stop()
        for robot in self.robot_list:
            if not robot['is_new']:
                robot['action_now'] = action_type['end_script']

    def robot_start_module(self):
        '''机器人开始模块运行'''
        for robot in self.robot_list:
            if not robot['is_new']:
                robot['module_now'] = action_type['start_module']

    def robot_stop_module(self):
        '''机器人停止模块运行'''
        for robot in self.robot_list:
            if not robot['is_new']:
                robot['module_now'] = action_type['end_module']




if __name__ == '__main__':


    # robot.robot_start()
    # print(robot.robot_list)
    # robot.robot_start_action()
    # print(robot.robot_list)
    # robot.robot_stop_action()
    # print(robot.robot_list)
    Robot().robot_start_action()






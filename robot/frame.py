from config.frame_config import *
from log.test_log import LOG
from robot.robot_name import *

robot = Robot()


class frame_action():
    all_action_scripts = {}  # 所有行为集合
    all_action_modules = {}  # 所有功能模块集合
    runtime_data = []

    def __init__(self):

        pass

    def msg_process(self, robot):
        pass

    def get_action_list(self,action_list:dict):
        '''

        :param action_list:  获取所有行为
        :return:
        '''
        for i,j in action_list.items():
            self.all_action_scripts[i] = j
        print(self.all_action_scripts)
        return self.all_action_scripts

    def get_module_list(self,module_list:dict):
        '''

        :param module_list:  获取所有模块
        :return:
        '''
        for i,j in module_list.items():
            self.all_action_modules[i] = j
        return self.all_action_modules

    def clear_action_list(self):
        '''
        清除所有行为
        :return:
        '''
        self.all_action_scripts.clear()
        return self.all_action_scripts

    def clear_module_list(self):
        '''
        清除所有模块
        :return:
        '''
        self.all_action_modules.clear()
        return self.all_action_modules

    def get_action(self, need_action):
        '''

        :param need_action: 获取需要的行为状态
        :return:
        '''

        for i,j in self.all_action_scripts:

            if need_action == i:
                return need_action
            else:
                return LOG.error('找不到这个行为动作 >> {}'.format(need_action))

    def get_next_action(self, need_action):
        '''

        :return:返回下一个动作的机器人
        '''

        action = self.get_action(need_action)
        for robot_value in robot.robot_list:
            robot_value['action_now'] = action
        return robot.robot_list


    def get_module(self, need_module):
        '''
        获取对应模块

        :return:
        '''
        for i in self.all_action_modules:
            if need_module == i:
                return need_module
            else:
                return LOG.error('找不到当前模块 >> {}'.format(need_module))

    def get_next_module(self, need_module):
        '''

        :param need_module:  需要模块
        :return: 返回下一个模块的机器人
        '''

        module = self.get_action(need_module)
        for robot_value in robot.robot_list:
            robot_value['module_now'] = module

        return robot.robot_list

    def clear_module(self):
        '''
        清空当前模块动作
        :return:
        '''
        for robot_value in robot.robot_list:
            robot_value['module_now'] = 'init_module'
        return robot.robot_list

    def init_action(self):
        '''
        重置行为
        :return:
        '''
        for robot_value in robot.robot_list:
            robot_value['action_now'] = 'init_action'
        return robot.robot_list

    def init_module(self):
        '''
        停止行为时或者重置行为时，重置模块
        :return:
        '''
        robot.robot_stop_action()
        for robot_value in robot.robot_list:
            if robot_value['action_now'] == 'end_script' or robot_value['action_now'] == 'init_action':
                robot_value['module_now'] = 'init_module'

        return robot.robot_list
    def insert_action(self,insert_action_key,insert_action_value):
        '''
        插入行为
        :return:
        '''
        self.all_action_scripts[insert_action_key] = insert_action_value
        return self.all_action_scripts

    def insert_module(self,insert_module_key,insert_module_value):
        '''
        插入新的模块
        :return:
        '''
        self.all_action_modules[insert_module_key] = insert_module_value
        return self.all_action_modules




if __name__ == '__main__':
    frame_action().get_action_list(action_result)
    frame_action().insert_action('test','123')
    frame_action().get_action_list(action_result)





import yaml

class read_robot():
    def yaml_load(self,yaml_file):
        '''
        :param yaml_file: 需要读取文件
        :return: 读取后数据
        '''
        yaml_type = yaml.safe_load(open(yaml_file))
        return yaml_type

    def yaml_write(self,yaml_file,data):
        '''
        :param yaml_file: 需要写入文件
        :param data: 需要传入数据
        :return:
        '''
        fw = open(yaml_file,'a',encoding='utf-8')
        yaml.dump(data,fw)














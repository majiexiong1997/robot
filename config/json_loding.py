import json

class JsonLoad:
    def json_load(self,json_file):
        '''

        :param json_file:  需要读取json文件
        :return: 返回json数据
        '''
        with open(json_file,'r') as load_f:
            load_dict = json.load(load_f)
            return load_dict
    def json_dump(self,json_file,data):
        '''

        :param json_file: 需要写入json文件
        :param data: 需要写入的数据
        '''
        with open(json_file,'w') as dump_f:
            json.dump(data,dump_f)

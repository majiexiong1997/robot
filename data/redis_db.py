from random import choice

from redis.connection import BlockingConnectionPool
from redis import Redis

redis_db = {
    'host': '127.0.0.1',
    'post': 6379,

}


class RedisClient:
    '''
    redis 功能二次封装
    '''

    def __init__(self, **kwargs):
        '''
        :param kwargs: 数据库配置，如果设置密码了请在传入字典中加 password : xxx
        '''

        self.__conn = Redis(connection_pool=BlockingConnectionPool(decode_responses=True, **kwargs))
        print(self.__conn)
        self.name = 'root'

    def get_key(self):
        '''
        :return: 当前hash内所有key
        '''
        proxies = self.__conn.hkeys(self.name)
        if proxies == []:
            print('查询不到,检查key值是否正确，当前key >> {}'.format(self.name))
            return False
        else:
            print('当前hash表的key值如下 >> {}'.format(proxies))
            return proxies

    def get_dict(self):
        '''
        :return: 返回当前表的所有数据
        '''
        proxies = self.__conn.hgetall(self.name)
        if proxies == {}:
            print('查询不到,检查key值是否正确，当前key >> {}'.format(self.name))
            return False
        else:
            print('当前字典 >> {}'.format(proxies))
            return proxies

    def put(self, key, value):
        '''
        写入键值对
        :return:
        '''
        data = self.__conn.hset(self.name, key, value)
        return data

    def pop(self):
        '''弹出并删除第一个hash值，并删除该键值对
        :return : 弹出的hash值
        '''
        proxies = self.__conn.hkeys(self.name)

        for proxy in proxies:
            proxy_info = self.__conn.hget(self.name, proxy)
            self.__conn.hdel(self.name, proxy)
            return proxy_info
        else:
            return False

    def delete(self, key):
        '''
        :param key: 对应key值
        :return: 查不到无法删除返回false
        '''
        proxies = self.__conn.hdel(self.name, key)
        if proxies == 0:
            print('当前hash表 >> {} 中查不到这个键'.format(self.name))
            return False
        else:
            print('已删除')

    def exists(self, key):
        '''
        :return: 判断值是否存在，存在返回true 不存在返回false
        '''
        proxies = self.__conn.hexists(self.name, key)
        if proxies:
            return True
        else:
            return False

    def clear(self):
        '''
        清除当前表
        :return:
        '''
        return self.__conn.delete(self.name)

    def get_count(self):
        '''
        统计表内键值对数量
        :return:
        '''
        return self.__conn.hlen(self.name)

    def change_table(self, name):
        '''
        切换操作表
        :param name:
        :return:
        '''
        self.name = name
    def info(self):

        info = self.__conn.info()
        for i,j in info.items():
            print(i,j)


if __name__ == '__main__':
    RedisClient().info()
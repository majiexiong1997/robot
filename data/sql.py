import hashlib

import pymysql

from config.robot_config import config_table
from log.test_log import *


class db_connect:
    '''数据库连接'''
    game_connect = False

    def __init__(self):
        self.game_connect = False
        self.config = config_table
        try:
            LOG.debug('>>正在链接游戏数据库：{},{} 账号 = {},密码 = {},库 = {}'.format(self.config['db_game_dsn'],
                                                                    self.config['db_game_port'],
                                                                    self.config['db_game_user'],
                                                                    self.config['db_game_pswd'],
                                                                    self.config['db_game_db']))

            self.db = pymysql.connect(self.config['db_game_dsn'], self.config['db_game_user']
                                                , self.config['db_game_pswd'], self.config['db_game_db'])
            self.cursor = self.db.cursor()
            self.game_connect = True


        except Exception as e:
            LOG.error('>>链接游戏数据库失败：{},{} 账号 = {},密码 = {},库 = {},错误信息{}'.format(self.config['db_game_dsn'],
                                                                           self.config['db_game_port'],
                                                                           self.config['db_game_user'],
                                                                           self.config['db_game_pswd'],
                                                                           self.config['db_game_db'],
                                                                           e))

    def catch_robot(self, account, password):
        '''查询'''
        try:
            sql = 'SELECT * FROM game.account WHERE account={}'.format(account)
            self.cursor.execute(sql)
            list_cat = []
            list_cat.append(self.cursor.fetchall())

        except Exception as e:
            print("查询数据失败{}".format(e))
            self.db.rollback()

    def create_robot(self, id , account, password):
        md5 = hashlib.md5()
        md5.update(password)
        str_password = md5.hexdigest()
        try:
            sql = 'INSERT INTO account(id,account,password,gm) values(%d,%s,%s,1000)'.format(id, account, str_password)
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            LOG.error('dawdawrfaf')
            self.db.rollback()


    def create_robot_account(self,account,password):
        if not self.game_connect :
            LOG.error('未连接数据库')
            pass



if __name__ == '__main__':
    db_connect()
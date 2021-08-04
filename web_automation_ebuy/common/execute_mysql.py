# -*- coding: utf-8 -*-


import pymysql
from common.logger import output_log
from data import common_data


class ExecuteMysql(object):

    def __init__(self):
        # 连接数据库
        self.con = pymysql.connect(
            host=common_data.host,
            port=3306,
            user=common_data.user,
            password=common_data.password,
            database=common_data.database,
            charset="utf8")
        output_log.info('数据库连接成功')
        # 创建游标
        self.cur = self.con.cursor()

    def find_one(self, sql):
        output_log.info('正在执行查询数据库, sql --> {}'.format(sql))
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据，并返回查询结果
        self.con.commit()
        res = self.cur.fetchone()
        output_log.info('数据库查询成功, 查询结果 --> {}'.format(res))
        return res

    def find_many(self, sql, number):
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据，并返回查询结果
        self.con.commit()
        return self.cur.fetchmany(number)

    def find_all(self, sql):
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据，并返回查询结果
        self.con.commit()
        return self.cur.fetchall()

    def find_count(self, sql):
        count = self.cur.execute(sql)
        self.con.commit()
        return count

    def close(self):
        self.con.close()


if __name__ == '__main__':

    db = ExecuteMysql()
    # sql = "SELECT COUNT(id) FROM ap_projects WHERE is_delete=0;"
    # sql = "SELECT * FROM ap_projects WHERE name='微信';"
    # res = db.find_one(sql=sql)
    # create_time, update_time = res[0], res[1]
    # create_time = str(create_time).split('.')[0]
    # print(create_time, type(create_time))
    # res[0] = create_time
    # print(res)
    # id, role_id, create_time = db.find_one(sql=sql)
    # print(id, role_id, create_time)
    # print(type(id, role_id, create_time))

    name = '微信'
    # sql = "SELECT create_time, update_time, `name`, leader, tester, " \
    #       "programmer, publish_app, `desc` FROM ap_projects WHERE name='{}" \
    #       "' AND is_delete=0 AND user_id=1;".format(name)
    # sql = f"""SELECT create_time, update_time, `name`, leader, tester, programmer, publish_app, `desc`
    #          FROM ap_projects
    #          WHERE name='{name}' AND is_delete=0 AND user_id=1;"""
    # create_time, update_time, name, leader, tester, programmer, publish_app, desc = db.find_one(
    #     sql=sql)
    # create_time = str(create_time).split('.')[0]
    # update_time = str(update_time).split('.')[0]
    #
    # print(create_time)
    # print(name)

    sql = "SELECT id, username FROM auth_user WHERE id < 10;"
    res = db.find_count(sql)
    print(res)


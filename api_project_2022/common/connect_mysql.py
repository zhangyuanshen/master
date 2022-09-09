import pymysql
from config.config import dbinfo_loacl
class DbConnect():
    def __init__(self,db_cof,database="test"):
        self.db_cof = db_cof
        # 连接数据库
        self.db = pymysql.connect(
            database=database,
            cursorclass=pymysql.cursors.DictCursor,
            **db_cof
        )
        # 获取游标
        self.cursor = self.db.cursor()

    def select(self,sql):
        """sql查询语句"""
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self,sql):
        """sql删除，修改语句"""
        try:
            # 执行语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
    def close(self):
        # 关闭连接
        self.db.close()
        pass


if __name__ == '__main__':
    # db = DbConnect(dbinfo_online,database="healthy_rc")
    # result = db.selet("SELECT * FROM water_records WHERE user_id = 3608 AND record_on ='2021-07-05';")
    # db.close()
    # print(result)

    db = DbConnect(dbinfo_loacl, database="test")
    db.execute("delete from student WHERE s_id = 11;")
    db.close()
    # print(result)

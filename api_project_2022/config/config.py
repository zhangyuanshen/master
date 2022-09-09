import os
#当前文件路径
CUR_PATH = os.path.realpath(__file__)
# print(CUR_PATH)
#项目根目录
ROOT_PATH = os.path.dirname(os.path.dirname(CUR_PATH))
# print(ROOT_PATH)

# 数据库配置信息
dbinfo_loacl ={
            "host":"localhost",
            "user":"root",
            "password":"123456",
            "port":3306
}
dbinfo_rc ={
    "host":"rm-8vbz6ur111qxh1ehp.mysql.zhangbei.rds.aliyuncs.com",
    "user":"bhuser",
    "password":"363099",
    "port":3306
}


import pytest
"""注册之前先去数据库删除对应的用户,单独写一个fixture"""
@pytest.fixture()
def delete_user(db):
    """删除"""
    user_name = "test_api"
    sql = "delete from users where user_name='%s';" %user_name
    # print("执行sql：%s"%sql)
    db.execute(sql)

if __name__ == '__main__':
    user_name = "test_api"
    sql = "delete from users where user_name='%s';" % user_name
    print("执行sql：%s" % sql)
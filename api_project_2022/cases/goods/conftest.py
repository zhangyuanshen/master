import pytest
@pytest.fixture()
def delete_by_goodscode(db):
    def delete_goods(goodscode):
        """"去数据库删除"""
        sql = "delete from goods where goodscode='%s';"%goodscode
        db.execute(sql)
    return delete_goods
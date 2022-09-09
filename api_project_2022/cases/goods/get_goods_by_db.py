# 添加完成之后
import pytest

from api.goods import add_goods,get_goods
from common.connect_mysql import DbConnect,dbinfo_loacl


def get_goods_db():
    db =DbConnect(dbinfo_loacl)
    sql = "select id ,goodscode from goods where goodscode='ceshi';"
    result = db.select(sql)
    # 返回查询的数据库内容
    return result

test_data ={
            ["ceshi_goodscode",{"goodscode":"ceshi_goodscode","goodsstatus":1}]
}

@pytest.mark.parametrize("test_input,expected",test_data)
def test_get_goods(session,delete_by_goodscode,test_input,expected):
#     先删除数据库内已有的商品
    delete_by_goodscode(goodscode=test_input)
# 新增一个商品 先写伪代码获取到商品id
    add = add_goods(session,goodscode=test_input)
    sid =add.json()["data"]["id"]
    # 根据ID进行查询
    r = get_goods(session,goodsid=sid)
    # 验证数据库中的数据是否一致
    assert get_goods_db()["id"]==sid
    assert get_goods_db()["goodscode"]==expected["goodscode"]
    assert get_goods_db()["goodsstatus"]==expected["goodsstatus"]

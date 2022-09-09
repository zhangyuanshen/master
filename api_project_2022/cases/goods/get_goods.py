import pytest
from api.goods import add_goods,get_goods

def test_get_goods(session,delete_by_goodscode):
#     先删除数据库内已有的商品
    delete_by_goodscode(goodscode="ceshi")
# 新增一个商品 先写伪代码获取到商品id
    add = add_goods(session,goodscode='ceshi')
    sid =add.json()["data"]["id"]
    # 根据ID进行查询
    r = get_goods(session,goodsid=sid)
    assert r.json()["code"]=="ceshi"


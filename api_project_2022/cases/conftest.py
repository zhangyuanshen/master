from api.login import login_get_token
from common.connect_mysql import DbConnect,dbinfo_loacl
import requests
import pytest
"""
对当前模块和子模块都生效
若放子模块里 仅针对子模块生效
"""
@pytest.fixture()
def session(base_url):
    """登陆获取token"""
    s = requests.session()
    login_get_token(s,base_url)
    yield s
    s.close()
@pytest.fixture(scope="function")
def unlogin():
    """不需要登陆的接口"""
    s = requests.session()
    yield s
    s.close()

@pytest.fixture(scope="session")
def db():
    db = DbConnect(dbinfo_loacl, database="TSP")
    yield db
    db.close()

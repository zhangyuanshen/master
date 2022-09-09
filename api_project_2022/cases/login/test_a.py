import pytest
from common.read_yaml import yaml_to_python
from config.config import ROOT_PATH
from api.login import login_get_token
import os
# login_data = yaml_to_python(os.path.join(ROOT_PATH,"data","login_data.yml"))

login_data = [
    [{"sign": "\/64tM2LXcNJQcySX1k3KSZKASI8=", "app_key": "one",
      "context_params": "eyJsb2dpbiI6IjE4NTMzMzM0NDQ0IiwicGFzc3dvcmQiOiIxMjM0NTYiLCJkZXZpY2VfdG9rZW4iOiI2Q0MzQTI2QS1CQkJDLTRFOTEtODQ1Qy1GODc1OTA3N0YxMUQifQ=="},
     {"83e570ae-14c9-49d4-a730-915b9bfacfcc"}]]
#     [{"sign": "\/64tM2LXcNJQcySX1k3KSZKAS", "app_key": "one",
#       "context_params": "eyJsb2dpbiI6IjE4NTMzMzM0NDQ0IiwicGFzc3dvcmQiOiIxMjM0NTYiLCJkZXZpY2VfdG9rZW4iOiI2Q0MzQTI2QS1CQkJDLTRFOTEtODQ1Qy1GODc1OTA3N0YxMUQifQ=="},
#      {"message": "app sign验证失败", "code": 102}]
# ]


# @pytest.mark.parametrize("test_input,expected", login_data)
# def test_login_case(unlogin, base_url,test_input, expected):
#     r = login_get_token(unlogin,base_url, sign=test_input["sign"],
#                         app_key=test_input["app_key"],
#                         context_params=test_input["context_params"])
#     if r.json()["errors"]:
#         assert r.json()["errors"][0]== expected
#     else:
#         assert r.json()["user"]["user_key"]==expected

@pytest.mark.parametrize("test_input,expected", login_data)
def test_login_case1(session,base_url,test_input,expected):
    r = login_get_token(session,base_url,sign=test_input["sign"],app_key=test_input["app_key"],
                        context_params=test_input["context_params"])
    assert r.json()["user"]["user_name"]=='api_test'

import requests
from base.baseurl import RcUrl
from base.util import Util
# s = requests.Session()


def login_get_token():
    """"登陆获取token"""
    sign = Util().signature_create()
    app_key = "one"
    context_params = str(Util().context_params_create(), encoding="utf8")
    # url =RcUrl.passport_url+"/api/v1/users/login"
    # print("url====",url)
    body = {
        "sign": sign,
        "app_key": app_key,
        "context_params": context_params
    }
    # print("context_params====",context_params)
    # print("bady====",body)
    r = requests.post(RcUrl().get_token_url(),body)
    # r = s.post(url,json=body)
    # print(r.text)
    # 更新信息头 得到token
    token = r.json()["token"]
    # header = {
    #     'token': token
    # }
    #
    # requests.headers.update(header)
    return token



if __name__ == '__main__':
    s = requests.Session()

    r= login_get_token()
    print(r)



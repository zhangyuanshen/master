import base64
import hashlib
import hmac
import json

import requests

from base.baseurl import RcUrl


class Util:
    app_key = "one"
    app_secret = "boohee-test-test-test"
    def base64_encode(self, test_str):
        # 编码

        encode_bs64 = test_str.encode("utf-8")
        str_url = base64.b64encode(encode_bs64)
        # print(str_url)
        return str_url

    def base64_decode(self, encode_str):
        # 解码
        decode_str = base64.decodebytes(encode_str)
        print(decode_str.decode())  # 默认以utf8解码

    # 生成context_params 使用BASE64加密
    def context_params_create(self):
        login_dic = {"login": "testapi", "password": "123456", "device_token": "CE4F70E1-73B7-4FFD-A11A-8FD83C3C1066"}
        # dump函数 dumps函数 load loads
        login_json_str = json.dumps(login_dic)
        context_str = self.base64_encode(login_json_str)
        return context_str

    """
    hash.digest() 返回摘要，作为二进制数据字符串值
    hash.hexdigest() 返回摘要，作为十六进制数据字符串值
    """
    def hash_hmac(self, bytes_context, secret):
        secret_key = secret.encode(encoding='utf-8')
        data_to_sign = bytes_context.encode(encoding='utf-8')
        digest = hmac.new(secret_key, data_to_sign, digestmod=hashlib.sha1).digest()

        # 再进行一次BASE64编码，加SECRET
        digest_b64 = base64.b64encode(digest)

        return digest_b64.decode(encoding='utf-8')

    # 生成signature
    def signature_create(self):
        # base64加密后的字符串
        context = str(self.context_params_create(), encoding="utf8")
        # 和key一起进行HMAC加密

        hash_code = self.hash_hmac(self.app_key + context, self.app_secret)
        # print(hash_code)

        return hash_code

    # def get_token(self):
    #
    #     # context_params
    #     context_params = str(self.context_params_create(), encoding="utf8")
    #     # print("context_str == " + context_params)
    #     sign = self.signature_create()
    #     # print("sign == " + sign)
    #     loginparams = {
    #         "sign": sign,
    #         "app_key": self.app_key,
    #         "context_params": context_params
    #     }
    #
    #     # print("BaseUrl().get_token_url == " + BaseUrl().get_token_url())
    #     # print("调用一次登录接口")
    #     r = requests.post(RcUrl().get_token_url(), loginparams).json()
    #     print(r)
    #     # print("结束")
    #     return r["token"]
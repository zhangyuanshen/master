import json
import os

import requests
import yaml

from base.util import Util
from api.login import login_get_token


class BaseApi:
    params = dict()
    base_token = login_get_token()
    def send(self, data):

        raw_data = json.dumps(data)
        # print(raw_data)

        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
            data = json.loads(raw_data)
        # print(data)
        responsedata = requests.request(**data)


        # print("raw_data == " + raw_data)
        # print("responsecode == " + str(responsedata.status_code))

        return responsedata

if __name__=="__main":

    _path = os.path.abspath("../../data/record_data.yml")
    with open(_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    b = BaseApi()
    b.send(data["add_food"])
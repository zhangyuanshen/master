import os

import yaml

from base.baseapi import BaseApi
from base.baseurl import RcUrl
from api.login import login_get_token
from common.read_yaml import yaml_to_python
from config.config import ROOT_PATH


class EatingApi(BaseApi):
    def __init__(self):
        self.params["token"] = self.base_token

        _path = os.path.abspath("../../data/record_data.yml")
        with open(_path, encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def add_food(self,params):
        self.params["url"] = RcUrl().add_v2_food()
        return self.send(self.data[params])

    def update_food(self,params,food_id):
        self.params['url'] = RcUrl().update_v2_food(food_id)
        return self.send(self.data[params])

    def delete_food(self,params,food_id):
        self.params["url"] = RcUrl().delete_v2_food(food_id)
        return self.send(self.data[params])

if __name__ == '__main__':
    curpath = os.path.realpath(__file__)
    root_path = os.path.dirname(os.path.dirname(curpath))
    yaml_path = os.path.join(root_path, "data", "record_data.yml")
    _path = os.path.abspath(__file__)
    print(_path)
    print(curpath)
    print(root_path)
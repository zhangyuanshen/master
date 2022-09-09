import allure
import pytest

from api.recordapi.eating import EatingApi


"""
  {
    "amount": 100,
    "food_name": "酸奶",
    "calory": 70,
    "code": "suannai_junzhi",
    "food_unit_id": "0",
    "record_on": "2022-08-31",
    "time_type": "1",
    "unit_name": "克",
    "record_from": "常见",
    "token": "xpUxZgBZ2ybxsPiWPPK8sPfc2qyucLMh"
  }
{
	"amount": 100,
	"food_name": "鸡蛋",
	"calory": 139,
	"code": "jidan_junzhi",
	"food_unit_id": "0",
	"record_on": "2022-08-31",
	"time_type": "1",
	"unit_name": "克",
	"record_from": "常见",
	"token": "xpUxZgBZ2ybxsPiWPPK8sPfc2qyucLMh"
}
"""


@allure.feature("record接口")
class TestAtEating():
    def setup_class(self):
        food_id = EatingApi().add_food("add_food").json()["id"]
        self.food_id = food_id
    def teardown_class(self):
        pass


    @allure.story("食物相关接口")
    @allure.title("食物接口新增米饭")
    def test_add_eating(self):
        result = EatingApi().add_food("add_food")
        print(result)
        assert result.json()["food_name"] == "米饭"

    # @pytest.mark.skip

    @allure.title("更新食物到200g")
    def test_update_eating(self):
        result = EatingApi().update_food("update_food",self.food_id)
        print(result.json())
        assert result.json()["amount"] == 200

    @allure.title("删除食物")
    def test_delete_food(self):
        result = EatingApi().delete_food("delete_food",self.food_id)
        assert result.status_code == 200
        print(result)

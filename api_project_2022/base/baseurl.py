class RcUrl:
    passport_url = "http://passport.iboohee.com"
    one_url = "http://one.iboohee.com"
    status_url = "http://status.iboohee.com"
    bingo_url = "http://bingo.iboohee.com"
    food_url = "http://food.iboohee.com"
    record_url = "http://record.iboohee.com"
    nice_url = "http://nice.iboohee.com"
    healthy_url = "http://healthy.iboohee.com"
    ifood_url = "http://ifood.iboohee.com"
    nice_url = "http://nice.iboohee.com"
    columbus_url = "http://columbus.iboohee.com"

    def get_token_url(self):
        url = self.passport_url +"/api/v1/users/login"
        return url

    def add_v2_food(self):
        url = self.record_url +"/api/v2/eatings"
        return url

    # https://record.boohee.com/api/v2/eatings?token=xpUxZgBZ2ybxsPiWPPK8sPfc2qyucLMh&record_on=2022-08-31
    def get_v2_food(self):
        url = self.record_url +"api/v2/eatings?record_on=2022-08-31"

    def update_v2_food(self,food_id):
        url = self.record_url +"/api/v2/eatings/"+str(food_id)
        return url

    def delete_v2_food(self,food_id):
        url = self.record_url +"/api/v2/eatings/"+str(food_id)
        return url


if __name__ =="__main__":

    re = RcUrl()
    result = re.update_v2_food(10)
    print(result)
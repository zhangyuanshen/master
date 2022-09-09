import requests
from base.baseurl import RcUrl

def change_user_info():
    url =RcUrl.record_url + "/api/v1/users/one_change_profile"
    return url

if __name__ == '__main__':
    s = requests.session()
    from api.login import login_get_token
    login_get_token()

    print()

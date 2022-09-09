# import requests
#
# from api.login import login_get_token
#
# s = requests.session()
# r=login_get_token(s)
# r=s.get(url="https://seafarer.iboohee.com/api/v1/home_dietitian_tips")
#
# print(r.json())

# def num_add(fun):
#     def add_num(fun):
#         fun()
#         print(i+1)
#     return add_num



import random
l1 = [1,2,3,4,5,6,7]
# @num_add
def random_list(list):
    rand_list = []
    while len(rand_list)<len(list ):
        random_index = random.randint(0,len(list)-1)
        if random_index not in rand_list:
            rand_list.append(random_index)
    print(rand_list)
    new_list=[]
    for i in rand_list:
        new_list.append(l1[i])
    return new_list
x = random_list(l1)
print(x)

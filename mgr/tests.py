import pprint
import requests

# Create your tests here.

# response = requests.get('http://localhost/api/mgr/customers?action=list_customer')
# pprint.pprint(response.json())

# 构建添加 客户信息的 消息体，是json格式
# payload = {
#     "action": "add_customer",
#     "data": {
#         "name": "武汉市桥西医院",
#         "phonenumber": "13345679934",
#         "address": "武汉市桥西医院北路"
#     }
# }
#
# # 发送请求给web服务
# response = requests.post('http://localhost/api/mgr/customers',
#               json=payload)
#
# pprint.pprint(response.json())
#
# # 构建查看 客户信息的消息体
# response = requests.get('http://localhost/api/mgr/customers?action=list_customer')
#
# # 发送请求给web服务
# pprint.pprint(response.json())


payload = {
    'username': 'Fino',
    'password': '010125020307lot'
}

response = requests.post('http://localhost/api/mgr/signin',
              data=payload)

pprint.pprint(response.json())
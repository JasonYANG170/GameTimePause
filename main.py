import requests
import json
import os
import hashlib

token = os.environ['TOKEN']
user = os.environ['PHONE']
# print('user:', user)
password = os.environ['PASSWORD']


# print('password:', password)
def calculate_md5(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash


md5_result = calculate_md5(password)
# print("MD5 哈希值为:", md5_result)

# 定义要发送的数据
data = {
    "username": user,
    "password": md5_result,
    "user_type": "0",
    "src_channel": "guanwang",
    "code": "8fAAIgr3HHmcX7JY",
    "country_code": 86,
    "lang": "en",
    "os_type": 5
}
url = 'https://webapi.leigod.com/wap/login/bind'
response = requests.post(url, json=data)
if response.status_code == 200:
    # print('返回值:', response.json())
    account_token = response.json()['data']['login_info']['account_token']
  #  print('account_token:', account_token)
    data = {
        "account_token": account_token,
        "lang": "en",
        "os_type": 5
    }
    url = 'https://webapi.leigod.com/api/user/pause'
    response = requests.post(url, json=data)
    if response.status_code == 200:
        state = response.json().get('msg', '')
        text = '未知错误'

        if state == 'Account has been paused, do not duplicate operation':
            text = '您的加速器已经暂停过了'
        elif state == 'OK':  # 使用elif代替else if
            text = '加速时长暂停成功'
        else:  # 最后一个条件应该是else
            text = '未知错误：' + str(response.json())

        print(text)

        title = 'GameTimePause'  # 改成你要的标题内容
        content = text  # 改成你要的正文内容
        url = 'http://www.pushplus.plus/send?token=' + token + '&title=' + title + '&content=' + content
        requests.get(url)
    else:
        print('请求失败:', response.text)
else:
    print('请求失败:', response.text)

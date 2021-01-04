'''
Author: zhuohoudeputao
LastEditors: zhuohoudeputao
LastEditTime: 2021-01-04 17:00:42
Description: file content
'''
# import sys
# import os
# sys.path.append(os.getcwd())
# print(os.getcwd())

import requests
import json

with open('config.json', 'r') as config:
    data = json.load(config)

ip = data["ip"]
wlanuserip = ip
wlanacip = data["wlanacip"]

# login address
post_addr="https://s.scut.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanuserip="+wlanuserip+"&wlanacip="+wlanacip+"&wlanacname=6108-North-slot3&redirect=&session=&vlanid=scut-student&port=&iTermType=1&protocol=https:"

# head
post_header={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '69',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'Hm_lvt_cad45348d1fdf49a7a9a1f8b99526616=1539305328; PHPSESSID=3jk9f34l2s13v5grtrhdlcp913',
'Host': 's.scut.edu.cn:801',
'Origin': 'https://s.scut.edu.cn',
'Referer': 'https://s.scut.edu.cn/a70.htm?wlanuserip='+wlanuserip+'&wlanacip='+wlanacip+'&wlanacname=6108-North-slot3&redirect=&session=&vlanid=scut-student&ip='+ip+'&mac=000000000000',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# data
post_data={
'DDDDD': data["id"], # your id
'upass': data["passwd"], # password
'R1': '0',
'R2': '',
'R6': '0',
'para': '00',
'0MKKey': '123456'
}

# request
print('requesting...')
z=requests.post(post_addr, data=post_data, headers=post_header)
print(z)
print('login success!')

# for debug
import time
time.sleep(2)
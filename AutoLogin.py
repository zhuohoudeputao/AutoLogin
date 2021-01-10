'''
Author: zhuohoudeputao
LastEditors: zhuohoudeputao
LastEditTime: 2021-01-04 17:00:42
Description: file content
'''
import requests
import json
import logging
from win10toast import ToastNotifier

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
handler = logging.FileHandler('log.txt')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# logger.addHandler(console)

def isConnected():
    import os
    exit_code = os.system('ping www.baidu.com') # this one will run in a cmd window
    if exit_code:
        return False
    return True

def isConnected2():
    try:
        content = requests.get('https://www.baidu.com', timeout=3.0)
        # print(content)
    except:
        return False
    return True

def load_data():
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

    return post_addr, post_data, post_header

if __name__=="__main__":
    toaster = ToastNotifier()
    if isConnected2():
        logger.info('Network is connected. Exiting...')
        toaster.show_toast("AutoLogin", 
                        "Network is connected. Exiting...",
                        icon_path='scut.ico',
                        duration=5)
    else:
        logger.info('Network is not connected. Trying to log in...')
        logger.debug('Loading data...')
        post_addr, post_data, post_header = load_data()
        z=requests.post(post_addr, data=post_data, headers=post_header)
        logger.debug(str(z))
        if isConnected2():
            logger.info('Login success!')
            toaster.show_toast("AutoLogin", 
                        "Login success!",
                        icon_path='scut.ico',
                        duration=5)
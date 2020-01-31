import requests

ip = "172.28.143.167"
wlanuserip = ip
wlanacip = "172.28.255.251"

#登录地址
post_addr="https://s.scut.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanuserip="+wlanuserip+"&wlanacip="+wlanacip+"&wlanacname=6108-North-slot3&redirect=&session=&vlanid=scut-student&port=&iTermType=1&protocol=https:"

#构造头部信息
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

#构造登录数据
post_data={
'DDDDD': '', #你的学号
'upass': '', #你的密码
'R1': '0',
'R2': '',
'R6': '0',
'para': '00',
'0MKKey': '123456'
}
#发送post请求登录网页
z=requests.post(post_addr,data=post_data,headers=post_header)
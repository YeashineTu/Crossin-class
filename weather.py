#!/usr/bin/python
# -*- encoding：utf-8 -*-
import urllib.request
import json

data=urllib.request.urlopen('http://m.weather.com.cn/data3/city.xml')
d=data.read().decode('utf-8')
d=d.split(',')
provice=d[0:3]  #d[19:20] list  d[19] str
result=""
for p in provice:
	code=p.split('|')[0]   #取第一个元素
	url1='http://m.weather.com.cn/data3/city'+code+'.xml'
	city=urllib.request.urlopen(url1).read().decode('utf-8').split(',')
	for c in city:
		code1=c.split('|')[0]
		url2='http://m.weather.com.cn/data3/city'+code1+'.xml'
		distict=urllib.request.urlopen(url2).read().decode('utf-8').split(',')
		for d in distict:
			code2=d.split('|')[0]
			name=d.split('|')[1]
			line="'%s':'%s',"%(name,code2)
			result+=line
result='{'+result+'}'

f=open('weather.txt','w',encoding='utf-8')
f.write(result)
f.close()
result=eval(result)
print(type(result))

##写文件只能是str,所以要在读文件的时候转化为dict
##str转化成字典
##字典可以多行
##eval
##

print('你想查哪个城市的天气')
city=input()
f=open('weather.txt',encoding='utf-8')
cityCode=eval(f.read())
print(cityCode)
f.close()
if cityCode.get(city):
	url="http://www.weather.com.cn/data/cityinfo/"+"101"+cityCode[city]+".html"
	f=urllib.request.urlopen(url)
	t=f.read().decode('utf-8')   #不加.decode('utf-8')也行
	print(url)
	print(t)
	dict=json.loads(t)
	weatherinfo=dict['weatherinfo']
	print('城市：%s'%city)
	print('天气：%s'%weatherinfo['weather'])
	print('最低温度：%s'%weatherinfo['temp1'])
	print('最高温度：%s'%weatherinfo['temp2'])
else:
	print('没有找到对应城市的天气信息！')
#只能read一次

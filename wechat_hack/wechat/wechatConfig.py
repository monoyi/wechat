#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import make_response
import hashlib
import random
from mode import scanPort,sendSMS,queryData
from mode import Zoomeye,Readfile,Pocsuite
from mode import Vulscan

def wechat_auth(token,data):
	signature = data.get('signature','')
	timestamp = data.get('timestamp','')
	nonce = data.get('nonce','')
	echostr = data.get('echostr','')
	s = [timestamp,nonce,token]
	s.sort()
	s = ''.join(s)
	if (hashlib.sha1(s).hexdigest() == signature):
	    return make_response(echostr)

def wechat_mode(content):
	if content==u"攻击":
	    return """
G1:端口扫描
G2:短信攻击
G3:md5查询
G4:搜索zoomeye
G5:使用pocsuite批量获得shell
G6:tiny Batch weB vulnerability Scanner
Read:查看结果文件
攻击格式：编号&目标
例如：　
    G1&127.0.0.1
    G2&188****1111
    G3&md5
    G4&struts
	G5&joomla
	G6&www.baidu.com
    Read&target_1234567890abcdef
""", 'text'
	elif  "G1&" in content:
		arr=content.split('&')
		return "你扫描的IP端口为："+str(scanPort.init(arr[1])), 'text'
	elif  "G2&" in content:
		arr=content.split('&')
		return "系统提示："+str(sendSMS.sendSMS(arr[1])), 'text'
	elif  "G3&" in content:
		arr=content.split('&')
		return str(queryData.queryData(arr[1])), 'text'
	elif  "G4&" in content:
		arr = content.split('&')
		return "结果在文件 " + str(Zoomeye.Zoomeye(arr[1])), 'text'

	elif "G5&" in content:
		arr = content.split('&')
		return str(Pocsuite.Pocsuite(arr[1])), 'text'

	elif "G6&" in content:
		arr = content.split('&')
		return "结果在文件 " + str(Vulscan.main(arr[1])), 'text'		

	elif  "Read&" in content:
		arr = content.split('&')
		return str(Readfile.Readfile(arr[1])), 'text'
	else:
		l = [lines for lines in open('./scentence','r').read().split('\n')]
		result = {}
		result['title'] = l[random.randint(0,len(l)-1)]
		result['url'] = 'http://104.194.78.117:8000/' + str(random.randint(1,10)) + '.png'
		return result, 'news'

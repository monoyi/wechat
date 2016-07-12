def Readfile(filename):
    print filename	
    try:    
    	f = open('/root/wechat_hack/' + filename, 'r')
        ans = ''
        for i in range(0, 10):
             ans += f.readline()
	return ans

    except Exception, e:
        print e
	return "wrong filename!" 

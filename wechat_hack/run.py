#! /usr/bin/python
# -*- coding: utf-8 -*-
import time
from flask import Flask,g,request,make_response
import hashlib
import xml.etree.ElementTree as ET
from wechat import wechatConfig

app = Flask(__name__)

@app.route('/tools',methods=['GET','POST'])
def tools():
	if request.method == 'GET':
		token='jeremylin'
		return wechatConfig.wechat_auth(token,request.args)
	else:
		req = request.stream.read()
		resultData = ET.fromstring(req)

		toUser = resultData.find('ToUserName').text
		fromUser = resultData.find('FromUserName').text
		content = resultData.find('Content').text
		
		resultContent, mode = wechatConfig.wechat_mode(content)
                
                    
                    
                if mode == 'text':

                    formData = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
                    response = make_response(formData % (fromUser,toUser,str(int(time.time())),'text', resultContent))
                    response.content_type='application/xml'
                    return response
                
                elif mode == 'news':

                    formData = """
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[%s]]></Title> 
<Description><![CDATA[发送“攻击”二字试试看]]></Description>
<PicUrl><![CDATA[%s]]></PicUrl>
<Url><![CDATA[http://github.com]]></Url>
</item>
</Articles>
</xml>
"""
     		    print resultContent
	            response = make_response(formData % (fromUser,toUser,str(int(time.time())), resultContent['title'], resultContent['url'])) 
                    response.content_type='application/xml'
                    return response


if __name__ == '__main__':
    app.run(host="104.194.78.117",port=80, debug=True)

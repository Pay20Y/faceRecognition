# encoding:utf-8
import base64
import urllib
import urllib2

'''
人脸探测
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"

# 二进制方式打开图片文件
f = open('/home/george/data/1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
params = urllib.urlencode(params)

access_token = '24.be4e6182551c536066845f05f85e10b7.2592000.1517971792.282335-10644820'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content
# encoding:utf-8
import base64
import urllib
import urllib2
import os
import types
import string

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"
access_token = "24.be4e6182551c536066845f05f85e10b7.2592000.1517971792.282335-10644820"
request_url = request_url + "?access_token=" + access_token

faceDict = {}
for filename in os.listdir('../../data/shrinkLFW/'):
	temp = filename.split('.')
	front = temp[0]
	personName = front[:-5]
	if not faceDict.has_key(personName):
		file1 = personName+'_0001.jpg'
		file2 = personName+'_0002.jpg'
		faceDict[personName] = [file1,file2]
print 'faceDict size is: ',len(faceDict)

times_FNMR = 0.0
count_FNMR = 0
for face in faceDict:
	print 'now calc %s' %face
	image1 = open("../../data/shrinkLFW/" + faceDict[face][0],"rb")
	image2 = open("../../data/shrinkLFW/" + faceDict[face][1],"rb")

	image1_encoding = base64.b64encode(image1.read())
	image2_encoding = base64.b64encode(image2.read())

	params = {"images":image1_encoding + ',' + image2_encoding}
	params = urllib.urlencode(params)

	request = urllib2.Request(url=request_url, data=params)
	request.add_header('Content-Type', 'application/x-www-form-urlencoded')
	response = urllib2.urlopen(request)
	content = response.read()
	if content:
		times_FNMR = times_FNMR + 1
		print content
		result_score = string.atof(content[48:62])
		print result_score
		if result_score < 80:
			count_FNMR = count_FNMR + 1
		# result = content["result"][0]["score"]
    	# print result
FNMR = count_FNMR / times_FNMR

'''
times = 0.0
count_FMR = 0;
for face in faceDict:

	if face == "Abdel_Nasser_Assidi":
		continue
	image1 = open("../../data/shrinkLFW/" + faceDict[face][0],"rb")
	image2 = open("../../data/shrinkLFW/" + faceDict[face][1],"rb")

	image1_encoding = base64.b64encode(image1.read())
	image2_encoding = base64.b64encode(image2.read())


	for face_compare in faceDict:
		if face_compare == "Abdel_Nasser_Assidi":
			continue
		if face_compare != face:
			image_compare = open("../../data/shrinkLFW/" + faceDict[face_compare][1],"rb")
			image_compare_encoding = base64.b64encode(image_compare.read())

			params_compare = {"images":image1_encoding + "," + image_compare_encoding}
			params_compare = urllib2.Request(url=request_url,data=params_compare)

			request = urllib2.Request(url=request_url, data=params_compare)
			request.add_header('Content-Type', 'application/x-www-form-urlencoded')
			response = urllib2.urlopen(request)
			content = response.read()

			if content:
				times = times + 1
				result_score = content[48:63]
				if result_score >= 80:
					count_FMR = count_FMR + 1

FMR = count_FMR / times
'''
print "after %f times match test,FNMR is: "%times_FNMR,FNMR
# print "FMR  is: ",FMR
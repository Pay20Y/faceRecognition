import face_recognition
import os
from numpy import *

# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

# Load some images to compare against

def file2dict():
	print "Now set the file_info in dict..."
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
	return faceDict

def writeDistance(face_Dict):
	count = 1
	print "Now get image_encoding then write 2 file..."
	# f = open("faceEncoding","w")
	f_inner = open("disInner.txt","w")
	f_outter = open("disOutter.txt","w")
	for faceKey in face_Dict:
		print 'now calc No.%d, %s' %(count,faceKey)
		image1 = face_recognition.load_image_file("../../data/shrinkLFW/" + face_Dict[faceKey][0])
		image2 = face_recognition.load_image_file("../../data/shrinkLFW/" + face_Dict[faceKey][1])

		length1 = len(face_recognition.face_encodings(image1))
		length2 = len(face_recognition.face_encodings(image2))

		if (length1 == 0 and length2 != 0):
			# print "if!"
			image1_encoding = ones(128) * 100
			image2_encoding = face_recognition.face_encodings(image2)[0]
		elif (length2 == 0 and length1 != 0):
			# print "elif!"
			image1_encoding = face_recognition.face_encodings(image1)[0]
			image2_encoding = ones(128) * 100
		else:
			# print "else!"
			image1_encoding = face_recognition.face_encodings(image1)[0]
			image2_encoding = face_recognition.face_encodings(image2)[0]
		
		image1_encoding = [image1_encoding]
		# image2_encoding = [image2_encoding]
		face_distance = face_recognition.face_distance(image1_encoding,image2_encoding)
		face_distance = str(face_distance[0])
		f_inner.write(face_distance + " ")

		for faceInner in face_Dict:
			
			image_compare = face_recognition.load_image_file("../../data/shrinkLFW/" + face_Dict[faceInner][1])

			length_compare = len(face_recognition.face_encodings(image_compare))

			if length_compare == 0:
				compare_image_encoding = ones(128) * 100
			else:
				compare_image_encoding = face_recognition.face_encodings(image_compare)[0]
			
			face_distance_out = face_recognition.face_distance(image1_encoding,compare_image_encoding)
			f_outter.write(str(face_distance_out[0]) + " ")
		f_outter.write("\n")
		count = count + 1
		# print image1_encoding
		# print compare_image2_encoding
		'''
		for element in image1_encoding:
			element_str = str(element)
			f.write(element_str + " ")
		f.write("\n")
		for element in image2_encoding:
			element_str = str(element)
			f.write(element_str + " ")
		f.write("\n")
		count = count + 1
		f.close()
		'''
	f_outter.close()
	f_inner.close()

def readDistance():
	f_inner_read = open("disInner.txt","r")
	f_outter_read = open("disOutter.txt","r")

	disLine = f_inner_read.readline()
	while disLine_inner:
		disList_inner = disLine_inner.split()
		disList_inner = disList_inner[:128]

	inner_times = len(disList)

	for inner_dis in disList_inner:
			

'''
def getDistance():
	encodingMat = []
	encodeFile = open("faceEncoding.txt","r")
	line = encodeFile.readline()
	while line:
		temp = line.split(" ")
		temp = temp[:128]
		encodingMat.append(temp)
		line = encodeFile.readline()
	encodeFile.close()
	# print "encodingMat's size is: ",len(encodingMat)
	# print len(encodingMat[0])

	innerDis_list = []
	# print type(array(encodingMat[0]))
	
	for i in range(len(encodingMat) - 1):
		attr1 = array(encodingMat[i])
		attr2 = array(encodingMat[i+1])
		inner_face_distance = face_recognition.face_distance(attr1,attr2)
		innerDis_list.append(inner_face_distance[0])

	print innerDis_list
'''

def execute():
	faceDict = file2dict()
	writeDistance(faceDict)
	# writeEncodings(faceDict)
# clac inner class
'''
count = 0
times_innner = 0.0
countReg = 0
times_outter = 0.0
for face in faceDict:
	print 'now calc %s' %face
	image1 = face_recognition.load_image_file("../../data/shrinkLFW/" + faceDict[face][0])
	image2 = face_recognition.load_image_file("../../data/shrinkLFW/" + faceDict[face][1])

	length1 = len(face_recognition.face_encodings(image1))
	length2 = len(face_recognition.face_encodings(image2))

	if (length1 == 0 or length2 == 0):
		continue;

	image1_encoding = face_recognition.face_encodings(image1)[0]
	image2_encoding = face_recognition.face_encodings(image2)[0]

	inner_encoding = [image1_encoding]
	outter_encoding = [image1_encoding,image2_encoding]

	face_distances = face_recognition.face_distance(inner_encoding,image2_encoding)
	times_innner = times_innner + 1

	for faceInner in faceDict:
		if(faceInner != face):
			image1_compare = face_recognition.load_image_file("../../data/shrinkLFW/" + faceDict[faceInner][0])
			image2_compare = face_recognition.load_image_file("../../data/shrinkLFW/" + faceDict[faceInner][1])

			length1_compare = len(face_recognition.face_encodings(image1_compare))
			length2_compare = len(face_recognition.face_encodings(image2_compare))

			if (length1_compare == 0 or length2_compare == 0):
				continue

			# compare_image1_encoding = face_recognition.face_encodings(image1_compare)[0]
			compare_image2_encoding = face_recognition.face_encodings(image2_compare)[0]

			# face_distances1 = face_recognition.face_distance(outter_encoding,compare_image1_encoding)
			face_distances2 = face_recognition.face_distance(inner_encoding,compare_image2_encoding)

			times_outter = times_outter + 1
			
			if face_distances2[0] < 0.6:
				countReg = countReg + 1

	if face_distances[0] > 0.6:
		count = count + 1

FNMR = count / times_innner
print "after %f times match test,FNMR = " %times_innner,FNMR

FMR = countReg / 39600.0
print "after %f times match test,FMR  = " %times_outter,FMR
'''
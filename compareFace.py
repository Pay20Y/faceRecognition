import face_recognition
import os

# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

# Load some images to compare against

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

# for k in faceDict:
    # print "faceDict[%s] =" % k,faceDict[k]

# clac inner class
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

	if length1 == 0 or length2 == 0:
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

			if length1_compare == 0 or length2_compare == 0:
				continue

			compare_image1_encoding = face_recognition.face_encodings(image1_compare)[0]
			compare_image2_encoding = face_recognition.face_encodings(image2_compare)[0]

			face_distances1 = face_recognition.face_distance(outter_encoding,compare_image1_encoding)
			face_distances2 = face_recognition.face_distance(outter_encoding,compare_image2_encoding)

			times_outter = times_outter + 8
			if face_distances1[0] < 0.6:
				countReg = countReg + 1
			if face_distances1[1] < 0.6:
				countReg = countReg + 1
			if face_distances2[0] < 0.6:
				countReg = countReg + 1
			if face_distances2[1] < 0.6:
				countReg = countReg + 1
	if face_distances[0] > 0.6:
		count = count + 1

FNMR = count / times_innner
print "after %f times match test,FNMR = " %times_innner,FNMR

FMR = countReg / 39600.0
print "after %f times match test,FMR = " %times_outter,FMR

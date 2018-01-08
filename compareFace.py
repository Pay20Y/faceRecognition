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
countReg = 0
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

FNMR = count / 100.0
print "FNMR = ",FNMR

FMR = countReg / 39600.0
print "FMR = ",FMR

#clac outter class


	#known_obama_image = face_recognition.load_image_file("obama.jpg")
	#known_biden_image = face_recognition.load_image_file("biden.jpg")

# Get the face encodings for the known images
# obama_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
# biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]

# known_encodings = [
    # obama_face_encoding,
    # biden_face_encoding
# ]

# Load a test image and get encondings for it
# image_to_test = face_recognition.load_image_file("obama2.jpg")
# image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
# face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

# for i, face_distance in enumerate(face_distances):
    # print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    # print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    # print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))

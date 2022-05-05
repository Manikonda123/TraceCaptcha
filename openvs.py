from asyncio.windows_events import NULL
import cv2
import numpy as np
from matplotlib import pyplot as plt
from binascii import a2b_base64

#code sourced from https://www.geeksforgeeks.org/opencv-python-tutorial/
# I have made adjustments and edits to fit my needs

# reading image
#cv2.namedWindow("output", cv2.WINDOW_NORMAL)
data="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"
binary_data = a2b_base64(data)
fd = open('image.png', 'wb')
fd.write(binary_data)
fd.close()
img = cv2.imread('image.png')
# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:

	# here we are ignoring first counter because
	# findcontour function detects whole image as shape
	if i == 0:
		i = 1
		continue

	# cv2.approxPloyDP() function to approximate the shape
	approx = cv2.approxPolyDP(
		contour, 0.01 * cv2.arcLength(contour, True), True)
	
	# using drawContours() function
	cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

	# finding center point of shape
	M = cv2.moments(contour)
	if M['m00'] != 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00'])

	# putting shape name at center of each shape
	if len(approx) == 3:
		cv2.putText(img, 'Triangle', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		print('triangle')

	elif len(approx) == 4:
		cv2.putText(img, 'Quadrilateral', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		print('Quadrilateral')

	elif len(approx) == 5:
		cv2.putText(img, 'Pentagon', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		print('Pentagon')

	elif len(approx) == 6:
		cv2.putText(img, 'Hexagon', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		print('Hexagon')

	else:
		cv2.putText(img, 'circle', (x, y),
					cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		print('circle')
        

#!/usr/bin/env python

import cv2
import time
from pylab import *
import warp
import matching
import stitcher

def stitch_horizontal(img1,img2):
	""" Calls functions for stitching horizontally. """

	# Call matches for extracting inliers and homography
	H = matching.matches(img1,img2)
	print '----------'
	#calculate the stitched image size
	h2,w2 = img2.shape[:2]
	tx = H[0,2]
	ty = H[1,2]
	h = int(round(h2 + 100))
	w = int(round(w2*1.6))	
	H = np.matrix([[1,0,tx],[0,1,0],[0,0,1]])
	img2_warped = cv2.warpPerspective(img2,H,(w,h))
	#affine transformation matrix, the picture should align if H is ok
	mat = matrix([[1, 0, 0], [0, 1, 0]], dtype=float)
	im1w = cv2.warpAffine(img1,mat,(w,h))
	im2w = cv2.warpAffine(img2_warped,mat,(w,h))
	# Find a seam between the two images
	A = stitcher.stitch_horizontal(im1w,im2w,w2)

	return A


def stitch_vertical(img1,img2):
	""" Calls functions for stitching horizontally. """

	# Call matches for extracting inliers and homography
	H = matching.matches(img1,img2)
	print '----------'
	#calculate the stitched image size
	h2,w2 = img2.shape[:2]
	tx = H[0,2]
	ty = H[1,2]
	h = int(round(h2 + 100))
	w = int(round(w2*1.6))	
	H = np.matrix([[1,0,tx],[0,1,0],[0,0,1]])
	img2_warped = cv2.warpPerspective(img2,H,(w,h))
	#affine transformation matrix, the picture should align if H is ok
	mat = matrix([[1, 0, 0], [0, 1, 0]], dtype=float)
	im1w = cv2.warpAffine(img1,mat,(w,h))
	im2w = cv2.warpAffine(img2_warped,mat,(w,h))
	# Find a seam between the two images
	A = stitcher.stitch_vertical(im1w,im2w,w2)

	return A


images = ["cam7.png", "cam8.png"]

for i in range(len(images)):
    images[i] = cv2.imread(images[i])

for i in range(0,len(images)):
	while len(images) > 1:
		img1 = images.pop(0)
		img2 = images.pop(0)
		
		im_stitch = stitch_horizontal(img1,img2)
		images.append(im_stitch)	
		
	cv2.imwrite('Stitched.jpg',im_stitch)
	im_stitch = im_stitch[:, :, ::-1]		
	imshow(im_stitch)
	show()	



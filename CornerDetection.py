import numpy as np 
import cv2

cap= cv2.VideoCapture(0)
#fgbg= cv2.createBackgroundSubtractorMOG2()
fgbg= cv2.createBackgroundSubtractorMOG2()
while(1):
	ret, frame= cap.read()
	fgmask= fgbg.apply(frame)
	cv2.imshow('original',frame)
	cv2.imshow('fgbg,', fgmask)

	k= cv2.waitKey(30) & 0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()


	



































# corner detection

# img= cv2.imread('/Users/vijendrasharma/Desktop/opencv-corner-detection-sample.jpg')
# gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray= np.float32(gray)

# corners= cv2.goodFeaturesToTrack(gray,50,0.01, 10)
# # corners= np.int0(corners)

# for c in corners:
# 	x,y= c.ravel()
# 	cv2.circle(img, (x,y), 3, 255, -1)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#feature detection 
# img1= cv2.imread('/Users/vijendrasharma/Desktop/opencv-feature-matching-image.jpg')
# img2= cv2.imread('/Users/vijendrasharma/Desktop/opencv-feature-matching-template.jpg')



# orb= cv2.ORB_create()
# kp1, des1= orb.detectAndCompute(img1, None)
# kp2, des2= orb.detectAndCompute(img2, None)

# bf= cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck= True)
# matches= bf.match(des1, des2)
# matches= sorted(matches, key= lambda x:x.distance)

# img3= cv2.drawMatches(img1,kp1,img2,kp2,matches[:15],None,flags=2)

# cv2.imshow('img', img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


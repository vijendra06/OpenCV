# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_image_links= ' http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02960352 '
    neg_image_links= urllib.request.urlopen(neg_image_links).read().decode()
    picnum= 953
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
    for i in neg_image_links.split('\n'):
        try:
            urllib.request.urlretrieve(i,"neg/"+str(picnum)+".jpg")
            img= cv2.imread("neg/"+str(picnum)+".jpg", cv2.IMREAD_GRAYSCALE)
            resizedimage= cv2.resize(img,(100,100))
            cv2.imwrite("neg/"+str(picnum)+".jpg", resizedimage)
            picnum+=1
            
        except Exception as e:
            print(str(e))
            
            
 store_raw_images()
            
            
            
    
 



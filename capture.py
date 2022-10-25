import os
from picamera2 import Picamera2
import time
import csv
import cv2
import numpy as np

pretime = 0
newFolder = True
folderN = 1
num = 1

cam = Picamera2()
cam.start()

while newFolder:
    if os.path.exists(f"trials/trial{folderN}"):
        folderN += 1
    else:
        os.mkdir(f"trials/trial{folderN}")
        os.mkdir(f"trials/trial{folderN}/images")
        os.mkdir(f"trials/trial{folderN}/annotated")
        newFolder = False

with open(f"trials/trial{folderN}/data.csv",'w') as csvfile:
    fieldnames = ['ID','Time', 'Picture','Fishes']
    filewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    filewriter.writeheader()
    while True:
        if(pretime + 10 <= time.time()):
            pretime = time.time()
            #cam.capture_file(f"trials/trial{folderN}/images/{num}.jpg")
            img = cam.capture_array()
            #contrast part
            #img = cv2.imread(f"trials/trial{folderN}/images/{num}.jpg", 1)
            l = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
            l_c, a, b = cv2.split(l)
            clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
            cl = clahe.apply(l_c)
            limg = cv2.merge((cl,a,b))
            final_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
            cv2.imwrite(f"trials/trial{folderN}/images/{num}.jpg", final_img)
            
            filewriter.writerow({'ID':num,'Time':time.asctime(time.localtime()),'Picture':'contrast_photo.jpg','Fishes':0})
            num += 1
            





        


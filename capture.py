import os
from picamera2 import Picamera2
import time
import csv

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
            cam.capture_file(f"trials/trial{folderN}/images/{num}.jpg")
            filewriter.writerow({'ID':num,'Time':time.asctime(time.localtime()),'Picture':f"trials/trial{folderN}/images/{num}",'Fishes':0})
            num += 1
            





        
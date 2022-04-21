#This code extracts video frames from videos
import os
import cv2

#The source dir contains all the videos
source_dir = './test_source'
target_dir = './test_target'

print(source_dir)

def getFrame(sec, target_path):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(target_path) + '/image_' + str(count) + '.jpg', image)
    return hasFrames

file_names = os.listdir(source_dir)
for file_name in file_names:
    source_path = os.path.join(source_dir, file_name)
    vidcap = cv2.VideoCapture(source_path)
    target_path = os.path.join(target_dir, file_name)
    #Create one target folder for each video
    #-> All images from the same video gets into same folder 
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    print('File:',file_name)
    print('Target_path:', target_path)
    sec = 0
    frameRate = 1.0 #capture image every 1.0 seconds
    count = 1
    success = getFrame(sec, target_path)
    while success:
        count = count +1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, target_path)

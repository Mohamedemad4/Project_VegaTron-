import cv2
import numpy as np

def gen_1to1(video_path,batch_size=100+1,res=(1080, 1920, 3)):
    "split video into Frames "
    vidcap = cv2.VideoCapture(video_path)
    success ,image = vidcap.read()
    count_b=0
    xtempC=0
    B=np.empty((batch_size,res[0],res[1],res[2]),dtype=np.uint8)
    while success:
      success,image = vidcap.read()
      B[count_b]=image 
      count_b+=1
      if batch_size==count_b:
        yield count_b
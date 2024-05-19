import cv2
import numpy as np
from PIL import Image
def save_image(image,addr,num):
  address = addr + str(num)+ '.png'
  cv2.imwrite(address,image)
videoCapture = cv2.VideoCapture("BadApple.flv")
ipt = input('请输入想要的帧率      ')
success, frame = videoCapture.read()
i = 0
timeF = 60 / int(ipt)
j=0
while success :
  i = i + 1
  if (i % timeF == 0):
    j = j + 1
    save_image(frame,'./output/',j)
    print('save image:',i)
  success, frame = videoCapture.read()

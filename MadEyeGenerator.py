import imageio
import numpy
import math
import cv2
import time
from itertools import chain
import os

#===-----------------------------------------------------------------
# Mad Eye Generator
# Olgierd Rogowicz 2022 v1.2
#===-----------------------------------------------------------------

# Reading numbers from frames
class MadEyeGenerator():
  def __init__(self):
    self.eye = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    self.random_numbers = []
  
  def newFrame(self):
    if os.path.exists("last_frame.png"):
      os.remove("last_frame.png")
    time.sleep(0.1)
    check, frame = self.eye.read()
    if check:
      img_name = "last_frame.png"
      cv2.imwrite(img_name, frame)
      
  def generateNumbers(self):
    tempList = []
    tempSublist = []
    
    self.newFrame()
    image = imageio.imread('last_frame.png')
    imgHigth, imgWidth, imgChannel = image.shape
 
    # Loading values from the entire frame into the temp list
    for i in range(imgHigth):
      for j in range(imgWidth):
        for k in range(imgChannel):
          if(image[i][j][k] >= 5 and image[i][j][k] <= 250):
            tempList.append(image[i][j][k] & 0b1)

    # Calculating the size of a square matrix
    square = math.floor(math.sqrt(len(tempList)))

    for i in range(square*square):
      tempSublist.append(tempList[i])

    # Mixing matricesrefd
    tempSublist = numpy.array(tempSublist).reshape(square,square)
    transpose = tempSublist.T
    tempSublist = transpose.tolist()
    tempSublist = list(chain.from_iterable(tempSublist))
  
    tmp = 0
    i = 0
    while(i < len(tempSublist)):
      for j in range(8):
        valTmp = tempSublist[i+j]
        tmp = tmp | (valTmp << j)
      i += 8
      self.random_numbers.append(tmp)
      tmp = 0
      valTmp = 0
      if i+8 > len(tempSublist):
        break

  def getNumbers(self, N):
    while(len(self.random_numbers) < N):
      print("Before gene:",N, len(self.random_numbers))
      self.generateNumbers()
      print("After gene:",N, len(self.random_numbers))
    for i in range(N):
      if i == 0:
        output = bytes([self.random_numbers[0]])
        self.random_numbers.pop(0)
      else:
        output += bytes([self.random_numbers[0]])
        self.random_numbers.pop(0)
    return output
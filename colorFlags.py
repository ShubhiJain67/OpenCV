import cv2

names=[name for name in dir()]
print names

cvNames=[name for name in dir(cv2)]
print len(cvNames)

cvColorNames=[name for name in dir(cv2)if name.startswith("COLOR")]
print len(cvColorNames)

cvCVNames=[name for name in dir(cv2)if name.startswith("CV_")]
print len(cvCVNames)

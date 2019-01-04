import cv2
import numpy as np

image1=cv2.imread("./RefernceImage/image1.jpeg")
image2=cv2.imread("./RefernceImage/image2.jpeg")

difference=cv2.subtract(image1,image2)

# if diff =0 then return false else false
# print image1

# print image2
# print difference
result=not np.any(difference)
print result

if result is True:
	print "No difference"
if result is False:
	cv2.imwrite("./ResultImages/difference.jpeg",difference)
	print "There is difference"
	cv2.waitKey(0) #until ny key is pressed
	
cv2.destroyAllWindows()
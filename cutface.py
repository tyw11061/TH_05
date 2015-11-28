#-*- coding:utf-8 -*-
#画像から一番大きい顔の切り出し
import numpy
import cv2

cascade_path = "./haarcascade/haarcascade_frontalface_alt.xml"
color = (255, 255, 255) #白

image = cv2.imread("./OIX.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascade = cv2.CascadeClassifier(cascade_path)
facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

print(facerect)
print()
face = []
if len(facerect) == 1:
	face=facerect[0]

if len(facerect) > 2:
    max_rect = 0
    for rect in facerect:
        rect_size = rect[2]*rect[3]
        if max_rect <= rect_size:
            max_rect = rect_size
            face=rect
            print(face)

if len(facerect) <= 0:
    exit()
print()
#cv2.rectangle(image, tuple(face[0:2]),tuple(face[0:2]+face[2:4]), color, thickness=2)
#cv2.imshow("result",image)
#cv2.waitKey(0)
#cv2.imwrite("detected.jpg", image)


#cv2.imwrite('demo.jpg', image[rect])
print (face)
if face[0] < 0:
    x = face[0]
else:
    x = face[0]-20
if face[1] < 0:
    y = face[1]
else:
    y = face[1]
w = face[2]
h = face[3]

x -= 10
y -= 10
w += 20
h += 20

# img[y: y + h, x: x + w] 
cv2.imwrite('demo.jpg', image[y:y+h, x:x+w])

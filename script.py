import cv2   #importing a module or libraries or packages or file for opencv
# using method loading the classifier
# load the required trained XML classifiers
detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# capture the image from camera or photos
imp_img=cv2.VideoCapture("mark.jpg")
"""1)read the two variables first one is res is result ,if the image is read put yes else put no////2)second variable 
takes as img is image for img reading pixels"""
res ,img =imp_img.read()
#to convert image into several sizes and colors
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#(GRAY_IMAGE,scale factor(re sizeing image),min Neighbor)
faces=detect.detectMultiScale(gray,1.3,5)
#4 coordinates for using face detection of triangle x,y,w,h
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
cv2.imshow("Elon Image",img)  #To show image
cv2.waitKey(0)           # to show image how much time /// 0 will use to show image untill we close
cv2.destroyAllWindows()

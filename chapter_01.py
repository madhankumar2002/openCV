#openCV form Scratch
#chapter-01
import cv2 # importing opencv-python package
import numpy as np #importing numpy for matrices
print("package installed sucessfully !")

#importing image
img=cv2.imread("resources/elon musk.png") #read image
cv2.imshow("output",img) #display image
cv2.waitKey(0)# used to pause the display of image on screen

#importing video
vid=cv2.VideoCapture(0) # '0' opens webcam
vid.set(3,640) # index-3 for width
vid.set(4,480) # index-4 for height
vid.set(10,500)
while True : # using while loop to display video(as sequence of images)
    success,img=vid.read()
    cv2.imshow("vid output",img)
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break
#converting RGB to GREY scale and blurring :
img=cv2.imread("resources/elon musk.png")
kernel=np.ones((5,5),np.uint8) #kernel matrix with ones with size5

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting RGB to GREY scale
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)#blurring image
imgCanny=cv2.Canny(img,100,100)#to detect edges
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1) #apply a morphological filter to images
imgEroded=cv2.erode(imgDilation,kernel,iterations=1) #erodes boundaries of foreground object

cv2.imshow("Grey img",imgGray)# display grey scale image
cv2.imshow("blur img",imgBlur)# display blur image
cv2.imshow("Canny img",imgCanny)# display edges in image
cv2.imshow("GDilation img",imgDilation)# display diluted edges in image
cv2.imshow("eroded img",imgEroded)# display eroded image
cv2.waitKey(0)# used to pause the display of image on screen

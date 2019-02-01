import numpy as np
import cv2 as cv
area=[]
avarea=[]
kernel = np.ones((5,5),np.uint8)
cap=cv.VideoCapture(1)
ret,im=cap.read()
ex=0
why=0
test=(0,0)
# cv.imshow("size",im)
# cv.waitKey()
# cv.destroyAllWindows()
def coordinates(event,x,y,flags,param):
    if event==cv.EVENT_FLAG_LBUTTON:
        global ex
        global why
        ex=x
        why=y
        print ("x=",x,"y=",y)
u=116
v=87
lower_color = np.array([0,u-30,v-30])
upper_color = np.array([255,u+30,v+30])
while True:

        # Take each frame
        _, frame = cap.read()
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
        mask = cv.inRange(hsv, lower_color, upper_color)
        res = cv.bitwise_and(frame,frame, mask= mask)
        thresh=cv.Canny(res,100,200)
        im3, contours1, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(thresh, contours1, -1 , (0,0,255), 3)
        for i in range(len(contours1)):
                area.append(cv.contourArea(contours1[i]))
        (m,n),radius = cv.minEnclosingCircle(contours1[0])
        center = (int(m),int(n))
        r = int(radius)
        for i in range(len(contours1)):
                #avarea.append(cv.contourArea(contours1[i]))
                (m,n),radius = cv.minEnclosingCircle(contours1[i])
                if radius > r:
                        center = (int(m),int(n))
                        r = int(radius)
                        ind = i
        (m,n),radius= cv.minEnclosingCircle(contours1[ind])
        center=(int(m),int(n))
        if test!=center:
                cv.circle(frame,center,int(radius),(0,255,0),2)
                
        test=center
        cv.imshow("im3",frame)
        cv.setMouseCallback('im3',coordinates)
        if cv.waitKey(5)==27:
                print ("x=",center[0],"y=",center[1])
                print ("x=",round((center[0]-320)*(0.0854)),"y=",round((480-center[1])*(0.0854)))
                #break
        if cv.waitKey(5)==ord('c'):
                break #print ("x=",center[0],"y=",center[1])
                #print ("x=",round((center[0]-320)*(30/357))-4,"y=",round((480-center[1])*(30/357))-9)


# print ("x=",center[0],"y=",center[1])
# print ("x=",round((center[0]-320)*(30/357))-4,"y=",round((480-center[1])*(30/357))-9)
# print ("to"+"\n","x=",ex,"y=",why)
# print ("x=",(ex-320)*(30/357)-4,"y=",(480-why)*(30/357)-9)

        #cv.imshow('frame',frame)
        #cv.imshow('mask',mask)
        #cv.imshow('res',res)
        #if cv.waitKey(30)==27:
        #break
# thresh=cv.Canny(res,100,200)
# im3, contours1, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(thresh, contours1, -1 , (0,0,255), 3)
# for i in range(len(contours1)):
#         area.append(cv.contourArea(contours1[i]))
# (m,n),radius = cv.minEnclosingCircle(contours1[0])
# center = (int(m),int(n))
# r = int(radius)
# for i in range(len(contours1)):
#         avarea.append(cv.contourArea(contours1[i]))
#         (m,n),radius = cv.minEnclosingCircle(contours1[i])
#         if radius > r:
#                 center = (int(m),int(n))
#                 r = int(radius)
#                 ind = i
"""(x,y),radius = cv.minEnclosingCircle(contours1[ind])
center = (int(x),int(y))
radius = int(radius)"""
# cv.circle(im,center,radius,(0,255,0),2)
# print center[0],center[1]
# ret1,im=cap.read()
# (m,n),radius= cv.minEnclosingCircle(contours1[ind])
# center=(int(m),int(n))
# #cv.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
# cv.circle(im,center,int(radius),(0,255,0),2)
# # cv.imshow("im3",im)
# # cv.waitKey()
# print (center)
# print ("x=",center[0]-320)
# print ("y=",480-center[1])
# """rect = cv.minAreaRect(contours[ind])
# box = cv.boxPoints(rect)
# box = np.int0(box)
# print box"""
# #cv.drawContours(img,[box],0,(0,0,255),2)
# while True:
#         _, im = cap.read()
#         cv.circle(im,center,int(radius),(0,255,0),2)
#         cv.imshow("im3",im)
#         cv.setMouseCallback('im3',coordinates)
#         if cv.waitKey(30)==27:
#                 break
# cv.destroyAllWindows()
# print ("x=",center[0],"y=",center[1])
# print ("to"+"\n","x=",ex,"y=",why)
# """
# cv.imshow("ed",thresh)
# k=cv.waitKey()


# maxval=max(area)


# print len(area)
# print ind
# cv.drawContours(im, contours, -1 , (0,0,255), 3)

# print x,y

# cv.imshow("im",im)
# k=cv.waitKey()"""
# """thresh=cv.Canny(thresh,100,200)
# im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# for i in range(len(contours)):
#         area.append(cv.contourArea(contours[i]))
# (x,y),radius = cv.minEnclosingCircle(contours[0])
# center = (int(x),int(y))
# r = int(radius)
# #cv.drawContours(im, contours, -1 , (0,0,255), 3)
# for i in range(len(contours)):
#         avarea.append(cv.contourArea(contours[i]))
#         (x,y),radius = cv.minEnclosingCircle(contours[i])
#         if radius > r:
#                 center = (int(x),int(y))
#                 r = int(radius)
#                 ind = i
# (x,y),radius = cv.minEnclosingCircle(contours[ind])
# center = (int(x),int(y))
# radius = int(radius)
# cv.circle(im,center,radius,(0,255,0),2)
# f=center[0]
# s=center[1]
# color=im[s][f]
# cv.imshow("frame",im)
# if cv.waitKey(30)==27:
#         break"""
#129,116,87​
"""print np.size(im,0),np.size(im,1)
imgray = im #cv.cvtColor(im, cv.COLOR_BGR2GRAY)
imgray = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(imgray, cv.MORPH_CLOSE, kernel)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
imgray = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
thresh=cv.Canny(imgray,100,200)
# blur = cv.GaussianBlur(imgray,(5,5),0)
# ret3,thresh = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("frame",thresh)
cv.waitKey()
cv.destroyAllWindows()
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
        area.append(cv.contourArea(contours[i]))
(x,y),radius = cv.minEnclosingCircle(contours[0])
center = (int(x),int(y))
r = int(radius)
#cv.drawContours(im, contours, -1 , (0,0,255), 3)
for i in range(len(contours)):
        avarea.append(cv.contourArea(contours[i]))
        (x,y),radius = cv.minEnclosingCircle(contours[i])
        if radius > r:
                center = (int(x),int(y))
                r = int(radius)
                ind = i
(x,y),radius = cv.minEnclosingCircle(contours[ind])
center = (int(x),int(y))
radius = int(radius)
#cv.circle(im,center,radius,(0,255,0),2)
f=center[0]
s=center[1]
color=im[s][f]
cv.imshow("frame",im)
cv.destroyAllWindows()
print color
chsv=np.uint8([[color]])
colorhsv=cv.cvtColor(chsv,cv.COLOR_BGR2HSV)
colorhsv=colorhsv[0][0]
print colorhsv"""
